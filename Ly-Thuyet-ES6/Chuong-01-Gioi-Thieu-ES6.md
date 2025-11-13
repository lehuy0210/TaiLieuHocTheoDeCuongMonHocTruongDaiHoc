# CHƯƠNG 1: GIỚI THIỆU ES6

## 1.1. ES6 (ES2015) là gì?

ES6 (ECMAScript 2015) là phiên bản lớn nhất của JavaScript, được release năm 2015 với nhiều tính năng mới.

### 1.1.1. Lịch sử

- **1995**: JavaScript được tạo ra bởi Brendan Eich
- **1997**: ES1 - First edition
- **1999**: ES3
- **2009**: ES5
- **2015**: ES6/ES2015 - Major update
- **2016+**: Yearly releases (ES2016, ES2017, ...)

### 1.1.2. Tại sao học ES6?

- Modern JavaScript syntax
- Cleaner và readable code
- Powerful features
- Industry standard
- Required cho frameworks (React, Vue, Angular)

## 1.2. Browser Support

**Modern Browsers:**
- Chrome 51+
- Firefox 54+
- Safari 10+
- Edge 15+

**Transpilers (cho old browsers):**
- Babel
- TypeScript

## 1.3. ES6 Features Overview

### 1.3.1. Các tính năng chính

1. **let & const** - Block-scoped variables
2. **Arrow Functions** - Shorter function syntax
3. **Template Literals** - String interpolation
4. **Destructuring** - Extract values from objects/arrays
5. **Spread & Rest** - Spread/collect elements
6. **Classes** - OOP syntax
7. **Modules** - Import/Export
8. **Promises** - Async operations
9. **Default Parameters** - Function parameters
10. **Enhanced Object Literals** - Object shortcuts

## 1.4. Quick Comparison: ES5 vs ES6

### 1.4.1. Variables

**ES5:**
```javascript
var name = 'John';
```

**ES6:**
```javascript
let name = 'John';
const AGE = 30;
```

### 1.4.2. Functions

**ES5:**
```javascript
function add(a, b) {
    return a + b;
}
```

**ES6:**
```javascript
const add = (a, b) => a + b;
```

### 1.4.3. String Concatenation

**ES5:**
```javascript
var greeting = 'Hello, ' + name + '!';
```

**ES6:**
```javascript
const greeting = `Hello, ${name}!`;
```

### 1.4.4. Objects

**ES5:**
```javascript
var obj = {
    name: name,
    age: age,
    greet: function() {
        console.log('Hello');
    }
};
```

**ES6:**
```javascript
const obj = {
    name,
    age,
    greet() {
        console.log('Hello');
    }
};
```

## 1.5. Setup Environment

### 1.5.1. Node.js

```bash
# Check Node version
node --version

# Run ES6 code
node script.js
```

### 1.5.2. Browser Console

```javascript
// Chrome DevTools Console
console.log('ES6 works!');
```

### 1.5.3. VS Code

**Recommended extensions:**
- ESLint
- Prettier
- JavaScript (ES6) code snippets

## 1.6. Hello World

```javascript
// ES6 Hello World
const message = 'Hello, ES6!';
console.log(message);

// Arrow function
const greet = (name) => {
    console.log(`Hello, ${name}!`);
};

greet('World');
```

## 1.7. Strict Mode

```javascript
'use strict';

// Prevents common mistakes
x = 10; // Error: x is not defined
```

## 1.8. Resources

- MDN JavaScript Documentation
- javascript.info
- ES6 Features (github.com/lukehoban/es6features)
- Babel REPL (để test code)

## 1.9. Practical Code Examples

### Example 1: Real-world ES6 Application Setup

