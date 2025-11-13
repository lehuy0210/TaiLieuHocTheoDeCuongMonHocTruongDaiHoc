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

## 10.9. Use Cases Thực Tế

### Use Case 1: API Request Configuration

```javascript
// Real-world API request builder
async function apiRequest(
    endpoint,
    {
        method = 'GET',
        headers = {},
        body = null,
        timeout = 5000,
        retries = 3,
        shouldRetry = (status) => status >= 500
    } = {}
) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            ...headers
        },
        timeout
    };

    if (body) {
        options.body = JSON.stringify(body);
    }

    let lastError;
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), timeout);

            const response = await fetch(endpoint, {
                ...options,
                signal: controller.signal
            });

            clearTimeout(timeoutId);

            if (!response.ok) {
                if (shouldRetry(response.status) && attempt < retries) {
                    await new Promise(r => setTimeout(r, 1000 * attempt));
                    continue;
                }
                throw new Error(`HTTP ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            lastError = error;
            if (attempt === retries) throw error;
        }
    }

    throw lastError;
}

// Usage
apiRequest('/api/users');
apiRequest('/api/users', { method: 'POST', body: { name: 'John' } });
apiRequest('/api/data', { timeout: 10000, retries: 5 });
```

### Use Case 2: Database Query Builder

```javascript
// SQL-like query builder with defaults
class QueryBuilder {
    constructor(
        table,
        {
            select = '*',
            where = null,
            limit = null,
            offset = 0,
            orderBy = null,
            isDistinct = false
        } = {}
    ) {
        this.table = table;
        this.select = select;
        this.where = where;
        this.limit = limit;
        this.offset = offset;
        this.orderBy = orderBy;
        this.isDistinct = isDistinct;
    }

    build() {
        let query = `SELECT ${this.isDistinct ? 'DISTINCT' : ''} ${this.select}`;
        query += ` FROM ${this.table}`;

        if (this.where) {
            query += ` WHERE ${this.where}`;
        }

        if (this.orderBy) {
            query += ` ORDER BY ${this.orderBy}`;
        }

        if (this.limit) {
            query += ` LIMIT ${this.limit}`;
        }

        if (this.offset) {
            query += ` OFFSET ${this.offset}`;
        }

        return query;
    }
}

// Usage
const builder1 = new QueryBuilder('users');
console.log(builder1.build());  // SELECT * FROM users

const builder2 = new QueryBuilder('users', {
    select: 'id, name, email',
    where: 'age > 18',
    orderBy: 'name ASC',
    limit: 10
});
console.log(builder2.build());
```

### Use Case 3: React-like Component Props

```javascript
// Component factory with default props
function createButton({
    text = 'Click me',
    type = 'button',
    disabled = false,
    className = 'btn',
    size = 'md',
    variant = 'primary',
    onClick = () => {},
    loading = false,
    icon = null
} = {}) {
    const sizeClasses = {
        sm: 'btn-sm',
        md: 'btn-md',
        lg: 'btn-lg'
    };

    const variantClasses = {
        primary: 'btn-primary',
        secondary: 'btn-secondary',
        danger: 'btn-danger'
    };

    const classes = [
        className,
        sizeClasses[size] || 'btn-md',
        variantClasses[variant] || 'btn-primary'
    ].join(' ');

    return {
        render() {
            return `
                <button
                    type="${type}"
                    class="${classes}"
                    ${disabled || loading ? 'disabled' : ''}
                    onclick="${onClick}"
                >
                    ${loading ? '<span class="spinner"></span>' : ''}
                    ${icon ? `<i class="${icon}"></i>` : ''}
                    ${text}
                </button>
            `;
        }
    };
}

// Usage
const btn1 = createButton();
const btn2 = createButton({ text: 'Submit', variant: 'primary', size: 'lg' });
const btn3 = createButton({ text: 'Delete', variant: 'danger', disabled: true });
const btn4 = createButton({
    text: 'Download',
    icon: 'icon-download',
    size: 'lg'
});
```

### Use Case 4: Logger with Formatting

```javascript
// Advanced logger with default formatting
class Logger {
    constructor(options = {}) {
        this.level = options.level || 'info';
        this.format = options.format || 'simple';
        this.colors = options.colors !== false;
        this.timestamp = options.timestamp !== false;
        this.context = options.context || '';
    }

