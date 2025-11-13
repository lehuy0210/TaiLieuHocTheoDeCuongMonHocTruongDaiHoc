# JavaScript Nâng Cao 3 - Tài Liệu Học Tập

## Mục Lục
1. [Composition vs Inheritance](#1-composition-vs-inheritance)
2. [Type Coercion](#2-type-coercion)
3. [Pass By Reference vs Pass By Value](#3-pass-by-reference-vs-pass-by-value)
4. [Higher Order Functions](#4-higher-order-functions)

---

## 1. Composition vs Inheritance

### 1.1 Inheritance (Kế thừa) là gì?

Inheritance là cơ chế cho phép class con kế thừa properties và methods từ class cha.

```javascript
// Ví dụ Inheritance cơ bản
class Animal {
  constructor(name) {
    this.name = name;
  }
  
  eat() {
    console.log(`${this.name} đang ăn`);
  }
  
  sleep() {
    console.log(`${this.name} đang ngủ`);
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }
  
  bark() {
    console.log(`${this.name} sủa: Gâu gâu!`);
  }
}

class Cat extends Animal {
  constructor(name, color) {
    super(name);
    this.color = color;
  }
  
  meow() {
    console.log(`${this.name} kêu: Meo meo!`);
  }
}

const dog = new Dog("Milu", "Corgi");
dog.eat();   // Kế thừa từ Animal
dog.bark();  // Method riêng của Dog

const cat = new Cat("Kitty", "white");
cat.eat();   // Kế thừa từ Animal
cat.meow();  // Method riêng của Cat
```

### 1.2 Vấn Đề với Inheritance

```javascript
// Vấn đề 1: Hierarchy cứng nhắc
class Vehicle {
  move() {
    console.log("Di chuyển");
  }
}

class Car extends Vehicle {
  drive() {
    console.log("Lái xe");
  }
}

class Boat extends Vehicle {
  sail() {
    console.log("Chèo thuyền");
  }
}

// Vấn đề: Nếu muốn có AmphibiousCar (xe lội nước)?
// Nó cần cả drive() và sail()
// Không thể extend cả Car và Boat (multiple inheritance không support)

// Vấn đề 2: Tight coupling
class Employee {
  constructor(name, salary) {
    this.name = name;
    this.salary = salary;
  }
  
  work() {
    console.log(`${this.name} đang làm việc`);
  }
  
  getSalary() {
    return this.salary;
  }
}

class Manager extends Employee {
  constructor(name, salary, team) {
    super(name, salary);
    this.team = team;
  }
  
  manage() {
    console.log(`${this.name} quản lý team ${this.team}`);
  }
}

// Nếu muốn thay đổi Employee, có thể ảnh hưởng đến Manager
// Tight coupling giữa parent và child classes

// Vấn đề 3: Gorilla/Banana problem
// "Bạn muốn một quả chuối nhưng phải lấy cả con gorilla cầm chuối và cả khu rừng"
class Animal {
  eat() { }
  sleep() { }
  makeSound() { }
  reproduce() { }
  // ... 50 methods khác
}

class Bird extends Animal {
  fly() { }
}

// Bird kế thừa tất cả methods từ Animal
// Kể cả những methods không cần thiết
```

### 1.3 Composition (Kết hợp) là gì?

Composition là kỹ thuật xây dựng objects phức tạp từ các objects nhỏ hơn.

```javascript
// Factory functions cho behaviors
const canEat = (state) => ({
  eat(food) {
    console.log(`${state.name} đang ăn ${food}`);
    state.energy += 10;
  }
});

const canWalk = (state) => ({
  walk() {
    console.log(`${state.name} đang đi bộ`);
    state.energy -= 5;
  }
});

const canSwim = (state) => ({
  swim() {
    console.log(`${state.name} đang bơi`);
    state.energy -= 3;
  }
});

const canFly = (state) => ({
  fly() {
    console.log(`${state.name} đang bay`);
    state.energy -= 8;
  }
});

// Compose function
const compose = (...fns) => (obj) => {
  return fns.reduce((acc, fn) => {
    return { ...acc, ...fn(obj) };
  }, obj);
};

// Tạo các animals khác nhau bằng composition
function createDog(name) {
  const state = {
    name,
    energy: 100
  };
  
  return compose(
    canEat,
    canWalk
  )(state);
}

function createDuck(name) {
  const state = {
    name,
    energy: 100
  };
  
  return compose(
    canEat,
    canWalk,
    canSwim,
    canFly
  )(state);
}

function createFish(name) {
  const state = {
    name,
    energy: 100
  };
  
  return compose(
    canEat,
    canSwim
  )(state);
}

// Sử dụng
const dog = createDog("Milu");
dog.eat("thịt");
dog.walk();
// dog.fly(); // undefined - không có method này

const duck = createDuck("Donald");
duck.eat("gạo");
duck.walk();
duck.swim();
duck.fly();

const fish = createFish("Nemo");
fish.eat("tảo");
fish.swim();
// fish.walk(); // undefined
```

### 1.4 So Sánh Composition vs Inheritance

```javascript
// ============================================
// INHERITANCE APPROACH
// ============================================
class Vehicle {
  constructor(name) {
    this.name = name;
  }
  
  move() {
    console.log(`${this.name} đang di chuyển`);
  }
}

class FlyingVehicle extends Vehicle {
  fly() {
    console.log(`${this.name} đang bay`);
  }
}

class WaterVehicle extends Vehicle {
  sail() {
    console.log(`${this.name} đang đi trên nước`);
  }
}

// Vấn đề: Không thể tạo vehicle vừa bay vừa đi nước
// const amphibious = ???

// ============================================
// COMPOSITION APPROACH
// ============================================
const withMovement = (state) => ({
  move() {
    console.log(`${state.name} đang di chuyển`);
  }
});

const withFlying = (state) => ({
  fly() {
    console.log(`${state.name} đang bay`);
  }
});

const withSailing = (state) => ({
  sail() {
    console.log(`${state.name} đang đi trên nước`);
  }
});

const withDriving = (state) => ({
  drive() {
    console.log(`${state.name} đang lái trên đường`);
  }
});

// Flexible: Tạo bất kỳ combination nào
function createAirplane(name) {
  const state = { name };
  return Object.assign(state, withMovement(state), withFlying(state));
}

function createBoat(name) {
  const state = { name };
  return Object.assign(state, withMovement(state), withSailing(state));
}

function createCar(name) {
  const state = { name };
  return Object.assign(state, withMovement(state), withDriving(state));
}

function createAmphibiousCar(name) {
  const state = { name };
  return Object.assign(
    state,
    withMovement(state),
    withDriving(state),
    withSailing(state)
  );
}

function createFlyingCar(name) {
  const state = { name };
  return Object.assign(
    state,
    withMovement(state),
    withDriving(state),
    withFlying(state)
  );
}

// Sử dụng
const flyingCar = createFlyingCar("DeLorean");
flyingCar.drive();
flyingCar.fly();
// flyingCar.sail(); // undefined - không có
```

### 1.5 Composition với Modern JavaScript

```javascript
// Sử dụng mixins
const EaterMixin = {
  eat(food) {
    console.log(`${this.name} ăn ${food}`);
  }
};

const WalkerMixin = {
  walk() {
    console.log(`${this.name} đi bộ`);
  }
};

const SpeakerMixin = {
  speak(message) {
    console.log(`${this.name} nói: ${message}`);
  }
};

// Helper function để apply mixins
function mixin(target, ...sources) {
  Object.assign(target.prototype, ...sources);
}

// Tạo class với mixins
class Person {
  constructor(name) {
    this.name = name;
  }
}

mixin(Person, EaterMixin, WalkerMixin, SpeakerMixin);

const person = new Person("An");
person.eat("cơm");
person.walk();
person.speak("Xin chào!");

// Hoặc dùng class extends với mixins
const applyMixins = (targetClass, ...mixins) => {
  mixins.forEach(mixin => {
    Object.getOwnPropertyNames(mixin).forEach(name => {
      if (name !== 'constructor') {
        targetClass.prototype[name] = mixin[name];
      }
    });
  });
};

class Robot {
  constructor(name) {
    this.name = name;
  }
}

applyMixins(Robot, WalkerMixin, SpeakerMixin);

const robot = new Robot("R2D2");
robot.walk();
robot.speak("Beep boop!");
```

### 1.6 Ví Dụ Thực Tế: Game Characters

```javascript
// ============================================
// BAD: Using Inheritance
// ============================================
class Character {
  constructor(name, health) {
    this.name = name;
    this.health = health;
  }
  
  takeDamage(damage) {
    this.health -= damage;
  }
}

class Warrior extends Character {
  constructor(name, health, weapon) {
    super(name, health);
    this.weapon = weapon;
  }
  
  attack() {
    return this.weapon.damage;
  }
}

class Mage extends Character {
  constructor(name, health, mana) {
    super(name, health);
    this.mana = mana;
  }
  
  castSpell() {
    if (this.mana >= 10) {
      this.mana -= 10;
      return 50;
    }
    return 0;
  }
}

// Vấn đề: Không thể tạo BattleMage (vừa attack vừa castSpell)

// ============================================
// GOOD: Using Composition
// ============================================
const hasHealth = (state) => ({
  takeDamage(damage) {
    state.health -= damage;
    console.log(`${state.name} nhận ${damage} sát thương. HP còn: ${state.health}`);
  },
  heal(amount) {
    state.health += amount;
    console.log(`${state.name} hồi ${amount} HP. HP hiện tại: ${state.health}`);
  },
  isDead() {
    return state.health <= 0;
  }
});

const canAttack = (state) => ({
  attack(target) {
    const damage = state.attackPower || 10;
    console.log(`${state.name} tấn công ${target.name} gây ${damage} sát thương`);
    target.takeDamage(damage);
  }
});

const canCastSpells = (state) => ({
  castSpell(spellName, target) {
    const manaCost = state.spells[spellName] || 10;
    
    if (state.mana >= manaCost) {
      state.mana -= manaCost;
      const damage = manaCost * 5;
      console.log(`${state.name} dùng ${spellName}! Mana còn: ${state.mana}`);
      target.takeDamage(damage);
    } else {
      console.log(`${state.name} không đủ mana!`);
    }
  },
  restoreMana(amount) {
    state.mana += amount;
    console.log(`${state.name} hồi ${amount} mana. Mana: ${state.mana}`);
  }
});

const canDefend = (state) => ({
  defend() {
    state.isDefending = true;
    console.log(`${state.name} đang phòng thủ`);
  }
});

// Factory functions
function createWarrior(name) {
  const state = {
    name,
    health: 100,
    attackPower: 20,
    isDefending: false
  };
  
  return Object.assign(
    state,
    hasHealth(state),
    canAttack(state),
    canDefend(state)
  );
}

function createMage(name) {
  const state = {
    name,
    health: 80,
    mana: 100,
    spells: {
      fireball: 15,
      lightning: 20,
      heal: 10
    }
  };
  
  return Object.assign(
    state,
    hasHealth(state),
    canCastSpells(state)
  );
}

function createBattleMage(name) {
  const state = {
    name,
    health: 90,
    mana: 80,
    attackPower: 15,
    spells: {
      fireball: 15,
      lightning: 20
    },
    isDefending: false
  };
  
  return Object.assign(
    state,
    hasHealth(state),
    canAttack(state),
    canCastSpells(state),
    canDefend(state)
  );
}

// Test game
const warrior = createWarrior("Conan");
const mage = createMage("Gandalf");
const battleMage = createBattleMage("Merlin");

warrior.attack(mage);
mage.castSpell("fireball", warrior);
battleMage.attack(warrior);
battleMage.castSpell("lightning", mage);
battleMage.defend();
```

### 1.7 Khi Nào Dùng Composition, Khi Nào Dùng Inheritance?

```javascript
// ✅ Dùng INHERITANCE khi:
// 1. Có relationship "is-a" rõ ràng
class Vehicle { }
class Car extends Vehicle { } // Car IS-A Vehicle ✓

// 2. Hierarchy đơn giản, ít thay đổi
class Shape {
  getArea() { }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }
  
  getArea() {
    return Math.PI * this.radius ** 2;
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }
  
  getArea() {
    return this.width * this.height;
  }
}

// ✅ Dùng COMPOSITION khi:
// 1. Cần flexibility cao
// 2. Có relationship "has-a" hoặc "can-do"
// 3. Muốn tái sử dụng behavior

// Ví dụ: Email service
const withLogging = (service) => ({
  ...service,
  log(message) {
    console.log(`[LOG] ${new Date().toISOString()}: ${message}`);
  }
});

const withRetry = (service) => ({
  ...service,
  async sendWithRetry(email, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
      try {
        return await service.send(email);
      } catch (error) {
        if (i === maxRetries - 1) throw error;
        console.log(`Retry ${i + 1}/${maxRetries}...`);
        await new Promise(resolve => setTimeout(resolve, 1000));
      }
    }
  }
});

const withValidation = (service) => ({
  ...service,
  validateAndSend(email) {
    if (!email.to || !email.subject || !email.body) {
      throw new Error("Email thiếu thông tin bắt buộc");
    }
    
    if (!email.to.includes('@')) {
      throw new Error("Email không hợp lệ");
    }
    
    return service.send(email);
  }
});

// Base service
const basicEmailService = {
  send(email) {
    console.log(`Gửi email đến ${email.to}`);
    return Promise.resolve({ success: true });
  }
};

// Compose các features
const emailService = withValidation(
  withRetry(
    withLogging(basicEmailService)
  )
);

// Sử dụng
emailService.log("Email service started");
emailService.validateAndSend({
  to: "user@example.com",
  subject: "Hello",
  body: "Test email"
});
```

### 1.8 Best Practices

```javascript
// ✅ GOOD: Composition với pure functions
const withTimestamp = (obj) => ({
  ...obj,
  timestamp: Date.now(),
  getAge() {
    return Date.now() - this.timestamp;
  }
});

const withId = (obj) => ({
  ...obj,
  id: Math.random().toString(36).substr(2, 9)
});

const createUser = (name, email) => {
  const user = { name, email };
  return withTimestamp(withId(user));
};

const user = createUser("An", "an@example.com");
console.log(user);

// ✅ GOOD: Pipe function cho composition
const pipe = (...fns) => (value) => {
  return fns.reduce((acc, fn) => fn(acc), value);
};

const enhance = pipe(
  withId,
  withTimestamp
);

const product = enhance({ name: "Laptop", price: 1000 });
console.log(product);

// ❌ BAD: Deep inheritance hierarchy
class A { }
class B extends A { }
class C extends B { }
class D extends C { }
class E extends D { } // Quá sâu, khó maintain

// ✅ GOOD: Flat composition
const featureA = (obj) => ({ ...obj, methodA() { } });
const featureB = (obj) => ({ ...obj, methodB() { } });
const featureC = (obj) => ({ ...obj, methodC() { } });

const createE = () => {
  const obj = {};
  return featureC(featureB(featureA(obj)));
};
```

---

## 2. Type Coercion

### 2.1 Type Coercion là gì?

Type Coercion là quá trình JavaScript tự động chuyển đổi giữa các kiểu dữ liệu.

```javascript
// Implicit coercion (ngầm định)
console.log(5 + "5");        // "55" (number → string)
console.log("5" - 2);        // 3 (string → number)
console.log(true + 1);       // 2 (boolean → number)
console.log(false + 10);     // 10 (boolean → number)
console.log("10" * "2");     // 20 (string → number)
console.log([] + []);        // "" (array → string)
console.log({} + {});        // "[object Object][object Object]"

// Explicit coercion (tường minh)
console.log(Number("5"));    // 5
console.log(String(123));    // "123"
console.log(Boolean(0));     // false
console.log(Boolean(1));     // true
```

### 2.2 String Coercion

```javascript
// Dùng + với string → chuyển sang string
console.log("5" + 5);        // "55"
console.log(5 + "5");        // "55"
console.log("Hello" + 123);  // "Hello123"
console.log(true + "!");     // "true!"

// Template literals
const age = 25;
console.log(`Tôi ${age} tuổi`); // "Tôi 25 tuổi"

// String() function
console.log(String(123));     // "123"
console.log(String(true));    // "true"
console.log(String(null));    // "null"
console.log(String(undefined)); // "undefined"
console.log(String([1, 2, 3])); // "1,2,3"
console.log(String({ name: "An" })); // "[object Object]"

// toString() method
console.log((123).toString());     // "123"
console.log(true.toString());      // "true"
console.log([1, 2, 3].toString()); // "1,2,3"

// Số với cơ số khác nhau
const num = 255;
console.log(num.toString(2));   // "11111111" (binary)
console.log(num.toString(8));   // "377" (octal)
console.log(num.toString(16));  // "ff" (hexadecimal)
```

### 2.3 Number Coercion

```javascript
// Dùng +, -, *, / → chuyển sang number
console.log("5" - 2);        // 3
console.log("10" * "2");     // 20
console.log("20" / "4");     // 5
console.log("5" % "2");      // 1

// Unary + operator
console.log(+"123");         // 123
console.log(+"45.67");       // 45.67
console.log(+true);          // 1
console.log(+false);         // 0
console.log(+null);          // 0
console.log(+undefined);     // NaN
console.log(+"hello");       // NaN

// Number() function
console.log(Number("123"));      // 123
console.log(Number("12.5"));     // 12.5
console.log(Number(""));         // 0
console.log(Number(" "));        // 0
console.log(Number(true));       // 1
console.log(Number(false));      // 0
console.log(Number(null));       // 0
console.log(Number(undefined));  // NaN
console.log(Number("123abc"));   // NaN

// parseInt() và parseFloat()
console.log(parseInt("123"));        // 123
console.log(parseInt("123.45"));     // 123 (bỏ phần thập phân)
console.log(parseInt("123abc"));     // 123 (parse đến khi gặp non-digit)
console.log(parseInt("abc123"));     // NaN
console.log(parseInt("0xFF"));       // 255 (hex)
console.log(parseInt("10", 2));      // 2 (binary)
console.log(parseInt("10", 8));      // 8 (octal)
console.log(parseInt("10", 16));     // 16 (hex)

console.log(parseFloat("123.45"));   // 123.45
console.log(parseFloat("123.45abc")); // 123.45
console.log(parseFloat(".5"));       // 0.5
```

### 2.4 Boolean Coercion

```javascript
// Falsy values: false, 0, -0, "", null, undefined, NaN
// Tất cả giá trị khác là truthy

// Boolean() function
console.log(Boolean(0));         // false
console.log(Boolean(1));         // true
console.log(Boolean(-1));        // true
console.log(Boolean(""));        // false
console.log(Boolean(" "));       // true (có space)
console.log(Boolean("0"));       // true (string)
console.log(Boolean("false"));   // true (string)
console.log(Boolean(null));      // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN));       // false
console.log(Boolean([]));        // true (empty array)
console.log(Boolean({}));        // true (empty object)

// Double NOT (!!) operator
console.log(!!0);                // false
console.log(!!1);                // true
console.log(!!"hello");          // true
console.log(!!"");               // false

// Trong if statements
if ("") {
  console.log("Không chạy");
}

if ("hello") {
  console.log("Có chạy"); // ✓
}

// Logical operators
console.log(true && "hello");    // "hello"
console.log(false && "hello");   // false
console.log(true || "hello");    // true
console.log(false || "hello");   // "hello"
console.log(null ?? "default");  // "default" (nullish coalescing)
```

### 2.5 Object to Primitive Coercion

```javascript
// ToPrimitive algorithm
const obj = {
  toString() {
    return "Object as string";
  },
  valueOf() {
    return 42;
  }
};

console.log(String(obj));   // "Object as string" (toString được gọi)
console.log(Number(obj));   // 42 (valueOf được gọi)
console.log(obj + "");      // "42" (valueOf được gọi trước)
console.log(obj + 10);      // 52 (valueOf được gọi)

// Date object
const date = new Date();
console.log(date + "");     // String representation
console.log(Number(date));  // Timestamp

// Array coercion
console.log([1, 2, 3] + ""); // "1,2,3"
console.log([] + "");        // ""
console.log([1] + [2]);      // "12"
console.log([1, 2] + [3, 4]); // "1,23,4"

// Object coercion
console.log({} + "");        // "[object Object]"
console.log({ a: 1 } + "");  // "[object Object]"

// Custom coercion
const point = {
  x: 10,
  y: 20,
  toString() {
    return `(${this.x}, ${this.y})`;
  },
  valueOf() {
    return Math.sqrt(this.x ** 2 + this.y ** 2);
  }
};

console.log(String(point));  // "(10, 20)"
console.log(Number(point));  // 22.360679774997898
console.log(point + "");     // "22.360679774997898"
console.log(point * 2);      // 44.721359549995796
```

### 2.6 Comparison Operators và Coercion

```javascript
// == (loose equality) - có coercion
console.log(5 == "5");       // true
console.log(true == 1);      // true
console.log(false == 0);     // true
console.log(null == undefined); // true
console.log("" == 0);        // true
console.log("" == false);    // true

// === (strict equality) - không coercion
console.log(5 === "5");      // false
console.log(true === 1);     // false
console.log(null === undefined); // false

// Comparison với coercion
console.log("10" > 5);       // true (string → number)
console.log("10" < "5");     // true (string comparison)
console.log("abc" > "ab");   // true (lexicographic)
console.log([1] > null);     // true ([1] → 1, null → 0)

// Các trường hợp đặc biệt
console.log(NaN == NaN);     // false
console.log(NaN === NaN);    // false
console.log(Object.is(NaN, NaN)); // true

console.log(+0 == -0);       // true
console.log(+0 === -0);      // true
console.log(Object.is(+0, -0)); // false

// Type coercion order
console.log([] == 0);        // true ([] → "" → 0)
console.log([] == "");       // true ([] → "")
console.log([] == false);    // true ([] → "" → 0, false → 0)
console.log(![] == false);   // true (![] → false)
```

### 2.7 Các Tình Huống Phức Tạp

```javascript
// Weird cases
console.log([] + []);        // ""
console.log([] + {});        // "[object Object]"
console.log({} + []);        // 0 hoặc "[object Object]" (phụ thuộc context)
console.log({} + {});        // NaN hoặc "[object Object][object Object]"

console.log(![] + []);       // "false"
console.log(+[] + []);       // "0"
console.log(!![] + []);      // "true"

console.log(true + false);   // 1
console.log(12 / "6");       // 2
console.log("number" + 15 + 3);     // "number153"
console.log(15 + 3 + "number");     // "18number"

// Tại sao: operator precedence và coercion
console.log([1, 2, 3] == "1,2,3");  // true
console.log([1, 2, 3] === "1,2,3"); // false

// Array to number coercion
console.log(+[]);            // 0
console.log(+[5]);           // 5
console.log(+[1, 2]);        // NaN

// Conditional (ternary) operator
const value = 0;
console.log(value ? "truthy" : "falsy"); // "falsy"

const value2 = "0";
console.log(value2 ? "truthy" : "falsy"); // "truthy"
```

### 2.8 Best Practices

```javascript
// ✅ GOOD: Explicit coercion
const age = "25";
const ageNumber = Number(age);
const ageStr = String(123);
const isActive = Boolean(status);

// ❌ BAD: Implicit coercion gây confusion
const result = age + 5; // "255" - không như mong đợi

// ✅ GOOD: Use strict equality
if (value === 0) { }
if (value === "") { }
if (value === null) { }

// ❌ BAD: Loose equality
if (value == 0) { } // Khớp cả "", false, null

// ✅ GOOD: Check type trước
function add(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new TypeError('Arguments must be numbers');
  }
  return a + b;
}

// ✅ GOOD: Use isNaN correctly
console.log(isNaN("hello"));     // true
console.log(Number.isNaN("hello")); // false (better)
console.log(Number.isNaN(NaN));     // true

// ✅ GOOD: Nullish coalescing
const value = 0;
console.log(value ?? 10);        // 0 (value không null/undefined)
console.log(value || 10);        // 10 (value là falsy)

const name = "";
console.log(name ?? "Anonymous"); // "" (name không null/undefined)
console.log(name || "Anonymous"); // "Anonymous" (name là falsy)

// ✅ GOOD: Optional chaining
const user = null;
console.log(user?.name ?? "Unknown"); // "Unknown"

// Utility functions
function toNumber(value) {
  const num = Number(value);
  if (Number.isNaN(num)) {
    throw new TypeError(`Cannot convert ${value} to number`);
  }
  return num;
}

function toString(value) {
  if (value == null) {
    return "";
  }
  return String(value);
}

function toBoolean(value) {
  return Boolean(value);
}
```

---

## 3. Pass By Reference vs Pass By Value

### 3.1 Primitive Types (Pass by Value)

Primitive types: string, number, boolean, undefined, null, symbol, bigint

```javascript
// Primitives được pass by value (copy value)
let x = 10;
let y = x;  // Copy value của x sang y

console.log(x); // 10
console.log(y); // 10

y = 20;         // Thay đổi y

console.log(x); // 10 (x không thay đổi)
console.log(y); // 20

// Ví dụ với function
function changeValue(num) {
  num = 100;
  console.log("Inside function:", num); // 100
}

let value = 50;
changeValue(value);
console.log("Outside function:", value); // 50 (không thay đổi)

/*
Memory Layout:

Stack:
┌───────────┐
│ x: 10     │
├───────────┤
│ y: 20     │ ← Copy độc lập
├───────────┤
│ value: 50 │
└───────────┘
*/
```

### 3.2 Objects (Pass by Reference)

Objects, Arrays, Functions được pass by reference (copy reference, không copy value)

```javascript
// Objects được pass by reference
let obj1 = { name: "An" };
let obj2 = obj1;  // Copy reference, không copy value

console.log(obj1.name); // "An"
console.log(obj2.name); // "An"

obj2.name = "Bình";     // Thay đổi qua obj2

console.log(obj1.name); // "Bình" (obj1 cũng thay đổi!)
console.log(obj2.name); // "Bình"

console.log(obj1 === obj2); // true (cùng reference)

/*
Memory Layout:

Stack:              Heap:
┌───────────┐      ┌──────────────┐
│ obj1: 0x001─────→│ { name: "Bình" }
├───────────┤  ↗   └──────────────┘
│ obj2: 0x001─────┘
└───────────┘
*/

// Array example
let arr1 = [1, 2, 3];
let arr2 = arr1;

arr2.push(4);

console.log(arr1); // [1, 2, 3, 4] (cũng thay đổi)
console.log(arr2); // [1, 2, 3, 4]
```

### 3.3 Function Arguments

```javascript
// Primitive arguments (pass by value)
function modifyPrimitive(x) {
  x = x * 2;
  console.log("Inside:", x); // 20
}

let num = 10;
modifyPrimitive(num);
console.log("Outside:", num); // 10 (không đổi)

// Object arguments (pass by reference)
function modifyObject(obj) {
  obj.name = "Modified";
  console.log("Inside:", obj.name); // "Modified"
}

let person = { name: "Original" };
modifyObject(person);
console.log("Outside:", person.name); // "Modified" (đã đổi!)

// Array arguments
function modifyArray(arr) {
  arr.push(4);
  console.log("Inside:", arr); // [1, 2, 3, 4]
}

let numbers = [1, 2, 3];
modifyArray(numbers);
console.log("Outside:", numbers); // [1, 2, 3, 4] (đã đổi!)
```

### 3.4 Reassignment vs Mutation

```javascript
// Reassignment không ảnh hưởng original
function reassignObject(obj) {
  obj = { name: "New Object" }; // Tạo object mới
  console.log("Inside:", obj.name); // "New Object"
}

let user = { name: "Original" };
reassignObject(user);
console.log("Outside:", user.name); // "Original" (không đổi)

/*
Giải thích:
- obj = { name: "New Object" } tạo object mới
- obj giờ trỏ đến object mới
- user vẫn trỏ đến object cũ
*/

// Mutation ảnh hưởng original
function mutateObject(obj) {
  obj.name = "Mutated"; // Thay đổi property
  console.log("Inside:", obj.name); // "Mutated"
}

let user2 = { name: "Original" };
mutateObject(user2);
console.log("Outside:", user2.name); // "Mutated" (đã đổi!)

/*
Memory visualization:

Reassignment:
Before:    user → Object A
After:     user → Object A
           obj → Object B (new)

Mutation:
Before:    user → Object A
           obj → Object A (same)
After:     user → Object A (modified)
           obj → Object A (modified)
*/
```

### 3.5 Shallow Copy vs Deep Copy

```javascript
// ============================================
// SHALLOW COPY
// ============================================

// 1. Object.assign()
const original = { name: "An", age: 25 };
const copy1 = Object.assign({}, original);

copy1.name = "Bình";
console.log(original.name); // "An" (không đổi)
console.log(copy1.name);    // "Bình"

// Vấn đề với nested objects
const user = {
  name: "An",
  address: {
    city: "Hanoi"
  }
};

const userCopy = Object.assign({}, user);
userCopy.address.city = "Saigon"; // Thay đổi nested object

console.log(user.address.city);     // "Saigon" (đã đổi - vấn đề!)
console.log(userCopy.address.city); // "Saigon"

// 2. Spread operator (...)
const arr = [1, 2, 3];
const arrCopy = [...arr];

arrCopy.push(4);
console.log(arr);     // [1, 2, 3] (không đổi)
console.log(arrCopy); // [1, 2, 3, 4]

// Vấn đề với nested arrays
const matrix = [[1, 2], [3, 4]];
const matrixCopy = [...matrix];

matrixCopy[0][0] = 99;
console.log(matrix[0][0]);     // 99 (đã đổi!)
console.log(matrixCopy[0][0]); // 99

// 3. Array.slice()
const numbers = [1, 2, 3];
const numbersCopy = numbers.slice();

numbersCopy.push(4);
console.log(numbers);     // [1, 2, 3]
console.log(numbersCopy); // [1, 2, 3, 4]

// ============================================
// DEEP COPY
// ============================================

// 1. JSON.parse(JSON.stringify()) - Simple but limited
const deepUser = {
  name: "An",
  address: {
    city: "Hanoi",
    country: "Vietnam"
  }
};

const deepCopy1 = JSON.parse(JSON.stringify(deepUser));
deepCopy1.address.city = "Saigon";

console.log(deepUser.address.city);  // "Hanoi" (không đổi!)
console.log(deepCopy1.address.city); // "Saigon"

// Hạn chế: không copy functions, undefined, Date, RegExp, etc.
const problematic = {
  func: () => console.log("Hello"),
  date: new Date(),
  undef: undefined,
  regex: /test/g
};

const problemCopy = JSON.parse(JSON.stringify(problematic));
console.log(problemCopy);
// {
//   date: "2024-01-01T00:00:00.000Z" (string, not Date!)
//   regex: {} (empty object!)
//   // func và undef bị mất!
// }

// 2. Recursive deep clone
function deepClone(obj) {
  // Handle primitive types và null
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }
  
  // Handle Date
  if (obj instanceof Date) {
    return new Date(obj.getTime());
  }
  
  // Handle Array
  if (Array.isArray(obj)) {
    return obj.map(item => deepClone(item));
  }
  
  // Handle Object
  const clonedObj = {};
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      clonedObj[key] = deepClone(obj[key]);
    }
  }
  
  return clonedObj;
}

// Test deep clone
const complex = {
  name: "An",
  age: 25,
  hobbies: ["reading", "coding"],
  address: {
    city: "Hanoi",
    coordinates: {
      lat: 21.0285,
      lng: 105.8542
    }
  },
  birthDate: new Date("1999-01-01")
};

const complexCopy = deepClone(complex);
complexCopy.address.coordinates.lat = 10.8231;
complexCopy.hobbies.push("gaming");

console.log(complex.address.coordinates.lat);  // 21.0285 (không đổi)
console.log(complexCopy.address.coordinates.lat); // 10.8231

console.log(complex.hobbies);     // ["reading", "coding"]
console.log(complexCopy.hobbies); // ["reading", "coding", "gaming"]

// 3. structuredClone() - Modern solution (Node 17+, modern browsers)
const modernCopy = structuredClone(complex);
modernCopy.address.city = "Saigon";

console.log(complex.address.city);     // "Hanoi"
console.log(modernCopy.address.city);  // "Saigon"
```

### 3.6 Preventing Modifications

```javascript
// 1. Object.freeze() - Ngăn modifications hoàn toàn
const frozen = Object.freeze({
  name: "An",
  age: 25
});

frozen.name = "Bình";     // Không hiệu lực (strict mode: TypeError)
frozen.salary = 1000;     // Không hiệu lực
delete frozen.age;        // Không hiệu lực

console.log(frozen); // { name: "An", age: 25 }

// Lưu ý: freeze chỉ shallow
const partialFrozen = Object.freeze({
  name: "An",
  address: {
    city: "Hanoi"
  }
});

partialFrozen.name = "Bình"; // Không đổi
partialFrozen.address.city = "Saigon"; // ĐỔI được! (nested object)

console.log(partialFrozen);
// { name: "An", address: { city: "Saigon" } }

// Deep freeze
function deepFreeze(obj) {
  Object.freeze(obj);
  
  Object.getOwnPropertyNames(obj).forEach(prop => {
    if (obj[prop] !== null
        && typeof obj[prop] === 'object'
        && !Object.isFrozen(obj[prop])) {
      deepFreeze(obj[prop]);
    }
  });
  
  return obj;
}

const fullyFrozen = deepFreeze({
  name: "An",
  address: {
    city: "Hanoi"
  }
});

fullyFrozen.address.city = "Saigon"; // Không đổi
console.log(fullyFrozen.address.city); // "Hanoi"

// 2. Object.seal() - Ngăn add/delete, cho phép modify
const sealed = Object.seal({
  name: "An",
  age: 25
});

sealed.name = "Bình";     // OK
sealed.salary = 1000;     // Không thêm được
delete sealed.age;        // Không xóa được

console.log(sealed); // { name: "Bình", age: 25 }

// 3. Object.preventExtensions() - Chỉ ngăn add properties
const restricted = Object.preventExtensions({
  name: "An",
  age: 25
});

restricted.name = "Bình";  // OK
restricted.salary = 1000;  // Không thêm được
delete restricted.age;     // XÓA được!

console.log(restricted); // { name: "Bình" }

// Check object status
console.log(Object.isFrozen(frozen));      // true
console.log(Object.isSealed(sealed));      // true
console.log(Object.isExtensible(restricted)); // false
```

### 3.7 Best Practices

```javascript
// ✅ GOOD: Return new objects thay vì modify
function addItem(cart, item) {
  return [...cart, item]; // New array
}

const cart1 = [{ name: "Laptop" }];
const cart2 = addItem(cart1, { name: "Mouse" });

console.log(cart1); // [{ name: "Laptop" }] (không đổi)
console.log(cart2); // [{ name: "Laptop" }, { name: "Mouse" }]

// ❌ BAD: Modify trực tiếp
function addItemBad(cart, item) {
  cart.push(item); // Mutate original
  return cart;
}

// ✅ GOOD: Defensive copying
function updateUser(user, updates) {
  return {
    ...user,
    ...updates,
    updatedAt: new Date()
  };
}

const user = { name: "An", email: "an@example.com" };
const updated = updateUser(user, { email: "new@example.com" });

console.log(user.email);    // "an@example.com"
console.log(updated.email); // "new@example.com"

// ✅ GOOD: Use const for references
const config = {
  apiUrl: "https://api.example.com",
  timeout: 5000
};

// config = {}; // TypeError: Assignment to constant variable
config.timeout = 10000; // OK (modify property)

// ✅ GOOD: Immutable patterns
class ImmutableUser {
  constructor(name, age) {
    Object.defineProperty(this, 'name', {
      value: name,
      writable: false,
      enumerable: true
    });
    Object.defineProperty(this, 'age', {
      value: age,
      writable: false,
      enumerable: true
    });
  }
  
  withAge(newAge) {
    return new ImmutableUser(this.name, newAge);
  }
}

const user1 = new ImmutableUser("An", 25);
const user2 = user1.withAge(26);

console.log(user1.age); // 25
console.log(user2.age); // 26

// ✅ GOOD: Avoid reference sharing
function createUser(name, sharedConfig) {
  return {
    name,
    config: { ...sharedConfig } // Copy config
  };
}

const defaultConfig = { theme: "light", lang: "vi" };
const user1 = createUser("An", defaultConfig);
const user2 = createUser("Bình", defaultConfig);

user1.config.theme = "dark";

console.log(user1.config.theme); // "dark"
console.log(user2.config.theme); // "light" (không ảnh hưởng)
console.log(defaultConfig.theme); // "light" (không ảnh hưởng)
```

---

## 4. Higher Order Functions

### 4.1 Higher Order Function là gì?

Higher Order Function (HOF) là function nhận function khác làm argument hoặc return function.

```javascript
// Function nhận function làm argument
function executeFunction(fn) {
  console.log("Đang thực thi function...");
  fn();
  console.log("Hoàn thành!");
}

executeFunction(() => {
  console.log("Hello from callback!");
});

// Function return function
function createMultiplier(multiplier) {
  return function(number) {
    return number * multiplier;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5));  // 10
console.log(triple(5));  // 15
```

### 4.2 Array Methods (Built-in HOFs)

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// ============================================
// 1. map() - Transform mỗi element
// ============================================
const doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

const users = [
  { name: "An", age: 25 },
  { name: "Bình", age: 30 },
  { name: "Chi", age: 28 }
];

const names = users.map(user => user.name);
console.log(names); // ["An", "Bình", "Chi"]

const userSummaries = users.map(user => ({
  summary: `${user.name} (${user.age} tuổi)`
}));
console.log(userSummaries);

// ============================================
// 2. filter() - Lọc elements
// ============================================
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2, 4, 6, 8, 10]

const adults = users.filter(user => user.age >= 18);
console.log(adults); // All users

const youngAdults = users.filter(user => user.age >= 18 && user.age < 30);
console.log(youngAdults); // An and Chi

// ============================================
// 3. reduce() - Tích lũy thành một giá trị
// ============================================
const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum); // 55

const product = numbers.reduce((acc, num) => acc * num, 1);
console.log(product); // 3628800

// Count occurrences
const fruits = ["apple", "banana", "apple", "orange", "banana", "apple"];
const fruitCount = fruits.reduce((acc, fruit) => {
  acc[fruit] = (acc[fruit] || 0) + 1;
  return acc;
}, {});
console.log(fruitCount); // { apple: 3, banana: 2, orange: 1 }

// Group by age
const groupedByAge = users.reduce((acc, user) => {
  const age = user.age;
  if (!acc[age]) {
    acc[age] = [];
  }
  acc[age].push(user);
  return acc;
}, {});
console.log(groupedByAge);

// ============================================
// 4. forEach() - Iterate không return
// ============================================
numbers.forEach((num, index) => {
  console.log(`Index ${index}: ${num}`);
});

// ============================================
// 5. find() - Tìm element đầu tiên thỏa mãn
// ============================================
const firstEven = numbers.find(num => num % 2 === 0);
console.log(firstEven); // 2

const userAn = users.find(user => user.name === "An");
console.log(userAn); // { name: "An", age: 25 }

// ============================================
// 6. findIndex() - Tìm index đầu tiên
// ============================================
const firstEvenIndex = numbers.findIndex(num => num % 2 === 0);
console.log(firstEvenIndex); // 1

// ============================================
// 7. some() - Kiểm tra CÓ ÍT NHẤT một element thỏa mãn
// ============================================
const hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven); // true

const hasMinor = users.some(user => user.age < 18);
console.log(hasMinor); // false

// ============================================
// 8. every() - Kiểm tra TẤT CẢ elements thỏa mãn
// ============================================
const allPositive = numbers.every(num => num > 0);
console.log(allPositive); // true

const allAdults = users.every(user => user.age >= 18);
console.log(allAdults); // true

// ============================================
// 9. sort() - Sắp xếp (mutates array!)
// ============================================
const unsorted = [3, 1, 4, 1, 5, 9, 2, 6];
const sorted = [...unsorted].sort((a, b) => a - b);
console.log(sorted); // [1, 1, 2, 3, 4, 5, 6, 9]

const sortedDesc = [...unsorted].sort((a, b) => b - a);
console.log(sortedDesc); // [9, 6, 5, 4, 3, 2, 1, 1]

// Sort objects
const sortedByAge = [...users].sort((a, b) => a.age - b.age);
console.log(sortedByAge);

// ============================================
// 10. flatMap() - Map rồi flatten
// ============================================
const nested = [[1, 2], [3, 4], [5, 6]];
const flattened = nested.flatMap(arr => arr);
console.log(flattened); // [1, 2, 3, 4, 5, 6]

const sentences = ["Hello world", "How are you"];
const words = sentences.flatMap(sentence => sentence.split(" "));
console.log(words); // ["Hello", "world", "How", "are", "you"]
```

### 4.3 Chaining Array Methods

```javascript
const products = [
  { name: "Laptop", price: 1000, category: "Electronics", inStock: true },
  { name: "Phone", price: 500, category: "Electronics", inStock: true },
  { name: "Shirt", price: 50, category: "Clothing", inStock: false },
  { name: "Shoes", price: 100, category: "Clothing", inStock: true },
  { name: "Watch", price: 200, category: "Accessories", inStock: true }
];

// Lọc, transform, và tính tổng
const totalElectronicsInStock = products
  .filter(p => p.category === "Electronics")
  .filter(p => p.inStock)
  .map(p => p.price)
  .reduce((sum, price) => sum + price, 0);

console.log(totalElectronicsInStock); // 1500

// Complex chain
const affordableProductNames = products
  .filter(p => p.inStock)           // Có sẵn
  .filter(p => p.price < 200)       // Giá < 200
  .map(p => p.name.toUpperCase())   // Uppercase names
  .sort();                           // Sort A-Z

console.log(affordableProductNames); // ["PHONE", "SHOES"]

// Tạo report
const categoryReport = products
  .reduce((acc, product) => {
    const cat = product.category;
    
    if (!acc[cat]) {
      acc[cat] = {
        totalProducts: 0,
        inStock: 0,
        totalValue: 0
      };
    }
    
    acc[cat].totalProducts++;
    if (product.inStock) {
      acc[cat].inStock++;
      acc[cat].totalValue += product.price;
    }
    
    return acc;
  }, {});

console.log(categoryReport);
/*
{
  Electronics: { totalProducts: 2, inStock: 2, totalValue: 1500 },
  Clothing: { totalProducts: 2, inStock: 1, totalValue: 100 },
  Accessories: { totalProducts: 1, inStock: 1, totalValue: 200 }
}
*/
```

### 4.4 Creating Custom HOFs

```javascript
// ============================================
// 1. Timing function
// ============================================
function measureTime(fn) {
  return function(...args) {
    const start = performance.now();
    const result = fn(...args);
    const end = performance.now();
    console.log(`Execution time: ${(end - start).toFixed(2)}ms`);
    return result;
  };
}

const slowFunction = measureTime(function(n) {
  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum += i;
  }
  return sum;
});

