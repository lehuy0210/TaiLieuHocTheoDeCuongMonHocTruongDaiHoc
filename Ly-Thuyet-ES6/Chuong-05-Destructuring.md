# CHƯƠNG 5: DESTRUCTURING

## 5.1. Giới thiệu Destructuring

Destructuring cho phép extract values từ arrays hoặc properties từ objects vào distinct variables.

### 5.1.1. Why Destructuring?

**ES5:**
```javascript
var user = { name: 'John', age: 30 };
var name = user.name;
var age = user.age;

var numbers = [1, 2, 3];
var first = numbers[0];
var second = numbers[1];
```

**ES6:**
```javascript
const user = { name: 'John', age: 30 };
const { name, age } = user;

const numbers = [1, 2, 3];
const [first, second] = numbers;
```

## 5.2. Object Destructuring

### 5.2.1. Basic Syntax

```javascript
const user = {
    name: 'John',
    age: 30,
    city: 'NYC'
};

// Extract properties
const { name, age, city } = user;

console.log(name);  // "John"
console.log(age);   // 30
console.log(city);  // "NYC"
```

### 5.2.2. Variable Renaming

```javascript
const user = { name: 'John', age: 30 };

// Rename variables
const { name: userName, age: userAge } = user;

console.log(userName);  // "John"
console.log(userAge);   // 30
// console.log(name);   // ReferenceError
```

### 5.2.3. Default Values

```javascript
const user = { name: 'John' };

// Provide defaults for missing properties
const { name, age = 25, city = 'Unknown' } = user;

console.log(name);  // "John"
console.log(age);   // 25 (default)
console.log(city);  // "Unknown" (default)
```

### 5.2.4. Combining Rename and Default

```javascript
const user = { name: 'John' };

const { name: userName, age: userAge = 30 } = user;

console.log(userName);  // "John"
console.log(userAge);   // 30 (default)
```

### 5.2.5. Nested Objects

```javascript
const user = {
    name: 'John',
    address: {
        city: 'NYC',
        country: 'USA'
    }
};

// Nested destructuring
const {
    name,
    address: { city, country }
} = user;

console.log(name);     // "John"
console.log(city);     // "NYC"
console.log(country);  // "USA"
// console.log(address); // ReferenceError (address not extracted)
```

### 5.2.6. Deep Nesting

```javascript
const data = {
    user: {
        profile: {
            name: 'John',
            age: 30
        }
    }
};

const {
    user: {
        profile: { name, age }
    }
} = data;

console.log(name, age);  // "John" 30
```

## 5.3. Array Destructuring

### 5.3.1. Basic Syntax

```javascript
const numbers = [1, 2, 3, 4, 5];

// Extract elements
const [first, second, third] = numbers;

console.log(first);   // 1
console.log(second);  // 2
console.log(third);   // 3
```

### 5.3.2. Skipping Elements

```javascript
const numbers = [1, 2, 3, 4, 5];

// Skip elements with commas
const [first, , third, , fifth] = numbers;

console.log(first);  // 1
console.log(third);  // 3
console.log(fifth);  // 5
```

### 5.3.3. Default Values

```javascript
const numbers = [1];

const [first, second = 2, third = 3] = numbers;

console.log(first);   // 1
console.log(second);  // 2 (default)
console.log(third);   // 3 (default)
```

### 5.3.4. Rest Elements

```javascript
const numbers = [1, 2, 3, 4, 5];

// Collect remaining elements
const [first, second, ...rest] = numbers;

console.log(first);   // 1
console.log(second);  // 2
console.log(rest);    // [3, 4, 5]
```

### 5.3.5. Swapping Variables

```javascript
let a = 1;
let b = 2;

// Swap without temp variable
[a, b] = [b, a];

console.log(a);  // 2
console.log(b);  // 1
```

### 5.3.6. Nested Arrays

```javascript
const nested = [1, [2, 3], 4];

const [first, [second, third], fourth] = nested;

console.log(first);   // 1
console.log(second);  // 2
console.log(third);   // 3
console.log(fourth);  // 4
```

## 5.4. Function Parameters

### 5.4.1. Object Parameters

```javascript
// Without destructuring
function displayUser(user) {
    console.log(user.name);
    console.log(user.age);
}

// With destructuring
function displayUser({ name, age }) {
    console.log(name);
    console.log(age);
}

displayUser({ name: 'John', age: 30 });
```

### 5.4.2. Default Parameter Values

```javascript
function createUser({ name, age = 25, city = 'NYC' }) {
    return { name, age, city };
}

createUser({ name: 'John' });
// { name: 'John', age: 25, city: 'NYC' }
```

### 5.4.3. Default Parameter Object

```javascript
function createUser({ name, age } = {}) {
    return { name: name || 'Guest', age: age || 0 };
}

createUser();  // { name: 'Guest', age: 0 }
createUser({ name: 'John', age: 30 });  // { name: 'John', age: 30 }
```

### 5.4.4. Array Parameters

```javascript
function sum([a, b, c]) {
    return a + b + c;
}

sum([1, 2, 3]);  // 6
```

### 5.4.5. Mixed Destructuring

```javascript
function displayData({ user: { name, age }, items: [first, second] }) {
    console.log(`${name}, ${age}`);
    console.log(`First item: ${first}, Second item: ${second}`);
}

displayData({
    user: { name: 'John', age: 30 },
    items: ['Apple', 'Banana', 'Orange']
});
```

## 5.5. Practical Examples

### 5.5.1. API Response Handling

```javascript
// Fetch user data
fetch('/api/user')
    .then(response => response.json())
    .then(({ id, name, email, profile: { avatar } }) => {
        console.log(`${name} (${email})`);
        console.log(`Avatar: ${avatar}`);
    });
```

### 5.5.2. React Props

```javascript
// React component with destructured props
function UserCard({ name, age, avatar, isOnline = false }) {
    return `
        <div class="card">
            <img src="${avatar}" alt="${name}" />
            <h3>${name}</h3>
            <p>Age: ${age}</p>
            <span>${isOnline ? 'Online' : 'Offline'}</span>
        </div>
    `;
}
```

### 5.5.3. Config Objects

```javascript
function initApp({
    apiUrl = 'https://api.example.com',
    timeout = 5000,
    retries = 3,
    debug = false
} = {}) {
    console.log('API URL:', apiUrl);
    console.log('Timeout:', timeout);
    console.log('Retries:', retries);
    console.log('Debug:', debug);
}

initApp({ apiUrl: 'https://custom.com', debug: true });
```

### 5.5.4. Returning Multiple Values

```javascript
function getMinMax(numbers) {
    return {
        min: Math.min(...numbers),
        max: Math.max(...numbers),
        length: numbers.length
    };
}

const { min, max, length } = getMinMax([1, 2, 3, 4, 5]);
console.log(`Min: ${min}, Max: ${max}, Count: ${length}`);
```

### 5.5.5. For-of Loop

```javascript
const users = [
    { id: 1, name: 'John', age: 30 },
    { id: 2, name: 'Jane', age: 25 }
];

for (const { id, name, age } of users) {
    console.log(`${id}: ${name} (${age})`);
}
```