    log(message, data = {}, level = 'info') {
        if (!this.shouldLog(level)) return;

        const timestamp = this.timestamp ? new Date().toISOString() : '';
        const prefix = this.context ? `[${this.context}]` : '';

        let output = '';
        if (this.format === 'simple') {
            output = `${timestamp} ${prefix} [${level.toUpperCase()}] ${message}`;
        } else if (this.format === 'json') {
            output = JSON.stringify({
                timestamp,
                level,
                context: this.context,
                message,
                data
            });
        }

        console.log(output);
        if (Object.keys(data).length > 0) {
            console.log(data);
        }
    }

    shouldLog(level) {
        const levels = { debug: 0, info: 1, warn: 2, error: 3 };
        return levels[level] >= levels[this.level];
    }

    info(message, data = {}) {
        this.log(message, data, 'info');
    }

    error(message, data = {}) {
        this.log(message, data, 'error');
    }
}

// Usage
const logger = new Logger({
    level: 'info',
    format: 'json',
    context: 'MyApp'
});

logger.info('User logged in', { userId: 123 });
logger.error('Failed to fetch', { status: 500 });
```

### Use Case 5: Validation with Default Rules

```javascript
// Validator with default rules
class Validator {
    constructor(schema = {}) {
        this.schema = schema;
    }

    validate(data) {
        const errors = {};

        for (const [field, rules] of Object.entries(this.schema)) {
            const value = data[field];
            const fieldErrors = [];

            const {
                required = false,
                type = 'string',
                minLength = 0,
                maxLength = Infinity,
                min = -Infinity,
                max = Infinity,
                pattern = null,
                custom = null,
                message = {}
            } = rules;

            // Required check
            if (required && !value) {
                fieldErrors.push(message.required || `${field} is required`);
                continue;
            }

            if (!value) continue;

            // Type check
            if (typeof value !== type) {
                fieldErrors.push(message.type || `${field} must be ${type}`);
                continue;
            }

            // Length check
            if (type === 'string') {
                if (value.length < minLength) {
                    fieldErrors.push(message.minLength || `${field} too short`);
                }
                if (value.length > maxLength) {
                    fieldErrors.push(message.maxLength || `${field} too long`);
                }
            }

            // Number range check
            if (type === 'number') {
                if (value < min) {
                    fieldErrors.push(message.min || `${field} too small`);
                }
                if (value > max) {
                    fieldErrors.push(message.max || `${field} too large`);
                }
            }

            // Pattern check
            if (pattern && !pattern.test(value)) {
                fieldErrors.push(message.pattern || `${field} format invalid`);
            }

            // Custom validation
            if (custom && !custom(value)) {
                fieldErrors.push(message.custom || `${field} validation failed`);
            }

            if (fieldErrors.length > 0) {
                errors[field] = fieldErrors;
            }
        }

        return {
            valid: Object.keys(errors).length === 0,
            errors
        };
    }
}

// Usage
const userValidator = new Validator({
    name: {
        required: true,
        type: 'string',
        minLength: 2,
        maxLength: 50,
        message: { required: 'Name is required' }
    },
    email: {
        required: true,
        type: 'string',
        pattern: /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/,
        message: { pattern: 'Invalid email format' }
    },
    age: {
        type: 'number',
        min: 18,
        max: 120,
        message: { min: 'Must be 18 or older' }
    }
});

const result = userValidator.validate({
    name: 'John Doe',
    email: 'john@example.com',
    age: 25
});

console.log(result);  // { valid: true, errors: {} }
```

## 10.10. Tips & Tricks

### Tip 1: Conditional Defaults with OR

```javascript
// Default parameter with OR operator
function getConfig(options) {
    // Old way
    const config = {
        timeout: options.timeout || 5000,
        retries: options.retries || 3
    };

    // Using default parameters
    return function() {
        const { timeout = 5000, retries = 3 } = options;
        return { timeout, retries };
    }
}
```

### Tip 2: Using Previous Parameters

```javascript
// Use previous parameter as default
function createDateRange(
    start = new Date(),
    end = new Date(start.getTime() + 24 * 60 * 60 * 1000)
) {
    return { start, end };
}

createDateRange();  // Current date + 1 day
createDateRange(new Date('2024-01-01'));  // Jan 1 + 1 day
```

### Tip 3: Lazy Evaluation of Defaults

```javascript
// Default values are evaluated at call time, not definition time
let counter = 0;

