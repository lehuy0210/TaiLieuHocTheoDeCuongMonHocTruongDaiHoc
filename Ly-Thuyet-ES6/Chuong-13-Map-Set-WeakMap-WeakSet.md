# CHƯƠNG 13: MAP, SET, WEAKMAP, WEAKSET

## 13.1. Map

### 13.1.1. Giới thiệu Map

Map là collection of key-value pairs, cho phép keys có bất kỳ data type nào.

**Object vs Map:**
```javascript
// Object: Keys are strings/symbols only
const obj = {
    name: 'John',
    1: 'number key becomes string'
};

// Map: Keys can be any type
const map = new Map();
map.set('name', 'John');
map.set(1, 'number key');
map.set({}, 'object key');
map.set([], 'array key');
```

### 13.1.2. Creating Maps

```javascript
// Empty map
const map = new Map();

// From array of pairs
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['active', true]
]);

// From Object.entries()
const obj = { name: 'John', age: 30 };
const map = new Map(Object.entries(obj));
```

### 13.1.3. Basic Operations

```javascript
const map = new Map();

// Set values
map.set('name', 'John');
map.set('age', 30);
map.set('active', true);

// Get values
console.log(map.get('name'));   // "John"
console.log(map.get('age'));    // 30
console.log(map.get('missing')); // undefined

// Check existence
console.log(map.has('name'));    // true
console.log(map.has('missing')); // false

// Delete
map.delete('age');
console.log(map.has('age'));  // false

// Size
console.log(map.size);  // 2

// Clear all
map.clear();
console.log(map.size);  // 0
```

### 13.1.4. Chaining Set

```javascript
const map = new Map()
    .set('name', 'John')
    .set('age', 30)
    .set('active', true);
```

### 13.1.5. Any Type as Key

```javascript
const map = new Map();

// Object as key
const objKey = { id: 1 };
map.set(objKey, 'object value');
console.log(map.get(objKey));  // "object value"

// Function as key
const fnKey = () => {};
map.set(fnKey, 'function value');

// NaN as key (works in Map!)
map.set(NaN, 'NaN value');
console.log(map.get(NaN));  // "NaN value"
```

### 13.1.6. Iteration

```javascript
const map = new Map([
    ['name', 'John'],
    ['age', 30],
    ['active', true]
]);

// for...of
for (const [key, value] of map) {
    console.log(key, value);
}

// forEach
map.forEach((value, key) => {
    console.log(key, value);
});

// Keys
for (const key of map.keys()) {
    console.log(key);
}

// Values
for (const value of map.values()) {
    console.log(value);
}

// Entries
for (const [key, value] of map.entries()) {
    console.log(key, value);
}
```

### 13.1.7. Convert to Array

```javascript
const map = new Map([
    ['name', 'John'],
    ['age', 30]
]);

// To array of entries
const entries = [...map];  // [['name', 'John'], ['age', 30]]
const entries = Array.from(map);

// To array of keys
const keys = [...map.keys()];  // ['name', 'age']

// To array of values
const values = [...map.values()];  // ['John', 30]

// To object
const obj = Object.fromEntries(map);
// { name: 'John', age: 30 }
```

## 13.2. Set

### 13.2.1. Giới thiệu Set

Set là collection of unique values (no duplicates).

```javascript
// Array with duplicates
const arr = [1, 2, 2, 3, 3, 4];

// Set removes duplicates
const set = new Set(arr);
console.log([...set]);  // [1, 2, 3, 4]
```

### 13.2.2. Creating Sets

```javascript
// Empty set
const set = new Set();

// From array
const set = new Set([1, 2, 3, 4, 5]);

// From string (unique characters)
const set = new Set('hello');  // Set {'h', 'e', 'l', 'o'}
```

### 13.2.3. Basic Operations

```javascript
const set = new Set();

// Add values
set.add(1);
set.add(2);
set.add(3);
set.add(2);  // Ignored (duplicate)

// Check existence
console.log(set.has(2));  // true
console.log(set.has(5));  // false

// Delete
set.delete(2);
console.log(set.has(2));  // false

// Size
console.log(set.size);  // 2

// Clear
set.clear();
console.log(set.size);  // 0
```

### 13.2.4. Chaining Add