### 5.5.6. Array Methods

```javascript
const users = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 },
    { name: 'Bob', age: 35 }
];

// map
const names = users.map(({ name }) => name);

// filter
const adults = users.filter(({ age }) => age >= 30);

// forEach
users.forEach(({ name, age }) => {
    console.log(`${name}: ${age}`);
});
```

## 5.6. Advanced Patterns

### 5.6.1. Computed Property Names

```javascript
const key = 'name';
const { [key]: value } = { name: 'John', age: 30 };

console.log(value);  // "John"
```

### 5.6.2. Rest in Objects

```javascript
const user = {
    id: 1,
    name: 'John',
    age: 30,
    city: 'NYC',
    country: 'USA'
};

const { id, ...userData } = user;

console.log(id);         // 1
console.log(userData);   // { name: 'John', age: 30, city: 'NYC', country: 'USA' }
```

### 5.6.3. Combining Arrays and Objects

```javascript
const data = {
    user: 'John',
    scores: [85, 90, 95]
};

const { user, scores: [test1, test2, test3] } = data;

console.log(user);   // "John"
console.log(test1);  // 85
console.log(test2);  // 90
console.log(test3);  // 95
```

### 5.6.4. Function Chaining

```javascript
const process = ({ value }) => ({ value: value * 2 });
const format = ({ value }) => ({ result: `Value: ${value}` });

const { result } = format(process({ value: 10 }));
console.log(result);  // "Value: 20"
```

## 5.7. Common Patterns

### 5.7.1. Object Property Extraction

```javascript
// Extract specific properties
const { name, age } = user;

// Extract and rename
const { name: userName, age: userAge } = user;

// Extract with defaults
const { name, age = 25 } = user;
```

### 5.7.2. Array Element Extraction

```javascript
// Get first and last
const [first, ...middle] = array;
const last = middle.pop();

// Or using length
const [first] = array;
const last = array[array.length - 1];
```

### 5.7.3. Partial Extraction

```javascript
// Only get what you need
const { name } = user;  // Ignore other properties

const [first] = array;  // Ignore other elements
```

## 5.8. Best Practices

### 5.8.1. Readability

```javascript
// Good: Clear destructuring
const { name, age } = user;

// Bad: Too much nesting
const { user: { profile: { address: { city } } } } = data;

// Better: Break it down
const { user } = data;
const { profile } = user;
const { address } = profile;
const { city } = address;
```

### 5.8.2. Default Values

```javascript
// Always provide defaults for optional properties
function createUser({ name, age = 0, city = 'Unknown' } = {}) {
    return { name, age, city };
}
```

### 5.8.3. Error Handling

```javascript
// Safe destructuring
try {
    const { data: { user: { name } } } = response;
} catch (error) {
    console.error('Invalid response structure');
}

// Or use optional chaining (ES2020)
const name = response?.data?.user?.name;
```

## 5.9. Common Mistakes

### 5.9.1. Destructuring null/undefined

```javascript
// Error: Cannot destructure undefined
const { name } = undefined;  // TypeError

// Fix: Provide default
const { name } = undefined || {};  // OK
const { name } = user ?? {};       // OK (nullish coalescing)
```

### 5.9.2. Variable Already Declared

```javascript
let name = 'Jane';

// Error: name already declared
let { name } = { name: 'John' };  // SyntaxError

// Fix: Use different name
let { name: userName } = { name: 'John' };
```

### 5.9.3. Assigning to Existing Variables

```javascript
let name, age;

// Wrong: This is a block, not destructuring
{ name, age } = user;  // SyntaxError

// Correct: Wrap in parentheses
({ name, age } = user);  // OK
```

## 5.10. Advanced Practical Examples

### Example 1: Advanced Data Processing Pipeline

```javascript
class DataProcessor {
    process(data) {
        return this.transform(data)
            .then(this.validate)
            .then(this.enrich)
            .then(this.format);
    }

    transform({ records, metadata }) {
        const transformed = records.map(({ id, value, timestamp }) => ({
            id,
            value: value * 2,
            processedAt: new Date(timestamp).toISOString()
        }));

        return Promise.resolve({
            records: transformed,
            metadata: { ...metadata, transformed: true }
        });
    }

    validate({ records, metadata }) {
        const valid = records.filter(({ value }) => value > 0);

        if (valid.length === 0) {
            throw new Error('No valid records');
        }

        return Promise.resolve({
            records: valid,
            metadata: { ...metadata, validated: true }
        });
    }

    enrich({ records, metadata }) {
        const enriched = records.map(record => {
            const { id, value, processedAt } = record;
            return {
                ...record,
                enriched: {
                    category: value > 100 ? 'high' : 'low',
                    processed: true
                }
            };
        });

        return Promise.resolve({
            records: enriched,
            metadata: { ...metadata, enriched: true }
        });
    }

    format({ records, metadata }) {
        const { transformed, validated, enriched } = metadata;

        return Promise.resolve({
            data: records,
            summary: {
                total: records.length,
                pipeline: { transformed, validated, enriched }
            }
        });
    }
}

// Usage
const processor = new DataProcessor();

processor.process({
    records: [
        { id: 1, value: 50, timestamp: Date.now() },
        { id: 2, value: 150, timestamp: Date.now() }
    ],
    metadata: { source: 'api' }
}).then(({ data, summary }) => {
    console.log('Processed data:', data);
    console.log('Summary:', summary);
});
```

### Example 2: Complex State Management

```javascript
class StateManager {
    constructor(initialState = {}) {
        this.state = initialState;
        this.listeners = [];
    }

    setState(updates) {
        const {
            user = this.state.user,
            ui = this.state.ui,
            data = this.state.data
        } = updates;

        const prevState = { ...this.state };
        this.state = {
            user: { ...this.state.user, ...user },
            ui: { ...this.state.ui, ...ui },
            data: { ...this.state.data, ...data }
        };

        this.notify(prevState, this.state);
    }

    select(...paths) {
        return paths.reduce((result, path) => {
            const keys = path.split('.');
            const value = keys.reduce((obj, key) => obj?.[key], this.state);
            result[path] = value;
            return result;
        }, {});
    }

    subscribe(listener) {
        this.listeners.push(listener);
        return () => {
            this.listeners = this.listeners.filter(l => l !== listener);
        };
    }

    notify(prevState, nextState) {
        this.listeners.forEach(listener => {
            listener(prevState, nextState);
        });
    }
}

// Usage
const store = new StateManager({
    user: { id: 1, name: 'John', profile: { avatar: 'url' } },
    ui: { theme: 'dark', sidebar: false },
    data: { items: [], loading: false }
});

// Subscribe to changes
store.subscribe((prev, next) => {
    const {
        user: { name: prevName },
        ui: { theme: prevTheme }
    } = prev;

    const {
        user: { name: nextName },
        ui: { theme: nextTheme }
    } = next;

    if (prevName !== nextName) {
        console.log(`User name changed: ${prevName} -> ${nextName}`);
    }

    if (prevTheme !== nextTheme) {
        console.log(`Theme changed: ${prevTheme} -> ${nextTheme}`);
    }
});

// Update state
store.setState({
    user: { name: 'Jane' },
    ui: { theme: 'light' }
});

// Select specific values
const { 'user.name': userName, 'ui.theme': theme } = store.select('user.name', 'ui.theme');
console.log(userName, theme);
```

