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

### 2.3 Observer Pattern - Theo Dõi Và Thông Báo

**Tư duy**: Giống như đăng ký nhận tin từ báo:
- Bạn đăng ký (subscribe) nhận tin từ báo
- Khi có tin mới, báo gửi (notify) cho tất cả người đăng ký
- Bạn có thể hủy đăng ký (unsubscribe) bất kỳ lúc nào

**Ứng dụng thực tế**:
- Event handling (click, submit, etc.)
- Notification system
- State management (Redux, MobX)
- Real-time updates

```javascript
// Subject (Chủ thể) - Người gửi thông báo
class NewsAgency {
  constructor() {
    this.subscribers = []; // Danh sách người đăng ký
  }

  // Đăng ký nhận tin
  subscribe(observer) {
    this.subscribers.push(observer);
    console.log(`✓ ${observer.name} đã đăng ký nhận tin`);
  }

  // Hủy đăng ký
  unsubscribe(observer) {
    this.subscribers = this.subscribers.filter(sub => sub !== observer);
    console.log(`✗ ${observer.name} đã hủy đăng ký`);
  }

  // Gửi thông báo cho tất cả subscribers
  notify(news) {
    console.log(`\n📰 TIN MỚI: ${news}\n`);
    this.subscribers.forEach(subscriber => {
      subscriber.update(news);
    });
  }
}

// Observer (Người quan sát) - Người nhận thông báo
class Subscriber {
  constructor(name) {
    this.name = name;
  }

  // Nhận thông báo
  update(news) {
    console.log(`→ ${this.name} đã đọc: "${news}"`);
  }
}

// === Sử dụng ===
const vnexpress = new NewsAgency();

const reader1 = new Subscriber("Nguyễn Văn A");
const reader2 = new Subscriber("Trần Thị B");
const reader3 = new Subscriber("Lê Văn C");

// Đăng ký
vnexpress.subscribe(reader1);
vnexpress.subscribe(reader2);
vnexpress.subscribe(reader3);

// Gửi tin
vnexpress.notify("Việt Nam vô địch SEA Games!");
// 📰 TIN MỚI: Việt Nam vô địch SEA Games!
// → Nguyễn Văn A đã đọc: "Việt Nam vô địch SEA Games!"
// → Trần Thị B đã đọc: "Việt Nam vô địch SEA Games!"
// → Lê Văn C đã đọc: "Việt Nam vô địch SEA Games!"

// Hủy đăng ký
vnexpress.unsubscribe(reader2);

// Gửi tin mới
vnexpress.notify("Giá vàng tăng cao kỷ lục");
// 📰 TIN MỚI: Giá vàng tăng cao kỷ lục
// → Nguyễn Văn A đã đọc: "Giá vàng tăng cao kỷ lục"
// → Lê Văn C đã đọc: "Giá vàng tăng cao kỷ lục"
// (Trần Thị B không nhận được vì đã hủy)
```

**📌 Bài Tập 4: Hệ Thống Thông Báo Đơn Hàng**

```javascript
// Yêu cầu: Tạo hệ thống thông báo khi có đơn hàng mới
// 1. Class OrderSystem (Subject): subscribe(), unsubscribe(), notify()
// 2. Class Customer (Observer): update() - nhận thông báo
// 3. Class ShippingCompany (Observer): update() - chuẩn bị giao hàng
// 4. Class WarehouseManager (Observer): update() - đóng gói hàng

// TODO: Hoàn thành code
```

<details>
<summary>👉 Xem Lời Giải</summary>

```javascript
class OrderSystem {
  constructor() {
    this.observers = [];
  }

  subscribe(observer) {
    this.observers.push(observer);
  }

  unsubscribe(observer) {
    this.observers = this.observers.filter(obs => obs !== observer);
  }

  // Tạo đơn hàng mới
  createOrder(orderInfo) {
    console.log(`\n🛒 ĐỚN HÀNG MỚI #${orderInfo.id}`);
    console.log(`Sản phẩm: ${orderInfo.product}`);
    console.log(`Khách hàng: ${orderInfo.customerName}\n`);

    this.notify(orderInfo);
  }

  notify(orderInfo) {
    this.observers.forEach(observer => {
      observer.update(orderInfo);
    });
  }
}

