# CHƯƠNG 7: CLASSES

## 7.1. Giới thiệu ES6 Classes

Classes trong ES6 là syntax sugar cho prototype-based inheritance.

### 7.1.1. ES5 vs ES6

**ES5 (Constructor Function):**
```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.greet = function() {
    console.log('Hello, ' + this.name);
};

var john = new Person('John', 30);
```

**ES6 (Class):**
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log(`Hello, ${this.name}`);
    }
}

const john = new Person('John', 30);
```

## 7.2. Class Syntax

### 7.2.1. Basic Class

```javascript
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    getInfo() {
        return `${this.name} (${this.email})`;
    }

    updateEmail(newEmail) {
        this.email = newEmail;
    }
}

const user = new User('John', 'john@example.com');
console.log(user.getInfo());  // "John (john@example.com)"
```

### 7.2.2. Constructor

```javascript
class Product {
    constructor(name, price) {
        // Initialize properties
        this.name = name;
        this.price = price;
        this.created = new Date();
    }
}

// Constructor is optional
class Empty {
    // No constructor needed
}
```

### 7.2.3. Methods

```javascript
class Calculator {
    // Instance methods
    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }

    multiply(a, b) {
        return a * b;
    }
}

const calc = new Calculator();
console.log(calc.add(5, 3));  // 8
```

### 7.2.4. Getters and Setters

```javascript
class Circle {
    constructor(radius) {
        this._radius = radius;
    }

    // Getter
    get radius() {
        return this._radius;
    }

    // Setter
    set radius(value) {
        if (value > 0) {
            this._radius = value;
        } else {
            throw new Error('Radius must be positive');
        }
    }

    get area() {
        return Math.PI * this._radius ** 2;
    }

    get diameter() {
        return this._radius * 2;
    }
}

const circle = new Circle(5);
console.log(circle.radius);    // 5
console.log(circle.area);      // 78.54...
circle.radius = 10;            // Using setter
console.log(circle.diameter);  // 20
```

## 7.3. Static Methods and Properties

### 7.3.1. Static Methods

```javascript
class MathUtils {
    static add(a, b) {
        return a + b;
    }

    static multiply(a, b) {
        return a * b;
    }

    static PI = 3.14159;  // Static property
}

// Call without instance
console.log(MathUtils.add(5, 3));  // 8
console.log(MathUtils.PI);         // 3.14159

// Cannot call on instance
const utils = new MathUtils();
// utils.add(5, 3);  // Error: not a function
```

### 7.3.2. Static Use Cases

```javascript
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    // Static factory method
    static create(name, email) {
        return new User(name, email);
    }

    // Static utility
    static validateEmail(email) {
        return /\S+@\S+\.\S+/.test(email);
    }

    // Static counter
    static count = 0;
    static incrementCount() {
        User.count++;
    }
}

const user = User.create('John', 'john@example.com');
console.log(User.validateEmail('test@test.com'));  // true
```

## 7.4. Inheritance

### 7.4.1. Extends Keyword

```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a sound`);
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name);  // Call parent constructor
        this.breed = breed;
    }

    speak() {
        console.log(`${this.name} barks`);
    }
}

const dog = new Dog('Rex', 'German Shepherd');
dog.speak();  // "Rex barks"
```

### 7.4.2. Super Keyword

```javascript
class Shape {
    constructor(color) {
        this.color = color;
    }

    describe() {
        return `A ${this.color} shape`;
    }
}

class Rectangle extends Shape {
    constructor(color, width, height) {
        super(color);  // Call parent constructor
        this.width = width;
        this.height = height;
    }

    describe() {
        // Call parent method
        return `${super.describe()} with area ${this.area()}`;
    }

    area() {
        return this.width * this.height;
    }
}

const rect = new Rectangle('red', 10, 5);
console.log(rect.describe());  // "A red shape with area 50"
```

### 7.4.3. Method Overriding

```javascript
class Vehicle {
    start() {
        console.log('Vehicle starting...');
    }

    stop() {
        console.log('Vehicle stopping...');
    }
}

class Car extends Vehicle {
    start() {
        console.log('Car engine starting...');
    }

    // stop() inherited from Vehicle
}

const car = new Car();
car.start();  // "Car engine starting..."
car.stop();   // "Vehicle stopping..."
```