### Example 3: Advanced Form Handler

```javascript
class FormHandler {
    constructor(form) {
        this.form = form;
        this.validators = new Map();
        this.errors = new Map();
    }

    addValidator(field, validator) {
        if (!this.validators.has(field)) {
            this.validators.set(field, []);
        }
        this.validators.get(field).push(validator);
    }

    async validate(data) {
        this.errors.clear();

        for (const [field, validators] of this.validators) {
            for (const validator of validators) {
                const { isValid, message } = await validator(data[field], data);

                if (!isValid) {
                    if (!this.errors.has(field)) {
                        this.errors.set(field, []);
                    }
                    this.errors.get(field).push(message);
                }
            }
        }

        return this.errors.size === 0;
    }

    async submit(formData) {
        const {
            username,
            email,
            password,
            profile: { firstName, lastName, age } = {},
            preferences: { newsletter = false, notifications = true } = {}
        } = formData;

        const isValid = await this.validate(formData);

        if (!isValid) {
            return {
                success: false,
                errors: Object.fromEntries(this.errors)
            };
        }

        // Process form
        const processed = {
            credentials: { username, email, password },
            profile: { firstName, lastName, age },
            preferences: { newsletter, notifications }
        };

        return {
            success: true,
            data: processed
        };
    }

    getErrors() {
        return Object.fromEntries(this.errors);
    }
}

// Usage
const formHandler = new FormHandler();

// Add validators
formHandler.addValidator('email', (value) => ({
    isValid: /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
    message: 'Invalid email format'
}));

formHandler.addValidator('password', (value) => ({
    isValid: value && value.length >= 8,
    message: 'Password must be at least 8 characters'
}));

formHandler.addValidator('age', (value) => ({
    isValid: value >= 18,
    message: 'Must be at least 18 years old'
}));

// Submit form
formHandler.submit({
    username: 'johndoe',
    email: 'john@example.com',
    password: 'securepass123',
    profile: {
        firstName: 'John',
        lastName: 'Doe',
        age: 25
    },
    preferences: {
        newsletter: true
    }
}).then(result => {
    if (result.success) {
        console.log('Form submitted:', result.data);
    } else {
        console.error('Validation errors:', result.errors);
    }
});
```

### Example 4: GraphQL Query Builder

```javascript
class GraphQLQueryBuilder {
    constructor() {
        this.selections = [];
        this.variables = {};
    }

    select(fields) {
        if (typeof fields === 'string') {
            this.selections.push(fields);
        } else if (typeof fields === 'object') {
            const formatted = this.formatObject(fields);
            this.selections.push(formatted);
        }
        return this;
    }

    formatObject(obj, indent = 0) {
        const spaces = '  '.repeat(indent);
        const entries = Object.entries(obj);

        const formatted = entries.map(([key, value]) => {
            if (typeof value === 'object' && !Array.isArray(value)) {
                return `${spaces}${key} {\n${this.formatObject(value, indent + 1)}\n${spaces}}`;
            } else if (Array.isArray(value)) {
                return `${spaces}${key}`;
            }
            return `${spaces}${key}`;
        }).join('\n');

        return formatted;
    }

    build(queryName, args = {}) {
        const argString = Object.entries(args)
            .map(([key, value]) => `${key}: $${key}`)
            .join(', ');

        const variableString = Object.entries(args)
            .map(([key, value]) => `$${key}: ${typeof value === 'number' ? 'Int' : 'String'}`)
            .join(', ');

        return `
query ${queryName}${variableString ? `(${variableString})` : ''} {
  ${queryName}${argString ? `(${argString})` : ''} {
${this.selections.join('\n')}
  }
}
        `.trim();
    }
}

// Usage
const query = new GraphQLQueryBuilder();

query.select({
    user: {
        id: true,
        name: true,
        profile: {
            avatar: true,
            bio: true
        },
        posts: {
            title: true,
            content: true,
            comments: {
                text: true,
                author: {
                    name: true
                }
            }
        }
    }
});

const gql = query.build('getUser', { userId: 123 });
console.log(gql);
```

### Example 5: Event Emitter with Destructuring

```javascript
class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    on(event, handler) {
        if (!this.events.has(event)) {
            this.events.set(event, []);
        }

        this.events.get(event).push(handler);

        return () => this.off(event, handler);
    }

    off(event, handler) {
        if (!this.events.has(event)) return;

        const handlers = this.events.get(event);
        const index = handlers.indexOf(handler);

        if (index > -1) {
            handlers.splice(index, 1);
        }
    }

    emit(event, data) {
        if (!this.events.has(event)) return;

        const handlers = this.events.get(event);

        handlers.forEach(handler => {
            try {
                handler(data);
            } catch (error) {
                console.error(`Error in ${event} handler:`, error);
            }
        });
    }

    once(event, handler) {
        const wrapper = (data) => {
            handler(data);
            this.off(event, wrapper);
        };

        this.on(event, wrapper);
    }
}

// Usage
const emitter = new EventEmitter();

// Subscribe to user events
emitter.on('user:login', ({ user: { id, name }, timestamp }) => {
    console.log(`User ${name} (${id}) logged in at ${timestamp}`);
});

emitter.on('user:update', ({ user: { id, changes }, metadata: { updatedBy } }) => {
    console.log(`User ${id} updated by ${updatedBy}:`);
    Object.entries(changes).forEach(([key, { from, to }]) => {
        console.log(`  ${key}: ${from} -> ${to}`);
    });
});

// Emit events
emitter.emit('user:login', {
    user: { id: 1, name: 'John' },
    timestamp: new Date().toISOString()
});

emitter.emit('user:update', {
    user: {
        id: 1,
        changes: {
            email: { from: 'old@example.com', to: 'new@example.com' },
            name: { from: 'John', to: 'John Doe' }
        }
    },
    metadata: {
        updatedBy: 'admin',
        timestamp: Date.now()
    }
});
```

### Example 6: Advanced Middleware System

