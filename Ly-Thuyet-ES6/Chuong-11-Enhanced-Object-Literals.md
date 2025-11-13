# CHƯƠNG 11: ENHANCED OBJECT LITERALS

## 11.1. Giới thiệu Enhanced Object Literals

ES6 cải thiện object literal syntax với các tính năng mới: property shorthand, method shorthand, computed property names, và hơn nữa.

## 11.2. Property Shorthand

### 11.2.1. Basic Shorthand

**ES5:**
```javascript
var name = 'John';
var age = 30;

var user = {
    name: name,
    age: age
};
```

**ES6:**
```javascript
const name = 'John';
const age = 30;

const user = {
    name,  // Same as name: name
    age    // Same as age: age
};
```

### 11.2.2. Practical Example

```javascript
function createUser(name, email, age) {
    return {
        name,
        email,
        age,
        created: new Date(),
        active: true
    };
}

const user = createUser('John', 'john@example.com', 30);
// { name: 'John', email: 'john@example.com', age: 30, created: ..., active: true }
```

## 11.3. Method Shorthand

### 11.3.1. Function Methods

**ES5:**
```javascript
var user = {
    name: 'John',
    greet: function() {
        console.log('Hello, ' + this.name);
    }
};
```

**ES6:**
```javascript
const user = {
    name: 'John',
    greet() {
        console.log(`Hello, ${this.name}`);
    }
};
```

### 11.3.2. Multiple Methods

```javascript
const calculator = {
    value: 0,

    add(n) {
        this.value += n;
        return this;
    },

    subtract(n) {
        this.value -= n;
        return this;
    },

    multiply(n) {
        this.value *= n;
        return this;
    },

    getValue() {
        return this.value;
    }
};

calculator.add(10).subtract(3).multiply(2).getValue();  // 14
```

## 11.4. Computed Property Names

### 11.4.1. Dynamic Keys

**ES5:**
```javascript
var key = 'name';
var user = {};
user[key] = 'John';
```

**ES6:**
```javascript
const key = 'name';
const user = {
    [key]: 'John'
};
```

### 11.4.2. Expressions in Keys

```javascript
const prefix = 'user';
const id = 123;

const obj = {
    [prefix + '_' + id]: 'John',
    [`${prefix}_${id}_email`]: 'john@example.com',
    [prefix + '_age']: 30
};

console.log(obj.user_123);        // "John"
console.log(obj.user_123_email);  // "john@example.com"
```

### 11.4.3. Function Calls in Keys

```javascript
function makeKey(prefix, id) {
    return `${prefix}_${id}`;
}

const data = {
    [makeKey('user', 1)]: 'John',
    [makeKey('user', 2)]: 'Jane'
};

console.log(data.user_1);  // "John"
console.log(data.user_2);  // "Jane"
```

### 11.4.4. Symbol Keys

```javascript
const sym1 = Symbol('id');
const sym2 = Symbol('type');

const obj = {
    [sym1]: 123,
    [sym2]: 'user',
    name: 'John'
};

console.log(obj[sym1]);  // 123
console.log(obj[sym2]);  // "user"
```

## 11.5. Combined Features

### 11.5.1. Shorthand + Methods

```javascript
const name = 'John';
const age = 30;

const user = {
    name,
    age,

    greet() {
        return `Hello, I'm ${this.name}`;
    },

    getInfo() {
        return `${this.name} is ${this.age} years old`;
    }
};
```

### 11.5.2. Shorthand + Computed Properties

```javascript
const field = 'email';
const value = 'john@example.com';

const user = {
    name: 'John',
    [field]: value,

    [`get${field.charAt(0).toUpperCase() + field.slice(1)}`]() {
        return this[field];
    }
};

