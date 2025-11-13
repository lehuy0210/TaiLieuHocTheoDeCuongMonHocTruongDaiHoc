# JavaScript Nâng Cao 2 - Tài Liệu Học Tập

## Mục Lục
1. [JavaScript Engine and Runtime](#1-javascript-engine-and-runtime)
2. [Error Handling](#2-error-handling)
3. [Stack Overflow](#3-stack-overflow)
4. [Memory Leaks](#4-memory-leaks)

---

## 1. JavaScript Engine and Runtime

### 1.1 JavaScript Engine là gì?

JavaScript Engine là chương trình thực thi code JavaScript. Mỗi trình duyệt có engine riêng:
- **V8**: Chrome, Node.js, Edge
- **SpiderMonkey**: Firefox
- **JavaScriptCore (Nitro)**: Safari

### 1.2 Các Thành Phần của JavaScript Engine

```
┌─────────────────────────────────────────┐
│         JavaScript Engine (V8)          │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────────┐  ┌─────────────────┐│
│  │   Parser     │→ │   AST           ││
│  │ (Phân tích)  │  │ (Cây cú pháp)   ││
│  └──────────────┘  └─────────────────┘│
│          ↓                              │
│  ┌──────────────────────────────────┐  │
│  │      Interpreter                 │  │
│  │      (Ignition trong V8)         │  │
│  │  → Bytecode                      │  │
│  └──────────────────────────────────┘  │
│          ↓                              │
│  ┌──────────────────────────────────┐  │
│  │   JIT Compiler (TurboFan)        │  │
│  │   → Optimized Machine Code       │  │
│  └──────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

### 1.3 Cách JavaScript Engine Hoạt Động

#### Bước 1: Parsing (Phân Tích)

```javascript
// Code JavaScript
function add(a, b) {
  return a + b;
}

// Engine sẽ parse thành AST (Abstract Syntax Tree)
/*
{
  type: "FunctionDeclaration",
  name: "add",
  params: ["a", "b"],
  body: {
    type: "ReturnStatement",
    value: {
      type: "BinaryExpression",
      operator: "+",
      left: "a",
      right: "b"
    }
  }
}
*/
```

#### Bước 2: Compilation

```javascript
// Just-In-Time (JIT) Compilation

// Code ban đầu
function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

// Lần đầu chạy: Interpreted (chậm)
fibonacci(5);

// Sau nhiều lần gọi: Engine nhận ra "hot function"
// → Compile thành machine code tối ưu (nhanh)
for (let i = 0; i < 10000; i++) {
  fibonacci(10); // Sẽ được optimize
}
```

### 1.4 Execution Context (Ngữ cảnh thực thi)

```javascript
// Execution Context gồm:
// 1. Variable Environment
// 2. Lexical Environment  
// 3. this binding

var globalVar = "Global";

function outer() {
  var outerVar = "Outer";
  
  function inner() {
    var innerVar = "Inner";
    console.log(globalVar);  // Truy cập được
    console.log(outerVar);   // Truy cập được
    console.log(innerVar);   // Truy cập được
  }
  
  inner();
}

outer();

/*
Call Stack khi chạy:

┌─────────────────────┐
│  inner() context    │ ← Current
├─────────────────────┤
│  outer() context    │
├─────────────────────┤
│  Global context     │
└─────────────────────┘
*/
```

### 1.5 Hoisting (Kéo lên)

```javascript
// Hoisting với var
console.log(x); // undefined (không lỗi!)
var x = 5;

// Giải thích: Engine xử lý như sau
var x;           // Declaration được "hoist"
console.log(x);  // undefined
x = 5;          // Assignment ở vị trí ban đầu

// Hoisting với function
sayHello(); // "Hello!" (Hoạt động!)

function sayHello() {
  console.log("Hello!");
}

// let và const KHÔNG bị hoisting như var
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 10;
```

### 1.6 Scope Chain (Chuỗi phạm vi)

```javascript
const global = "Global";

function level1() {
  const l1 = "Level 1";
  
  function level2() {
    const l2 = "Level 2";
    
    function level3() {
      const l3 = "Level 3";
      
      // Tìm kiếm biến theo scope chain
      console.log(l3);     // Tìm ở level3 ✓
      console.log(l2);     // Tìm ở level2 ✓
      console.log(l1);     // Tìm ở level1 ✓
      console.log(global); // Tìm ở global ✓
      // console.log(notExist); // ReferenceError
    }
    
    level3();
  }
  
  level2();
}

level1();

/*
Scope Chain:
level3 scope → level2 scope → level1 scope → global scope
*/
```

### 1.7 Closure (Bao đóng)

```javascript
// Closure cho phép function "nhớ" scope khi nó được tạo

function makeCounter() {
  let count = 0; // Private variable
  
  return function() {
    count++;
    return count;
  };
}

const counter1 = makeCounter();
const counter2 = makeCounter();

console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter1()); // 3

console.log(counter2()); // 1 (counter riêng)
console.log(counter2()); // 2

// Ví dụ thực tế: Private methods
function createBankAccount(initialBalance) {
  let balance = initialBalance; // Private
  
  return {
    deposit(amount) {
      if (amount > 0) {
        balance += amount;
        return `Đã nạp ${amount}. Số dư: ${balance}`;
      }
      return "Số tiền không hợp lệ";
    },
    
    withdraw(amount) {
      if (amount > 0 && amount <= balance) {
        balance -= amount;
        return `Đã rút ${amount}. Số dư: ${balance}`;
      }
      return "Không thể rút tiền";
    },
    
    getBalance() {
      return balance;
    }
  };
}

const myAccount = createBankAccount(1000);
console.log(myAccount.deposit(500));     // Đã nạp 500. Số dư: 1500
console.log(myAccount.withdraw(200));    // Đã rút 200. Số dư: 1300
console.log(myAccount.getBalance());     // 1300
// console.log(myAccount.balance);       // undefined (private!)
```

### 1.8 JavaScript Runtime Environment

```
┌────────────────────────────────────────────────────┐
│              JavaScript Runtime                     │
├────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────────────────┐  ┌──────────────────┐  │
│  │   JavaScript Engine  │  │    Web APIs      │  │
│  │   (V8, SpiderMonkey) │  │  - setTimeout    │  │
│  │                      │  │  - fetch         │  │
│  │   - Call Stack       │  │  - DOM APIs      │  │
│  │   - Memory Heap      │  │  - Console       │  │
│  └──────────────────────┘  └──────────────────┘  │
│            ↕                        ↓              │
│  ┌──────────────────────────────────────────────┐ │
│  │            Callback Queue                    │ │
│  │  [callback1] [callback2] [callback3]        │ │
│  └──────────────────────────────────────────────┘ │
│            ↑                                       │
│  ┌──────────────────────────────────────────────┐ │
│  │            Microtask Queue                   │ │
│  │  [promise1] [promise2]                       │ │
│  └──────────────────────────────────────────────┘ │
│            ↑                                       │
│         Event Loop                                 │
│                                                     │
└────────────────────────────────────────────────────┘
```

### 1.9 Call Stack trong Thực Tế

```javascript
function first() {
  console.log("First function start");
  second();
  console.log("First function end");
}

function second() {
  console.log("Second function start");
  third();
  console.log("Second function end");
}

function third() {
  console.log("Third function");
}

first();

/*
Call Stack Timeline:

Bước 1:                 Bước 2:                 Bước 3:
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│             │         │  second()   │         │   third()   │
│             │         ├─────────────┤         ├─────────────┤
│   first()   │         │   first()   │         │  second()   │
├─────────────┤         ├─────────────┤         ├─────────────┤
│   global    │         │   global    │         │   first()   │
└─────────────┘         └─────────────┘         ├─────────────┤
                                                │   global    │
                                                └─────────────┘

Output:
First function start
Second function start
Third function
Second function end
First function end
*/
```

### 1.10 Memory Heap

```javascript
// Primitive types → Stack
let age = 25;
let name = "John";
let isActive = true;

// Objects, Arrays, Functions → Heap
let user = {
  name: "John",
  age: 25,
  address: {
    city: "Hanoi"
  }
};

let numbers = [1, 2, 3, 4, 5];

/*
Memory Layout:

Stack:                  Heap:
┌──────────────┐       ┌──────────────────────┐
│ age: 25      │       │ Object {             │ ← user trỏ đến
│ name: "John" │       │   name: "John",      │
│ isActive: true│      │   age: 25,           │
│ user: 0x001  │───────→  address: 0x002     │
│ numbers: 0x003─┐     │ }                    │
└──────────────┘ │     ├──────────────────────┤
                 │     │ Object {             │ ← address trỏ đến
                 │     │   city: "Hanoi"      │
                 │     │ }                    │
                 │     ├──────────────────────┤
                 └────→│ Array [1,2,3,4,5]    │ ← numbers trỏ đến
                       └──────────────────────┘
*/
```

### 1.11 Garbage Collection

```javascript
// JavaScript tự động giải phóng memory không còn sử dụng

function createUser() {
  let user = {
    name: "Temp User",
    data: new Array(1000000)
  };
  
  return user.name;
  // Object 'user' sẽ bị garbage collected sau khi function return
}

let name = createUser();
// Bây giờ object user không còn reference → GC sẽ xóa

// Mark and Sweep Algorithm
let obj1 = { data: "some data" };
let obj2 = obj1; // 2 references

obj1 = null; // 1 reference còn lại
obj2 = null; // 0 references → có thể GC

// Cycle reference (GC hiện đại xử lý được)
function createCycle() {
  let a = {};
  let b = {};
  
  a.ref = b;
  b.ref = a; // Circular reference
  
  return "Done";
}

createCycle();
// a và b không còn reference từ bên ngoài → GC sẽ xóa
```

---

## 2. Error Handling

### 2.1 Các Loại Error trong JavaScript

```javascript
// 1. SyntaxError - Lỗi cú pháp
// console.log("Hello"  // Missing closing parenthesis

// 2. ReferenceError - Biến không tồn tại
// console.log(nonExistentVariable);

// 3. TypeError - Sai kiểu dữ liệu
// const num = 5;
// num.toUpperCase(); // TypeError: num.toUpperCase is not a function

// 4. RangeError - Giá trị ngoài phạm vi
function recursiveError(x) {
  return recursiveError(x); // Stack overflow
}
// recursiveError(1);

// 5. URIError - Lỗi encode/decode URI
// decodeURIComponent('%'); // URIError: URI malformed

// 6. EvalError - Lỗi với eval() (hiếm gặp)
```

### 2.2 Try-Catch-Finally

```javascript
// Cấu trúc cơ bản
try {
  // Code có thể gây lỗi
  const result = riskyOperation();
  console.log(result);
} catch (error) {
  // Xử lý lỗi
  console.error("Đã xảy ra lỗi:", error.message);
} finally {
  // Luôn chạy, dù có lỗi hay không
  console.log("Cleanup code here");
}

// Ví dụ thực tế
function parseJSON(jsonString) {
  try {
    const data = JSON.parse(jsonString);
    console.log("Parse thành công:", data);
    return data;
  } catch (error) {
    console.error("Lỗi parse JSON:", error.message);
    return null;
  } finally {
    console.log("Hoàn thành xử lý JSON");
  }
}

parseJSON('{"name": "John"}'); // Thành công
parseJSON('{invalid json}');    // Lỗi nhưng không crash
```

### 2.3 Throw Custom Errors

```javascript
// Throw error đơn giản
function divide(a, b) {
  if (b === 0) {
    throw new Error("Không thể chia cho 0");
  }
  return a / b;
}

try {
  console.log(divide(10, 2)); // 5
  console.log(divide(10, 0)); // Throw error
} catch (error) {
  console.error("Lỗi:", error.message);
}

// Throw với các loại Error khác nhau
function validateAge(age) {
  if (typeof age !== 'number') {
    throw new TypeError("Tuổi phải là số");
  }
  
  if (age < 0 || age > 150) {
    throw new RangeError("Tuổi không hợp lệ (0-150)");
  }
  
  return true;
}

try {
  validateAge("25");  // TypeError
} catch (error) {
  console.error(`${error.name}: ${error.message}`);
}

try {
  validateAge(200);   // RangeError
} catch (error) {
  console.error(`${error.name}: ${error.message}`);
}
```

### 2.4 Custom Error Classes

```javascript
// Tạo Error class riêng
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
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

class AuthenticationError extends Error {
  constructor(message) {
    super(message);
    this.name = "AuthenticationError";
    this.statusCode = 401;
  }
}

// Sử dụng
function validateUser(user) {
  if (!user.email) {
    throw new ValidationError("Email là bắt buộc");
  }
  
  if (!user.email.includes('@')) {
    throw new ValidationError("Email không hợp lệ");
  }
  
  return true;
}

function loginUser(username, password) {
  if (username !== "admin" || password !== "password") {
    throw new AuthenticationError("Sai tên đăng nhập hoặc mật khẩu");
  }
  
  return { username, token: "abc123" };
}

// Xử lý nhiều loại error
try {
  validateUser({ name: "John" });
} catch (error) {
  if (error instanceof ValidationError) {
    console.error("Lỗi validation:", error.message);
  } else if (error instanceof AuthenticationError) {
    console.error("Lỗi xác thực:", error.message);
    // Redirect to login page
  } else {
    console.error("Lỗi không xác định:", error);
  }
}
```

### 2.5 Error Handling với Async/Await

```javascript
// Async function với try-catch
async function fetchUserData(userId) {
  try {
    const response = await fetch(`https://api.example.com/users/${userId}`);
    
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
    
  } catch (error) {
    console.error("Lỗi khi fetch user:", error.message);
    throw error; // Re-throw để caller xử lý
  }
}

// Sử dụng
async function main() {
  try {
    const user = await fetchUserData(1);
    console.log("User:", user);
  } catch (error) {
    console.error("Không thể lấy dữ liệu user");
  }
}

// Multiple async operations
async function loadDashboard() {
  try {
    const [user, posts, comments] = await Promise.all([
      fetchUserData(1),
      fetchPosts(1),
      fetchComments(1)
    ]);
    
    return { user, posts, comments };
    
  } catch (error) {
    console.error("Lỗi khi load dashboard:", error);
    return null;
  }
}
```

### 2.6 Error Boundaries Pattern

```javascript
// Wrapper function để bắt lỗi
function withErrorHandling(fn) {
  return async function(...args) {
    try {
      return await fn(...args);
    } catch (error) {
      console.error(`Error in ${fn.name}:`, error.message);
      // Log to error tracking service (Sentry, LogRocket, etc.)
      logErrorToService(error);
      return null;
    }
  };
}

// Sử dụng
const safeFunction = withErrorHandling(async function riskyFunction(x) {
  if (x < 0) {
    throw new Error("Số âm không được phép");
  }
  return x * 2;
});

await safeFunction(5);   // 10
await safeFunction(-1);  // null (error được handle)

// Error logging service
function logErrorToService(error) {
  const errorLog = {
    message: error.message,
    stack: error.stack,
    timestamp: new Date().toISOString(),
    userAgent: navigator.userAgent,
    url: window.location.href
  };
  
  console.log("Logging error:", errorLog);
  // Send to server: fetch('/api/errors', { method: 'POST', body: JSON.stringify(errorLog) })
}
```

### 2.7 Best Practices

```javascript
// ✅ Good: Specific error messages
function processPayment(amount) {
  if (typeof amount !== 'number') {
    throw new TypeError('Amount phải là number, nhận được: ' + typeof amount);
  }
  
  if (amount <= 0) {
    throw new RangeError('Amount phải lớn hơn 0');
  }
  
  if (amount > 1000000) {
    throw new Error('Amount vượt quá giới hạn cho phép (1,000,000)');
  }
  
  return { success: true, amount };
}

// ❌ Bad: Generic error messages
function processPaymentBad(amount) {
  if (!amount || amount <= 0 || amount > 1000000) {
    throw new Error('Invalid amount'); // Không rõ lỗi gì
  }
  return { success: true, amount };
}

// ✅ Good: Early return với validation
function createUser(userData) {
  if (!userData) {
    throw new ValidationError("User data is required");
  }
  
  if (!userData.email) {
    throw new ValidationError("Email is required");
  }
  
  if (!userData.password || userData.password.length < 8) {
    throw new ValidationError("Password must be at least 8 characters");
  }
  
  // Process user creation
  return { id: 1, ...userData };
}

// ✅ Good: Error context
class APIError extends Error {
  constructor(message, statusCode, endpoint) {
    super(message);
    this.name = "APIError";
    this.statusCode = statusCode;
    this.endpoint = endpoint;
    this.timestamp = new Date();
  }
  
  toJSON() {
    return {
      name: this.name,
      message: this.message,
      statusCode: this.statusCode,
      endpoint: this.endpoint,
      timestamp: this.timestamp
    };
  }
}

async function callAPI(endpoint) {
  const response = await fetch(endpoint);
  
  if (!response.ok) {
    throw new APIError(
      "API call failed",
      response.status,
      endpoint
    );
  }
  
  return response.json();
}
```

---

## 3. Stack Overflow

### 3.1 Stack Overflow là gì?

Stack Overflow xảy ra khi Call Stack bị đầy (quá nhiều function calls lồng nhau).

```javascript
// Ví dụ gây Stack Overflow
function infiniteRecursion() {
  infiniteRecursion(); // Gọi chính nó mãi mãi
}

// infiniteRecursion(); // RangeError: Maximum call stack size exceeded

/*
Call Stack khi bị overflow:

┌──────────────────┐
│ infiniteRecursion│ ← Level 10000+
├──────────────────┤
│ infiniteRecursion│ ← Level 9999
├──────────────────┤
│ infiniteRecursion│ ← Level 9998
├──────────────────┤
│      ...         │
├──────────────────┤
│ infiniteRecursion│ ← Level 2
├──────────────────┤
│ infiniteRecursion│ ← Level 1
├──────────────────┤
│     global       │
└──────────────────┘
    ↓ OVERFLOW! 💥
*/
```

### 3.2 Nguyên Nhân Gây Stack Overflow

```javascript
// 1. Đệ quy không có điều kiện dừng
function factorial(n) {
  return n * factorial(n - 1); // Không có base case!
}
// factorial(5); // Stack overflow

// 2. Đệ quy với base case sai
function countDown(n) {
  console.log(n);
  if (n > 0) { // Sai: không bao giờ <= 0 nếu n âm
    countDown(n - 1);
  }
}
// countDown(-5); // Stack overflow

// 3. Mutual recursion (đệ quy chéo)
function isEven(n) {
  if (n === 0) return true;
  return isOdd(n - 1);
}

function isOdd(n) {
  if (n === 0) return false;
  return isEven(n - 1);
}

// isEven(100000); // Stack overflow với số lớn
```

### 3.3 Đệ Quy Đúng Cách

```javascript
// ✅ Good: Có base case rõ ràng
function factorial(n) {
  // Base case
  if (n <= 1) {
    return 1;
  }
  
  // Recursive case
  return n * factorial(n - 1);
}

console.log(factorial(5)); // 120

// ✅ Good: Fibonacci với base cases
function fibonacci(n) {
  // Base cases
  if (n === 0) return 0;
  if (n === 1) return 1;
  
  // Recursive case
  return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(10)); // 55

// ✅ Good: Tính tổng mảng
function sumArray(arr, index = 0) {
  // Base case: hết mảng
  if (index >= arr.length) {
    return 0;
  }
  
  // Recursive case
  return arr[index] + sumArray(arr, index + 1);
}

console.log(sumArray([1, 2, 3, 4, 5])); // 15
```

### 3.4 Giải Pháp: Iteration thay vì Recursion

```javascript
// Recursion (có thể bị stack overflow)
function sumRecursive(n) {
  if (n <= 0) return 0;
  return n + sumRecursive(n - 1);
}

// Iteration (an toàn hơn)
function sumIterative(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}

console.log(sumIterative(100000)); // Hoạt động tốt

// Fibonacci iteration
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

console.log(fibonacciIterative(50)); // Nhanh và không bị overflow
```

### 3.5 Tail Call Optimization (TCO)

```javascript
// Non-tail recursive (không optimize được)
function factorialNormal(n) {
  if (n <= 1) return 1;
  return n * factorialNormal(n - 1); // Phải nhân sau khi return
}

// Tail recursive (có thể optimize)
function factorialTail(n, accumulator = 1) {
  if (n <= 1) return accumulator;
  return factorialTail(n - 1, n * accumulator); // Return ngay
}

console.log(factorialTail(5)); // 120

// Lưu ý: TCO chỉ được hỗ trợ trong strict mode và một số engines

// Sum với tail recursion
function sumTail(n, accumulator = 0) {
  if (n <= 0) return accumulator;
  return sumTail(n - 1, accumulator + n);
}

console.log(sumTail(10000)); // An toàn hơn
```

### 3.6 Trampoline Pattern

```javascript
// Trampoline giúp tránh stack overflow với recursion
function trampoline(fn) {
  return function(...args) {
    let result = fn(...args);
    
    while (typeof result === 'function') {
      result = result();
    }
    
    return result;
  };
}

// Sử dụng trampoline
function sumTrampoline(n, accumulator = 0) {
  if (n <= 0) {
    return accumulator;
  }
  
  return () => sumTrampoline(n - 1, accumulator + n);
}

const sum = trampoline(sumTrampoline);
console.log(sum(100000)); // Không bị stack overflow!

// Fibonacci với trampoline
function fibTrampoline(n, a = 0, b = 1) {
  if (n === 0) return a;
  if (n === 1) return b;
  
  return () => fibTrampoline(n - 1, b, a + b);
}

const fib = trampoline(fibTrampoline);
console.log(fib(10)); // 55
```

### 3.7 Memoization (Tối ưu đệ quy)

```javascript
// Không có memoization - chậm với số lớn
function fibonacciSlow(n) {
  if (n <= 1) return n;
  return fibonacciSlow(n - 1) + fibonacciSlow(n - 2);
}

// Có memoization - nhanh hơn nhiều
function fibonacciMemo() {
  const cache = {};
  
  return function fib(n) {
    if (n <= 1) return n;
    
    if (cache[n]) {
      return cache[n];
    }
    
    cache[n] = fib(n - 1) + fib(n - 2);
    return cache[n];
  };
}

const fibonacci = fibonacciMemo();

console.time('fib40');
console.log(fibonacci(40)); // 102334155
console.timeEnd('fib40'); // ~1ms

// Generic memoization wrapper
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

console.log(factorial(100)); // Tính nhanh
console.log(factorial(100)); // Lấy từ cache
```

### 3.8 Debugging Stack Overflow

```javascript
// Thêm logging để debug
function debugRecursion(n, depth = 0) {
  console.log(`${'  '.repeat(depth)}Calling with n=${n}, depth=${depth}`);
  
  if (depth > 100) {
    console.error("Too deep! Possible stack overflow");
    return;
  }
  
  if (n <= 1) {
    console.log(`${'  '.repeat(depth)}Base case reached`);
    return 1;
  }
  
  return n * debugRecursion(n - 1, depth + 1);
}

// debugRecursion(5);

// Đếm số lần gọi
let callCount = 0;
const MAX_CALLS = 10000;

function safeRecursion(n) {
  callCount++;
  
  if (callCount > MAX_CALLS) {
    throw new Error(`Exceeded max calls (${MAX_CALLS}). Possible infinite recursion.`);
  }
  
  if (n <= 1) {
    callCount = 0; // Reset
    return 1;
  }
  
  return n * safeRecursion(n - 1);
}

try {
  console.log(safeRecursion(5));
} catch (error) {
  console.error(error.message);
}
```

---

## 4. Memory Leaks

### 4.1 Memory Leak là gì?

Memory Leak xảy ra khi ứng dụng giữ memory mà không còn cần thiết, dẫn đến hết memory.

```javascript
// Ví dụ memory leak đơn giản
let theThing = null;

function replaceThing() {
  let leak = theThing;
  let unused = function() {
    if (leak) {
      console.log("message");
    }
  };
  
  theThing = {
    longStr: new Array(1000000).join('*'),
    someMethod: function() {
      console.log("something");
    }
  };
}

// Mỗi lần gọi, memory tăng
setInterval(replaceThing, 1000); // Memory leak!
```

### 4.2 Các Nguyên Nhân Phổ Biến

#### 4.2.1 Global Variables

```javascript
// ❌ Bad: Global variables không được giải phóng
function createData() {
  // Quên var/let/const → tạo global variable
  leakyData = new Array(1000000).fill('data');
}

createData();
// leakyData tồn tại mãi mãi trong global scope

// ✅ Good: Sử dụng local variables
function createDataSafe() {
  let data = new Array(1000000).fill('data');
  // data sẽ được GC sau khi function kết thúc
}

createDataSafe();
```

#### 4.2.2 Forgotten Timers

```javascript
// ❌ Bad: Timer không được clear
function startTimer() {
  let counter = 0;
  const data = new Array(1000000).fill('data');
  
  setInterval(() => {
    counter++;
    console.log(counter, data.length);
  }, 1000);
  
  // Timer và data sẽ tồn tại mãi mãi!
}

// ✅ Good: Clear timer khi không cần
function startTimerSafe() {
  let counter = 0;
  const data = new Array(1000000).fill('data');
  
  const timerId = setInterval(() => {
    counter++;
    console.log(counter, data.length);
    
    if (counter >= 10) {
      clearInterval(timerId); // Dọn dẹp!
    }
  }, 1000);
  
  return timerId; // Để caller có thể clear nếu cần
}

// Clear timer từ bên ngoài
const timerId = startTimerSafe();
// Sau đó: clearInterval(timerId);
```

#### 4.2.3 Event Listeners Không Được Remove

```javascript
// ❌ Bad: Event listeners không được remove
function attachBadListener() {
  const bigData = new Array(1000000).fill('data');
  
  document.getElementById('button').addEventListener('click', function() {
    console.log(bigData.length);
  });
  
  // bigData bị giữ lại bởi listener!
}

// ✅ Good: Remove listener khi không cần
function attachGoodListener() {
  const bigData = new Array(1000000).fill('data');
  const button = document.getElementById('button');
  
  const handleClick = function() {
    console.log(bigData.length);
  };
  
  button.addEventListener('click', handleClick);
  
  // Cleanup function
  return function cleanup() {
    button.removeEventListener('click', handleClick);
  };
}

const cleanup = attachGoodListener();
// Khi không cần: cleanup();

// ✅ Good: Sử dụng { once: true }
document.getElementById('button').addEventListener('click', function() {
  console.log('Clicked');
}, { once: true }); // Tự động remove sau 1 lần
```

#### 4.2.4 Closures

```javascript
// ❌ Bad: Closure giữ reference không cần thiết
function createClosure() {
  const largeData = new Array(1000000).fill('data');
  const smallData = 'small';
  
  return function() {
    console.log(smallData);
    // largeData không được dùng nhưng vẫn bị giữ lại!
  };
}

const fn = createClosure();
// largeData bị leak

// ✅ Good: Chỉ giữ data cần thiết
function createClosureSafe() {
  const largeData = new Array(1000000).fill('data');
  const smallData = 'small';
  
  // Process largeData nếu cần
  const result = largeData.length;
  
  return function() {
    console.log(smallData, result);
    // Chỉ smallData và result được giữ lại
  };
}
```

#### 4.2.5 DOM References

```javascript
// ❌ Bad: Giữ reference đến removed DOM elements
const elements = [];

function addElement() {
  const div = document.createElement('div');
  div.innerHTML = new Array(1000).join('x');
  document.body.appendChild(div);
  elements.push(div); // Lưu reference
}

function removeElements() {
  document.body.innerHTML = ''; // Remove từ DOM
  // Nhưng elements array vẫn giữ reference → Memory leak!
}

// ✅ Good: Clear references
const elementsSafe = [];

function addElementSafe() {
  const div = document.createElement('div');
  div.innerHTML = new Array(1000).join('x');
  document.body.appendChild(div);
  elementsSafe.push(div);
}

function removeElementsSafe() {
  // Remove từ DOM
  elementsSafe.forEach(el => el.remove());
  
  // Clear references
  elementsSafe.length = 0;
}
```

### 4.3 Detecting Memory Leaks

```javascript
// Monitoring memory usage
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
  }
}

// Test for memory leak
function testForLeak() {
  const initial = performance.memory.usedJSHeapSize;
  
  // Chạy function nhiều lần
  for (let i = 0; i < 1000; i++) {
    suspiciousFunction();
  }
  
  // Force garbage collection (chỉ hoạt động trong Chrome với --expose-gc flag)
  if (global.gc) {
    global.gc();
  }
  
  const final = performance.memory.usedJSHeapSize;
  const leaked = final - initial;
  
  console.log(`Memory leaked: ${(leaked / 1048576).toFixed(2)} MB`);
}
```

### 4.4 Best Practices để Tránh Memory Leaks

```javascript
// 1. Sử dụng WeakMap và WeakSet
// WeakMap không ngăn GC xóa keys
const cache = new WeakMap();

function processObject(obj) {
  if (cache.has(obj)) {
    return cache.get(obj);
  }
  
  const result = expensiveOperation(obj);
  cache.set(obj, result);
  return result;
}

// Khi obj không còn reference khác, nó sẽ được GC
// và entry trong WeakMap cũng tự động bị xóa

// 2. Cleanup trong lifecycle methods
class Component {
  constructor() {
    this.timers = [];
    this.listeners = [];
  }
  
  mount() {
    // Add timer
    const timerId = setInterval(() => {
      this.update();
    }, 1000);
    this.timers.push(timerId);
    
    // Add listener
    const handleClick = () => this.onClick();
    document.addEventListener('click', handleClick);
    this.listeners.push({ element: document, event: 'click', handler: handleClick });
  }
  
  unmount() {
    // Clear timers
    this.timers.forEach(id => clearInterval(id));
    this.timers = [];
    
    // Remove listeners
    this.listeners.forEach(({ element, event, handler }) => {
      element.removeEventListener(event, handler);
    });
    this.listeners = [];
  }
  
  update() {
    console.log('Updating...');
  }
  
  onClick() {
    console.log('Clicked');
  }
}

// 3. Sử dụng AbortController cho fetch
async function fetchWithCleanup(url) {
  const controller = new AbortController();
  
  try {
    const response = await fetch(url, {
      signal: controller.signal
    });
    return await response.json();
  } catch (error) {
    if (error.name === 'AbortError') {
      console.log('Fetch aborted');
    }
    throw error;
  }
}

// Cancel request nếu cần
// controller.abort();

// 4. Nullify references
function processLargeData() {
  let largeArray = new Array(1000000).fill('data');
  
  // Process data
  const result = largeArray.reduce((sum, item) => sum + item.length, 0);
  
  // Clear reference
  largeArray = null;
  
  return result;
}
```

### 4.5 Memory Leak Detection Tools

```javascript
// Chrome DevTools Memory Profiler
// 1. Mở DevTools → Memory tab
// 2. Take Heap Snapshot
// 3. Thực hiện actions
// 4. Take another Heap Snapshot
// 5. Compare để tìm leaks

// Simple leak detector
class LeakDetector {
  constructor() {
    this.snapshots = [];
  }
  
  takeSnapshot(name) {
    if (performance.memory) {
      this.snapshots.push({
        name,
        timestamp: Date.now(),
        memory: performance.memory.usedJSHeapSize
      });
    }
  }
  
  analyze() {
    console.log('\n=== Memory Analysis ===');
    
    for (let i = 1; i < this.snapshots.length; i++) {
      const prev = this.snapshots[i - 1];
      const curr = this.snapshots[i];
      
      const diff = curr.memory - prev.memory;
      const diffMB = (diff / 1048576).toFixed(2);
      
      console.log(`${prev.name} → ${curr.name}: ${diffMB} MB`);
      
      if (diff > 5242880) { // > 5MB
        console.warn('⚠️ Possible memory leak detected!');
      }
    }
  }
  
  reset() {
    this.snapshots = [];
  }
}

// Usage
const detector = new LeakDetector();

detector.takeSnapshot('Initial');

// Run suspicious code
for (let i = 0; i < 1000; i++) {
  createSomething();
}

detector.takeSnapshot('After 1000 iterations');

detector.analyze();
```

### 4.6 Bài Tập Thực Hành

```javascript
// Bài tập: Tìm và fix memory leaks

// Leak 1: Global variable
function leak1() {
  // FIX: Thêm let/const
  data = new Array(1000000);
}

// Leak 2: Timer
function leak2() {
  setInterval(() => {
    const data = new Array(1000000);
    console.log(data.length);
  }, 1000);
  // FIX: Lưu timerId và clear khi không cần
}

// Leak 3: Event listener
function leak3() {
  const button = document.getElementById('btn');
  const data = new Array(1000000);
  
  button.addEventListener('click', () => {
    console.log(data.length);
  });
  // FIX: Remove listener hoặc dùng WeakMap
}

// Leak 4: Closure
function leak4() {
  const large = new Array(1000000);
  
  return function() {
    console.log('Hello');
    // FIX: Không giữ reference đến large
  };
}

// Solution: Safe version
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
      } else if (resource.type === 'listener') {
        resource.element.removeEventListener(resource.event, resource.handler);
      }
    }
    
    this.resources.clear();
    console.log('All resources cleaned up');
  }
}