```javascript
class MiddlewareSystem {
    constructor() {
        this.middlewares = [];
    }

    use(middleware) {
        this.middlewares.push(middleware);
        return this;
    }

    async execute(context) {
        const {
            request: initialRequest,
            metadata: initialMetadata = {}
        } = context;

        let currentContext = {
            request: initialRequest,
            response: null,
            metadata: initialMetadata
        };

        for (const middleware of this.middlewares) {
            try {
                const result = await middleware(currentContext);

                if (result) {
                    const {
                        request = currentContext.request,
                        response = currentContext.response,
                        metadata = currentContext.metadata,
                        stopPipeline = false
                    } = result;

                    currentContext = { request, response, metadata };

                    if (stopPipeline) {
                        break;
                    }
                }
            } catch (error) {
                currentContext.metadata.error = error;
                break;
            }
        }

        return currentContext;
    }
}

// Middleware examples
const authMiddleware = async ({ request, metadata }) => {
    const { headers: { authorization } = {} } = request;

    if (!authorization) {
        return {
            response: { status: 401, body: 'Unauthorized' },
            stopPipeline: true
        };
    }

    const [, token] = authorization.split(' ');

    return {
        metadata: {
            ...metadata,
            user: { id: 1, name: 'John' },
            authenticated: true
        }
    };
};

const loggingMiddleware = async ({ request, metadata }) => {
    const {
        method,
        path,
        headers: { 'user-agent': userAgent } = {}
    } = request;

    console.log(`[${new Date().toISOString()}] ${method} ${path}`);
    console.log(`User-Agent: ${userAgent}`);

    if (metadata.user) {
        const { user: { id, name } } = metadata;
        console.log(`User: ${name} (${id})`);
    }

    return {
        metadata: {
            ...metadata,
            logged: true
        }
    };
};

const validationMiddleware = async ({ request, metadata }) => {
    const { body: { email, password } = {} } = request;

    const errors = [];

    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        errors.push('Invalid email');
    }

    if (!password || password.length < 8) {
        errors.push('Password must be at least 8 characters');
    }

    if (errors.length > 0) {
        return {
            response: { status: 400, body: { errors } },
            stopPipeline: true
        };
    }

    return {
        metadata: {
            ...metadata,
            validated: true
        }
    };
};

// Usage
const system = new MiddlewareSystem();

system
    .use(authMiddleware)
    .use(loggingMiddleware)
    .use(validationMiddleware);

system.execute({
    request: {
        method: 'POST',
        path: '/api/login',
        headers: {
            'authorization': 'Bearer token123',
            'user-agent': 'Mozilla/5.0'
        },
        body: {
            email: 'john@example.com',
            password: 'securepass123'
        }
    }
}).then(({ response, metadata }) => {
    console.log('Response:', response);
    console.log('Metadata:', metadata);
});
```

### Example 7: Advanced Router System

```javascript
class Router {
    constructor() {
        this.routes = new Map();
    }

    addRoute(pattern, handler) {
        const regex = this.patternToRegex(pattern);
        this.routes.set(pattern, { regex, handler, pattern });
    }

    patternToRegex(pattern) {
        const escaped = pattern.replace(/\//g, '\\/');
        const withParams = escaped.replace(/:(\w+)/g, '(?<$1>[^/]+)');
        return new RegExp(`^${withParams}$`);
    }

    async route(path, context = {}) {
        for (const [, { regex, handler, pattern }] of this.routes) {
            const match = path.match(regex);

            if (match) {
                const { groups: params = {} } = match;

                const {
                    query = {},
                    headers = {},
                    body = {},
                    metadata = {}
                } = context;

                const routeContext = {
                    params,
                    query,
                    headers,
                    body,
                    metadata,
                    path: pattern
                };

                return await handler(routeContext);
            }
        }

        return { status: 404, body: 'Not found' };
    }
}

// Usage
const router = new Router();

router.addRoute('/users/:id', async ({ params: { id }, query: { include = '' } }) => {
    const includes = include.split(',').filter(Boolean);

    return {
        status: 200,
        body: {
            id,
            name: 'John Doe',
            ...(includes.includes('profile') && {
                profile: { avatar: 'url', bio: 'Developer' }
            }),
            ...(includes.includes('posts') && {
                posts: [{ id: 1, title: 'Post 1' }]
            })
        }
    };
});

router.addRoute('/posts/:postId/comments/:commentId', async ({
    params: { postId, commentId },
    metadata: { user }
}) => {
    return {
        status: 200,
        body: {
            postId,
            commentId,
            requestedBy: user?.name || 'Anonymous'
        }
    };
});

// Route requests
router.route('/users/123', {
    query: { include: 'profile,posts' }
}).then(response => {
    console.log('User response:', response);
});

router.route('/posts/456/comments/789', {
    metadata: { user: { name: 'John' } }
}).then(response => {
    console.log('Comment response:', response);
});
```

## 5.11. Real-World Use Cases

### Use Case 1: Shopping Cart Manager

```javascript
class ShoppingCart {
    constructor() {
        this.items = [];
        this.discounts = [];
    }

    addItem({ product: { id, name, price }, quantity = 1, options = {} }) {
        const {
            color = 'default',
            size = 'M',
            customization = null
        } = options;

        const existing = this.items.find(item => {
            const {
                product: { id: itemId },
                options: { color: itemColor, size: itemSize }
            } = item;

            return itemId === id && itemColor === color && itemSize === size;
        });

        if (existing) {
            existing.quantity += quantity;
        } else {
            this.items.push({
                product: { id, name, price },
                quantity,
                options: { color, size, customization }
            });
        }
    }

    removeItem(itemId, { color, size } = {}) {
        this.items = this.items.filter(item => {
            const {
                product: { id },
                options: { color: itemColor, size: itemSize }
            } = item;

            return !(id === itemId &&
                (!color || itemColor === color) &&
                (!size || itemSize === size));
        });
    }

    applyDiscount({ code, type, value, conditions = {} }) {
        const {
            minAmount = 0,
            applicableProducts = null,
            expiresAt = null
        } = conditions;

        this.discounts.push({
            code,
            type,
            value,
            conditions: { minAmount, applicableProducts, expiresAt }
        });
    }

    calculate() {
        let subtotal = 0;
        let totalDiscount = 0;

        // Calculate subtotal
        this.items.forEach(({ product: { price }, quantity }) => {
            subtotal += price * quantity;
        });

        // Apply discounts
        this.discounts.forEach(discount => {
            const {
                type,
                value,
                conditions: { minAmount, applicableProducts, expiresAt }
            } = discount;

            // Check conditions
            if (subtotal < minAmount) return;
            if (expiresAt && new Date(expiresAt) < new Date()) return;

            let discountAmount = 0;

            if (type === 'percentage') {
                discountAmount = (subtotal * value) / 100;
            } else if (type === 'fixed') {
                discountAmount = value;
            }

            totalDiscount += Math.min(discountAmount, subtotal - totalDiscount);
        });

        const total = subtotal - totalDiscount;
        const tax = total * 0.1; // 10% tax

        return {
            subtotal,
            discount: totalDiscount,
            tax,
            total: total + tax,
            items: this.items.map(({ product: { name }, quantity, options }) => ({
                name,
                quantity,
                options
            }))
        };
    }
}

// Usage
const cart = new ShoppingCart();

cart.addItem({
    product: { id: 1, name: 'T-Shirt', price: 29.99 },
    quantity: 2,
    options: { color: 'blue', size: 'L' }
});

cart.addItem({
    product: { id: 2, name: 'Jeans', price: 59.99 },
    quantity: 1,
    options: { color: 'black', size: '32' }
});

cart.applyDiscount({
    code: 'SAVE10',
    type: 'percentage',
    value: 10,
    conditions: { minAmount: 50 }
});

const {
    subtotal,
    discount,
    tax,
    total,
    items
} = cart.calculate();

console.log(`Subtotal: $${subtotal.toFixed(2)}`);
console.log(`Discount: -$${discount.toFixed(2)}`);
console.log(`Tax: $${tax.toFixed(2)}`);
console.log(`Total: $${total.toFixed(2)}`);
console.log('Items:', items);
```