console.log(user.email);      // "john@example.com"
console.log(user.getEmail()); // "john@example.com"
```

## 11.4. Use Cases Thực Tế với ES6

### 11.4.1. Use Case 1: React-like Component Factory

```javascript
// Tạo component factory với state management
function createComponent(name, initialState = {}, methods = {}) {
    let state = { ...initialState };
    const watchers = [];

    return {
        name,
        state,

        // Getter cho state
        getState() {
            return { ...state };
        },

        // Setter với notification
        setState(updates) {
            state = { ...state, ...updates };
            watchers.forEach(watcher => watcher(state));
            return this;
        },

        // Watch changes
        watch(callback) {
            watchers.push(callback);
            return () => watchers.splice(watchers.indexOf(callback), 1);
        },

        // Render method
        render() {
            return `<${this.name}>${JSON.stringify(this.state)}</${this.name}>`;
        },

        // Dynamic methods
        ...methods
    };
}

// Usage
const counter = createComponent(
    'Counter',
    { count: 0 },
    {
        increment() { this.setState({ count: this.state.count + 1 }); },
        decrement() { this.setState({ count: this.state.count - 1 }); }
    }
);
```

### 11.4.2. Use Case 2: Object Factory Pattern

```javascript
// Factory tạo objects với consistent structure
function createUserFactory(defaults = {}) {
    return (userData) => {
        const {
            id,
            name,
            email,
            role = 'user',
            active = true,
            ...extras
        } = { ...defaults, ...userData };

        return {
            id,
            name,
            email,
            role,
            active,
            ...extras,

            // Methods
            isAdmin() { return this.role === 'admin'; },
            isActive() { return this.active; },
            getProfile() {
                return `${this.name} (${this.email}) - Role: ${this.role}`;
            },
            deactivate() {
                return { ...this, active: false };
            }
        };
    };
}

const userFactory = createUserFactory({ active: true });
const user1 = userFactory({ id: 1, name: 'John', email: 'john@example.com' });
const user2 = userFactory({ id: 2, name: 'Jane', email: 'jane@example.com', role: 'admin' });
```

### 11.4.3. Use Case 3: API Response Mapper

```javascript
// Mapper chuyển đổi API response sang internal object
function createResponseMapper(fieldMap) {
    return (apiResponse) => {
        const mapped = {};

        Object.entries(fieldMap).forEach(([internalKey, apiKey]) => {
            if (typeof apiKey === 'function') {
                mapped[internalKey] = apiKey(apiResponse);
            } else {
                mapped[internalKey] = apiResponse[apiKey];
            }
        });

        return {
            ...mapped,
            get raw() { return apiResponse; },
            getDisplayName() {
                return `${this.firstName} ${this.lastName}`;
            }
        };
    };
}

const userMapper = createResponseMapper({
    id: 'user_id',
    firstName: 'first_name',
    lastName: 'last_name',
    email: 'email_address',
    joinDate: (api) => new Date(api.created_at)
});

const apiData = {
    user_id: 1,
    first_name: 'John',
    last_name: 'Doe',
    email_address: 'john@example.com',
    created_at: '2023-01-01'
};

const userObj = userMapper(apiData);
```

### 11.4.4. Use Case 4: Configuration Manager

```javascript
// Manager quản lý configurations với environments
function createConfigManager(environments) {
    return (env = 'development') => {
        const baseConfig = environments.default || {};
        const envConfig = environments[env] || {};
        const merged = { ...baseConfig, ...envConfig };

        return {
            ...merged,
            env,

            get(key, defaultValue = undefined) {
                return this[key] ?? defaultValue;
            },

            has(key) {
                return key in this;
            },

            getAll() {
                const { env, get, has, getAll, ...config } = this;
                return config;
            },

            validate(schema) {
                const errors = [];
                Object.entries(schema).forEach(([key, validator]) => {
                    if (!validator(this[key])) {
                        errors.push(`Invalid ${key}`);
                    }
                });
                return errors;
            }
        };
    };
}

const configManager = createConfigManager({
    default: {
        port: 3000,
        timeout: 5000,
        retries: 3
    },
    production: {
        port: 8080,
        timeout: 10000,
        debug: false,
        ssl: true
    },
    development: {
        port: 3000,
        debug: true,
        ssl: false
    }
});