slowFunction(1000000); // Logs execution time

// ============================================
// 2. Memoization
// ============================================
function memoize(fn) {
  const cache = new Map();
  
  return function(...args) {
    const key = JSON.stringify(args);
    
    if (cache.has(key)) {
      console.log("Returning from cache");
      return cache.get(key);
    }
    
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

const expensiveCalculation = memoize(function(n) {
  console.log("Calculating...");
  let result = 0;
  for (let i = 0; i < n; i++) {
    result += i;
  }
  return result;
});

console.log(expensiveCalculation(1000)); // Calculating... 499500
console.log(expensiveCalculation(1000)); // Returning from cache 499500

// ============================================
// 3. Debounce - Delay execution
// ============================================
function debounce(fn, delay) {
  let timeoutId;
  
  return function(...args) {
    clearTimeout(timeoutId);
    
    timeoutId = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}

const searchAPI = debounce(function(query) {
  console.log("Searching for:", query);
  // API call here
}, 500);

// Chỉ gọi API sau khi dừng typing 500ms
searchAPI("java");
searchAPI("javasc");
searchAPI("javascript"); // Chỉ cái này được gọi

// ============================================
// 4. Throttle - Limit execution rate
// ============================================
function throttle(fn, limit) {
  let inThrottle;
  
  return function(...args) {
    if (!inThrottle) {
      fn.apply(this, args);
      inThrottle = true;
      
      setTimeout(() => {
        inThrottle = false;
      }, limit);
    }
  };
}

const handleScroll = throttle(function() {
  console.log("Scroll event handled");
}, 1000);

// Gọi tối đa 1 lần / 1000ms
window.addEventListener('scroll', handleScroll);

// ============================================
// 5. Once - Execute only once
// ============================================
function once(fn) {
  let called = false;
  let result;
  
  return function(...args) {
    if (!called) {
      called = true;
      result = fn.apply(this, args);
    }
    return result;
  };
}

const initializeApp = once(function() {
  console.log("App initialized");
  return { status: "initialized" };
});

initializeApp(); // "App initialized"
initializeApp(); // Không log gì (không chạy lại)

// ============================================
// 6. Compose - Kết hợp functions
// ============================================
function compose(...fns) {
  return function(value) {
    return fns.reduceRight((acc, fn) => fn(acc), value);
  };
}

const addOne = x => x + 1;
const double = x => x * 2;
const square = x => x * x;

const calculate = compose(square, double, addOne);
console.log(calculate(3)); // ((3 + 1) * 2)^2 = 64

// ============================================
// 7. Pipe - Giống compose nhưng left-to-right
// ============================================
function pipe(...fns) {
  return function(value) {
    return fns.reduce((acc, fn) => fn(acc), value);
  };
}

const transform = pipe(addOne, double, square);
console.log(transform(3)); // ((3 + 1) * 2)^2 = 64

// ============================================
// 8. Retry - Thử lại khi fail
// ============================================
function retry(fn, maxAttempts = 3) {
  return async function(...args) {
    for (let i = 0; i < maxAttempts; i++) {
      try {
        return await fn(...args);
      } catch (error) {
        if (i === maxAttempts - 1) {
          throw error;
        }
        console.log(`Attempt ${i + 1} failed, retrying...`);
        await new Promise(resolve => setTimeout(resolve, 1000));
      }
    }
  };
}

const unreliableAPI = retry(async function(url) {
  console.log("Calling API...");
  // Simulate random failure
  if (Math.random() < 0.7) {
    throw new Error("API Error");
  }
  return { data: "Success" };
}, 5);

// unreliableAPI("https://api.example.com");
```

### 4.5 Functional Programming Patterns

```javascript
// ============================================
// 1. Currying - Transform multi-arg function
// ============================================
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    } else {
      return function(...nextArgs) {
        return curried.apply(this, args.concat(nextArgs));
      };
    }
  };
}

