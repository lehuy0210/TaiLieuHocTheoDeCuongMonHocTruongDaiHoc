# CHƯƠNG 6: SPREAD & REST OPERATORS

## 6.1. Giới thiệu

Cả Spread và Rest đều dùng syntax `...`, nhưng có mục đích khác nhau:
- **Spread**: Expands (phân tán) elements
- **Rest**: Collects (thu thập) elements

## 6.2. Spread Operator (...)

### 6.2.1. Array Spreading

**Basic Spread:**
```javascript
const numbers = [1, 2, 3];

// ES5
console.log.apply(console, numbers);  // 1 2 3

// ES6
console.log(...numbers);  // 1 2 3
```

**Combining Arrays:**
```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// ES5
const combined = arr1.concat(arr2);

// ES6
const combined = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// Mix with literals
const mixed = [0, ...arr1, 3.5, ...arr2, 7];
// [0, 1, 2, 3, 3.5, 4, 5, 6, 7]
```

**Copying Arrays:**
```javascript
const original = [1, 2, 3];

// ES5 - creates reference (not copy)
const copy1 = original;
copy1.push(4);  // Modifies original!

// ES5 - real copy
const copy2 = original.slice();

// ES6 - real copy
const copy3 = [...original];

copy3.push(4);  // Does NOT modify original
```

### 6.2.2. Array Methods

**Math Functions:**
```javascript
const numbers = [5, 2, 8, 1, 9];

// ES5
const max = Math.max.apply(null, numbers);

// ES6
const max = Math.max(...numbers);  // 9
const min = Math.min(...numbers);  // 1
```

**Array.push():**
```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// ES5
arr1.push.apply(arr1, arr2);

// ES6
arr1.push(...arr2);
console.log(arr1);  // [1, 2, 3, 4, 5, 6]
```

### 6.2.3. Object Spreading

**Copying Objects:**
```javascript
const user = { name: 'John', age: 30 };

// Shallow copy
const copy = { ...user };

copy.age = 31;  // Does NOT modify original
console.log(user.age);  // 30
```

**Merging Objects:**
```javascript
const defaults = { theme: 'light', lang: 'en' };
const userPrefs = { theme: 'dark' };

// Later properties override earlier ones
const settings = { ...defaults, ...userPrefs };
// { theme: 'dark', lang: 'en' }
```

**Adding Properties:**
```javascript
const user = { name: 'John', age: 30 };

const updatedUser = {
    ...user,
    age: 31,
    city: 'NYC'
};
// { name: 'John', age: 31, city: 'NYC' }
```

### 6.2.4. Function Arguments

```javascript
function add(a, b, c) {
    return a + b + c;
}

const numbers = [1, 2, 3];

// ES5
add.apply(null, numbers);

// ES6
add(...numbers);  // 6
```

### 6.2.5. String Spreading

```javascript
const str = 'Hello';

// Spread string into array
const chars = [...str];  // ['H', 'e', 'l', 'l', 'o']

// Spread in array literal
const arr = ['start', ...str, 'end'];
// ['start', 'H', 'e', 'l', 'l', 'o', 'end']
```

### 6.2.6. Converting Iterables

```javascript
// Set to Array
const set = new Set([1, 2, 3]);
const arr = [...set];  // [1, 2, 3]

// Map keys/values to Array
const map = new Map([['a', 1], ['b', 2]]);
const keys = [...map.keys()];      // ['a', 'b']
const values = [...map.values()];  // [1, 2]
const entries = [...map];          // [['a', 1], ['b', 2]]

// NodeList to Array
const divs = document.querySelectorAll('div');
const divArray = [...divs];
```

## 6.3. Rest Parameters (...)

### 6.3.1. Function Parameters

**Basic Rest:**
```javascript
// ES5
function sum() {
    var args = Array.prototype.slice.call(arguments);
    return args.reduce(function(a, b) { return a + b; });
}

// ES6
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b);
}

sum(1, 2, 3, 4);  // 10
```

**Named + Rest:**
```javascript
function greet(greeting, ...names) {
    return `${greeting} ${names.join(', ')}!`;
}

greet('Hello', 'John', 'Jane', 'Bob');
// "Hello John, Jane, Bob!"
```

