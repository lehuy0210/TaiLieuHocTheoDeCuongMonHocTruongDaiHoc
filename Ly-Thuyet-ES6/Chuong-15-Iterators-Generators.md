# CHƯƠNG 15: ITERATORS & GENERATORS

## 15.1. Iterators

### 15.1.1. Giới thiệu Iterators

Iterator là object với method `next()` trả về `{ value, done }`.

```javascript
// Manual iterator
const iterator = {
    current: 0,
    last: 3,

    next() {
        if (this.current <= this.last) {
            return { value: this.current++, done: false };
        }
        return { done: true };
    }
};

console.log(iterator.next());  // { value: 0, done: false }
console.log(iterator.next());  // { value: 1, done: false }
console.log(iterator.next());  // { value: 2, done: false }
console.log(iterator.next());  // { value: 3, done: false }
console.log(iterator.next());  // { done: true }
```

### 15.1.2. Iterable Protocol

Object là iterable nếu có method `[Symbol.iterator]()`.

```javascript
const iterable = {
    data: [1, 2, 3],

    [Symbol.iterator]() {
        let index = 0;
        const data = this.data;

        return {
            next() {
                if (index < data.length) {
                    return { value: data[index++], done: false };
                }
                return { done: true };
            }
        };
    }
};

// Can use for...of
for (const value of iterable) {
    console.log(value);  // 1, 2, 3
}

// Can spread
console.log([...iterable]);  // [1, 2, 3]

// Can destructure
const [first, second] = iterable;
```

### 15.1.3. Built-in Iterables

```javascript
// Arrays
const arr = [1, 2, 3];
for (const val of arr) { }

// Strings
const str = 'hello';
for (const char of str) { }

// Maps
const map = new Map([['a', 1], ['b', 2]]);
for (const [key, value] of map) { }

// Sets
const set = new Set([1, 2, 3]);
for (const val of set) { }

// NodeList
const divs = document.querySelectorAll('div');
for (const div of divs) { }
```

## 15.2. Generators

### 15.2.1. Generator Functions

Generator function (function*) trả về generator object (iterator).

```javascript
function* generatorFunction() {
    yield 1;
    yield 2;
    yield 3;
}

const gen = generatorFunction();

console.log(gen.next());  // { value: 1, done: false }
console.log(gen.next());  // { value: 2, done: false }
console.log(gen.next());  // { value: 3, done: false }
console.log(gen.next());  // { done: true }
```

### 15.2.2. Yield

```javascript
function* counter() {
    let count = 0;
    while (true) {
        yield count++;
    }
}

const gen = counter();
console.log(gen.next().value);  // 0
console.log(gen.next().value);  // 1
console.log(gen.next().value);  // 2
```

### 15.2.3. Iterating Generators

```javascript
function* numbers() {
    yield 1;
    yield 2;
    yield 3;
}

// for...of
for (const num of numbers()) {
    console.log(num);  // 1, 2, 3
}

// Spread
const arr = [...numbers()];  // [1, 2, 3]

// Destructuring
const [a, b, c] = numbers();
```

### 15.2.4. Return in Generators

```javascript
function* gen() {
    yield 1;
    yield 2;
    return 3;  // Final value
    yield 4;   // Never reached
}

const g = gen();
console.log(g.next());  // { value: 1, done: false }
console.log(g.next());  // { value: 2, done: false }
console.log(g.next());  // { value: 3, done: true }
console.log(g.next());  // { value: undefined, done: true }

// for...of doesn't include return value
for (const val of gen()) {
    console.log(val);  // 1, 2 (not 3)
}
```

## 15.3. Generator Methods

### 15.3.1. next(value)

```javascript
function* echo() {
    const input1 = yield 'Waiting for input 1';
    console.log('Got:', input1);

    const input2 = yield 'Waiting for input 2';
    console.log('Got:', input2);
}

const gen = echo();
console.log(gen.next());        // { value: 'Waiting for input 1', done: false }
console.log(gen.next('Hello')); // Got: Hello, { value: 'Waiting for input 2', done: false }
console.log(gen.next('World')); // Got: World, { done: true }
```

### 15.3.2. throw()

```javascript
function* errorHandler() {
    try {
        yield 1;
        yield 2;
    } catch (error) {
        console.log('Caught:', error.message);
    }
    yield 3;
}

const gen = errorHandler();
console.log(gen.next());              // { value: 1, done: false }
console.log(gen.throw(new Error('Oops')));  // Caught: Oops, { value: 3, done: false }
```

### 15.3.3. return()

```javascript
function* gen() {
    yield 1;
    yield 2;
    yield 3;
}

const g = gen();
console.log(g.next());        // { value: 1, done: false }
console.log(g.return('done')); // { value: 'done', done: true }
console.log(g.next());        // { done: true }
```