function add(a, b, c) {
  return a + b + c;
}

const curriedAdd = curry(add);

console.log(curriedAdd(1)(2)(3));      // 6
console.log(curriedAdd(1, 2)(3));      // 6
console.log(curriedAdd(1)(2, 3));      // 6
console.log(curriedAdd(1, 2, 3));      // 6

// Practical use
const multiply = curry((a, b, c) => a * b * c);
const double = multiply(2);
const quadruple = double(2);

console.log(quadruple(5)); // 20

// ============================================
// 2. Partial Application
// ============================================
function partial(fn, ...presetArgs) {
  return function(...laterArgs) {
    return fn(...presetArgs, ...laterArgs);
  };
}

function greet(greeting, name) {
  return `${greeting}, ${name}!`;
}

const sayHello = partial(greet, "Hello");
const sayHi = partial(greet, "Hi");

console.log(sayHello("An"));   // "Hello, An!"
console.log(sayHi("Bình"));    // "Hi, Bình!"

// ============================================
// 3. Function Composition với Utilities
// ============================================
const map = fn => array => array.map(fn);
const filter = fn => array => array.filter(fn);
const reduce = (fn, init) => array => array.reduce(fn, init);

const data = [1, 2, 3, 4, 5, 6];

const processData = pipe(
  filter(x => x % 2 === 0),
  map(x => x * 2),
  reduce((sum, x) => sum + x, 0)
);