### Use Case 2: API Client with Request Builder

```javascript
class APIClient {
    constructor(baseURL, defaultHeaders = {}) {
        this.baseURL = baseURL;
        this.defaultHeaders = defaultHeaders;
        this.interceptors = {
            request: [],
            response: []
        };
    }

    addRequestInterceptor(interceptor) {
        this.interceptors.request.push(interceptor);
    }

    addResponseInterceptor(interceptor) {
        this.interceptors.response.push(interceptor);
    }

    async request({
        method = 'GET',
        path,
        params = {},
        headers = {},
        body = null,
        timeout = 5000,
        retries = 0
    }) {
        let config = {
            method,
            url: `${this.baseURL}${path}`,
            headers: { ...this.defaultHeaders, ...headers },
            body,
            params,
            timeout,
            retries
        };

        // Apply request interceptors
        for (const interceptor of this.interceptors.request) {
            const result = await interceptor(config);
            if (result) {
                const {
                    url = config.url,
                    headers: newHeaders = config.headers,
                    body: newBody = config.body
                } = result;

                config = { ...config, url, headers: newHeaders, body: newBody };
            }
        }

        // Build query string
        const queryString = Object.entries(config.params)
            .map(([key, value]) => `${key}=${encodeURIComponent(value)}`)
            .join('&');

        const fullURL = queryString ? `${config.url}?${queryString}` : config.url;

        // Make request with retries
        let attempt = 0;
        let lastError;

        while (attempt <= config.retries) {
            try {
                const response = await this.makeRequest(fullURL, config);

                // Apply response interceptors
                let finalResponse = response;

                for (const interceptor of this.interceptors.response) {
                    const result = await interceptor(finalResponse);
                    if (result) {
                        finalResponse = result;
                    }
                }

                return finalResponse;
            } catch (error) {
                lastError = error;
                attempt++;

                if (attempt <= config.retries) {
                    await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
                }
            }
        }

        throw lastError;
    }

    async makeRequest(url, { method, headers, body, timeout }) {
        // Simulated fetch
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve({
                    status: 200,
                    data: { success: true },
                    headers: {}
                });
            }, 100);
        });
    }

    async get(path, options = {}) {
        return this.request({ ...options, method: 'GET', path });
    }

    async post(path, body, options = {}) {
        return this.request({ ...options, method: 'POST', path, body });
    }

    async put(path, body, options = {}) {
        return this.request({ ...options, method: 'PUT', path, body });
    }

    async delete(path, options = {}) {
        return this.request({ ...options, method: 'DELETE', path });
    }
}

// Usage
const api = new APIClient('https://api.example.com', {
    'Content-Type': 'application/json'
});

// Add auth interceptor
api.addRequestInterceptor(async (config) => {
    const token = 'Bearer token123';

    return {
        headers: {
            ...config.headers,
            'Authorization': token
        }
    };
});

// Add logging interceptor
api.addResponseInterceptor(async (response) => {
    const { status, data } = response;
    console.log(`Response ${status}:`, data);
    return response;
});

// Make requests
api.get('/users', {
    params: { page: 1, limit: 10 }
}).then(({ data }) => {
    console.log('Users:', data);
});

api.post('/users', {
    name: 'John Doe',
    email: 'john@example.com'
}).then(({ data }) => {
    console.log('Created:', data);
});
```

### Use Case 3: Form Validator

```javascript
class FormValidator {
    constructor() {
        this.rules = new Map();
        this.messages = new Map();
    }

    addRule(field, rule) {
        if (!this.rules.has(field)) {
            this.rules.set(field, []);
        }
        this.rules.get(field).push(rule);
    }

    async validate(data) {
        const errors = new Map();

        for (const [field, rules] of this.rules) {
            for (const rule of rules) {
                const { type, params = {}, message } = rule;

                const isValid = await this.validateField(
                    data[field],
                    type,
                    params,
                    data
                );

                if (!isValid) {
                    if (!errors.has(field)) {
                        errors.set(field, []);
                    }
                    errors.get(field).push(message || `${field} is invalid`);
                }
            }
        }

        return {
            isValid: errors.size === 0,
            errors: Object.fromEntries(errors)
        };
    }

    async validateField(value, type, params, allData) {
        switch (type) {
            case 'required':
                return value !== null && value !== undefined && value !== '';

            case 'email':
                return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);

            case 'min':
                const { length: minLength } = params;
                return String(value).length >= minLength;

            case 'max':
                const { length: maxLength } = params;
                return String(value).length <= maxLength;

            case 'match':
                const { field: matchField } = params;
                return value === allData[matchField];

            case 'custom':
                const { validator } = params;
                return await validator(value, allData);

            default:
                return true;
        }
    }
}

// Usage
const validator = new FormValidator();

validator.addRule('username', {
    type: 'required',
    message: 'Username is required'
});

validator.addRule('username', {
    type: 'min',
    params: { length: 3 },
    message: 'Username must be at least 3 characters'
});

validator.addRule('email', {
    type: 'required',
    message: 'Email is required'
});

validator.addRule('email', {
    type: 'email',
    message: 'Invalid email format'
});

validator.addRule('password', {
    type: 'min',
    params: { length: 8 },
    message: 'Password must be at least 8 characters'
});

validator.addRule('confirmPassword', {
    type: 'match',
    params: { field: 'password' },
    message: 'Passwords do not match'
});

validator.addRule('age', {
    type: 'custom',
    params: {
        validator: (value) => value >= 18
    },
    message: 'Must be at least 18 years old'
});

// Validate form data
validator.validate({
    username: 'johndoe',
    email: 'john@example.com',
    password: 'securepass123',
    confirmPassword: 'securepass123',
    age: 25
}).then(({ isValid, errors }) => {
    if (isValid) {
        console.log('Form is valid!');
    } else {
        console.error('Validation errors:', errors);
    }
});
```

### Use Case 4: Database Query Builder

