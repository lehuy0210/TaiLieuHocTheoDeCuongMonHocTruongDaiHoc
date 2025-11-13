# JavaScript Nâng Cao Part 2 - Tài Liệu Chi Tiết
## Dành cho Sinh Viên Trung Bình - Khá

---

## 📚 Mục Lục
1. [JavaScript Engine và Runtime](#1-javascript-engine-và-runtime)
2. [Error Handling (Xử Lý Lỗi)](#2-error-handling)
3. [Stack Overflow](#3-stack-overflow)
4. [Memory Leaks (Rò Rỉ Bộ Nhớ)](#4-memory-leaks)

---

## 1. JavaScript Engine và Runtime

### 🤔 Tư Duy: JavaScript "Chạy" Như Thế Nào?

Bạn có bao giờ tự hỏi: Tại sao code JavaScript lại chạy được? Ai đọc code và biến nó thành hành động?

**Câu trả lời**: **JavaScript Engine** - "bộ não" của trình duyệt!

**Ví dụ đời thực**:
- Bạn viết code JavaScript → Như viết công thức nấu ăn
- JavaScript Engine đọc code → Như đầu bếp đọc công thức
- Engine thực thi → Đầu bếp nấu món ăn

### 1.1 JavaScript Engine Là Gì?

**Định nghĩa đơn giản**: JavaScript Engine là chương trình "dịch" và "chạy" code JavaScript.

**Các Engine phổ biến**:

| Trình Duyệt/Platform | Engine Sử Dụng |
|----------------------|----------------|
| Chrome, Edge, Opera  | **V8** |
| Firefox              | **SpiderMonkey** |
| Safari               | **JavaScriptCore (Nitro)** |
| Node.js              | **V8** |

**💡 Điểm Quan Trọng**: Mỗi engine có cách tối ưu riêng, nhưng đều tuân theo chuẩn ECMAScript.

### 1.2 Cách Engine Hoạt Động - 4 Bước Quan Trọng

```
┌─────────────────────────────────────────────────┐
│           QUY TRÌNH XỬ LÝ CODE                  │
└─────────────────────────────────────────────────┘

1️⃣ PARSING (Phân tích cú pháp)
   Code JavaScript → AST (Abstract Syntax Tree)
   ↓
2️⃣ COMPILATION (Biên dịch)
   AST → Bytecode (mã trung gian)
   ↓
3️⃣ EXECUTION (Thực thi)
   Chạy Bytecode
   ↓
4️⃣ OPTIMIZATION (Tối ưu - JIT)
   "Hot code" → Machine code tối ưu
```

**Ví dụ Cụ Thể**:

```javascript
// Code bạn viết:
function greet(name) {
  return "Hello, " + name;
}

// ===== BƯỚC 1: PARSING =====
// Engine phân tích và tạo AST (Abstract Syntax Tree)
/*
{
  type: "FunctionDeclaration",
  name: "greet",
  params: ["name"],
  body: {
    type: "ReturnStatement",
    argument: {
      type: "BinaryExpression",
      operator: "+",
      left: "Hello, ",
      right: "name"
    }
  }
}
*/

// ===== BƯỚC 2: COMPILATION =====
// AST → Bytecode (mã máy ảo)
// (Tương tự Assembly nhưng cho máy ảo JavaScript)

// ===== BƯỚC 3: EXECUTION =====
console.log(greet("An")); // "Hello, An"

// ===== BƯỚC 4: OPTIMIZATION =====
// Nếu gọi greet() nhiều lần, Engine sẽ optimize
for (let i = 0; i < 10000; i++) {
  greet("User" + i);
}
// → Engine nhận ra: "Ah, function này được gọi nhiều!"
// → Compile thành machine code tối ưu → Chạy nhanh hơn!
```

### 1.3 Execution Context - "Ngữ Cảnh Thực Thi"

**Tư duy**: Giống như "phòng làm việc" cho mỗi function.

**Mỗi Execution Context chứa**:
1. **Variable Environment**: Lưu biến (var, let, const)
2. **Lexical Environment**: Scope và outer reference
3. **this binding**: Con trỏ `this`

```javascript
// Global Execution Context
const globalVar = "I'm global";

function outer(x) {
  // Outer Execution Context
  const outerVar = "I'm outer";

  function inner(y) {
    // Inner Execution Context
    const innerVar = "I'm inner";

    console.log(innerVar);  // Tìm ở inner context
    console.log(outerVar);  // Tìm ở outer context
    console.log(globalVar); // Tìm ở global context
    console.log(x, y);      // Tìm parameters
  }

  inner(20);
}

outer(10);

/*
📊 CALL STACK khi chạy:

Bước 1:                    Bước 2:                    Bước 3:
┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
│                 │        │  outer(10)      │        │  inner(20)      │
│                 │        │  - x: 10        │        │  - y: 20        │
│                 │        │  - outerVar     │        │  - innerVar     │
│   Global        │        ├─────────────────┤        ├─────────────────┤
│  - globalVar    │        │   Global        │        │  outer(10)      │
│  - outer        │        │  - globalVar    │        ├─────────────────┤
│                 │        │  - outer        │        │   Global        │
└─────────────────┘        └─────────────────┘        └─────────────────┘

Sau khi inner() kết thúc → Pop ra khỏi stack
Sau khi outer() kết thúc → Pop ra khỏi stack
Chỉ còn Global context
*/
```

**📌 Bài Tập 1: Dự Đoán Kết Quả**

```javascript
function mystery() {
  console.log("1. Start");

  function inner() {
    console.log("2. Inner");
  }

  console.log("3. Before inner");
  inner();
  console.log("4. After inner");
}

mystery();
console.log("5. End");

// Hãy dự đoán thứ tự output!
```

<details>
<summary>👉 Xem Đáp Án</summary>

```
Output:
1. Start
3. Before inner
2. Inner
4. After inner
5. End

Giải thích:
- mystery() được gọi → log "1. Start"
- Gặp function inner nhưng chưa gọi
- Log "3. Before inner"
- Gọi inner() → log "2. Inner"
- inner() kết thúc, quay lại mystery()
- Log "4. After inner"
- mystery() kết thúc
- Log "5. End"
```
</details>

### 1.4 Hoisting - "Kéo Lên Đầu"

**Tư duy**: JavaScript "đọc trước" tất cả declarations (khai báo) trước khi chạy code.

**Hoisting với `var`**:

```javascript
// ===== Code bạn viết =====
console.log(x); // undefined (KHÔNG phải lỗi!)
var x = 5;
console.log(x); // 5

// ===== Engine xử lý như sau =====
var x;              // Declaration được "hoist" lên đầu
console.log(x);     // undefined (đã khai báo nhưng chưa gán)
x = 5;             // Assignment ở vị trí gốc
console.log(x);     // 5
```

**Hoisting với Function**:

```javascript
// ===== Hoạt động tốt! =====
sayHello(); // "Hello!" (Function được hoist)

function sayHello() {
  console.log("Hello!");
}

// ===== Engine xử lý =====
// Function declaration được hoist HOÀN TOÀN (cả body)
function sayHello() {
  console.log("Hello!");
}

sayHello(); // Bây giờ mới gọi
```

**⚠️ `let` và `const` KHÔNG bị hoisting như `var`**:

```javascript
// ❌ LỖI với let/const
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 10;

console.log(z); // ReferenceError: Cannot access 'z' before initialization
const z = 20;

// ✅ ĐÚNG: Khai báo trước khi dùng
let a = 5;
console.log(a); // 5

const b = 10;
console.log(b); // 10
```

**💡 Lý Do**: `let` và `const` có "Temporal Dead Zone" (TDZ) - vùng chết tạm thời từ đầu block đến dòng khai báo.

**📌 Bài Tập 2: Hoisting Challenge**

```javascript
var name = "Global";

function test() {
  console.log(name);
  var name = "Local";
  console.log(name);
}

test();

// Output là gì?
// A) "Global", "Local"
// B) undefined, "Local"
// C) ReferenceError
```

<details>
<summary>👉 Xem Đáp Án</summary>

**Đáp án: B) undefined, "Local"**

```javascript
// Engine xử lý như sau:
var name = "Global";

function test() {
  var name;           // Hoisted lên đầu function
  console.log(name);  // undefined (đã khai báo chưa gán)
  name = "Local";     // Assignment
  console.log(name);  // "Local"
}

test();
```

**Giải thích**: `var name` trong function bị hoist, che mất biến global!
</details>

### 1.5 Scope Chain - "Chuỗi Phạm Vi"

**Tư duy**: Giống như chuỗi "hỏi cha mẹ - ông bà - tổ tiên" khi không tìm thấy thứ mình cần.

```javascript
const level0 = "Global";

function level1() {
  const l1 = "Level 1";

  function level2() {
    const l2 = "Level 2";

    function level3() {
      const l3 = "Level 3";

      // TÌM KIẾM BIẾN - Quy trình:

      console.log(l3);
      // Bước 1: Tìm trong level3 → ✓ Tìm thấy!

      console.log(l2);
      // Bước 1: Tìm trong level3 → ✗ Không có
      // Bước 2: Tìm trong level2 (cha) → ✓ Tìm thấy!

      console.log(l1);
      // Bước 1: Tìm trong level3 → ✗
      // Bước 2: Tìm trong level2 → ✗
      // Bước 3: Tìm trong level1 (ông) → ✓ Tìm thấy!

      console.log(level0);
      // Bước 1: level3 → ✗
      // Bước 2: level2 → ✗
      // Bước 3: level1 → ✗
      // Bước 4: Global → ✓ Tìm thấy!

      // console.log(notExist);
      // Tìm hết scope chain → ReferenceError!
    }

    level3();
  }

  level2();
}

level1();

/*
🔗 SCOPE CHAIN:
level3 scope → level2 scope → level1 scope → global scope → null
*/
```

**Ví Dụ Thực Tế - Module Pattern**:

```javascript
function createCounter() {
  // Private variable - chỉ có trong function scope
  let count = 0;

  // Return public methods
  return {
    increment() {
      count++; // Truy cập count qua scope chain
      console.log(`Count: ${count}`);
    },

    decrement() {
      count--; // Truy cập count qua scope chain
      console.log(`Count: ${count}`);
    },

    getCount() {
      return count; // Truy cập count qua scope chain
    }
  };
}

const counter1 = createCounter();
const counter2 = createCounter();

counter1.increment(); // Count: 1
counter1.increment(); // Count: 2
console.log(counter1.getCount()); // 2

counter2.increment(); // Count: 1
// counter1 và counter2 có scope riêng!

// Không thể truy cập count trực tiếp
console.log(counter1.count); // undefined (private!)
```

### 1.6 Closure - "Bao Đóng" (Khái Niệm Quan Trọng!)

**Tư duy**: Function "nhớ" môi trường nơi nó được tạo ra.

**Định nghĩa**: Closure là function có thể truy cập biến từ outer scope, ngay cả khi outer function đã kết thúc.

```javascript
// ===== VÍ DỤ CƠ BẢN =====
function makeGreeter(greeting) {
  // greeting được "bắt" bởi closure

  return function(name) {
    console.log(`${greeting}, ${name}!`);
  };
}

const sayHello = makeGreeter("Hello");
const sayHi = makeGreeter("Hi");

sayHello("An");   // "Hello, An!"
sayHi("Bình");    // "Hi, Bình!"

// Giải thích:
// - sayHello "nhớ" greeting = "Hello"
// - sayHi "nhớ" greeting = "Hi"
// - Mỗi closure có môi trường riêng!
```

**Ứng Dụng Thực Tế 1: Private Variables**

```javascript
function createBankAccount(initialBalance) {
  // Private variable - không thể truy cập từ bên ngoài
  let balance = initialBalance;
  let transactionHistory = [];

  // Public methods - có thể truy cập balance qua closure
  return {
    deposit(amount) {
      if (amount <= 0) {
        return "Số tiền phải > 0";
      }

      balance += amount;
      transactionHistory.push({
        type: "deposit",
        amount,
        date: new Date()
      });

      return `✓ Nạp ${amount}đ. Số dư: ${balance}đ`;
    },

    withdraw(amount) {
      if (amount <= 0) {
        return "Số tiền phải > 0";
      }

      if (amount > balance) {
        return "Số dư không đủ";
      }

      balance -= amount;
      transactionHistory.push({
        type: "withdraw",
        amount,
        date: new Date()
      });

      return `✓ Rút ${amount}đ. Số dư: ${balance}đ`;
    },

    getBalance() {
      return balance;
    },

    getHistory() {
      return [...transactionHistory]; // Return copy
    }
  };
}

// Sử dụng
const myAccount = createBankAccount(1000);

console.log(myAccount.deposit(500));    // ✓ Nạp 500đ. Số dư: 1500đ
console.log(myAccount.withdraw(300));   // ✓ Rút 300đ. Số dư: 1200đ
console.log(myAccount.getBalance());    // 1200

// Không thể truy cập trực tiếp
console.log(myAccount.balance);         // undefined ✓ (bảo mật!)
console.log(myAccount.transactionHistory); // undefined ✓
```

**⚠️ Lỗi Thường Gặp với Closure trong Loop**

```javascript
// ❌ SAI: Tất cả log ra 3
console.log("Với var:");
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i); // 3, 3, 3
  }, 100);
}

// TẠI SAO?
// - var có function scope (không có block scope)
// - Khi setTimeout chạy (sau 100ms), loop đã kết thúc
// - Lúc đó i = 3 (điều kiện dừng)
// - Cả 3 closures đều "nhìn" cùng 1 biến i = 3

// ✅ GIẢI PHÁP 1: Dùng IIFE tạo scope riêng
console.log("\nVới IIFE:");
for (var i = 0; i < 3; i++) {
  (function(index) {
    setTimeout(function() {
      console.log(index); // 0, 1, 2 ✓
    }, 100);
  })(i); // Pass i vào IIFE
}

// ✅ GIẢI PHÁP 2: Dùng let (block scope)
console.log("\nVới let:");
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i); // 0, 1, 2 ✓
  }, 100);
}
// let tạo scope riêng cho mỗi iteration!
```

**📌 Bài Tập 3: Closure Challenge**

```javascript
function createMultiplier(x) {
  return function(y) {
    return x * y;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

// Hỏi:
console.log(double(5));  // ?
console.log(triple(5));  // ?
console.log(double(10)); // ?
```

<details>
<summary>👉 Xem Đáp Án</summary>

```javascript
console.log(double(5));  // 10 (2 * 5)
console.log(triple(5));  // 15 (3 * 5)
console.log(double(10)); // 20 (2 * 10)

// Giải thích:
// - double "nhớ" x = 2
// - triple "nhớ" x = 3
// - Mỗi closure có biến x riêng!
```
</details>

### 1.7 Memory Heap - "Kho Chứa Dữ Liệu"

**Tư duy**: Memory được chia thành 2 vùng:
- **Stack**: Lưu primitive types và references (nhanh, nhỏ, LIFO)
- **Heap**: Lưu objects, arrays, functions (lớn, linh hoạt)

```javascript
// ===== PRIMITIVE TYPES → STACK =====
let age = 25;           // Lưu trực tiếp trong stack
let name = "John";      // Lưu trực tiếp trong stack
let isActive = true;    // Lưu trực tiếp trong stack

// ===== REFERENCE TYPES → HEAP =====
let person = {          // Object lưu trong heap
  name: "John",
  age: 25,
  address: {
    city: "Hanoi"
  }
};

let numbers = [1, 2, 3, 4, 5]; // Array lưu trong heap

/*
📊 MEMORY LAYOUT:

STACK (Fast, Limited):          HEAP (Slower, Large):
┌──────────────────┐           ┌──────────────────────────┐
│ age: 25          │           │ Object {                 │ ← person
│ name: "John"     │           │   name: "John",          │
│ isActive: true   │           │   age: 25,               │
│ person: 0x001    │───────────→  address: 0x002         │
│ numbers: 0x003   │───┐       │ }                        │
└──────────────────┘   │       ├──────────────────────────┤
                       │       │ Object {                 │ ← address
                       │       │   city: "Hanoi"          │
                       │       │ }                        │
                       │       ├──────────────────────────┤
                       └───────→ Array [1,2,3,4,5]        │ ← numbers
                               └──────────────────────────┘

Stack lưu ADDRESS (0x001, 0x003)
Heap lưu DATA thực sự
*/
```

**⚠️ Reference vs Value - Điểm Quan Trọng**:

```javascript
// === PRIMITIVES: Copy by VALUE ===
let a = 10;
let b = a;    // Copy giá trị
b = 20;       // Thay đổi b không ảnh hưởng a

console.log(a); // 10 ✓
console.log(b); // 20

// === OBJECTS: Copy by REFERENCE ===
let obj1 = { x: 10 };
let obj2 = obj1;  // Copy reference (địa chỉ)
obj2.x = 20;      // Thay đổi qua obj2

console.log(obj1.x); // 20 ✗ (bị ảnh hưởng!)
console.log(obj2.x); // 20
// Vì obj1 và obj2 trỏ đến CÙNG 1 object!

// Để copy độc lập:
let obj3 = { ...obj1 };     // Shallow copy
obj3.x = 30;
console.log(obj1.x); // 20 ✓ (không bị ảnh hưởng)
```

### 1.8 Garbage Collection - "Dọn Dẹp Rác"

**Tư duy**: JavaScript tự động giải phóng memory không còn dùng - bạn không cần lo!

**Mark-and-Sweep Algorithm**:

```javascript
/*
┌─────────────────────────────────────────┐
│      GARBAGE COLLECTION PROCESS         │
└─────────────────────────────────────────┘

PHASE 1: MARK (Đánh dấu)
- Bắt đầu từ ROOTS (global variables, call stack)
- Đi theo tất cả references
- Mark (đánh dấu) objects có thể truy cập được

PHASE 2: SWEEP (Quét dọn)
- Scan toàn bộ heap
- Unmarked objects → Xóa (giải phóng memory)
- Marked objects → Unmark (chuẩn bị cho lần sau)
*/

// Ví dụ:
function createUser() {
  let user = {
    name: "Temp User",
    data: new Array(1000000).fill('x') // 1 triệu phần tử
  };

  return user.name; // Chỉ return primitive
  // Object 'user' không còn reference → GC sẽ xóa
}

let userName = createUser();
// user object đã bị Garbage Collected!

// === Circular References (GC xử lý được!) ===
function createCircular() {
  let a = {};
  let b = {};

  a.ref = b;
  b.ref = a; // Circular reference!

  return "Done";
}

createCircular();
// a và b không reachable từ bên ngoài → GC vẫn xóa được
// (Modern engines thông minh!)
```

**💡 Generational GC - Tối Ưu Hơn**:

```
┌──────────────────────────────────────┐
│      YOUNG GENERATION (New Space)     │
│           ~8MB, GC nhanh ~1-10ms     │
├──────────────────────────────────────┤
│ - Objects mới tạo                    │
│ - 90%+ objects chết sớm              │
│ - GC thường xuyên (Minor GC)         │
└──────────────────────────────────────┘
            ↓ survived multiple GCs
┌──────────────────────────────────────┐
│       OLD GENERATION (Old Space)      │
│       ~1.4GB, GC chậm ~100-1000ms    │
├──────────────────────────────────────┤
│ - Objects sống lâu                   │
│ - GC ít thường xuyên (Major GC)      │
└──────────────────────────────────────┘
```

---

## 2. Error Handling

### 🤔 Tư Duy: Tại Sao Cần Xử Lý Lỗi?

**Vấn đề**: Code không phải lúc nào cũng chạy đúng:
- User nhập sai dữ liệu
- Network timeout
- File không tồn tại
- API trả về lỗi

**Giải pháp**: **Error Handling** - Xử lý lỗi một cách chuyên nghiệp!

### 2.1 Các Loại Error Phổ Biến

```javascript
// ===== 1. SyntaxError - Lỗi cú pháp =====
// console.log("Hello"  // ✗ Thiếu dấu đóng ngoặc
// → SyntaxError: Unexpected end of input

// ===== 2. ReferenceError - Biến không tồn tại =====
// console.log(notDeclared); // ✗
// → ReferenceError: notDeclared is not defined

// ===== 3. TypeError - Sai kiểu dữ liệu =====
const num = 5;
// num.toUpperCase(); // ✗ Number không có method này
// → TypeError: num.toUpperCase is not a function

// ===== 4. RangeError - Giá trị ngoài phạm vi =====
const arr = new Array(-1); // ✗ Length không thể âm
// → RangeError: Invalid array length

// ===== 5. URIError - Lỗi encode/decode URI =====
// decodeURIComponent('%'); // ✗ URI malformed
// → URIError: URI malformed

// ===== 6. Custom Errors - Tự định nghĩa =====
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

throw new ValidationError("Email không hợp lệ");
// → ValidationError: Email không hợp lệ
```

### 2.2 Try-Catch-Finally - Bắt và Xử Lý Lỗi

**Cấu trúc cơ bản**:

```javascript
try {
  // Code có thể gây lỗi
  riskyOperation();

} catch (error) {
  // Xử lý lỗi
  console.error("Đã xảy ra lỗi:", error.message);

} finally {
  // Luôn chạy (dù có lỗi hay không)
  console.log("Cleanup code");
}
```

**Ví Dụ Thực Tế 1: Parse JSON**

```javascript
function parseJSON(jsonString) {
  try {
    const data = JSON.parse(jsonString);
    console.log("✓ Parse thành công:", data);
    return data;

  } catch (error) {
    console.error("✗ Lỗi parse JSON:", error.message);
    return null;

  } finally {
    console.log("→ Hoàn thành xử lý JSON");
  }
}

// Test
parseJSON('{"name": "John", "age": 25}');
// ✓ Parse thành công: {name: "John", age: 25}
// → Hoàn thành xử lý JSON

parseJSON('{invalid json}');
// ✗ Lỗi parse JSON: Unexpected token i in JSON at position 1
// → Hoàn thành xử lý JSON
// Return: null
```

**Ví Dụ Thực Tế 2: Chia Số**

```javascript
function divide(a, b) {
  try {
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new TypeError("Cả 2 số phải là number");
    }

    if (b === 0) {
      throw new Error("Không thể chia cho 0");
    }

    return a / b;

  } catch (error) {
    console.error(`Lỗi: ${error.message}`);
    return null;
  }
}

// Test
console.log(divide(10, 2));     // 5
console.log(divide(10, 0));     // Lỗi: Không thể chia cho 0 → null
console.log(divide("10", 2));   // Lỗi: Cả 2 số phải là number → null
```

### 2.3 Custom Error Classes - Tạo Error Riêng

**Tư duy**: Tạo các loại error cụ thể để dễ xử lý.

```javascript
// ===== Tạo Error Classes =====
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

class AuthenticationError extends Error {
  constructor(message) {
    super(message);
    this.name = "AuthenticationError";
    this.statusCode = 401;
  }
}

class DatabaseError extends Error {
  constructor(message, query) {
    super(message);
    this.name = "DatabaseError";
    this.query = query;
    this.timestamp = new Date();
  }
}

// ===== Sử Dụng =====
function validateUser(user) {
  if (!user.email) {
    throw new ValidationError("Email là bắt buộc", "email");
  }

  if (!user.email.includes('@')) {
    throw new ValidationError("Email không hợp lệ", "email");
  }

  if (!user.password || user.password.length < 8) {
    throw new ValidationError("Mật khẩu phải >= 8 ký tự", "password");
  }

  return true;
}

function loginUser(username, password) {
  if (username !== "admin" || password !== "12345678") {
    throw new AuthenticationError("Sai tên đăng nhập hoặc mật khẩu");
  }

  return { username, token: "abc123" };
}

// ===== Xử Lý Nhiều Loại Error =====
try {
  validateUser({ name: "John" }); // Thiếu email

} catch (error) {
  if (error instanceof ValidationError) {
    console.error(`✗ Validation lỗi [${error.field}]: ${error.message}`);
    // Hiển thị lỗi ở form field cụ thể

  } else if (error instanceof AuthenticationError) {
    console.error(`✗ Xác thực lỗi: ${error.message}`);
    // Redirect to login page

  } else if (error instanceof DatabaseError) {
    console.error(`✗ Database lỗi: ${error.message}`);
    console.error(`Query: ${error.query}`);
    // Log to monitoring service

  } else {
    console.error("✗ Lỗi không xác định:", error);
  }
}

// Output: ✗ Validation lỗi [email]: Email là bắt buộc
```

### 2.4 Error Handling với Async/Await

**Tư duy**: Async code cũng cần xử lý lỗi!

```javascript
// ===== Ví dụ 1: Fetch API =====
async function fetchUser(userId) {
  try {
    const response = await fetch(`https://api.example.com/users/${userId}`);

    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    const data = await response.json();
    console.log("✓ User data:", data);
    return data;

  } catch (error) {
    console.error("✗ Lỗi khi fetch:", error.message);
    throw error; // Re-throw để caller xử lý
  }
}

// Sử dụng
async function main() {
  try {
    const user = await fetchUser(1);
    console.log("Success:", user);

  } catch (error) {
    console.error("Failed to load user");
  }
}

// ===== Ví dụ 2: Multiple Async Operations =====
async function loadDashboard(userId) {
  try {
    // Gọi parallel
    const [user, posts, comments] = await Promise.all([
      fetchUser(userId),
      fetchPosts(userId),
      fetchComments(userId)
    ]);

    return { user, posts, comments };

  } catch (error) {
    console.error("✗ Lỗi load dashboard:", error.message);
    return null;
  }
}
```

**📌 Bài Tập 4: Hệ Thống Đăng Ký User**

```javascript
// Yêu cầu: Tạo hàm registerUser với validation đầy đủ
// Input: { email, password, age }
// Validation:
// - email: required, phải có @
// - password: required, >= 8 ký tự
// - age: required, 13-120
//
// Sử dụng Custom Error classes

// TODO: Hoàn thành code
```

<details>
<summary>👉 Xem Lời Giải</summary>

```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

function registerUser(userData) {
  try {
    // Validate email
    if (!userData.email) {
      throw new ValidationError("Email là bắt buộc", "email");
    }

    if (!userData.email.includes('@')) {
      throw new ValidationError("Email phải chứa @", "email");
    }

    // Validate password
    if (!userData.password) {
      throw new ValidationError("Password là bắt buộc", "password");
    }

    if (userData.password.length < 8) {
      throw new ValidationError("Password phải >= 8 ký tự", "password");
    }

    // Validate age
    if (!userData.age) {
      throw new ValidationError("Tuổi là bắt buộc", "age");
    }

    if (userData.age < 13 || userData.age > 120) {
      throw new ValidationError("Tuổi phải từ 13-120", "age");
    }

    // Success
    console.log("✓ Đăng ký thành công!");
    return {
      id: Date.now(),
      email: userData.email,
      age: userData.age,
      createdAt: new Date()
    };

  } catch (error) {
    if (error instanceof ValidationError) {
      console.error(`✗ Lỗi [${error.field}]: ${error.message}`);
      return { success: false, error: error.message, field: error.field };
    }

    console.error("✗ Lỗi không xác định:", error);
    return { success: false, error: error.message };
  }
}

// Test cases
console.log("\n=== Test 1: Valid ===");
registerUser({ email: "user@example.com", password: "password123", age: 25 });

console.log("\n=== Test 2: Missing email ===");
registerUser({ password: "password123", age: 25 });

console.log("\n=== Test 3: Invalid email ===");
registerUser({ email: "invalid", password: "password123", age: 25 });

console.log("\n=== Test 4: Short password ===");
registerUser({ email: "user@example.com", password: "123", age: 25 });

console.log("\n=== Test 5: Invalid age ===");
registerUser({ email: "user@example.com", password: "password123", age: 150 });
```
</details>

---

## 3. Stack Overflow

### 🤔 Tư Duy: Call Stack Bị "Tràn"

**Vấn đề**: Call Stack có giới hạn (khoảng 10,000-15,000 calls tùy trình duyệt). Nếu vượt quá → **Stack Overflow**!

**Nguyên nhân phổ biến**: Đệ quy không có điều kiện dừng.

### 3.1 Stack Overflow Là Gì?

```javascript
// ===== VÍ DỤ GÂY STACK OVERFLOW =====
function infiniteRecursion() {
  infiniteRecursion(); // Gọi chính nó mãi mãi!
}

// infiniteRecursion();
// → RangeError: Maximum call stack size exceeded

/*
📊 CALL STACK BỊ OVERFLOW:

┌──────────────────┐
│ infiniteRecursion│ ← Level 15000 (Giới hạn!)
├──────────────────┤
│ infiniteRecursion│ ← Level 14999
├──────────────────┤
│ infiniteRecursion│ ← Level 14998
├──────────────────┤
│      ...         │
├──────────────────┤
│ infiniteRecursion│ ← Level 2
├──────────────────┤
│ infiniteRecursion│ ← Level 1
├──────────────────┤
│     global       │
└──────────────────┘
      ↓
   💥 OVERFLOW!
*/
```

### 3.2 Đệ Quy Đúng Cách - Có Base Case

**Quy tắc vàng**: Mọi đệ quy phải có:
1. **Base case**: Điều kiện dừng
2. **Recursive case**: Gọi lại chính nó với input nhỏ hơn

```javascript
// ===== ❌ SAI: Không có base case =====
function factorialWrong(n) {
  return n * factorialWrong(n - 1); // Không bao giờ dừng!
}

// ===== ✅ ĐÚNG: Có base case =====
function factorial(n) {
  // Base case
  if (n <= 1) {
    return 1;
  }

  // Recursive case
  return n * factorial(n - 1);
}

console.log(factorial(5)); // 120
// 5 * factorial(4)
// 5 * 4 * factorial(3)
// 5 * 4 * 3 * factorial(2)
// 5 * 4 * 3 * 2 * factorial(1)
// 5 * 4 * 3 * 2 * 1 = 120

// ===== VÍ DỤ 2: Fibonacci =====
function fibonacci(n) {
  // Base cases
  if (n === 0) return 0;
  if (n === 1) return 1;

  // Recursive case
  return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(6)); // 8
// 0, 1, 1, 2, 3, 5, 8

// ===== VÍ DỤ 3: Sum mảng =====
function sumArray(arr, index = 0) {
  // Base case: Hết mảng
  if (index >= arr.length) {
    return 0;
  }

  // Recursive case
  return arr[index] + sumArray(arr, index + 1);
}

console.log(sumArray([1, 2, 3, 4, 5])); // 15
```

### 3.3 Giải Pháp: Iteration Thay Vì Recursion

**Tư duy**: Loop thường an toàn hơn đệ quy cho số lượng lớn.

```javascript
// ===== RECURSION (Có thể bị stack overflow) =====
function sumRecursive(n) {
  if (n <= 0) return 0;
  return n + sumRecursive(n - 1);
}

console.log(sumRecursive(10));      // 55 ✓
// console.log(sumRecursive(100000)); // Stack overflow! ✗

// ===== ITERATION (An toàn) =====
function sumIterative(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}

console.log(sumIterative(10));      // 55 ✓
console.log(sumIterative(100000));  // 5000050000 ✓ (OK!)

// ===== Fibonacci Iterative =====
function fibonacciIterative(n) {
  if (n <= 1) return n;

  let prev = 0, curr = 1;

  for (let i = 2; i <= n; i++) {
    let next = prev + curr;
    prev = curr;
    curr = next;
  }

  return curr;
}

console.log(fibonacciIterative(50)); // Rất nhanh!
```

### 3.4 Memoization - Tối Ưu Đệ Quy

**Tư duy**: Cache kết quả đã tính để không tính lại.

```javascript
// ===== Không memoization - Chậm =====
function fibSlow(n) {
  if (n <= 1) return n;
  return fibSlow(n - 1) + fibSlow(n - 2);
}

// console.time("fib40");
// console.log(fibSlow(40)); // ~2-3 giây!
// console.timeEnd("fib40");

// ===== Với memoization - Nhanh =====
function fibMemo() {
  const cache = {};

  return function fib(n) {
    if (n <= 1) return n;

    // Check cache trước
    if (cache[n]) {
      return cache[n];
    }

    // Tính và lưu cache
    cache[n] = fib(n - 1) + fib(n - 2);
    return cache[n];
  };
}

const fibonacci = fibMemo();

console.time("fib40");
console.log(fibonacci(40)); // 102334155 (~1ms!)
console.timeEnd("fib40");

// ===== Generic Memoization Wrapper =====
function memoize(fn) {
  const cache = {};

  return function(...args) {
    const key = JSON.stringify(args);

    if (cache[key]) {
      return cache[key];
    }

    const result = fn.apply(this, args);
    cache[key] = result;
    return result;
  };
}

// Sử dụng
const factorial = memoize(function(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
});

console.log(factorial(100)); // Rất nhanh!
console.log(factorial(100)); // Lấy từ cache → Instant!
```

**📌 Bài Tập 5: Tối Ưu Đệ Quy**

```javascript
// Cho function tính tổng các số từ 1 đến n
function slowSum(n) {
  if (n <= 0) return 0;
  return n + slowSum(n - 1);
}

// Yêu cầu:
// 1. Viết phiên bản iteration
// 2. Viết phiên bản memoization
// 3. So sánh performance với n = 10000

// TODO: Hoàn thành code
```

<details>
<summary>👉 Xem Lời Giải</summary>

```javascript
// ===== 1. Phiên bản Iteration =====
function sumIterative(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}

// ===== 2. Phiên bản Memoization =====
function createMemoizedSum() {
  const cache = {};

  return function sumMemo(n) {
    if (n <= 0) return 0;

    if (cache[n]) {
      return cache[n];
    }

    cache[n] = n + sumMemo(n - 1);
    return cache[n];
  };
}

const sumMemoized = createMemoizedSum();

// ===== 3. Performance Test =====
const n = 10000;

console.log("\n=== Performance Comparison ===");

// Test Iterative
console.time("Iterative");
const result1 = sumIterative(n);
console.timeEnd("Iterative");
console.log("Result:", result1);

// Test Memoized
console.time("Memoized");
const result2 = sumMemoized(n);
console.timeEnd("Memoized");
console.log("Result:", result2);

// Test Memoized lần 2 (từ cache)
console.time("Memoized (cached)");
const result3 = sumMemoized(n);
console.timeEnd("Memoized (cached)");
console.log("Result:", result3);

/*
Expected Output:
Iterative: ~0.5ms
Memoized: ~5-10ms (lần đầu)
Memoized (cached): ~0.001ms (rất nhanh!)
*/
```
</details>

---

## 4. Memory Leaks

### 🤔 Tư Duy: Memory Leak Là Gì?

**Định nghĩa**: Memory Leak là khi ứng dụng giữ memory mà không còn cần thiết, dần dần hết memory → App chậm/crash.

**Ví dụ đời thực**:
- Bạn mượn sách từ thư viện nhưng không trả
- Thư viện hết sách để cho mượn
- Người khác không mượn được
→ Memory leak tương tự!

### 4.1 Các Nguyên Nhân Phổ Biến

#### 4.1.1 Global Variables (Biến Toàn Cục)

```javascript
// ===== ❌ SAI: Tạo global variable vô tình =====
function createData() {
  // Quên var/let/const → Tạo global variable!
  leakyData = new Array(1000000).fill('data');
}

createData();
console.log(window.leakyData); // Tồn tại mãi mãi!
// → Memory leak!

// ===== ✅ ĐÚNG: Dùng local variable =====
function createDataSafe() {
  let data = new Array(1000000).fill('data');
  // data sẽ được GC sau khi function kết thúc
}

createDataSafe();
// data đã bị giải phóng ✓
```

#### 4.1.2 Timers Không Được Clear

```javascript
// ===== ❌ SAI: Timer không được clear =====
function startBadTimer() {
  const bigData = new Array(1000000).fill('data');

  setInterval(() => {
    console.log(bigData.length);
  }, 1000);

  // Timer chạy mãi → bigData không bao giờ được GC!
}

// startBadTimer(); // Memory leak!

// ===== ✅ ĐÚNG: Clear timer khi không cần =====
function startGoodTimer() {
  const bigData = new Array(1000000).fill('data');
  let counter = 0;

  const timerId = setInterval(() => {
    counter++;
    console.log(`${counter}: ${bigData.length}`);

    if (counter >= 10) {
      clearInterval(timerId); // Dọn dẹp!
      console.log("Timer đã dừng");
    }
  }, 1000);

  return timerId; // Để caller có thể clear
}

// Sử dụng
const timerId = startGoodTimer();
// Nếu cần dừng sớm: clearInterval(timerId);
```

#### 4.1.3 Event Listeners Không Được Remove

```javascript
// ===== ❌ SAI: Listener không được remove =====
function attachBadListener() {
  const bigData = new Array(1000000).fill('data');

  document.getElementById('btn').addEventListener('click', function() {
    console.log(bigData.length);
  });

  // bigData bị giữ lại bởi listener → Leak!
}

// ===== ✅ ĐÚNG: Remove listener =====
function attachGoodListener() {
  const bigData = new Array(1000000).fill('data');
  const button = document.getElementById('btn');

  const handleClick = function() {
    console.log(bigData.length);
  };

  button.addEventListener('click', handleClick);

  // Return cleanup function
  return function cleanup() {
    button.removeEventListener('click', handleClick);
    console.log("✓ Listener đã được remove");
  };
}

// Sử dụng
const cleanup = attachGoodListener();
// Khi không cần: cleanup();

// ===== ✅ TỐT HƠN: Dùng { once: true } =====
document.getElementById('btn').addEventListener('click', function() {
  console.log('Clicked');
}, { once: true }); // Tự động remove sau 1 lần!
```

#### 4.1.4 Closures Giữ References Không Cần Thiết

```javascript
// ===== ❌ SAI: Closure giữ data không cần thiết =====
function createBadClosure() {
  const largeData = new Array(1000000).fill('data');
  const smallData = 'small';

  return function() {
    console.log(smallData);
    // largeData không được dùng nhưng vẫn bị closure giữ lại!
  };
}

const fn = createBadClosure();
// largeData bị leak! ✗

// ===== ✅ ĐÚNG: Chỉ giữ data cần thiết =====
function createGoodClosure() {
  const largeData = new Array(1000000).fill('data');
  const smallData = 'small';

  // Process largeData nếu cần
  const summary = largeData.length;

  return function() {
    console.log(smallData, summary);
    // Chỉ smallData và summary được giữ lại ✓
  };
}

const fn2 = createGoodClosure();
// largeData đã được GC! ✓
```

#### 4.1.5 DOM References (Detached DOM Nodes)

```javascript
// ===== ❌ SAI: Giữ reference đến removed DOM =====
const elements = [];

function addBadElement() {
  const div = document.createElement('div');
  div.innerHTML = new Array(1000).join('x');
  document.body.appendChild(div);
  elements.push(div); // Lưu reference
}

function removeBadElements() {
  document.body.innerHTML = ''; // Remove từ DOM
  // Nhưng elements array vẫn giữ reference → Leak!
}

// ===== ✅ ĐÚNG: Clear references =====
const elementsSafe = [];

function addGoodElement() {
  const div = document.createElement('div');
  div.innerHTML = new Array(1000).join('x');
  document.body.appendChild(div);
  elementsSafe.push(div);
}

function removeGoodElements() {
  // Remove từ DOM
  elementsSafe.forEach(el => el.remove());

  // Clear references
  elementsSafe.length = 0;
  console.log("✓ DOM elements và references đã clear");
}
```

### 4.2 Detecting Memory Leaks - Phát Hiện Rò Rỉ

```javascript
// ===== Monitor Memory Usage =====
function checkMemory() {
  if (performance.memory) {
    const used = performance.memory.usedJSHeapSize;
    const total = performance.memory.totalJSHeapSize;
    const limit = performance.memory.jsHeapSizeLimit;

    console.log({
      used: `${(used / 1048576).toFixed(2)} MB`,
      total: `${(total / 1048576).toFixed(2)} MB`,
      limit: `${(limit / 1048576).toFixed(2)} MB`,
      percentage: `${((used / limit) * 100).toFixed(2)}%`
    });
  } else {
    console.log("⚠️ performance.memory không available");
  }
}

// Monitor mỗi 5 giây
setInterval(checkMemory, 5000);

// ===== Leak Detector Class =====
class LeakDetector {
  constructor() {
    this.snapshots = [];
  }

  takeSnapshot(label) {
    if (performance.memory) {
      this.snapshots.push({
        label,
        timestamp: Date.now(),
        memory: performance.memory.usedJSHeapSize
      });
      console.log(`📸 Snapshot "${label}" taken`);
    }
  }

  analyze() {
    console.log('\n=== 📊 Memory Leak Analysis ===\n');

    for (let i = 1; i < this.snapshots.length; i++) {
      const prev = this.snapshots[i - 1];
      const curr = this.snapshots[i];

      const diff = curr.memory - prev.memory;
      const diffMB = (diff / 1048576).toFixed(2);
      const timeDiff = curr.timestamp - prev.timestamp;

      console.log(`${prev.label} → ${curr.label}:`);
      console.log(`  Memory change: ${diffMB} MB`);
      console.log(`  Time: ${timeDiff}ms`);

      if (diff > 10485760) { // > 10MB
        console.warn('  ⚠️ Potential memory leak detected!');
      }
      console.log('');
    }
  }

  reset() {
    this.snapshots = [];
    console.log("✓ Snapshots reset");
  }
}

// ===== Sử dụng =====
const detector = new LeakDetector();

detector.takeSnapshot('Initial');

// Chạy suspicious code
for (let i = 0; i < 1000; i++) {
  // suspiciousFunction();
}

detector.takeSnapshot('After 1000 iterations');

// Force GC nếu available (Chrome với --expose-gc flag)
if (global.gc) {
  global.gc();
  detector.takeSnapshot('After GC');
}

detector.analyze();
```

### 4.3 Best Practices - Tránh Memory Leaks

**1. Sử Dụng WeakMap và WeakSet**

```javascript
// ===== WeakMap không ngăn GC xóa keys =====
const cache = new WeakMap();

function processObject(obj) {
  // Check cache
  if (cache.has(obj)) {
    return cache.get(obj);
  }

  // Expensive operation
  const result = obj.data + " processed";
  cache.set(obj, result);
  return result;
}

// Sử dụng
let myObj = { data: "important" };
console.log(processObject(myObj)); // "important processed"

// Khi myObj không còn reference khác
myObj = null;
// → Entry trong WeakMap tự động bị xóa! ✓

// ===== So sánh với Map thông thường =====
const regularCache = new Map();

function processWithMap(obj) {
  if (regularCache.has(obj)) {
    return regularCache.get(obj);
  }

  const result = obj.data + " processed";
  regularCache.set(obj, result);
  return result;
}

let myObj2 = { data: "important" };
processWithMap(myObj2);

myObj2 = null;
// Entry trong Map VẪN tồn tại → Memory leak! ✗
// Phải manual xóa: regularCache.delete(myObj2);
```

**2. Cleanup trong Component Lifecycle**

```javascript
class Component {
  constructor() {
    this.timers = [];
    this.listeners = [];
  }

  mount() {
    console.log("✓ Component mounted");

    // Add timer
    const timerId = setInterval(() => {
      this.update();
    }, 1000);
    this.timers.push(timerId);

    // Add listeners
    const handleClick = () => this.onClick();
    const handleResize = () => this.onResize();

    document.addEventListener('click', handleClick);
    window.addEventListener('resize', handleResize);

    this.listeners.push(
      { element: document, event: 'click', handler: handleClick },
      { element: window, event: 'resize', handler: handleResize }
    );
  }

  unmount() {
    console.log("✓ Component unmounted - Cleaning up...");

    // Clear all timers
    this.timers.forEach(id => clearInterval(id));
    this.timers = [];

    // Remove all listeners
    this.listeners.forEach(({ element, event, handler }) => {
      element.removeEventListener(event, handler);
    });
    this.listeners = [];

    console.log("✓ Cleanup complete");
  }

  update() {
    console.log("Component updating...");
  }

  onClick() {
    console.log("Clicked");
  }

  onResize() {
    console.log("Resized");
  }
}

// Sử dụng
const myComponent = new Component();
myComponent.mount();

// Sau 10 giây, unmount
setTimeout(() => {
  myComponent.unmount();
}, 10000);
```

**3. AbortController cho Fetch**

```javascript
class DataFetcher {
  constructor() {
    this.controller = new AbortController();
  }

  async fetchData(url) {
    try {
      const response = await fetch(url, {
        signal: this.controller.signal
      });

      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status}`);
      }

      const data = await response.json();
      console.log("✓ Data fetched:", data);
      return data;

    } catch (error) {
      if (error.name === 'AbortError') {
        console.log("✓ Fetch was cancelled");
      } else {
        console.error("✗ Fetch error:", error.message);
      }
      return null;
    }
  }

  cancel() {
    this.controller.abort();
    console.log("✓ Fetch request cancelled");
  }
}

// Sử dụng
const fetcher = new DataFetcher();
fetcher.fetchData('https://api.example.com/data');

// Cancel nếu cần (ví dụ: user navigate away)
setTimeout(() => {
  fetcher.cancel();
}, 1000);
```

**4. Nullify Large Objects**

```javascript
function processLargeData() {
  let largeArray = new Array(1000000).fill({
    data: 'x'.repeat(1000)
  });

  console.log("Processing large data...");

  // Process data
  const result = {
    count: largeArray.length,
    firstItem: largeArray[0],
    lastItem: largeArray[largeArray.length - 1]
  };

  // Nullify để help GC
  largeArray = null;
  console.log("✓ Large array nullified");

  return result;
}

const summary = processLargeData();
console.log("Summary:", summary);
// largeArray đã được GC! ✓
```

### 4.4 Chrome DevTools - Memory Profiler

```
┌─────────────────────────────────────────────┐
│     CHROME DEVTOOLS MEMORY PROFILING        │
├─────────────────────────────────────────────┤
│                                             │
│  1. Mở DevTools → Memory tab                │
│                                             │
│  2. Take Heap Snapshot (Chụp ảnh memory)    │
│     → Thấy tất cả objects trong memory      │
│                                             │
│  3. Thực hiện actions (tạo/xóa objects)     │
│                                             │
│  4. Take another Heap Snapshot              │
│                                             │
│  5. Compare 2 snapshots                     │
│     → Xem objects nào tăng                  │
│     → Tìm "Detached DOM tree"               │
│     → Check unexpected retained objects     │
│                                             │
│  6. Analyze:                                │
│     - Summary view: Grouped by constructor  │
│     - Comparison view: Show differences     │
│     - Containment view: Show object tree    │
│     - Statistics view: Pie chart            │
│                                             │
└─────────────────────────────────────────────┘
```

**📌 Bài Tập 6: Fix Memory Leaks**

```javascript
// Code dưới đây có 4 memory leaks. Hãy tìm và fix!

// Leak 1: Global variable
function leak1() {
  data = new Array(1000000); // Missing let/const
}

// Leak 2: Timer
function leak2() {
  const bigData = new Array(1000000);
  setInterval(() => {
    console.log(bigData.length);
  }, 1000); // Never cleared!
}

// Leak 3: Event listener
function leak3() {
  const button = document.getElementById('btn');
  const bigData = new Array(1000000);

  button.addEventListener('click', () => {
    console.log(bigData.length);
  }); // Never removed!
}

// Leak 4: Closure
function leak4() {
  const huge = new Array(1000000);

  return function() {
    console.log('Hello');
    // huge is captured but never used!
  };
}

// TODO: Fix all 4 leaks!
```

<details>
<summary>👉 Xem Lời Giải</summary>

```javascript
// ===== FIXED VERSION =====

// Fix 1: Add let/const
function noLeak1() {
  let data = new Array(1000000); // ✓ Local variable
}

// Fix 2: Clear timer
function noLeak2() {
  const bigData = new Array(1000000);
  let counter = 0;

  const timerId = setInterval(() => {
    counter++;
    console.log(bigData.length);

    if (counter >= 10) {
      clearInterval(timerId); // ✓ Clear timer
    }
  }, 1000);

  return timerId; // Let caller clear if needed
}

// Fix 3: Remove event listener
function noLeak3() {
  const button = document.getElementById('btn');
  const bigData = new Array(1000000);

  const handleClick = () => {
    console.log(bigData.length);
  };

  button.addEventListener('click', handleClick);

  // ✓ Return cleanup function
  return function cleanup() {
    button.removeEventListener('click', handleClick);
  };
}

// Fix 4: Don't capture unused variables
function noLeak4() {
  const huge = new Array(1000000);

  // Process huge if needed
  const summary = huge.length;

  return function() {
    console.log('Hello', summary);
    // ✓ Only summary is captured, not huge array
  };
}

// ===== Better: Safe Component Pattern =====
class SafeComponent {
  constructor() {
    this.resources = new Map();
  }

  addTimer(name, callback, interval) {
    const id = setInterval(callback, interval);
    this.resources.set(name, { type: 'timer', id });
  }

  addListener(name, element, event, handler) {
    element.addEventListener(event, handler);
    this.resources.set(name, { type: 'listener', element, event, handler });
  }

  cleanup() {
    for (const [name, resource] of this.resources) {
      if (resource.type === 'timer') {
        clearInterval(resource.id);
        console.log(`✓ Timer "${name}" cleared`);
      } else if (resource.type === 'listener') {
        resource.element.removeEventListener(resource.event, resource.handler);
        console.log(`✓ Listener "${name}" removed`);
      }
    }

    this.resources.clear();
    console.log("✓ All resources cleaned up");
  }
}

// Usage
const component = new SafeComponent();
component.addTimer('update', () => console.log('Update'), 1000);
component.addListener('click', document, 'click', () => console.log('Clicked'));

// Later: component.cleanup();
```
</details>

---

## 📚 Tổng Kết Part 2

### ✅ Kiến Thức Đã Học

**1. JavaScript Engine & Runtime**
- Cách Engine hoạt động: Parse → Compile → Execute → Optimize
- Execution Context, Call Stack, Memory Heap
- Hoisting (var, function, let/const)
- Scope Chain & Closure (quan trọng!)
- Garbage Collection (Mark-and-Sweep, Generational GC)

**2. Error Handling**
- Các loại Error phổ biến (SyntaxError, TypeError, RangeError, etc.)
- Try-Catch-Finally
- Custom Error classes
- Error handling với Async/Await

**3. Stack Overflow**
- Nguyên nhân: Đệ quy không có base case
- Giải pháp: Iteration, Memoization
- Tail call optimization (TCO)

**4. Memory Leaks**
- 5 nguyên nhân phổ biến (global vars, timers, listeners, closures, DOM refs)
- Detecting leaks với Chrome DevTools
- Best practices: WeakMap, cleanup, AbortController, nullify

### 📝 Checklist Ôn Tập

- [ ] Giải thích được cách JavaScript Engine hoạt động
- [ ] Hiểu Execution Context và Call Stack
- [ ] Phân biệt Hoisting của var vs let/const
- [ ] Hiểu và áp dụng được Closure
- [ ] Xử lý errors với try-catch
- [ ] Tạo Custom Error classes
- [ ] Tránh Stack Overflow với đệ quy
- [ ] Áp dụng Memoization để tối ưu
- [ ] Nhận biết và fix Memory Leaks
- [ ] Sử dụng Chrome DevTools Memory Profiler

### 🎯 Bài Tập Tổng Hợp

**Tạo Ứng Dụng Task Manager với đầy đủ features:**

1. **Error Handling**:
   - Validate input với custom errors
   - Handle async errors đúng cách
   - Log errors ra console/service

2. **Tránh Stack Overflow**:
   - Implement recursive search trong task tree
   - Optimize với iteration hoặc memoization

3. **Tránh Memory Leaks**:
   - Cleanup timers đúng cách
   - Remove event listeners khi unmount
   - Clear DOM references
   - Use WeakMap cho cache

4. **Monitoring**:
   - Track memory usage
   - Detect potential leaks
   - Performance monitoring

### 💡 Tips Quan Trọng

```javascript
// 1. Always cleanup resources
class MyComponent {
  mount() { /* add listeners, timers */ }
  unmount() { /* MUST cleanup! */ }
}

// 2. Use WeakMap for metadata
const metadata = new WeakMap(); // Auto GC!

// 3. Nullify large objects
let bigData = createBigData();
const summary = process(bigData);
bigData = null; // Help GC

// 4. Use AbortController
const controller = new AbortController();
fetch(url, { signal: controller.signal });
// Later: controller.abort();

// 5. Monitor memory in development
if (process.env.NODE_ENV === 'development') {
  setInterval(checkMemory, 5000);
}
```

### 🔍 Debug Tips

**Chrome DevTools Shortcuts**:
- `Ctrl+Shift+J`: Mở Console
- `F12 → Memory`: Memory Profiler
- `F12 → Performance`: Record timeline
- `debugger;`: Breakpoint trong code
- `console.trace()`: Show call stack

**Node.js Flags**:
```bash
# Expose GC
node --expose-gc script.js

# Trace optimization
node --trace-opt script.js

# Trace deoptimization
node --trace-deopt script.js
```

---

**🎉 Hoàn Thành Part 2! 🚀**

*"Hiểu cách JavaScript hoạt động bên trong sẽ giúp bạn viết code tốt hơn!"*

**→ Chuyển sang Part 3 để học về IIFE, call/apply/bind, và JIT Compiler!**