function getCounter(value = counter++) {
    return value;
}

console.log(getCounter());  // 0
console.log(getCounter());  // 1
console.log(getCounter());  // 2
```

### Tip 4: Required Parameters Pattern

```javascript
// Make parameters required using error function
const required = (param) => {
    throw new Error(`${param} is required`);
};

function createUser(
    name = required('name'),
    email = required('email')
) {
    return { name, email };
}

// createUser();  // Error
createUser('John', 'john@example.com');  // OK
```

### Tip 5: Nested Defaults with Destructuring

```javascript
// Combine defaults with destructuring
function processConfig({
    app: {
        name = 'MyApp',
        version = '1.0.0'
    } = {},
    database: {
        host = 'localhost',
        port = 3306
    } = {}
} = {}) {
    return { app: { name, version }, database: { host, port } };
}

processConfig();
processConfig({ app: { name: 'CustomApp' } });
```

### Tip 6: Spread with Defaults

```javascript
// Combine spread operator with defaults
function merge(target = {}, source = {}) {
    return { ...target, ...source };
}

merge();  // {}
merge({ a: 1 });  // { a: 1 }
merge({ a: 1 }, { b: 2 });  // { a: 1, b: 2 }
```

### Tip 7: Arrow Functions with Defaults

```javascript
// Arrow functions support default parameters
const greet = (name = 'Guest', greeting = 'Hello') =>
    `${greeting}, ${name}!`;

greet();  // "Hello, Guest!"
greet('John');  // "Hello, John!"

// Short callbacks with defaults
const map = (fn = x => x) => arr => arr.map(fn);
```

### Tip 8: Callback with Default Handler

```javascript
// Default callback function
function process(data, onSuccess = console.log, onError = console.error) {
    try {
        const result = transform(data);
        onSuccess(result);
    } catch (error) {
        onError(error);
    }
}

process({ value: 10 });  // Logs to console
process(
    { value: 10 },
    (result) => alert(`Success: ${result}`),
    (error) => alert(`Error: ${error}`)
);
```

### Tip 9: Method Chaining with Defaults

```javascript
// Builder pattern with default options
class QueryBuilder {
    constructor(table = 'users') {
        this.table = table;
        this.filters = [];
        this.sorts = [];
    }

    where(condition = 'true') {
        this.filters.push(condition);
        return this;
    }

    sort(field = 'id', direction = 'ASC') {
        this.sorts.push(`${field} ${direction}`);
        return this;
    }

    build() {
        return `SELECT * FROM ${this.table}`;
    }
}

new QueryBuilder()
    .where('age > 18')
    .sort('name')
    .build();
```

### Tip 10: Factory Functions with Defaults

```javascript
// Factory with configuration defaults
function createTimer(
    callback = () => {},
    interval = 1000,
    autoStart = true
) {
    let timerId;
    let running = false;

    return {
        start() {
            if (running) return;
            running = true;
            timerId = setInterval(callback, interval);
        },
        stop() {
            running = false;
            clearInterval(timerId);
        },
        isRunning: () => running
    };
}

// Use defaults
const timer = createTimer(() => console.log('tick'));
timer.start();
```

## 10.11. Common Mistakes

### Mistake 1: Falsy Values vs undefined

```javascript
// BAD: Falsy values trigger default
function log(message, showTime = true) {
    console.log(message, showTime);
}

log('Test', false);  // showTime = false (expected)
log('Test', 0);      // showTime = 0 (expected)
log('Test', '');     // showTime = '' (expected)

// GOOD: Only undefined triggers default
log('Test', undefined);  // showTime = true
log('Test');             // showTime = true
```

### Mistake 2: Parameter Order Matters

```javascript
// BAD: Can't skip parameters
function greet(greeting = 'Hello', name = 'Guest') {
    return `${greeting}, ${name}!`;
}

greet('John');  // "John, Guest!" (John treated as greeting!)

// GOOD: Use undefined to skip
greet(undefined, 'John');  // "Hello, John!"

// BETTER: Use object destructuring
function greetBetter({ greeting = 'Hello', name = 'Guest' } = {}) {
    return `${greeting}, ${name}!`;
}