**Important:** Rest must be last parameter:
```javascript
// Valid
function fn(a, b, ...rest) { }

// Invalid
function fn(...rest, a, b) { }  // SyntaxError
```

### 6.3.2. Array Destructuring

```javascript
const numbers = [1, 2, 3, 4, 5];

// Get first and rest
const [first, ...rest] = numbers;
console.log(first);  // 1
console.log(rest);   // [2, 3, 4, 5]

// Get first, second, and rest
const [a, b, ...others] = numbers;
console.log(a);       // 1
console.log(b);       // 2
console.log(others);  // [3, 4, 5]
```

**Note:** Rest must be last element:
```javascript
// Valid
const [first, ...rest] = arr;

// Invalid
const [...rest, last] = arr;  // SyntaxError
```

### 6.3.3. Object Destructuring

```javascript
const user = {
    id: 1,
    name: 'John',
    age: 30,
    city: 'NYC',
    country: 'USA'
};

// Extract some properties, collect rest
const { id, name, ...details } = user;

console.log(id);      // 1
console.log(name);    // "John"
console.log(details); // { age: 30, city: 'NYC', country: 'USA' }
```

## 6.4. Practical Examples

### 6.4.1. Array Manipulation

```javascript
// Remove duplicates
const numbers = [1, 2, 2, 3, 3, 4];
const unique = [...new Set(numbers)];  // [1, 2, 3, 4]

// Flatten one level
const nested = [[1, 2], [3, 4], [5, 6]];
const flat = [].concat(...nested);  // [1, 2, 3, 4, 5, 6]

// Insert in middle
const arr = [1, 2, 5, 6];
const inserted = [...arr.slice(0, 2), 3, 4, ...arr.slice(2)];
// [1, 2, 3, 4, 5, 6]

// Remove element
const remove = (arr, index) => [
    ...arr.slice(0, index),
    ...arr.slice(index + 1)
];
```

### 6.4.2. Object Updates (Immutable)

```javascript
// Update property
const user = { name: 'John', age: 30 };
const updated = { ...user, age: 31 };

// Add property
const withCity = { ...user, city: 'NYC' };

// Remove property
const { age, ...withoutAge } = user;

// Conditional properties
const isAdmin = true;
const userWithRole = {
    ...user,
    ...(isAdmin && { role: 'admin' })
};
```

### 6.4.3. Function Utilities

```javascript
// Flexible sum function
const sum = (...numbers) => numbers.reduce((a, b) => a + b, 0);
sum(1, 2, 3);        // 6
sum(1, 2, 3, 4, 5);  // 15

// Logger with prefix
const log = (prefix, ...messages) => {
    console.log(`[${prefix}]`, ...messages);
};
log('INFO', 'User', 'logged in');  // [INFO] User logged in

// First and rest pattern
const processData = (config, ...items) => {
    items.forEach(item => {
        console.log(`Processing ${item} with config:`, config);
    });
};
```

### 6.4.4. Component Props (React-like)

```javascript
// Pass all props except specific ones
function Button({ type, children, ...props }) {
    return `<button type="${type}" {...props}>${children}</button>`;
}

// Merge default and custom props
function createComponent(defaults) {
    return (customProps) => {
        const props = { ...defaults, ...customProps };
        return props;
    };
}
```

### 6.4.5. State Management

```javascript
// Redux-like state updates
const state = {
    user: { name: 'John', age: 30 },
    posts: [1, 2, 3],
    loading: false
};

// Update nested property
const newState = {
    ...state,
    user: {
        ...state.user,
        age: 31
    }
};

// Add to array
const withNewPost = {
    ...state,
    posts: [...state.posts, 4]
};
```

## 6.5. Advanced Patterns

### 6.5.1. Deep Clone (Shallow vs Deep)

```javascript
// Shallow clone (1 level)
const original = { a: 1, b: { c: 2 } };
const shallow = { ...original };
shallow.b.c = 3;  // Modifies original.b.c!

// Deep clone (recursive)
function deepClone(obj) {
    if (typeof obj !== 'object' || obj === null) return obj;
    const clone = Array.isArray(obj) ? [] : {};
    for (let key in obj) {
        clone[key] = deepClone(obj[key]);
    }
    return clone;
}

// Or use JSON (limitations: no functions, dates, etc.)
const deep = JSON.parse(JSON.stringify(original));
```

