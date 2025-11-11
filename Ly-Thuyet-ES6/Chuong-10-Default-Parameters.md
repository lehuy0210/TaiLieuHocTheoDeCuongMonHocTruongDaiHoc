# CHƯƠNG 10: DEFAULT PARAMETERS

## 10.1. Giới thiệu Default Parameters

Default parameters cho phép khởi tạo function parameters với default values nếu không có value được truyền vào.

### 10.1.1. ES5 vs ES6

**ES5:**
```javascript
function greet(name, greeting) {
    name = name || 'Guest';
    greeting = greeting || 'Hello';
    return greeting + ', ' + name + '!';
}
```

**ES6:**
```javascript
function greet(name = 'Guest', greeting = 'Hello') {
    return `${greeting}, ${name}!`;
}
```

## 10.2. Basic Syntax

### 10.2.1. Simple Defaults

```javascript
function multiply(a, b = 1) {
    return a * b;
}

console.log(multiply(5));     // 5 (b defaults to 1)
console.log(multiply(5, 2));  // 10
```

### 10.2.2. Multiple Defaults

```javascript
function createUser(name = 'Guest', age = 0, role = 'user') {
    return { name, age, role };
}

console.log(createUser());
// { name: 'Guest', age: 0, role: 'user' }

console.log(createUser('John'));
// { name: 'John', age: 0, role: 'user' }

console.log(createUser('John', 30));
// { name: 'John', age: 30, role: 'user' }

console.log(createUser('John', 30, 'admin'));
// { name: 'John', age: 30, role: 'admin' }
```

### 10.2.3. Default with undefined

```javascript
function log(message, level = 'info') {
    console.log(`[${level}] ${message}`);
}

log('Test');              // [info] Test
log('Test', undefined);   // [info] Test (uses default)
log('Test', null);        // [null] Test (null is a value)
log('Test', 'error');     // [error] Test
```

## 10.3. Advanced Default Values

### 10.3.1. Expressions as Defaults

```javascript
function createId(prefix = 'user', id = Date.now()) {
    return `${prefix}_${id}`;
}

console.log(createId());  // "user_1234567890"
```

### 10.3.2. Function Calls as Defaults

```javascript
function getDefaultName() {
    return 'Guest';
}

function greet(name = getDefaultName()) {
    return `Hello, ${name}!`;
}

console.log(greet());        // "Hello, Guest!"
console.log(greet('John'));  // "Hello, John!"
```

### 10.3.3. Previous Parameters as Defaults

```javascript
function createRange(start, end = start + 10) {
    return { start, end };
}

console.log(createRange(1));     // { start: 1, end: 11 }
console.log(createRange(5, 20)); // { start: 5, end: 20 }

// More complex
function multiply(a, b = a, c = a * b) {
    return { a, b, c };
}

console.log(multiply(2));        // { a: 2, b: 2, c: 4 }
console.log(multiply(2, 3));     // { a: 2, b: 3, c: 6 }
console.log(multiply(2, 3, 10)); // { a: 2, b: 3, c: 10 }
```

### 10.3.4. Object/Array Defaults

```javascript
function configure(options = { theme: 'light', lang: 'en' }) {
    console.log(options);
}

configure();  // { theme: 'light', lang: 'en' }
configure({ theme: 'dark' });  // { theme: 'dark' }

// Array default
function sum(numbers = [0]) {
    return numbers.reduce((a, b) => a + b);
}

console.log(sum());        // 0
console.log(sum([1, 2, 3])); // 6
```

## 10.4. With Destructuring

### 10.4.1. Object Parameter Destructuring

```javascript
// Basic destructuring with defaults
function createUser({ name = 'Guest', age = 0, role = 'user' }) {
    return { name, age, role };
}

createUser({ name: 'John' });
// { name: 'John', age: 0, role: 'user' }

// Default entire parameter
function createUser({ name = 'Guest', age = 0 } = {}) {
    return { name, age };
}

createUser();              // { name: 'Guest', age: 0 }
createUser({});            // { name: 'Guest', age: 0 }
createUser({ name: 'John' }); // { name: 'John', age: 0 }
```

### 10.4.2. Nested Destructuring

