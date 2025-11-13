# CHƯƠNG 2: LET, CONST VÀ BLOCK SCOPE

## 2.1. Vấn đề với VAR

### 2.1.1. Function Scope

```javascript
// var is function-scoped
function example() {
    var x = 1;
    if (true) {
        var x = 2;  // Same variable!
        console.log(x);  // 2
    }
    console.log(x);  // 2 (not 1!)
}
```

### 2.1.2. Hoisting

```javascript
console.log(x);  // undefined (not error!)
var x = 5;

// Được interpret như:
var x;
console.log(x);  // undefined
x = 5;
```

### 2.1.3. Global Scope Pollution

```javascript
var name = 'John';
var name = 'Jane';  // No error, overwrites

// Loop variable leaks
for (var i = 0; i < 5; i++) {
    // ...
}
console.log(i);  // 5 (still accessible!)
```

## 2.2. LET

### 2.2.1. Block Scope

```javascript
// let is block-scoped
{
    let x = 1;
    console.log(x);  // 1
}
console.log(x);  // ReferenceError: x is not defined
```

### 2.2.2. If Statements

```javascript
if (true) {
    let x = 1;
    console.log(x);  // 1
}
console.log(x);  // ReferenceError
```

### 2.2.3. For Loops

```javascript
// ES5 - var problem
for (var i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i);  // 3, 3, 3
    }, 1000);
}

// ES6 - let solution
for (let i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i);  // 0, 1, 2
    }, 1000);
}
```

### 2.2.4. Temporal Dead Zone (TDZ)

```javascript
// Cannot access before declaration
console.log(x);  // ReferenceError: Cannot access before initialization
let x = 5;

// TDZ example
let x = 1;
{
    console.log(x);  // ReferenceError (TDZ)
    let x = 2;
}
```

### 2.2.5. No Redeclaration

```javascript
let x = 1;
let x = 2;  // SyntaxError: Identifier 'x' has already been declared

// But reassignment is OK
let y = 1;
y = 2;  // OK
```

## 2.3. CONST

### 2.3.1. Constant Values

```javascript
const PI = 3.14159;
console.log(PI);  // 3.14159

PI = 3.14;  // TypeError: Assignment to constant variable
```

### 2.3.2. Must Initialize

```javascript
const x;  // SyntaxError: Missing initializer

const y = 10;  // OK
```

### 2.3.3. Block Scope

```javascript
const MAX = 100;
{
    const MAX = 50;
    console.log(MAX);  // 50
}
console.log(MAX);  // 100
```

### 2.3.4. Objects & Arrays with CONST

**Important:** const prevents reassignment, not mutation!

```javascript
// Objects
const person = { name: 'John' };

person.name = 'Jane';  // OK (mutation)
person.age = 30;       // OK (adding property)

person = {};  // TypeError: Assignment to constant

// Arrays
const numbers = [1, 2, 3];

numbers.push(4);     // OK
numbers[0] = 10;     // OK

numbers = [];  // TypeError: Assignment to constant
```

### 2.3.5. Freezing Objects

```javascript
const person = Object.freeze({ name: 'John' });

person.name = 'Jane';  // Silently fails (strict mode: error)
person.age = 30;       // Silently fails

console.log(person);  // { name: 'John' }

// Deep freeze
const obj = Object.freeze({
    name: 'John',
    address: Object.freeze({
        city: 'NYC'
    })
});
```

## 2.4. VAR vs LET vs CONST

| Feature | var | let | const |
|---------|-----|-----|-------|
| Scope | Function | Block | Block |
| Hoisting | Yes (undefined) | No (TDZ) | No (TDZ) |
| Redeclaration | Yes | No | No |
| Reassignment | Yes | Yes | No |
| Global Object | Yes | No | No |

### 2.4.1. Scope Comparison

```javascript
function scopeTest() {
    var a = 1;
    let b = 2;
    const c = 3;

    if (true) {
        var a = 10;    // Same variable
        let b = 20;    // Different variable
        const c = 30;  // Different variable
        console.log(a, b, c);  // 10, 20, 30
    }

    console.log(a, b, c);  // 10, 2, 3
}
```

### 2.4.2. Hoisting Comparison