class Customer {
  constructor(name) {
    this.name = name;
  }

  update(orderInfo) {
    console.log(`✓ [Khách hàng ${this.name}] Đã nhận xác nhận đơn hàng #${orderInfo.id}`);
  }
}

class ShippingCompany {
  constructor(name) {
    this.name = name;
  }

  update(orderInfo) {
    console.log(`✓ [${this.name}] Chuẩn bị giao hàng đến ${orderInfo.address}`);
  }
}

class WarehouseManager {
  update(orderInfo) {
    console.log(`✓ [Kho hàng] Bắt đầu đóng gói ${orderInfo.product}`);
  }
}

// Sử dụng
const orderSystem = new OrderSystem();

const customer = new Customer("Nguyễn Văn A");
const shipper = new ShippingCompany("Giao Hàng Nhanh");
const warehouse = new WarehouseManager();

orderSystem.subscribe(customer);
orderSystem.subscribe(shipper);
orderSystem.subscribe(warehouse);

// Tạo đơn hàng
orderSystem.createOrder({
  id: "DH001",
  product: "iPhone 15 Pro Max",
  customerName: "Nguyễn Văn A",
  address: "123 Nguyễn Huệ, Q1, TP.HCM"
});

// 🛒 ĐỚN HÀNG MỚI #DH001
// Sản phẩm: iPhone 15 Pro Max
// Khách hàng: Nguyễn Văn A
//
// ✓ [Khách hàng Nguyễn Văn A] Đã nhận xác nhận đơn hàng #DH001
// ✓ [Giao Hàng Nhanh] Chuẩn bị giao hàng đến 123 Nguyễn Huệ, Q1, TP.HCM
// ✓ [Kho hàng] Bắt đầu đóng gói iPhone 15 Pro Max
```
</details>

### 2.4 Factory Pattern - Nhà Máy Tạo Objects

**Tư duy**: Giống như nhà máy sản xuất:
- Bạn đặt hàng "Tôi muốn xe hơi màu đỏ"
- Nhà máy tạo ra xe hơi theo yêu cầu
- Bạn không cần biết cách làm xe

**Ứng dụng thực tế**:
- Tạo nhiều loại objects khác nhau nhưng có interface giống nhau
- Game development (tạo enemies, items, characters)
- UI components (buttons, inputs, modals)

```javascript
// Các classes cơ bản
class Laptop {
  constructor(brand, ram, storage) {
    this.type = "Laptop";
    this.brand = brand;
    this.ram = ram;
    this.storage = storage;
  }

  getInfo() {
    return `${this.type} ${this.brand}: RAM ${this.ram}GB, SSD ${this.storage}GB`;
  }
}

class Phone {
  constructor(brand, camera, battery) {
    this.type = "Phone";
    this.brand = brand;
    this.camera = camera;
    this.battery = battery;
  }

  getInfo() {
    return `${this.type} ${this.brand}: Camera ${this.camera}MP, Pin ${this.battery}mAh`;
  }
}

class Tablet {
  constructor(brand, screenSize, stylus) {
    this.type = "Tablet";
    this.brand = brand;
    this.screenSize = screenSize;
    this.stylus = stylus;
  }

  getInfo() {
    return `${this.type} ${this.brand}: Màn hình ${this.screenSize}", ${this.stylus ? 'Có' : 'Không có'} bút`;
  }
}

// Factory - Nhà máy tạo sản phẩm
class ElectronicsFactory {
  createProduct(type, specs) {
    switch(type) {
      case "laptop":
        return new Laptop(specs.brand, specs.ram, specs.storage);

      case "phone":
        return new Phone(specs.brand, specs.camera, specs.battery);

      case "tablet":
        return new Tablet(specs.brand, specs.screenSize, specs.stylus);

      default:
        throw new Error(`Không hỗ trợ loại sản phẩm: ${type}`);
    }
  }
}

