# JavaScript Nâng Cao Part 1 - Tài Liệu Chi Tiết
## Dành cho Sinh Viên Trung Bình - Khá

---

## 📚 Mục Lục
1. [Prototype và Prototype Chain](#1-prototype-và-prototype-chain)
2. [JavaScript Patterns (Các Mẫu Thiết Kế)](#2-javascript-patterns)
3. [Lập Trình Bất Đồng Bộ & Event Loop](#3-lập-trình-bất-đồng-bộ--event-loop)
4. [JavaScript Modules (Mô-đun)](#4-javascript-modules)

---

## 1. Prototype và Prototype Chain

### 🤔 Tư Duy: Tại Sao Cần Prototype?

Hãy tưởng tượng bạn có 1000 objects `person`. Mỗi `person` đều có method `sayHello()`. Nếu mỗi object đều tạo riêng một copy của `sayHello()`, bạn sẽ lãng phí rất nhiều bộ nhớ.

**Giải pháp**: Dùng **Prototype** - tất cả objects có thể "chia sẻ" chung một method!

### 1.1 Prototype Là Gì?

**Định nghĩa đơn giản**:
- Prototype là một object "mẫu" mà các objects khác có thể "học hỏi" (kế thừa)
- Mỗi object trong JavaScript đều có một prototype ẩn

**Ví dụ dễ hiểu**:

```javascript
// Tạo object đơn giản
const animal = {
  eats: true,
  walk() {
    console.log("Động vật đang đi");
  }
};

// Tạo object mới kế thừa từ animal
const rabbit = {
  jumps: true
};

// Thiết lập prototype: rabbit "học" từ animal
rabbit.__proto__ = animal;

// Bây giờ rabbit có thể dùng cả thuộc tính của animal!
console.log(rabbit.jumps); // true (thuộc tính riêng)
console.log(rabbit.eats);  // true (kế thừa từ animal)
rabbit.walk();             // "Động vật đang đi" (kế thừa từ animal)
```

**💡 Lưu Ý Quan Trọng**:
- `__proto__` là cách cũ (không nên dùng trong code thực tế)
- Nên dùng `Object.create()` hoặc class (sẽ học sau)

### 1.2 Prototype Chain (Chuỗi Prototype)

**Tư duy**: Giống như chuỗi thừa kế trong gia đình:
- Con kế thừa từ cha
- Cha kế thừa từ ông
- Ông kế thừa từ tổ tiên...

```javascript
// Ví dụ: Chuỗi kế thừa 3 tầng
const animal = {
  eats: true,
  walk() {
    console.log("Đi bộ");
  }
};

const rabbit = {
  jumps: true,
  __proto__: animal  // rabbit kế thừa animal
};

const longEar = {
  earLength: 10,
  __proto__: rabbit  // longEar kế thừa rabbit
};

// Truy cập thuộc tính - JavaScript tìm kiếm theo chuỗi
console.log(longEar.jumps);      // true (tìm ở rabbit)
console.log(longEar.eats);       // true (tìm ở animal)
console.log(longEar.earLength);  // 10 (thuộc tính riêng)
longEar.walk();                  // "Đi bộ" (tìm ở animal)
```

**🔍 Quy Trình Tìm Kiếm**:

```
Khi gọi longEar.eats:
1. Tìm trong longEar → Không có
2. Tìm trong rabbit (prototype của longEar) → Không có
3. Tìm trong animal (prototype của rabbit) → ✓ Tìm thấy!
4. Trả về true
```

**📌 Bài Tập Tự Luyện 1**:

```javascript
// Hãy dự đoán kết quả
const vehicle = {
  wheels: 4,
  move() {
    return "Di chuyển";
  }
};

const car = {
  brand: "Toyota",
  __proto__: vehicle
};

const sportsCar = {
  speed: 300,
  __proto__: car
};

console.log(sportsCar.brand);   // ?
console.log(sportsCar.wheels);  // ?
console.log(sportsCar.move());  // ?
console.log(sportsCar.speed);   // ?
```

<details>
<summary>👉 Xem Đáp Án</summary>

```javascript
console.log(sportsCar.brand);   // "Toyota" (từ car)
console.log(sportsCar.wheels);  // 4 (từ vehicle)
console.log(sportsCar.move());  // "Di chuyển" (từ vehicle)
console.log(sportsCar.speed);   // 300 (thuộc tính riêng)
```

**Giải thích**: JavaScript tìm kiếm theo chuỗi: sportsCar → car → vehicle
</details>

### 1.3 Constructor Function và Prototype

**Tư duy**: Constructor function như một "cái khuôn" để tạo ra nhiều objects giống nhau.

```javascript
// Constructor function (chữ cái đầu viết hoa theo quy ước)
function Person(name, age) {
  // 'this' trỏ đến object mới được tạo
  this.name = name;
  this.age = age;
}

// Thêm method vào prototype (KHÔNG phải vào từng object)
Person.prototype.sayHello = function() {
  console.log(`Xin chào, tôi là ${this.name}`);
};

Person.prototype.getInfo = function() {
  return `${this.name}, ${this.age} tuổi`;
};

// Tạo objects từ constructor
const person1 = new Person("An", 25);
const person2 = new Person("Bình", 30);

person1.sayHello(); // "Xin chào, tôi là An"
person2.sayHello(); // "Xin chào, tôi là Bình"

// Kiểm tra: cả 2 objects dùng CHUNG 1 function
console.log(person1.sayHello === person2.sayHello); // true ✓
```

**⚠️ Lỗi Thường Gặp**:

```javascript
// ❌ SAI: Thêm method vào constructor (tạo copy mỗi lần)
function PersonBad(name) {
  this.name = name;
  this.sayHello = function() {  // Tạo function mới mỗi lần!
    console.log("Hello");
  };
}

const p1 = new PersonBad("An");
const p2 = new PersonBad("Bình");
console.log(p1.sayHello === p2.sayHello); // false ✗ (2 functions khác nhau, lãng phí!)

// ✅ ĐÚNG: Thêm vào prototype (chia sẻ chung)
function PersonGood(name) {
  this.name = name;
}

PersonGood.prototype.sayHello = function() {
  console.log("Hello");
};

const p3 = new PersonGood("Chi");
const p4 = new PersonGood("Dũng");
console.log(p3.sayHello === p4.sayHello); // true ✓ (cùng 1 function, tiết kiệm!)
```

### 1.4 ES6 Classes - Cú Pháp Hiện Đại

**Tư duy**: Class là cách viết đẹp hơn của constructor function (bên trong vẫn dùng prototype).

```javascript
// Cú pháp class (ES6+) - dễ đọc hơn
class Animal {
  // Constructor chạy khi tạo object mới
  constructor(name) {
    this.name = name;
  }

  // Method tự động được thêm vào prototype
  speak() {
    console.log(`${this.name} đang kêu`);
  }

  eat() {
    console.log(`${this.name} đang ăn`);
  }
}

// Kế thừa với 'extends'
class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Gọi constructor của class cha (BẮT BUỘC!)
    this.breed = breed;
  }

  // Override method của class cha
  speak() {
    console.log(`${this.name} sủa: Gâu gâu!`);
  }

  // Method riêng của Dog
  fetch() {
    console.log(`${this.name} đang đuổi bắt bóng`);
  }
}

const myDog = new Dog("Milu", "Corgi");
myDog.speak();  // "Milu sủa: Gâu gâu!" (method của Dog)
myDog.eat();    // "Milu đang ăn" (kế thừa từ Animal)
myDog.fetch();  // "Milu đang đuổi bắt bóng" (method riêng)
```

**🔑 Các Khái Niệm Quan Trọng**:

1. **`constructor()`**: Hàm khởi tạo, chạy khi tạo object mới
2. **`super()`**: Gọi constructor của class cha (BẮT BUỘC khi dùng extends)
3. **`extends`**: Kế thừa từ class khác
4. **Override**: Ghi đè method của class cha

**📌 Bài Tập Thực Hành 2: Hệ Thống Quản Lý Sinh Viên**

```javascript
// Yêu cầu: Tạo hệ thống quản lý sinh viên với các chức năng:
// 1. Class Person: name, age, introduce()
// 2. Class Student extends Person: studentId, major, grades[], addGrade(), getAverage()
// 3. Tạo 2 sinh viên, thêm điểm, tính điểm trung bình

// TODO: Hãy hoàn thành code dưới đây
```

<details>
<summary>👉 Xem Lời Giải</summary>

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  introduce() {
    console.log(`Tôi là ${this.name}, ${this.age} tuổi`);
  }
}

class Student extends Person {
  constructor(name, age, studentId, major) {
    super(name, age); // Gọi constructor của Person
    this.studentId = studentId;
    this.major = major;
    this.grades = []; // Mảng lưu điểm
  }

  // Thêm điểm môn học
  addGrade(subject, score) {
    this.grades.push({ subject, score });
    console.log(`Đã thêm điểm ${subject}: ${score}`);
  }

  // Tính điểm trung bình
  getAverage() {
    if (this.grades.length === 0) {
      return 0;
    }

    const total = this.grades.reduce((sum, grade) => sum + grade.score, 0);
    return (total / this.grades.length).toFixed(2);
  }

  // Override method introduce
  introduce() {
    super.introduce(); // Gọi method của Person
    console.log(`Mã SV: ${this.studentId}, Ngành: ${this.major}`);
  }
}

// Sử dụng
const student1 = new Student("Nguyễn Văn A", 20, "SV001", "CNTT");
student1.introduce();
// Tôi là Nguyễn Văn A, 20 tuổi
// Mã SV: SV001, Ngành: CNTT

student1.addGrade("JavaScript", 8.5);
student1.addGrade("HTML/CSS", 9.0);
student1.addGrade("ReactJS", 8.0);

console.log(`Điểm TB: ${student1.getAverage()}`); // Điểm TB: 8.50

const student2 = new Student("Trần Thị B", 21, "SV002", "QTKD");
student2.addGrade("Marketing", 7.5);
student2.addGrade("Quản trị", 8.5);
console.log(`Điểm TB: ${student2.getAverage()}`); // Điểm TB: 8.00
```

**Giải thích chi tiết**:
- `super(name, age)`: Gọi constructor của Person để khởi tạo name và age
- `reduce()`: Tính tổng điểm của tất cả môn học
- `toFixed(2)`: Làm tròn đến 2 chữ số thập phân
</details>

---

## 2. JavaScript Patterns

### 🤔 Tư Duy: Tại Sao Cần Design Patterns?

Design Patterns (Mẫu thiết kế) như "công thức nấu ăn" được kiểm chứng:
- Giải quyết các vấn đề phổ biến
- Code dễ đọc, dễ bảo trì
- Tái sử dụng được nhiều lần

### 2.1 Module Pattern - Tạo Code Có Tính Riêng Tư

**Tư duy**: Giống như một cái hộp:
- Bên trong (private): Chỉ hộp biết
- Bên ngoài (public): Người khác có thể dùng

```javascript
const Calculator = (function() {
  // ===== PRIVATE (Chỉ bên trong mới truy cập được) =====
  let result = 0; // Biến private

  function log(message) {
    console.log(`[Calculator] ${message}`);
  }

  // ===== PUBLIC (Công khai ra ngoài) =====
  return {
    add(x) {
      result += x;
      log(`Đã cộng ${x}, kết quả: ${result}`);
      return this; // Cho phép chaining (gọi liên tiếp)
    },

    subtract(x) {
      result -= x;
      log(`Đã trừ ${x}, kết quả: ${result}`);
      return this;
    },

    multiply(x) {
      result *= x;
      log(`Đã nhân ${x}, kết quả: ${result}`);
      return this;
    },

    getResult() {
      return result;
    },

    reset() {
      result = 0;
      log("Đã reset");
      return this;
    }
  };
})();

// Sử dụng - Method Chaining
Calculator.add(5).multiply(2).subtract(3);
// [Calculator] Đã cộng 5, kết quả: 5
// [Calculator] Đã nhân 2, kết quả: 10
// [Calculator] Đã trừ 3, kết quả: 7

console.log(Calculator.getResult()); // 7

// Không thể truy cập biến private
console.log(Calculator.result); // undefined ✗
// console.log(Calculator.log); // undefined ✗
```

**💡 Lợi Ích**:
1. **Encapsulation** (Đóng gói): Ẩn chi tiết bên trong
2. **Security**: Không ai có thể thay đổi `result` trực tiếp từ bên ngoài
3. **Method Chaining**: Gọi nhiều methods liên tiếp

**📌 Bài Tập 3: Tạo Shopping Cart với Module Pattern**

```javascript
// Yêu cầu:
// 1. Private: items[], total
// 2. Public: addItem(name, price, quantity), removeItem(name), getTotal(), getItems(), clear()
// 3. Tự động tính tổng khi thêm/xóa items

// TODO: Hoàn thành code
```

<details>
<summary>👉 Xem Lời Giải</summary>

```javascript
const ShoppingCart = (function() {
  // Private variables
  let items = [];
  let total = 0;

  // Private function
  function calculateTotal() {
    total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  }

  function findItem(name) {
    return items.find(item => item.name === name);
  }

  // Public API
  return {
    addItem(name, price, quantity = 1) {
      const existingItem = findItem(name);

      if (existingItem) {
        existingItem.quantity += quantity;
        console.log(`Đã tăng số lượng ${name}`);
      } else {
        items.push({ name, price, quantity });
        console.log(`Đã thêm ${name} vào giỏ hàng`);
      }

      calculateTotal();
      return this;
    },

    removeItem(name) {
      const index = items.findIndex(item => item.name === name);

      if (index !== -1) {
        items.splice(index, 1);
        console.log(`Đã xóa ${name} khỏi giỏ hàng`);
        calculateTotal();
      } else {
        console.log(`Không tìm thấy ${name}`);
      }

      return this;
    },

    getTotal() {
      return total;
    },

    getItems() {
      return [...items]; // Return copy để bảo vệ data
    },

    clear() {
      items = [];
      total = 0;
      console.log("Đã xóa toàn bộ giỏ hàng");
      return this;
    }
  };
})();

// Sử dụng
ShoppingCart
  .addItem("Laptop", 20000000, 1)
  .addItem("Chuột", 200000, 2)
  .addItem("Bàn phím", 500000, 1);

console.log("Tổng tiền:", ShoppingCart.getTotal().toLocaleString('vi-VN'), "đ");
// Tổng tiền: 20,900,000 đ

console.log("Danh sách:", ShoppingCart.getItems());

ShoppingCart.removeItem("Chuột");
console.log("Tổng tiền sau khi xóa:", ShoppingCart.getTotal().toLocaleString('vi-VN'), "đ");
// Tổng tiền sau khi xóa: 20,500,000 đ
```
</details>

### 2.2 Singleton Pattern - Chỉ Có Một Instance Duy Nhất

**Tư duy**: Giống như chỉ có 1 tổng thống, 1 CEO trong công ty.

**Ứng dụng thực tế**:
- Kết nối Database (chỉ cần 1 kết nối)
- Configuration object (chỉ 1 config cho toàn app)
- Logger (chỉ 1 instance để log)

```javascript
class Database {
  constructor() {
    // Nếu đã có instance, return instance cũ
    if (Database.instance) {
      return Database.instance;
    }

    // Khởi tạo lần đầu
    this.connection = null;
    this.data = [];
    Database.instance = this; // Lưu instance
  }

  connect() {
    if (!this.connection) {
      this.connection = "Đã kết nối DB";
      console.log("✓ Kết nối database thành công");
    } else {
      console.log("✓ Database đã được kết nối rồi");
    }
  }

  insert(record) {
    this.data.push(record);
    console.log("✓ Đã thêm record:", record);
  }

  getAll() {
    return this.data;
  }
}

// Test Singleton
const db1 = new Database();
const db2 = new Database();
const db3 = new Database();

console.log(db1 === db2); // true ✓
console.log(db2 === db3); // true ✓
// Tất cả đều là CÙNG MỘT object!

db1.connect();
db1.insert({ id: 1, name: "User 1" });

// db2 và db3 cũng thấy data này
console.log(db2.getAll()); // [{ id: 1, name: "User 1" }]
console.log(db3.getAll()); // [{ id: 1, name: "User 1" }]
```

Tôi sẽ tiếp tục viết phần còn lại. Bạn muốn tôi hoàn thành tất cả 4 file không?