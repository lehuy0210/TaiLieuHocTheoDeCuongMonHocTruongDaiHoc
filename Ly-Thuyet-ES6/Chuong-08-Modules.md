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

## 8.6. Use Cases Thực Tế

### Use Case 1: E-commerce Application Structure

```javascript
// utils/validation.js
export function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export function validatePassword(password) {
    return password.length >= 8;
}

// services/userService.js
import { validateEmail, validatePassword } from '../utils/validation.js';

const API_BASE = 'https://api.example.com';

export async function registerUser(email, password) {
    if (!validateEmail(email)) {
        throw new Error('Invalid email');
    }
    if (!validatePassword(password)) {
        throw new Error('Password too weak');
    }

    const response = await fetch(`${API_BASE}/users/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });

    return response.json();
}

export async function loginUser(email, password) {
    const response = await fetch(`${API_BASE}/users/login`, {
        method: 'POST',
        body: JSON.stringify({ email, password })
    });
    return response.json();
}

// models/Product.js
export default class Product {
    constructor(id, name, price, stock) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    isAvailable() {
        return this.stock > 0;
    }

    calculateDiscount(percentage) {
        return this.price * (1 - percentage / 100);
    }
}

// main.js
import * as userService from './services/userService.js';
import Product from './models/Product.js';

async function appStart() {
    try {
        const user = await userService.loginUser('user@example.com', 'Pass123!');
        console.log('User logged in:', user);

        const product = new Product(1, 'Laptop', 1000, 5);
        console.log('Product available:', product.isAvailable());
    } catch (error) {
        console.error('Error:', error);
    }
}

appStart();
```

### Use Case 2: Component Library with Barrel Exports

```javascript
// components/Button/Button.js
export default class Button {
    constructor(props) {
        this.props = props;
    }

    render() {
        return `<button>${this.props.label}</button>`;
    }
}

// components/Button/index.js
export { default } from './Button.js';

// components/Input/Input.js
export default class Input {
    constructor(props) {
        this.props = props;
    }

    render() {
        return `<input placeholder="${this.props.placeholder}" />`;
    }
}

// components/Input/index.js
export { default } from './Input.js';

// components/Form/Form.js
export default class Form {
    constructor(fields) {
        this.fields = fields;
    }

    render() {
        return `<form>${this.fields.map(f => f.render()).join('')}</form>`;
    }
}

// components/Form/index.js
export { default } from './Form.js';

// components/index.js (Barrel export)
export { default as Button } from './Button/index.js';
export { default as Input } from './Input/index.js';
export { default as Form } from './Form/index.js';

// Usage
import { Button, Input, Form } from './components/index.js';

const button = new Button({ label: 'Submit' });
const input = new Input({ placeholder: 'Name' });
```

### Use Case 3: Configuration Management

```javascript
// config/environment.js
export const ENV = process.env.NODE_ENV || 'development';

export const isProduction = ENV === 'production';
export const isDevelopment = ENV === 'development';

// config/api.js
import { ENV } from './environment.js';

export const API_CONFIG = {
    development: {
        baseURL: 'http://localhost:3000/api',
        timeout: 10000
    },
    production: {
        baseURL: 'https://api.example.com',
        timeout: 5000
    }
};

export function getAPIConfig() {
    return API_CONFIG[ENV];
}

export const API_ENDPOINTS = {
    users: '/users',
    products: '/products',
    orders: '/orders'
};

// config/index.js (Barrel export)
export * from './environment.js';
export * from './api.js';

// Usage
import { getAPIConfig, isDevelopment } from './config/index.js';

const apiConfig = getAPIConfig();
console.log('API Base:', apiConfig.baseURL);
```

### Use Case 4: Lazy Loading Features

```javascript
// features/dashboard.js
export function renderDashboard() {
    return '<div>Dashboard Content</div>';
}

export function initDashboard() {
    console.log('Dashboard initialized');
}

// features/admin.js
export function renderAdmin() {
    return '<div>Admin Panel</div>';
}