const config = configManager('production');
```

### 11.4.5. Use Case 5: Builder Pattern

```javascript
// Builder tạo complex objects step by step
function createQueryBuilder() {
    const query = {
        select: [],
        from: '',
        where: [],
        join: [],
        orderBy: [],
        limit: null
    };

    return {
        select(...fields) {
            return {
                ...this,
                query: { ...query, select: fields }
            };
        },

        from(table) {
            return {
                ...this,
                query: { ...query, from: table }
            };
        },

        where(condition) {
            return {
                ...this,
                query: { ...query, where: [...query.where, condition] }
            };
        },

        join(table, condition) {
            return {
                ...this,
                query: { ...query, join: [...query.join, { table, condition }] }
            };
        },

        orderBy(field, direction = 'ASC') {
            return {
                ...this,
                query: { ...query, orderBy: [...query.orderBy, { field, direction }] }
            };
        },

        limit(n) {
            return {
                ...this,
                query: { ...query, limit: n }
            };
        },

        build() {
            return query;
        },

        toString() {
            let sql = `SELECT ${query.select.join(', ')} FROM ${query.from}`;
            if (query.join.length) sql += ` ${query.join.map(j => `JOIN ${j.table} ON ${j.condition}`).join(' ')}`;
            if (query.where.length) sql += ` WHERE ${query.where.join(' AND ')}`;
            if (query.orderBy.length) sql += ` ORDER BY ${query.orderBy.map(o => `${o.field} ${o.direction}`).join(', ')}`;
            if (query.limit) sql += ` LIMIT ${query.limit}`;
            return sql;
        }
    };
}
```

## 11.6. Practical Examples

### 11.6.1. API Response Mapping

```javascript
function mapUser(data) {
    const { id, first_name, last_name, email, created_at } = data;

    return {
        id,
        name: `${first_name} ${last_name}`,
        email,
        createdAt: new Date(created_at),

        getFullName() {
            return this.name;
        },

        getAge() {
            const today = new Date();
            const years = today.getFullYear() - this.createdAt.getFullYear();
            return years;
        }
    };
}
```

### 11.6.2. State Management

```javascript
function createStore(initialState = {}) {
    let state = { ...initialState };
    const listeners = [];

    return {
        getState() {
            return { ...state };
        },

        setState(updates) {
            state = { ...state, ...updates };
            listeners.forEach(listener => listener(state));
        },

        subscribe(listener) {
            listeners.push(listener);
            return () => {
                const index = listeners.indexOf(listener);
                listeners.splice(index, 1);
            };
        }
    };
}
```

### 11.6.3. Dynamic Object Creation

```javascript
function createFormData(fields) {
    const data = {};

    fields.forEach(field => {
        Object.assign(data, {
            [field.name]: field.value,
            [`${field.name}Valid`]: field.valid,
            [`validate${capitalize(field.name)}`]() {
                // Validation logic
                return this[`${field.name}Valid`];
            }
        });
    });

    return data;
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}
```

### 11.6.4. Event Handlers

```javascript
function createComponent(name, handlers = {}) {
    const component = {
        name,

        render() {
            return `<div class="${this.name}">Component</div>`;
        }
    };

    // Add event handlers dynamically
    Object.entries(handlers).forEach(([event, handler]) => {
        component[`on${capitalize(event)}`] = handler;
    });

    return component;
}

const button = createComponent('button', {
    click: () => console.log('Clicked'),
    hover: () => console.log('Hovered')
});
```

### 11.6.5. Configuration Builder

```javascript
function buildConfig(env) {
    const isProduction = env === 'production';
    const apiUrl = isProduction
        ? 'https://api.example.com'
        : 'http://localhost:3000';

    return {
        env,
        apiUrl,
        debug: !isProduction,
        timeout: isProduction ? 10000 : 5000,

        getEndpoint(path) {
            return `${this.apiUrl}${path}`;
        },

        log(message) {
            if (this.debug) {
                console.log(`[${this.env}]`, message);
            }
        }
    };
}
```

## 11.7. Getters and Setters

### 11.7.1. Basic Getters/Setters

```javascript
const user = {
    firstName: 'John',
    lastName: 'Doe',

    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },

    set fullName(name) {
        const [first, last] = name.split(' ');
        this.firstName = first;
        this.lastName = last;
    }
};