```javascript
class QueryBuilder {
    constructor(table) {
        this.table = table;
        this.query = {
            select: ['*'],
            where: [],
            orderBy: [],
            limit: null,
            offset: null,
            joins: []
        };
    }

    select(...fields) {
        this.query.select = fields;
        return this;
    }

    where(conditions) {
        const {
            field,
            operator = '=',
            value,
            logic = 'AND'
        } = conditions;

        this.query.where.push({ field, operator, value, logic });
        return this;
    }

    orWhere(conditions) {
        return this.where({ ...conditions, logic: 'OR' });
    }

    orderBy(field, direction = 'ASC') {
        this.query.orderBy.push({ field, direction });
        return this;
    }

    limit(count) {
        this.query.limit = count;
        return this;
    }

    offset(count) {
        this.query.offset = count;
        return this;
    }

    join(table, conditions) {
        const {
            type = 'INNER',
            on: { leftField, rightField }
        } = conditions;

        this.query.joins.push({
            type,
            table,
            leftField,
            rightField
        });

        return this;
    }

    build() {
        const {
            select,
            where,
            orderBy,
            limit,
            offset,
            joins
        } = this.query;

        let sql = `SELECT ${select.join(', ')} FROM ${this.table}`;

        // Joins
        if (joins.length > 0) {
            const joinClauses = joins.map(({ type, table, leftField, rightField }) =>
                `${type} JOIN ${table} ON ${leftField} = ${rightField}`
            );
            sql += ' ' + joinClauses.join(' ');
        }

        // Where clauses
        if (where.length > 0) {
            const whereClauses = where.map(({ field, operator, value, logic }, index) => {
                const clause = `${field} ${operator} ?`;
                return index === 0 ? clause : `${logic} ${clause}`;
            });
            sql += ' WHERE ' + whereClauses.join(' ');
        }

        // Order by
        if (orderBy.length > 0) {
            const orderClauses = orderBy.map(({ field, direction }) =>
                `${field} ${direction}`
            );
            sql += ' ORDER BY ' + orderClauses.join(', ');
        }

        // Limit & Offset
        if (limit !== null) {
            sql += ` LIMIT ${limit}`;
        }

        if (offset !== null) {
            sql += ` OFFSET ${offset}`;
        }

        const params = where.map(({ value }) => value);

        return { sql, params };
    }
}

// Usage
const query = new QueryBuilder('users');

const { sql, params } = query
    .select('users.id', 'users.name', 'posts.title')
    .join('posts', {
        type: 'LEFT',
        on: {
            leftField: 'users.id',
            rightField: 'posts.user_id'
        }
    })
    .where({ field: 'users.age', operator: '>=', value: 18 })
    .where({ field: 'users.status', operator: '=', value: 'active' })
    .orWhere({ field: 'users.role', operator: '=', value: 'admin' })
    .orderBy('users.created_at', 'DESC')
    .limit(10)
    .offset(0)
    .build();

console.log(sql);
console.log('Params:', params);
```

### Use Case 5: Configuration Manager

```javascript
class ConfigManager {
    constructor(defaults = {}) {
        this.config = { ...defaults };
        this.environments = new Map();
    }

    set(path, value) {
        const keys = path.split('.');
        let current = this.config;

        for (let i = 0; i < keys.length - 1; i++) {
            const key = keys[i];
            if (!current[key] || typeof current[key] !== 'object') {
                current[key] = {};
            }
            current = current[key];
        }

        current[keys[keys.length - 1]] = value;
    }

    get(path, defaultValue = null) {
        const keys = path.split('.');
        let current = this.config;

        for (const key of keys) {
            if (current[key] === undefined) {
                return defaultValue;
            }
            current = current[key];
        }

        return current;
    }

    merge(newConfig) {
        this.config = this.deepMerge(this.config, newConfig);
    }

    deepMerge(target, source) {
        const result = { ...target };

        for (const [key, value] of Object.entries(source)) {
            if (value && typeof value === 'object' && !Array.isArray(value)) {
                result[key] = this.deepMerge(result[key] || {}, value);
            } else {
                result[key] = value;
            }
        }

        return result;
    }

    loadEnvironment(env, config) {
        this.environments.set(env, config);
    }

    switchEnvironment(env) {
        const envConfig = this.environments.get(env);

        if (envConfig) {
            this.merge(envConfig);
        }
    }

    extract(...paths) {
        return paths.reduce((result, path) => {
            result[path] = this.get(path);
            return result;
        }, {});
    }
}

// Usage
const config = new ConfigManager({
    app: {
        name: 'MyApp',
        version: '1.0.0',
        port: 3000
    },
    database: {
        host: 'localhost',
        port: 5432,
        name: 'myapp_db'
    },
    api: {
        url: 'https://api.example.com',
        timeout: 5000,
        retries: 3
    }
});

// Load environment-specific configs
config.loadEnvironment('production', {
    app: { port: 8080 },
    database: { host: 'prod-db.example.com' },
    api: { url: 'https://api.production.com' }
});

config.loadEnvironment('development', {
    app: { port: 3000 },
    database: { host: 'localhost' },
    api: { url: 'http://localhost:4000' }
});

// Switch environment
config.switchEnvironment('production');

// Extract specific values
const {
    'app.port': port,
    'database.host': dbHost,
    'api.url': apiUrl
} = config.extract('app.port', 'database.host', 'api.url');

console.log(`Port: ${port}`);
console.log(`DB Host: ${dbHost}`);
console.log(`API URL: ${apiUrl}`);
```

## 5.12. Tips & Tricks

### Tip 1: Nested Destructuring with Defaults

```javascript
const config = {
    server: {
        // host is missing
        port: 3000
    }
};

// Deep default values
const {
    server: {
        host = 'localhost',
        port = 8080
    } = {}
} = config;

console.log(host);  // "localhost" (default)
console.log(port);  // 3000 (from config)
```

### Tip 2: Destructuring with Computed Property Names

```javascript
const key = 'username';
const data = { username: 'johndoe', email: 'john@example.com' };

// Use computed property names
const { [key]: value } = data;
console.log(value);  // "johndoe"

// Multiple computed properties
const keys = ['username', 'email'];
const values = keys.map(k => ({ [k]: data[k] }));
console.log(values);  // [{ username: 'johndoe' }, { email: 'john@example.com' }]
```

### Tip 3: Destructuring Function Return Values

```javascript
// Return multiple values as object
function getUser() {
    return {
        id: 1,
        name: 'John',
        email: 'john@example.com',
        metadata: { created: Date.now() }
    };
}

// Destructure only what you need
const { id, name } = getUser();

// Or destructure nested values
const { metadata: { created } } = getUser();
```

### Tip 4: Destructuring in Array Methods

```javascript
const users = [
    { id: 1, name: 'John', age: 30, active: true },
    { id: 2, name: 'Jane', age: 25, active: false },
    { id: 3, name: 'Bob', age: 35, active: true }
];

// Map with destructuring
const names = users.map(({ name }) => name);

// Filter with destructuring
const activeUsers = users.filter(({ active }) => active);

// Reduce with destructuring
const totalAge = users.reduce((sum, { age }) => sum + age, 0);

// Find with destructuring
const { name: foundName } = users.find(({ id }) => id === 2) || {};
```

### Tip 5: Destructuring with Rest to Exclude Properties

```javascript
const user = {
    id: 1,
    password: 'secret',
    name: 'John',
    email: 'john@example.com'
};

// Remove password from user object
const { password, ...userWithoutPassword } = user;

console.log(userWithoutPassword);
// { id: 1, name: 'John', email: 'john@example.com' }
```

### Tip 6: Destructuring with Aliasing in Loops

```javascript
const products = [
    { product: { id: 1, name: 'Laptop', price: 999 } },
    { product: { id: 2, name: 'Mouse', price: 29 } }
];

// Destructure and alias in loop
for (const { product: { name, price } } of products) {
    console.log(`${name}: $${price}`);
}
```

### Tip 7: Destructuring with Optional Chaining

```javascript
const data = {
    user: {
        // profile is undefined
    }
};

// Safe destructuring with optional chaining
const { user: { profile: { avatar } = {} } = {} } = data;
console.log(avatar);  // undefined (no error)

// Or use optional chaining directly
const avatar = data?.user?.profile?.avatar;
```

### Tip 8: Destructuring in Promise Chains