console.log(processData(data)); // 24 (2+4+6)*2

// ============================================
// 4. Predicates và Combinators
// ============================================
const isEven = x => x % 2 === 0;
const isPositive = x => x > 0;
const isLessThan10 = x => x < 10;

const and = (...predicates) => x => predicates.every(p => p(x));
const or = (...predicates) => x => predicates.some(p => p(x));
const not = predicate => x => !predicate(x);

const isEvenPositive = and(isEven, isPositive);
const isOddOrNegative = or(not(isEven), not(isPositive));

console.log([1, 2, 3, 4, -2].filter(isEvenPositive)); // [2, 4]
console.log([1, 2, 3, 4, -2].filter(isOddOrNegative)); // [1, 3, -2]
```

### 4.6 Real-World Examples

```javascript
// ============================================
// Example 1: Data Processing Pipeline
// ============================================
const orders = [
  { id: 1, user: "An", items: [{ price: 100 }, { price: 50 }], status: "completed" },
  { id: 2, user: "Bình", items: [{ price: 200 }], status: "completed" },
  { id: 3, user: "Chi", items: [{ price: 150 }], status: "pending" },
  { id: 4, user: "An", items: [{ price: 300 }, { price: 100 }], status: "completed" }
];

// Calculate total revenue from completed orders
const totalRevenue = orders
  .filter(order => order.status === "completed")
  .flatMap(order => order.items)
  .map(item => item.price)
  .reduce((sum, price) => sum + price, 0);