```javascript
// var - hoisted to undefined
console.log(a);  // undefined
var a = 1;

// let - TDZ
console.log(b);  // ReferenceError
let b = 2;

// const - TDZ
console.log(c);  // ReferenceError
const c = 3;
```

## 2.5. Block Scope Examples

### 2.5.1. Switch Statements

```javascript
switch (value) {
    case 1: {
        let result = 'One';
        console.log(result);
        break;
    }
    case 2: {
        let result = 'Two';  // Different variable
        console.log(result);
        break;
    }
}
```

### 2.5.2. Try-Catch

```javascript
try {
    let x = 1;
    throw new Error('Test');
} catch (e) {
    let x = 2;  // Different variable
    console.log(x);  // 2
}
```

### 2.5.3. Nested Blocks

```javascript
{
    let x = 1;
    {
        let x = 2;
        {
            let x = 3;
            console.log(x);  // 3
        }
        console.log(x);  // 2
    }
    console.log(x);  // 1
}
```

## 2.6. Practical Examples

### 2.6.1. Loop Closures

```javascript
// Problem with var
const buttons = document.querySelectorAll('button');

for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
        console.log(i);  // Always logs buttons.length
    });
}

// Solution with let
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
        console.log(i);  // Logs correct index
    });
}
```

### 2.6.2. Configuration

```javascript
// Use const for config values
const CONFIG = {
    API_URL: 'https://api.example.com',
    TIMEOUT: 5000,
    MAX_RETRIES: 3
};

// Can modify properties (if needed)
CONFIG.TIMEOUT = 10000;  // OK

// But cannot reassign
CONFIG = {};  // TypeError
```

### 2.6.3. Function Parameters

```javascript
function example(x) {
    // x is like let
    x = 10;  // OK

    let x = 20;  // SyntaxError: duplicate
}
```

## 2.7. Best Practices

### 2.7.1. When to Use Each

**Use const by default:**
```javascript
const name = 'John';
const age = 30;
const users = [];
```

**Use let when you need to reassign:**
```javascript
let counter = 0;
counter++;

let message = 'Loading...';
message = 'Done!';
```

**Avoid var:**
```javascript
// DON'T use var in modern code
var x = 1;  // ❌

// Use let or const
let x = 1;   // ✅
const y = 2; // ✅
```

### 2.7.2. Naming Conventions

```javascript
// Constants (truly constant values)
const MAX_SIZE = 100;
const API_KEY = 'abc123';

// Regular const (can be mutated)
const user = { name: 'John' };
const items = [1, 2, 3];
```

### 2.7.3. Block Scope Strategy

```javascript
// Keep variables in smallest scope possible
{
    const temp = calculate();
    processResult(temp);
}
// temp not accessible here

// Instead of:
const temp = calculate();
processResult(temp);
// temp still accessible (not needed)
```

## 2.8. Common Mistakes

### 2.8.1. Thinking const is Immutable

```javascript
// WRONG assumption
const arr = [1, 2, 3];
arr.push(4);  // This works! arr is not immutable

// const prevents reassignment only
arr = [5, 6, 7];  // TypeError
```

### 2.8.2. Using let in Global Scope

```javascript
// Avoid
let globalVar = 'value';

// Better: use const if not reassigning
const GLOBAL_CONST = 'value';

// Or: use modules (later chapter)
```

### 2.8.3. TDZ Confusion

```javascript
const x = 1;

function test() {
    console.log(x);  // ReferenceError (TDZ)
    const x = 2;
}
```

## 2.9. Advanced Practical Examples

### Example 1: Counter with Closure

```javascript
// Creating a private counter using block scope
function createCounter() {
    let count = 0;

    return {
        increment() {
            return ++count;
        },
        decrement() {
            return --count;
        },
        getCount() {
            return count;
        },
        reset() {
            count = 0;
            return count;
        }
    };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount());  // 2
console.log(counter.decrement()); // 1
console.log(counter.reset());     // 0
// console.log(count); // ReferenceError - count is private
```

### Example 2: Loop with Immediate Values