```javascript
fetch('/api/user')
    .then(response => response.json())
    .then(({ data: { user: { id, name } } }) => {
        console.log(`User ${id}: ${name}`);
    });

// With async/await
async function getUser() {
    const response = await fetch('/api/user');
    const { data: { user: { id, name } } } = await response.json();
    return { id, name };
}
```

### Tip 9: Destructuring with Type Coercion

```javascript
const data = { count: '42', active: 'true' };

// Destructure and coerce types
const {
    count = 0,
    active = false
} = data;

// Convert to proper types
const numCount = Number(count);
const boolActive = active === 'true';

// Or destructure and convert in one step
function parseData({ count, active }) {
    return {
        count: Number(count),
        active: active === 'true'
    };
}
```

### Tip 10: Destructuring with Array Spread

```javascript
const numbers = [1, 2, 3, 4, 5];

// Get first, last, and rest
const [first, ...middle] = numbers;
const last = middle.pop();

console.log(first);   // 1
console.log(last);    // 5
console.log(middle);  // [2, 3, 4]

// Alternative: destructure with length
const [f, , , , l] = numbers;
console.log(f, l);  // 1 5
```

## 5.13. Common Mistakes

### Mistake 1: Forgetting Parentheses When Assigning to Existing Variables

```javascript
let name, age;

// ERROR: This is interpreted as a block
{ name, age } = { name: 'John', age: 30 };  // ❌ SyntaxError

// CORRECT: Wrap in parentheses
({ name, age } = { name: 'John', age: 30 });  // ✅
```

### Mistake 2: Destructuring undefined or null

```javascript
const data = null;

// ERROR: Cannot destructure null
const { name } = data;  // ❌ TypeError

// CORRECT: Provide fallback
const { name } = data || {};  // ✅
const { name } = data ?? {};  // ✅ (nullish coalescing)
```

### Mistake 3: Overwriting Variables in Scope

```javascript
const name = 'Jane';

// ERROR: 'name' is already declared
const { name } = { name: 'John' };  // ❌ SyntaxError

// CORRECT: Rename the destructured variable
const { name: userName } = { name: 'John' };  // ✅
console.log(name);      // "Jane"
console.log(userName);  // "John"
```

### Mistake 4: Deep Nesting Without Safety Checks

```javascript
const data = {
    user: {
        // profile is undefined
    }
};

// ERROR: Cannot destructure undefined
const {
    user: {
        profile: { avatar }
    }
} = data;  // ❌ TypeError

// CORRECT: Provide defaults
const {
    user: {
        profile: { avatar } = {}
    } = {}
} = data;  // ✅

// OR: Use optional chaining
const avatar = data?.user?.profile?.avatar;  // ✅
```

### Mistake 5: Expecting Destructured Parameters to be Required

```javascript
// Expects object parameter
function greet({ name, age }) {
    console.log(`${name} is ${age}`);
}

greet();  // ❌ TypeError: Cannot destructure undefined

// CORRECT: Provide default parameter
function greet({ name, age } = {}) {
    console.log(`${name || 'Guest'} is ${age || 'unknown'}`);
}

greet();  // ✅ "Guest is unknown"
```

### Mistake 6: Confusing Rest with Spread

```javascript
const arr = [1, 2, 3];

// Rest: Collect remaining elements (only in destructuring)
const [first, ...rest] = arr;
console.log(rest);  // [2, 3] ✅

// Can't use rest in the middle
const [first, ...middle, last] = arr;  // ❌ SyntaxError

// CORRECT: Rest must be last
const [first, second, ...rest] = arr;  // ✅
```

### Mistake 7: Destructuring Arrays as Objects

```javascript
const arr = [1, 2, 3];

// ERROR: Trying to destructure array as object
const { 0: first } = arr;  // ❌ Works but weird

// CORRECT: Use array destructuring
const [first] = arr;  // ✅

// However, this DOES work (arrays are objects)
const { length } = arr;
console.log(length);  // 3
```

### Mistake 8: Not Understanding Default Values

```javascript
const { name, age = 25 } = { name: 'John', age: undefined };

console.log(age);  // 25 (default used because value is undefined)

// But null doesn't trigger default
const { name, age = 25 } = { name: 'John', age: null };
console.log(age);  // null ❌ (not 25!)

// CORRECT: Use nullish coalescing
const { name, age: userAge } = { name: 'John', age: null };
const age = userAge ?? 25;  // ✅ 25
```

## 5.14. Troubleshooting

### Issue 1: Cannot Destructure Property of Undefined

```javascript
// Problem
const data = undefined;
const { user } = data;  // TypeError

// Solution 1: Default to empty object
const { user } = data || {};

// Solution 2: Optional chaining
const user = data?.user;

// Solution 3: Try-catch
let user;
try {
    ({ user } = data);
} catch {
    user = null;
}
```

### Issue 2: Lost Reference to Original Object

```javascript
const user = {
    name: 'John',
    address: { city: 'NYC' }
};

// This only extracts city, loses reference to address
const {
    address: { city }
} = user;

console.log(city);     // "NYC"
console.log(address);  // ReferenceError

// Solution: Extract both if needed
const {
    address,
    address: { city: userCity }
} = user;

console.log(address);  // { city: 'NYC' }
console.log(userCity); // "NYC"
```

### Issue 3: Destructuring in Async Functions

```javascript
// Problem: Can't await destructured value
const { data } = await fetch('/api/user').json();  // ❌ SyntaxError

// Solution: Two steps
const response = await fetch('/api/user');
const { data } = await response.json();  // ✅

// Or chain properly
const { data } = await (await fetch('/api/user')).json();  // ✅ (but ugly)
```

### Issue 4: Destructuring with Dynamic Keys

```javascript
// Problem: Want to destructure dynamic key
const key = 'username';
const data = { username: 'john', email: 'john@example.com' };

// Can't do this
const { key } = data;  // ❌ Looks for property 'key'

// Solution: Use computed property
const { [key]: value } = data;  // ✅
console.log(value);  // "john"
```

### Issue 5: Reassigning Destructured const

```javascript
const { name } = { name: 'John' };
name = 'Jane';  // ❌ TypeError: Assignment to constant

// Solution: Use let
let { name } = { name: 'John' };
name = 'Jane';  // ✅

// Or destructure to new variable
const { name } = { name: 'John' };
const newName = 'Jane';
```

### Issue 6: Destructuring with Template Literals

```javascript
const user = { name: 'John', age: 30 };

// Problem: Can't destructure inside template literal
console.log(`User: ${{ name, age }}`);  // ❌ Logs "[object Object]"

// Solution: Destructure first
const { name, age } = user;
console.log(`User: ${name}, ${age}`);  // ✅ "User: John, 30"

// Or access properties
console.log(`User: ${user.name}, ${user.age}`);  // ✅
```

## 5.15. Advanced Topics

### Advanced Topic 1: Destructuring with Proxies

```javascript
const handler = {
    get(target, prop) {
        if (prop in target) {
            return target[prop];
        }
        return `Property '${prop}' not found`;
    }
};

const user = new Proxy({
    name: 'John',
    age: 30
}, handler);

// Destructure from proxy
const { name, email } = user;

console.log(name);   // "John"
console.log(email);  // "Property 'email' not found"
```