## 15.4. Yield*

### 15.4.1. Delegating Generators

```javascript
function* gen1() {
    yield 1;
    yield 2;
}

function* gen2() {
    yield* gen1();  // Delegate to gen1
    yield 3;
}

console.log([...gen2()]);  // [1, 2, 3]
```

### 15.4.2. Yield* with Arrays

```javascript
function* gen() {
    yield* [1, 2, 3];
    yield* 'abc';
}

console.log([...gen()]);  // [1, 2, 3, 'a', 'b', 'c']
```

### 15.4.3. Recursive Generators

```javascript
function* flatten(arr) {
    for (const item of arr) {
        if (Array.isArray(item)) {
            yield* flatten(item);
        } else {
            yield item;
        }
    }
}

const nested = [1, [2, [3, 4], 5], 6];
console.log([...flatten(nested)]);  // [1, 2, 3, 4, 5, 6]
```

## 15.5. Practical Examples

### 15.5.1. Range Generator

```javascript
function* range(start, end, step = 1) {
    for (let i = start; i <= end; i += step) {
        yield i;
    }
}

console.log([...range(1, 10)]);       // [1, 2, 3, ..., 10]
console.log([...range(0, 20, 5)]);    // [0, 5, 10, 15, 20]

for (const num of range(1, 5)) {
    console.log(num);  // 1, 2, 3, 4, 5
}
```

### 15.5.2. Infinite Sequence

```javascript
function* fibonacci() {
    let [prev, curr] = [0, 1];
    while (true) {
        yield curr;
        [prev, curr] = [curr, prev + curr];
    }
}

// Take first 10
function take(n, iterable) {
    const result = [];
    for (const item of iterable) {
        if (result.length >= n) break;
        result.push(item);
    }
    return result;
}

console.log(take(10, fibonacci()));
// [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### 15.5.3. ID Generator

```javascript
function* idGenerator() {
    let id = 1;
    while (true) {
        yield id++;
    }
}

const ids = idGenerator();
console.log(ids.next().value);  // 1
console.log(ids.next().value);  // 2
console.log(ids.next().value);  // 3
```

### 15.5.4. Tree Traversal

```javascript
class TreeNode {
    constructor(value, children = []) {
        this.value = value;
        this.children = children;
    }

    *[Symbol.iterator]() {
        yield this.value;
        for (const child of this.children) {
            yield* child;
        }
    }
}

const tree = new TreeNode(1, [
    new TreeNode(2, [
        new TreeNode(4),
        new TreeNode(5)
    ]),
    new TreeNode(3)
]);

console.log([...tree]);  // [1, 2, 4, 5, 3]
```

### 15.5.5. Pagination

```javascript
async function* fetchPages(url) {
    let page = 1;
    let hasMore = true;

    while (hasMore) {
        const response = await fetch(`${url}?page=${page}`);
        const data = await response.json();

        yield data.items;

        hasMore = data.hasMore;
        page++;
    }
}

// Usage
(async () => {
    for await (const items of fetchPages('/api/items')) {
        console.log('Page items:', items);
    }
})();
```

### 15.5.6. Custom Iterable Class

```javascript
class Collection {
    constructor(data) {
        this.data = data;
    }

    *[Symbol.iterator]() {
        for (const item of this.data) {
            yield item;
        }
    }

    *filter(predicate) {
        for (const item of this.data) {
            if (predicate(item)) {
                yield item;
            }
        }
    }

    *map(fn) {
        for (const item of this.data) {
            yield fn(item);
        }
    }
}

const collection = new Collection([1, 2, 3, 4, 5]);

// Filter
const evens = [...collection.filter(x => x % 2 === 0)];
console.log(evens);  // [2, 4]

// Map
const doubled = [...collection.map(x => x * 2)];
console.log(doubled);  // [2, 4, 6, 8, 10]
```

## 15.6. Async Generators

### 15.6.1. Basic Async Generator

```javascript
async function* asyncGenerator() {
    yield await Promise.resolve(1);
    yield await Promise.resolve(2);
    yield await Promise.resolve(3);
}

(async () => {
    for await (const value of asyncGenerator()) {
        console.log(value);  // 1, 2, 3
    }
})();
```

### 15.6.2. Async Iteration

```javascript
async function* fetchUsers() {
    const ids = [1, 2, 3, 4, 5];

    for (const id of ids) {
        const response = await fetch(`/api/users/${id}`);
        yield await response.json();
    }
}

(async () => {
    for await (const user of fetchUsers()) {
        console.log('User:', user);
    }
})();
```

### 15.6.3. Stream Processing

```javascript
async function* readLines(url) {
    const response = await fetch(url);
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    let buffer = '';

    while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
            yield line;
        }
    }

    if (buffer) yield buffer;
}
```

## 15.7. Advanced Patterns

### 15.7.1. Pipeline

```javascript
function* map(iterable, fn) {
    for (const item of iterable) {
        yield fn(item);
    }
}

