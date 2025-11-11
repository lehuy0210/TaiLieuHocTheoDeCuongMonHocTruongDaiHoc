# CHƯƠNG 8: MODULES (IMPORT/EXPORT)

## 8.1. Giới thiệu ES6 Modules

ES6 Modules cho phép chia code thành các files riêng biệt, dễ maintain và reuse.

### 8.1.1. Before ES6 Modules

**Global Scope (Bad):**
```javascript
// script1.js
var user = 'John';

// script2.js
console.log(user);  // Global variable
```

**CommonJS (Node.js):**
```javascript
// module.js
module.exports = { name: 'John' };

// main.js
const user = require('./module');
```

**ES6 Modules:**
```javascript
// module.js
export const name = 'John';

// main.js
import { name } from './module.js';
```

## 8.2. Export

### 8.2.1. Named Exports

```javascript
// math.js

// Export variables
export const PI = 3.14159;
export let count = 0;

// Export functions
export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

// Export classes
export class Calculator {
    multiply(a, b) {
        return a * b;
    }
}
```

### 8.2.2. Export List

```javascript
// math.js
const PI = 3.14159;
function add(a, b) {
    return a + b;
}
function subtract(a, b) {
    return a - b;
}

// Export at the end
export { PI, add, subtract };
```

### 8.2.3. Export with Rename

```javascript
// math.js
function add(a, b) {
    return a + b;
}

// Export with different name
export { add as sum };
```

### 8.2.4. Default Export

```javascript
// User.js
export default class User {
    constructor(name) {
        this.name = name;
    }
}

// Or
class User {
    constructor(name) {
        this.name = name;
    }
}
export default User;

// Function
export default function greet(name) {
    return `Hello, ${name}!`;
}

// Value
export default 42;
```

### 8.2.5. Mixed Exports

```javascript
// utils.js
export const VERSION = '1.0.0';

export function helper() {
    return 'helping...';
}

// Default export
export default class Utils {
    static log(message) {
        console.log(message);
    }
}
```

## 8.3. Import

### 8.3.1. Named Imports

```javascript
// Import specific exports
import { PI, add, subtract } from './math.js';

console.log(PI);        // 3.14159
console.log(add(5, 3)); // 8
```

### 8.3.2. Import with Rename

```javascript
// Rename on import
import { add as sum, subtract as diff } from './math.js';

console.log(sum(5, 3));  // 8
console.log(diff(5, 3)); // 2
```

### 8.3.3. Import All

```javascript
// Import everything as namespace
import * as Math from './math.js';

console.log(Math.PI);
console.log(Math.add(5, 3));
console.log(Math.subtract(5, 3));
```

### 8.3.4. Default Import

```javascript
// Import default export (any name)
import User from './User.js';
import MyUser from './User.js';  // Same thing, different name

const user = new User('John');
```

### 8.3.5. Mixed Imports

```javascript
// Import default and named
import Utils, { VERSION, helper } from './utils.js';

console.log(VERSION);
console.log(helper());
Utils.log('Hello');
```

### 8.3.6. Side Effect Import

```javascript
// Just execute the module (no imports)
import './polyfill.js';
import './init.js';
```

## 8.4. Dynamic Imports

### 8.4.1. import() Function

```javascript
// Lazy loading
button.addEventListener('click', async () => {
    const module = await import('./heavy-module.js');
    module.doSomething();
});

// Conditional import
if (condition) {
    const module = await import('./module-a.js');
} else {
    const module = await import('./module-b.js');
}

// With .then()
import('./module.js')
    .then(module => {
        module.doSomething();
    })
    .catch(error => {
        console.error('Failed to load module');
    });
```

### 8.4.2. Practical Dynamic Import

```javascript
// Load based on user action
async function loadFeature(featureName) {
    try {
        const module = await import(`./features/${featureName}.js`);
        return module.default;
    } catch (error) {
        console.error(`Failed to load ${featureName}`);
    }
}

// Route-based code splitting
async function navigateTo(route) {
    const Component = await import(`./pages/${route}.js`);
    render(Component.default);
}
```

## 8.5. Module Patterns

### 8.5.1. Config Module

```javascript
// config.js
export const API_URL = 'https://api.example.com';
export const TIMEOUT = 5000;
export const MAX_RETRIES = 3;

export const config = {
    API_URL,
    TIMEOUT,
    MAX_RETRIES
};
```

### 8.5.2. Utility Module

```javascript
// utils.js
export function formatDate(date) {
    return date.toISOString().split('T')[0];
}

export function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

export function debounce(fn, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn(...args), delay);
    };
}
```

### 8.5.3. Service Module

```javascript
// userService.js
const API_URL = '/api/users';

export async function getUsers() {
    const response = await fetch(API_URL);
    return response.json();
}

export async function getUser(id) {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
}

export async function createUser(userData) {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData)
    });
    return response.json();
}
```

### 8.5.4. Class Module

```javascript
// User.js
export default class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    getInfo() {
        return `${this.name} (${this.email})`;
    }
}

// Or multiple classes
export class Admin extends User {
    constructor(name, email) {
        super(name, email);
        this.role = 'admin';
    }
}

export class Guest extends User {
    constructor(name) {
        super(name, 'guest@example.com');
        this.role = 'guest';
    }
}
```

## 8.6. Practical Examples

### 8.6.1. Project Structure

```
src/
├── index.js
├── config.js
├── utils/
│   ├── format.js
│   ├── validate.js
│   └── index.js
├── services/
│   ├── userService.js
│   └── apiService.js
└── components/
    ├── User.js
    └── App.js
```