greetBetter({ name: 'John' });  // "Hello, John!"
```

### Mistake 3: Mutable Default Objects

```javascript
// BAD: Shared reference across calls
function addItem(item, list = []) {
    list.push(item);
    return list;
}

const list1 = addItem(1);  // [1]
const list2 = addItem(2);  // [2] - New list created each time!
// Actually this is OK because [] creates new array each time

// REALLY BAD: Shared object
const defaultConfig = { timeout: 5000 };
function fetchData(url, config = defaultConfig) {
    config.timeout = 3000;  // Modifies shared object!
    return fetch(url, config);
}

fetchData('/api/1');  // config.timeout = 3000
fetchData('/api/2');  // config.timeout already 3000!

// GOOD: Create new object
function fetchDataGood(url, config = {}) {
    const opts = { timeout: 5000, ...config };
    return fetch(url, opts);
}
```

### Mistake 4: Complex Expressions as Defaults

```javascript
// BAD: Performance issue
function process(data = complexExpensive()) {
    // Called every time function is defined, not called!
}

// GOOD: Lazy evaluation
function processGood(data) {
    if (data === undefined) {
        data = complexExpensive();
    }
}

// Or keep complex defaults
function processArrow(data = undefined) {
    data = data ?? complexExpensive();
}
```

### Mistake 5: this Binding Issues

```javascript
// BAD: this is not bound correctly
function User(name = 'Guest') {
    this.name = name;
}

User.prototype.greet = function(greeting = 'Hello') {
    return `${greeting}, ${this.name}!`;
};

const user = new User('John');
const greetFn = user.greet;
greetFn();  // "Hello, undefined!" - this is undefined

// GOOD: Use arrow function or bind
const user2 = new User('John');
const greetFn2 = () => user2.greet();
greetFn2();  // "Hello, John!"
```

### Mistake 6: Optional vs Required Confusion

```javascript
// BAD: No clear indication what's required
function createProduct(name, price, category, discount) {
    // Which are required?
}

// GOOD: Clear required and optional
function createProductGood(
    name,  // required
    price,  // required
    category = 'general',  // optional
    discount = 0  // optional
) {
    return { name, price, category, discount };
}
```

### Mistake 7: Destructuring with Missing Properties

```javascript
// BAD: Will throw if property doesn't exist
function process({ value } = {}) {
    console.log(value.toString());  // Error if value is undefined
}

// GOOD: Provide defaults
function processGood({ value = 0 } = {}) {
    console.log(value.toString());
}
```

### Mistake 8: Array Destructuring Defaults

```javascript
// BAD: Defaults not applied properly
function process([a, b, c] = []) {
    console.log(a, b, c);
}

process([1]);  // 1, undefined, undefined

// GOOD: Provide defaults in destructuring
function processGood([a = 0, b = 0, c = 0] = []) {
    console.log(a, b, c);
}

processGood([1]);  // 1, 0, 0
```

### Mistake 9: Null vs undefined Handling

```javascript
// BAD: null not handled as default trigger
function log(message, showTime = true) {
    console.log(message, showTime);
}

log('Test', null);  // showTime = null (not true!)

// GOOD: Use nullish coalescing
function logGood(message, showTime) {
    const time = showTime ?? true;
    console.log(message, time);
}

logGood('Test', null);  // showTime = true
```

### Mistake 10: Hoisting and Temporal Dead Zone

```javascript
// BAD: Using variable before declaration
function test(value = getValue()) {
    // getValue might not be defined yet
}

// GOOD: Define function first
const getValue = () => 'default';

function testGood(value = getValue()) {
    // Now getValue is defined
}
```

## 10.12. Troubleshooting Issues

### Issue 1: Default Not Applied

**Problem:**
```javascript
function log(message, showTime = true) {
    console.log(message, showTime);
}

log('Test', 0);  // showTime = 0 (not true)
log('Test', false);  // showTime = false (not true)
```

**Solution:**
```javascript
// Only undefined triggers default
function logFixed(message, showTime = true) {
    if (showTime === undefined) {
        showTime = true;
    }
    console.log(message, showTime);
}

// Or use nullish coalescing
function logBetter(message, showTime) {
    showTime = showTime ?? true;
    console.log(message, showTime);
}
```

### Issue 2: Complex Expressions in Defaults

**Problem:**
```javascript
// This might cause issues
function process(data = JSON.parse(jsonString)) {
    // jsonString might not be available
}
```

**Solution:**
```javascript
// Evaluate in function body instead
function processFixed(data) {
    if (data === undefined) {
        data = JSON.parse(jsonString);
    }
    return data;
}