// === Sử dụng ===
const factory = new ElectronicsFactory();

// Tạo laptop
const laptop = factory.createProduct("laptop", {
  brand: "Dell",
  ram: 16,
  storage: 512
});
console.log(laptop.getInfo());
// Laptop Dell: RAM 16GB, SSD 512GB

// Tạo phone
const phone = factory.createProduct("phone", {
  brand: "iPhone 15",
  camera: 48,
  battery: 4000
});
console.log(phone.getInfo());
// Phone iPhone 15: Camera 48MP, Pin 4000mAh

// Tạo tablet
const tablet = factory.createProduct("tablet", {
  brand: "iPad Pro",
  screenSize: 12.9,
  stylus: true
});
console.log(tablet.getInfo());
// Tablet iPad Pro: Màn hình 12.9", Có bút
```

**💡 Lợi Ích Factory Pattern**:
1. **Đơn giản hóa**: Không cần biết cách tạo từng loại object
2. **Dễ mở rộng**: Thêm loại mới chỉ cần thêm vào factory
3. **Tập trung**: Logic tạo object ở một chỗ

---

## 3. Lập Trình Bất Đồng Bộ & Event Loop

### 🤔 Tư Duy: Tại Sao Cần Lập Trình Bất Đồng Bộ?

**Ví dụ thực tế**:
Bạn vào quán cà phê:
- ❌ **Đồng bộ (Synchronous)**: Đứng chờ barista pha xong cà phê mới được đặt món tiếp theo → Chậm!
- ✅ **Bất đồng bộ (Asynchronous)**: Gọi món xong, ngồi chờ, barista làm xong sẽ gọi → Hiệu quả!

**Trong lập trình**:
- Gọi API lấy dữ liệu: mất 2-3 giây
- Nếu chờ đến khi xong mới chạy tiếp → App bị "đơ"
- Giải pháp: Chạy tiếp code khác, khi API xong sẽ xử lý

### 3.1 Callback Functions - Hàm Gọi Lại

**Định nghĩa**: Callback là function được truyền vào function khác để "gọi lại" sau.

```javascript
// === Ví dụ 1: Callback đơn giản ===
function sayHello(name, callback) {
  console.log(`Xin chào ${name}!`);
  callback(); // Gọi function được truyền vào
}

function sayGoodbye() {
  console.log("Tạm biệt!");
}

sayHello("An", sayGoodbye);
// Xin chào An!
// Tạm biệt!

// === Ví dụ 2: Callback với setTimeout ===
console.log("1. Bắt đầu");

setTimeout(function() {
  console.log("2. Sau 2 giây");
}, 2000);

console.log("3. Kết thúc");

// Output:
// 1. Bắt đầu
// 3. Kết thúc
// (đợi 2 giây)
// 2. Sau 2 giây
```

**🔍 Giải Thích**:
1. Log "1. Bắt đầu"
2. `setTimeout` đặt callback vào hàng đợi, chờ 2 giây
3. Chương trình chạy tiếp, log "3. Kết thúc"
4. Sau 2 giây, callback chạy, log "2. Sau 2 giây"

**⚠️ Vấn Đề: Callback Hell (Địa ngục callback)**

```javascript
// Callback lồng nhau nhiều tầng → Khó đọc, khó maintain
getUserData(userId, function(user) {
  getOrders(user.id, function(orders) {
    getOrderDetails(orders[0].id, function(details) {
      getPaymentInfo(details.paymentId, function(payment) {
        console.log(payment);
        // 😱 Callback Hell!
      });
    });
  });
});
```

### 3.2 Promises - Lời Hứa

**Tư duy**: Promise như "giấy hứa" trong đời sống:
- Bạn đặt hàng online → Nhận "giấy hứa" sẽ giao hàng
- Kết quả có thể:
  - ✅ **Fulfilled**: Giao hàng thành công
  - ❌ **Rejected**: Giao hàng thất bại
  - ⏳ **Pending**: Đang trên đường giao

```javascript
// === Tạo Promise ===
function fetchUser(userId) {
  return new Promise((resolve, reject) => {
    console.log(`Đang tải user ${userId}...`);

    setTimeout(() => {
      if (userId > 0) {
        // Thành công
        resolve({
          id: userId,
          name: `User ${userId}`,
          email: `user${userId}@example.com`
        });
      } else {
        // Thất bại
        reject(new Error("User ID không hợp lệ"));
      }
    }, 1500);
  });
}