function* filter(iterable, predicate) {
    for (const item of iterable) {
        if (predicate(item)) {
            yield item;
        }
    }
}

function* take(iterable, n) {
    let count = 0;
    for (const item of iterable) {
        if (count++ >= n) break;
        yield item;
    }
}

// Usage
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const result = take(
    filter(
        map(numbers, x => x * 2),
        x => x > 5
    ),
    3
);

console.log([...result]);  // [6, 8, 10]
```

### 15.7.2. Lazy Evaluation

```javascript
function* lazyMap(iterable, fn) {
    for (const item of iterable) {
        console.log('Mapping:', item);
        yield fn(item);
    }
}

const nums = [1, 2, 3, 4, 5];
const mapped = lazyMap(nums, x => x * 2);

// Not executed yet
console.log('Starting iteration');

// Executes lazily
for (const val of mapped) {
    console.log('Got:', val);
    if (val >= 6) break;  // Stops early
}
```

### 15.7.3. Co-routines

```javascript
function* ping() {
    console.log('ping');
    yield* pong();
    console.log('ping again');
}

function* pong() {
    console.log('pong');
}

[...ping()];
// ping
// pong
// ping again
```

## 15.8. Best Practices

### 15.8.1. Use Generators for Sequences

```javascript
// Good: Generator for sequence
function* sequence(start, end) {
    for (let i = start; i <= end; i++) {
        yield i;
    }
}

// vs Array (memory intensive for large ranges)
function sequenceArray(start, end) {
    return Array.from({ length: end - start + 1 }, (_, i) => start + i);
}
```

### 15.8.2. Lazy Evaluation

```javascript
// Good: Lazy (only compute what's needed)
function* lazyFilter(iterable, predicate) {
    for (const item of iterable) {
        if (predicate(item)) yield item;
    }
}

// vs Eager (computes everything upfront)
function eagerFilter(array, predicate) {
    return array.filter(predicate);
}
```

### 15.8.3. Infinite Sequences

```javascript
// Good: Generator can represent infinite sequences
function* naturalNumbers() {
    let n = 1;
    while (true) {
        yield n++;
    }
}

// Array can't represent infinite sequences
```

## 15.9. Common Mistakes

### 15.9.1. Reusing Generators

```javascript
function* gen() {
    yield 1;
    yield 2;
}

const g = gen();
console.log([...g]);  // [1, 2]
console.log([...g]);  // [] (exhausted!)

// Create new generator each time
console.log([...gen()]);  // [1, 2]
console.log([...gen()]);  // [1, 2]
```

### 15.9.2. Forgetting yield*

```javascript
function* wrong() {
    [1, 2, 3];  // Doesn't yield anything
}

function* correct() {
    yield* [1, 2, 3];  // Yields all elements
}
```

### 15.9.3. Mixing Async and Sync

```javascript
// Wrong: Can't use await in regular generator
function* wrong() {
    yield await fetch('/api');  // SyntaxError
}

// Correct: Use async generator
async function* correct() {
    yield await fetch('/api');
}
```

## 15.8. Real-world Use Cases

### Use Case 1: Data Stream Processing

```javascript
async function* readDataStream(url) {
    const response = await fetch(url);
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    try {
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            yield decoder.decode(value, { stream: true });
        }
    } finally {
        reader.releaseLock();
    }
}

// Usage
(async () => {
    for await (const chunk of readDataStream('/api/data')) {
        console.log('Processing chunk:', chunk);
        // Process each chunk as it arrives
    }
})();
```

### Use Case 2: Pagination with Generators

```javascript
async function* getPaginatedItems(apiUrl, pageSize = 20) {
    let page = 0;
    let hasMore = true;

    while (hasMore) {
        const url = `${apiUrl}?page=${page}&limit=${pageSize}`;
        const response = await fetch(url);
        const data = await response.json();

        for (const item of data.items) {
            yield item;
        }

        hasMore = data.hasMore;
        page++;
    }
}

// Usage
(async () => {
    for await (const item of getPaginatedItems('/api/products')) {
        console.log('Product:', item);
        // Process each product
    }
})();
```

### Use Case 3: Lazy Sequence Evaluation

```javascript
function* naturalNumbers() {
    let n = 1;
    while (true) {
        yield n++;
    }
}

function* filter(iterable, predicate) {
    for (const item of iterable) {
        if (predicate(item)) {
            yield item;
        }
    }
}

function* map(iterable, transform) {
    for (const item of iterable) {
        yield transform(item);
    }
}

function* take(iterable, count) {
    let taken = 0;
    for (const item of iterable) {
        if (taken++ >= count) break;
        yield item;
    }
}