### 6.5.2. Conditional Spreading

```javascript
const condition = true;
const obj = {
    name: 'John',
    ...(condition && { age: 30 }),
    ...(false && { city: 'NYC' })  // Not included
};
// { name: 'John', age: 30 }

// Array conditional
const arr = [
    1,
    2,
    ...(condition ? [3, 4] : []),
    5
];
// [1, 2, 3, 4, 5]
```

### 6.5.3. Dynamic Object Keys

```javascript
const key = 'name';
const value = 'John';

const obj = {
    ...{ [key]: value },
    age: 30
};
// { name: 'John', age: 30 }
```

### 6.5.4. Pipe/Compose Functions

```javascript
const pipe = (...fns) => (value) =>
    fns.reduce((acc, fn) => fn(acc), value);

const add5 = x => x + 5;
const multiply2 = x => x * 2;
const subtract3 = x => x - 3;

const compute = pipe(add5, multiply2, subtract3);
compute(10);  // (10 + 5) * 2 - 3 = 27
```

## 6.6. Common Patterns

### 6.6.1. Cloning & Merging

```javascript
// Clone array
const clone = [...original];

// Clone object
const clone = { ...original };

// Merge multiple objects
const merged = { ...obj1, ...obj2, ...obj3 };

// Merge with override
const config = { ...defaultConfig, ...userConfig };
```

### 6.6.2. Variadic Functions

```javascript
// Accept any number of arguments
const multiply = (...numbers) =>
    numbers.reduce((acc, n) => acc * n, 1);

const concat = (...strings) => strings.join('');

const max = (...numbers) => Math.max(...numbers);
```

### 6.6.3. Array Operations

```javascript
// Prepend
const prepend = (arr, ...items) => [...items, ...arr];

// Append
const append = (arr, ...items) => [...arr, ...items];

// Insert at index
const insert = (arr, index, ...items) => [
    ...arr.slice(0, index),
    ...items,
    ...arr.slice(index)
];
```

## 6.7. Best Practices

### 6.7.1. Immutability

```javascript
// DO: Create new objects/arrays
const newState = { ...state, updated: true };
const newArray = [...array, newItem];

// DON'T: Mutate original
state.updated = true;        // ❌
array.push(newItem);         // ❌
```

### 6.7.2. Performance

```javascript
// Good: Simple spreading
const arr = [...smallArray];

// Caution: Spreading large arrays (O(n))
const arr = [...veryLargeArray];  // Can be slow

// Alternative for large arrays
const arr = Array.from(veryLargeArray);
```

### 6.7.3. Naming Rest Parameters

```javascript
// Good: Descriptive names
function log(level, ...messages) { }
function sum(...numbers) { }

// Bad: Generic names
function fn(...args) { }  // Less clear
```

## 6.8. Common Mistakes

### 6.8.1. Rest Must Be Last

```javascript
// Wrong
function fn(...rest, last) { }  // SyntaxError
const [...rest, last] = arr;    // SyntaxError

// Correct
function fn(first, ...rest) { }
const [first, ...rest] = arr;
```

### 6.8.2. Shallow Copy Issues

```javascript
const original = { a: 1, b: { c: 2 } };
const copy = { ...original };

copy.b.c = 3;
console.log(original.b.c);  // 3 (modified!)

// Fix: Deep clone
const deepCopy = JSON.parse(JSON.stringify(original));
```

### 6.8.3. Spread vs Rest Context

```javascript
// Spread: Expands
const arr = [...[1, 2, 3]];  // [1, 2, 3]

// Rest: Collects
const [first, ...rest] = [1, 2, 3];  // rest = [2, 3]
```

## 6.9. Tips & Tricks

### Tip 1: Shallow Clone vs Deep Clone

```javascript
// Shallow clone (only first level)
const obj = { a: 1, b: { c: 2 } };
const shallow = { ...obj };
shallow.b.c = 3; // Affects original!

// Deep clone for nested objects
const deep = {
    ...obj,
    b: { ...obj.b }
};

// Or use JSON (with limitations)
const deepClone = JSON.parse(JSON.stringify(obj));
```