console.log("Total Revenue:", totalRevenue); // 750

// Get top customers
const customerTotals = orders
  .filter(order => order.status === "completed")
  .reduce((acc, order) => {
    const total = order.items.reduce((sum, item) => sum + item.price, 0);
    acc[order.user] = (acc[order.user] || 0) + total;
    return acc;
  }, {});

console.log("Customer Totals:", customerTotals);
// { An: 550, Bình: 200 }

// ============================================
// Example 2: Async Operations với HOFs
// ============================================
async function fetchWithRetry(url, maxRetries = 3) {
  const retry = async (attempt = 1) => {
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    } catch (error) {
      if (attempt >= maxRetries) throw error;
      console.log(`Retry ${attempt}/${maxRetries}`);
      await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
      return retry(attempt + 1);
    }
  };
  
  return retry();
}

// ============================================
// Example 3: Event Handler Management
// ============================================
class EventManager {
  constructor() {
    this.handlers = new Map();
  }
  
  on(event, handler) {
    if (!this.handlers.has(event)) {
      this.handlers.set(event, []);
    }
    this.handlers.get(event).push(handler);
    
    // Return unsubscribe function
    return () => {
      const handlers = this.handlers.get(event);
      const index = handlers.indexOf(handler);
      if (index > -1) {
        handlers.splice(index, 1);
      }
    };
  }
  
