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

## 7.6. Use Cases Thực Tế

### Use Case 1: Shopping Cart System

```javascript
class Product {
    constructor(id, name, price, stock) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    decreaseStock(quantity) {
        if (this.stock >= quantity) {
            this.stock -= quantity;
            return true;
        }
        return false;
    }
}

class CartItem {
    constructor(product, quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    getSubtotal() {
        return this.product.price * this.quantity;
    }
}

class ShoppingCart {
    #items = [];
    #discountRate = 0;

    addItem(product, quantity = 1) {
        const existing = this.#items.find(item => item.product.id === product.id);

        if (existing) {
            existing.quantity += quantity;
        } else {
            this.#items.push(new CartItem(product, quantity));
        }
    }

    removeItem(productId) {
        this.#items = this.#items.filter(item => item.product.id !== productId);
    }

    updateQuantity(productId, quantity) {
        const item = this.#items.find(i => i.product.id === productId);
        if (item) {
            item.quantity = Math.max(0, quantity);
        }
    }

    applyDiscount(rate) {
        this.#discountRate = Math.min(rate, 1);
    }

    get subtotal() {
        return this.#items.reduce((sum, item) => sum + item.getSubtotal(), 0);
    }

    get discount() {
        return this.subtotal * this.#discountRate;
    }

    get total() {
        return this.subtotal - this.discount;
    }

    get itemCount() {
        return this.#items.reduce((sum, item) => sum + item.quantity, 0);
    }

    getItems() {
        return [...this.#items];
    }

    clear() {
        this.#items = [];
    }
}

// Usage
const cart = new ShoppingCart();
const product1 = new Product(1, 'Laptop', 1000, 5);
const product2 = new Product(2, 'Mouse', 50, 10);

cart.addItem(product1, 1);
cart.addItem(product2, 2);
console.log(cart.total);  // 1100

cart.applyDiscount(0.1);  // 10% discount
console.log(cart.total);  // 990
```

### Use Case 2: User Management System

```javascript
class User {
    #password;
    #email;

    constructor(username, email, password) {
        this.username = username;
        this.#email = email;
        this.#password = this.#hashPassword(password);
        this.createdAt = new Date();
        this.lastLogin = null;
    }

    #hashPassword(password) {
        return btoa(password);  // Simple hash (not secure!)
    }

    #validatePassword(password) {
        return this.#hashPassword(password) === this.#password;
    }

    get email() {
        return this.#email;
    }

    changeEmail(newEmail) {
        if (/\S+@\S+\.\S+/.test(newEmail)) {
            this.#email = newEmail;
            return true;
        }
        return false;
    }

    changePassword(oldPassword, newPassword) {
        if (this.#validatePassword(oldPassword) && newPassword.length >= 6) {
            this.#password = this.#hashPassword(newPassword);
            return true;
        }
        return false;
    }

    login(password) {
        if (this.#validatePassword(password)) {
            this.lastLogin = new Date();
            return true;
        }
        return false;
    }

    getInfo() {
        return {
            username: this.username,
            email: this.#email,
            createdAt: this.createdAt,
            lastLogin: this.lastLogin
        };
    }
}

class Admin extends User {
    #permissions = ['read', 'write', 'delete', 'admin'];

    constructor(username, email, password) {
        super(username, email, password);
        this.role = 'admin';
    }

    hasPermission(permission) {
        return this.#permissions.includes(permission);
    }

    addPermission(permission) {
        if (!this.#permissions.includes(permission)) {
            this.#permissions.push(permission);
        }
    }
}

class Guest extends User {
    constructor(username) {
        super(username, `guest-${Date.now()}@guest.com`, 'guest');
        this.role = 'guest';
    }

    changeEmail() {
        return false;  // Guests can't change email
    }

    changePassword() {
        return false;  // Guests can't change password
    }
}

// Usage
const user = new User('john', 'john@example.com', 'password123');
console.log(user.login('password123'));  // true

const admin = new Admin('admin', 'admin@example.com', 'adminpass');
console.log(admin.hasPermission('admin'));  // true
```