// === Sử dụng Promise ===
fetchUser(1)
  .then(user => {
    console.log("✓ Thành công:", user);
    // Có thể return promise khác để chain
    return fetchUser(2);
  })
  .then(user2 => {
    console.log("✓ User 2:", user2);
  })
  .catch(error => {
    console.error("✗ Lỗi:", error.message);
  })
  .finally(() => {
    console.log("✓ Hoàn tất (dù thành công hay thất bại)");
  });

// Output:
// Đang tải user 1...
// (đợi 1.5s)
// ✓ Thành công: {id: 1, name: "User 1", email: "user1@example.com"}
// Đang tải user 2...
// (đợi 1.5s)
// ✓ User 2: {id: 2, name: "User 2", email: "user2@example.com"}
// ✓ Hoàn tất
```

**🔑 Các Methods Quan Trọng**:
- `.then()`: Xử lý khi thành công
- `.catch()`: Xử lý khi lỗi
- `.finally()`: Chạy dù thành công hay lỗi

**💡 Promise.all() - Chờ Tất Cả**

```javascript
// Gọi nhiều APIs cùng lúc
const promise1 = fetchUser(1);
const promise2 = fetchUser(2);
const promise3 = fetchUser(3);

Promise.all([promise1, promise2, promise3])
  .then(results => {
    console.log("Tất cả users:", results);
    // [user1, user2, user3]
  })
  .catch(error => {
    console.error("Có ít nhất 1 lỗi:", error);
  });
```

### 3.3 Async/Await - Cú Pháp Hiện Đại

**Tư duy**: Làm code bất đồng bộ trông giống code đồng bộ → Dễ đọc!

```javascript
// === Cách cũ với Promise ===
function getUserWithPromise(userId) {
  fetchUser(userId)
    .then(user => {
      console.log("User:", user);
      return fetchOrders(user.id);
    })
    .then(orders => {
      console.log("Orders:", orders);
    })
    .catch(error => {
      console.error("Lỗi:", error);
    });
}

// === Cách mới với Async/Await ===
async function getUserWithAsync(userId) {
  try {
    // 'await' chờ promise hoàn thành
    const user = await fetchUser(userId);
    console.log("User:", user);

    const orders = await fetchOrders(user.id);
    console.log("Orders:", orders);

    return { user, orders };
  } catch (error) {
    console.error("Lỗi:", error);
  }
}

// Gọi async function
getUserWithAsync(1);
```

**🔑 Các Quy Tắc**:
1. `async` function luôn return Promise
2. `await` chỉ dùng được trong `async` function
3. Dùng `try/catch` để bắt lỗi

**📌 Bài Tập 5: Hệ Thống Đặt Phòng Khách Sạn**

```javascript
// Yêu cầu: Tạo hệ thống đặt phòng với các bước:
// 1. checkAvailability(roomId) - Kiểm tra phòng trống (1s)
// 2. createBooking(roomId, guestName) - Tạo booking (1.5s)
// 3. processPayment(bookingId, amount) - Thanh toán (2s)
// 4. sendConfirmation(bookingId) - Gửi xác nhận (1s)
//
// Dùng Async/Await để xử lý tuần tự