**utils/index.js (Barrel export):**
```javascript
export * from './format.js';
export * from './validate.js';
```

**Usage:**
```javascript
// Instead of
import { formatDate } from './utils/format.js';
import { validateEmail } from './utils/validate.js';

// Use barrel
import { formatDate, validateEmail } from './utils/index.js';
```

### 8.6.2. API Client

```javascript
// api.js
const BASE_URL = 'https://api.example.com';

async function request(endpoint, options = {}) {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
        headers: {
            'Content-Type': 'application/json',
            ...options.headers
        },
        ...options
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
}

export const api = {
    get: (endpoint) => request(endpoint),
    post: (endpoint, data) => request(endpoint, {
        method: 'POST',
        body: JSON.stringify(data)
    }),
    put: (endpoint, data) => request(endpoint, {
        method: 'PUT',
        body: JSON.stringify(data)
    }),
    delete: (endpoint) => request(endpoint, {
        method: 'DELETE'
    })
};
```

### 8.6.3. State Manager

```javascript
// store.js
class Store {
    #state = {};
    #listeners = [];

    getState() {
        return { ...this.#state };
    }

    setState(updates) {
        this.#state = { ...this.#state, ...updates };
        this.#notify();
    }

    subscribe(listener) {
        this.#listeners.push(listener);
        return () => {
            this.#listeners = this.#listeners.filter(l => l !== listener);
        };
    }

    #notify() {
        this.#listeners.forEach(listener => listener(this.#state));
    }
}

export default new Store();
```

## 8.7. HTML Usage

### 8.7.1. Script Type Module

```html
<!DOCTYPE html>
<html>
<head>
    <title>ES6 Modules</title>
</head>
<body>
    <!-- type="module" required -->
    <script type="module">
        import { add } from './math.js';
        console.log(add(5, 3));
    </script>

    <!-- Or external -->
    <script type="module" src="./main.js"></script>
</body>
</html>
```

### 8.7.2. Module vs Script

```html
<!-- Module (strict mode, deferred) -->
<script type="module" src="./app.js"></script>

<!-- Classic script (not strict, blocking) -->
<script src="./legacy.js"></script>
```

## 8.8. Module Features

### 8.8.1. Modules are Singletons

```javascript
// counter.js
let count = 0;

export function increment() {
    count++;
}

export function getCount() {
    return count;
}

// a.js
import { increment, getCount } from './counter.js';
increment();
console.log(getCount());  // 1

// b.js
import { getCount } from './counter.js';
console.log(getCount());  // 1 (same instance)
```

### 8.8.2. Modules are Strict Mode

```javascript
// module.js (automatically strict mode)
x = 10;  // ReferenceError: x is not defined
```

### 8.8.3. Modules are Deferred

```javascript
// Modules load asynchronously and execute after DOM is ready
// Similar to <script defer>
```

### 8.8.4. Live Bindings

```javascript
// counter.js
export let count = 0;

export function increment() {
    count++;
}

// main.js
import { count, increment } from './counter.js';
console.log(count);  // 0
increment();
console.log(count);  // 1 (live binding!)
```

## 8.9. Best Practices

### 8.9.1. One Export per Module (Default)

```javascript
// Good: Single responsibility
// User.js
export default class User { }

// Bad: Multiple unrelated exports
export class User { }
export class Product { }
export class Order { }
```

### 8.9.2. Named Exports for Utilities

```javascript
// utils.js - multiple related functions
export function format() { }
export function validate() { }
export function parse() { }
```

### 8.9.3. Avoid Circular Dependencies

```javascript
// Bad: Circular dependency
// a.js
import { b } from './b.js';
export const a = 1;

// b.js
import { a } from './a.js';
export const b = 2;

// Fix: Extract common code
// common.js
export const shared = {};

// a.js
import { shared } from './common.js';
export const a = 1;

// b.js
import { shared } from './common.js';
export const b = 2;
```

### 8.9.4. Use Barrel Exports

```javascript
// components/index.js
export { default as Button } from './Button.js';
export { default as Input } from './Input.js';
export { default as Form } from './Form.js';

// Usage
import { Button, Input, Form } from './components/index.js';
```

## 8.10. Common Mistakes

### 8.10.1. Forgetting .js Extension

```javascript
// Works in some bundlers, but not browser
import { add } from './math';  // May fail

// Correct for browsers
import { add } from './math.js';
```

### 8.10.2. Using Require in Modules

```javascript
// Wrong: Don't mix CommonJS and ES6
import { a } from './a.js';
const b = require('./b.js');  // Error

// Use only ES6 imports
import { a } from './a.js';
import { b } from './b.js';
```

### 8.10.3. Importing Non-existent Export

```javascript
// math.js
export function add(a, b) { return a + b; }

// main.js
import { subtract } from './math.js';  // Error: subtract not exported
```

## 8.11. Exercises

### Exercise 1: Create Math Module

```javascript
// Create math.js with add, subtract, multiply, divide
// Use named exports
// Import and use in main.js
```

### Exercise 2: User Service

```javascript
// Create userService.js with:
// - getUsers()
// - getUser(id)
// - createUser(data)
// Export as default object
```

### Exercise 3: Dynamic Import

```javascript
// Create a function that dynamically imports a module based on input
async function loadModule(name) {
    // Your code
}
```

---

**Kết luận:** ES6 Modules giúp organize code tốt hơn, tránh global scope pollution, và hỗ trợ tree-shaking. Sử dụng named exports cho utilities và default export cho main class/component.

**Chương tiếp theo:** Default Parameters