// Usage
const component = new SafeComponent();
component.addTimer('update', () => console.log('Update'), 1000);
// Later: component.cleanup();
```

---

## Tổng Kết

### Checklist Kiến Thức

- [ ] Hiểu cách JavaScript Engine hoạt động (Parser, Compiler, Execution)
- [ ] Nắm vững Execution Context, Call Stack, và Memory Heap
- [ ] Hiểu về Hoisting, Scope Chain, và Closure
- [ ] Biết cách xử lý errors với try-catch-finally
- [ ] Tạo và sử dụng Custom Error classes
- [ ] Hiểu nguyên nhân và cách tránh Stack Overflow
- [ ] Nắm vững các kỹ thuật tối ưu đệ quy (TCO, Trampoline, Memoization)
- [ ] Nhận biết và sửa Memory Leaks
- [ ] Sử dụng tools để detect memory leaks
- [ ] Apply best practices để tránh memory leaks

### Key Takeaways

1. **JavaScript Engine**: Hiểu cách code được parse, compile, và execute
2. **Error Handling**: Luôn xử lý errors đúng cách, sử dụng custom errors khi cần
3. **Stack Overflow**: Cẩn thận với đệ quy, sử dụng iteration hoặc tối ưu hóa
4. **Memory Leaks**: Luôn cleanup resources (timers, listeners, references)

### Bài Tập Tổng Hợp

Tạo một ứng dụng **Task Manager** với các yêu cầu:

1. **Error Handling**:
   - Validate input với custom errors
   - Handle async errors properly
   - Log errors to console/service

2. **Tránh Stack Overflow**:
   - Implement recursive search trong task tree
   - Optimize với iteration hoặc memoization

3. **Tránh Memory Leaks**:
   - Proper cleanup của timers
   - Remove event listeners khi unmount
   - Clear DOM references

4. **Monitoring**:
   - Track memory usage
   - Detect potential leaks
   - Performance monitoring

### Debug Tips

```javascript
// 1. Chrome DevTools
// - Console: console.log, console.table, console.trace
// - Debugger: debugger; statement
// - Sources: Breakpoints, watch expressions
// - Performance: Record timeline
// - Memory: Heap snapshots

// 2. Logging helper
function log(label, data) {
  console.group(label);
  console.log('Data:', data);
  console.log('Type:', typeof data);
  console.log('Timestamp:', new Date().toISOString());
  console.trace('Stack trace:');
  console.groupEnd();
}

// 3. Performance monitoring
function measurePerformance(fn, label) {
  const start = performance.now();
  const result = fn();
  const end = performance.now();
  
  console.log(`${label}: ${(end - start).toFixed(2)}ms`);
  return result;
}
```

### Tài Liệu Tham Khảo

- **JavaScript Engine**: V8 Documentation, MDN
- **Error Handling**: MDN Error Reference
- **Memory**: Chrome DevTools Memory Profiler
- **Performance**: Web.dev Performance Guides

### Tips Học Tập

1. **Practice debugging**: Dùng DevTools thường xuyên
2. **Profile your code**: Check memory và performance
3. **Read source code**: Học từ libraries lớn
4. **Write tests**: Unit tests giúp catch errors sớm
5. **Monitor production**: Sử dụng error tracking tools

---

**Happy Coding! 🚀**

*Tip: Luôn viết code defensive, xử lý errors properly, và cleanup resources đúng cách!*