// TODO: Hoàn thành code
```

<details>
<summary>👉 Xem Lời Giải</summary>

```javascript
// Giả lập các functions bất đồng bộ
function checkAvailability(roomId) {
  return new Promise((resolve, reject) => {
    console.log(`1️⃣ Đang kiểm tra phòng ${roomId}...`);
    setTimeout(() => {
      const available = Math.random() > 0.2; // 80% có phòng
      if (available) {
        resolve({ roomId, available: true, price: 1000000 });
      } else {
        reject(new Error("Phòng đã hết"));
      }
    }, 1000);
  });
}

function createBooking(roomId, guestName) {
  return new Promise((resolve) => {
    console.log(`2️⃣ Đang tạo booking cho ${guestName}...`);
    setTimeout(() => {
      const bookingId = `BK${Date.now()}`;
      resolve({ bookingId, roomId, guestName });
    }, 1500);
  });
}

function processPayment(bookingId, amount) {
  return new Promise((resolve, reject) => {
    console.log(`3️⃣ Đang xử lý thanh toán ${amount.toLocaleString('vi-VN')}đ...`);
    setTimeout(() => {
      const success = Math.random() > 0.1; // 90% thành công
      if (success) {
        resolve({ bookingId, amount, paymentId: `PAY${Date.now()}` });
      } else {
        reject(new Error("Thanh toán thất bại"));
      }
    }, 2000);
  });
}

function sendConfirmation(bookingId) {
  return new Promise((resolve) => {
    console.log(`4️⃣ Đang gửi email xác nhận...`);
    setTimeout(() => {
      resolve({ bookingId, confirmed: true });
    }, 1000);
  });
}

// === Hàm chính - Đặt phòng ===
async function bookRoom(roomId, guestName) {
  console.log(`\n🏨 BẮT ĐẦU ĐẶT PHÒNG\n`);

  try {
    // Bước 1: Kiểm tra phòng trống
    const room = await checkAvailability(roomId);
    console.log(`✓ Phòng ${roomId} còn trống, giá ${room.price.toLocaleString('vi-VN')}đ\n`);

    // Bước 2: Tạo booking
    const booking = await createBooking(roomId, guestName);
    console.log(`✓ Đã tạo booking ${booking.bookingId}\n`);

    // Bước 3: Thanh toán
    const payment = await processPayment(booking.bookingId, room.price);
    console.log(`✓ Thanh toán thành công, mã ${payment.paymentId}\n`);

    // Bước 4: Gửi xác nhận
    const confirmation = await sendConfirmation(booking.bookingId);
    console.log(`✓ Đã gửi email xác nhận\n`);

    console.log(`🎉 ĐẶT PHÒNG THÀNH CÔNG!\n`);
    return {
      success: true,
      booking,
      payment,
      confirmation
    };

  } catch (error) {
    console.error(`\n❌ ĐẶT PHÒNG THẤT BẠI: ${error.message}\n`);
    return { success: false, error: error.message };
  }
}

// Sử dụng
bookRoom(101, "Nguyễn Văn A");
```
</details>

### 3.4 Event Loop - Vòng Lặp Sự Kiện

**Tư duy**: Event Loop như một "thư ký" giúp JavaScript xử lý nhiều việc cùng lúc:

```
┌────────────────────────────┐
│      CALL STACK            │  ← Chạy code JavaScript
│   (Ngăn xếp gọi hàm)       │
└────────────────────────────┘
            ↓
┌────────────────────────────┐
│      WEB APIs              │  ← setTimeout, fetch, DOM
│   (Xử lý bất đồng bộ)      │
└────────────────────────────┘
            ↓
┌────────────────────────────┐
│   CALLBACK QUEUE           │  ← Hàng đợi callbacks
│   [callback1, callback2]   │
└────────────────────────────┘
            ↓
      EVENT LOOP ←──────────┘  ← Kiểm tra & đưa vào Call Stack
```

**Ví dụ minh họa**:

```javascript
console.log("1. Start");

