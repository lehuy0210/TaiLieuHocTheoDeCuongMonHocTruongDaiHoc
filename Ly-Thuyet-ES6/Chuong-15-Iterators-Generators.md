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

## 15.10. Exercises

### Exercise 1: Fibonacci Generator

```javascript
// Create Fibonacci generator
function* fibonacci() {
    // Your code
}

console.log(take(10, fibonacci()));
// [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Exercise 2: Custom Range

```javascript
// Create range generator with step
function* range(start, end, step) {
    // Your code
}

console.log([...range(0, 10, 2)]);  // [0, 2, 4, 6, 8, 10]
```

### Exercise 3: Flatten Array

```javascript
// Create generator to flatten nested array
function* flatten(arr) {
    // Your code
}

const nested = [1, [2, [3, 4]], 5];
console.log([...flatten(nested)]);  // [1, 2, 3, 4, 5]
```

---

**Kết luận:** Iterators và Generators cung cấp cách powerful để làm việc với sequences, lazy evaluation, và async iteration. Hữu ích cho performance và memory efficiency.

**Hoàn thành tất cả chương ES6!**