console.log(user.fullName);  // "John Doe"
user.fullName = 'Jane Smith';
console.log(user.firstName);  // "Jane"
console.log(user.lastName);   // "Smith"
```

### 11.7.2. Computed Properties

```javascript
const rectangle = {
    width: 10,
    height: 5,

    get area() {
        return this.width * this.height;
    },

    get perimeter() {
        return 2 * (this.width + this.height);
    }
};

console.log(rectangle.area);       // 50
console.log(rectangle.perimeter);  // 30

rectangle.width = 20;
console.log(rectangle.area);       // 100
```

## 11.8. Advanced Patterns

### 11.8.1. Chainable Methods

```javascript
const query = {
    _collection: 'users',
    _filters: [],
    _limit: null,

    from(collection) {
        this._collection = collection;
        return this;
    },

    where(field, value) {
        this._filters.push({ field, value });
        return this;
    },

    limit(n) {
        this._limit = n;
        return this;
    },

    execute() {
        console.log('Query:', {
            collection: this._collection,
            filters: this._filters,
            limit: this._limit
        });
    }
};

query
    .from('users')
    .where('age', 30)
    .where('active', true)
    .limit(10)
    .execute();
```

### 11.8.2. Private-like Properties

```javascript
const createCounter = () => {
    let _count = 0;  // Private variable

    return {
        increment() {
            _count++;
        },

        decrement() {
            _count--;
        },

        get count() {
            return _count;
        }
    };
};

const counter = createCounter();
counter.increment();
console.log(counter.count);  // 1
// counter._count  // undefined (not accessible)
```

### 11.8.3. Mixins

```javascript
const canEat = {
    eat(food) {
        console.log(`Eating ${food}`);
    }
};

const canWalk = {
    walk() {
        console.log('Walking...');
    }
};

const canSwim = {
    swim() {
        console.log('Swimming...');
    }
};

// Combine mixins
const duck = {
    name: 'Donald',
    ...canEat,
    ...canWalk,
    ...canSwim
};

duck.eat('bread');
duck.walk();
duck.swim();
```

## 11.9. Best Practices

### 11.9.1. Use Shorthand When Possible

```javascript
// Good
const user = { name, age, email };

// Verbose
const user = { name: name, age: age, email: email };
```

### 11.9.2. Consistent Method Style

```javascript
// Good: Use method shorthand
const obj = {
    method1() { },
    method2() { }
};

// Avoid mixing styles
const obj = {
    method1() { },
    method2: function() { }
};
```

### 11.9.3. Meaningful Computed Keys

```javascript
// Good: Clear intent
const config = {
    [`${env}_api_url`]: url
};

// Bad: Unclear
const config = {
    [a + b + c]: value
};
```

## 11.10. Tips & Tricks

### Tip 1: Combine Shorthand with Computed Keys

```javascript
// Efficient way to create objects dynamically
const field = 'email';
const email = 'test@example.com';

const obj = {
    email,  // Shorthand
    [`${field}Valid`]: true  // Computed key
};
```

### Tip 2: Using Getters for Computed Properties

```javascript
const user = {
    firstName: 'John',
    lastName: 'Doe',
    age: 30,

    // Computed properties without recalculating
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },

    get isAdult() {
        return this.age >= 18;
    }
};

console.log(user.fullName);  // "John Doe"
```

### Tip 3: Dynamic Method Names

```javascript
// Tạo validators dynamically
const validators = {};
['email', 'username', 'password'].forEach(field => {
    validators[`validate${field.charAt(0).toUpperCase() + field.slice(1)}`] = (value) => {
        return value && value.length > 0;
    };
});

console.log(validators.validateEmail('test@example.com'));  // true
```

### Tip 4: Object Merging with Shorthand

```javascript
// Merge multiple objects efficiently
const base = { a: 1, b: 2 };
const extended = { c: 3, d: 4 };
const merged = { ...base, ...extended };

// Hoặc sử dụng Object.assign
const merged2 = Object.assign({}, base, extended);
```

### Tip 5: Conditional Properties

```javascript
// Thêm properties có điều kiện
const user = {
    name: 'John',
    age: 30,
    ...(isAdmin && { role: 'admin', permissions: ['read', 'write', 'delete'] })
};
```

### Tip 6: Using Symbols with Computed Keys

```javascript
const privateId = Symbol('id');
const privateData = Symbol('data');