```javascript
// Modern ES6 application structure
'use strict';

// Configuration with ES6 features
const appConfig = {
    name: 'MyApp',
    version: '1.0.0',
    env: process.env.NODE_ENV || 'development',

    // Enhanced object literal method
    getInfo() {
        return `${this.name} v${this.version} (${this.env})`;
    },

    // Computed property names
    [`${process.env.NODE_ENV}_API`]: 'https://api.example.com'
};

// Template literals for logging
console.log(`Starting ${appConfig.getInfo()}`);

// Arrow functions for callbacks
const features = ['let/const', 'arrow functions', 'template literals'];
features.forEach(feature => console.log(`✓ ${feature}`));

// Destructuring
const { name, version } = appConfig;
console.log(`App: ${name}, Version: ${version}`);
```

### Example 2: Data Processing with ES6

```javascript
// Working with user data
const users = [
    { id: 1, name: 'John Doe', age: 25, role: 'developer' },
    { id: 2, name: 'Jane Smith', age: 30, role: 'designer' },
    { id: 3, name: 'Bob Johnson', age: 28, role: 'developer' }
];

// Filter developers using arrow functions
const developers = users.filter(user => user.role === 'developer');

// Map to extract names with template literals
const developerNames = developers.map(dev => `${dev.name} (${dev.age} years)`);

console.log('Developers:', developerNames);
// Output: ['John Doe (25 years)', 'Bob Johnson (28 years)']

// Find specific user
const jane = users.find(user => user.name === 'Jane Smith');
console.log(`Found: ${jane.name}, Role: ${jane.role}`);

// Check if all developers are over 20
const allAdults = developers.every(dev => dev.age > 20);
console.log(`All developers are adults: ${allAdults}`);
```

### Example 3: ES6 Class for API Service

```javascript
// Modern API service class
class APIService {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.headers = {
            'Content-Type': 'application/json'
        };
    }

    // Method using template literals and arrow functions
    async fetchData(endpoint) {
        try {
            const response = await fetch(`${this.baseURL}/${endpoint}`, {
                headers: this.headers
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`API Error: ${error.message}`);
            throw error;
        }
    }

    // Method with default parameters
    async postData(endpoint, data = {}) {
        const response = await fetch(`${this.baseURL}/${endpoint}`, {
            method: 'POST',
            headers: this.headers,
            body: JSON.stringify(data)
        });

        return response.json();
    }
}

// Usage
const api = new APIService('https://api.example.com');
api.fetchData('users')
    .then(users => console.log('Users:', users))
    .catch(err => console.error('Error:', err));
```

### Example 4: Module Pattern with ES6

```javascript
// utils.js - Export utilities
export const formatCurrency = (amount, currency = 'USD') => {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency
    }).format(amount);
};

export const formatDate = (date) => {
    return new Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(new Date(date));
};

export class Logger {
    static log(message, level = 'info') {
        const timestamp = new Date().toISOString();
        console.log(`[${timestamp}] [${level.toUpperCase()}] ${message}`);
    }

    static error(message) {
        this.log(message, 'error');
    }

    static warn(message) {
        this.log(message, 'warn');
    }
}

// main.js - Import and use
import { formatCurrency, formatDate, Logger } from './utils.js';

const price = 1234.56;
Logger.log(`Price: ${formatCurrency(price)}`);
Logger.log(`Date: ${formatDate(new Date())}`);
```

### Example 5: Promise-based Workflow

```javascript
// Simulating async operations with Promises
const fetchUserData = (userId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (userId > 0) {
                resolve({
                    id: userId,
                    name: `User ${userId}`,
                    email: `user${userId}@example.com`
                });
            } else {
                reject(new Error('Invalid user ID'));
            }
        }, 1000);
    });
};

const fetchUserPosts = (userId) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve([
                { id: 1, title: 'First Post', userId },
                { id: 2, title: 'Second Post', userId }
            ]);
        }, 800);
    });
};

// Using Promise.all for parallel requests
const loadUserProfile = async (userId) => {
    try {
        const [user, posts] = await Promise.all([
            fetchUserData(userId),
            fetchUserPosts(userId)
        ]);

        return {
            ...user,
            posts,
            postCount: posts.length
        };
    } catch (error) {
        console.error(`Error loading profile: ${error.message}`);
        throw error;
    }
};

// Usage
loadUserProfile(1).then(profile => {
    console.log('User Profile:', profile);
    console.log(`${profile.name} has ${profile.postCount} posts`);
});
```

