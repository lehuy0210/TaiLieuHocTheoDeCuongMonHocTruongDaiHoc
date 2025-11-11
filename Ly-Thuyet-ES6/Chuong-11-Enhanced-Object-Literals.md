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

## 11.10. Common Mistakes

### 11.10.1. Arrow Functions in Methods

```javascript
// Bad: Arrow function doesn't bind 'this'
const user = {
    name: 'John',
    greet: () => {
        console.log(this.name);  // undefined
    }
};

// Good: Use method shorthand
const user = {
    name: 'John',
    greet() {
        console.log(this.name);  // "John"
    }
};
```

### 11.10.2. Computed Key Evaluation

```javascript
let key = 'name';
const obj = {
    [key]: 'John'  // Evaluated once at creation
};

key = 'age';
console.log(obj.name);  // "John" (still name)
console.log(obj.age);   // undefined
```

### 11.10.3. Duplicate Keys

```javascript
// Last one wins
const obj = {
    name: 'John',
    age: 30,
    name: 'Jane'  // Overwrites first name
};

console.log(obj.name);  // "Jane"
```

## 11.11. Exercises

### Exercise 1: Shorthand Practice

```javascript
// Convert to enhanced object literal
const name = 'John';
const age = 30;
function greet() {
    return 'Hello';
}

const user = {
    name: name,
    age: age,
    greet: function() {
        return greet();
    }
};
```

### Exercise 2: Computed Properties

```javascript
// Create an object with dynamic keys from array
const fields = ['name', 'email', 'age'];
const values = ['John', 'john@example.com', 30];

// Create object: { name: 'John', email: '...', age: 30 }
```

### Exercise 3: Chainable Object

```javascript
// Create a chainable query builder with:
// - select(fields)
// - from(table)
// - where(condition)
// - build() - returns query object
```

---

**Kết luận:** Enhanced object literals làm code ngắn gọn và dễ đọc hơn với property shorthand, method shorthand, và computed property names.

**Chương tiếp theo:** Async/Await