setTimeout(() => {
  console.log("2. Timeout");
}, 0); // 0 giây vẫn phải chờ!

Promise.resolve().then(() => {
  console.log("3. Promise");
});

console.log("4. End");

// Output:
// 1. Start
// 4. End
// 3. Promise
// 2. Timeout

// Giải thích:
// - "1. Start" và "4. End": Code đồng bộ, chạy ngay
// - "3. Promise": Microtask, ưu tiên cao hơn
// - "2. Timeout": Macrotask, ưu tiên thấp nhất
```

**🔑 Hai Loại Task**:
1. **Microtasks** (ưu tiên cao): Promises, queueMicrotask
2. **Macrotasks** (ưu tiên thấp): setTimeout, setInterval, I/O

---

## 4. JavaScript Modules

### 🤔 Tư Duy: Tại Sao Cần Modules?

**Vấn đề**: File JavaScript dài 5000 dòng → Khó đọc, khó maintain, khó tái sử dụng

**Giải pháp**: Chia nhỏ thành nhiều modules (files nhỏ), mỗi module làm 1 việc cụ thể

**Lợi ích**:
- ✅ Tổ chức code tốt hơn
- ✅ Tái sử dụng dễ dàng
- ✅ Tránh xung đột tên biến
- ✅ Dễ test từng phần

### 4.1 ES6 Modules (ESM) - Chuẩn Hiện Đại

**Export - Xuất Ra**

```javascript
// === math.js - Named Exports ===
export const PI = 3.14159;

export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

export function multiply(a, b) {
  return a * b;
}

// Hoặc export một lần ở cuối
const divide = (a, b) => a / b;
const power = (a, b) => Math.pow(a, b);

export { divide, power };

// === user.js - Default Export ===
export default class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  getInfo() {
    return `${this.name} - ${this.email}`;
  }
}

// Có thể có cả default và named exports
export const USER_ROLES = {
  ADMIN: 'admin',
  USER: 'user',
  GUEST: 'guest'
};
```

**Import - Nhập Vào**

```javascript
// === app.js ===

// Import named exports
import { add, subtract, PI } from './math.js';

console.log(add(5, 3));      // 8
console.log(subtract(10, 4)); // 6
console.log(PI);             // 3.14159

// Import với alias (đổi tên)
import { add as sum, multiply as times } from './math.js';
console.log(sum(2, 3));      // 5
console.log(times(4, 5));    // 20

// Import tất cả
import * as MathUtils from './math.js';
console.log(MathUtils.add(1, 2));     // 3
console.log(MathUtils.multiply(3, 4)); // 12

// Import default export
import User from './user.js';
const user1 = new User("An", "an@example.com");
console.log(user1.getInfo()); // An - an@example.com

// Import cả default và named
import User, { USER_ROLES } from './user.js';
console.log(USER_ROLES.ADMIN); // 'admin'
```

### 4.2 Ví Dụ Thực Tế: Ứng Dụng Todo

**Cấu trúc thư mục**:
```
todo-app/
├── index.html
├── src/
│   ├── models/
│   │   └── Todo.js
│   ├── services/
│   │   └── TodoService.js
│   ├── utils/
│   │   └── helpers.js
│   └── app.js
```

**1. Model - Todo.js**

```javascript
// models/Todo.js
export default class Todo {
  constructor(id, title, completed = false) {
    this.id = id;
    this.title = title;
    this.completed = completed;
    this.createdAt = new Date();
  }

  toggle() {
    this.completed = !this.completed;
  }

  updateTitle(newTitle) {
    if (newTitle.trim()) {
      this.title = newTitle;
    }
  }

  getAge() {
    const now = new Date();
    const diff = now - this.createdAt;
    const minutes = Math.floor(diff / 60000);

    if (minutes < 1) return "Vừa xong";
    if (minutes < 60) return `${minutes} phút trước`;
    const hours = Math.floor(minutes / 60);
    return `${hours} giờ trước`;
  }
}
```

**2. Service - TodoService.js**

```javascript
// services/TodoService.js
import Todo from '../models/Todo.js';