### Example 6: Advanced Destructuring & Spread

```javascript
// Working with complex data structures
const product = {
    id: 101,
    name: 'Laptop',
    price: 999,
    specs: {
        cpu: 'Intel i7',
        ram: '16GB',
        storage: '512GB SSD'
    },
    tags: ['electronics', 'computers', 'featured']
};

// Nested destructuring
const {
    name,
    price,
    specs: { cpu, ram },
    tags: [firstTag, ...otherTags]
} = product;

console.log(`${name} - $${price}`);
console.log(`CPU: ${cpu}, RAM: ${ram}`);
console.log(`Primary tag: ${firstTag}, Others: ${otherTags.join(', ')}`);

// Spread operator for object merging
const discount = 0.1;
const productOnSale = {
    ...product,
    originalPrice: price,
    price: price * (1 - discount),
    onSale: true
};

console.log('Sale Product:', productOnSale);

// Spread for array operations
const newTags = ['bestseller', 'premium'];
const allTags = [...product.tags, ...newTags];
console.log('All tags:', allTags);
```

### Example 7: Iterators and Generators Preview

```javascript
// Generator function for custom iteration
function* idGenerator() {
    let id = 1;
    while (true) {
        yield id++;
    }
}

const gen = idGenerator();
console.log(gen.next().value); // 1
console.log(gen.next().value); // 2
console.log(gen.next().value); // 3

// Custom iterable object
const range = {
    start: 1,
    end: 5,

    [Symbol.iterator]() {
        let current = this.start;
        const end = this.end;

        return {
            next() {
                if (current <= end) {
                    return { value: current++, done: false };
                }
                return { done: true };
            }
        };
    }
};

// Using for...of with custom iterable
for (const num of range) {
    console.log(num); // 1, 2, 3, 4, 5
}

// Array from iterable
const numbers = [...range];
console.log('Numbers:', numbers); // [1, 2, 3, 4, 5]
```

## 1.10. Real-World Use Cases

### Use Case 1: E-commerce Shopping Cart

```javascript
// Shopping cart with ES6 features
class ShoppingCart {
    constructor() {
        this.items = [];
    }

    addItem(product, quantity = 1) {
        const existingItem = this.items.find(item => item.product.id === product.id);

        if (existingItem) {
            existingItem.quantity += quantity;
        } else {
            this.items.push({ product, quantity });
        }

        console.log(`Added ${quantity}x ${product.name} to cart`);
    }

    removeItem(productId) {
        this.items = this.items.filter(item => item.product.id !== productId);
    }

    get total() {
        return this.items.reduce((sum, item) =>
            sum + (item.product.price * item.quantity), 0
        );
    }

    get itemCount() {
        return this.items.reduce((count, item) => count + item.quantity, 0);
    }

    checkout() {
        const summary = {
            items: this.items.map(({ product, quantity }) => ({
                name: product.name,
                quantity,
                subtotal: product.price * quantity
            })),
            total: this.total,
            itemCount: this.itemCount
        };

        return summary;
    }
}

// Usage
const cart = new ShoppingCart();
cart.addItem({ id: 1, name: 'Laptop', price: 999 }, 1);
cart.addItem({ id: 2, name: 'Mouse', price: 29 }, 2);

const summary = cart.checkout();
console.log(`Total: $${summary.total} (${summary.itemCount} items)`);
```

### Use Case 2: Form Validation

```javascript
// Modern form validation
class FormValidator {
    constructor(rules) {
        this.rules = rules;
    }

    validate(data) {
        const errors = {};

        for (const [field, validators] of Object.entries(this.rules)) {
            const value = data[field];

            for (const validator of validators) {
                const error = validator(value, data);
                if (error) {
                    errors[field] = errors[field] || [];
                    errors[field].push(error);
                }
            }
        }

        return {
            isValid: Object.keys(errors).length === 0,
            errors
        };
    }
}

// Validator functions
const required = (value) => !value ? 'This field is required' : null;
const email = (value) =>
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) ? 'Invalid email' : null;
const minLength = (min) => (value) =>
    value.length < min ? `Minimum ${min} characters required` : null;

// Usage
const validator = new FormValidator({
    username: [required, minLength(3)],
    email: [required, email],
    password: [required, minLength(8)]
});

const formData = {
    username: 'jo',
    email: 'invalid-email',
    password: '123'
};

const result = validator.validate(formData);
console.log('Validation result:', result);
```