// Or define variable first
const defaultData = JSON.parse(jsonString);
function processBetter(data = defaultData) {
    return data;
}
```

### Issue 3: Shared Mutable Objects

**Problem:**
```javascript
function addItem(item, list = [1, 2, 3]) {
    list.push(item);
    return list;
}

const arr1 = addItem(4);  // [1, 2, 3, 4]
const arr2 = addItem(5);  // [1, 2, 3, 5] - New array each time
```

**Solution:**
```javascript
// Create new array each time (default behavior)
function addItemFixed(item, list) {
    list = list || [1, 2, 3];
    list.push(item);
    return list;
}

// Or avoid modification
function addItemBetter(item, list = [1, 2, 3]) {
    return [...list, item];
}
```

### Issue 4: Destructuring with Wrong Shape

**Problem:**
```javascript
function process({ name, age } = {}) {
    console.log(name, age);
}

process();  // undefined, undefined
process({});  // undefined, undefined
process({ name: 'John' });  // 'John', undefined

// What if wrong shape passed?
process('string');  // Error: Cannot destructure string
```

**Solution:**
```javascript
// Use proper defaults
function processFixed({ name = 'Guest', age = 0 } = {}) {
    console.log(name, age);
}

// Or type check
function processSafe(options = {}) {
    if (typeof options !== 'object') {
        options = {};
    }
    const { name = 'Guest', age = 0 } = options;
    console.log(name, age);
}
```

### Issue 5: Performance with Expensive Defaults

**Problem:**
```javascript
function fetch(url, options = getDefaultOptions()) {
    // getDefaultOptions() called on each definition
}

// Better but still inefficient
function fetchData(url, options) {
    const opts = options || getDefaultOptions();
}
```

**Solution:**
```javascript
// Lazy evaluation
function fetchLazy(url, options) {
    if (options === undefined) {
        options = getDefaultOptions();
    }
}

// Or cache default
const DEFAULT_OPTIONS = getDefaultOptions();
function fetchCached(url, options = DEFAULT_OPTIONS) {
    return fetch(url, options);
}

// Or use nullish coalescing
function fetchNulls(url, options = null) {
    options = options ?? getDefaultOptions();
}
```

### Issue 6: Rest Parameters with Defaults

**Problem:**
```javascript
// Can't have rest with defaults easily
function process(...items = []) {  // Error
    // Code
}
```

**Solution:**
```javascript
// Rest must be last, no defaults possible
function processFixed(...items) {
    items = items.length === 0 ? [] : items;
}

// Alternative: use parameters first
function processBetter(defaultValue = 'item', ...items) {
    items = items.length === 0 ? [defaultValue] : items;
}

// Or check after
function processBest(...items) {
    if (items.length === 0) {
        items = [getDefault()];
    }
}
```

### Issue 7: Method Defaults with this

**Problem:**
```javascript
class User {
    name = 'Guest';

    greet(greeting = 'Hello') {
        return `${greeting}, ${this.name}!`;
    }
}

const user = new User();
const fn = user.greet;
fn();  // "Hello, undefined!" - this is not bound
```

**Solution:**
```javascript
class UserFixed {
    name = 'Guest';

    // Use arrow function to bind this
    greet = (greeting = 'Hello') => {
        return `${greeting}, ${this.name}!`;
    };
}

const user = new UserFixed();
const fn = user.greet;
fn();  // "Hello, Guest!"
```

### Issue 8: Conditional Defaults

**Problem:**
```javascript
// Hard to have conditional defaults
function process(mode = 'dev') {
    const config = mode === 'dev'
        ? { debug: true }
        : { debug: false };
}
```

**Solution:**
```javascript
// Use function for complex logic
const getConfig = (mode) => {
    if (mode === 'dev') return { debug: true };
    return { debug: false };
};

function processFixed(mode = 'dev', config = getConfig(mode)) {
    // Code
}
```

### Issue 9: Document Default Values

**Problem:**
```javascript
function process(options) {
    // What are default values?
    const { timeout, retries, cache } = options || {};
}
```

**Solution:**
```javascript
/**
 * Process data
 * @param {Object} options - Configuration options
 * @param {number} [options.timeout=5000] - Request timeout in ms
 * @param {number} [options.retries=3] - Number of retries
 * @param {boolean} [options.cache=true] - Enable caching
 */