### Tip 2: Conditional Spread

```javascript
// Spread only if condition is true
const user = {
    name: 'John',
    ...(isAdmin && { role: 'admin' }),
    ...(isPremium && { premium: true })
};
```

### Tip 3: Merge Without Duplicates

```javascript
// Use Set with spread
const arr1 = [1, 2, 3];
const arr2 = [3, 4, 5];
const unique = [...new Set([...arr1, ...arr2])];
// [1, 2, 3, 4, 5]
```

### Tip 4: Rest with Destructuring

```javascript
// Extract first, keep rest
const [first, ...rest] = [1, 2, 3, 4, 5];
console.log(first); // 1
console.log(rest);  // [2, 3, 4, 5]
```

### Tip 5: Function Composition

```javascript
// Compose functions
const compose = (...fns) => (x) =>
    fns.reduceRight((acc, fn) => fn(acc), x);

const pipe = (...fns) => (x) =>
    fns.reduce((acc, fn) => fn(acc), x);
```

### Tip 6: Default Values

```javascript
// Provide defaults
function createUser(options = {}) {
    const defaults = {
        name: 'Guest',
        age: 0,
        role: 'user'
    };
    return { ...defaults, ...options };
}
```

### Tip 7: Immutable Updates

```javascript
// Update nested object immutably
const state = {
    user: { profile: { name: 'John', age: 30 } }
};

const newState = {
    ...state,
    user: {
        ...state.user,
        profile: {
            ...state.user.profile,
            age: 31
        }
    }
};
```

### Tip 8: Variadic Wrapper

```javascript
// Wrapper accepting any number of args
function createLogger(prefix) {
    return (...args) => {
        console.log(prefix, ...args);
    };
}

const log = createLogger('[LOG]');
log('message', 1, 2, 3);
```

### Tip 9: Object Property Filtering

```javascript
// Filter object properties
function omit(obj, ...keys) {
    const result = { ...obj };
    keys.forEach(key => delete result[key]);
    return result;
}

function pick(obj, ...keys) {
    return keys.reduce((result, key) => ({
        ...result,
        [key]: obj[key]
    }), {});
}
```

### Tip 10: Spread for String

```javascript
// Convert string to array correctly
const str = 'hello';
const chars = [...str];  // ['h', 'e', 'l', 'l', 'o']

// Works with emojis correctly
const emoji = '👨‍👩‍👧‍👦';
const emojiArr = [...emoji]; // Correct count
```

## 6.10. Common Mistakes

### Mistake 1: Shallow Copy Issues

```javascript
// BAD: Nested objects referenced
const original = { a: 1, b: { c: 2 } };
const copy = { ...original };
copy.b.c = 3;
console.log(original.b.c); // 3 - Changed!

// GOOD: Deep copy nested
const copy = {
    ...original,
    b: { ...original.b }
};
```

### Mistake 2: Modifying Rest Parameters

```javascript
// BAD: Modifies original
function process(...items) {
    items.push(99);
    return items;
}

// GOOD: Create new array
function process(...items) {
    return [...items, 99];
}
```

### Mistake 3: Spreading Null/Undefined

```javascript
// BAD: Throws error
const obj = { ...null };      // TypeError
const obj = { ...undefined }; // TypeError

// GOOD: Use conditional
const obj = { ...(value || {}) };
const obj = { ...(value ?? {}) };
```

### Mistake 4: Rest Must Be Last

```javascript
// BAD: Syntax error
function wrong(...rest, last) { }  // Error

// GOOD
function correct(first, ...rest) { }
```

### Mistake 5: Spread Order Matters

```javascript
// BAD: Wrong order
const user = {
    name: 'Updated',
    ...{ name: 'Original', age: 30 }
};
// name becomes 'Original'

// GOOD: Spread first
const user = {
    ...{ name: 'Original', age: 30 },
    name: 'Updated'
};
```

### Mistake 6: Mixing Rest with Arguments

```javascript
// BAD: Don't use arguments
function wrong(...args) {
    console.log(arguments); // Don't do this
}

// GOOD: Use rest only
function correct(...args) {
    console.log(args);
}
```