### Use Case 3: Data Transformation Pipeline

```javascript
// Functional data processing pipeline
const processData = (data) => {
    return data
        .filter(item => item.active)
        .map(item => ({
            ...item,
            fullName: `${item.firstName} ${item.lastName}`,
            age: new Date().getFullYear() - item.birthYear
        }))
        .sort((a, b) => b.age - a.age)
        .slice(0, 10);
};

const users = [
    { id: 1, firstName: 'John', lastName: 'Doe', birthYear: 1990, active: true },
    { id: 2, firstName: 'Jane', lastName: 'Smith', birthYear: 1985, active: true },
    { id: 3, firstName: 'Bob', lastName: 'Johnson', birthYear: 1995, active: false }
];

const processed = processData(users);
console.log('Top active users:', processed);
```

### Use Case 4: Event Handling System

```javascript
// Modern event emitter
class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    on(event, callback) {
        if (!this.events.has(event)) {
            this.events.set(event, []);
        }
        this.events.get(event).push(callback);

        // Return unsubscribe function
        return () => this.off(event, callback);
    }

    off(event, callback) {
        if (!this.events.has(event)) return;

        const callbacks = this.events.get(event);
        const index = callbacks.indexOf(callback);
        if (index > -1) {
            callbacks.splice(index, 1);
        }
    }

    emit(event, ...args) {
        if (!this.events.has(event)) return;

        this.events.get(event).forEach(callback => {
            callback(...args);
        });
    }

    once(event, callback) {
        const onceCallback = (...args) => {
            callback(...args);
            this.off(event, onceCallback);
        };
        this.on(event, onceCallback);
    }
}

// Usage
const emitter = new EventEmitter();

const unsubscribe = emitter.on('user:login', (user) => {
    console.log(`User logged in: ${user.name}`);
});

emitter.once('app:ready', () => {
    console.log('Application is ready!');
});

emitter.emit('user:login', { name: 'John Doe' });
emitter.emit('app:ready');
```

### Use Case 5: Async Data Fetcher with Retry

```javascript
// Robust data fetcher with retry logic
class DataFetcher {
    constructor(baseURL, maxRetries = 3) {
        this.baseURL = baseURL;
        this.maxRetries = maxRetries;
    }

    async fetchWithRetry(endpoint, retries = 0) {
        try {
            const response = await fetch(`${this.baseURL}/${endpoint}`);

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            if (retries < this.maxRetries) {
                console.log(`Retry ${retries + 1}/${this.maxRetries} for ${endpoint}`);
                await this.delay(1000 * Math.pow(2, retries)); // Exponential backoff
                return this.fetchWithRetry(endpoint, retries + 1);
            }

            throw error;
        }
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async fetchMultiple(endpoints) {
        return Promise.all(
            endpoints.map(endpoint => this.fetchWithRetry(endpoint))
        );
    }
}

// Usage
const fetcher = new DataFetcher('https://api.example.com', 3);
fetcher.fetchWithRetry('users/1')
    .then(data => console.log('User data:', data))
    .catch(error => console.error('Failed after retries:', error));
```

## 1.11. Tips & Tricks

### Tip 1: Use const by Default
```javascript
// Good practice
const PI = 3.14159;
const users = [];

// Only use let when reassignment is needed
let counter = 0;
counter++;
```

### Tip 2: Destructuring for Function Parameters
```javascript
// Instead of
function createUser(name, age, email) {
    // ...
}

// Use destructuring
function createUser({ name, age, email }) {
    console.log(`Creating user: ${name}, ${age}, ${email}`);
}

createUser({ name: 'John', age: 25, email: 'john@example.com' });
```