const user = {
    name: 'John',
    [privateId]: 123,
    [privateData]: { internal: 'secret' },

    getId() {
        return this[privateId];
    }
};
```

### Tip 7: Method Chaining Pattern

```javascript
// Enable fluent API
const calculator = {
    value: 0,

    add(n) {
        this.value += n;
        return this;
    },

    multiply(n) {
        this.value *= n;
        return this;
    },

    get result() {
        return this.value;
    }
};

console.log(calculator.add(5).multiply(2).add(3).result);  // 13
```

### Tip 8: Lazy Evaluation with Getters

```javascript
const expensiveData = {
    _cache: null,

    get data() {
        if (!this._cache) {
            console.log('Computing expensive operation...');
            this._cache = computeExpensiveData();
        }
        return this._cache;
    }
};

// data được tính chỉ khi truy cập lần đầu
```

### Tip 9: Destructuring with Renaming

```javascript
const user = {
    firstName: 'John',
    lastName: 'Doe',
    age: 30
};

// Rename properties khi destructure
const { firstName: first, lastName: last, age } = user;
console.log(first, last);  // John Doe
```

### Tip 10: Template Literal Keys

```javascript
// Sử dụng template literals cho computed keys
const prefix = 'api';
const version = 'v1';

const endpoints = {
    [`${prefix}_${version}_users`]: '/users',
    [`${prefix}_${version}_posts`]: '/posts',
    [`${prefix}_${version}_comments`]: '/comments'
};

console.log(endpoints.api_v1_users);  // '/users'
```

## 11.11. Common Mistakes

### Mistake 1: Arrow Functions Losing 'this'

```javascript
// BAD: this is undefined or window
const obj = {
    name: 'John',
    greet: () => {
        console.log(this.name);  // undefined
    }
};

// GOOD: Method shorthand
const obj = {
    name: 'John',
    greet() {
        console.log(this.name);  // "John"
    }
};
```

### Mistake 2: Computed Keys Evaluated Once

```javascript
// BAD: Key không update
let key = 'name';
const obj = {
    [key]: 'John'
};

key = 'email';
obj[key] = 'john@example.com';
console.log(obj);  // { name: 'John', email: '...' }
```

### Mistake 3: Duplicate Keys Silently Overwrite

```javascript
// BAD: Last value wins
const obj = {
    name: 'John',
    age: 30,
    name: 'Jane'  // Overwrites silently
};
console.log(obj.name);  // 'Jane'
```

### Mistake 4: Modifying Getter Without Setter

```javascript
// BAD: Read-only getter
const obj = {
    name: 'John',
    age: 30,

    get info() {
        return `${this.name} is ${this.age}`;
    }
};

obj.info = 'new value';  // Silent failure, không thay đổi
```

### Mistake 5: Complex Computed Keys

```javascript
// BAD: Khó đọc
const obj = {
    [['a', 'b'].join('_')]: 'value',  // a_b
    [Math.random()]: 'random'  // Unpredicatable
};

// GOOD: Clear intent
const prefix = 'user';
const obj = {
    [`${prefix}_name`]: 'value'
};
```

### Mistake 6: Not Handling 'this' Binding

```javascript
// BAD: this không được bind
const obj = {
    count: 0,
    increment() {
        this.count++;
    }
};

const fn = obj.increment;
fn();  // this is undefined

// GOOD: Bind explicitly
const fn = obj.increment.bind(obj);
fn();  // Works correctly
```

### Mistake 7: Spreading Non-Objects

```javascript
// BAD: Cannot spread non-objects
const arr = [1, 2, 3];
const obj = { ...arr };  // { '0': 1, '1': 2, '2': 3 }

// GOOD: Use proper methods
const obj = Object.fromEntries(arr.map((v, i) => [i, v]));
```

### Mistake 8: Infinite Loops with Getters

```javascript
// BAD: Infinite recursion
const obj = {
    get value() {
        return this.value;  // Calls itself infinitely
    }
};