### Advanced Topic 2: Destructuring with Symbols

```javascript
const ID = Symbol('id');
const PRIVATE = Symbol('private');

const user = {
    [ID]: 123,
    name: 'John',
    [PRIVATE]: 'secret'
};

// Destructure symbol properties
const { [ID]: userId, name } = user;

console.log(userId);  // 123
console.log(name);    // "John"
```

### Advanced Topic 3: Destructuring with Getters

```javascript
const user = {
    firstName: 'John',
    lastName: 'Doe',
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    }
};

// Destructure getter (calls the getter)
const { fullName } = user;

console.log(fullName);  // "John Doe"
```

### Advanced Topic 4: Destructuring in Generators

```javascript
function* generateUsers() {
    yield { id: 1, name: 'John' };
    yield { id: 2, name: 'Jane' };
    yield { id: 3, name: 'Bob' };
}

// Destructure in for-of with generator
for (const { id, name } of generateUsers()) {
    console.log(`${id}: ${name}`);
}

// Destructure generator results
const [first, second] = generateUsers();
console.log(first);   // { id: 1, name: 'John' }
console.log(second);  // { id: 2, name: 'Jane' }
```

### Advanced Topic 5: Destructuring with Weak References

```javascript
class Cache {
    constructor() {
        this.cache = new WeakMap();
    }

    set(key, value) {
        this.cache.set(key, value);
    }

    get(key) {
        return this.cache.get(key);
    }

    destructure(key, properties) {
        const data = this.cache.get(key);

        if (!data) {
            return null;
        }

        // Destructure specific properties
        const result = {};
        properties.forEach(prop => {
            result[prop] = data[prop];
        });

        return result;
    }
}

// Usage
const cache = new Cache();
const userKey = { id: 1 };

cache.set(userKey, {
    name: 'John',
    email: 'john@example.com',
    age: 30
});

// Destructure from WeakMap
const userData = cache.destructure(userKey, ['name', 'email']);
console.log(userData);  // { name: 'John', email: 'john@example.com' }
```

## 5.16. Exercises (Extended)

### Exercise 1: Basic Object Destructuring

```javascript
// Extract name and age from user object
const user = { name: 'John', age: 30, city: 'NYC', country: 'USA' };

// Your code here
// Extract only name and age
```

### Exercise 2: Array Swapping

```javascript
// Swap x and y using array destructuring
let x = 10;
let y = 20;

// Your code here
// Result: x should be 20, y should be 10
```

### Exercise 3: Function Parameters

```javascript
// Create a function that takes an object parameter and returns a greeting
// Use destructuring with default values

function greetUser(/* your parameters */) {
    // name (required)
    // age (default: 25)
    // city (default: 'Unknown')

    // Return: "Hello, {name}! You are {age} years old and live in {city}."
}

// Test cases:
// greetUser({ name: 'John' })
// greetUser({ name: 'Jane', age: 30, city: 'NYC' })
```

### Exercise 4: Nested Destructuring

```javascript
// Extract city and country from nested object
const data = {
    user: {
        name: 'John',
        address: {
            city: 'NYC',
            country: 'USA',
            zip: '10001'
        }
    },
    metadata: {
        created: Date.now()
    }
};

// Extract: name, city, country using destructuring
// Your code here
```

### Exercise 5: Rest Operator

```javascript
// Extract first two elements and collect the rest
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Use destructuring to get:
// first = 1
// second = 2
// rest = [3, 4, 5, 6, 7, 8, 9, 10]
```

### Exercise 6: Object Rest

```javascript
// Remove password from user object using destructuring
const user = {
    id: 1,
    username: 'johndoe',
    email: 'john@example.com',
    password: 'secret123',
    role: 'admin'
};

// Create new object without password
// Your code here
```

### Exercise 7: Array Method Destructuring

```javascript
// Given an array of products, use destructuring in array methods
const products = [
    { id: 1, name: 'Laptop', price: 999, category: 'electronics' },
    { id: 2, name: 'Book', price: 15, category: 'books' },
    { id: 3, name: 'Mouse', price: 29, category: 'electronics' }
];

// 1. Use map to extract just names
// 2. Use filter to get products under $50, destructuring price
// 3. Use reduce to sum all prices, destructuring price
```

### Exercise 8: Renaming Properties

```javascript
// Destructure and rename properties
const apiResponse = {
    user_id: 123,
    user_name: 'John Doe',
    user_email: 'john@example.com'
};

// Rename to: id, name, email
// Your code here
```

### Exercise 9: Complex Nested Destructuring

```javascript
// Extract specific values from complex object
const response = {
    status: 200,
    data: {
        users: [
            {
                id: 1,
                profile: {
                    name: 'John',
                    contact: {
                        email: 'john@example.com',
                        phone: '555-1234'
                    }
                }
            }
        ]
    },
    metadata: {
        timestamp: Date.now(),
        version: '1.0'
    }
};

// Extract:
// - First user's name
// - First user's email
// - Response version
// Your code here
```

### Exercise 10: Function with Multiple Return Values

```javascript
// Create a function that returns multiple values using object
function analyzeArray(numbers) {
    // Calculate and return:
    // - min
    // - max
    // - average
    // - length

    // Your code here
}

// Destructure the result
const result = analyzeArray([1, 2, 3, 4, 5]);
// Extract all values using destructuring
```

### Exercise 11: Default Values Challenge

```javascript
// Create a function with complex default values
function createConfig(options) {
    // Default structure:
    // {
    //   server: {
    //     host: 'localhost',
    //     port: 3000,
    //     ssl: false
    //   },
    //   database: {
    //     host: 'localhost',
    //     port: 5432,
    //     name: 'myapp'
    //   }
    // }

    // Use destructuring with nested defaults
    // Your code here
}

// Test:
// createConfig({})
// createConfig({ server: { port: 8080 } })
// createConfig({ database: { name: 'production' } })
```

### Exercise 12: Advanced Challenge - Transform API Response

```javascript
// Transform this API response using destructuring
const apiData = {
    response: {
        status: 'success',
        data: {
            users: [
                {
                    userId: 1,
                    userName: 'john_doe',
                    userProfile: {
                        firstName: 'John',
                        lastName: 'Doe',
                        contacts: {
                            primaryEmail: 'john@example.com',
                            secondaryEmail: 'johndoe@example.com'
                        }
                    },
                    userSettings: {
                        theme: 'dark',
                        notifications: true
                    }
                }
            ]
        }
    }
};

// Transform to this structure for the first user:
// {
//   id: 1,
//   username: 'john_doe',
//   name: 'John Doe',
//   email: 'john@example.com',
//   settings: { theme: 'dark', notifications: true }
// }

// Use destructuring and minimal manual assignment
// Your code here
```

---

**Kết luận:** Destructuring là tính năng mạnh mẽ giúp code ngắn gọn và dễ đọc hơn. Nắm vững object destructuring, array destructuring, default values, và rest/spread operators sẽ giúp bạn viết JavaScript hiện đại hiệu quả hơn.

**Chương tiếp theo:** Spread & Rest Operators