### Tip 3: Template Literals for Multi-line Strings
```javascript
// Old way
const html = '<div>\n' +
    '  <h1>Title</h1>\n' +
    '  <p>Content</p>\n' +
    '</div>';

// ES6 way
const htmlES6 = `
    <div>
        <h1>Title</h1>
        <p>Content</p>
    </div>
`;
```

### Tip 4: Arrow Functions for Array Methods
```javascript
const numbers = [1, 2, 3, 4, 5];

// Concise array operations
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((acc, n) => acc + n, 0);

console.log({ doubled, evens, sum });
```

### Tip 5: Object Shorthand
```javascript
const name = 'John';
const age = 30;

// Old way
const user1 = { name: name, age: age };

// ES6 shorthand
const user2 = { name, age };
```

### Tip 6: Default Parameters
```javascript
// Avoid manual default checks
function greet(name = 'Guest', greeting = 'Hello') {
    return `${greeting}, ${name}!`;
}

console.log(greet()); // "Hello, Guest!"
console.log(greet('John')); // "Hello, John!"
console.log(greet('Jane', 'Hi')); // "Hi, Jane!"
```

### Tip 7: Spread for Array/Object Copying
```javascript
// Safe array copy
const original = [1, 2, 3];
const copy = [...original];

// Safe object copy (shallow)
const user = { name: 'John', age: 30 };
const userCopy = { ...user };
```

### Tip 8: Optional Chaining (ES2020)
```javascript
// Safe property access
const user = { profile: { name: 'John' } };

// Without optional chaining
const name1 = user && user.profile && user.profile.name;

// With optional chaining
const name2 = user?.profile?.name;
```

### Tip 9: Nullish Coalescing (ES2020)
```javascript
// Better than || for default values
const value1 = 0;
const result1 = value1 || 10; // 10 (unexpected!)
const result2 = value1 ?? 10; // 0 (correct!)

const value2 = null;
const result3 = value2 ?? 'default'; // 'default'
```

### Tip 10: Use async/await for Cleaner Async Code
```javascript
// Promise chains (harder to read)
fetch('api/users')
    .then(res => res.json())
    .then(users => fetch(`api/posts/${users[0].id}`))
    .then(res => res.json())
    .then(posts => console.log(posts));

// async/await (cleaner)
async function getUserPosts() {
    const usersRes = await fetch('api/users');
    const users = await usersRes.json();
    const postsRes = await fetch(`api/posts/${users[0].id}`);
    const posts = await postsRes.json();
    console.log(posts);
}
```

## 1.12. Common Mistakes

### Mistake 1: Confusing let/const with var
```javascript
// BAD: Using var in modern code
var x = 10;
if (true) {
    var x = 20; // Same variable!
}
console.log(x); // 20

// GOOD: Using let for block scope
let y = 10;
if (true) {
    let y = 20; // Different variable
}
console.log(y); // 10
```

### Mistake 2: Arrow Function and 'this' Context
```javascript
// BAD: Arrow function in object methods
const obj = {
    name: 'John',
    greet: () => {
        console.log(`Hello, ${this.name}`); // 'this' is not obj!
    }
};

// GOOD: Regular function for methods
const obj2 = {
    name: 'John',
    greet() {
        console.log(`Hello, ${this.name}`);
    }
};
```

### Mistake 3: Forgetting to Return in Arrow Functions
```javascript
// BAD: Missing return
const double = (n) => {
    n * 2; // No return!
};

// GOOD: Implicit return
const double2 = (n) => n * 2;

// Or explicit return
const double3 = (n) => {
    return n * 2;
};
```

### Mistake 4: Mutating const Objects/Arrays
```javascript
// MISTAKE: Thinking const makes objects immutable
const user = { name: 'John' };
user.name = 'Jane'; // This works! const doesn't prevent mutations
user.age = 30; // This also works!

// CORRECT: const prevents reassignment
// user = { name: 'Bob' }; // Error!

// To make truly immutable, use Object.freeze()
const immutableUser = Object.freeze({ name: 'John' });
// immutableUser.name = 'Jane'; // Silent fail in non-strict, error in strict mode
```