// GOOD: Use backing property
const obj = {
    _value: 0,
    get value() {
        return this._value;
    },
    set value(v) {
        this._value = v;
    }
};
```

### Mistake 9: Missing Method Calls

```javascript
// BAD: Forgot to call method
const obj = {
    getName() {
        return 'John';
    }
};

console.log(obj.getName);  // function, not 'John'

// GOOD: Call the method
console.log(obj.getName());  // 'John'
```

### Mistake 10: Computed Keys with Side Effects

```javascript
// BAD: Side effects in computed keys
let counter = 0;
const obj = {
    [counter++]: 'first',
    [counter++]: 'second'
};

console.log(counter);  // 2 (unexpected mutation)

// GOOD: Separate logic
const id1 = counter++;
const id2 = counter++;
const obj = {
    [id1]: 'first',
    [id2]: 'second'
};
```

## 11.12. Troubleshooting Issues

### Issue 1: Getters/Setters Not Working on Spread

**Problem:**
```javascript
const obj = {
    _name: 'John',
    get name() { return this._name; },
    set name(v) { this._name = v; }
};

const copy = { ...obj };
copy.name = 'Jane';  // Setter not called
```

**Solution:**
```javascript
const copy = Object.create(
    Object.getPrototypeOf(obj),
    Object.getOwnPropertyDescriptors(obj)
);
```

### Issue 2: Method Binding in Factory Pattern

**Problem:**
```javascript
function createUser(name) {
    return {
        name,
        greet() {
            console.log(this.name);
        }
    };
}

const user = createUser('John');
const fn = user.greet;
fn();  // this is undefined
```

**Solution:**
```javascript
function createUser(name) {
    return {
        name,
        greet: function() {
            console.log(this.name);
        }.bind(this)  // Explicit binding
    };
}
```

### Issue 3: Computed Keys Performance

**Problem:**
```javascript
// Slow: Computing keys every time
for (let i = 0; i < 1000; i++) {
    obj[`key_${heavyComputation(i)}`] = value;
}
```

**Solution:**
```javascript
// Cache computed keys
const keys = Array.from({ length: 1000 }, (_, i) =>
    `key_${heavyComputation(i)}`
);
const obj = Object.fromEntries(
    keys.map((key, i) => [key, values[i]])
);
```

### Issue 4: Symbol Properties Lost

**Problem:**
```javascript
const sym = Symbol('id');
const obj = {
    name: 'John',
    [sym]: 123
};

const { name, ...rest } = obj;
console.log(rest);  // {}, không có symbol
```

**Solution:**
```javascript
const symbols = Object.getOwnPropertySymbols(obj);
const { name, ...rest } = obj;
const result = {
    name,
    ...rest,
    ...symbols.reduce((acc, sym) => ({ ...acc, [sym]: obj[sym] }), {})
};
```

### Issue 5: Circular References

**Problem:**
```javascript
const obj = {
    self: null
};
obj.self = obj;  // Circular reference

JSON.stringify(obj);  // Error!
```

**Solution:**
```javascript
const obj = {
    name: 'John',
    // Don't store circular refs directly
};

// Use WeakMap for circular tracking
const circular = new WeakMap();
function serialize(obj) {
    if (circular.has(obj)) return '[Circular]';
    circular.set(obj, true);
    // ... serialization logic
}
```

### Issue 6: Method Not Inherited

**Problem:**
```javascript
const parent = {
    greet() { return 'Hello'; }
};

const child = { ...parent };
// child has own property 'greet', not inherited
```

**Solution:**
```javascript
// Use Object.assign for inherited properties
const child = Object.assign({}, parent);

// Or Object.create for prototype chain
const child = Object.create(parent);
```

### Issue 7: Getter Called Every Time

**Problem:**
```javascript
const obj = {
    _data: null,
    get data() {
        console.log('Computing...');
        return expensiveOperation();  // Called every access
    }
};
```

**Solution:**
```javascript
const obj = {
    _data: null,
    get data() {
        if (!this._data) {
            console.log('Computing once...');
            this._data = expensiveOperation();
        }
        return this._data;
    },
    clearCache() {
        this._data = null;
    }
};
```

### Issue 8: Property Names as Strings vs Symbols

**Problem:**
```javascript
const obj = {
    [Symbol.for('id')]: 123,
    ['id']: 456
};