// Lazy evaluation chain
const result = take(
    map(
        filter(naturalNumbers(), x => x % 2 === 0),
        x => x * x
    ),
    5
);

console.log([...result]); // [4, 16, 36, 64, 100]
```

### Use Case 4: Tree Traversal Generators

```javascript
class TreeNode {
    constructor(value, left = null, right = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    *dfs() {
        yield this.value;
        if (this.left) yield* this.left.dfs();
        if (this.right) yield* this.right.dfs();
    }

    *bfs() {
        const queue = [this];
        while (queue.length > 0) {
            const node = queue.shift();
            yield node.value;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }
}

// Usage
const root = new TreeNode(
    1,
    new TreeNode(2, new TreeNode(4), new TreeNode(5)),
    new TreeNode(3)
);

console.log([...root.dfs()]); // [1, 2, 4, 5, 3] (DFS)
console.log([...root.bfs()]); // [1, 2, 3, 4, 5] (BFS)
```

### Use Case 5: Infinite Sequence Generators

```javascript
function* fibonacci() {
    let [a, b] = [0, 1];
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}

function* powers(base) {
    let power = 1;
    while (true) {
        yield Math.pow(base, power++);
    }
}

function* cycleArray(arr) {
    let index = 0;
    while (true) {
        yield arr[index];
        index = (index + 1) % arr.length;
    }
}

// Usage
const fib = fibonacci();
console.log(fib.next().value); // 0
console.log(fib.next().value); // 1
console.log(fib.next().value); // 1
console.log(fib.next().value); // 2

// Using take helper
function take(n, iterable) {
    const result = [];
    for (const item of iterable) {
        if (result.length >= n) break;
        result.push(item);
    }
    return result;
}

console.log(take(10, fibonacci())); // First 10 fibonacci numbers
```

## 15.9. Tips & Tricks

### Tip 1: Combining Generators with Array Methods

```javascript
function* range(start, end) {
    for (let i = start; i < end; i++) {
        yield i;
    }
}

// Convert to array for array methods
const result = [...range(1, 10)]
    .filter(x => x % 2 === 0)
    .map(x => x * 2);

console.log(result); // [4, 8, 12, 16, 18]

// Or use lazy operations
function* filter(iterable, fn) {
    for (const item of iterable) {
        if (fn(item)) yield item;
    }
}

function* map(iterable, fn) {
    for (const item of iterable) {
        yield fn(item);
    }
}

const lazyResult = [...map(filter(range(1, 10), x => x % 2 === 0), x => x * 2)];
console.log(lazyResult); // [4, 8, 12, 16, 18]
```

### Tip 2: Generator as State Machine

```javascript
function* lightSwitch() {
    let state = 'OFF';
    while (true) {
        const action = yield state;
        if (action === 'TOGGLE') {
            state = state === 'OFF' ? 'ON' : 'OFF';
        }
    }
}

const light = lightSwitch();
console.log(light.next().value); // 'OFF'
console.log(light.next('TOGGLE').value); // 'ON'
console.log(light.next('TOGGLE').value); // 'OFF'
```

### Tip 3: Generator Memoization

```javascript
function memoizedGenerator(fn) {
    const cache = new Map();

    return function* (...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            yield* cache.get(key);
        } else {
            const result = yield* fn(...args);
            cache.set(key, [result]);
        }
    };
}

function* expensive(n) {
    console.log(`Computing ${n}`);
    yield n * 2;
}

const memoized = memoizedGenerator(expensive);
console.log([...memoized(5)]); // Computing 5, [10]
console.log([...memoized(5)]); // [10] - from cache
```

### Tip 4: Async Generator for Real-time Updates

```javascript
async function* watchFile(filename) {
    let lastContent = '';

    while (true) {
        const response = await fetch(`/api/file/${filename}`);
        const content = await response.text();

        if (content !== lastContent) {
            yield { filename, content };
            lastContent = content;
        }

        await new Promise(resolve => setTimeout(resolve, 1000));
    }
}

// Usage
(async () => {
    for await (const update of watchFile('config.json')) {
        console.log('File updated:', update);
    }
})();
```

### Tip 5: Generator Composition

```javascript
function* A() {
    yield 1;
    yield 2;
}

function* B() {
    yield 3;
    yield 4;
}

function* C() {
    yield 5;
    yield 6;
}

function* compose(...generators) {
    for (const gen of generators) {
        yield* gen();
    }
}

console.log([...compose(A, B, C)]); // [1, 2, 3, 4, 5, 6]
```

### Tip 6: Generator with try-finally

```javascript
function* resource() {
    const res = setupResource();
    try {
        yield res;
    } finally {
        cleanup(res);
    }
}

// Ensure cleanup happens
for (const res of resource()) {
    console.log('Using resource:', res);
    break; // Early exit still triggers finally
}
```

### Tip 7: Two-way Communication with Generators

```javascript
function* echo() {
    while (true) {
        const input = yield;
        console.log('Received:', input);
    }
}

const gen = echo();
gen.next(); // Start generator
gen.next('Hello'); // Received: Hello
gen.next('World'); // Received: World
```

### Tip 8: Delegating Errors in Generators

```javascript
function* errorHandler() {
    try {
        yield 1;
        yield 2;
    } catch (error) {
        console.log('Caught:', error.message);
        yield 'error handled';
    }
}

const gen = errorHandler();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.throw(new Error('Oops'))); // Caught: Oops
// { value: 'error handled', done: false }
```

### Tip 9: Generator with Sentinel Value

```javascript
const DONE = Symbol('done');