```javascript
const set = new Set()
    .add(1)
    .add(2)
    .add(3);
```

### 13.2.5. Iteration

```javascript
const set = new Set([1, 2, 3, 4, 5]);

// for...of
for (const value of set) {
    console.log(value);
}

// forEach
set.forEach(value => {
    console.log(value);
});

// values()
for (const value of set.values()) {
    console.log(value);
}

// keys() (same as values for Set)
for (const key of set.keys()) {
    console.log(key);
}
```

### 13.2.6. Convert to Array

```javascript
const set = new Set([1, 2, 3, 4, 5]);

// Spread
const arr = [...set];

// Array.from()
const arr = Array.from(set);
```

### 13.2.7. Set Operations

```javascript
// Union
function union(setA, setB) {
    return new Set([...setA, ...setB]);
}

// Intersection
function intersection(setA, setB) {
    return new Set([...setA].filter(x => setB.has(x)));
}

// Difference
function difference(setA, setB) {
    return new Set([...setA].filter(x => !setB.has(x)));
}

// Symmetric Difference
function symmetricDifference(setA, setB) {
    return new Set([
        ...[...setA].filter(x => !setB.has(x)),
        ...[...setB].filter(x => !setA.has(x))
    ]);
}

const a = new Set([1, 2, 3]);
const b = new Set([3, 4, 5]);

console.log([...union(a, b)]);         // [1, 2, 3, 4, 5]
console.log([...intersection(a, b)]);  // [3]
console.log([...difference(a, b)]);    // [1, 2]
console.log([...symmetricDifference(a, b)]);  // [1, 2, 4, 5]
```

## 13.3. WeakMap

### 13.3.1. Giới thiệu WeakMap

WeakMap giống Map nhưng:
- Keys must be objects (not primitives)
- Keys are weakly referenced (can be garbage collected)
- Not iterable
- No size property

```javascript
const weakMap = new WeakMap();

let obj = { id: 1 };
weakMap.set(obj, 'some data');

console.log(weakMap.get(obj));  // "some data"

// When obj is no longer referenced, it can be garbage collected
obj = null;  // weakMap entry also removed automatically
```

### 13.3.2. WeakMap Operations

```javascript
const weakMap = new WeakMap();
const obj1 = {};
const obj2 = {};

// Set
weakMap.set(obj1, 'value1');
weakMap.set(obj2, 'value2');

// Get
console.log(weakMap.get(obj1));  // "value1"

// Has
console.log(weakMap.has(obj1));  // true

// Delete
weakMap.delete(obj1);
console.log(weakMap.has(obj1));  // false

// Cannot use primitives as keys
// weakMap.set('key', 'value');  // TypeError
```

### 13.3.3. Use Cases

**Private Data:**
```javascript
const privateData = new WeakMap();

class User {
    constructor(name, password) {
        this.name = name;
        privateData.set(this, { password });
    }

    checkPassword(input) {
        return privateData.get(this).password === input;
    }
}

const user = new User('John', 'secret123');
console.log(user.password);  // undefined
console.log(user.checkPassword('secret123'));  // true
```

**Caching:**
```javascript
const cache = new WeakMap();

function process(obj) {
    if (cache.has(obj)) {
        return cache.get(obj);
    }

    const result = expensiveOperation(obj);
    cache.set(obj, result);
    return result;
}
```

**Metadata:**
```javascript
const metadata = new WeakMap();

function addMetadata(element, data) {
    metadata.set(element, data);
}

function getMetadata(element) {
    return metadata.get(element);
}

const div = document.createElement('div');
addMetadata(div, { clicks: 0, created: Date.now() });
```

## 13.4. WeakSet

### 13.4.1. Giới thiệu WeakSet

WeakSet giống Set nhưng:
- Values must be objects
- Weakly referenced
- Not iterable
- No size property

```javascript
const weakSet = new WeakSet();

let obj = { id: 1 };
weakSet.add(obj);

console.log(weakSet.has(obj));  // true

obj = null;  // Can be garbage collected
```

### 13.4.2. WeakSet Operations