## 7.5. Private Fields and Methods

### 7.5.1. Private Fields (#)

```javascript
class BankAccount {
    #balance = 0;  // Private field

    constructor(initialBalance) {
        this.#balance = initialBalance;
    }

    deposit(amount) {
        this.#balance += amount;
    }

    withdraw(amount) {
        if (amount <= this.#balance) {
            this.#balance -= amount;
            return true;
        }
        return false;
    }

    getBalance() {
        return this.#balance;
    }
}

const account = new BankAccount(1000);
account.deposit(500);
console.log(account.getBalance());  // 1500
// console.log(account.#balance);   // SyntaxError: Private field
```

### 7.5.2. Private Methods

```javascript
class User {
    #password;

    constructor(username, password) {
        this.username = username;
        this.#password = this.#hashPassword(password);
    }

    // Private method
    #hashPassword(password) {
        return btoa(password);  // Simple encoding (not secure!)
    }

    // Private method
    #validatePassword(password) {
        return this.#hashPassword(password) === this.#password;
    }

    // Public method
    login(password) {
        return this.#validatePassword(password);
    }
}

const user = new User('john', 'secret123');
console.log(user.login('secret123'));  // true
// user.#hashPassword('test');         // SyntaxError
```

## 7.6. Practical Examples

### 7.6.1. Todo List

```javascript
class TodoList {
    #todos = [];
    #nextId = 1;

    add(text) {
        const todo = {
            id: this.#nextId++,
            text,
            completed: false,
            createdAt: new Date()
        };
        this.#todos.push(todo);
        return todo;
    }

    complete(id) {
        const todo = this.#todos.find(t => t.id === id);
        if (todo) {
            todo.completed = true;
        }
    }

    getAll() {
        return [...this.#todos];
    }

    getActive() {
        return this.#todos.filter(t => !t.completed);
    }

    getCompleted() {
        return this.#todos.filter(t => t.completed);
    }
}
```

### 7.6.2. Shopping Cart

```javascript
class ShoppingCart {
    #items = [];

    addItem(product, quantity = 1) {
        const existing = this.#items.find(i => i.product.id === product.id);
        if (existing) {
            existing.quantity += quantity;
        } else {
            this.#items.push({ product, quantity });
        }
    }

    removeItem(productId) {
        this.#items = this.#items.filter(i => i.product.id !== productId);
    }

    get total() {
        return this.#items.reduce((sum, item) => {
            return sum + (item.product.price * item.quantity);
        }, 0);
    }

    get itemCount() {
        return this.#items.reduce((sum, item) => sum + item.quantity, 0);
    }

    getItems() {
        return [...this.#items];
    }
}
```

### 7.6.3. Validator

```javascript
class Validator {
    static isEmail(email) {
        return /\S+@\S+\.\S+/.test(email);
    }

    static isPhone(phone) {
        return /^\d{10}$/.test(phone);
    }

    static isStrongPassword(password) {
        return password.length >= 8 &&
               /[A-Z]/.test(password) &&
               /[a-z]/.test(password) &&
               /[0-9]/.test(password);
    }

    static isURL(url) {
        try {
            new URL(url);
            return true;
        } catch {
            return false;
        }
    }
}

console.log(Validator.isEmail('test@example.com'));  // true
console.log(Validator.isStrongPassword('Abc123'));   // false
```

## 7.7. Advanced Patterns

### 7.7.1. Abstract Classes (Pattern)

```javascript
class AbstractShape {
    constructor() {
        if (new.target === AbstractShape) {
            throw new Error('Cannot instantiate abstract class');
        }
    }

    area() {
        throw new Error('Must implement area()');
    }
}

class Square extends AbstractShape {
    constructor(side) {
        super();
        this.side = side;
    }

    area() {
        return this.side ** 2;
    }
}

// const shape = new AbstractShape();  // Error
const square = new Square(5);
console.log(square.area());  // 25
```

### 7.7.2. Singleton Pattern