### Use Case 3: Component System (React-like)

```javascript
class Component {
    #state = {};
    #subscribers = [];
    #mounted = false;

    constructor(props = {}) {
        this.props = props;
    }

    setState(updates) {
        this.#state = { ...this.#state, ...updates };
        this.#notifySubscribers();
    }

    getState() {
        return { ...this.#state };
    }

    subscribe(callback) {
        this.#subscribers.push(callback);
        return () => {
            this.#subscribers = this.#subscribers.filter(cb => cb !== callback);
        };
    }

    #notifySubscribers() {
        this.#subscribers.forEach(cb => cb(this));
    }

    mount() {
        this.#mounted = true;
        this.componentDidMount();
    }

    unmount() {
        this.#mounted = false;
        this.componentWillUnmount();
    }

    isMounted() {
        return this.#mounted;
    }

    componentDidMount() {}
    componentWillUnmount() {}
    render() {}
}

class Button extends Component {
    constructor(props) {
        super(props);
        this.setState({ clicks: 0 });
    }

    onClick() {
        const state = this.getState();
        this.setState({ clicks: state.clicks + 1 });
        this.props.onClick?.();
    }

    render() {
        const state = this.getState();
        return `<button>${this.props.label} (${state.clicks})</button>`;
    }
}

class Form extends Component {
    constructor(props) {
        super(props);
        this.setState({ formData: {} });
    }

    handleInput(name, value) {
        const state = this.getState();
        this.setState({
            formData: { ...state.formData, [name]: value }
        });
    }

    submit() {
        this.props.onSubmit?.(this.getState().formData);
    }

    render() {
        return '<form>...</form>';
    }
}

// Usage
const button = new Button({
    label: 'Click me',
    onClick: () => console.log('Clicked!')
});

button.subscribe(component => {
    console.log('Button state:', component.getState());
});

button.mount();
button.onClick();
button.unmount();
```

### Use Case 4: Database Connection Pool

```javascript
class DatabaseConnection {
    #connected = false;
    #queryCount = 0;

    constructor(id) {
        this.id = id;
    }

    connect() {
        this.#connected = true;
        console.log(`Connection ${this.id} connected`);
    }

    disconnect() {
        this.#connected = false;
        console.log(`Connection ${this.id} disconnected`);
    }

    isConnected() {
        return this.#connected;
    }

    async query(sql) {
        if (!this.#connected) {
            throw new Error('Connection not established');
        }
        this.#queryCount++;
        return { result: 'data', sql };
    }

    getQueryCount() {
        return this.#queryCount;
    }
}

class DatabasePool {
    #connections = [];
    #available = [];
    #poolSize = 5;

    constructor(poolSize = 5) {
        this.#poolSize = poolSize;
        this.#initializeConnections();
    }

    #initializeConnections() {
        for (let i = 0; i < this.#poolSize; i++) {
            const conn = new DatabaseConnection(i);
            conn.connect();
            this.#connections.push(conn);
            this.#available.push(conn);
        }
    }

    getConnection() {
        if (this.#available.length === 0) {
            throw new Error('No available connections');
        }
        return this.#available.pop();
    }

    releaseConnection(conn) {
        if (this.#connections.includes(conn)) {
            this.#available.push(conn);
        }
    }

    async execute(sql) {
        const conn = this.getConnection();
        try {
            return await conn.query(sql);
        } finally {
            this.releaseConnection(conn);
        }
    }

    close() {
        this.#connections.forEach(conn => conn.disconnect());
        this.#connections = [];
        this.#available = [];
    }
}

// Usage
const pool = new DatabasePool(3);
const result = await pool.execute('SELECT * FROM users');
pool.close();
```

### Use Case 5: Event Emitter