class TodoService {
  constructor() {
    this.todos = [];
    this.nextId = 1;
  }

  // Thêm todo mới
  addTodo(title) {
    if (!title.trim()) {
      throw new Error("Tiêu đề không được để trống");
    }

    const todo = new Todo(this.nextId++, title);
    this.todos.push(todo);
    console.log(`✓ Đã thêm: "${title}"`);
    return todo;
  }

  // Xóa todo
  removeTodo(id) {
    const index = this.todos.findIndex(todo => todo.id === id);
    if (index !== -1) {
      const removed = this.todos.splice(index, 1)[0];
      console.log(`✓ Đã xóa: "${removed.title}"`);
      return true;
    }
    return false;
  }

  // Đánh dấu hoàn thành/chưa hoàn thành
  toggleTodo(id) {
    const todo = this.todos.find(t => t.id === id);
    if (todo) {
      todo.toggle();
      console.log(`✓ ${todo.title}: ${todo.completed ? 'Hoàn thành' : 'Chưa hoàn thành'}`);
      return true;
    }
    return false;
  }

  // Lấy tất cả todos
  getAllTodos() {
    return [...this.todos]; // Return copy
  }

  // Lấy todos chưa hoàn thành
  getActiveTodos() {
    return this.todos.filter(todo => !todo.completed);
  }

  // Lấy todos đã hoàn thành
  getCompletedTodos() {
    return this.todos.filter(todo => todo.completed);
  }

  // Thống kê
  getStats() {
    return {
      total: this.todos.length,
      active: this.getActiveTodos().length,
      completed: this.getCompletedTodos().length
    };
  }
}

// Export singleton instance
export default new TodoService();
```

**3. Utilities - helpers.js**

```javascript
// utils/helpers.js