console.log(obj.id);  // 456 (string key)
console.log(obj[Symbol.for('id')]);  // 123 (symbol key)
```

**Solution:**
```javascript
// Be consistent with key types
const obj = {
    id: 123,  // String key
    description: 'User'
};

const objWithSymbols = {
    [Symbol.for('id')]: 123,  // Symbol key
    description: 'User'
};
```

### Issue 9: Computed Keys with Null/Undefined

**Problem:**
```javascript
const key = null;
const obj = {
    [key]: 'value'  // Converted to 'null'
};

console.log(obj.null);  // 'value'
console.log(Object.keys(obj));  // ['null']
```

**Solution:**
```javascript
const key = null;
const obj = {
    [key ?? 'default']: 'value'  // Use nullish coalescing
};
```

### Issue 10: Method Shorthand vs Function Property

**Problem:**
```javascript
const obj1 = {
    greet() { }  // Method shorthand - different descriptor
};

const obj2 = {
    greet: function() { }  // Function property
};

// Slightly different behavior and performance
```

**Solution:**
```javascript
// Use method shorthand consistently
const obj = {
    name: 'John',
    greet() { return 'Hello'; },
    getValue() { return this.name; }
};
```

## 11.13. Advanced Topics

### 11.13.1. Proxy with Object Literals

```javascript
const handler = {
    get(target, prop) {
        console.log(`Getting ${prop}`);
        return target[prop];
    },
    set(target, prop, value) {
        console.log(`Setting ${prop} = ${value}`);
        target[prop] = value;
        return true;
    }
};

const user = {
    name: 'John',
    age: 30
};

const proxyUser = new Proxy(user, handler);
proxyUser.name = 'Jane';  // Logs: Setting name = Jane
```

### 11.13.2. Object Descriptors

```javascript
const obj = {};

Object.defineProperty(obj, 'name', {
    value: 'John',
    writable: false,  // Cannot change
    enumerable: true,  // Shows in for...in
    configurable: false  // Cannot redefine
});

Object.defineProperties(obj, {
    age: {
        value: 30,
        writable: true
    },
    email: {
        value: 'john@example.com',
        enumerable: true
    }
});
```

### 11.13.3. Freezing Objects

```javascript
const config = {
    apiUrl: 'http://localhost:3000',
    timeout: 5000
};

// Prevent modifications
Object.freeze(config);
config.apiUrl = 'http://example.com';  // Silently fails
Object.isFrozen(config);  // true

// Shallow freeze only
const user = {
    name: 'John',
    address: { city: 'NYC' }
};

Object.freeze(user);
user.address.city = 'LA';  // Works! Only top level frozen
```

### 11.13.4. Sealed Objects

```javascript
const data = {
    id: 1,
    name: 'Test'
};

Object.seal(data);  // Cannot add/remove properties

data.name = 'Updated';  // Works
data.email = 'test@example.com';  // Fails silently
delete data.id;  // Fails silently

Object.isSealed(data);  // true
```

### 11.13.5. Object Composition Pattern

```javascript
// Compose behavior from multiple objects
const canEat = {
    eat(food) {
        console.log(`Eating ${food}`);
        return this;
    }
};

const canWalk = {
    walk(distance) {
        console.log(`Walking ${distance}m`);
        return this;
    }
};

const canSwim = {
    swim(distance) {
        console.log(`Swimming ${distance}m`);
        return this;
    }
};

// Compose a duck
const duck = {
    name: 'Donald',
    ...canEat,
    ...canWalk,
    ...canSwim
};

duck.eat('bread').walk(100).swim(50);
```

## 11.14. Exercises

### Exercise 1 (Dễ): Property Shorthand

```javascript
// Chuyển đổi sang enhanced object literal
const name = 'John';
const email = 'john@example.com';
const age = 30;

const user = {
    name: name,
    email: email,
    age: age
};

// Giải pháp:
// const user = { name, email, age };
```

### Exercise 2 (Dễ): Method Shorthand

```javascript
// Chuyển đổi sang method shorthand
const calculator = {
    value: 0,
    add: function(n) {
        this.value += n;
        return this.value;
    }
};