  once(event, handler) {
    const wrappedHandler = (...args) => {
      handler(...args);
      this.off(event, wrappedHandler);
    };
    return this.on(event, wrappedHandler);
  }
  
  off(event, handler) {
    const handlers = this.handlers.get(event);
    if (handlers) {
      const index = handlers.indexOf(handler);
      if (index > -1) {
        handlers.splice(index, 1);
      }
    }
  }
  
  emit(event, ...args) {
    const handlers = this.handlers.get(event);
    if (handlers) {
      handlers.forEach(handler => handler(...args));
    }
  }
}

// Usage
const events = new EventManager();

const unsubscribe = events.on('userLogin', (user) => {
  console.log(`${user} logged in`);
});

events.once('firstVisit', () => {
  console.log("Welcome!");
});

events.emit('userLogin', 'An');  // "An logged in"
events.emit('firstVisit');        // "Welcome!"
events.emit('firstVisit');        // (không log gì)

unsubscribe();
events.emit('userLogin', 'Bình'); // (không log gì)
```

### 4.7 Best Practices

```javascript
// ✅ GOOD: Pure functions (không side effects)
const addTax = (price, taxRate) => price * (1 + taxRate);
const total = addTax(100, 0.1); // 110

// ❌ BAD: Impure function (có side effects)
let globalTax = 0.1;
function addTaxBad(price) {
  return price * (1 + globalTax); // Phụ thuộc global state
}