export function initAdmin() {
    console.log('Admin initialized');
}

// app.js
async function loadFeature(name) {
    try {
        const module = await import(`./features/${name}.js`);
        module.init();
        return module;
    } catch (error) {
        console.error(`Failed to load ${name}:`, error);
    }
}

async function handleNavigation(route) {
    const module = await loadFeature(route);
    const content = module[`render${route.charAt(0).toUpperCase() + route.slice(1)}`]?.();
    document.getElementById('app').innerHTML = content;
}

// Usage
button.addEventListener('click', () => handleNavigation('dashboard'));
```

### Use Case 5: Plugin System with Dynamic Imports

```javascript
// plugins/analytics.js
export default class AnalyticsPlugin {
    constructor(config) {
        this.config = config;
    }

    track(event, data) {
        console.log(`[Analytics] ${event}:`, data);
    }

    initialize() {
        console.log('Analytics initialized');
    }
}

// plugins/tracking.js
export default class TrackingPlugin {
    track(action) {
        console.log(`[Tracking] ${action}`);
    }

    initialize() {
        console.log('Tracking initialized');
    }
}

// plugins/index.js
export { default as Analytics } from './analytics.js';
export { default as Tracking } from './tracking.js';

// app.js
import * as plugins from './plugins/index.js';

class App {
    constructor() {
        this.plugins = [];
    }

    async loadPlugin(name, config) {
        const PluginClass = plugins[name];
        if (!PluginClass) {
            throw new Error(`Plugin ${name} not found`);
        }

        const plugin = new PluginClass(config);
        plugin.initialize();
        this.plugins.push(plugin);
        return plugin;
    }

    async init() {
        await this.loadPlugin('Analytics', { apiKey: 'key123' });
        await this.loadPlugin('Tracking', {});
    }
}

const app = new App();
app.init();
```

## 8.7. Practical Examples

### 8.7.1. Project Structure

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

## 8.8. Tips & Tricks

### Tip 1: Namespace Imports for Large Modules

```javascript
// Bad: Too many individual imports
import { action1, action2, action3, action4, action5 } from './actions.js';

// Good: Use namespace
import * as actions from './actions.js';

// Or re-export as namespace
// actions/index.js
export * as default from './types.js';
```

### Tip 2: Conditional Dynamic Imports

```javascript
// Load different modules based on environment
async function loadAuthModule() {
    const authModule = process.env.NODE_ENV === 'production'
        ? await import('./auth/prod.js')
        : await import('./auth/dev.js');
    return authModule;
}
```

### Tip 3: Re-exporting with Renaming

```javascript
// oldAPI.js
export function getData() { }
export function postData() { }

// newAPI.js - Re-export with different names
export { getData as fetch, postData as send } from './oldAPI.js';

// Usage
import { fetch, send } from './newAPI.js';
```

### Tip 4: Default Exports for Main Classes

```javascript
// User.js
export default class User {
    constructor(name) {
        this.name = name;
    }
}

// Usage - Can import with any name
import Person from './User.js';  // Still works!
import Account from './User.js';  // Also works!
```

### Tip 5: Lazy Loading on Demand

```javascript
// Split code for routes
const routes = {
    dashboard: () => import('./pages/Dashboard.js'),
    settings: () => import('./pages/Settings.js'),
    profile: () => import('./pages/Profile.js')
};

async function navigate(route) {
    const Page = await routes[route]();
    return Page.default;  // Get default export
}
```

### Tip 6: Checking if Module Export Exists

```javascript
// Check if optional feature is available
async function loadOptionalFeature(name) {
    try {
        const module = await import(`./features/${name}.js`);
        return module.default || module;
    } catch (e) {
        console.warn(`Feature ${name} not available`);
        return null;
    }
}
```

### Tip 7: Circular Dependency Prevention

```javascript
// Instead of direct import in module A and B
// Create a third module C that both import from

// common.js
export const config = {};

// moduleA.js
import { config } from './common.js';