// Format ngày giờ
export function formatDate(date) {
  return date.toLocaleDateString('vi-VN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  });
}

// Tạo ID ngẫu nhiên
export function generateId() {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

// Validate input
export function validateTodoTitle(title) {
  if (!title || typeof title !== 'string') {
    return { valid: false, error: "Tiêu đề phải là chuỗi" };
  }

  const trimmed = title.trim();
  if (trimmed.length === 0) {
    return { valid: false, error: "Tiêu đề không được để trống" };
  }

  if (trimmed.length > 100) {
    return { valid: false, error: "Tiêu đề không được quá 100 ký tự" };
  }

  return { valid: true, value: trimmed };
}

// Constants
export const CONSTANTS = {
  MAX_TITLE_LENGTH: 100,
  STORAGE_KEY: 'todos_app',
  COLORS: {
    ACTIVE: '#007bff',
    COMPLETED: '#28a745'
  }
};
```

**4. Main App - app.js**

```javascript
// app.js
import todoService from './services/TodoService.js';
import { formatDate, validateTodoTitle, CONSTANTS } from './utils/helpers.js';

class TodoApp {
  constructor() {
    this.service = todoService;
    this.init();
  }

  init() {
    console.log("📝 TODO APP STARTED\n");
    this.demo();
  }

  demo() {
    // Thêm todos
    console.log("=== THÊM TODOS ===");
    this.service.addTodo("Học JavaScript Modules");
    this.service.addTodo("Làm bài tập ES6");
    this.service.addTodo("Ôn thi cuối kỳ");
    this.service.addTodo("Đi chơi");

    // Hiển thị
    console.log("\n=== DANH SÁCH ===");
    this.displayTodos();

    // Đánh dấu hoàn thành
    console.log("\n=== ĐÁNH DẤU HOÀN THÀNH ===");
    this.service.toggleTodo(1);
    this.service.toggleTodo(2);

    // Hiển thị lại
    console.log("\n=== SAU KHI CẬP NHẬT ===");
    this.displayTodos();

    // Thống kê
    console.log("\n=== THỐNG KÊ ===");
    this.displayStats();

    // Xóa
    console.log("\n=== XÓA TODO ===");
    this.service.removeTodo(4);
    this.displayTodos();
  }

  displayTodos() {
    const todos = this.service.getAllTodos();

    if (todos.length === 0) {
      console.log("(Chưa có todo nào)");
      return;
    }

    todos.forEach(todo => {
      const status = todo.completed ? "✅" : "⬜";
      const age = todo.getAge();
      console.log(`${status} [${todo.id}] ${todo.title} (${age})`);
    });
  }

  displayStats() {
    const stats = this.service.getStats();
    console.log(`📊 Tổng: ${stats.total}`);
    console.log(`⬜ Đang làm: ${stats.active}`);
    console.log(`✅ Hoàn thành: ${stats.completed}`);

    if (stats.total > 0) {
      const percent = ((stats.completed / stats.total) * 100).toFixed(1);
      console.log(`📈 Tiến độ: ${percent}%`);
    }
  }
}

// Khởi chạy app
new TodoApp();
```

**Chạy trong HTML**:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Todo App</title>
</head>
<body>
  <h1>Todo App</h1>
  <p>Mở Console để xem kết quả</p>

  <!-- Import module với type="module" -->
  <script type="module" src="./src/app.js"></script>
</body>
</html>
```

**💡 Lưu Ý Quan Trọng**:
- Phải có `type="module"` trong thẻ `<script>`
- Modules chạy trong strict mode tự động
- Không thể dùng `import/export` ngoài modules
- Cần web server (không chạy được bằng file://)

---

## 📚 Tổng Kết Part 1

### ✅ Kiến Thức Đã Học

**1. Prototype & Prototype Chain**
- Prototype là "mẫu" để objects khác kế thừa
- Prototype Chain: chuỗi kế thừa nhiều tầng
- Constructor functions & ES6 Classes

**2. JavaScript Patterns**
- Module Pattern: Tạo private/public members
- Singleton Pattern: Chỉ 1 instance duy nhất
- Observer Pattern: Theo dõi và thông báo
- Factory Pattern: Tạo objects linh hoạt

**3. Asynchronous JavaScript**
- Callbacks: Hàm gọi lại (callback hell!)
- Promises: Lời hứa với then/catch
- Async/Await: Cú pháp đẹp, dễ đọc
- Event Loop: Xử lý bất đồng bộ

**4. JavaScript Modules**
- ES6 Modules: import/export
- Tổ chức code thành files nhỏ
- Tái sử dụng và maintain dễ dàng

### 📝 Checklist Ôn Tập

- [ ] Giải thích được Prototype là gì
- [ ] Phân biệt Constructor Function vs Class
- [ ] Tạo được Module với private/public members
- [ ] Hiểu và dùng được Promise
- [ ] Viết được async/await
- [ ] Tổ chức code thành modules

### 🎯 Bài Tập Tổng Hợp

**Tạo Ứng Dụng Quản Lý Sinh Viên**

Yêu cầu:
1. Dùng ES6 Classes (Person, Student)
2. Tạo Module Pattern cho StudentManager
3. Dùng Async/Await để "giả lập" lưu database
4. Tổ chức thành modules riêng

Hints:
- `models/Student.js`: Class Student
- `services/StudentService.js`: Quản lý students
- `utils/validators.js`: Validate dữ liệu
- `app.js`: Main application

### 💡 Tips Học Tốt

1. **Thực hành mỗi ngày**: Code 30-60 phút/ngày
2. **Làm bài tập**: Tự tạo mini projects
3. **Debug thường xuyên**: Dùng `console.log`, DevTools
4. **Đọc code người khác**: Học từ GitHub
5. **Hỏi khi không hiểu**: Google, Stack Overflow, ChatGPT

---

**🎉 Chúc bạn học tốt JavaScript Nâng Cao! 🚀**

*Hãy chuyển sang Part 2 để học tiếp về JavaScript Engine, Error Handling, và Memory Management!*