// Giải pháp: Sử dụng method shorthand
```

### Exercise 3 (Dễ): Computed Properties

```javascript
// Tạo object với computed keys từ array
const fields = ['username', 'password', 'email'];

// Tạo object: { username: '', password: '', email: '' }
```

### Exercise 4 (Dễ): Getters/Setters

```javascript
// Tạo object với getter cho fullName
const person = {
    firstName: 'John',
    lastName: 'Doe'
    // Thêm getter fullName
};

console.log(person.fullName);  // "John Doe"
```

### Exercise 5 (Trung bình): Dynamic Object Factory

```javascript
// Tạo factory tạo user objects
function createUser(name, email, role = 'user') {
    // Trả về object với:
    // - name, email, role (shorthand)
    // - getProfile() method
    // - isAdmin() method
}

const user1 = createUser('John', 'john@example.com');
const user2 = createUser('Jane', 'jane@example.com', 'admin');
```

### Exercise 6 (Trung bình): Configuration Builder

```javascript
// Tạo configuration object builder
function createConfig(env) {
    // Trả về object với các settings khác nhau tùy theo env (development/production)
    // Có methods: get(key), has(key)
}
```

### Exercise 7 (Trung bình): Chainable Query Builder

```javascript
// Tạo query builder với chaining
const query = {
    // select(fields)
    // where(condition)
    // orderBy(field, direction)
    // build()  <- trả về query object
};

// Usage:
// query.select('name', 'email').where('age > 18').orderBy('name').build();
```

### Exercise 8 (Trung bình): Object Merger

```javascript
// Tạo hàm merge multiple objects
function mergeObjects(...objects) {
    // Merge tất cả objects, later ones override earlier
    // Sử dụng spread operator
}

const result = mergeObjects(
    { a: 1, b: 2 },
    { b: 3, c: 4 },
    { c: 5, d: 6 }
);
// { a: 1, b: 3, c: 5, d: 6 }
```

### Exercise 9 (Trung bình): Computed Keys from Data

```javascript
// Tạo cache object với computed keys
function createCache(data) {
    // Tạo object với keys: `cache_${key}` cho mỗi item
    // Thêm get(key) và set(key, value) methods
}
```

### Exercise 10 (Khó): Observer Pattern

```javascript
// Tạo observable object
function createObservable(data) {
    // Trả về object có:
    // - Tất cả properties của data
    // - subscribe(callback) - gọi callback khi data thay đổi
    // - Getters/Setters cho mỗi property
}

const user = createObservable({ name: 'John', age: 30 });
user.subscribe((data) => console.log('Updated:', data));
user.name = 'Jane';  // Logs: Updated: { name: 'Jane', age: 30 }
```

### Exercise 11 (Khó): Lazy Computed Properties

```javascript
// Tạo object với lazy-computed properties
function createLazyObject(computeFns) {
    // computeFns = { age: () => 2023 - birthYear, ... }
    // Properties được tính chỉ khi access, caching result
}

const user = createLazyObject({
    age: () => { console.log('Computing...'); return 30; }
});
user.age;  // Logs: Computing... -> 30
user.age;  // 30 (không log, dùng cache)
```

### Exercise 12 (Khó): Deep Freeze with Thaw

```javascript
// Tạo object frozen nhưng có thể unfreeze
function createFrozenObject(data) {
    const frozen = Object.freeze({ ...data });

    return {
        get() { return { ...frozen }; },
        getProperty(key) { return frozen[key]; },
        thaw() { return { ...frozen }; }  // Return unfrozen copy
    };
}

const config = createFrozenObject({ apiUrl: 'http://localhost' });
config.get().apiUrl = 'http://example.com';  // Fails
const modifiable = config.thaw();
modifiable.apiUrl = 'http://example.com';  // Works
```

---

**Kết luận:** Enhanced object literals làm code ngắn gọn và dễ đọc hơn với property shorthand, method shorthand, và computed property names. Nắm vững các patterns như factories, builders, và composition để tạo maintainable code.

**Chương tiếp theo:** Async/Await