```javascript
// var problem - all handlers reference the same i
const handlers = [];

for (var i = 0; i < 5; i++) {
    handlers.push(function() {
        return i * 2;
    });
}

console.log(handlers[0]()); // 10 (not 0!)
console.log(handlers[2]()); // 10 (not 4!)

// let solution - each iteration creates new binding
const handlersLet = [];

for (let i = 0; i < 5; i++) {
    handlersLet.push(function() {
        return i * 2;
    });
}

console.log(handlersLet[0]()); // 0
console.log(handlersLet[2]()); // 4
```

### Example 3: Configuration Management

```javascript
// Application configuration with const
const APP_CONFIG = {
    api: {
        baseURL: 'https://api.example.com',
        timeout: 5000,
        retries: 3
    },
    features: {
        darkMode: true,
        notifications: true
    },
    version: '1.0.0'
};

// Can modify nested properties
APP_CONFIG.api.timeout = 10000;
APP_CONFIG.features.darkMode = false;

// But cannot reassign entire config
// APP_CONFIG = {}; // TypeError

// To make truly immutable, use deep freeze
function deepFreeze(obj) {
    Object.keys(obj).forEach(prop => {
        if (typeof obj[prop] === 'object' && !Object.isFrozen(obj[prop])) {
            deepFreeze(obj[prop]);
        }
    });
    return Object.freeze(obj);
}

const IMMUTABLE_CONFIG = deepFreeze({
    api: { baseURL: 'https://api.example.com' }
});

// Now this won't work:
// IMMUTABLE_CONFIG.api.baseURL = 'other'; // Error in strict mode
```

### Example 4: Event Listener Management

```javascript
// Managing event listeners with proper scope
class EventManager {
    constructor() {
        this.listeners = new Map();
    }

    on(event, callback) {
        if (!this.listeners.has(event)) {
            this.listeners.set(event, []);
        }

        // Using const for local scope
        const eventListeners = this.listeners.get(event);
        eventListeners.push(callback);

        // Return unsubscribe function
        return () => {
            const index = eventListeners.indexOf(callback);
            if (index > -1) {
                eventListeners.splice(index, 1);
            }
        };
    }

    emit(event, data) {
        if (!this.listeners.has(event)) return;

        // Using const for iteration
        const callbacks = this.listeners.get(event);
        for (const callback of callbacks) {
            callback(data);
        }
    }
}

// Usage
const events = new EventManager();

const unsubscribe = events.on('update', (data) => {
    console.log('Update received:', data);
});

events.emit('update', { value: 42 });
unsubscribe(); // Remove listener
```

### Example 5: Module Pattern with Block Scope

```javascript
// Creating a private module using IIFE and let/const
const Calculator = (function() {
    // Private variables (not accessible outside)
    let history = [];
    const MAX_HISTORY = 10;

    // Private function
    function addToHistory(operation, result) {
        history.push({ operation, result, timestamp: Date.now() });
        if (history.length > MAX_HISTORY) {
            history.shift();
        }
    }

    // Public API
    return {
        add(a, b) {
            const result = a + b;
            addToHistory(`${a} + ${b}`, result);
            return result;
        },

        subtract(a, b) {
            const result = a - b;
            addToHistory(`${a} - ${b}`, result);
            return result;
        },

        multiply(a, b) {
            const result = a * b;
            addToHistory(`${a} * ${b}`, result);
            return result;
        },

        divide(a, b) {
            if (b === 0) throw new Error('Division by zero');
            const result = a / b;
            addToHistory(`${a} / ${b}`, result);
            return result;
        },

        getHistory() {
            return [...history]; // Return copy, not reference
        },

        clearHistory() {
            history = [];
        }
    };
})();

// Usage
console.log(Calculator.add(5, 3));      // 8
console.log(Calculator.multiply(4, 2)); // 8
console.log(Calculator.getHistory());   // Array with 2 operations
// console.log(history); // ReferenceError - private!
```

### Example 6: State Management