function* countdown(n) {
    while (n > 0) {
        yield n--;
    }
    yield DONE;
}

let result;
do {
    result = countdown(3).next();
    if (result.value !== DONE) {
        console.log(result.value);
    }
} while (result.value !== DONE);
```

### Tip 10: Infinite Repeating Generator

```javascript
function* repeat(value) {
    while (true) {
        yield value;
    }
}

function* take(iterable, n) {
    let count = 0;
    for (const item of iterable) {
        if (count++ >= n) break;
        yield item;
    }
}

console.log([...take(repeat('x'), 5)]); // ['x', 'x', 'x', 'x', 'x']
```

## 15.10. Common Mistakes

### Mistake 1: Arrow Functions in Generators

```javascript
// WRONG: Can't use arrow function syntax
const gen = () => {
    yield 1; // SyntaxError
};

// RIGHT: Use function*
function* gen() {
    yield 1;
}
```

### Mistake 2: Forgetting yield in Generator

```javascript
// WRONG: Function without yield
function* gen() {
    return [1, 2, 3]; // Not yielding items
}

console.log([...gen()]); // [] - empty!

// RIGHT: Use yield for each item
function* gen() {
    yield 1;
    yield 2;
    yield 3;
}

console.log([...gen()]); // [1, 2, 3]
```

### Mistake 3: Reusing Generator

```javascript
function* gen() {
    yield 1;
    yield 2;
}

const g = gen();
console.log([...g]); // [1, 2]
console.log([...g]); // [] - exhausted!

// RIGHT: Create new generator each time
console.log([...gen()]); // [1, 2]
console.log([...gen()]); // [1, 2]
```

### Mistake 4: Mixing await and yield

```javascript
// WRONG: Regular generator can't use await
function* wrong() {
    yield await fetch('/api'); // SyntaxError
}

// RIGHT: Use async generator
async function* correct() {
    yield await fetch('/api');
}
```

### Mistake 5: Return Value in for...of

```javascript
function* gen() {
    yield 1;
    yield 2;
    return 3; // Return value
}

// WRONG: return value is ignored in for...of
for (const val of gen()) {
    console.log(val); // 1, 2 (not 3!)
}

// RIGHT: Use manual iteration to get return
const g = gen();
let result;
while (!(result = g.next()).done) {
    console.log(result.value);
}
console.log('Return:', result.value); // Return: 3
```

### Mistake 6: Generator without Star

```javascript
// WRONG: Regular function
function gen() {
    yield 1; // SyntaxError
}

// RIGHT: Add star
function* gen() {
    yield 1;
}
```

### Mistake 7: Trying to Iterate Non-Iterator

```javascript
// WRONG: Object without Symbol.iterator
const obj = { a: 1, b: 2 };
for (const x of obj) { } // TypeError

// RIGHT: Make it iterable
obj[Symbol.iterator] = function* () {
    for (const key in this) {
        yield this[key];
    }
};

for (const x of obj) {
    console.log(x); // 1, 2
}
```

### Mistake 8: Async Generator Return

```javascript
async function* gen() {
    yield 1;
    yield 2;
    return 3; // Return works differently
}

(async () => {
    for await (const val of gen()) {
        console.log(val); // 1, 2 (not 3!)
    }
})();
```

### Mistake 9: Generator Performance Issues

```javascript
// WRONG: Converting large generator to array
function* largeSequence() {
    for (let i = 0; i < 1000000; i++) {
        yield i;
    }
}

const arr = [...largeSequence()]; // Uses lots of memory!

// RIGHT: Use generator directly
function take(n, iterable) {
    const result = [];
    for (const item of iterable) {
        if (result.length >= n) break;
        result.push(item);
    }
    return result;
}

const first100 = take(100, largeSequence()); // Efficient
```

### Mistake 10: Generator Context Loss

```javascript
// WRONG: Lost context
const obj = {
    items: [1, 2, 3],
    *gen() {
        for (const item of this.items) {
            yield item;
        }
    }
};