function processDocumented({
    timeout = 5000,
    retries = 3,
    cache = true
} = {}) {
    // Code
}
```

### Issue 10: Testing with Defaults

**Problem:**
```javascript
function calculate(a, b = 10) {
    return a + b;
}

// Hard to test default behavior
test('calculate with default', () => {
    expect(calculate(5)).toBe(15);
});
```

**Solution:**
```javascript
// Extract logic for easier testing
const calculateWithDefault = (a, b = 10) => a + b;

// Test both cases
test('with default', () => {
    expect(calculateWithDefault(5)).toBe(15);
});

test('with explicit value', () => {
    expect(calculateWithDefault(5, 20)).toBe(25);
});
```

## 10.13. Advanced Topics

### 10.13.1. Dynamic Defaults with Getters

```javascript
// Use getter for dynamic defaults
class Configuration {
    get #defaultTimeout() {
        return navigator.connection?.effectiveType === '4g' ? 5000 : 10000;
    }

    fetch(url, { timeout = this.#defaultTimeout } = {}) {
        return fetch(url, { signal: AbortSignal.timeout(timeout) });
    }
}
```

### 10.13.2. Defaults with Symbols

```javascript
// Use symbols for private defaults
const DEFAULT_CONFIG = Symbol('defaultConfig');

function createApp({
    name = 'MyApp',
    [DEFAULT_CONFIG]: config = { debug: false }
} = {}) {
    return { name, debug: config.debug };
}

createApp({ name: 'CustomApp' });
```

### 10.13.3. Recursive Defaults

```javascript
// Defaults with recursive structures
function buildTree({
    value,
    children = [],
    metadata = {
        id: Math.random(),
        created: new Date()
    }
} = {}) {
    return {
        value,
        children,
        metadata
    };
}

buildTree({ value: 'root' });
```

### 10.13.4. Proxy for Default Handling

```javascript
// Use Proxy to intercept undefined defaults
function createConfig(config = {}) {
    return new Proxy(config, {
        get(target, prop) {
            if (!(prop in target)) {
                // Return sensible default for missing property
                return getDefaultValue(prop);
            }
            return target[prop];
        }
    });
}

const config = createConfig({ timeout: 5000 });
console.log(config.timeout);  // 5000
console.log(config.retries);  // undefined or default
```

### 10.13.5. Type-Safe Defaults with Validation

```javascript
// Defaults with runtime type checking
function validateConfig({
    port = 3000,
    host = 'localhost',
    timeout = 5000
} = {}) {
    const validators = {
        port: (v) => typeof v === 'number' && v > 0 && v < 65536,
        host: (v) => typeof v === 'string',
        timeout: (v) => typeof v === 'number' && v > 0
    };

    const config = { port, host, timeout };

    for (const [key, value] of Object.entries(config)) {
        if (!validators[key](value)) {
            throw new TypeError(`Invalid ${key}: ${value}`);
        }
    }

    return config;
}
```

## 10.14. Best Practices

### 10.14.1. Put Required First

```javascript
// DO: Required parameters first
function createUser(name, email, age = 0, role = 'user') {
    return { name, email, age, role };
}

// DON'T: Hard to use
function createUserBad(age = 0, role = 'user', name, email) {
    return { name, email, age, role };
}
```

### 10.14.2. Use Objects for Many Parameters

```javascript
// DO: Use object for many parameters
function createUser({
    name,
    email,
    age = 0,
    role = 'user',
    verified = false
} = {}) {
    return { name, email, age, role, verified };
}

// DON'T: Too many parameters
function createUserBad(name, email, age, role, verified) {
    // Hard to read and call
}
```

### 10.14.3. Document Defaults

```javascript
/**
 * @param {string} url - API endpoint
 * @param {Object} options - Request options
 * @param {string} [options.method='GET'] - HTTP method
 * @param {number} [options.timeout=5000] - Timeout in ms
 * @returns {Promise}
 */
function apiRequest(url, {
    method = 'GET',
    timeout = 5000
} = {}) {
    // Implementation
}
```

## 10.15. Exercises

### Exercise 1 (Dễ): Create Calculate Function

```javascript
// Create a function that calculates with default operator
function calculate(a, b, operator = '+') {
    // Support +, -, *, /
    // Your code
}