```javascript
function displayAddress({
    user = 'Guest',
    address: {
        city = 'Unknown',
        country = 'Unknown'
    } = {}
} = {}) {
    return `${user} from ${city}, ${country}`;
}

displayAddress();  // "Guest from Unknown, Unknown"
displayAddress({
    user: 'John',
    address: { city: 'NYC' }
});  // "John from NYC, Unknown"
```

### 10.4.3. Array Parameter Destructuring

```javascript
function sum([a = 0, b = 0, c = 0] = []) {
    return a + b + c;
}

console.log(sum());           // 0
console.log(sum([1]));        // 1
console.log(sum([1, 2]));     // 3
console.log(sum([1, 2, 3]));  // 6
```

## 10.5. Practical Examples

### 10.5.1. API Request Function

```javascript
async function fetchData(
    url,
    {
        method = 'GET',
        headers = {},
        timeout = 5000,
        retries = 3
    } = {}
) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            ...headers
        }
    };

    // Implementation...
    return fetch(url, options);
}

// Usage
fetchData('/api/users');
fetchData('/api/users', { method: 'POST' });
fetchData('/api/users', { timeout: 10000, retries: 5 });
```

### 10.5.2. Logger Function

```javascript
function log(
    message,
    level = 'info',
    timestamp = new Date().toISOString()
) {
    console.log(`[${timestamp}] ${level.toUpperCase()}: ${message}`);
}

log('Application started');
// [2024-01-15T10:30:00.000Z] INFO: Application started

log('Error occurred', 'error');
// [2024-01-15T10:30:00.000Z] ERROR: Error occurred
```

### 10.5.3. Pagination Function

```javascript
function paginate(items, { page = 1, pageSize = 10 } = {}) {
    const start = (page - 1) * pageSize;
    const end = start + pageSize;

    return {
        items: items.slice(start, end),
        page,
        pageSize,
        total: items.length,
        totalPages: Math.ceil(items.length / pageSize)
    };
}

const items = Array.from({ length: 100 }, (_, i) => i);
console.log(paginate(items));  // page 1, 10 items
console.log(paginate(items, { page: 2 }));  // page 2, 10 items
console.log(paginate(items, { pageSize: 20 }));  // page 1, 20 items
```

### 10.5.4. Component Configuration

```javascript
function createButton({
    text = 'Click me',
    type = 'button',
    disabled = false,
    className = 'btn',
    onClick = () => {}
} = {}) {
    return {
        render() {
            return `
                <button
                    type="${type}"
                    class="${className}"
                    ${disabled ? 'disabled' : ''}
                    onclick="${onClick}"
                >
                    ${text}
                </button>
            `;
        }
    };
}

// Usage
const btn1 = createButton();
const btn2 = createButton({ text: 'Submit', type: 'submit' });
const btn3 = createButton({ disabled: true, className: 'btn-danger' });
```

### 10.5.5. Search Function

```javascript
function search(
    query,
    {
        caseSensitive = false,
        wholeWord = false,
        regex = false,
        limit = 100
    } = {}
) {
    // Implementation
    console.log(`Searching for: ${query}`);
    console.log(`Options:`, { caseSensitive, wholeWord, regex, limit });
}

search('javascript');
search('JavaScript', { caseSensitive: true });
search('js', { wholeWord: true, limit: 50 });
```

## 10.6. Required Parameters Pattern

### 10.6.1. Throw Error for Required

```javascript
function required(param) {
    throw new Error(`Parameter ${param} is required`);
}

function createUser(
    name = required('name'),
    email = required('email'),
    age = 0
) {
    return { name, email, age };
}

// createUser();  // Error: Parameter name is required
// createUser('John');  // Error: Parameter email is required
createUser('John', 'john@example.com');  // OK
```

### 10.6.2. Optional vs Required Mix

```javascript
function updateUser(
    id = required('id'),
    updates = {}
) {
    return { id, ...updates };
}

// updateUser();  // Error
updateUser(1);  // OK
updateUser(1, { name: 'John' });  // OK
```

## 10.7. Common Patterns

### 10.7.1. Config Objects