```javascript
class EventEmitter {
    #events = {};
    #maxListeners = 10;

    on(event, listener) {
        if (!this.#events[event]) {
            this.#events[event] = [];
        }

        if (this.#events[event].length >= this.#maxListeners) {
            console.warn(`Max listeners (${this.#maxListeners}) for ${event}`);
        }

        this.#events[event].push(listener);

        return () => this.off(event, listener);
    }

    once(event, listener) {
        const wrapper = (...args) => {
            listener(...args);
            this.off(event, wrapper);
        };
        return this.on(event, wrapper);
    }

    off(event, listener) {
        if (!this.#events[event]) return;
        this.#events[event] = this.#events[event].filter(l => l !== listener);
    }

    emit(event, ...args) {
        if (!this.#events[event]) return false;
        this.#events[event].forEach(listener => listener(...args));
        return true;
    }

    removeAllListeners(event) {
        if (event) {
            delete this.#events[event];
        } else {
            this.#events = {};
        }
    }

    listenerCount(event) {
        return this.#events[event]?.length || 0;
    }
}

// Usage
const emitter = new EventEmitter();

emitter.on('user:login', (username) => {
    console.log(`${username} logged in`);
});

emitter.once('welcome', () => {
    console.log('Welcome to the app!');
});

emitter.emit('user:login', 'john');
emitter.emit('welcome');
emitter.emit('welcome');  // Won't log again
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

## 7.8. Tips & Tricks

### Tip 1: Method Chaining

```javascript
class Builder {
    constructor() {
        this.result = {};
    }

    setName(name) {
        this.result.name = name;
        return this;
    }

    setAge(age) {
        this.result.age = age;
        return this;
    }

    setEmail(email) {
        this.result.email = email;
        return this;
    }

    build() {
        return this.result;
    }
}

// Usage: Chaining methods
const user = new Builder()
    .setName('John')
    .setAge(30)
    .setEmail('john@example.com')
    .build();
```

### Tip 2: Factory Methods

```javascript
class User {
    constructor(name, email, role) {
        this.name = name;
        this.email = email;
        this.role = role;
    }

    static createAdmin(name, email) {
        return new User(name, email, 'admin');
    }

    static createGuest(name) {
        return new User(name, `guest-${Date.now()}@example.com`, 'guest');
    }

    static fromObject(obj) {
        return new User(obj.name, obj.email, obj.role || 'user');
    }
}

// Usage
const admin = User.createAdmin('john', 'john@example.com');
const guest = User.createGuest('jane');
const user = User.fromObject({ name: 'Bob', email: 'bob@example.com' });
```

### Tip 3: Private Field Naming Convention

```javascript
class Account {
    // Double hash for truly private
    #balance = 0;

    // Single underscore for protected (convention only)
    _logger = console;

    // Prefix for internal
    __version = '1.0.0';

    getBalance() {
        return this.#balance;
    }
}
```

### Tip 4: Default Parameter in Constructor

```javascript
class Config {
    constructor(options = {}) {
        this.host = options.host ?? 'localhost';
        this.port = options.port ?? 3000;
        this.debug = options.debug ?? false;
        this.timeout = options.timeout ?? 5000;
    }

    getConnection() {
        return `${this.host}:${this.port}`;
    }
}

// Usage
const config1 = new Config();  // All defaults
const config2 = new Config({ host: '192.168.1.1', port: 8080 });
```

### Tip 5: Mixing Static and Instance Methods

```javascript
class MathHelper {
    // Instance state
    value = 0;

    constructor(initialValue = 0) {
        this.value = initialValue;
    }

    // Instance methods
    add(n) {
        this.value += n;
        return this;
    }

    getValue() {
        return this.value;
    }

    // Static utility methods
    static PI = 3.14159;
    static E = 2.71828;

    static random(min, max) {
        return Math.random() * (max - min) + min;
    }

    static isNumber(value) {
        return typeof value === 'number' && !isNaN(value);
    }
}

// Usage
const math = new MathHelper(10);
math.add(5).add(3);  // Instance chaining

console.log(MathHelper.PI);  // Static property
console.log(MathHelper.random(1, 10));  // Static method
```

### Tip 6: Getters and Setters for Validation

```javascript
class User {
    #age;
    #email;

    constructor(name, email, age) {
        this.name = name;
        this.email = email;  // Uses setter
        this.age = age;       // Uses setter
    }

    get age() {
        return this.#age;
    }

    set age(value) {
        if (value < 0 || value > 150) {
            throw new Error('Age must be between 0 and 150');
        }
        this.#age = value;
    }

    get email() {
        return this.#email;
    }

    set email(value) {
        if (!/@/.test(value)) {
            throw new Error('Invalid email');
        }
        this.#email = value;
    }
}

// Usage
const user = new User('John', 'john@example.com', 30);
user.age = 200;  // Throws error
```

### Tip 7: Using Symbols for Privacy (Alternative to #)

```javascript
const _balance = Symbol('balance');

class BankAccount {
    constructor(initialBalance) {
        this[_balance] = initialBalance;
    }

    deposit(amount) {
        this[_balance] += amount;
    }

    getBalance() {
        return this[_balance];
    }
}

// More private than _ but less strict than #
// Symbol properties are not enumerable by default
```

### Tip 8: Composition over Inheritance

```javascript
// Behaviors as compositions
const canEat = {
    eat() { console.log('eating'); }
};

const canWalk = {
    walk() { console.log('walking'); }
};

const canFly = {
    fly() { console.log('flying'); }
};

class Dog {
    constructor(name) {
        this.name = name;
        Object.assign(this, canEat, canWalk);
    }
}

class Bird {
    constructor(name) {
        this.name = name;
        Object.assign(this, canEat, canFly);
    }
}

// Usage
const dog = new Dog('Rex');
dog.eat();
dog.walk();

const bird = new Bird('Tweet');
bird.eat();
bird.fly();
```

### Tip 9: Instanceof vs Duck Typing

```javascript
class Shape {
    area() { }
}

class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }

    area() {
        return Math.PI * this.radius ** 2;
    }
}

class FakeCircle {
    constructor(radius) {
        this.radius = radius;
    }

    area() {
        return Math.PI * this.radius ** 2;
    }
}

// Instanceof check
const real = new Circle(5);
console.log(real instanceof Shape);  // true

const fake = new FakeCircle(5);
console.log(fake instanceof Shape);  // false

// Duck typing - check behavior, not type
function getArea(obj) {
    return obj.area?.();  // Works with both
}

console.log(getArea(real));  // 78.54...
console.log(getArea(fake));  // 78.54...
```

### Tip 10: Constructor.name for Debugging

```javascript
class MyClass {
    constructor() {}
}

class OtherClass {
    constructor() {}
}

function getClassName(instance) {
    return instance.constructor.name;
}

const obj1 = new MyClass();
const obj2 = new OtherClass();

console.log(getClassName(obj1));  // 'MyClass'
console.log(getClassName(obj2));  // 'OtherClass'

// Useful for logging and debugging
```

## 7.9. Common Mistakes

### Mistake 1: Forgetting 'new' Keyword

```javascript
// BAD: Classes require 'new'
class Person {
    constructor(name) {
        this.name = name;
    }
}

const person = Person('John');  // TypeError

// GOOD
const person = new Person('John');
```

### Mistake 2: Forgetting 'super()' in Child Constructor

```javascript
// BAD: Missing super() call
class Animal {
    constructor(name) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        // ReferenceError: Must call super() before 'this'
        this.breed = breed;  // Error!
        super(name);  // Wrong order
    }
}

// GOOD
class Dog extends Animal {
    constructor(name, breed) {
        super(name);  // Call first!
        this.breed = breed;
    }
}
```

### Mistake 3: 'this' Context in Callbacks

```javascript
// BAD: 'this' is undefined
class Counter {
    count = 0;

    increment() {
        this.count++;
    }

    start() {
        setInterval(function() {
            this.increment();  // Error: this is undefined
        }, 1000);
    }
}

// GOOD: Use arrow function
class Counter {
    count = 0;

    increment() {
        this.count++;
    }

    start() {
        setInterval(() => {
            this.increment();  // 'this' preserved
        }, 1000);
    }
}

// Or use bind()
setInterval(this.increment.bind(this), 1000);
```

### Mistake 4: Modifying Private Fields from Outside

```javascript
// BAD: Trying to access private field
class Account {
    #balance = 0;

    getBalance() {
        return this.#balance;
    }
}

const account = new Account();
console.log(account.#balance);  // SyntaxError

// GOOD: Use public method
console.log(account.getBalance());
```

### Mistake 5: Static Methods Using 'this'

```javascript
// BAD: Confusion about 'this' in static
class User {
    static count = 0;

    constructor(name) {
        this.name = name;
        this.count++;  // References instance, not static!
    }
}

// GOOD
class User {
    static count = 0;

    constructor(name) {
        this.name = name;
        User.count++;  // Reference class directly
    }
}
```

### Mistake 6: Forgetting Property Initialization

```javascript
// BAD: Using undefined properties
class User {
    constructor(name) {
        this.name = name;
        // this.email not initialized
    }

    getInfo() {
        return `${this.name} (${this.email})`;  // undefined!
    }
}

// GOOD: Initialize all properties
class User {
    constructor(name, email = '') {
        this.name = name;
        this.email = email;
    }

    getInfo() {
        return `${this.name} (${this.email})`;
    }
}
```

### Mistake 7: Shallow Copy in Constructor

```javascript
// BAD: Shared reference
class Config {
    constructor(options = {}) {
        this.options = options;  // Same reference
    }
}

const defaults = { debug: false };
const config1 = new Config(defaults);
const config2 = new Config(defaults);

config1.options.debug = true;
console.log(config2.options.debug);  // true! Should be false

// GOOD: Deep copy
class Config {
    constructor(options = {}) {
        this.options = { ...options };  // New object
    }
}
```

### Mistake 8: Method Names Conflict

```javascript
// BAD: Name collision with inherited methods
class MyArray extends Array {
    constructor() {
        super();
        this.map = 'custom';  // Shadows Array.prototype.map
    }
}

const arr = new MyArray();
arr.push(1, 2, 3);
arr.map(x => x * 2);  // Error: this.map is not a function

// GOOD: Use different names
class MyArray extends Array {
    constructor() {
        super();
        this.customMap = (fn) => this.map(fn);
    }
}
```

### Mistake 9: Missing Return in Getter

```javascript
// BAD: Getter doesn't return
class Circle {
    constructor(radius) {
        this._radius = radius;
    }

    get radius() {
        this._radius;  // No return!
    }
}

const circle = new Circle(5);
console.log(circle.radius);  // undefined

// GOOD
class Circle {
    constructor(radius) {
        this._radius = radius;
    }

    get radius() {
        return this._radius;
    }
}
```

### Mistake 10: Constructor Does Too Much

```javascript
// BAD: Too many responsibilities
class User {
    constructor(name, email, password) {
        this.name = name;
        this.email = email;
        this.password = this.#hash(password);
        this.validate();
        this.save();  // Side effects in constructor!
    }
}

// GOOD: Separate concerns
class User {
    constructor(name, email, password) {
        this.name = name;
        this.email = email;
        this.password = this.#hash(password);
    }

    validate() {
        // Validation logic
    }

    save() {
        // Save logic
    }
}

// Create and setup separately
const user = new User('John', 'john@example.com', 'pass');
if (user.validate()) {
    user.save();
}
```

## 7.10. Troubleshooting Issues

### Issue 1: Accessing Parent Method in Child Class

**Problem:**
```javascript
class Animal {
    speak() {
        console.log('Animal sound');
    }
}

class Dog extends Animal {
    speak() {
        console.log('Woof!');
        // How to call parent method?
    }
}
```

**Solution:**
```javascript
class Dog extends Animal {
    speak() {
        super.speak();  // Call parent method
        console.log('Woof!');
    }
}
```

### Issue 2: Passing Arguments to Parent Constructor

**Problem:**
```javascript
class Vehicle {
    constructor(make, model) {
        this.make = make;
        this.model = model;
    }
}

class Car extends Vehicle {
    constructor(make, model, doors) {
        // How to pass to parent?
    }
}
```

**Solution:**
```javascript
class Car extends Vehicle {
    constructor(make, model, doors) {
        super(make, model);  // Pass to parent
        this.doors = doors;
    }
}
```

### Issue 3: Private Field Scope

**Problem:**
```javascript
class Parent {
    #secret = 'parent';
}

class Child extends Parent {
    getSecret() {
        return this.#secret;  // Error!
    }
}
```

**Solution:**
```javascript
// Each class has its own private space
class Parent {
    #secret = 'parent';

    getSecret() {
        return this.#secret;
    }
}

class Child extends Parent {
    getParentSecret() {
        return this.getSecret();  // Call parent method
    }
}
```

### Issue 4: Getters/Setters with Private Fields

**Problem:**
```javascript
class User {
    constructor(age) {
        this.age = age;  // Doesn't use setter!
    }

    set age(value) {
        if (value < 0) throw new Error('Invalid');
        this._age = value;
    }

    get age() {
        return this._age;
    }
}
```

**Solution:**
```javascript
class User {
    #age;

    constructor(age) {
        this.age = age;  // Uses setter
    }

    set age(value) {
        if (value < 0) throw new Error('Invalid');
        this.#age = value;
    }

    get age() {
        return this.#age;
    }
}
```

### Issue 5: Class Expression vs Declaration

**Problem:**
```javascript
// Named class expression
const MyClass = class OtherName {
    getName() {
        return OtherName.name;  // 'OtherName'
    }
};

console.log(MyClass.name);  // 'OtherName'
```

**Solution:**
```javascript
// Keep it simple: use class declaration
class MyClass {
    getName() {
        return MyClass.name;  // 'MyClass'
    }
}

// Or consistent class expression
const MyClass = class {
    getName() {
        return MyClass.name;  // 'MyClass'
    }
};
```

### Issue 6: Extending Built-in Classes

**Problem:**
```javascript
class MyArray extends Array {
    doubleAll() {
        return this.map(x => x * 2);
    }
}

const arr = new MyArray(1, 2, 3);
const doubled = arr.doubleAll();
console.log(doubled instanceof MyArray);  // false!
```

**Solution:**
```javascript
class MyArray extends Array {
    doubleAll() {
        return new MyArray(...this.map(x => x * 2));
    }
}

const arr = new MyArray(1, 2, 3);
const doubled = arr.doubleAll();
console.log(doubled instanceof MyArray);  // true
```

### Issue 7: Serialization with Classes

**Problem:**
```javascript
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    getInfo() {
        return `${this.name}: ${this.email}`;
    }
}

const user = new User('John', 'john@example.com');
const json = JSON.stringify(user);
const parsed = JSON.parse(json);

console.log(parsed.getInfo());  // Error: not a function
```

**Solution:**
```javascript
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    toJSON() {
        return { name: this.name, email: this.email };
    }

    static fromJSON(json) {
        const obj = typeof json === 'string' ? JSON.parse(json) : json;
        return new User(obj.name, obj.email);
    }

    getInfo() {
        return `${this.name}: ${this.email}`;
    }
}

const user = new User('John', 'john@example.com');
const json = JSON.stringify(user);
const parsed = User.fromJSON(json);
console.log(parsed.getInfo());  // Works!
```

### Issue 8: Memory Leaks with Event Listeners

**Problem:**
```javascript
class Component {
    constructor(element) {
        this.element = element;
        this.handler = () => this.onClick();
        this.element.addEventListener('click', this.handler);
    }

    onClick() {
        console.log('clicked');
    }

    // Listener never removed - memory leak!
}
```

**Solution:**
```javascript
class Component {
    constructor(element) {
        this.element = element;
        this.handler = () => this.onClick();
        this.element.addEventListener('click', this.handler);
    }

    onClick() {
        console.log('clicked');
    }

    destroy() {
        this.element.removeEventListener('click', this.handler);
    }
}
```

### Issue 9: Multiple Inheritance

**Problem:**
```javascript
// JavaScript doesn't support multiple inheritance
class Dog extends Animal, Trainable {  // Syntax error
}
```

**Solution:**
```javascript
// Use composition or mixins
const Trainable = {
    train() { }
};

const Flyable = {
    fly() { }
};

class Dog extends Animal {
    constructor(name) {
        super(name);
        Object.assign(this, Trainable);
    }
}

// Or use mixins
function Trainable(Class) {
    return class extends Class {
        train() { }
    };
}

class Dog extends Trainable(Animal) {
    constructor(name) {
        super(name);
    }
}
```

### Issue 10: Static Inheritance

**Problem:**
```javascript
class Parent {
    static getName() {
        return 'Parent';
    }
}

class Child extends Parent {
    // Static methods inherited
}

console.log(Child.getName());  // 'Parent'
```

**Solution:**
```javascript
class Parent {
    static getName() {
        return this.name;  // Use 'this' for polymorphism
    }
}

class Child extends Parent {
    // Inherited static method works correctly
}

console.log(Child.getName());  // 'Child'
console.log(Parent.getName());  // 'Parent'
```

## 7.11. Advanced Topics

### Topic 1: Mixin Pattern

```javascript
// Create reusable behaviors
const Loggable = {
    log(msg) {
        console.log(`[${this.constructor.name}] ${msg}`);
    }
};

const Saveable = {
    save() {
        console.log('Saving...');
        this.log('Saved successfully');
    }
};

// Apply to class
class User {
    constructor(name) {
        this.name = name;
    }
}

Object.assign(User.prototype, Loggable, Saveable);

const user = new User('John');
user.log('Created');
user.save();
```

### Topic 2: Decorator Pattern

```javascript
function cached(target, property, descriptor) {
    const originalMethod = descriptor.value;
    const cache = new Map();

    descriptor.value = function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }

        const result = originalMethod.apply(this, args);
        cache.set(key, result);
        return result;
    };

    return descriptor;
}

class Calculator {
    @cached
    expensive(n) {
        console.log(`Computing ${n}...`);
        return n * n;
    }
}
```

### Topic 3: Observer Pattern

```javascript
class Subject {
    #observers = [];

    subscribe(observer) {
        this.#observers.push(observer);
        return () => {
            this.#observers = this.#observers.filter(o => o !== observer);
        };
    }

    notify(data) {
        this.#observers.forEach(obs => obs.update(data));
    }
}

class Observer {
    update(data) {
        console.log('Updated:', data);
    }
}

// Usage
const subject = new Subject();
const observer1 = new Observer();
const observer2 = new Observer();

subject.subscribe(observer1);
subject.subscribe(observer2);

subject.notify({ message: 'Hello' });
```

### Topic 4: Builder Pattern

```javascript
class QueryBuilder {
    #query = {};

    select(fields) {
        this.#query.select = fields;
        return this;
    }

    from(table) {
        this.#query.from = table;
        return this;
    }

    where(condition) {
        this.#query.where = condition;
        return this;
    }

    orderBy(field, direction = 'ASC') {
        this.#query.orderBy = { field, direction };
        return this;
    }

    limit(count) {
        this.#query.limit = count;
        return this;
    }

    build() {
        return this.#query;
    }
}

// Usage
const query = new QueryBuilder()
    .select(['id', 'name', 'email'])
    .from('users')
    .where('age > 18')
    .orderBy('name')
    .limit(10)
    .build();
```

### Topic 5: Strategy Pattern

```javascript
class PaymentProcessor {
    constructor(strategy) {
        this.strategy = strategy;
    }

    setStrategy(strategy) {
        this.strategy = strategy;
    }

    process(amount) {
        return this.strategy.pay(amount);
    }
}

class CreditCardStrategy {
    pay(amount) {
        console.log(`Processing $${amount} via Credit Card`);
        return true;
    }
}

class PayPalStrategy {
    pay(amount) {
        console.log(`Processing $${amount} via PayPal`);
        return true;
    }
}

class CryptoStrategy {
    pay(amount) {
        console.log(`Processing $${amount} via Crypto`);
        return true;
    }
}

// Usage
const processor = new PaymentProcessor(new CreditCardStrategy());
processor.process(100);

processor.setStrategy(new PayPalStrategy());
processor.process(200);

processor.setStrategy(new CryptoStrategy());
processor.process(50);
```

## 7.12. Exercises

### Exercise 1 (Dễ): Rectangle Class

```javascript
// Create a Rectangle class with:
// - constructor(width, height)
// - area() method: returns width * height
// - perimeter() method: returns 2 * (width + height)
// - isSquare() method: returns true if width === height
```

### Exercise 2 (Dễ): Counter Class

```javascript
// Create Counter class:
// - constructor(initialValue = 0)
// - increment() method
// - decrement() method
// - reset() method
// - getCount() getter
```

### Exercise 3 (Dễ): Temperature Converter

```javascript
// Create Temperature class:
// - constructor(celsius)
// - fahrenheit getter/setter
// - kelvin getter
// - isDangerous() method: true if > 50°C
```

### Exercise 4 (Dễ): Person Class with Inheritance

```javascript
// Person class with name, age
// Employee extends Person with salary
// Manager extends Employee with department

// Usage:
// const emp = new Employee('John', 30, 50000);
// const mgr = new Manager('Jane', 35, 80000, 'IT');
```

### Exercise 5 (Trung bình): Stack Data Structure

```javascript
// Create Stack class:
// - push(item)
// - pop() returns removed item
// - peek() returns top item without removing
// - isEmpty() returns boolean
// - size getter
// - clear()
```

### Exercise 6 (Trung bình): Bank Account with Transactions

```javascript
// Account class:
// - Private balance
// - deposit(amount) with transaction log
// - withdraw(amount) with validation
// - transfer(target, amount)
// - getTransactionHistory()
```

### Exercise 7 (Trung bình): Form Validator

```javascript
// Validator class:
// - addRule(fieldName, rule)
// - validate(data)
// - getErrors()
// Should support: required, minLength, email, custom rules
```

### Exercise 8 (Trung bình): Event System

```javascript
// EventEmitter class:
// - on(event, handler)
// - once(event, handler)
// - off(event, handler)
// - emit(event, ...args)
// - listenerCount(event)
```

### Exercise 9 (Khó): Plugin System

```javascript
// Create Plugin system:
// - PluginManager class
// - register(name, PluginClass)
// - execute(name, config)
// - Each plugin extends Plugin base class
// - Plugins can have dependencies
```

### Exercise 10 (Khó): ORM (Object-Relational Mapping)

```javascript
// Simple ORM:
// - Model base class
// - Model.find(id)
// - Model.findAll()
// - save()
// - delete()
// - Relationships (hasMany, belongsTo)
```

### Exercise 11 (Khó): Middleware Pipeline

```javascript
// Request-Response middleware system:
// - Pipeline class
// - use(middleware)
// - execute(context)
// - Each middleware can modify context
// - Error handling
```

### Exercise 12 (Khó): Type-Safe Store with Proxy

```javascript
// Create typed store:
// - Store<T> with type validation
// - Proxy-based field tracking
// - Watch(key, callback) for changes
// - getChanges() to track modifications
// - rollback() functionality
```

---

**Kết luận:** Classes trong ES6 cung cấp syntax rõ ràng hơn cho OOP trong JavaScript. Hỗ trợ inheritance, encapsulation với private fields, static members, và các design patterns. Sử dụng composition khi cần tính linh hoạt.

**Chương tiếp theo:** Modules (Import/Export)