### Mistake 5: Template Literal Syntax Errors
```javascript
// BAD: Using quotes instead of backticks
const name = 'John';
const greeting = 'Hello, ${name}!'; // This won't interpolate!

// GOOD: Using backticks
const greeting2 = `Hello, ${name}!`; // Correct interpolation
```

### Mistake 6: Not Handling Promise Rejections
```javascript
// BAD: Unhandled promise rejection
fetch('api/data')
    .then(res => res.json()); // No error handling!

// GOOD: Always catch errors
fetch('api/data')
    .then(res => res.json())
    .catch(error => console.error('Error:', error));

// BETTER: With async/await
async function fetchData() {
    try {
        const res = await fetch('api/data');
        return await res.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}
```

### Mistake 7: Shallow vs Deep Copy
```javascript
// MISTAKE: Thinking spread does deep copy
const original = {
    name: 'John',
    address: { city: 'New York' }
};

const copy = { ...original };
copy.address.city = 'Boston'; // This mutates original too!

console.log(original.address.city); // 'Boston' (unexpected!)

// CORRECT: Deep copy when needed
const deepCopy = JSON.parse(JSON.stringify(original));
// Or use a library like lodash's cloneDeep
```

### Mistake 8: Destructuring with Different Names
```javascript
// BAD: Confusing syntax
const { name: name } = user; // Redundant

// GOOD: Renaming when needed
const { name: userName } = user; // Rename to userName

// GOOD: Same name shorthand
const { name } = user;
```

## 1.13. Troubleshooting

### Issue 1: "Unexpected token" Error

**Problem:**
```javascript
const message = `Hello ${name}`; // SyntaxError in old browsers
```

**Solution:**
```javascript
// Use Babel to transpile ES6 to ES5
// Install: npm install --save-dev @babel/core @babel/preset-env

// .babelrc
{
    "presets": ["@babel/preset-env"]
}
```

### Issue 2: Module Import Not Working

**Problem:**
```javascript
import { myFunction } from './utils.js';
// SyntaxError: Cannot use import statement outside a module
```

**Solution:**
```html
<!-- In HTML, add type="module" -->
<script type="module" src="main.js"></script>
```

Or in Node.js:
```json
// package.json
{
    "type": "module"
}
```

### Issue 3: 'this' is undefined in Arrow Function

**Problem:**
```javascript
class Counter {
    constructor() {
        this.count = 0;
    }

    increment = () => {
        setTimeout(() => {
            this.count++; // Works!
        }, 1000);
    }
}
```

**Explanation:**
Arrow functions inherit 'this' from parent scope, which is useful for callbacks.

### Issue 4: Cannot Reassign const

**Problem:**
```javascript
const PI = 3.14;
PI = 3.14159; // TypeError: Assignment to constant variable
```

**Solution:**
```javascript
// Use let if reassignment is needed
let value = 10;
value = 20; // OK

// Or use const for objects and mutate properties
const config = { theme: 'light' };
config.theme = 'dark'; // OK (property mutation)
```

### Issue 5: Async/Await Not Working

**Problem:**
```javascript
const data = await fetch('api/data'); // SyntaxError: await is only valid in async function
```

**Solution:**
```javascript
// Wrap in async function
async function fetchData() {
    const data = await fetch('api/data');
    return data;
}

// Or use top-level await (ES2022, in modules)
// In module scope:
const data = await fetch('api/data');
```

### Issue 6: Destructuring undefined

**Problem:**
```javascript
const { name } = undefined; // TypeError: Cannot destructure property 'name' of 'undefined'
```

**Solution:**
```javascript
// Provide default value
const { name } = undefined || {};

// Or use optional chaining with nullish coalescing
const obj = undefined;
const name = obj?.name ?? 'default';
```

## 1.14. Advanced Topics

### Advanced Topic 1: Proxy and Reflect