const gen = obj.gen();
delete obj.items;
[...gen]; // Error: can't find items

// RIGHT: Capture context
const obj = {
    items: [1, 2, 3],
    *gen() {
        const items = this.items;
        for (const item of items) {
            yield item;
        }
    }
};
```

## 15.11. Troubleshooting Issues

### Issue 1: Generator Not Iterable Directly

**Problem:**
```javascript
function* gen() {
    yield 1;
    yield 2;
}

const g = gen;
for (const x of g) { } // TypeError: not iterable
```

**Solution:**
```javascript
function* gen() {
    yield 1;
    yield 2;
}

const g = gen(); // Call function to get generator
for (const x of g) {
    console.log(x); // 1, 2
}
```

### Issue 2: async/await with Generator

**Problem:**
```javascript
function* fetchData() {
    const data = await fetch('/api'); // SyntaxError
    yield data;
}
```

**Solution:**
```javascript
async function* fetchData() {
    const response = await fetch('/api');
    yield await response.json();
}

(async () => {
    for await (const data of fetchData()) {
        console.log(data);
    }
})();
```

### Issue 3: Generator Memory Leak

**Problem:**
```javascript
function* generateLargeObjects() {
    while (true) {
        yield new Array(1000000); // Large objects
    }
}

const gen = generateLargeObjects();
for (let i = 0; i < 10000; i++) {
    gen.next(); // Keeps creating large objects
}
```

**Solution:**
```javascript
function* generateLargeObjects() {
    while (true) {
        yield new Array(100); // Smaller objects
    }
}

// Or use WeakMap for cleanup
const created = new WeakMap();
function* trackObjects() {
    let obj = {};
    while (true) {
        yield obj;
        created.set(obj, true);
        obj = null; // Allow GC
        obj = {};
    }
}
```

### Issue 4: Nested Generators

**Problem:**
```javascript
function* outer() {
    const inner = function* () {
        yield 1;
        yield 2;
    };
    // inner is not called!
}

[...outer()]; // []
```

**Solution:**
```javascript
function* outer() {
    const inner = function* () {
        yield 1;
        yield 2;
    };
    yield* inner(); // Delegate to inner
}

[...outer()]; // [1, 2]
```

### Issue 5: Generator State Management

**Problem:**
```javascript
function* counter() {
    let count = 0;
    while (true) {
        yield count++;
    }
}

const c1 = counter();
const c2 = counter();

c1.next(); // 0
c2.next(); // Also 0 - separate state
```

**Solution:**
```javascript
function createCounter() {
    return function* counter() {
        let count = 0;
        while (true) {
            yield count++;
        }
    };
}

const c1 = createCounter()();
const c2 = createCounter()();

console.log(c1.next().value); // 0
console.log(c1.next().value); // 1
console.log(c2.next().value); // 0 - separate
```

### Issue 6: Generator with Complex Yields

**Problem:**
```javascript
function* complexYield() {
    yield { x: 1 };
    yield { x: 2 };
}

// Mutating yielded objects affects others
const gen = complexYield();
const obj1 = gen.next().value;
obj1.x = 999;

const obj2 = gen.next().value;
console.log(obj2.x); // Still 2, but confusing
```

**Solution:**
```javascript
function* complexYield() {
    yield Object.freeze({ x: 1 });
    yield Object.freeze({ x: 2 });
}

const gen = complexYield();
const obj1 = gen.next().value;
// obj1.x = 999; // Error in strict mode

const obj2 = gen.next().value;
console.log(obj2.x); // 2 (safe)
```

### Issue 7: Performance of yield*

**Problem:**
```javascript
function* range(n) {
    for (let i = 0; i < n; i++) {
        yield i;
    }
}

function* nested(n) {
    for (let i = 0; i < n; i++) {
        for (const x of range(n)) {
            yield x;
        }
    }
}

// Inefficient: creates multiple generators
[...nested(100)].length;
```

**Solution:**
```javascript
function* range(n) {
    for (let i = 0; i < n; i++) {
        yield i;
    }
}

function* nested(n) {
    for (let i = 0; i < n; i++) {
        yield* range(n); // More efficient
    }
}

[...nested(100)].length; // Much faster
```

### Issue 8: Generator with External Dependencies

**Problem:**
```javascript
let counter = 0;

function* gen() {
    yield ++counter;
    yield ++counter;
}

console.log([...gen()]); // [1, 2]
console.log([...gen()]); // [3, 4] - counter modified globally
```

**Solution:**
```javascript
function createGen() {
    let counter = 0;
    return function* gen() {
        yield ++counter;
        yield ++counter;
    };
}

const gen1 = createGen();
const gen2 = createGen();