// ✅ GOOD: Descriptive names
const filterAdults = users => users.filter(user => user.age >= 18);
const calculateAverage = numbers => numbers.reduce((a, b) => a + b, 0) / numbers.length;

// ❌ BAD: Unclear names
const fn1 = users => users.filter(u => u.age >= 18);
const fn2 = nums => nums.reduce((a, b) => a + b, 0) / nums.length;

// ✅ GOOD: Small, focused functions
const isAdult = user => user.age >= 18;
const getName = user => user.name;
const toUpperCase = str => str.toUpperCase();

const getAdultNames = users => users
  .filter(isAdult)
  .map(getName)
  .map(toUpperCase);

// ✅ GOOD: Avoid premature optimization
// Đơn giản, dễ đọc trước
const getActiveUsers = users => {
  return users.filter(user => user.isActive);
};

// Optimize sau nếu cần
const getActiveUsersMemo = memoize(users => {
  return users.filter(user => user.isActive);
});

// ✅ GOOD: Error handling trong HOFs
const safeDivide = (a, b) => {
  if (b === 0) {
    throw new Error("Division by zero");
  }
  return a / b;
};

const tryCatch = fn => {
  return (...args) => {
    try {
      return { success: true, data: fn(...args) };
    } catch (error) {
      return { success: false, error: error.message };
    }
  };
};