```javascript
// Simple state management using const and let
class Store {
    constructor(initialState = {}) {
        // Private state - can only be modified through methods
        let state = { ...initialState };
        const listeners = new Set();

        // Public methods
        this.getState = () => ({ ...state }); // Return copy

        this.setState = (updates) => {
            const oldState = state;
            state = { ...state, ...updates };

            // Notify listeners
            listeners.forEach(listener => {
                listener(state, oldState);
            });
        };

        this.subscribe = (listener) => {
            listeners.add(listener);
            return () => listeners.delete(listener); // Unsubscribe
        };

        this.reset = () => {
            state = { ...initialState };
            listeners.forEach(listener => listener(state, {}));
        };
    }
}

// Usage
const store = new Store({ count: 0, user: null });

const unsubscribe = store.subscribe((newState, oldState) => {
    console.log('State changed:', newState);
});

store.setState({ count: 1 });
store.setState({ user: { name: 'John' } });
console.log(store.getState()); // { count: 1, user: { name: 'John' } }
```

### Example 7: Temporal Dead Zone in Practice

```javascript
// Understanding TDZ with practical examples

// Example 1: Function parameter TDZ
function example1(a = b, b = 2) {
    return a + b;
}
// example1(); // ReferenceError: b is not defined (TDZ)

// Correct version
function example2(b = 2, a = b) {
    return a + b;
}
console.log(example2()); // 4 (2 + 2)

// Example 2: TDZ in blocks
function example3() {
    const x = 'outer';

    if (true) {
        // TDZ starts here
        // console.log(x); // ReferenceError
        const x = 'inner'; // TDZ ends here
        console.log(x); // 'inner'
    }

    console.log(x); // 'outer'
}

example3();

// Example 3: TDZ with typeof
console.log(typeof undeclaredVar); // "undefined" (no error)
// console.log(typeof declaredVar); // ReferenceError (TDZ)
let declaredVar = 'value';
```

## 2.10. Real-World Use Cases

### Use Case 1: Managing API Request State

```javascript
class APIRequestManager {
    constructor() {
        // Using const for objects that won't be reassigned
        const requests = new Map();
        const maxRetries = 3;

        this.fetch = async (url, options = {}) => {
            // Using let for values that change
            let retries = 0;
            const requestId = `${url}-${Date.now()}`;

            // Store request info
            requests.set(requestId, {
                url,
                status: 'pending',
                attempts: 0
            });

            while (retries < maxRetries) {
                try {
                    const response = await fetch(url, options);

                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}`);
                    }

                    // Update status
                    requests.get(requestId).status = 'success';
                    return await response.json();

                } catch (error) {
                    retries++;
                    requests.get(requestId).attempts = retries;

                    if (retries >= maxRetries) {
                        requests.get(requestId).status = 'failed';
                        throw error;
                    }

                    // Wait before retry
                    await new Promise(resolve =>
                        setTimeout(resolve, 1000 * retries)
                    );
                }
            }
        };

        this.getRequests = () => Array.from(requests.values());
        this.clearRequests = () => requests.clear();
    }
}
```

### Use Case 2: Form Validation

```javascript
class FormValidator {
    constructor(formElement) {
        // Const for elements that won't change
        const form = formElement;
        const errors = new Map();
        const validators = new Map();

        // Validation rules
        validators.set('required', (value) => {
            return value.trim() !== '' || 'This field is required';
        });

        validators.set('email', (value) => {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(value) || 'Invalid email address';
        });

        validators.set('minLength', (min) => (value) => {
            return value.length >= min || `Minimum ${min} characters required`;
        });

        validators.set('maxLength', (max) => (value) => {
            return value.length <= max || `Maximum ${max} characters allowed`;
        });

        this.validate = (field, rules) => {
            const value = form.elements[field].value;
            const fieldErrors = [];

            // Using const in loop
            for (const rule of rules) {
                let validator;
                let result;

                if (typeof rule === 'string') {
                    validator = validators.get(rule);
                    result = validator(value);
                } else {
                    const [ruleName, ...args] = rule;
                    validator = validators.get(ruleName);
                    result = validator(...args)(value);
                }

                if (result !== true) {
                    fieldErrors.push(result);
                }
            }

            if (fieldErrors.length > 0) {
                errors.set(field, fieldErrors);
                return false;
            } else {
                errors.delete(field);
                return true;
            }
        };

        this.validateAll = (fieldRules) => {
            errors.clear();
            let isValid = true;

            for (const [field, rules] of Object.entries(fieldRules)) {
                if (!this.validate(field, rules)) {
                    isValid = false;
                }
            }

            return isValid;
        };

        this.getErrors = () => Object.fromEntries(errors);
        this.clearErrors = () => errors.clear();
    }
}
```

### Use Case 3: Caching System

```javascript
// Implementing a cache with TTL using let/const
class Cache {
    constructor(defaultTTL = 60000) {
        const store = new Map();
        const DEFAULT_TTL = defaultTTL;

        this.set = (key, value, ttl = DEFAULT_TTL) => {
            const expiresAt = Date.now() + ttl;
            store.set(key, { value, expiresAt });

            // Auto-cleanup
            setTimeout(() => {
                if (store.has(key)) {
                    const item = store.get(key);
                    if (Date.now() >= item.expiresAt) {
                        store.delete(key);
                    }
                }
            }, ttl);
        };

        this.get = (key) => {
            if (!store.has(key)) return null;

            const item = store.get(key);

            // Check expiration
            if (Date.now() >= item.expiresAt) {
                store.delete(key);
                return null;
            }

            return item.value;
        };

        this.has = (key) => {
            return this.get(key) !== null;
        };

        this.delete = (key) => {
            return store.delete(key);
        };

        this.clear = () => {
            store.clear();
        };

        this.size = () => {
            // Clean expired items first
            let validCount = 0;
            for (const [key, item] of store) {
                if (Date.now() < item.expiresAt) {
                    validCount++;
                } else {
                    store.delete(key);
                }
            }
            return validCount;
        };
    }
}