```javascript
// Creating a validation proxy
const createValidatedObject = (target, validators) => {
    return new Proxy(target, {
        set(obj, prop, value) {
            if (validators[prop]) {
                if (!validators[prop](value)) {
                    throw new Error(`Invalid value for ${prop}`);
                }
            }
            obj[prop] = value;
            return true;
        }
    });
};

// Usage
const userValidators = {
    age: (value) => typeof value === 'number' && value > 0,
    email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)
};

const user = createValidatedObject({}, userValidators);
user.age = 25; // OK
user.email = 'john@example.com'; // OK
// user.age = -5; // Error: Invalid value for age
```

### Advanced Topic 2: Symbol for Private Properties

```javascript
// Using Symbols for privacy
const _private = Symbol('private');

class BankAccount {
    constructor(balance) {
        this[_private] = { balance };
    }

    get balance() {
        return this[_private].balance;
    }

    deposit(amount) {
        if (amount > 0) {
            this[_private].balance += amount;
        }
    }

    withdraw(amount) {
        if (amount > 0 && amount <= this[_private].balance) {
            this[_private].balance -= amount;
            return amount;
        }
        return 0;
    }
}

const account = new BankAccount(1000);
console.log(account.balance); // 1000
account.deposit(500);
console.log(account.balance); // 1500
// account[_private] // Cannot access without the symbol
```

### Advanced Topic 3: Meta-programming with Reflect

```javascript
// Using Reflect for meta-programming
class SmartObject {
    constructor(data) {
        Object.assign(this, data);
    }

    static create(data) {
        return Reflect.construct(this, [data]);
    }

    hasProperty(prop) {
        return Reflect.has(this, prop);
    }

    getProperty(prop) {
        return Reflect.get(this, prop);
    }

    setProperty(prop, value) {
        return Reflect.set(this, prop, value);
    }

    deleteProperty(prop) {
        return Reflect.deleteProperty(this, prop);
    }
}

const obj = SmartObject.create({ name: 'John', age: 30 });
console.log(obj.hasProperty('name')); // true
console.log(obj.getProperty('age')); // 30
obj.setProperty('email', 'john@example.com');
```

### Advanced Topic 4: Custom Iterators

```javascript
// Creating custom iterable collections
class CustomCollection {
    constructor(items) {
        this.items = items;
    }

    *[Symbol.iterator]() {
        for (let item of this.items) {
            yield item;
        }
    }

    *reverse() {
        for (let i = this.items.length - 1; i >= 0; i--) {
            yield this.items[i];
        }
    }

    *filter(predicate) {
        for (let item of this.items) {
            if (predicate(item)) {
                yield item;
            }
        }
    }

    *map(mapper) {
        for (let item of this.items) {
            yield mapper(item);
        }
    }
}

const collection = new CustomCollection([1, 2, 3, 4, 5]);

// Normal iteration
for (const item of collection) {
    console.log(item); // 1, 2, 3, 4, 5
}

// Reverse iteration
for (const item of collection.reverse()) {
    console.log(item); // 5, 4, 3, 2, 1
}

// Filtered iteration
for (const item of collection.filter(x => x % 2 === 0)) {
    console.log(item); // 2, 4
}
```

### Advanced Topic 5: WeakMap for Private Data

```javascript
// Using WeakMap for truly private data
const privateData = new WeakMap();

class SecureUser {
    constructor(username, password) {
        privateData.set(this, {
            username,
            password: this.hashPassword(password)
        });
    }

    hashPassword(password) {
        // Simplified hash (use proper hashing in production)
        return btoa(password);
    }

    authenticate(password) {
        const data = privateData.get(this);
        return data.password === this.hashPassword(password);
    }

    get username() {
        return privateData.get(this).username;
    }
}

const user = new SecureUser('john', 'secret123');
console.log(user.username); // 'john'
console.log(user.authenticate('secret123')); // true
console.log(user.authenticate('wrong')); // false
// No way to access password directly!
```

## 1.15. Exercises