### Mistake 7: Spreading Non-Iterables

```javascript
// BAD: Can't spread objects to array
const obj = { a: 1, b: 2 };
const arr = [...obj]; // TypeError

// GOOD: Use Object methods
const arr = Object.values(obj);
const entries = Object.entries(obj);
```

### Mistake 8: Performance Issues

```javascript
// BAD: Inefficient for large arrays
function merge(...arrays) {
    return [...arrays[0], ...arrays[1]];
}

// GOOD: Use concat
function merge(...arrays) {
    return [].concat(...arrays);
}
```

### Mistake 9: Can't Destructure in Rest

```javascript
// BAD: Syntax error
function wrong([...rest, last]) { }

// GOOD
function correct([first, ...rest]) {
    const last = rest[rest.length - 1];
}
```

### Mistake 10: Breaking References

```javascript
// BAD: Spread breaks reference
const original = [1, 2, 3];
const wrapped = { items: original };
const copied = { ...wrapped, items: [...wrapped.items] };

original.push(4);
console.log(copied.items); // [1, 2, 3] - No 4!

// GOOD: Keep reference if needed
const copied = { ...wrapped };
```

## 6.11. Troubleshooting

### Issue 1: Custom Objects Not Spreading

**Problem:**
```javascript
class MyClass {
    constructor(value) {
        this.value = value;
    }
}

const obj = new MyClass(42);
const spread = { ...obj };
console.log(spread instanceof MyClass); // false
```

**Solution:**
```javascript
class MyClass {
    constructor(value) {
        this.value = value;
    }

    clone() {
        return Object.assign(new MyClass(this.value), this);
    }
}
```

### Issue 2: Losing Getters/Setters

**Problem:**
```javascript
const obj = {
    _value: 0,
    get value() { return this._value; },
    set value(v) { this._value = v; }
};

const spread = { ...obj };
spread.value = 10; // Setter not copied!
```

**Solution:**
```javascript
// Use Object.assign
const spread = Object.assign({}, obj);

// Or copy descriptors
const spread = Object.defineProperties(
    {},
    Object.getOwnPropertyDescriptors(obj)
);
```

### Issue 3: Memory with Large Spreads

**Problem:**
```javascript
const huge = new Array(1000000).fill(0);
const copies = [...huge, ...huge, ...huge]; // Memory issue
```

**Solution:**
```javascript
// Use concat
const copies = [].concat(huge, huge, huge);

// Or build gradually
const result = [];
result.push(...huge);
result.push(...huge);
result.push(...huge);
```

### Issue 4: Circular References

**Problem:**
```javascript
const obj = { a: 1 };
obj.self = obj;
const spread = { ...obj };
console.log(spread.self === spread); // false
```

**Solution:**
```javascript
function deepClone(obj, hash = new WeakMap()) {
    if (Object(obj) !== obj) return obj;
    if (hash.has(obj)) return hash.get(obj);

    const result = Array.isArray(obj) ? [] : {};
    hash.set(obj, result);

    return Object.assign(
        result,
        ...Object.keys(obj).map(key => ({
            [key]: deepClone(obj[key], hash)
        }))
    );
}
```

### Issue 5: Rest Performance

**Problem:**
```javascript
// Slow for many arguments
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b, 0);
}
sum(...Array(10000).fill(1));
```

**Solution:**
```javascript
// Accept array directly
function sum(numbers) {
    if (!Array.isArray(numbers)) {
        numbers = Array.from(arguments);
    }
    return numbers.reduce((a, b) => a + b, 0);
}
```

### Issue 6: Spread Order in Objects

**Problem:**
```javascript
const config = {
    host: 'localhost',
    ...userConfig,
    port: 3000,
    ...defaultConfig
};
// Confusing order
```

**Solution:**
```javascript
// Be explicit
const config = {
    ...defaultConfig,
    ...userConfig,
    host: 'localhost',
    port: 3000
};
```

### Issue 7: Array Subclasses

**Problem:**
```javascript
class MyArray extends Array {
    sum() { return this.reduce((a, b) => a + b, 0); }
}

const arr = new MyArray(1, 2, 3);
const spread = [...arr];
console.log(spread.sum); // undefined
```

