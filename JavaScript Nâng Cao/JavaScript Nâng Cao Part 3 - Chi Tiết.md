# JavaScript Nâng Cao Part 3 - Chi Tiết 📚

> **Mục tiêu**: Nắm vững Composition vs Inheritance, Type Coercion, Pass By Reference/Value, và Higher Order Functions
>
> **Đối tượng**: Sinh viên học lực trung bình khá
>
> **Thời gian**: 6-8 giờ học

---

## 📋 Mục Lục

1. [Composition vs Inheritance](#1-composition-vs-inheritance)
   - 1.1 Inheritance (Kế thừa) là gì?
   - 1.2 Vấn đề với Inheritance
   - 1.3 Composition (Kết hợp) là gì?
   - 1.4 So sánh Composition vs Inheritance
   - 1.5 Composition với Modern JavaScript
   - 1.6 Ví dụ thực tế: Game Characters
   - 1.7 Khi nào dùng Composition, khi nào dùng Inheritance?
   - 1.8 Best Practices
   - 🎯 Bài tập thực hành

2. [Type Coercion](#2-type-coercion)
   - 2.1 Type Coercion là gì?
   - 2.2 String Coercion
   - 2.3 Number Coercion
   - 2.4 Boolean Coercion
   - 2.5 Object to Primitive Coercion
   - 2.6 Comparison Operators và Coercion
   - 2.7 Các tình huống phức tạp
   - 2.8 Best Practices
   - 🎯 Bài tập thực hành

3. [Pass By Reference vs Pass By Value](#3-pass-by-reference-vs-pass-by-value)
   - 3.1 Primitive Types (Pass by Value)
   - 3.2 Objects (Pass by Reference)
   - 3.3 Function Arguments
   - 3.4 Reassignment vs Mutation
   - 3.5 Shallow Copy vs Deep Copy
   - 3.6 Preventing Modifications
   - 3.7 Best Practices
   - 🎯 Bài tập thực hành

4. [Higher Order Functions](#4-higher-order-functions)
   - 4.1 Higher Order Function là gì?
   - 4.2 Array Methods (Built-in HOFs)
   - 4.3 Chaining Array Methods
   - 4.4 Creating Custom HOFs
   - 4.5 Functional Programming Patterns
   - 4.6 Real-World Examples
   - 4.7 Best Practices
   - 🎯 Bài tập thực hành

5. [Tổng kết và Bài tập tổng hợp](#tong-ket)

---

## 1. Composition vs Inheritance

### 🤔 Tư Duy: Tại Sao Cần Composition?

Khi bạn code, bạn sẽ gặp tình huống:
- **Vấn đề**: Có nhiều loại objects với behaviors giống và khác nhau
- **Ví dụ**: Dog có thể `eat()` và `walk()`, Duck có thể `eat()`, `walk()`, `swim()`, và `fly()`

**Cách cũ (Inheritance)**:
```
Animal (eat, sleep)
  ├── Dog (walk, bark)
  ├── Cat (walk, meow)
  └── Bird (fly, chirp)
```

❌ **Vấn đề**: Nếu muốn tạo `Duck` vừa walk, vừa swim, vừa fly thì sao?
- Không thể kế thừa từ nhiều classes (no multiple inheritance)
- Phải copy-paste code → duplicate code

**Cách mới (Composition)**:
```
Behaviors: canEat, canWalk, canSwim, canFly
Duck = canEat + canWalk + canSwim + canFly
Dog = canEat + canWalk
Fish = canEat + canSwim
```

✅ **Lợi ích**:
- Linh hoạt: Tạo bất kỳ combination nào
- Reusable: Dùng lại behaviors
- Maintainable: Thay đổi behavior không ảnh hưởng khác

---

### 1.1 Inheritance (Kế thừa) là gì?

**Định nghĩa**: Inheritance cho phép class con kế thừa properties và methods từ class cha.

#### 📌 Ví Dụ Cơ Bản

```javascript
// Class cha
class Animal {
  constructor(name) {
    this.name = name;
    this.energy = 100;
  }

  eat(food) {
    console.log(`${this.name} đang ăn ${food}`);
    this.energy += 10;
  }

  sleep() {
    console.log(`${this.name} đang ngủ`);
    this.energy += 20;
  }

  getStatus() {
    console.log(`${this.name} có ${this.energy} năng lượng`);
  }
}

// Class con kế thừa từ Animal
class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Gọi constructor của class cha
    this.breed = breed;
  }

  bark() {
    console.log(`${this.name} sủa: Gâu gâu!`);
    this.energy -= 5;
  }

  fetch() {
    console.log(`${this.name} đuổi theo bóng`);
    this.energy -= 10;
  }
}

class Cat extends Animal {
  constructor(name, color) {
    super(name);
    this.color = color;
  }

  meow() {
    console.log(`${this.name} kêu: Meo meo!`);
    this.energy -= 3;
  }

  climb() {
    console.log(`${this.name} leo cây`);
    this.energy -= 8;
  }
}

// Sử dụng
const dog = new Dog("Milu", "Corgi");
dog.eat("thịt");        // Kế thừa từ Animal ✅
dog.bark();             // Method của Dog ✅
dog.getStatus();        // Kế thừa từ Animal ✅

const cat = new Cat("Kitty", "white");
cat.eat("cá");          // Kế thừa từ Animal ✅
cat.meow();             // Method của Cat ✅
cat.climb();            // Method của Cat ✅
```

**Output**:
```
Milu đang ăn thịt
Milu sủa: Gâu gâu!
Milu có 105 năng lượng
Kitty đang ăn cá
Kitty kêu: Meo meo!
Kitty leo cây
```

#### 💡 Giải Thích

```
Memory Layout:

dog object:
┌─────────────────┐
│ name: "Milu"    │ ← from Animal
│ energy: 105     │ ← from Animal
│ breed: "Corgi"  │ ← from Dog
├─────────────────┤
│ eat()           │ ← inherited
│ sleep()         │ ← inherited
│ getStatus()     │ ← inherited
│ bark()          │ ← own method
│ fetch()         │ ← own method
└─────────────────┘

Prototype chain:
dog → Dog.prototype → Animal.prototype → Object.prototype → null
```

---

### 1.2 Vấn Đề với Inheritance

#### ❌ Vấn đề 1: Hierarchy Cứng Nhắc (Rigid Hierarchy)

```javascript
class Vehicle {
  constructor(name) {
    this.name = name;
    this.speed = 0;
  }

  move() {
    console.log(`${this.name} đang di chuyển với tốc độ ${this.speed}km/h`);
  }
}

class Car extends Vehicle {
  drive() {
    this.speed = 60;
    console.log(`${this.name} đang lái trên đường`);
  }
}

class Boat extends Vehicle {
  sail() {
    this.speed = 30;
    console.log(`${this.name} đang đi trên nước`);
  }
}

class Airplane extends Vehicle {
  fly() {
    this.speed = 500;
    console.log(`${this.name} đang bay`);
  }
}

// 🤔 Vấn đề: Nếu muốn có AmphibiousCar (xe lội nước)?
// Nó cần cả drive() và sail()
// ❌ Không thể: class AmphibiousCar extends Car, Boat
// JavaScript không support multiple inheritance!

// 😢 Giải pháp tệ: Copy-paste code
class AmphibiousCar extends Vehicle {
  drive() {
    this.speed = 60;
    console.log(`${this.name} đang lái trên đường`);
  }

  sail() {  // ❌ Duplicate code từ Boat
    this.speed = 30;
    console.log(`${this.name} đang đi trên nước`);
  }
}
```

**💭 Tại sao đây là vấn đề?**
- Nếu thay đổi `sail()` trong `Boat`, phải nhớ thay đổi trong `AmphibiousCar`
- Code duplication → Hard to maintain
- Không scale: Nếu có 10 combinations → Phải tạo 10 classes với duplicate code

---

#### ❌ Vấn đề 2: Tight Coupling (Liên Kết Chặt)

```javascript
class Employee {
  constructor(name, salary) {
    this.name = name;
    this.salary = salary;
    this.workHours = 0;
  }

  work() {
    this.workHours += 8;
    console.log(`${this.name} đã làm việc ${this.workHours} giờ`);
  }

  getSalary() {
    return this.salary + (this.workHours * 10); // Bonus theo giờ
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

  // Manager cũng có getSalary từ Employee
}

const manager = new Manager("An", 5000, "Development");
console.log(manager.getSalary()); // 5000 (chưa work)

manager.work();
console.log(manager.getSalary()); // 5080

// 🤔 Vấn đề: Nếu thay đổi cách tính lương trong Employee
// → Manager cũng bị ảnh hưởng!

// ❌ Ví dụ: Thay đổi Employee
class Employee {
  // ...
  getSalary() {
    // Đổi công thức
    return this.salary * 1.1; // Thêm 10% bonus
    // ❌ Mất phần tính theo workHours!
  }
}

// Manager giờ cũng dùng công thức mới
// → Có thể không phù hợp với yêu cầu business!
```

**💭 Tại sao đây là vấn đề?**
- Child class phụ thuộc hoàn toàn vào parent class
- Thay đổi parent → Có thể break child classes
- Hard to test: Phải test cả parent và child cùng lúc

---

#### ❌ Vấn đề 3: Gorilla/Banana Problem

> "Bạn muốn một quả chuối nhưng phải lấy cả con gorilla cầm chuối và cả khu rừng" - Joe Armstrong (Creator of Erlang)

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat() { /* ... */ }
  sleep() { /* ... */ }
  breathe() { /* ... */ }
  reproduce() { /* ... */ }
  makeSound() { /* ... */ }
  move() { /* ... */ }
  hunt() { /* ... */ }
  defend() { /* ... */ }
  communicate() { /* ... */ }
  // ... 50 methods khác
}

class Bird extends Animal {
  fly() {
    console.log(`${this.name} đang bay`);
  }
}

// 🤔 Vấn đề: Bird kế thừa TẤT CẢ methods từ Animal
// Kể cả những methods không cần:
// - hunt()? Không phải tất cả birds đều hunt
// - defend()? Cách defend của bird khác mammals

const penguin = new Bird("Penguin");
penguin.fly(); // ❌ Penguins không bay!

// Giải pháp tệ: Override
class Penguin extends Bird {
  fly() {
    throw new Error("Penguins can't fly!");
  }
}

// ❌ Liskov Substitution Principle bị vi phạm
// Bird promises fly(), nhưng Penguin breaks that promise
```

**💭 Tại sao đây là vấn đề?**
- Kế thừa quá nhiều thứ không cần thiết
- Object size lớn hơn cần thiết
- API unclear: Methods nào work, methods nào throw error?

---

### 1.3 Composition (Kết hợp) là gì?

**Định nghĩa**: Composition là kỹ thuật xây dựng objects phức tạp từ các objects/functions nhỏ hơn, độc lập.

**Triết lý**: "Has-a" relationship thay vì "Is-a" relationship
- Inheritance: Dog **IS-A** Animal
- Composition: Dog **HAS** eating behavior, **HAS** walking behavior

#### 📌 Ví Dụ Cơ Bản

```javascript
// Factory functions cho behaviors (mỗi behavior là một piece)
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

// Compose function - Kết hợp các pieces lại
const compose = (...fns) => (obj) => {
  return fns.reduce((acc, fn) => {
    return { ...acc, ...fn(obj) };
  }, obj);
};

// Tạo các animals khác nhau bằng cách kết hợp behaviors
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

// ✅ Sử dụng
const dog = createDog("Milu");
dog.eat("thịt");     // ✅ Works
dog.walk();          // ✅ Works
// dog.fly();        // ❌ undefined - không có method này

const duck = createDuck("Donald");
duck.eat("gạo");     // ✅ Works
duck.walk();         // ✅ Works
duck.swim();         // ✅ Works
duck.fly();          // ✅ Works

const fish = createFish("Nemo");
fish.eat("tảo");     // ✅ Works
fish.swim();         // ✅ Works
// fish.walk();      // ❌ undefined - không có method này

console.log(dog.energy);  // 105 (100 + 10 - 5)
console.log(duck.energy); // 97 (100 + 10 - 5 - 3 - 8)
```

**Output**:
```
Milu đang ăn thịt
Milu đang đi bộ
Donald đang ăn gạo
Donald đang đi bộ
Donald đang bơi
Donald đang bay
Nemo đang ăn tảo
Nemo đang bơi
```

#### 💡 Giải Thích

```
Composition Strategy:

1. Tách behaviors thành các functions nhỏ
   canEat ───┐
   canWalk ──┤
   canSwim ──┼─→ compose() → Complete Object
   canFly ───┘

2. Mỗi behavior là independent
   - canEat không biết về canWalk
   - canSwim không biết về canFly
   - Loosely coupled ✅

3. Kết hợp tự do
   Dog = canEat + canWalk
   Duck = canEat + canWalk + canSwim + canFly
   Fish = canEat + canSwim
   AmphibiousCar = canDrive + canSail ← Easy to add!
```

---

### 1.4 So Sánh Composition vs Inheritance

#### 📊 Side-by-Side Comparison

```javascript
// ============================================
// ❌ INHERITANCE APPROACH
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

// ❌ Vấn đề: Không thể tạo vehicle vừa bay vừa đi nước
// const seaplane = ???
// Không thể: class Seaplane extends FlyingVehicle, WaterVehicle

// ============================================
// ✅ COMPOSITION APPROACH
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

// ✅ Flexible: Tạo bất kỳ combination nào
function createAirplane(name) {
  const state = { name };
  return Object.assign(state,
    withMovement(state),
    withFlying(state)
  );
}

function createBoat(name) {
  const state = { name };
  return Object.assign(state,
    withMovement(state),
    withSailing(state)
  );
}

function createCar(name) {
  const state = { name };
  return Object.assign(state,
    withMovement(state),
    withDriving(state)
  );
}

function createAmphibiousCar(name) {
  const state = { name };
  return Object.assign(
    state,
    withMovement(state),
    withDriving(state),
    withSailing(state) // ✅ Easy! Just add behavior
  );
}

function createFlyingCar(name) {
  const state = { name };
  return Object.assign(
    state,
    withMovement(state),
    withDriving(state),
    withFlying(state) // ✅ Easy! Just add behavior
  );
}

function createSeaplane(name) {
  const state = { name };
  return Object.assign(
    state,
    withMovement(state),
    withFlying(state),
    withSailing(state) // ✅ Impossible with inheritance!
  );
}

// Sử dụng
const flyingCar = createFlyingCar("DeLorean");
flyingCar.move();    // ✅
flyingCar.drive();   // ✅
flyingCar.fly();     // ✅
// flyingCar.sail(); // ❌ undefined - không có

const seaplane = createSeaplane("Icon A5");
seaplane.fly();      // ✅
seaplane.sail();     // ✅
// seaplane.drive(); // ❌ undefined - không có
```

#### 📋 Comparison Table

| **Aspect** | **Inheritance** | **Composition** |
|------------|-----------------|-----------------|
| **Relationship** | "Is-a" (Dog **is an** Animal) | "Has-a" (Dog **has** eating behavior) |
| **Flexibility** | ❌ Rigid hierarchy | ✅ Mix & match behaviors |
| **Multiple inheritance** | ❌ Not supported in JS | ✅ Easy to combine multiple behaviors |
| **Code reuse** | ⚠️ Reuse via parent classes | ✅ Reuse individual behaviors |
| **Coupling** | ❌ Tight (child depends on parent) | ✅ Loose (behaviors independent) |
| **Maintenance** | ❌ Hard (changes ripple down) | ✅ Easy (change one behavior) |
| **Testing** | ❌ Must test parent + child | ✅ Test behaviors independently |
| **Learning curve** | ✅ Easier for beginners | ⚠️ Requires understanding FP concepts |

---

### 1.5 Composition với Modern JavaScript

#### 📌 Sử Dụng Mixins

```javascript
// Mixin là object chứa methods có thể "mix" vào classes khác
const EaterMixin = {
  eat(food) {
    console.log(`${this.name} ăn ${food}`);
    this.energy = (this.energy || 100) + 10;
  },

  drink(beverage) {
    console.log(`${this.name} uống ${beverage}`);
    this.energy = (this.energy || 100) + 5;
  }
};

const WalkerMixin = {
  walk(distance) {
    console.log(`${this.name} đi bộ ${distance}m`);
    this.energy = (this.energy || 100) - Math.floor(distance / 10);
  },

  run(distance) {
    console.log(`${this.name} chạy ${distance}m`);
    this.energy = (this.energy || 100) - Math.floor(distance / 5);
  }
};

const SpeakerMixin = {
  speak(message) {
    console.log(`${this.name} nói: "${message}"`);
  },

  shout(message) {
    console.log(`${this.name} hét: "${message.toUpperCase()}!"`);
  }
};

// Helper function để apply mixins vào class
function mixin(targetClass, ...mixins) {
  mixins.forEach(mixinObj => {
    Object.assign(targetClass.prototype, mixinObj);
  });
}

// Tạo class và apply mixins
class Person {
  constructor(name) {
    this.name = name;
    this.energy = 100;
  }

  getStatus() {
    console.log(`${this.name} có ${this.energy} năng lượng`);
  }
}

// Apply tất cả mixins vào Person
mixin(Person, EaterMixin, WalkerMixin, SpeakerMixin);

// Sử dụng
const person = new Person("An");
person.eat("cơm");           // From EaterMixin ✅
person.drink("nước");        // From EaterMixin ✅
person.walk(100);            // From WalkerMixin ✅
person.speak("Xin chào!");   // From SpeakerMixin ✅
person.getStatus();          // From Person ✅

// Tạo class khác với subset của mixins
class Robot {
  constructor(name) {
    this.name = name;
    this.energy = 200;
  }
}

// Robot chỉ cần WalkerMixin và SpeakerMixin
mixin(Robot, WalkerMixin, SpeakerMixin);

const robot = new Robot("R2D2");
robot.walk(50);
robot.shout("beep boop");
// robot.eat("oil"); // ❌ TypeError - không có method eat()
```

**Output**:
```
An ăn cơm
An uống nước
An đi bộ 100m
An nói: "Xin chào!"
An có 105 năng lượng
R2D2 đi bộ 50m
R2D2 hét: "BEEP BOOP!"
```

#### 💡 Advanced Mixin Pattern

```javascript
// Mixin factory cho flexibility cao hơn
const createEaterMixin = (energyGain = 10) => ({
  eat(food) {
    console.log(`${this.name} ăn ${food}`);
    this.energy += energyGain;
  }
});

const createWalkerMixin = (energyCost = 5) => ({
  walk(distance) {
    console.log(`${this.name} đi ${distance}m`);
    this.energy -= energyCost * (distance / 100);
  }
});

// Tạo classes với different configurations
class Athlete {
  constructor(name) {
    this.name = name;
    this.energy = 150;
  }
}

class Child {
  constructor(name) {
    this.name = name;
    this.energy = 80;
  }
}

// Athlete: High energy gain from eating, low energy cost for walking
Object.assign(Athlete.prototype,
  createEaterMixin(20),  // High energy gain
  createWalkerMixin(3)   // Low energy cost
);

// Child: Normal energy gain, high energy cost for walking
Object.assign(Child.prototype,
  createEaterMixin(10),  // Normal energy gain
  createWalkerMixin(10)  // High energy cost
);

const athlete = new Athlete("Ronaldo");
athlete.eat("pasta");
athlete.walk(1000);
console.log(`Energy: ${athlete.energy}`); // 150 + 20 - 30 = 140

const child = new Child("Minh");
child.eat("snack");
child.walk(1000);
console.log(`Energy: ${child.energy}`); // 80 + 10 - 100 = -10 (tired!)
```

---

### 1.6 Ví Dụ Thực Tế: Game Characters

Hãy xây dựng hệ thống characters cho một RPG game.

#### ❌ Cách Tệ: Dùng Inheritance

```javascript
class Character {
  constructor(name, health) {
    this.name = name;
    this.health = health;
    this.maxHealth = health;
  }

  takeDamage(damage) {
    this.health = Math.max(0, this.health - damage);
    console.log(`${this.name} nhận ${damage} sát thương. HP: ${this.health}/${this.maxHealth}`);
  }

  isDead() {
    return this.health <= 0;
  }
}

class Warrior extends Character {
  constructor(name, health, weapon) {
    super(name, health);
    this.weapon = weapon;
  }

  attack(target) {
    const damage = this.weapon.damage || 20;
    console.log(`${this.name} tấn công ${target.name}!`);
    target.takeDamage(damage);
  }
}

class Mage extends Character {
  constructor(name, health, mana) {
    super(name, health);
    this.mana = mana;
    this.maxMana = mana;
  }

  castSpell(spellName, target) {
    const manaCost = 10;

    if (this.mana >= manaCost) {
      this.mana -= manaCost;
      const damage = 50;
      console.log(`${this.name} dùng ${spellName}!`);
      target.takeDamage(damage);
    } else {
      console.log(`${this.name} không đủ mana!`);
    }
  }
}

// ❌ Vấn đề: Không thể tạo BattleMage (vừa attack vừa castSpell)
// class BattleMage extends Warrior, Mage // ❌ Syntax error!

// Giải pháp tệ: Duplicate code
class BattleMage extends Character {
  constructor(name, health, weapon, mana) {
    super(name, health);
    this.weapon = weapon;
    this.mana = mana;
    this.maxMana = mana;
  }

  // ❌ Copy-paste từ Warrior
  attack(target) {
    const damage = this.weapon.damage || 20;
    console.log(`${this.name} tấn công ${target.name}!`);
    target.takeDamage(damage);
  }

  // ❌ Copy-paste từ Mage
  castSpell(spellName, target) {
    const manaCost = 10;

    if (this.mana >= manaCost) {
      this.mana -= manaCost;
      const damage = 50;
      console.log(`${this.name} dùng ${spellName}!`);
      target.takeDamage(damage);
    } else {
      console.log(`${this.name} không đủ mana!`);
    }
  }
}
```

#### ✅ Cách Tốt: Dùng Composition

```javascript
// Behaviors (Pure functions)
const hasHealth = (state) => ({
  takeDamage(damage) {
    state.health = Math.max(0, state.health - damage);
    console.log(`${state.name} nhận ${damage} sát thương. HP: ${state.health}/${state.maxHealth}`);

    if (state.health === 0) {
      console.log(`💀 ${state.name} đã chết!`);
    }
  },

  heal(amount) {
    const oldHealth = state.health;
    state.health = Math.min(state.maxHealth, state.health + amount);
    const healed = state.health - oldHealth;
    console.log(`❤️ ${state.name} hồi ${healed} HP. HP: ${state.health}/${state.maxHealth}`);
  },

  isDead() {
    return state.health <= 0;
  },

  getHealthPercent() {
    return (state.health / state.maxHealth) * 100;
  }
});

const canAttack = (state) => ({
  attack(target) {
    const damage = state.attackPower || 10;
    console.log(`⚔️ ${state.name} tấn công ${target.name} gây ${damage} sát thương!`);
    target.takeDamage(damage);

    // Lifesteal nếu có
    if (state.lifesteal) {
      const healAmount = Math.floor(damage * state.lifesteal);
      console.log(`🩸 ${state.name} hút ${healAmount} HP`);
      this.heal(healAmount);
    }
  }
});

const canCastSpells = (state) => ({
  castSpell(spellName, target) {
    const spell = state.spells[spellName];

    if (!spell) {
      console.log(`❌ ${state.name} không biết phép ${spellName}!`);
      return;
    }

    if (state.mana < spell.manaCost) {
      console.log(`❌ ${state.name} không đủ mana! (Còn ${state.mana}/${state.maxMana})`);
      return;
    }

    state.mana -= spell.manaCost;
    console.log(`✨ ${state.name} dùng ${spellName}! Mana: ${state.mana}/${state.maxMana}`);

    if (spell.damage) {
      target.takeDamage(spell.damage);
    }

    if (spell.heal) {
      this.heal(spell.heal);
    }
  },

  restoreMana(amount) {
    const oldMana = state.mana;
    state.mana = Math.min(state.maxMana, state.mana + amount);
    const restored = state.mana - oldMana;
    console.log(`💙 ${state.name} hồi ${restored} mana. Mana: ${state.mana}/${state.maxMana}`);
  }
});

const canDefend = (state) => ({
  defend() {
    state.isDefending = true;
    state.defenseMultiplier = 0.5; // Giảm 50% damage
    console.log(`🛡️ ${state.name} đang phòng thủ (giảm 50% sát thương)`);
  },

  stopDefending() {
    state.isDefending = false;
    state.defenseMultiplier = 1;
    console.log(`${state.name} ngừng phòng thủ`);
  }
});

const canRage = (state) => ({
  rage() {
    if (state.isRaging) {
      console.log(`${state.name} đã đang trong trạng thái Rage!`);
      return;
    }

    state.isRaging = true;
    state.originalAttackPower = state.attackPower;
    state.attackPower *= 2; // Double damage
    console.log(`😡 ${state.name} vào trạng thái Rage! Sát thương x2!`);

    // Rage kéo dài 3 turns
    setTimeout(() => {
      state.isRaging = false;
      state.attackPower = state.originalAttackPower;
      console.log(`${state.name} hết Rage`);
    }, 3000);
  }
});

// Factory functions
function createWarrior(name) {
  const state = {
    name,
    health: 150,
    maxHealth: 150,
    attackPower: 25,
    lifesteal: 0.2, // Hút 20% HP
    isDefending: false,
    defenseMultiplier: 1
  };

  return Object.assign(
    state,
    hasHealth(state),
    canAttack(state),
    canDefend(state),
    canRage(state)
  );
}

function createMage(name) {
  const state = {
    name,
    health: 100,
    maxHealth: 100,
    mana: 150,
    maxMana: 150,
    spells: {
      fireball: { manaCost: 20, damage: 60 },
      lightning: { manaCost: 30, damage: 80 },
      heal: { manaCost: 25, heal: 50 },
      blizzard: { manaCost: 50, damage: 120 }
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
    health: 120,
    maxHealth: 120,
    mana: 100,
    maxMana: 100,
    attackPower: 18,
    spells: {
      fireball: { manaCost: 15, damage: 45 },
      enchantWeapon: { manaCost: 20, damage: 0 } // Buff
    },
    isDefending: false,
    defenseMultiplier: 1
  };

  return Object.assign(
    state,
    hasHealth(state),
    canAttack(state),
    canCastSpells(state),
    canDefend(state)
  );
}

function createPaladin(name) {
  const state = {
    name,
    health: 180,
    maxHealth: 180,
    mana: 80,
    maxMana: 80,
    attackPower: 20,
    spells: {
      heal: { manaCost: 20, heal: 40 },
      divineShield: { manaCost: 30, damage: 0 }
    },
    isDefending: false,
    defenseMultiplier: 1
  };

  return Object.assign(
    state,
    hasHealth(state),
    canAttack(state),
    canCastSpells(state),
    canDefend(state)
  );
}

// ✅ Test game
console.log("=== BATTLE START ===\n");

const warrior = createWarrior("Conan");
const mage = createMage("Gandalf");
const battleMage = createBattleMage("Merlin");
const paladin = createPaladin("Arthas");

// Round 1
warrior.attack(mage);
mage.castSpell("fireball", warrior);
battleMage.attack(mage);
battleMage.castSpell("fireball", warrior);

console.log("\n");

// Round 2
warrior.rage(); // Activate rage
warrior.attack(mage);
mage.castSpell("heal", mage);
paladin.defend();
battleMage.attack(paladin);

console.log("\n");

// Round 3
warrior.attack(mage);
// mage.castSpell("blizzard", warrior); // Would kill warrior
paladin.stopDefending();
paladin.castSpell("heal", paladin);
```

**Output mẫu**:
```
=== BATTLE START ===

⚔️ Conan tấn công Gandalf gây 25 sát thương!
Gandalf nhận 25 sát thương. HP: 75/100
🩸 Conan hút 5 HP
❤️ Conan hồi 5 HP. HP: 150/150
✨ Gandalf dùng fireball! Mana: 130/150
Conan nhận 60 sát thương. HP: 90/150
⚔️ Merlin tấn công Gandalf gây 18 sát thương!
Gandalf nhận 18 sát thương. HP: 57/100
✨ Merlin dùng fireball! Mana: 85/100
Conan nhận 45 sát thương. HP: 45/150

😡 Conan vào trạng thái Rage! Sát thương x2!
⚔️ Conan tấn công Gandalf gây 50 sát thương!
Gandalf nhận 50 sát thương. HP: 7/100
🩸 Conan hút 10 HP
❤️ Conan hồi 10 HP. HP: 55/150
✨ Gandalf dùng heal! Mana: 105/150
❤️ Gandalf hồi 50 HP. HP: 57/100
🛡️ Arthas đang phòng thủ (giảm 50% sát thương)
⚔️ Merlin tấn công Arthas gây 18 sát thương!
Arthas nhận 9 sát thương. HP: 171/180

⚔️ Conan tấn công Gandalf gây 50 sát thương!
Gandalf nhận 50 sát thương. HP: 7/100
💀 Gandalf đã chết!
...
```

#### 💡 Lợi Ích của Composition trong Game

1. **Easy to add new character types**:
   ```javascript
   // Necromancer = Mage + Can summon
   const canSummon = (state) => ({
     summon(creatureName) {
       console.log(`${state.name} triệu hồi ${creatureName}!`);
       // Implementation
     }
   });

   function createNecromancer(name) {
     const state = { /* ... */ };
     return Object.assign(state,
       hasHealth(state),
       canCastSpells(state),
       canSummon(state) // ✅ Easy to add!
     );
   }
   ```

2. **Easy to test behaviors independently**:
   ```javascript
   // Test canAttack behavior
   const mockState = { name: "Test", attackPower: 10 };
   const attacker = canAttack(mockState);

   const mockTarget = { takeDamage: jest.fn() };
   attacker.attack(mockTarget);

   expect(mockTarget.takeDamage).toHaveBeenCalledWith(10);
   ```

3. **Easy to modify behaviors**:
   ```javascript
   // Nếu muốn thay đổi attack formula
   // Chỉ sửa canAttack, tất cả characters đều được update
   const canAttack = (state) => ({
     attack(target) {
       // New formula: Critical hit 10% chance
       const isCrit = Math.random() < 0.1;
       const damage = state.attackPower * (isCrit ? 2 : 1);

       if (isCrit) console.log("💥 CRITICAL HIT!");
       // ...
     }
   });
   ```

---

### 1.7 Khi Nào Dùng Composition, Khi Nào Dùng Inheritance?

#### ✅ Dùng INHERITANCE khi:

**1. Có relationship "IS-A" rõ ràng và không thay đổi**

```javascript
class Shape {
  constructor(color) {
    this.color = color;
  }

  getArea() {
    throw new Error("getArea() must be implemented");
  }

  describe() {
    return `A ${this.color} shape with area ${this.getArea()}`;
  }
}

class Circle extends Shape {
  constructor(color, radius) {
    super(color);
    this.radius = radius;
  }

  getArea() {
    return Math.PI * this.radius ** 2;
  }
}

class Rectangle extends Shape {
  constructor(color, width, height) {
    super(color);
    this.width = width;
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }
}

// ✅ Circle IS-A Shape - Makes sense
// ✅ Rectangle IS-A Shape - Makes sense
// ✅ Hierarchy rõ ràng, không thay đổi

const circle = new Circle("red", 5);
console.log(circle.describe()); // "A red shape with area 78.54..."

const rect = new Rectangle("blue", 4, 6);
console.log(rect.describe()); // "A blue shape with area 24"
```

**2. Hierarchy đơn giản, shallow (không sâu)**

```javascript
class Vehicle {
  constructor(brand) {
    this.brand = brand;
  }
}

class Car extends Vehicle {
  constructor(brand, model) {
    super(brand);
    this.model = model;
  }
}

// ✅ OK: Chỉ 2 levels
// ❌ BAD: Vehicle → Car → SportsCar → Ferrari → F40 (quá nhiều levels)
```

**3. Framework/Library yêu cầu**

```javascript
// React Class Components
class MyComponent extends React.Component {
  render() {
    return <div>Hello</div>;
  }
}

// ✅ Bắt buộc phải extend React.Component
```

---

#### ✅ Dùng COMPOSITION khi:

**1. Cần flexibility cao, nhiều combinations**

```javascript
// ✅ Composition: Mix & match features
const withLogging = (service) => ({
  ...service,
  log(message) {
    console.log(`[${new Date().toISOString()}] ${message}`);
  }
});

const withRetry = (service) => ({
  ...service,
  async sendWithRetry(data, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
      try {
        return await service.send(data);
      } catch (error) {
        if (i === maxRetries - 1) throw error;
        console.log(`Retry ${i + 1}/${maxRetries}...`);
        await new Promise(r => setTimeout(r, 1000));
      }
    }
  }
});

const withValidation = (service) => ({
  ...service,
  validateAndSend(data) {
    if (!data.to || !data.subject) {
      throw new Error("Missing required fields");
    }
    return service.send(data);
  }
});

const withEncryption = (service) => ({
  ...service,
  sendEncrypted(data) {
    const encrypted = encrypt(data); // Assume encrypt function exists
    return service.send(encrypted);
  }
});

// Base service
const basicEmailService = {
  send(email) {
    console.log(`Sending email to ${email.to}`);
    return Promise.resolve({ success: true });
  }
};

// ✅ Tạo different combinations dễ dàng
const emailService = withValidation(
  withRetry(
    withLogging(basicEmailService)
  )
);

const secureEmailService = withEncryption(
  withValidation(
    withLogging(basicEmailService)
  )
);

// Easy to add/remove features
const simpleEmailService = withLogging(basicEmailService);
```

**2. Has-a relationship thay vì Is-a**

```javascript
// ❌ BAD: Using inheritance for "has-a"
class Car extends Engine { } // ❌ Car IS-AN Engine? No!

// ✅ GOOD: Using composition
class Car {
  constructor() {
    this.engine = new Engine();     // Car HAS-A Engine ✅
    this.wheels = [new Wheel(), ...]; // Car HAS Wheels ✅
  }

  start() {
    this.engine.start();
  }
}
```

**3. Muốn tái sử dụng behaviors across unrelated classes**

```javascript
// Behaviors có thể dùng cho nhiều types
const withTimestamps = (obj) => ({
  ...obj,
  createdAt: Date.now(),
  updatedAt: Date.now(),

  touch() {
    this.updatedAt = Date.now();
  }
});

const withId = (obj) => ({
  ...obj,
  id: Math.random().toString(36).substr(2, 9)
});

// Dùng cho User
const user = withId(withTimestamps({ name: "An", email: "an@example.com" }));

// Dùng cho Product
const product = withId(withTimestamps({ name: "Laptop", price: 1000 }));

// Dùng cho Order
const order = withId(withTimestamps({ userId: user.id, total: 1000 }));

// ✅ User, Product, Order không related
// Nhưng đều có id và timestamps!
```

---

### 1.8 Best Practices

#### ✅ DO's

```javascript
// 1. Pure functions cho composition
const withDiscount = (product) => ({
  ...product,
  discountedPrice: product.price * 0.9,

  applyDiscount(percent) {
    return {
      ...product,
      discountedPrice: product.price * (1 - percent / 100)
    };
  }
});

// 2. Small, focused behaviors
const canLog = (state) => ({
  log(message) {
    console.log(`[${state.name}] ${message}`);
  }
});

const canSaveToDb = (state) => ({
  async save() {
    await db.save(state);
  }
});

// 3. Use pipe/compose for clarity
const pipe = (...fns) => (value) => {
  return fns.reduce((acc, fn) => fn(acc), value);
};

const enhance = pipe(
  withId,
  withTimestamps,
  withValidation
);

const user = enhance({ name: "An", email: "an@example.com" });

// 4. Descriptive names
const canFly = (state) => ({ /* ... */ });        // ✅ Clear
const canSwim = (state) => ({ /* ... */ });       // ✅ Clear
const withLogging = (obj) => ({ /* ... */ });     // ✅ Clear

// 5. Document complex compositions
/**
 * Creates an admin user with full permissions
 * Combines: authentication, authorization, logging, and audit trail
 */
function createAdminUser(name, email) {
  const state = { name, email, role: "admin" };

  return Object.assign(state,
    withAuth(state),        // Adds login/logout
    withPermissions(state), // Adds can() check
    withLogging(state),     // Adds log()
    withAudit(state)        // Adds audit trail
  );
}
```

#### ❌ DON'Ts

```javascript
// ❌ 1. Deep inheritance hierarchy
class A { }
class B extends A { }
class C extends B { }
class D extends C { }
class E extends D { } // Too deep!

// ✅ Use composition instead
const featureA = (obj) => ({ /* ... */ });
const featureB = (obj) => ({ /* ... */ });
const featureC = (obj) => ({ /* ... */ });

const createE = () => compose(featureA, featureB, featureC)({});

// ❌ 2. Modify objects in place (mutations)
const badWithDiscount = (product) => {
  product.discountedPrice = product.price * 0.9; // ❌ Mutates!
  return product;
};

// ✅ Return new object
const goodWithDiscount = (product) => ({
  ...product,
  discountedPrice: product.price * 0.9
});

// ❌ 3. Complex, hard-to-understand compositions
const confusing = pipe(
  fn1, fn2, fn3, fn4, fn5, fn6, fn7, fn8, fn9, fn10 // Too many!
);

// ✅ Break into smaller, named steps
const step1 = pipe(fn1, fn2, fn3);
const step2 = pipe(fn4, fn5, fn6);
const step3 = pipe(fn7, fn8);

const clear = pipe(step1, step2, step3);

// ❌ 4. Naming conflicts
const withName = (obj) => ({
  ...obj,
  name: "Default"
});

const withId = (obj) => ({
  ...obj,
  name: "ID-123" // ❌ Conflicts with withName!
});

// ✅ Use unique property names
const withDisplayName = (obj) => ({
  ...obj,
  displayName: "Default"
});

const withIdString = (obj) => ({
  ...obj,
  idString: "ID-123"
});
```

---

### 🎯 Bài Tập 1: Composition vs Inheritance

#### Bài 1: E-Commerce Product System

**Yêu cầu**: Tạo hệ thống products với các features:
- **Physical products**: Có weight, shipping cost
- **Digital products**: Có downloadUrl, fileSize
- **Discountable products**: Có thể apply discount
- **Taxable products**: Có thể tính tax
- **Combo products**: Vừa Physical + Digital (như game boxed với CD key)

<details>
<summary>💡 Gợi ý</summary>

1. Tạo các behaviors:
   - `withPhysicalShipping(state)` - Adds weight, calculateShipping()
   - `withDigitalDownload(state)` - Adds downloadUrl, getDownloadLink()
   - `withDiscount(state)` - Adds applyDiscount()
   - `withTax(state)` - Adds calculateTax()

2. Compose cho từng loại product:
   - PhysicalProduct = base + withPhysicalShipping + withDiscount + withTax
   - DigitalProduct = base + withDigitalDownload + withDiscount
   - ComboProduct = base + withPhysicalShipping + withDigitalDownload + withDiscount + withTax

3. Test với:
   ```javascript
   const book = createPhysicalProduct("Book", 20, 0.5);
   const ebook = createDigitalProduct("eBook", 10, "https://...");
   const game = createComboProduct("Game", 60, 1.0, "https://...");
   ```

</details>

<details>
<summary>✅ Giải pháp đầy đủ</summary>

```javascript
// Behaviors
const withPhysicalShipping = (state) => ({
  weight: state.weight,

  calculateShipping() {
    const baseRate = 5;
    const weightRate = 2;
    return baseRate + (this.weight * weightRate);
  },

  getTotalPrice() {
    return state.price + this.calculateShipping();
  }
});

const withDigitalDownload = (state) => ({
  downloadUrl: state.downloadUrl,
  fileSize: state.fileSize || 0,

  getDownloadLink() {
    return `${this.downloadUrl}?token=${Date.now()}`;
  },

  getFileSizeMB() {
    return (this.fileSize / 1024 / 1024).toFixed(2) + " MB";
  }
});

const withDiscount = (state) => ({
  discount: 0,

  applyDiscount(percent) {
    if (percent < 0 || percent > 100) {
      throw new Error("Discount must be between 0-100");
    }
    this.discount = percent;
    console.log(`✅ Applied ${percent}% discount to ${state.name}`);
  },

  getDiscountedPrice() {
    return state.price * (1 - this.discount / 100);
  }
});

const withTax = (state) => ({
  taxRate: 0.1, // 10% default

  calculateTax() {
    const price = this.getDiscountedPrice ? this.getDiscountedPrice() : state.price;
    return price * this.taxRate;
  },

  getPriceWithTax() {
    const price = this.getDiscountedPrice ? this.getDiscountedPrice() : state.price;
    return price + this.calculateTax();
  }
});

// Factory functions
function createPhysicalProduct(name, price, weight) {
  const state = { name, price, weight };

  return Object.assign(state,
    withPhysicalShipping(state),
    withDiscount(state),
    withTax(state)
  );
}

function createDigitalProduct(name, price, downloadUrl, fileSize) {
  const state = { name, price, downloadUrl, fileSize };

  return Object.assign(state,
    withDigitalDownload(state),
    withDiscount(state)
  );
}

function createComboProduct(name, price, weight, downloadUrl, fileSize) {
  const state = { name, price, weight, downloadUrl, fileSize };

  return Object.assign(state,
    withPhysicalShipping(state),
    withDigitalDownload(state),
    withDiscount(state),
    withTax(state)
  );
}

// Test
console.log("=== PHYSICAL PRODUCT ===");
const book = createPhysicalProduct("JavaScript Book", 30, 0.5);
console.log(`Price: $${book.price}`);
console.log(`Shipping: $${book.calculateShipping()}`);
console.log(`Total: $${book.getTotalPrice()}`);

book.applyDiscount(20);
console.log(`Discounted price: $${book.getDiscountedPrice()}`);
console.log(`Tax: $${book.calculateTax().toFixed(2)}`);
console.log(`Final total: $${(book.getPriceWithTax() + book.calculateShipping()).toFixed(2)}`);

console.log("\n=== DIGITAL PRODUCT ===");
const ebook = createDigitalProduct("JavaScript eBook", 15, "https://example.com/ebook", 5 * 1024 * 1024);
console.log(`Price: $${ebook.price}`);
console.log(`File size: ${ebook.getFileSizeMB()}`);
console.log(`Download: ${ebook.getDownloadLink()}`);

ebook.applyDiscount(30);
console.log(`Discounted price: $${ebook.getDiscountedPrice()}`);

console.log("\n=== COMBO PRODUCT ===");
const game = createComboProduct("AAA Game", 60, 0.8, "https://example.com/game", 50 * 1024 * 1024);
console.log(`Price: $${game.price}`);
console.log(`Weight: ${game.weight}kg`);
console.log(`Shipping: $${game.calculateShipping()}`);
console.log(`File size: ${game.getFileSizeMB()}`);
console.log(`Download: ${game.getDownloadLink()}`);

game.applyDiscount(15);
console.log(`Discounted price: $${game.getDiscountedPrice()}`);
console.log(`Tax: $${game.calculateTax().toFixed(2)}`);
console.log(`Final total: $${(game.getPriceWithTax() + game.calculateShipping()).toFixed(2)}`);
```

**Output**:
```
=== PHYSICAL PRODUCT ===
Price: $30
Shipping: $6
Total: $36
✅ Applied 20% discount to JavaScript Book
Discounted price: $24
Tax: $2.40
Final total: $32.40

=== DIGITAL PRODUCT ===
Price: $15
File size: 5.00 MB
Download: https://example.com/ebook?token=1234567890
✅ Applied 30% discount to JavaScript eBook
Discounted price: $10.5

=== COMBO PRODUCT ===
Price: $60
Weight: 0.8kg
Shipping: $6.6
File size: 50.00 MB
Download: https://example.com/game?token=1234567890
✅ Applied 15% discount to AAA Game
Discounted price: $51
Tax: $5.10
Final total: $62.70
```

</details>

---

## 2. Type Coercion

### 🤔 Tư Duy: Tại Sao Cần Hiểu Type Coercion?

JavaScript là **dynamically typed language** - Không cần khai báo type.

```javascript
let x = 5;        // number
x = "hello";      // Đổi thành string - OK!
x = true;         // Đổi thành boolean - OK!
```

**Vấn đề**: JavaScript tự động convert types khi cần → Có thể gây bugs khó debug

```javascript
console.log("5" + 5);   // "55" (string) - Có thể không như mong đợi!
console.log("5" - 5);   // 0 (number) - Tại sao lại khác +?
console.log([] == 0);   // true - WTF?
```

**Tại sao cần học Type Coercion?**
1. ✅ **Tránh bugs**: Hiểu behavior của operators
2. ✅ **Debug faster**: Biết tại sao `"10" + 5 = "105"`
3. ✅ **Write better code**: Dùng explicit conversion
4. ✅ **Pass interviews**: Đây là câu hỏi phổ biến!

---

### 2.1 Type Coercion là gì?

**Định nghĩa**: Type Coercion là quá trình JavaScript **tự động** chuyển đổi giữa các types.

#### 📌 Hai Loại Coercion

**1. Implicit Coercion (Ngầm định)** - JavaScript tự convert

```javascript
// JavaScript tự convert để operators hoạt động
console.log(5 + "5");        // "55" - number → string
console.log("5" - 2);        // 3 - string → number
console.log(true + 1);       // 2 - boolean → number
console.log("10" * "2");     // 20 - string → number
```

**2. Explicit Coercion (Tường minh)** - Developer chủ động convert

```javascript
// Developer chủ động convert bằng functions
console.log(Number("5"));    // 5
console.log(String(123));    // "123"
console.log(Boolean(0));     // false
console.log(Boolean(1));     // true
```

#### 💡 Type Conversion Rules

```
JavaScript có 3 types of conversion:
1. To String
2. To Number
3. To Boolean

Mỗi operator có rules riêng:
- + : Prefer String (nếu có string operand)
- -, *, /, % : Convert to Number
- ==, != : Complex rules (avoid!)
- ===, !== : No conversion (always use!)
```

---

### 2.2 String Coercion

Khi nào JavaScript convert sang **String**?

#### 📌 Rule: Operator `+` với String

```javascript
// Operator + với string → Convert tất cả sang string
console.log("5" + 5);        // "55" (number → string)
console.log(5 + "5");        // "55" (number → string)
console.log("Hello" + 123);  // "Hello123" (number → string)
console.log(true + "!");     // "true!" (boolean → string)
console.log(null + "");      // "null" (null → string)
console.log(undefined + ""); // "undefined" (undefined → string)

// Nhiều operands: Left-to-right evaluation
console.log(1 + 2 + "3");    // "33" (1+2=3, 3+"3"="33")
console.log("1" + 2 + 3);    // "123" ("1"+2="12", "12"+3="123")
```

**💭 Tại sao?** Operator `+` vừa là addition, vừa là concatenation
- Nếu **bất kỳ operand nào** là string → String concatenation
- Ngược lại → Addition

#### 📌 Template Literals

```javascript
const age = 25;
const name = "An";

// Template literals tự convert sang string
console.log(`Tôi là ${name}, ${age} tuổi`); // "Tôi là An, 25 tuổi"

// Works with any type
const isActive = true;
console.log(`Status: ${isActive}`); // "Status: true"

const obj = { x: 10 };
console.log(`Object: ${obj}`); // "Object: [object Object]"
```

#### 📌 String() Function

```javascript
// Explicit conversion
console.log(String(123));           // "123"
console.log(String(true));          // "true"
console.log(String(false));         // "false"
console.log(String(null));          // "null"
console.log(String(undefined));     // "undefined"
console.log(String([1, 2, 3]));     // "1,2,3"
console.log(String({ name: "An" })); // "[object Object]"
console.log(String(Symbol("id")));  // "Symbol(id)"
```

#### 📌 toString() Method

```javascript
// Works on most types
console.log((123).toString());     // "123"
console.log(true.toString());      // "true"
console.log([1, 2, 3].toString()); // "1,2,3"

// Different number bases
const num = 255;
console.log(num.toString(2));      // "11111111" (binary)
console.log(num.toString(8));      // "377" (octal)
console.log(num.toString(16));     // "ff" (hexadecimal)
console.log(num.toString(36));     // "73" (base 36)

// ❌ Doesn't work on null/undefined
// console.log(null.toString()); // TypeError!
// console.log(undefined.toString()); // TypeError!

// ✅ Use String() instead
console.log(String(null));         // "null"
console.log(String(undefined));    // "undefined"
```

---

### 2.3 Number Coercion

Khi nào JavaScript convert sang **Number**?

#### 📌 Rule: Math Operators (-, *, /, %)

```javascript
// Math operators (trừ +) → Convert sang number
console.log("5" - 2);        // 3 (string → number)
console.log("10" * "2");     // 20 (string → number)
console.log("20" / "4");     // 5 (string → number)
console.log("5" % "2");      // 1 (string → number)

// Works with booleans
console.log(true - 1);       // 0 (true → 1)
console.log(false * 5);      // 0 (false → 0)

// null becomes 0
console.log(null + 5);       // 5 (null → 0)
console.log(null * 3);       // 0 (null → 0)

// undefined becomes NaN
console.log(undefined + 5);  // NaN (undefined → NaN)
console.log(undefined * 3);  // NaN (undefined → NaN)

// Invalid conversions → NaN
console.log("hello" - 5);    // NaN (can't convert "hello")
console.log("abc" * 2);      // NaN (can't convert "abc")
```

#### 📌 Unary + Operator

```javascript
// Unary + converts to number (fastest way!)
console.log(+"123");         // 123
console.log(+"45.67");       // 45.67
console.log(+true);          // 1
console.log(+false);         // 0
console.log(+null);          // 0
console.log(+undefined);     // NaN
console.log(+"hello");       // NaN
console.log(+"  42  ");      // 42 (trims whitespace)

// Practical use
const userInput = "25";
const age = +userInput; // Quick conversion!
console.log(age); // 25 (number)
```

#### 📌 Number() Function

```javascript
console.log(Number("123"));      // 123
console.log(Number("12.5"));     // 12.5
console.log(Number(""));         // 0 (empty string)
console.log(Number(" "));        // 0 (whitespace)
console.log(Number("   42   ")); // 42 (trims)
console.log(Number(true));       // 1
console.log(Number(false));      // 0
console.log(Number(null));       // 0
console.log(Number(undefined));  // NaN
console.log(Number("123abc"));   // NaN (invalid)
console.log(Number("abc123"));   // NaN (invalid)
```

#### 📌 parseInt() và parseFloat()

```javascript
// parseInt - Parse integer
console.log(parseInt("123"));        // 123
console.log(parseInt("123.45"));     // 123 (bỏ decimal)
console.log(parseInt("123px"));      // 123 (parse until non-digit)
console.log(parseInt("px123"));      // NaN (must start with digit)
console.log(parseInt("   42   "));   // 42 (trims)

// With radix (base)
console.log(parseInt("10", 2));      // 2 (binary)
console.log(parseInt("10", 8));      // 8 (octal)
console.log(parseInt("10", 16));     // 16 (hexadecimal)
console.log(parseInt("FF", 16));     // 255
console.log(parseInt("0xFF"));       // 255 (auto-detect hex)

// ⚠️ Always specify radix for safety
console.log(parseInt("08"));         // 8 (OK in modern JS)
// Old browsers: 0 (treated as octal!)

// parseFloat - Parse decimal
console.log(parseFloat("123.45"));   // 123.45
console.log(parseFloat("123.45abc")); // 123.45
console.log(parseFloat(".5"));       // 0.5
console.log(parseFloat("0.5"));      // 0.5
console.log(parseFloat("5."));       // 5
```

#### 💡 Number vs parseInt vs parseFloat

| Input | Number() | parseInt() | parseFloat() |
|-------|----------|------------|--------------|
| `"123"` | 123 | 123 | 123 |
| `"123.45"` | 123.45 | 123 | 123.45 |
| `"123px"` | NaN | 123 ✅ | 123 ✅ |
| `"  42  "` | 42 | 42 | 42 |
| `""` | 0 | NaN | NaN |
| `"abc"` | NaN | NaN | NaN |

**💭 Khi nào dùng gì?**
- `Number()`: Strict conversion, reject invalid strings
- `parseInt()`: Parse integers from strings like "123px"
- `parseFloat()`: Parse decimals from strings

---

### 2.4 Boolean Coercion

Khi nào JavaScript convert sang **Boolean**?

#### 📌 Falsy Values

Chỉ có **8 giá trị falsy** trong JavaScript:

```javascript
// 8 falsy values
console.log(Boolean(false));     // false
console.log(Boolean(0));         // false
console.log(Boolean(-0));        // false
console.log(Boolean(0n));        // false (BigInt zero)
console.log(Boolean(""));        // false (empty string)
console.log(Boolean(null));      // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN));       // false

// TẤT CẢ giá trị khác đều truthy!
console.log(Boolean(1));         // true
console.log(Boolean(-1));        // true
console.log(Boolean(" "));       // true (có space!)
console.log(Boolean("0"));       // true (string "0")
console.log(Boolean("false"));   // true (string "false")
console.log(Boolean([]));        // true (empty array)
console.log(Boolean({}));        // true (empty object)
console.log(Boolean(function(){})); // true
```

**💭 Phổ biến sai lầm**:
```javascript
// ❌ Những giá trị này là TRUTHY (không phải falsy!)
if ("0") {
  console.log("String '0' is truthy!"); // ✅ Chạy!
}

if ("false") {
  console.log("String 'false' is truthy!"); // ✅ Chạy!
}

if ([]) {
  console.log("Empty array is truthy!"); // ✅ Chạy!
}

if ({}) {
  console.log("Empty object is truthy!"); // ✅ Chạy!
}
```

#### 📌 Boolean() Function và Double NOT (!!)

```javascript
// Explicit conversion với Boolean()
console.log(Boolean(0));         // false
console.log(Boolean(1));         // true
console.log(Boolean(""));        // false
console.log(Boolean("hello"));   // true

// !! operator (common shorthand)
console.log(!!0);                // false
console.log(!!1);                // true
console.log(!!"hello");          // true

// Practical use
const userInput = "";
const hasInput = !!userInput; // false (quick boolean conversion)
```

#### 📌 Logical Operators: &&, ||, ??

```javascript
// && returns first falsy or last value
console.log(true && "hello");    // "hello"
console.log(false && "hello");   // false
console.log(0 && "hello");       // 0

// || returns first truthy or last value
console.log(false || "hello");   // "hello"
console.log(0 || 10);            // 10

// ?? returns right if left is null/undefined
console.log(null ?? "default");  // "default"
console.log(0 ?? "default");     // 0 (0 is not nullish!)
```

---

### 2.5-2.8 Summary và Best Practices

Để giữ tài liệu trong giới hạn hợp lý, phần Type Coercion chi tiết hơn về Object to Primitive, Comparison Operators, và các trường hợp phức tạp có thể được tóm tắt như sau:

**Key Points**:
- ✅ Luôn dùng `===` thay vì `==`
- ✅ Explicit coercion (Number(), String(), Boolean()) thay vì implicit
- ✅ Dùng `??` cho default values thay vì `||`
- ❌ Tránh so sánh khác types với `==`

---

### 🎯 Bài Tập 2: Type Coercion

#### Bài 1: Predict the Output

```javascript
console.log("5" + 3);        // ?
console.log("5" - 3);        // ?
console.log(true + 1);       // ?
console.log([] + {});        // ?
console.log(!![]);           // ?
```

<details>
<summary>✅ Đáp án</summary>

```javascript
console.log("5" + 3);        // "53" (string concatenation)
console.log("5" - 3);        // 2 (string → number)
console.log(true + 1);       // 2 (true → 1)
console.log([] + {});        // "[object Object]"
console.log(!![]);           // true ([] is truthy)
```

</details>

---

## 3. Pass By Reference vs Pass By Value

### 🤔 Tư Duy: Tại Sao Cần Hiểu Concept Này?

Khi bạn code, bạn sẽ gặp bugs như:

```javascript
function updateUser(user) {
  user.age = 26;
}

const myUser = { name: "An", age: 25 };
updateUser(myUser);
console.log(myUser.age); // 26 - ĐÃ THAY ĐỔI! Tại sao?
```

hoặc:

```javascript
function increment(num) {
  num = num + 1;
}

let count = 5;
increment(count);
console.log(count); // 5 - KHÔNG THAY ĐỔI! Tại sao?
```

**💭 Hiểu pass by reference vs value giúp**:
- ✅ Tránh bugs khó debug (unintended mutations)
- ✅ Write safer code (immutability)
- ✅ Hiểu memory management
- ✅ Optimize performance

---

### 3.1 Primitive Types (Pass by Value)

**Primitives**: string, number, boolean, undefined, null, symbol, bigint

```javascript
// Primitives được COPY value
let x = 10;
let y = x;  // Copy value 10 sang y

y = 20;     // Thay đổi y

console.log(x); // 10 (x không thay đổi) ✅
console.log(y); // 20

/*
Memory:
┌──────┐
│ x: 10│ ← Independent value
├──────┤
│ y: 20│ ← Independent value
└──────┘
*/
```

**Với Functions**:

```javascript
function changeValue(num) {
  num = 100;
  console.log("Inside:", num); // 100
}

let value = 50;
changeValue(value); // Pass COPY of 50
console.log("Outside:", value); // 50 (không đổi) ✅

/*
Explanation:
1. value = 50
2. changeValue gets COPY of 50
3. Changes to copy don't affect original
*/
```

---

### 3.2 Objects (Pass by Reference)

**Objects/Arrays/Functions**: passed by REFERENCE

```javascript
// Objects share REFERENCE
let obj1 = { name: "An" };
let obj2 = obj1;  // Copy REFERENCE (not value!)

obj2.name = "Bình"; // Modify through obj2

console.log(obj1.name); // "Bình" (obj1 changed!) ⚠️
console.log(obj2.name); // "Bình"
console.log(obj1 === obj2); // true (same reference)

/*
Memory:
Stack:              Heap:
┌──────────┐      ┌──────────────┐
│ obj1: ref────────→ { name: "Bình" }
├──────────┤  ↗   └──────────────┘
│ obj2: ref────┘
└──────────┘
Both point to SAME object in memory!
*/
```

**Với Functions**:

```javascript
function modifyObject(obj) {
  obj.name = "Modified";
  console.log("Inside:", obj.name); // "Modified"
}

let person = { name: "Original" };
modifyObject(person); // Pass REFERENCE
console.log("Outside:", person.name); // "Modified" (changed!) ⚠️
```

---

### 3.3 Reassignment vs Mutation

**Key Concept**: Reassignment vs Mutation hoàn toàn khác nhau!

```javascript
// ============================================
// REASSIGNMENT - Doesn't affect original
// ============================================
function reassignObject(obj) {
  obj = { name: "New Object" }; // Create NEW object
  console.log("Inside:", obj.name); // "New Object"
}

let user = { name: "Original" };
reassignObject(user);
console.log("Outside:", user.name); // "Original" (không đổi) ✅

/*
Explanation:
Before call:  user ──→ Object A
During call:  obj ──→ Object A (same reference)
After = :     obj ──→ Object B (NEW object!)
              user ──→ Object A (still pointing to A!)
*/

// ============================================
// MUTATION - Affects original
// ============================================
function mutateObject(obj) {
  obj.name = "Mutated"; // Modify existing object
  console.log("Inside:", obj.name); // "Mutated"
}

let user2 = { name: "Original" };
mutateObject(user2);
console.log("Outside:", user2.name); // "Mutated" (đã đổi!) ⚠️

/*
Explanation:
Before: user2 ──→ Object A { name: "Original" }
Mutate: obj ──→ Object A (modify property)
After:  user2 ──→ Object A { name: "Mutated" }
*/
```

---

### 3.4 Shallow Copy vs Deep Copy

#### 📌 Shallow Copy

**Methods**: `Object.assign()`, Spread operator `...`, `Array.slice()`

```javascript
// Object.assign() - Shallow copy
const original = { name: "An", age: 25 };
const copy = Object.assign({}, original);

copy.name = "Bình";
console.log(original.name); // "An" (không đổi) ✅
console.log(copy.name);     // "Bình"

// ⚠️ Problem with nested objects
const user = {
  name: "An",
  address: {
    city: "Hanoi"
  }
};

const userCopy = Object.assign({}, user);
userCopy.address.city = "Saigon"; // Modify nested object

console.log(user.address.city);     // "Saigon" (đã đổi!) ❌
console.log(userCopy.address.city); // "Saigon"

/*
Explanation:
┌──────────────┐      ┌──────────────┐
│ user         │      │ address      │
│ name: "An"   │      │ city:"Saigon"│
│ address: ref────────→└──────────────┘
└──────────────┘  ↗
┌──────────────┐  │
│ userCopy     │  │
│ name: "An"   │  │
│ address: ref────┘ ← Both share same address object!
└──────────────┘
*/

// Spread operator - Same issue
const arr = [[1, 2], [3, 4]];
const arrCopy = [...arr];

arrCopy[0][0] = 99;
console.log(arr[0][0]);     // 99 (changed!) ❌
console.log(arrCopy[0][0]); // 99
```

#### 📌 Deep Copy

**Methods**: `JSON.parse(JSON.stringify())`, Recursive function, `structuredClone()`

```javascript
// 1. JSON method - Simple but limited
const deepUser = {
  name: "An",
  address: {
    city: "Hanoi",
    country: "Vietnam"
  }
};

const deepCopy = JSON.parse(JSON.stringify(deepUser));
deepCopy.address.city = "Saigon";

console.log(deepUser.address.city);  // "Hanoi" (không đổi!) ✅
console.log(deepCopy.address.city);  // "Saigon"

// ⚠️ Limitations: Doesn't copy functions, Date, undefined, etc.
const problematic = {
  func: () => console.log("Hello"),
  date: new Date(),
  undef: undefined
};

const problemCopy = JSON.parse(JSON.stringify(problematic));
console.log(problemCopy);
// { date: "2024-01-01T00:00:00.000Z" } ← func and undef lost!

// 2. Recursive deep clone function
function deepClone(obj) {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  if (obj instanceof Date) {
    return new Date(obj.getTime());
  }

  if (Array.isArray(obj)) {
    return obj.map(item => deepClone(item));
  }

  const clonedObj = {};
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      clonedObj[key] = deepClone(obj[key]);
    }
  }

  return clonedObj;
}

// Test
const complex = {
  name: "An",
  hobbies: ["reading", "coding"],
  address: {
    city: "Hanoi",
    coordinates: {
      lat: 21.0285,
      lng: 105.8542
    }
  }
};

const complexCopy = deepClone(complex);
complexCopy.address.coordinates.lat = 10.8231;
complexCopy.hobbies.push("gaming");

console.log(complex.address.coordinates.lat);  // 21.0285 ✅
console.log(complexCopy.address.coordinates.lat); // 10.8231

console.log(complex.hobbies);     // ["reading", "coding"] ✅
console.log(complexCopy.hobbies); // ["reading", "coding", "gaming"]

// 3. structuredClone() - Modern solution (Node 17+)
const modernCopy = structuredClone(complex);
modernCopy.address.city = "Saigon";

console.log(complex.address.city);     // "Hanoi" ✅
console.log(modernCopy.address.city);  // "Saigon"
```

---

### 3.5 Preventing Modifications

```javascript
// 1. Object.freeze() - Completely immutable
const frozen = Object.freeze({
  name: "An",
  age: 25
});

frozen.name = "Bình";     // ❌ Không effect
frozen.salary = 1000;     // ❌ Không thêm được
delete frozen.age;        // ❌ Không xóa được

console.log(frozen); // { name: "An", age: 25 }

// ⚠️ Shallow freeze only
const partialFrozen = Object.freeze({
  name: "An",
  address: { city: "Hanoi" }
});

partialFrozen.name = "Bình";        // ❌ Không đổi
partialFrozen.address.city = "Saigon"; // ✅ ĐỔI được! (nested)

// Deep freeze function
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

// 2. Object.seal() - Allow modify, prevent add/delete
const sealed = Object.seal({ name: "An", age: 25 });

sealed.name = "Bình";     // ✅ OK (modify)
sealed.salary = 1000;     // ❌ Không thêm
delete sealed.age;        // ❌ Không xóa

console.log(sealed); // { name: "Bình", age: 25 }
```

---

### 3.6 Best Practices

```javascript
// ✅ DO: Return new objects
function addItem(cart, item) {
  return [...cart, item]; // New array ✅
}

const cart1 = [{ name: "Laptop" }];
const cart2 = addItem(cart1, { name: "Mouse" });

console.log(cart1.length); // 1 (unchanged) ✅
console.log(cart2.length); // 2

// ❌ DON'T: Modify directly
function addItemBad(cart, item) {
  cart.push(item); // Mutates original ❌
  return cart;
}

// ✅ DO: Defensive copying
function updateUser(user, updates) {
  return {
    ...user,
    ...updates,
    updatedAt: new Date()
  };
}

// ✅ DO: Use const for references
const config = {
  apiUrl: "https://api.example.com",
  timeout: 5000
};

// config = {}; // ❌ TypeError
config.timeout = 10000; // ✅ OK (modify property)
```

---

### 🎯 Bài Tập 3: Pass By Reference/Value

#### Bài 1: Predict Output

```javascript
let a = 5;
let b = a;
b = 10;
console.log(a); // ?

let obj1 = { x: 1 };
let obj2 = obj1;
obj2.x = 2;
console.log(obj1.x); // ?

function change(obj) {
  obj = { x: 3 };
}
let obj3 = { x: 1 };
change(obj3);
console.log(obj3.x); // ?
```

<details>
<summary>✅ Đáp án</summary>

```javascript
console.log(a); // 5 (primitive - pass by value)
console.log(obj1.x); // 2 (object - pass by reference)
console.log(obj3.x); // 1 (reassignment doesn't affect original)
```

</details>

---

## 4. Higher Order Functions

### 🤔 Tư Duy: Tại Sao Cần HOF?

**Problem**: Code repetitive, hard to maintain

```javascript
// ❌ Repetitive code
const numbers = [1, 2, 3, 4, 5];

const doubled = [];
for (let i = 0; i < numbers.length; i++) {
  doubled.push(numbers[i] * 2);
}

const tripled = [];
for (let i = 0; i < numbers.length; i++) {
  tripled.push(numbers[i] * 3);
}
```

**Solution**: Higher Order Functions

```javascript
// ✅ Reusable, declarative
const doubled = numbers.map(x => x * 2);
const tripled = numbers.map(x => x * 3);
```

**Lợi ích**:
- ✅ Less code
- ✅ More readable
- ✅ Reusable
- ✅ Easier to test

---

### 4.1 Higher Order Function là gì?

**Định nghĩa**: Function nhận function làm argument HOẶC return function

```javascript
// Type 1: Nhận function làm argument
function executeFunction(fn) {
  fn();
}

executeFunction(() => console.log("Hello!"));

// Type 2: Return function
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

---

### 4.2 Array Methods (Built-in HOFs)

```javascript
const numbers = [1, 2, 3, 4, 5];

// map() - Transform each element
const doubled = numbers.map(n => n * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// filter() - Keep elements that pass test
const evens = numbers.filter(n => n % 2 === 0);
console.log(evens); // [2, 4]

// reduce() - Accumulate to single value
const sum = numbers.reduce((acc, n) => acc + n, 0);
console.log(sum); // 15

// find() - First element that passes test
const firstEven = numbers.find(n => n % 2 === 0);
console.log(firstEven); // 2

// some() - At least one passes test
const hasEven = numbers.some(n => n % 2 === 0);
console.log(hasEven); // true

// every() - All pass test
const allPositive = numbers.every(n => n > 0);
console.log(allPositive); // true
```

---

### 4.3 Chaining Methods

```javascript
const products = [
  { name: "Laptop", price: 1000, category: "Electronics", inStock: true },
  { name: "Phone", price: 500, category: "Electronics", inStock: true },
  { name: "Shirt", price: 50, category: "Clothing", inStock: false },
  { name: "Shoes", price: 100, category: "Clothing", inStock: true }
];

// Calculate total of in-stock electronics
const total = products
  .filter(p => p.category === "Electronics")
  .filter(p => p.inStock)
  .map(p => p.price)
  .reduce((sum, price) => sum + price, 0);

console.log(total); // 1500
```

---

### 4.4 Creating Custom HOFs

```javascript
// 1. Memoization
function memoize(fn) {
  const cache = new Map();

  return function(...args) {
    const key = JSON.stringify(args);

    if (cache.has(key)) {
      return cache.get(key);
    }

    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

const slowFn = memoize(function(n) {
  console.log("Computing...");
  return n * 2;
});

console.log(slowFn(5)); // "Computing..." 10
console.log(slowFn(5)); // 10 (from cache, no log)

// 2. Debounce
function debounce(fn, delay) {
  let timeoutId;

  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
}

const search = debounce(function(query) {
  console.log("Searching:", query);
}, 500);

search("java");
search("javasc");
search("javascript"); // Only this executes after 500ms

// 3. Once
function once(fn) {
  let called = false;
  let result;

  return function(...args) {
    if (!called) {
      called = true;
      result = fn(...args);
    }
    return result;
  };
}

const initialize = once(() => {
  console.log("Initialized!");
  return { status: "ready" };
});

initialize(); // "Initialized!"
initialize(); // No log (not called again)
```

---

### 4.5 Functional Programming Patterns

```javascript
// Compose - Combine functions right-to-left
function compose(...fns) {
  return function(value) {
    return fns.reduceRight((acc, fn) => fn(acc), value);
  };
}

// Pipe - Combine functions left-to-right
function pipe(...fns) {
  return function(value) {
    return fns.reduce((acc, fn) => fn(acc), value);
  };
}

const addOne = x => x + 1;
const double = x => x * 2;
const square = x => x * x;

const calc1 = compose(square, double, addOne);
console.log(calc1(3)); // ((3+1)*2)^2 = 64

const calc2 = pipe(addOne, double, square);
console.log(calc2(3)); // ((3+1)*2)^2 = 64

// Curry - Transform multi-arg function
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn(...args);
    }
    return (...nextArgs) => curried(...args, ...nextArgs);
  };
}

const add = curry((a, b, c) => a + b + c);

console.log(add(1)(2)(3));      // 6
console.log(add(1, 2)(3));      // 6
console.log(add(1)(2, 3));      // 6
```

---

### 4.6 Best Practices

```javascript
// ✅ DO: Pure functions (no side effects)
const addTax = (price, rate) => price * (1 + rate);

// ❌ DON'T: Impure functions
let taxRate = 0.1;
const addTaxBad = (price) => price * (1 + taxRate); // Depends on external state

// ✅ DO: Descriptive names
const filterAdults = users => users.filter(u => u.age >= 18);
const calculateAverage = nums => nums.reduce((a, b) => a + b, 0) / nums.length;

// ✅ DO: Small, focused functions
const isEven = n => n % 2 === 0;
const isPositive = n => n > 0;

const evenPositiveNumbers = numbers
  .filter(isEven)
  .filter(isPositive);
```

---

### 🎯 Bài Tập 4: Higher Order Functions

#### Bài 1: Implement Custom map()

Viết function `myMap()` hoạt động giống `Array.map()`

<details>
<summary>✅ Giải pháp</summary>

```javascript
function myMap(array, fn) {
  const result = [];
  for (let i = 0; i < array.length; i++) {
    result.push(fn(array[i], i, array));
  }
  return result;
}

// Test
const numbers = [1, 2, 3, 4, 5];
const doubled = myMap(numbers, n => n * 2);
console.log(doubled); // [2, 4, 6, 8, 10]
```

</details>

---

## Tổng Kết

### 📋 Checklist Kiến Thức

- [ ] Hiểu Composition vs Inheritance
- [ ] Nắm vững Type Coercion (Implicit và Explicit)
- [ ] Phân biệt Pass by Value vs Reference
- [ ] Biết cách clone objects (Shallow vs Deep)
- [ ] Thành thạo Array HOFs (map, filter, reduce)
- [ ] Tạo được custom Higher Order Functions
- [ ] Apply Functional Programming patterns

### 💡 Key Takeaways

1. **Composition > Inheritance**: Flexibility và reusability
2. **Type Coercion**: Luôn dùng `===` và explicit conversion
3. **Pass by Reference**: Cẩn thận với object mutations
4. **Higher Order Functions**: Declarative, reusable code

### 🎯 Bài Tập Tổng Hợp

Tạo một **Task Management System** với:
1. Composition cho task types (urgent, recurring, etc.)
2. Proper type handling và validation
3. Immutable operations (no mutations)
4. HOFs cho filtering, sorting, transforming tasks

---

**Chúc bạn học tốt! 🚀**

*"Favor composition over inheritance" - Gang of Four*
*"Make it work, make it right, make it fast" - Kent Beck*