// Usage
const cache = new Cache(5000); // 5 second TTL
cache.set('user', { name: 'John' });
console.log(cache.get('user')); // { name: 'John' }

setTimeout(() => {
    console.log(cache.get('user')); // null (expired)
}, 6000);
```

### Use Case 4: Debounce and Throttle

```javascript
// Debounce function using let for timer
function debounce(func, delay) {
    let timeoutId;

    return function(...args) {
        // Clear previous timeout
        if (timeoutId) {
            clearTimeout(timeoutId);
        }

        // Set new timeout
        timeoutId = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}

// Throttle function using let for lastCall
function throttle(func, limit) {
    let inThrottle;
    let lastCall;

    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            lastCall = Date.now();
            inThrottle = true;

            setTimeout(() => {
                inThrottle = false;
                if (Date.now() - lastCall >= limit) {
                    func.apply(this, args);
                }
            }, limit);
        }
    };
}

// Usage examples
const debouncedSearch = debounce((query) => {
    console.log('Searching for:', query);
}, 500);

const throttledScroll = throttle(() => {
    console.log('Scroll handler called');
}, 1000);
```

### Use Case 5: Singleton Pattern

```javascript
// Singleton using const and closure
const DatabaseConnection = (function() {
    let instance;
    const DB_URL = 'mongodb://localhost:27017';

    class Database {
        constructor() {
            if (instance) {
                throw new Error('Database instance already exists!');
            }
            this.url = DB_URL;
            this.connected = false;
        }

        connect() {
            if (!this.connected) {
                console.log(`Connecting to ${this.url}`);
                this.connected = true;
            }
            return this;
        }

        disconnect() {
            if (this.connected) {
                console.log('Disconnecting from database');
                this.connected = false;
            }
            return this;
        }

        query(sql) {
            if (!this.connected) {
                throw new Error('Not connected to database');
            }
            console.log('Executing query:', sql);
            return [];
        }
    }

    return {
        getInstance() {
            if (!instance) {
                instance = new Database();
            }
            return instance;
        }
    };
})();

// Usage
const db1 = DatabaseConnection.getInstance();
const db2 = DatabaseConnection.getInstance();
console.log(db1 === db2); // true - same instance
```

## 2.11. Tips & Tricks

### Tip 1: Default to const

```javascript
// Always start with const
const user = { name: 'John' };
const items = [1, 2, 3];
const PI = 3.14159;

// Only switch to let when you need reassignment
let counter = 0;
counter++;
```

### Tip 2: Smallest Scope Possible

```javascript
// BAD - wider scope than needed
let result;
if (condition) {
    result = calculate();
} else {
    result = defaultValue;
}

// GOOD - minimal scope
const result = condition ? calculate() : defaultValue;
```

### Tip 3: Loop Index with const

```javascript
// Use const for loop index when possible
const items = ['a', 'b', 'c'];