**Solution:**
```javascript
// Use slice
const copy = arr.slice();

// Or custom clone
class MyArray extends Array {
    clone() {
        return MyArray.from(this);
    }
}
```

### Issue 8: Nested Spread Confusion

**Problem:**
```javascript
const obj = { a: { b: { c: 1 } } };
const update = {
    ...obj,
    a: { ...obj.a, b: { c: 2 } }
};
// Lost nested properties?
```

**Solution:**
```javascript
// Spread all levels
const update = {
    ...obj,
    a: {
        ...obj.a,
        b: { ...obj.a.b, c: 2 }
    }
};
```

### Issue 9: Async Iterables

**Problem:**
```javascript
async function* asyncGen() {
    yield 1;
    yield 2;
}

const arr = [...asyncGen()]; // Error
```

**Solution:**
```javascript
async function collectAsync(asyncIterable) {
    const result = [];
    for await (const item of asyncIterable) {
        result.push(item);
    }
    return result;
}

const arr = await collectAsync(asyncGen());
```

### Issue 10: Rest with Defaults

**Problem:**
```javascript
function fn({ a = 1, ...rest } = {}) {
    console.log(a, rest);
}
fn({ a: 2, b: 3 }); // What is rest?
```

**Solution:**
```javascript
// Be explicit
function fn(options = {}) {
    const { a = 1, ...rest } = options;
    console.log(a, rest);
}
```

## 6.12. Advanced Topics

### 6.12.1. Proxy with Spread

```javascript
const handler = {
    get(target, prop) {
        console.log(`Getting ${prop}`);
        return target[prop];
    },
    ownKeys(target) {
        console.log('Spreading');
        return Reflect.ownKeys(target);
    }
};

const obj = new Proxy({ a: 1, b: 2 }, handler);
const spread = { ...obj };
```

### 6.12.2. Generator with Spread

```javascript
function* generator() {
    yield 1;
    yield 2;
    yield 3;
}

const arr = [...generator()]; // [1, 2, 3]

// Infinite generator
function* infinite() {
    let i = 0;
    while (true) yield i++;
}

function take(n, iterable) {
    const result = [];
    for (const item of iterable) {
        if (result.length >= n) break;
        result.push(item);
    }
    return result;
}
```

### 6.12.3. Symbol Properties

```javascript
// Spread doesn't copy symbols
const sym = Symbol('id');
const obj = {
    name: 'John',
    [sym]: 123
};

const spread = { ...obj };
console.log(spread[sym]); // undefined

// Copy symbols manually
const withSymbols = {
    ...obj,
    ...Object.getOwnPropertySymbols(obj).reduce((result, s) => ({
        ...result,
        [s]: obj[s]
    }), {})
};
```

### 6.12.4. Custom Spread Behavior

```javascript
class CustomSpread {
    constructor(data) {
        this.data = data;
    }

    *[Symbol.iterator]() {
        yield* this.data;
    }

    toJSON() {
        return this.data;
    }
}

const custom = new CustomSpread([1, 2, 3]);
const arr = [...custom]; // [1, 2, 3]
```

### 6.12.5. Optimization Patterns

```javascript
// BAD: Multiple spreads
function merge(...objs) {
    return { ...objs[0], ...objs[1], ...objs[2] };
}

// GOOD: Single reduce
function merge(...objs) {
    return objs.reduce((r, o) => ({ ...r, ...o }), {});
}

// BETTER: Object.assign
function merge(...objs) {
    return Object.assign({}, ...objs);
}
```

### 6.12.6. Type Preservation

```javascript
class TypedArray {
    constructor(type, ...values) {
        this.type = type;
        this.values = values;
    }

    map(fn) {
        return new TypedArray(
            this.type,
            ...this.values.map(fn)
        );
    }

    concat(...others) {
        return new TypedArray(
            this.type,
            ...this.values,
            ...others.flatMap(o => o.values)
        );
    }
}
```

### 6.12.7. Lazy Evaluation