// moduleB.js
import { config } from './common.js';
// No circular dependency!
```

### Tip 8: Re-exporting Everything from a Module

```javascript
// index.js - Barrel export
export * from './module1.js';
export * from './module2.js';
export { default as DefaultClass } from './main.js';

// Can also use:
export * as module1 from './module1.js';  // Namespace
```

### Tip 9: Side Effects Only Imports

```javascript
// polyfill.js
import 'core-js/stable';
import 'regenerator-runtime/runtime';

// app.js - Just execute, no imports
import './polyfill.js';  // Side effect only
import './styles.css';   // Side effect only
```

### Tip 10: Mock Modules for Testing

```javascript
// math.js
export function add(a, b) { return a + b; }

// __mocks__/math.js
export const add = jest.fn((a, b) => 0);

// test.js
jest.mock('./math.js');
import { add } from './math.js';

test('mocked', () => {
    expect(add(1, 2)).toBe(0);
});
```

## 8.9. Common Mistakes

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
// BAD: Export not defined
// math.js
export function add(a, b) { return a + b; }

// main.js
import { subtract } from './math.js';  // Error

// GOOD: Import what's exported
import { add } from './math.js';
```

### 8.10.4. Forgetting to Export

```javascript
// BAD: Defined but not exported
// math.js
function add(a, b) { return a + b; }

// main.js
import { add } from './math.js';  // Not found!

// GOOD: Export it
// math.js
export function add(a, b) { return a + b; }
```

### 8.10.5. Default Export Confusion

```javascript
// BAD: Both default and named (confusing)
export default function User() { }
export { User };

// GOOD: Pick one
export default function User() { }
```

### 8.10.6: Side Effects in Top-level Code

```javascript
// BAD: Unexpected side effects on import
// logger.js
const log = console.log.bind(console);
log('Logger loaded!');  // Prints on every import

// GOOD: Explicit initialization
// logger.js
export function init() {
    log('Logger loaded!');
}
```

### 8.10.7: Not Using Path Aliases

```javascript
// BAD: Fragile relative paths
import Button from '../../../components/Button.js';

// GOOD: Use path aliases (with bundler)
import Button from '@components/Button.js';
```

### 8.10.8: Importing Whole Module for One Function

```javascript
// BAD: Importing everything
import * as math from './math.js';
const result = math.add(1, 2);

// GOOD: Import only needed
import { add } from './math.js';
const result = add(1, 2);
```

### 8.10.9: Async Import Without Handling

```javascript
// BAD: Ignoring promise
import('./data.js');  // Promise not handled

// GOOD: Handle the promise
const data = await import('./data.js');

// Or with .then()
import('./data.js').then(module => {
    // Use module
}).catch(error => {
    // Handle error
});
```

### 8.10.10: Module Reload Misunderstandings

```javascript
// BAD: Expecting reload
const m = await import('./data.js?t=' + Date.now());
// This doesn't actually reload!

// GOOD: Modules are singletons
const m = await import('./data.js');
// Same instance always returned
```

## 8.11. Troubleshooting Issues

### Issue 1: Module Not Found Error

**Problem:**
```javascript
import { api } from './api';  // ModuleNotFoundError
```

**Solution:**
```javascript
// Check 1: Add .js extension
import { api } from './api.js';

// Check 2: Correct path
import { api } from '../services/api.js';

// Check 3: File exists and exports it
// api.js must have: export const api = ...
```

### Issue 2: Default vs Named Export Confusion

**Problem:**
```javascript
// User.js
export default class User { }

// Bad import
import { User } from './User.js';  // Error!
```

**Solution:**
```javascript
// Default import
import User from './User.js';

// Or export as named
// User.js
export class User { }

// Import named
import { User } from './User.js';
```

### Issue 3: Circular Dependencies

**Problem:**
```javascript
// a.js
import { b } from './b.js';
export const a = 1;

// b.js
import { a } from './a.js';
export const b = 2;
```