calculate(5, 3);      // 8 (default +)
calculate(5, 3, '*'); // 15
calculate(10, 2, '/'); // 5
```

### Exercise 2 (Dễ): Config Function

```javascript
// Create an init function with config object defaults
function init(config = {}) {
    // Default: { debug: false, timeout: 5000, retries: 3 }
    const { debug = false, timeout = 5000, retries = 3 } = config;
    return { debug, timeout, retries };
}
```

### Exercise 3 (Dễ): Required Parameters

```javascript
// Add required parameter checking
function createProduct(name, price, category = 'general') {
    // name and price should be required
    // category should default to 'general'
    // Your code
}
```

### Exercise 4 (Dễ): Greet Function

```javascript
// Create greet function with default name and greeting
function greet(name = 'Guest', greeting = 'Hello') {
    return `${greeting}, ${name}!`;
}

greet();  // "Hello, Guest!"
greet('John');  // "Hello, John!"
greet('Jane', 'Hi');  // "Hi, Jane!"
```

### Exercise 5 (Trung bình): Logger Function

```javascript
// Create logger with default level and format
function log(message, level = 'info', format = 'simple') {
    // Implement different formats: simple, json, detailed
    // Your code
}

log('Test');
log('Error occurred', 'error');
log('User logged in', 'info', 'detailed');
```

### Exercise 6 (Trung bình): API Request Builder

```javascript
// Create API request function with default options
async function request(url, {
    method = 'GET',
    headers = {},
    body = null,
    timeout = 5000
} = {}) {
    // Implementation using fetch
    // Your code
}
```

### Exercise 7 (Trung bình): Pagination Function

```javascript
// Create paginate function with defaults
function paginate(items, { page = 1, pageSize = 10 } = {}) {
    // Return paginated items with metadata
    // Your code
}

const items = Array.from({ length: 100 }, (_, i) => i);
paginate(items);  // page 1, 10 items
paginate(items, { page: 2, pageSize: 20 });
```

### Exercise 8 (Trung bình): Settings Manager

```javascript
// Create settings manager with nested defaults
class Settings {
    constructor({
        ui = { theme: 'light', fontSize: 14 },
        notifications = { email: true, push: false },
        privacy = { profile: 'public', activity: 'private' }
    } = {}) {
        this.ui = ui;
        this.notifications = notifications;
        this.privacy = privacy;
    }

    update(newSettings = {}) {
        // Merge new settings with existing ones
    }
}
```

### Exercise 9 (Khó): Configuration Class

```javascript
// Create advanced configuration class
class Config {
    constructor(overrides = {}) {
        const defaults = {
            app: { name: 'MyApp', version: '1.0.0' },
            server: { host: 'localhost', port: 3000 },
            database: { url: 'mongodb://localhost' }
        };

        // Implement deep merge with overrides
        // Your code
    }

    get(path = '') {
        // Get nested value by path: 'server.port'
    }
}
```

### Exercise 10 (Khó): Validator with Defaults

```javascript
// Create validator with default rules
class Validator {
    constructor(schema = {}) {
        // Implement rule defaults
        // Support: required, type, minLength, maxLength, pattern, custom
        // Your code
    }

    validate(data = {}) {
        // Return { valid: true/false, errors: {} }
    }
}
```

### Exercise 11 (Khó): Factory with Options

```javascript
// Create factory function with complex defaults
function createConnection({
    host = 'localhost',
    port = 5432,
    username = 'admin',
    password = '',
    database = 'default',
    ssl = false,
    timeout = 5000,
    pool = { min: 2, max: 10 }
} = {}) {
    // Create database connection with defaults
    // Implement connection pooling
    // Your code
}
```

### Exercise 12 (Khó): Middleware Chain

```javascript
// Create middleware chain with default handlers
function createMiddlewareChain(
    middlewares = [],
    errorHandler = console.error,
    finalHandler = (ctx) => ctx
) {
    // Chain middleware with proper error handling
    // Return function that processes request
    // Your code
}
```

---

**Kết luận:** Default parameters làm code clean hơn, dễ maintain hơn và giảm boilerplate code. Kết hợp với destructuring để tạo flexible function APIs.

**Chương tiếp theo:** Enhanced Object Literals