### Exercise 1: Convert ES5 to ES6
Convert the following ES5 code to ES6:
```javascript
// ES5 Code
var name = 'John';
var age = 30;

var user = {
    name: name,
    age: age,
    greet: function() {
        return 'Hello, ' + this.name;
    }
};

var users = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 }
];

var adults = users.filter(function(user) {
    return user.age >= 18;
});
```

### Exercise 2: Create a User Management Class
Create a `UserManager` class with the following features:
- Add user
- Remove user
- Find user by ID
- Get all users
- Use ES6 features (class, arrow functions, destructuring, etc.)

### Exercise 3: Async Data Loader
Create an async function that:
- Fetches user data from an API
- Fetches user's posts
- Combines the data
- Handles errors gracefully
- Use async/await, destructuring, and spread operator

### Exercise 4: Array Manipulation
Given an array of products:
```javascript
const products = [
    { id: 1, name: 'Laptop', price: 999, category: 'electronics' },
    { id: 2, name: 'Phone', price: 699, category: 'electronics' },
    { id: 3, name: 'Shirt', price: 29, category: 'clothing' }
];
```
Write functions to:
- Get all electronics
- Calculate total price
- Get product names only
- Group by category
Use ES6 array methods and arrow functions.

### Exercise 5: Template Literal Helper
Create a `template` function that:
- Takes a template string with placeholders
- Takes an object with values
- Returns the interpolated string
```javascript
// Example usage:
template('Hello, {name}! You are {age} years old.', { name: 'John', age: 30 });
// Output: "Hello, John! You are 30 years old."
```

### Exercise 6: Promise Chain
Create a promise chain that:
1. Simulates fetching user data (1 second delay)
2. Simulates fetching user's settings (1 second delay)
3. Combines both into a single object
4. Logs the result
Handle errors at each step.

### Exercise 7: Destructuring Exercise
Given this complex object:
```javascript
const data = {
    user: {
        id: 1,
        name: 'John',
        address: {
            city: 'New York',
            country: 'USA'
        }
    },
    posts: [
        { id: 1, title: 'First Post' },
        { id: 2, title: 'Second Post' }
    ]
};
```
Extract:
- User name
- City
- First post title
- All post titles as an array
Use destructuring for all extractions.

### Exercise 8: Module System
Create a math utility module with:
- Functions: add, subtract, multiply, divide
- Constants: PI, E
- A Calculator class
Export them properly and import in another file.

### Exercise 9: Event System
Build a simple event system with:
- `on(event, callback)` - subscribe to event
- `off(event, callback)` - unsubscribe from event
- `emit(event, data)` - trigger event
- `once(event, callback)` - subscribe once
Use ES6 classes and Map.

### Exercise 10: Data Transformer
Create a function that transforms this:
```javascript
const input = [
    { id: 1, name: 'John', score: 85 },
    { id: 2, name: 'Jane', score: 92 },
    { id: 3, name: 'Bob', score: 78 }
];
```
Into this:
```javascript
{
    'John': 85,
    'Jane': 92,
    'Bob': 78
}
```
Use reduce, destructuring, and object shorthand.

### Exercise 11: Custom Iterator
Create a `NumberRange` class that:
- Takes start and end values
- Is iterable using for...of
- Has a `step` method to skip numbers
```javascript
const range = new NumberRange(1, 10);
for (const num of range) {
    console.log(num); // 1, 2, 3, ..., 10
}

const evenRange = new NumberRange(0, 10).step(2);
for (const num of evenRange) {
    console.log(num); // 0, 2, 4, 6, 8, 10
}
```

### Exercise 12: Advanced Promise Handling
Create a `retry` function that:
- Takes an async function and max retries
- Retries on failure
- Uses exponential backoff
- Returns the result or throws after max retries
```javascript
const retry = async (fn, maxRetries = 3) => {
    // Your implementation
};

// Usage:
retry(() => fetch('https://api.example.com/data'), 3)
    .then(data => console.log(data))
    .catch(err => console.error('Failed after retries:', err));
```

---

**Chương tiếp theo:** Let, Const và Block Scope