const safeDivideWithCatch = tryCatch(safeDivide);
console.log(safeDivideWithCatch(10, 2));  // { success: true, data: 5 }
console.log(safeDivideWithCatch(10, 0));  // { success: false, error: "..." }
```

---

## Tổng Kết

### Checklist Kiến Thức

- [ ] Hiểu sự khác biệt giữa Composition và Inheritance
- [ ] Biết khi nào dùng Composition, khi nào dùng Inheritance
- [ ] Nắm vững Type Coercion (Implicit và Explicit)
- [ ] Hiểu Pass by Value vs Pass by Reference
- [ ] Biết cách clone objects (Shallow vs Deep copy)
- [ ] Thành thạo các Array HOFs (map, filter, reduce, etc.)
- [ ] Tạo được custom Higher Order Functions
- [ ] Apply Functional Programming patterns

### Key Takeaways

1. **Composition > Inheritance**: Ưu tiên composition để có code linh hoạt hơn
2. **Type Coercion**: Luôn dùng strict equality (===) và explicit coercion
3. **Pass by Reference**: Cẩn thận khi modify objects, prefer immutability
4. **Higher Order Functions**: Sử dụng để tạo code reusable và declarative

### Bài Tập Tổng Hợp

Tạo một **E-commerce Product Management System**:

1. **Composition**: Tạo products với các behaviors khác nhau (discountable, shippable, digital)
2. **HOFs**: Implement filter, sort, và transform products
3. **Immutability**: Ensure không modify original data
4. **Type Safety**: Validate inputs và handle coercion correctly

### Tips Cuối Cùng

```javascript
// 1. Think in transformations
const data = fetchData()
  .then(parse)
  .then(validate)
  .then(transform)
  .then(save);

// 2. Compose small functions
const processUser = pipe(
  normalizeEmail,
  hashPassword,
  addTimestamp,
  saveToDb
);

// 3. Avoid mutations
const updated = { ...original, newField: "value" };

// 4. Use descriptive names
const filterActiveUsers = users => users.filter(u => u.active);

// 5. Handle errors gracefully
const safe = tryCatch(riskyFunction);
```

---

**Chúc bạn học tốt! 🚀**

*Remember: "Favor composition over inheritance" - Gang of Four*
