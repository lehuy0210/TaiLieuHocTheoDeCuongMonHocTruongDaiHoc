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

## 6.9. Exercises

### Exercise 1: Combine Arrays

```javascript
// Combine these arrays without mutating originals
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
// Result: [1, 2, 3, 4, 5, 6]
```

### Exercise 2: Update Object

```javascript
// Update user age without mutating original
const user = { name: 'John', age: 30 };
// Create updated user with age 31
```

### Exercise 3: Flexible Function

```javascript
// Create a function that finds the average of any number of arguments
function average(/* your parameters */) {
    // Your code
}

average(1, 2, 3);     // 2
average(10, 20);      // 15
average(5);           // 5
```

### Exercise 4: Remove Element

```javascript
// Remove element at index from array (immutably)
const removeAt = (arr, index) => {
    // Your code using spread
};

const arr = [1, 2, 3, 4, 5];
removeAt(arr, 2);  // [1, 2, 4, 5]
```

---

**Kết luận:** Spread và Rest operators là công cụ mạnh mẽ để làm việc với arrays, objects, và function parameters. Giúp viết code immutable và linh hoạt hơn.

**Chương tiếp theo:** Classes