**Solution:**
```javascript
// Extract common module
// common.js
export const shared = {};

// a.js & b.js import from common.js
```

### Issue 4: Dynamic Import Path Issues

**Problem:**
```javascript
// Doesn't work - path must be literal
const name = 'auth';
const m = await import(`./modules/${name}`);
```

**Solution:**
```javascript
// Use full path in template
const m = await import(`./modules/${name}.js`);

// Or use module map
const modules = {
    auth: () => import('./auth.js')
};
const m = await modules[name]?.();
```

### Issue 5: Import Timing Issues

**Problem:**
```javascript
// config.js might load before env.js
import { apiKey } from './env.js';
export const config = { apiKey };
```

**Solution:**
```javascript
// Lazy initialization
export function getConfig() {
    const { apiKey } = require('./env.js');
    return { apiKey };
}
```

### Issue 6: Side Effects Not Running

**Problem:**
```javascript
// Unclear if CSS/polyfill applied
import './styles.css';
```

**Solution:**
```javascript
// Make intent explicit
import './styles.css';  // CSS side effect

// Or in dedicated init file
import './init.js';  // All polyfills & styles
```

### Issue 7: Modules Not Fully Initialized

**Problem:**
```javascript
// Module might not be ready
import { data } from './data.js';
// data might be undefined
```

**Solution:**
```javascript
// Lazy loading with initialization
export async function init() {
    // Initialize data
}

export function getData() {
    // Return initialized data
}

// main.js
await dataModule.init();
const data = dataModule.getData();
```

### Issue 8: Import JSON Files

**Problem:**
```javascript
// Works in Webpack, not standard
import data from './data.json';
```

**Solution:**
```javascript
// Standard fetch approach
const response = await fetch('./data.json');
const data = await response.json();

// Or newer JSON import
import data from './data.json' assert { type: 'json' };
```

### Issue 9: Tree Shaking Not Working

**Problem:**
```javascript
// import * prevents tree shaking
import * as utils from './utils.js';
utils.used();
```

**Solution:**
```javascript
// Named imports enable tree shaking
import { used } from './utils.js';
used();
```

### Issue 10: Missing Default Export

**Problem:**
```javascript
// No default export but trying to use
// index.js
export { Button } from './Button.js';

// Usage
import Components from './index.js';  // undefined
```

**Solution:**
```javascript
// Provide default export
export { default } from './Button.js';

// Or use named imports
import { Button } from './index.js';
```

## 8.12. Advanced Topics

### Topic 1: Module Federation

```javascript
// Shared module registry for micro frontends
// registry.js
export const modules = new Map();

export function register(name, module) {
    modules.set(name, module);
}

export function get(name) {
    return modules.get(name);
}

// app1.js
import { register } from './registry.js';
import Dashboard from './Dashboard.js';
register('dashboard', Dashboard);

// app2.js - Use shared module
import { get } from './registry.js';
const Dashboard = get('dashboard');
```

### Topic 2: Import Maps

```javascript
/*
<script type="importmap">
{
  "imports": {
    "lodash": "https://cdn.jsdelivr.net/npm/lodash-es",
    "utils/": "./src/utils/",
    "components/": "./src/components/"
  }
}
</script>
*/

// Can use short paths
import { debounce } from 'lodash';
import { formatDate } from 'utils/format.js';
```

### Topic 3: Virtual Modules

```javascript
class ModuleLoader {
    #modules = new Map();

    register(name, factory) {
        this.#modules.set(name, factory);
    }

    async load(name) {
        const factory = this.#modules.get(name);
        if (!factory) throw new Error(`Not found: ${name}`);
        return factory();
    }
}

const loader = new ModuleLoader();
loader.register('config', () => ({
    default: { apiUrl: 'https://api.example.com' }
}));

const config = await loader.load('config');
```

### Topic 4: Module Caching