```javascript
const weakSet = new WeakSet();
const obj1 = {};
const obj2 = {};

// Add
weakSet.add(obj1);
weakSet.add(obj2);

// Has
console.log(weakSet.has(obj1));  // true

// Delete
weakSet.delete(obj1);
console.log(weakSet.has(obj1));  // false

// Cannot use primitives
// weakSet.add(1);  // TypeError
```

### 13.4.3. Use Cases

**Track Objects:**
```javascript
const processedObjects = new WeakSet();

function process(obj) {
    if (processedObjects.has(obj)) {
        console.log('Already processed');
        return;
    }

    // Process object
    processedObjects.add(obj);
}
```

**Mark Objects:**
```javascript
const disabledElements = new WeakSet();

function disable(element) {
    disabledElements.add(element);
    element.setAttribute('disabled', true);
}

function isDisabled(element) {
    return disabledElements.has(element);
}
```

## 13.5. Practical Examples

### 13.5.1. Counting Occurrences

```javascript
function countOccurrences(arr) {
    const map = new Map();

    for (const item of arr) {
        map.set(item, (map.get(item) || 0) + 1);
    }

    return map;
}

const arr = ['a', 'b', 'a', 'c', 'b', 'a'];
const counts = countOccurrences(arr);
// Map { 'a' => 3, 'b' => 2, 'c' => 1 }
```

### 13.5.2. Grouping

```javascript
function groupBy(arr, key) {
    const map = new Map();

    for (const item of arr) {
        const groupKey = item[key];
        if (!map.has(groupKey)) {
            map.set(groupKey, []);
        }
        map.get(groupKey).push(item);
    }

    return map;
}

const users = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 },
    { name: 'Bob', age: 30 }
];

const byAge = groupBy(users, 'age');
```

### 13.5.3. Unique Values

```javascript
function getUnique(arr) {
    return [...new Set(arr)];
}

console.log(getUnique([1, 2, 2, 3, 3, 4]));  // [1, 2, 3, 4]
```

### 13.5.4. LRU Cache

```javascript
class LRUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.cache = new Map();
    }

    get(key) {
        if (!this.cache.has(key)) return -1;

        const value = this.cache.get(key);
        this.cache.delete(key);
        this.cache.set(key, value);  // Move to end
        return value;
    }

    put(key, value) {
        if (this.cache.has(key)) {
            this.cache.delete(key);
        }

        this.cache.set(key, value);

        if (this.cache.size > this.capacity) {
            const firstKey = this.cache.keys().next().value;
            this.cache.delete(firstKey);
        }
    }
}
```

## 13.6. Performance Comparison

| Operation | Object | Map | Set |
|-----------|---------|-----|-----|
| Add/Set | O(1) | O(1) | O(1) |
| Get | O(1) | O(1) | - |
| Has | O(1) | O(1) | O(1) |
| Delete | O(1) | O(1) | O(1) |
| Iterate | O(n) | O(n) | O(n) |
| Size | O(n) | O(1) | O(1) |

## 13.7. When to Use What

**Use Map when:**
- Need non-string keys
- Need to preserve insertion order
- Frequently add/remove key-value pairs
- Need size property

**Use Object when:**
- Keys are strings/symbols
- Need JSON serialization
- Working with existing code

**Use Set when:**
- Need unique values
- Frequently check membership
- Remove duplicates

**Use WeakMap when:**
- Need garbage collection for keys
- Store metadata/private data

**Use WeakSet when:**
- Track objects temporarily
- Need garbage collection

## 13.8. Exercises

### Exercise 1: Word Frequency

```javascript
// Count frequency of words in a sentence
function wordFrequency(sentence) {
    // Use Map to count occurrences
}

wordFrequency('hello world hello');
// Map { 'hello' => 2, 'world' => 1 }
```

### Exercise 2: Remove Duplicates

```javascript
// Remove duplicate objects from array
function removeDuplicates(arr) {
    // Use Set
}

removeDuplicates([1, 2, 2, 3, 3, 4]);  // [1, 2, 3, 4]
```

### Exercise 3: Private Data

```javascript
// Create a class with private data using WeakMap
class BankAccount {
    // Use WeakMap for private balance
}
```

---

**Kết luận:** Map và Set cung cấp data structures mới mạnh mẽ hơn Object và Array. WeakMap/WeakSet hữu ích cho memory management và private data.

**Chương tiếp theo:** Symbols