```javascript
function initialize({
    apiUrl = 'https://api.example.com',
    timeout = 5000,
    retries = 3,
    debug = false,
    cache = true
} = {}) {
    const config = { apiUrl, timeout, retries, debug, cache };
    console.log('Initialized with config:', config);
    return config;
}
```

### 10.7.2. Backward Compatibility

```javascript
// Old signature: fn(a, b, c)
// New signature: fn(a, options)
function process(data, options = {}) {
    const {
        validate = true,
        transform = false,
        async = false
    } = options;

    // Process data...
}
```

### 10.7.3. Factory Functions

```javascript
function createCounter(initial = 0, step = 1) {
    let count = initial;

    return {
        increment() {
            count += step;
            return count;
        },
        decrement() {
            count -= step;
            return count;
        },
        getValue() {
            return count;
        }
    };
}

const counter1 = createCounter();
const counter2 = createCounter(10);
const counter3 = createCounter(0, 5);
```

## 10.8. Best Practices

### 10.8.1. Put Required Parameters First

```javascript
// Good
function createUser(name, email, age = 0, role = 'user') {
    return { name, email, age, role };
}

// Bad (hard to use)
function createUser(age = 0, role = 'user', name, email) {
    return { name, email, age, role };
}
```

### 10.8.2. Use Object for Many Parameters

```javascript
// Bad: Too many parameters
function createUser(name, email, age, role, status, active, created) {
    // ...
}

// Good: Use object
function createUser({
    name,
    email,
    age = 0,
    role = 'user',
    status = 'active',
    active = true,
    created = new Date()
} = {}) {
    // ...
}
```

### 10.8.3. Document Default Values

```javascript
/**
 * Fetches data from API
 * @param {string} url - API endpoint
 * @param {Object} options - Request options
 * @param {string} [options.method='GET'] - HTTP method
 * @param {number} [options.timeout=5000] - Request timeout in ms
 * @param {number} [options.retries=3] - Number of retries
 */
function fetchData(url, {
    method = 'GET',
    timeout = 5000,
    retries = 3
} = {}) {
    // ...
}
```

## 10.9. Common Mistakes

### 10.9.1. Falsy Values vs undefined

```javascript
function log(message, showTime = true) {
    // ...
}

log('Test', false);  // showTime = false (not true!)
log('Test', 0);      // showTime = 0 (not true!)
log('Test', '');     // showTime = '' (not true!)
log('Test', null);   // showTime = null (not true!)

// Only undefined triggers default
log('Test', undefined);  // showTime = true
log('Test');             // showTime = true
```

### 10.9.2. Parameter Order Matters

```javascript
function greet(greeting = 'Hello', name = 'Guest') {
    return `${greeting}, ${name}!`;
}

// Can't skip greeting to provide name
greet('John');  // "John, Guest!" (wrong!)

// Must use undefined
greet(undefined, 'John');  // "Hello, John!" (correct)
```

### 10.9.3. Mutable Default Objects

```javascript
// Bad: Shared default object
function addItem(item, list = []) {
    list.push(item);
    return list;
}

const list1 = addItem(1);  // [1]
const list2 = addItem(2);  // [1, 2] - WRONG! Shared array

// Fix: Create new object each time
function addItem(item, list) {
    const arr = list || [];  // Or list ?? []
    arr.push(item);
    return arr;
}
```

## 10.10. Exercises

### Exercise 1: Create Calculate Function

```javascript
// Create a function that calculates with default operator
function calculate(a, b, operator = '+') {
    // Support +, -, *, /
    // Your code
}

calculate(5, 3);      // 8 (default +)
calculate(5, 3, '*'); // 15
```

### Exercise 2: Config Function

```javascript
// Create an init function with config object defaults
function init(config = {}) {
    // Default: { debug: false, timeout: 5000, retries: 3 }
    // Your code
}
```

### Exercise 3: Required Parameters

```javascript
// Add required parameter checking
function createProduct(name, price) {
    // name and price should be required
    // category should default to 'general'
    // Your code
}
```

---

**Kết luận:** Default parameters làm code clean hơn, dễ maintain hơn và giảm boilerplate code. Kết hợp với destructuring để tạo flexible function APIs.

**Chương tiếp theo:** Enhanced Object Literals