```javascript
class LazyArray {
    constructor(generator) {
        this.generator = generator;
    }

    *[Symbol.iterator]() {
        yield* this.generator();
    }

    map(fn) {
        const gen = this.generator;
        return new LazyArray(function*() {
            for (const item of gen()) {
                yield fn(item);
            }
        });
    }

    take(n) {
        const gen = this.generator;
        return new LazyArray(function*() {
            let count = 0;
            for (const item of gen()) {
                if (count++ >= n) break;
                yield item;
            }
        });
    }

    toArray() {
        return [...this];
    }
}
```

## 6.13. Exercises

### Exercise 1 (Dễ): Merge Arrays

```javascript
// Merge ba mảng thành một
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const arr3 = [7, 8, 9];

// Giải pháp sử dụng spread
```

### Exercise 2 (Dễ): Clone Object

```javascript
// Clone object và update property
const user = { name: 'John', age: 30, city: 'NYC' };

// Tạo newUser với age = 31
```

### Exercise 3 (Dễ): Rest Parameters

```javascript
// Hàm tính tổng số lượng arguments không giới hạn
function sum(...numbers) {
    // Code của bạn
}

console.log(sum(1, 2, 3, 4, 5));  // 15
```

### Exercise 4 (Dễ): Spread String

```javascript
// Chuyển string thành mảng và đảo ngược
const str = 'hello';

// Sử dụng spread và reverse
```

### Exercise 5 (Trung bình): Remove Duplicates

```javascript
// Loại bỏ phần tử trùng lặp
function removeDuplicates(arr) {
    // Code của bạn
}

console.log(removeDuplicates([1, 2, 2, 3, 3, 4]));
// [1, 2, 3, 4]
```

### Exercise 6 (Trung bình): Merge Nested Objects

```javascript
// Merge objects có nested properties
const obj1 = {
    name: 'John',
    address: { city: 'NYC', country: 'USA' }
};

const obj2 = {
    age: 30,
    address: { city: 'LA', zip: '90001' }
};

// Merge sao cho:
// { name: 'John', age: 30,
//   address: { city: 'LA', country: 'USA', zip: '90001' } }
```

### Exercise 7 (Trung bình): First and Rest

```javascript
// Tách phần tử đầu và phần còn lại
function firstAndRest(arr) {
    // Destructuring với rest
    // Return { first, rest }
}

console.log(firstAndRest([1, 2, 3, 4, 5]));
```

### Exercise 8 (Trung bình): Function Composition

```javascript
// Tạo hàm compose nhận nhiều functions
function compose(...fns) {
    // Code của bạn
}

const add1 = x => x + 1;
const double = x => x * 2;
const square = x => x * x;

const composed = compose(square, double, add1);
console.log(composed(5));  // 144
```

### Exercise 9 (Trung bình): Conditional Merge

```javascript
// Merge objects với điều kiện
function mergeIf(target, source, condition) {
    // Chỉ merge nếu condition = true
}

const user = { name: 'John' };
mergeIf(user, { age: 30 }, true);
```

### Exercise 10 (Khó): Deep Clone

```javascript
// Deep clone object
function deepClone(obj) {
    // Clone tất cả nested objects
    // Xử lý arrays và objects
}

const original = {
    name: 'John',
    address: {
        city: 'NYC',
        coords: { lat: 40, lng: -74 }
    },
    hobbies: ['reading', 'gaming']
};

const cloned = deepClone(original);
```

### Exercise 11 (Khó): Array Chunking

```javascript
// Chia mảng thành chunks
function chunk(arr, size) {
    // Sử dụng spread và slice
}

console.log(chunk([1, 2, 3, 4, 5, 6, 7], 3));
// [[1, 2, 3], [4, 5, 6], [7]]
```

### Exercise 12 (Khó): Curry with Rest

```javascript
// Curry function với rest parameters
function curry(fn) {
    // Nhận nhiều lần arguments
    // Gọi fn khi đủ parameters
}

function add(a, b, c) {
    return a + b + c;
}

const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3));     // 6
console.log(curriedAdd(1, 2)(3));     // 6
```

---

**Kết luận:** Spread và Rest operators là công cụ mạnh mẽ trong ES6, giúp code ngắn gọn và dễ đọc hơn. Sử dụng spread để copy/merge, rest để collect parameters. Hiểu rõ shallow vs deep copy và các edge cases để tránh bugs.

**Chương tiếp theo:** Classes