console.log([...gen1()]); // [1, 2]
console.log([...gen2()]); // [1, 2] - isolated
```

### Issue 9: Controlling Generator Execution

**Problem:**
```javascript
function* gen() {
    console.log('Start');
    yield 1;
    console.log('Middle');
    yield 2;
    console.log('End');
}

const g = gen();
// Nothing logged yet - generator not started
g.next(); // Logs "Start"
```

**Solution:**
```javascript
function* gen() {
    console.log('Start');
    yield 1;
    console.log('Middle');
    yield 2;
    console.log('End');
}

const g = gen();
console.log(g.next()); // { value: 1, done: false }
console.log(g.next()); // { value: 2, done: false }
console.log(g.next()); // { value: undefined, done: true }
```

### Issue 10: Async Generator Edge Cases

**Problem:**
```javascript
async function* gen() {
    yield Promise.resolve(1); // Doesn't await
    yield await Promise.resolve(2); // Awaits
}

(async () => {
    for await (const x of gen()) {
        console.log(typeof x); // Promise vs number
    }
})();
```

**Solution:**
```javascript
async function* gen() {
    yield await Promise.resolve(1); // Always await
    yield await Promise.resolve(2);
}

(async () => {
    for await (const x of gen()) {
        console.log(typeof x); // Both numbers
    }
})();
```

## 15.12. Advanced Topics

### Advanced Topic 1: Custom Iterator Class

```javascript
class CountUp {
    constructor(max) {
        this.max = max;
    }

    [Symbol.iterator]() {
        let count = 0;
        const max = this.max;

        return {
            next: () => {
                if (count < max) {
                    return { value: count++, done: false };
                }
                return { done: true };
            }
        };
    }

    *[Symbol.generator]() {
        for (let i = 0; i < this.max; i++) {
            yield i;
        }
    }
}

const counter = new CountUp(5);
console.log([...counter]); // [0, 1, 2, 3, 4]
```

### Advanced Topic 2: Transducers Pattern

```javascript
const mapping = (fn) => (xf) => ({
    '@@transducer/init': () => xf['@@transducer/init'](),
    '@@transducer/result': (v) => xf['@@transducer/result'](v),
    '@@transducer/step': (result, input) => xf['@@transducer/step'](result, fn(input))
});

const filtering = (predicate) => (xf) => ({
    '@@transducer/init': () => xf['@@transducer/init'](),
    '@@transducer/result': (v) => xf['@@transducer/result'](v),
    '@@transducer/step': (result, input) =>
        predicate(input) ? xf['@@transducer/step'](result, input) : result
});

function compose(...fns) {
    return (x) => fns.reduceRight((acc, fn) => fn(acc), x);
}

const transform = compose(
    mapping(x => x * 2),
    filtering(x => x > 5)
);

// Use with reduce
const xf = transform({
    '@@transducer/init': () => [],
    '@@transducer/result': (v) => v,
    '@@transducer/step': (result, input) => [...result, input]
});

console.log([1, 2, 3, 4, 5].reduce((r, x) => xf['@@transducer/step'](r, x), []));
```

### Advanced Topic 3: Observable-like Pattern

```javascript
class Observable {
    constructor(subscribe) {
        this.subscribe = subscribe;
    }

    static from(iterable) {
        return new Observable((observer) => {
            for (const item of iterable) {
                observer.next(item);
            }
            observer.complete();
        });
    }

    *[Symbol.iterator]() {
        const items = [];
        this.subscribe({
            next: (x) => items.push(x),
            complete: () => {}
        });
        yield* items;
    }

    map(fn) {
        return new Observable((observer) => {
            this.subscribe({
                next: (x) => observer.next(fn(x)),
                complete: () => observer.complete()
            });
        });
    }

    filter(predicate) {
        return new Observable((observer) => {
            this.subscribe({
                next: (x) => {
                    if (predicate(x)) observer.next(x);
                },
                complete: () => observer.complete()
            });
        });
    }
}

const obs = Observable.from([1, 2, 3, 4, 5])
    .filter(x => x % 2 === 0)
    .map(x => x * 2);

console.log([...obs]); // [4, 8]
```

### Advanced Topic 4: Generator-based Task Runner

```javascript
function* mainTask() {
    const result1 = yield fetch('/api/user/1').then(r => r.json());
    console.log('User:', result1);

    const result2 = yield fetch(`/api/posts/${result1.id}`).then(r => r.json());
    console.log('Posts:', result2);

    return { user: result1, posts: result2 };
}

function runGenerator(generatorFunc) {
    const iterator = generatorFunc();

    function handle(result) {
        if (result.done) return Promise.resolve(result.value);

        return Promise.resolve(result.value)
            .then((res) => handle(iterator.next(res)))
            .catch((err) => iterator.throw(err));
    }

    return handle(iterator.next());
}