// for...of with const
for (const item of items) {
    console.log(item);
}

// forEach with const
items.forEach((item, index) => {
    const message = `${index}: ${item}`;
    console.log(message);
});
```

### Tip 4: Destructuring with const

```javascript
const user = { name: 'John', age: 30, city: 'NYC' };

// Extract multiple values with const
const { name, age } = user;

// Renaming with const
const { city: location } = user;
```

### Tip 5: Avoid Mixing let and const in One Statement

```javascript
// BAD - confusing
let x = 1, y = 2;
const z = 3, w = 4;

// GOOD - clear and consistent
let x = 1;
let y = 2;
const z = 3;
const w = 4;
```

### Tip 6: Block Scope for Temporary Variables

```javascript
// Use blocks to limit scope of temporary variables
{
    const temp = heavyCalculation();
    const processed = process(temp);
    saveResult(processed);
}
// temp and processed are not accessible here

// Instead of polluting outer scope
const temp = heavyCalculation();
const processed = process(temp);
saveResult(processed);
// temp and processed still accessible (unnecessarily)
```

### Tip 7: const for Object Methods

```javascript
const utils = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b,
    divide: (a, b) => b !== 0 ? a / b : null
};

// Can add methods (object is mutable)
utils.mod = (a, b) => a % b;

// But cannot reassign utils itself
// utils = {}; // TypeError
```

### Tip 8: Avoid Global let/const

```javascript
// BAD - global variables
let globalCount = 0;
const globalConfig = {};

// GOOD - use modules or closures
export const createApp = () => {
    let count = 0;
    const config = {};

    return {
        getCount: () => count,
        increment: () => ++count
    };
};
```

### Tip 9: const in Switch Cases

```javascript
switch (type) {
    case 'user': {
        const user = getUser();
        processUser(user);
        break;
    }
    case 'admin': {
        const admin = getAdmin();
        processAdmin(admin);
        break;
    }
}
```

### Tip 10: Use const for Imports

```javascript
// ES6 modules - imports are const-like
import { useState, useEffect } from 'react';
import express from 'express';

// This won't work:
// useState = someOtherFunction; // Error
```

## 2.12. Common Mistakes (Extended)

### Mistake 1: Forgetting const is Not Immutable

```javascript
// WRONG - thinking const makes objects immutable
const settings = { theme: 'light' };
settings.theme = 'dark'; // This works!
console.log(settings); // { theme: 'dark' }

// CORRECT - understanding const prevents reassignment
const config = { mode: 'dev' };
// config = { mode: 'prod' }; // TypeError

// For immutability, use Object.freeze()
const frozen = Object.freeze({ theme: 'light' });
// frozen.theme = 'dark'; // Silently fails (strict: Error)
```

### Mistake 2: Using let for Everything

```javascript
// BAD - overusing let
let name = 'John';
let age = 30;
let city = 'NYC';

// GOOD - use const when not reassigning
const name = 'John';
const age = 30;
const city = 'NYC';
```

### Mistake 3: var in Block Scope

```javascript
// MISTAKE - using var thinking it has block scope
if (true) {
    var x = 10;
}
console.log(x); // 10 (leaked!)

// CORRECT - use let/const
if (true) {
    const x = 10;
}
// console.log(x); // ReferenceError
```

### Mistake 4: Hoisting Confusion

```javascript
// MISTAKE - relying on hoisting
function bad() {
    console.log(x); // undefined (not error)
    var x = 5;
}

// CORRECT - declare before use
function good() {
    const x = 5;
    console.log(x); // 5
}
```

### Mistake 5: TDZ in Default Parameters

```javascript
// MISTAKE - referencing later parameters
function bad(a = b, b = 1) {
    return a + b;
}
// bad(); // ReferenceError: b is not defined

// CORRECT - parameters defined in order
function good(b = 1, a = b) {
    return a + b;
}
console.log(good()); // 2
```

### Mistake 6: Redeclaration in Same Scope

```javascript
// MISTAKE - trying to redeclare
let x = 1;
let x = 2; // SyntaxError

// CORRECT - use different names or reassign
let x = 1;
x = 2; // OK (reassignment)