```javascript
class ModuleCache {
    #cache = new Map();
    #pending = new Map();

    async load(path) {
        if (this.#cache.has(path)) {
            return this.#cache.get(path);
        }

        if (this.#pending.has(path)) {
            return this.#pending.get(path);
        }

        const promise = import(path);
        this.#pending.set(path, promise);

        try {
            const module = await promise;
            this.#cache.set(path, module);
            return module;
        } finally {
            this.#pending.delete(path);
        }
    }

    invalidate(path) {
        this.#cache.delete(path);
    }

    clear() {
        this.#cache.clear();
    }
}
```

### Topic 5: Lazy Component Loading

```javascript
class LazyComponent {
    #module = null;

    async load() {
        if (!this.#module) {
            this.#module = await import('./heavy.js');
        }
        return this.#module;
    }

    async render() {
        const { render } = await this.load();
        return render();
    }

    async hydrate(element) {
        const { hydrate } = await this.load();
        hydrate(element);
    }
}

// Usage
const component = new LazyComponent();
const html = await component.render();  // Load on demand
```

## 8.13. Exercises

### Exercise 1 (Dễ): Math Module

```javascript
// Create math.js with:
// - add(a, b)
// - subtract(a, b)
// - multiply(a, b)
// - divide(a, b)
// Use named exports

// Create main.js that imports and uses them
```

### Exercise 2 (Dễ): User Module

```javascript
// Create User.js with default export class
// Create userService.js with named exports:
// - getUsers()
// - getUser(id)
// - createUser(data)

// Create main.js that imports both
```

### Exercise 3 (Dễ): Barrel Export

```javascript
// Create components directory:
// - Button.js (export Button)
// - Input.js (export Input)
// - Form.js (export Form)

// Create index.js re-exporting all
// Test importing from components/
```

### Exercise 4 (Dễ): Config Module

```javascript
// Create config.js with:
// - API_URL constant
// - TIMEOUT constant
// - getConfig() function

// Create main.js that uses it
```

### Exercise 5 (Trung bình): API Service Module

```javascript
// Create apiService.js:
// - get(url)
// - post(url, data)
// - put(url, data)
// - delete(url)

// Create userService.js using apiService
// - getUsers()
// - createUser(data)
```

### Exercise 6 (Trung bình): Plugin System

```javascript
// Create plugin base class
// Create 2-3 plugins
// Create pluginManager that:
// - loads plugins
// - initializes them
// - executes methods

// Create main.js to test
```

### Exercise 7 (Trung bình): Route-based Code Splitting

```javascript
// Create pages: Dashboard, Settings, Profile
// Create router that:
// - Takes route name
// - Dynamically imports page
// - Returns component

// Test all routes loading
```

### Exercise 8 (Trung bình): Feature Flags Module

```javascript
// Create feature flags module:
// - Toggle features on/off
// - Conditionally import features

// Create main.js that:
// - Enables/disables features
// - Loads appropriate modules
```

### Exercise 9 (Khó): Dependency Resolver

```javascript
// Create system that:
// - Tracks dependencies
// - Loads in correct order
// - Detects circular deps
// - Provides metadata

// Test with sample modules
```

### Exercise 10 (Khó): State Management System

```javascript
// Create store module:
// - State management
// - Actions as modules
// - Reducers as modules
// - Middleware support

// Create app.js integrating everything
```

### Exercise 11 (Khó): Module Analysis Tool

```javascript
// Create tool that:
// - Analyzes all imports
// - Builds dependency graph
// - Detects circular deps
// - Reports unused modules
// - Suggests optimizations

// Run on project files
```

### Exercise 12 (Khó): Hot Module Replacement

```javascript
// Create HMR system that:
// - Detects changes
// - Reloads modules
// - Maintains state
// - Notifies subscribers

// Test with sample modules
```

---

**Kết luận:** ES6 Modules là nền tảng của code organization hiện đại. Sử dụng default exports cho main classes, named exports cho utilities. Tránh circular dependencies. Dùng dynamic imports cho code splitting.

**Chương tiếp theo:** Promise & Async/Await