// Usage
runGenerator(mainTask).then((result) => {
    console.log('Final result:', result);
});
```

### Advanced Topic 5: Lazy Map Implementation

```javascript
class LazyMap {
    constructor(source, transform = (x) => x) {
        this.source = source;
        this.transform = transform;
    }

    map(fn) {
        return new LazyMap(this.source, (x) => fn(this.transform(x)));
    }

    filter(predicate) {
        const transform = this.transform;
        return new LazyMap(
            this.source,
            function* (x) {
                const val = transform(x);
                if (predicate(val)) yield val;
            }
        );
    }

    *[Symbol.iterator]() {
        for (const item of this.source) {
            yield this.transform(item);
        }
    }

    toArray() {
        return [...this];
    }
}

const lazy = new LazyMap([1, 2, 3, 4, 5])
    .map(x => x * 2)
    .filter(x => x > 5);

console.log(lazy.toArray()); // [6, 8, 10]
```

## 15.13. Exercises

### Exercise 1 (Dễ): Simple Generator

```javascript
// Create a simple generator that yields 1, 2, 3
function* simpleGen() {
    // Code của bạn
}

console.log([...simpleGen()]); // [1, 2, 3]
```

### Exercise 2 (Dễ): Generator with Argument

```javascript
// Create generator that yields from 1 to n
function* countTo(n) {
    // Code của bạn
}

console.log([...countTo(5)]); // [1, 2, 3, 4, 5]
```

### Exercise 3 (Dễ): Generator with yield*

```javascript
// Flatten two generators using yield*
function* gen1() {
    yield 1;
    yield 2;
}

function* gen2() {
    yield 3;
    yield 4;
}

function* combine() {
    // Use yield* to combine gen1 and gen2
}

console.log([...combine()]); // [1, 2, 3, 4]
```

### Exercise 4 (Dễ): Generator from Array

```javascript
// Create generator that yields from array
function* fromArray(arr) {
    // Code của bạn
}

console.log([...fromArray([10, 20, 30])]); // [10, 20, 30]
```

### Exercise 5 (Trung bình): Fibonacci Generator

```javascript
// Create Fibonacci generator
function* fibonacci(limit) {
    // Yield Fibonacci numbers up to limit
}

console.log([...fibonacci(50)]); // [1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Exercise 6 (Trung bình): Filter Generator

```javascript
// Create generator that yields filtered items
function* filterGen(arr, predicate) {
    // Code của bạn
}

console.log([...filterGen([1, 2, 3, 4, 5], x => x % 2 === 0)]); // [2, 4]
```

### Exercise 7 (Trung bình): Map Generator

```javascript
// Create generator that transforms items
function* mapGen(arr, transform) {
    // Code của bạn
}

console.log([...mapGen([1, 2, 3], x => x * 2)]); // [2, 4, 6]
```

### Exercise 8 (Trung bình): Take Generator

```javascript
// Create generator that takes first n items
function* take(iterable, n) {
    // Code của bạn
}

console.log([...take(range(1, 10), 5)]); // [1, 2, 3, 4, 5]
```

### Exercise 9 (Khó): Flatten Nested Array

```javascript
// Create generator to flatten nested arrays
function* flatten(arr) {
    // Recursive flatten
}

const nested = [1, [2, [3, 4]], 5];
console.log([...flatten(nested)]); // [1, 2, 3, 4, 5]
```

### Exercise 10 (Khó): Async Data Fetcher

```javascript
// Create async generator to fetch paginated data
async function* fetchPages(apiUrl) {
    // Fetch pages of data from API
}

// Usage:
// for await (const page of fetchPages('/api/items')) {
//     console.log(page);
// }
```

### Exercise 11 (Khó): Pipeline Composition

```javascript
// Create composable generator pipeline
function pipe(...generators) {
    // Compose multiple generators
}

const result = pipe(
    range(1, 10),
    arr => filterGen(arr, x => x % 2 === 0),
    arr => mapGen(arr, x => x * 2)
);

console.log([...result]); // [4, 8, 12, 16, 20]
```

### Exercise 12 (Khó): Stateful Generator

```javascript
// Create generator that maintains state
class StatefulGenerator {
    constructor(items) {
        this.items = items;
        this.index = 0;
    }

    *[Symbol.iterator]() {
        // Yield items while maintaining state
    }

    reset() {
        this.index = 0;
    }

    hasNext() {
        return this.index < this.items.length;
    }
}

const gen = new StatefulGenerator([1, 2, 3]);
console.log([...gen]); // [1, 2, 3]
gen.reset();
console.log([...gen]); // [1, 2, 3] again
```

---

**Kết luận:** Iterators và Generators cung cấp cách powerful để làm việc với sequences, lazy evaluation, và async iteration. Hữu ích cho performance và memory efficiency.

**Hoàn thành tất cả chương ES6!**