// Or different scopes
let y = 1;
{
    let y = 2; // OK (different scope)
}
```

### Mistake 7: const Without Initialization

```javascript
// MISTAKE
const x; // SyntaxError: Missing initializer
x = 10;

// CORRECT
const x = 10;
```

### Mistake 8: Closure with var

```javascript
// MISTAKE - closure captures wrong value
const funcs = [];
for (var i = 0; i < 3; i++) {
    funcs.push(() => console.log(i));
}
funcs.forEach(f => f()); // 3, 3, 3

// CORRECT - use let for proper closure
const funcsCorrect = [];
for (let i = 0; i < 3; i++) {
    funcsCorrect.push(() => console.log(i));
}
funcsCorrect.forEach(f => f()); // 0, 1, 2
```

## 2.13. Troubleshooting

### Issue 1: ReferenceError Before Declaration

**Problem:**
```javascript
console.log(x); // ReferenceError: Cannot access 'x' before initialization
const x = 5;
```

**Solution:**
Always declare variables before using them. Unlike var, let and const don't hoist to undefined.

### Issue 2: Cannot Reassign const

**Problem:**
```javascript
const PI = 3.14;
PI = 3.14159; // TypeError: Assignment to constant variable
```

**Solution:**
Use let if you need to reassign, or use const for objects and mutate properties:
```javascript
let value = 3.14;
value = 3.14159; // OK

const obj = { pi: 3.14 };
obj.pi = 3.14159; // OK (mutation)
```

### Issue 3: Block Scope Not Working

**Problem:**
```javascript
if (true) {
    var x = 10;
}
console.log(x); // 10 (accessible outside!)
```

**Solution:**
Use let or const instead of var:
```javascript
if (true) {
    const x = 10;
}
// console.log(x); // ReferenceError - correct behavior
```

### Issue 4: Loop Closure Issues

**Problem:**
```javascript
for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3
```

**Solution:**
Use let in the loop:
```javascript
for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100);
}
// Output: 0, 1, 2
```

### Issue 5: TDZ Errors

**Problem:**
```javascript
let x = 1;
{
    console.log(x); // ReferenceError
    let x = 2;
}
```

**Solution:**
Don't reference variables before their declaration in the same block:
```javascript
let x = 1;
{
    let x = 2; // Different variable
    console.log(x); // 2
}
```

### Issue 6: const in Switch Without Blocks

**Problem:**
```javascript
switch (value) {
    case 1:
        const x = 'one';
        break;
    case 2:
        const x = 'two'; // SyntaxError: Identifier 'x' has already been declared
        break;
}
```

**Solution:**
Use blocks in each case:
```javascript
switch (value) {
    case 1: {
        const x = 'one';
        break;
    }
    case 2: {
        const x = 'two';
        break;
    }
}
```

## 2.14. Advanced Topics

### Advanced Topic 1: Block Scope and Memory Management

```javascript
// Block scope can help with memory management
function processLargeData() {
    // Large data only exists in this block
    {
        const largeArray = new Array(1000000).fill('data');
        const processed = largeArray.map(item => process(item));
        saveResults(processed);
    }
    // largeArray is now eligible for garbage collection

    // Continue with other work
    doOtherStuff();
}
```

### Advanced Topic 2: const with Complex Data Structures

```javascript
// const with nested structures
const deepObject = {
    level1: {
        level2: {
            level3: 'value'
        }
    }
};

// Can mutate nested properties
deepObject.level1.level2.level3 = 'new value';

// Deep freeze utility
function deepFreeze(obj) {
    Object.keys(obj).forEach(prop => {
        if (typeof obj[prop] === 'object' && obj[prop] !== null) {
            deepFreeze(obj[prop]);
        }
    });
    return Object.freeze(obj);
}

const immutable = deepFreeze({
    a: { b: { c: 1 } }
});

// This won't work:
// immutable.a.b.c = 2; // Error in strict mode
```

### Advanced Topic 3: Performance Implications

```javascript
// const can enable better optimizations by the JS engine
const CONSTANT_VALUE = 42;

function compute() {
    // Engine knows CONSTANT_VALUE won't change
    return CONSTANT_VALUE * 2;
}

// vs

let variable = 42;