```javascript
class Database {
    static #instance = null;

    constructor() {
        if (Database.#instance) {
            return Database.#instance;
        }
        Database.#instance = this;
        this.connected = false;
    }

    connect() {
        this.connected = true;
        console.log('Database connected');
    }

    static getInstance() {
        if (!Database.#instance) {
            Database.#instance = new Database();
        }
        return Database.#instance;
    }
}

const db1 = new Database();
const db2 = new Database();
console.log(db1 === db2);  // true (same instance)
```

### 7.7.3. Factory Pattern

```javascript
class User {
    constructor(type, name) {
        this.type = type;
        this.name = name;
    }
}

class Admin extends User {
    constructor(name) {
        super('admin', name);
        this.permissions = ['read', 'write', 'delete'];
    }
}

class Guest extends User {
    constructor(name) {
        super('guest', name);
        this.permissions = ['read'];
    }
}

class UserFactory {
    static createUser(type, name) {
        switch (type) {
            case 'admin':
                return new Admin(name);
            case 'guest':
                return new Guest(name);
            default:
                return new User('user', name);
        }
    }
}

const admin = UserFactory.createUser('admin', 'John');
const guest = UserFactory.createUser('guest', 'Jane');
```

## 7.8. Best Practices

### 7.8.1. Naming Conventions

```javascript
class MyClass {
    publicProperty = 'public';
    #privateProperty = 'private';

    publicMethod() { }
    #privateMethod() { }

    get property() { }
    set property(value) { }

    static StaticMethod() { }
}
```

### 7.8.2. Single Responsibility

```javascript
// Good: Each class has single responsibility
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
}

class UserValidator {
    static validate(user) {
        return user.name && user.email;
    }
}

class UserRepository {
    save(user) { /* save to DB */ }
    findById(id) { /* find user */ }
}
```

### 7.8.3. Composition over Inheritance

```javascript
// Instead of deep inheritance
class Flyable {
    fly() {
        console.log('Flying...');
    }
}

class Swimmable {
    swim() {
        console.log('Swimming...');
    }
}

// Use composition
class Duck {
    constructor() {
        this.flyBehavior = new Flyable();
        this.swimBehavior = new Swimmable();
    }

    fly() {
        this.flyBehavior.fly();
    }

    swim() {
        this.swimBehavior.swim();
    }
}
```

## 7.9. Common Mistakes

### 7.9.1. Forgetting 'new'

```javascript
class Person {
    constructor(name) {
        this.name = name;
    }
}

// Error: Classes must be called with 'new'
const person = Person('John');  // TypeError

// Correct
const person = new Person('John');
```

### 7.9.2. Forgetting 'super()' in Constructor

```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        // Must call super() before using 'this'
        super(name);  // Required!
        this.breed = breed;
    }
}
```

### 7.9.3. 'this' in Callbacks

```javascript
class Counter {
    count = 0;

    increment() {
        this.count++;
    }

    start() {
        // Wrong: 'this' is undefined
        setInterval(function() {
            this.increment();  // Error
        }, 1000);

        // Fix 1: Arrow function
        setInterval(() => {
            this.increment();  // Works
        }, 1000);

        // Fix 2: .bind()
        setInterval(this.increment.bind(this), 1000);
    }
}
```

## 7.10. Exercises

### Exercise 1: Create Rectangle Class

```javascript
// Create a Rectangle class with:
// - constructor(width, height)
// - area() method
// - perimeter() method
// - isSquare() method
```

### Exercise 2: Bank Account

```javascript
// Create BankAccount class with:
// - Private balance field
// - deposit(amount) method
// - withdraw(amount) method (check sufficient funds)
// - getBalance() method
```

### Exercise 3: Inheritance

```javascript
// Create Animal and Dog classes
// Animal: constructor(name), speak()
// Dog: extends Animal, speak() override, wagTail()
```

---

**Kết luận:** Classes trong ES6 cung cấp syntax rõ ràng hơn cho OOP trong JavaScript. Hỗ trợ inheritance, encapsulation với private fields, và static members.

**Chương tiếp theo:** Modules (Import/Export)