function computeWithLet() {
    // Engine must check if variable changed
    return variable * 2;
}
```

### Advanced Topic 4: Temporal Dead Zone Deep Dive

```javascript
// TDZ creates a temporal "dead zone" from block start to declaration

// Example 1: Class expressions
const MyClass = class {
    static instance = new MyClass(); // Error: Cannot access before initialization
};

// Correct:
const MyClass2 = class {
    static create() {
        return new MyClass2(); // OK - after declaration
    }
};

// Example 2: Default parameters with functions
function outer() {
    const inner = (x = inner) => x; // ReferenceError
    return inner;
}

// Correct:
function outerCorrect() {
    const inner = (x = () => inner) => x();
    return inner;
}
```

### Advanced Topic 5: const in Module Scope

```javascript
// module.js
const privateVar = 'private';
export const publicVar = 'public';

// Private constants
const CACHE_SIZE = 100;
const cache = new Array(CACHE_SIZE);

export function useCache() {
    // Can access private const
    return cache;
}

// Note: exported const can still be mutated if it's an object
export const config = { theme: 'light' };
// Other modules can do: config.theme = 'dark'
// But cannot: config = {} (reassignment not allowed)
```

## 2.15. Exercises (Extended)

### Exercise 1: Fix the Loop
```javascript
// Fix this code to output 1, 2, 3
for (var i = 1; i <= 3; i++) {
    setTimeout(function() {
        console.log(i);
    }, i * 1000);
}
// Current output: 4, 4, 4
// Expected output: 1, 2, 3
```

### Exercise 2: Choose Correct Declaration
```javascript
// Declare these variables correctly:
// 1. A counter that increases
// 2. A user's name (won't change)
// 3. An array of items (items can be added)
// 4. Pi constant
// 5. A temporary calculation result
```

### Exercise 3: Block Scope Practice
```javascript
// What will this output?
const x = 1;
{
    const x = 2;
    {
        const x = 3;
        console.log(x); // ?
    }
    console.log(x); // ?
}
console.log(x); // ?
```

### Exercise 4: Fix TDZ Error
```javascript
// Fix this code
function example() {
    console.log(message);
    const message = 'Hello';
}
```

### Exercise 5: const vs Immutability
```javascript
// Make this object truly immutable
const user = {
    name: 'John',
    address: {
        city: 'NYC',
        country: 'USA'
    }
};
```

### Exercise 6: Refactor to ES6
```javascript
// Refactor this ES5 code to use let/const
var count = 0;

function increment() {
    count = count + 1;
    return count;
}

function reset() {
    count = 0;
}

var users = [];

function addUser(user) {
    users.push(user);
}
```

### Exercise 7: Event Handlers
```javascript
// Fix the event handler issue
const buttons = document.querySelectorAll('button');

for (var i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function() {
        console.log('Button ' + i + ' clicked');
    };
}
// Currently logs wrong button number
```

### Exercise 8: Closure and Scope
```javascript
// Create a function that returns a counter
// The counter should:
// - Start at 0
// - Have increment() method
// - Have decrement() method
// - Have getValue() method
// - Count should be private (not accessible directly)
```

### Exercise 9: Configuration Object
```javascript
// Create an app config object that:
// - Cannot be reassigned
// - Has nested properties (api, ui, features)
// - Properties can be modified but not replaced
// - Has a method to reset to defaults
```

### Exercise 10: Switch Statement Scope
```javascript
// Fix the scope error
const type = 'user';

switch(type) {
    case 'user':
        const message = 'User type';
        console.log(message);
        break;
    case 'admin':
        const message = 'Admin type';  // Error!
        console.log(message);
        break;
}
```

### Exercise 11: Module Pattern
```javascript
// Create a simple module using const and IIFE
// Module should have:
// - Private state
// - Public methods to access/modify state
// - Cannot access private state directly
```

### Exercise 12: Advanced Challenge
```javascript
// Create a caching system with:
// - Private cache storage
// - set(key, value, ttl) method
// - get(key) method
// - Automatic cleanup of expired items
// - size() method showing current cache size
// Use let/const appropriately
```

---

**Kết luận:** Sử dụng `const` mặc định, `let` khi cần reassign, tránh `var`. Block scope giúp code dễ hiểu và tránh bugs.

**Chương tiếp theo:** Arrow Functions
