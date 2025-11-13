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

## 13.6. Real-world Use Cases

### Use Case 1: Caching with TTL (Time To Live)

```javascript
class CacheWithTTL {
    constructor() {
        this.cache = new Map();
        this.timers = new Map();
    }

    set(key, value, ttl = 5000) {
        // Clear previous timer
        if (this.timers.has(key)) {
            clearTimeout(this.timers.get(key));
        }

        // Set value
        this.cache.set(key, value);

        // Set expiration timer
        const timer = setTimeout(() => {
            this.cache.delete(key);
            this.timers.delete(key);
        }, ttl);

        this.timers.set(key, timer);
    }

    get(key) {
        return this.cache.get(key);
    }

    has(key) {
        return this.cache.has(key);
    }

    clear() {
        // Clear all timers
        this.timers.forEach(timer => clearTimeout(timer));
        this.cache.clear();
        this.timers.clear();
    }
}

// Usage
const cache = new CacheWithTTL();
cache.set('user:1', { name: 'John', id: 1 }, 3000);
console.log(cache.get('user:1')); // { name: 'John', id: 1 }
setTimeout(() => {
    console.log(cache.get('user:1')); // undefined (expired)
}, 4000);
```

### Use Case 2: Dependency Tracking with WeakMap

```javascript
const dependencies = new WeakMap();

class Component {
    constructor(name) {
        this.name = name;
        dependencies.set(this, new Set());
    }

    addDependency(dep) {
        const deps = dependencies.get(this);
        deps.add(dep);
    }

    getDependencies() {
        return [...dependencies.get(this)];
    }

    update() {
        console.log(`${this.name} updated`);
        this.getDependencies().forEach(dep => {
            console.log(`  - notifying ${dep.name}`);
        });
    }
}

const compA = new Component('ComponentA');
const compB = new Component('ComponentB');
const compC = new Component('ComponentC');

compA.addDependency(compB);
compA.addDependency(compC);

compA.update();
// ComponentA updated
//   - notifying ComponentB
//   - notifying ComponentC
```

### Use Case 3: Set Operations for Filtering

```javascript
class UserFilter {
    constructor() {
        this.admins = new Set();
        this.moderators = new Set();
        this.banned = new Set();
    }

    addAdmin(userId) {
        this.admins.add(userId);
    }

    addModerator(userId) {
        this.moderators.add(userId);
    }

    banUser(userId) {
        this.banned.add(userId);
    }

    // Get users with specific role
    hasRole(userId, role) {
        switch(role) {
            case 'admin': return this.admins.has(userId);
            case 'moderator': return this.moderators.has(userId);
            default: return false;
        }
    }

    // Get active users (not banned)
    getActiveUsers(userIds) {
        return userIds.filter(id => !this.banned.has(id));
    }

    // Get users who are either admin or moderator
    getStaff() {
        return new Set([...this.admins, ...this.moderators]);
    }

    // Get admins who are not banned
    getActivAdmins() {
        return new Set([...this.admins].filter(id => !this.banned.has(id)));
    }
}

const filter = new UserFilter();
filter.addAdmin(1);
filter.addAdmin(2);
filter.addModerator(3);
filter.banUser(2);

console.log([...filter.getActivAdmins()]); // [1]
```

### Use Case 4: State Machine with Map

```javascript
class StateMachine {
    constructor(initialState = 'idle') {
        this.state = initialState;
        this.transitions = new Map();
        this.handlers = new Map();
    }

    addTransition(fromState, event, toState) {
        if (!this.transitions.has(fromState)) {
            this.transitions.set(fromState, new Map());
        }
        this.transitions.get(fromState).set(event, toState);
    }

    onEnter(state, handler) {
        if (!this.handlers.has(`enter:${state}`)) {
            this.handlers.set(`enter:${state}`, []);
        }
        this.handlers.get(`enter:${state}`).push(handler);
    }

    onExit(state, handler) {
        if (!this.handlers.has(`exit:${state}`)) {
            this.handlers.set(`exit:${state}`, []);
        }
        this.handlers.get(`exit:${state}`).push(handler);
    }

    dispatch(event) {
        const transitions = this.transitions.get(this.state);
        if (!transitions || !transitions.has(event)) {
            console.log(`No transition for event '${event}' in state '${this.state}'`);
            return false;
        }

        const nextState = transitions.get(event);

        // Run exit handlers
        const exitHandlers = this.handlers.get(`exit:${this.state}`) || [];
        exitHandlers.forEach(h => h());

        this.state = nextState;

        // Run enter handlers
        const enterHandlers = this.handlers.get(`enter:${this.state}`) || [];
        enterHandlers.forEach(h => h());

        return true;
    }

    getState() {
        return this.state;
    }
}

// Usage: Traffic light
const light = new StateMachine('red');
light.addTransition('red', 'go', 'green');
light.addTransition('green', 'slow', 'yellow');
light.addTransition('yellow', 'stop', 'red');

light.onExit('red', () => console.log('Traffic moving...'));
light.onEnter('green', () => console.log('Green light!'));

light.dispatch('go'); // Green light!
light.dispatch('slow');
light.dispatch('stop'); // Traffic moving...
```

### Use Case 5: Request Deduplication with Map

```javascript
class RequestDeduplicator {
    constructor() {
        this.pendingRequests = new Map();
    }

    async fetch(key, requestFn) {
        // If already fetching, return existing promise
        if (this.pendingRequests.has(key)) {
            return this.pendingRequests.get(key);
        }

        // Create new request
        const promise = requestFn()
            .then(result => {
                this.pendingRequests.delete(key);
                return result;
            })
            .catch(error => {
                this.pendingRequests.delete(key);
                throw error;
            });

        this.pendingRequests.set(key, promise);
        return promise;
    }
}

// Usage
const dedup = new RequestDeduplicator();

const fetchUser = (id) => fetch(`/api/users/${id}`).then(r => r.json());

// Multiple calls with same ID will use cached promise
Promise.all([
    dedup.fetch('user:1', () => fetchUser(1)),
    dedup.fetch('user:1', () => fetchUser(1)), // Same key, reuses promise
    dedup.fetch('user:2', () => fetchUser(2))
]);
```

## 13.7. Tips & Tricks

### Tip 1: Map with Default Values

```javascript
class MapWithDefaults extends Map {
    constructor(defaultValue = null) {
        super();
        this.defaultValue = defaultValue;
    }

    get(key) {
        if (!this.has(key)) {
            this.set(key, typeof this.defaultValue === 'function' ? this.defaultValue() : this.defaultValue);
        }
        return super.get(key);
    }
}

const map = new MapWithDefaults(() => []);
map.get('items').push(1);
map.get('items').push(2);
console.log(map.get('items')); // [1, 2]
```

### Tip 2: Converting Between Data Structures

```javascript
// Map to Object
const mapToObject = (map) => Object.fromEntries(map);

// Object to Map
const objectToMap = (obj) => new Map(Object.entries(obj));

// Set to Array with unique check
const setToArray = (set) => [...set];
const arrayToSet = (arr) => new Set(arr);

// Map to Array of entries
const mapToEntries = (map) => [...map];

// Filter Set
const filterSet = (set, predicate) => new Set([...set].filter(predicate));

// Map over Set
const mapSet = (set, fn) => new Set([...set].map(fn));

const set = new Set([1, 2, 3, 4, 5]);
const evens = filterSet(set, x => x % 2 === 0);
console.log([...evens]); // [2, 4]
```

### Tip 3: Set as Unique Array Builder

```javascript
class UniqueArray {
    constructor() {
        this.set = new Set();
    }

    add(value) {
        this.set.add(value);
        return this;
    }

    remove(value) {
        this.set.delete(value);
        return this;
    }

    toArray() {
        return [...this.set];
    }

    size() {
        return this.set.size;
    }

    has(value) {
        return this.set.has(value);
    }
}

const unique = new UniqueArray();
unique.add(1).add(2).add(2).add(3).add(1);
console.log(unique.toArray()); // [1, 2, 3]
console.log(unique.size()); // 3
```

### Tip 4: Multi-key Map

```javascript
class MultiKeyMap {
    constructor() {
        this.map = new Map();
    }

    set(keys, value) {
        const key = JSON.stringify(keys);
        this.map.set(key, value);
        return this;
    }

    get(keys) {
        const key = JSON.stringify(keys);
        return this.map.get(key);
    }

    has(keys) {
        const key = JSON.stringify(keys);
        return this.map.has(key);
    }

    delete(keys) {
        const key = JSON.stringify(keys);
        return this.map.delete(key);
    }
}

// Usage
const multiMap = new MultiKeyMap();
multiMap.set(['user', 1], 'John');
multiMap.set(['user', 2], 'Jane');
console.log(multiMap.get(['user', 1])); // "John"
```

### Tip 5: Nested Map Structure

```javascript
class NestedMap {
    constructor() {
        this.map = new Map();
    }

    set(path, value) {
        const keys = Array.isArray(path) ? path : [path];
        let current = this.map;

        for (let i = 0; i < keys.length - 1; i++) {
            if (!current.has(keys[i])) {
                current.set(keys[i], new Map());
            }
            current = current.get(keys[i]);
        }

        current.set(keys[keys.length - 1], value);
        return this;
    }

    get(path) {
        const keys = Array.isArray(path) ? path : [path];
        let current = this.map;

        for (const key of keys) {
            if (!current.has(key)) return undefined;
            current = current.get(key);
        }

        return current;
    }
}

// Usage
const nested = new NestedMap();
nested.set(['user', 1, 'profile', 'name'], 'John');
nested.set(['user', 1, 'profile', 'email'], 'john@example.com');
console.log(nested.get(['user', 1, 'profile', 'name'])); // "John"
```

### Tip 6: Set Intersection, Union, Difference

```javascript
const union = (a, b) => new Set([...a, ...b]);

const intersection = (a, b) => new Set([...a].filter(x => b.has(x)));

const difference = (a, b) => new Set([...a].filter(x => !b.has(x)));

const isSuperset = (a, b) => [...b].every(x => a.has(x));

const isDisjoint = (a, b) => intersection(a, b).size === 0;

// Usage
const set1 = new Set([1, 2, 3, 4]);
const set2 = new Set([3, 4, 5, 6]);

console.log([...union(set1, set2)]); // [1, 2, 3, 4, 5, 6]
console.log([...intersection(set1, set2)]); // [3, 4]
console.log([...difference(set1, set2)]); // [1, 2]
console.log(isSuperset(set1, new Set([2, 3]))); // true
```

### Tip 7: Private Data with WeakMap Pattern

```javascript
const privateData = new WeakMap();

class BankAccount {
    constructor(initialBalance) {
        privateData.set(this, {
            balance: initialBalance,
            transactions: []
        });
    }

    deposit(amount) {
        const data = privateData.get(this);
        data.balance += amount;
        data.transactions.push({ type: 'deposit', amount, date: new Date() });
    }

    withdraw(amount) {
        const data = privateData.get(this);
        if (data.balance >= amount) {
            data.balance -= amount;
            data.transactions.push({ type: 'withdraw', amount, date: new Date() });
            return true;
        }
        return false;
    }

    getBalance() {
        return privateData.get(this).balance;
    }

    getTransactions() {
        return [...privateData.get(this).transactions];
    }
}

const account = new BankAccount(1000);
account.deposit(500);
account.withdraw(200);
console.log(account.getBalance()); // 1300
console.log(account.getTransactions()); // Array of transaction objects
```

### Tip 8: Memoization with Map

```javascript
function createMemoizer(fn) {
    const cache = new Map();

    return function(...args) {
        const key = JSON.stringify(args);

        if (cache.has(key)) {
            console.log('Cached:', args);
            return cache.get(key);
        }

        console.log('Computing:', args);
        const result = fn(...args);
        cache.set(key, result);
        return result;
    };
}

const fibonacci = createMemoizer((n) => {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
});

console.log(fibonacci(5)); // Computing: [5]
console.log(fibonacci(5)); // Cached: [5]
```

### Tip 9: Object-to-Map Serialization

```javascript
class SerializableMap extends Map {
    toJSON() {
        return Array.from(this.entries());
    }

    static fromJSON(json) {
        return new SerializableMap(json);
    }
}

const map = new SerializableMap([['a', 1], ['b', 2]]);
const json = JSON.stringify(map);
console.log(json); // "[["a",1],["b",2]]"

const restored = SerializableMap.fromJSON(JSON.parse(json));
console.log(restored.get('a')); // 1
```

### Tip 10: Sorted Map

```javascript
class SortedMap extends Map {
    constructor(iterable, compareFn = (a, b) => a - b) {
        super(iterable);
        this.compareFn = compareFn;
    }

    *entries() {
        const sorted = [...super.entries()].sort((a, b) =>
            this.compareFn(a[0], b[0])
        );
        for (const entry of sorted) {
            yield entry;
        }
    }

    *keys() {
        const sorted = [...super.keys()].sort(this.compareFn);
        for (const key of sorted) {
            yield key;
        }
    }

    *values() {
        const sorted = [...super.entries()]
            .sort((a, b) => this.compareFn(a[0], b[0]))
            .map(e => e[1]);
        for (const value of sorted) {
            yield value;
        }
    }
}

const map = new SortedMap([[3, 'c'], [1, 'a'], [2, 'b']]);
console.log([...map.keys()]); // [1, 2, 3]
```

## 13.8. Common Mistakes

### Mistake 1: Modifying Set During Iteration

```javascript
// WRONG
const set = new Set([1, 2, 3, 4, 5]);
for (const item of set) {
    if (item === 2) {
        set.add(6); // Adding during iteration
    }
}

// RIGHT
const set = new Set([1, 2, 3, 4, 5]);
const itemsToAdd = [];
for (const item of set) {
    if (item === 2) {
        itemsToAdd.push(6);
    }
}
itemsToAdd.forEach(item => set.add(item));

// Or create new Set
const newSet = new Set([...set, 6]);
```

### Mistake 2: Comparing Objects in Set

```javascript
// WRONG: Objects are compared by reference
const set = new Set();
set.add({ id: 1 });
set.add({ id: 1 });
console.log(set.size); // 2 (not 1!)

// RIGHT: Store identifiable values
const set = new Set();
set.add(1); // id instead of object
set.add(1);
console.log(set.size); // 1

// Or use custom object with proper comparisons
class User {
    constructor(id) {
        this.id = id;
    }

    equals(other) {
        return this.id === other.id;
    }
}
```

### Mistake 3: Map Keys with Different Types

```javascript
// CONFUSING: Map treats different types differently
const map = new Map();
map.set('1', 'string key');
map.set(1, 'number key');
console.log(map.get('1')); // "string key"
console.log(map.get(1));   // "number key"

// BE CONSISTENT
const map = new Map();
map.set(String(1), 'value1');
map.set(String(2), 'value2');
// Or use numbers consistently
const map = new Map();
map.set(1, 'value1');
map.set(2, 'value2');
```

### Mistake 4: Forgetting WeakMap Limitations

```javascript
// WRONG: Can't iterate WeakMap
const weakMap = new WeakMap();
const obj1 = {};
const obj2 = {};
weakMap.set(obj1, 'value1');
weakMap.set(obj2, 'value2');

// WeakMap has no .size, .keys(), .values(), .entries()
// console.log(weakMap.size);     // Error!
// for (const [k, v] of weakMap) // Error!

// RIGHT: Use regular Map if you need iteration
const map = new Map();
map.set(obj1, 'value1');
map.set(obj2, 'value2');
console.log(map.size); // 2
for (const [key, value] of map) {
    console.log(key, value);
}
```

### Mistake 5: Assuming NaN Equality

```javascript
// CONFUSING in objects/arrays, but Map handles it well
const map = new Map();
map.set(NaN, 'value');
console.log(map.get(NaN)); // "value" (works!)

// In Set
const set = new Set([NaN, NaN, NaN]);
console.log(set.size); // 1 (deduplicated!)

// But in Object, NaN !== NaN
const obj = {};
obj[NaN] = 'value';
console.log(obj['NaN']); // "value" (converted to string)
```

### Mistake 6: Set with Objects - Reference Issues

```javascript
// WRONG: Different object instances are different values
const set = new Set();
set.add({x: 1});
set.add({x: 1});
console.log(set.size); // 2

// RIGHT: Keep reference
const obj = {x: 1};
const set = new Set();
set.add(obj);
set.add(obj);
console.log(set.size); // 1
```

### Mistake 7: Map Default Value Anti-pattern

```javascript
// WRONG: Modifies original
const map = new Map();
const arr = [];
map.set('items', arr);
map.get('items').push(1);
console.log(arr); // [1] - original modified!

// RIGHT: Be aware of mutability
const map = new Map();
map.set('items', []);
map.get('items').push(1);
// The array inside map was modified

// Or use immutable pattern
class ImmutableMap {
    constructor() {
        this.data = new Map();
    }

    set(key, value) {
        this.data.set(key, JSON.parse(JSON.stringify(value)));
    }

    get(key) {
        return JSON.parse(JSON.stringify(this.data.get(key)));
    }
}
```

### Mistake 8: WeakMap with Primitive Keys

```javascript
// WRONG: WeakMap only accepts objects
const weakMap = new WeakMap();
// weakMap.set('string', 'value');  // TypeError
// weakMap.set(123, 'value');       // TypeError
// weakMap.set(true, 'value');      // TypeError

// RIGHT: Use Map for primitives
const map = new Map();
map.set('string', 'value');
map.set(123, 'value');
map.set(true, 'value');

// Or wrap primitives (not recommended)
const weakMap = new WeakMap();
const stringKey = new String('key');
weakMap.set(stringKey, 'value');
```

### Mistake 9: Clearing Map vs Creating New

```javascript
// Both work but have different implications
const map1 = new Map();
map1.set('a', 1);

// Option 1: Clear
map1.clear();
console.log(map1.size); // 0

// Option 2: Create new
let map2 = new Map();
map2.set('a', 1);
map2 = new Map();
console.log(map2.size); // 0

// If map is shared, clearing is better
function getCache() {
    return cache; // Same reference
}

const cache = new Map();
cache.set('a', 1);
cache.clear(); // Affects all references
```

### Mistake 10: Shallow Copying Map/Set

```javascript
// WRONG: Shallow copy with nested objects
const originalMap = new Map([
    ['user', { name: 'John', address: { city: 'NYC' } }]
]);

const copy = new Map(originalMap);
copy.get('user').address.city = 'LA';

console.log(originalMap.get('user').address.city); // "LA" - Changed!

// RIGHT: Deep copy
function deepCopyMap(map) {
    return new Map(
        [...map].map(([key, value]) => [
            key,
            typeof value === 'object' && value !== null ?
                JSON.parse(JSON.stringify(value)) :
                value
        ])
    );
}

const deepCopy = deepCopyMap(originalMap);
deepCopy.get('user').address.city = 'LA';
console.log(originalMap.get('user').address.city); // "NYC" - Unchanged!
```

## 13.9. Troubleshooting Issues

### Issue 1: Memory Leaks with Map/Set

**Problem:**
```javascript
class EventManager {
    constructor() {
        this.listeners = new Map();
    }

    on(event, handler) {
        if (!this.listeners.has(event)) {
            this.listeners.set(event, new Set());
        }
        this.listeners.get(event).add(handler);
    }

    // Missing: off() method
}

// Memory leak: handlers accumulate
const manager = new EventManager();
for (let i = 0; i < 1000; i++) {
    manager.on('click', () => console.log('click'));
}
```

**Solution:**
```javascript
class EventManager {
    constructor() {
        this.listeners = new Map();
    }

    on(event, handler) {
        if (!this.listeners.has(event)) {
            this.listeners.set(event, new Set());
        }
        this.listeners.get(event).add(handler);

        // Return unsubscribe function
        return () => this.off(event, handler);
    }

    off(event, handler) {
        if (this.listeners.has(event)) {
            this.listeners.get(event).delete(handler);
            if (this.listeners.get(event).size === 0) {
                this.listeners.delete(event);
            }
        }
    }

    emit(event, ...args) {
        if (this.listeners.has(event)) {
            this.listeners.get(event).forEach(handler => handler(...args));
        }
    }
}

// Good usage
const manager = new EventManager();
const unsubscribe = manager.on('click', () => console.log('click'));
// Clean up
unsubscribe();
```

### Issue 2: WeakMap Garbage Collection

**Problem:**
```javascript
const cache = new WeakMap();

function cacheData(obj) {
    cache.set(obj, 'some data');
    return cache.get(obj);
}

const obj = { id: 1 };
console.log(cacheData(obj)); // "some data"

// obj reference lost, but...
// We can't verify it was garbage collected!
```

**Solution:**
```javascript
const cache = new WeakMap();
const instances = new Set(); // Track for testing

class CachedObject {
    constructor(id) {
        this.id = id;
        instances.add(this);
        cache.set(this, { data: `cached-${id}` });
    }

    getData() {
        return cache.get(this);
    }

    static clearCache(instance) {
        instances.delete(instance);
        // WeakMap will auto-clean when instance is GC'd
    }
}

const obj = new CachedObject(1);
console.log(obj.getData()); // { data: 'cached-1' }
CachedObject.clearCache(obj);
```

### Issue 3: Map Performance with Large Data

**Problem:**
```javascript
const map = new Map();

// Adding many items
for (let i = 0; i < 1000000; i++) {
    map.set(`key-${i}`, { data: 'value' });
}

// Linear search through large map
let count = 0;
for (const [key, value] of map) {
    if (value.data === 'specific') count++;
}
```

**Solution:**
```javascript
// Use secondary index for fast lookup
class IndexedMap {
    constructor() {
        this.data = new Map();
        this.indices = new Map(); // Secondary indices
    }

    set(key, value, indexKey) {
        this.data.set(key, value);

        if (indexKey !== undefined) {
            if (!this.indices.has(indexKey)) {
                this.indices.set(indexKey, new Set());
            }
            this.indices.get(indexKey).add(key);
        }
    }

    getByIndex(indexKey, value) {
        const keys = this.indices.get(`${indexKey}:${value}`) || new Set();
        return [...keys].map(k => this.data.get(k));
    }
}

// Or partition data
const smallMap = new Map();
const largeMap = new Map();

for (let i = 0; i < 100; i++) {
    smallMap.set(`key-${i}`, { data: 'hot' });
}
for (let i = 100; i < 1000000; i++) {
    largeMap.set(`key-${i}`, { data: 'cold' });
}
```

### Issue 4: Set with Complex Objects

**Problem:**
```javascript
const userSet = new Set();

const user1 = { id: 1, name: 'John' };
const user2 = { id: 1, name: 'John' };

userSet.add(user1);
userSet.add(user2);

console.log(userSet.size); // 2 (but should be 1!)
```

**Solution:**
```javascript
class UniqueSet {
    constructor(getKey = item => item) {
        this.map = new Map();
        this.getKey = getKey;
    }

    add(item) {
        const key = this.getKey(item);
        this.map.set(key, item);
        return this;
    }

    has(item) {
        const key = this.getKey(item);
        return this.map.has(key);
    }

    delete(item) {
        const key = this.getKey(item);
        return this.map.delete(key);
    }

    toArray() {
        return [...this.map.values()];
    }

    get size() {
        return this.map.size;
    }
}

const userSet = new UniqueSet(user => user.id);
userSet.add({ id: 1, name: 'John' });
userSet.add({ id: 1, name: 'John Updated' });
console.log(userSet.size); // 1
```

### Issue 5: Iterating Map While Modifying

**Problem:**
```javascript
const map = new Map([
    ['a', 1], ['b', 2], ['c', 3]
]);

for (const [key, value] of map) {
    if (key === 'b') {
        map.set('d', 4); // May cause unexpected behavior
    }
    console.log(key);
}
```

**Solution:**
```javascript
// Create snapshot before iteration
const map = new Map([
    ['a', 1], ['b', 2], ['c', 3]
]);

const entries = [...map.entries()]; // Snapshot
for (const [key, value] of entries) {
    if (key === 'b') {
        map.set('d', 4);
    }
    console.log(key);
}

console.log(map.size); // 4
```

### Issue 6: Set Deduplication with Objects

**Problem:**
```javascript
const users = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' },
    { id: 1, name: 'John' }  // Duplicate id
];

const uniqueUsers = [...new Set(users)];
console.log(uniqueUsers.length); // 3 (not 2!)
```

**Solution:**
```javascript
// Deduplicate by key
function deduplicateBy(arr, getKey) {
    const seen = new Set();
    return arr.filter(item => {
        const key = getKey(item);
        if (seen.has(key)) return false;
        seen.add(key);
        return true;
    });
}

const users = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' },
    { id: 1, name: 'John' }
];

const uniqueUsers = deduplicateBy(users, u => u.id);
console.log(uniqueUsers.length); // 2
```

### Issue 7: JSON Serialization with Map

**Problem:**
```javascript
const map = new Map([
    ['user', { name: 'John' }],
    ['settings', { theme: 'dark' }]
]);

const json = JSON.stringify(map);
console.log(json); // "{}" - Empty object!
```

**Solution:**
```javascript
// Convert to array before stringifying
const mapToJson = (map) => JSON.stringify([...map]);
const jsonToMap = (json) => new Map(JSON.parse(json));

const map = new Map([
    ['user', { name: 'John' }],
    ['settings', { theme: 'dark' }]
]);

const json = mapToJson(map);
console.log(json); // '[["user",{"name":"John"}],["settings",{"theme":"dark"}]]'

const restored = jsonToMap(json);
console.log(restored.get('user')); // { name: 'John' }
```

### Issue 8: WeakMap with Numeric Keys

**Problem:**
```javascript
const weakMap = new WeakMap();

// Trying to use Number or BigInt as key
const num = new Number(123);
weakMap.set(num, 'value');

// Later...
const anotherNum = new Number(123);
console.log(weakMap.has(anotherNum)); // false (different object!)
```

**Solution:**
```javascript
// Use object wrapper or regular Map
class KeyedValue {
    constructor(value) {
        this.value = value;
    }
}

const weakMap = new WeakMap();
const key = new KeyedValue(123);
weakMap.set(key, 'value');
console.log(weakMap.get(key)); // 'value'

// Or use Map for numeric keys
const map = new Map();
map.set(123, 'value');
console.log(map.get(123)); // 'value'
```

### Issue 9: Set with Array-like Duplicates

**Problem:**
```javascript
const set = new Set([
    [1, 2],
    [1, 2],
    [1, 2]
]);

console.log(set.size); // 3 (should be 1!)
```

**Solution:**
```javascript
// Stringify for comparison
function uniqueArrays(arrays) {
    const seen = new Set();
    return arrays.filter(arr => {
        const key = JSON.stringify(arr);
        if (seen.has(key)) return false;
        seen.add(key);
        return true;
    });
}

const arrays = [[1, 2], [1, 2], [1, 2]];
const unique = uniqueArrays(arrays);
console.log(unique.length); // 1

// Or use custom comparison
class SetWithComparator {
    constructor(compareFn) {
        this.items = [];
        this.compareFn = compareFn;
    }

    add(item) {
        if (!this.items.some(existing => this.compareFn(existing, item))) {
            this.items.push(item);
        }
        return this;
    }

    has(item) {
        return this.items.some(existing => this.compareFn(existing, item));
    }

    get size() {
        return this.items.length;
    }
}

const set = new SetWithComparator((a, b) => JSON.stringify(a) === JSON.stringify(b));
set.add([1, 2]).add([1, 2]).add([1, 2]);
console.log(set.size); // 1
```

### Issue 10: Map Performance with String Keys

**Problem:**
```javascript
// Slow: Creating new strings for keys
const map = new Map();
for (let i = 0; i < 1000000; i++) {
    map.set(`key_${i}`, i);
}

// Accessing with string creation
console.log(map.get(`key_${500000}`)); // Slow lookup
```

**Solution:**
```javascript
// Better: Use numeric keys when possible
const map = new Map();
for (let i = 0; i < 1000000; i++) {
    map.set(i, i);
}

console.log(map.get(500000)); // Faster

// Or reuse key objects
const keyPool = new Map();
function getKey(str) {
    if (!keyPool.has(str)) {
        keyPool.set(str, str);
    }
    return keyPool.get(str);
}

const dataMap = new Map();
for (let i = 0; i < 1000000; i++) {
    dataMap.set(getKey(`key_${i % 100}`), i); // Reuse keys
}
```

## 13.10. Advanced Topics

### Advanced Topic 1: Custom Collection with Map

```javascript
class Graph {
    constructor() {
        this.adjacencyList = new Map();
    }

    addVertex(vertex) {
        if (!this.adjacencyList.has(vertex)) {
            this.adjacencyList.set(vertex, new Set());
        }
    }

    addEdge(v1, v2, weight = 1) {
        this.addVertex(v1);
        this.addVertex(v2);
        this.adjacencyList.get(v1).add({vertex: v2, weight});
        this.adjacencyList.get(v2).add({vertex: v1, weight}); // undirected
    }

    getNeighbors(vertex) {
        return this.adjacencyList.get(vertex) || new Set();
    }

    *dfs(startVertex, visited = new Set()) {
        visited.add(startVertex);
        yield startVertex;

        for (const {vertex} of this.getNeighbors(startVertex)) {
            if (!visited.has(vertex)) {
                yield* this.dfs(vertex, visited);
            }
        }
    }

    *bfs(startVertex) {
        const visited = new Set([startVertex]);
        const queue = [startVertex];

        while (queue.length > 0) {
            const vertex = queue.shift();
            yield vertex;

            for (const {vertex: neighbor} of this.getNeighbors(vertex)) {
                if (!visited.has(neighbor)) {
                    visited.add(neighbor);
                    queue.push(neighbor);
                }
            }
        }
    }
}

// Usage
const graph = new Graph();
graph.addEdge('A', 'B');
graph.addEdge('A', 'C');
graph.addEdge('B', 'D');
graph.addEdge('C', 'D');

console.log([...graph.dfs('A')]); // DFS traversal
console.log([...graph.bfs('A')]); // BFS traversal
```

### Advanced Topic 2: Bloom Filter with Set

```javascript
class BloomFilter {
    constructor(size = 1000, hashFunctions = 3) {
        this.size = size;
        this.bits = new Set();
        this.hashFunctions = hashFunctions;
    }

    _hash(item, seed) {
        let hash = seed;
        for (let i = 0; i < item.length; i++) {
            hash = ((hash << 5) - hash) + item.charCodeAt(i);
            hash = hash & hash; // Convert to 32bit integer
        }
        return Math.abs(hash) % this.size;
    }

    add(item) {
        for (let i = 0; i < this.hashFunctions; i++) {
            const index = this._hash(item, i);
            this.bits.add(index);
        }
    }

    might Contains(item) {
        for (let i = 0; i < this.hashFunctions; i++) {
            const index = this._hash(item, i);
            if (!this.bits.has(index)) {
                return false;
            }
        }
        return true;
    }
}

const filter = new BloomFilter();
filter.add('apple');
filter.add('banana');
console.log(filter.mightContains('apple')); // true
console.log(filter.mightContains('cherry')); // possibly false
```

### Advanced Topic 3: LFU Cache (Least Frequently Used)

```javascript
class LFUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.cache = new Map(); // key -> {value, frequency}
        this.frequencies = new Map(); // frequency -> Set of keys
        this.minFreq = 0;
    }

    get(key) {
        if (!this.cache.has(key)) return -1;

        const {value, frequency} = this.cache.get(key);
        this._updateFrequency(key, frequency);

        return value;
    }

    put(key, value) {
        if (this.capacity <= 0) return;

        if (this.cache.has(key)) {
            const {frequency} = this.cache.get(key);
            this.cache.set(key, {value, frequency});
            this._updateFrequency(key, frequency);
            return;
        }

        if (this.cache.size >= this.capacity) {
            this._evictLFU();
        }

        this.cache.set(key, {value, frequency: 1});
        if (!this.frequencies.has(1)) {
            this.frequencies.set(1, new Set());
        }
        this.frequencies.get(1).add(key);
        this.minFreq = 1;
    }

    _updateFrequency(key, oldFreq) {
        const {value} = this.cache.get(key);
        const newFreq = oldFreq + 1;

        // Remove from old frequency set
        this.frequencies.get(oldFreq).delete(key);
        if (this.frequencies.get(oldFreq).size === 0) {
            this.frequencies.delete(oldFreq);
            if (oldFreq === this.minFreq) {
                this.minFreq = newFreq;
            }
        }

        // Add to new frequency set
        if (!this.frequencies.has(newFreq)) {
            this.frequencies.set(newFreq, new Set());
        }
        this.frequencies.get(newFreq).add(key);

        // Update cache
        this.cache.set(key, {value, frequency: newFreq});
    }

    _evictLFU() {
        const lfuSet = this.frequencies.get(this.minFreq);
        const keyToEvict = lfuSet.values().next().value;
        lfuSet.delete(keyToEvict);
        this.cache.delete(keyToEvict);
    }
}

// Usage
const cache = new LFUCache(2);
cache.put(1, 'a');
cache.put(2, 'b');
console.log(cache.get(1)); // 'a'
cache.put(3, 'c'); // Evicts key 2
console.log(cache.get(2)); // -1
```

### Advanced Topic 4: Multiset (Bag)

```javascript
class Multiset {
    constructor(iterable = []) {
        this.map = new Map();
        for (const item of iterable) {
            this.add(item);
        }
    }

    add(item, count = 1) {
        this.map.set(item, (this.map.get(item) || 0) + count);
    }

    remove(item, count = 1) {
        if (!this.map.has(item)) return false;
        const current = this.map.get(item);
        if (count >= current) {
            this.map.delete(item);
        } else {
            this.map.set(item, current - count);
        }
        return true;
    }

    count(item) {
        return this.map.get(item) || 0;
    }

    has(item) {
        return this.map.has(item);
    }

    get size() {
        let total = 0;
        for (const count of this.map.values()) {
            total += count;
        }
        return total;
    }

    toArray() {
        const result = [];
        for (const [item, count] of this.map) {
            for (let i = 0; i < count; i++) {
                result.push(item);
            }
        }
        return result;
    }
}

const bag = new Multiset([1, 1, 2, 2, 2, 3]);
console.log(bag.count(1)); // 2
console.log(bag.count(2)); // 3
console.log(bag.size); // 6
```

### Advanced Topic 5: Trie with Map

```javascript
class TrieNode {
    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
        this.value = null;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word, value = true) {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char);
        }
        node.isEndOfWord = true;
        node.value = value;
    }

    search(word) {
        const node = this._findNode(word);
        return node && node.isEndOfWord ? node.value : undefined;
    }

    startsWith(prefix) {
        return this._findNode(prefix) !== null;
    }

    *autoComplete(prefix) {
        const node = this._findNode(prefix);
        if (node) {
            yield* this._getAllWords(node, prefix);
        }
    }

    _findNode(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                return null;
            }
            node = node.children.get(char);
        }
        return node;
    }

    *_getAllWords(node, prefix) {
        if (node.isEndOfWord) {
            yield prefix;
        }
        for (const [char, child] of node.children) {
            yield* this._getAllWords(child, prefix + char);
        }
    }
}

// Usage
const trie = new Trie();
trie.insert('apple');
trie.insert('app');
trie.insert('application');
trie.insert('apply');

console.log([...trie.autoComplete('app')]); // ['app', 'apple', 'application', 'apply']
```

## 13.11. Exercises

### Exercise 1 (Dễ): Create Map from Array

```javascript
// Tạo map từ array, với index là key
const arr = ['a', 'b', 'c', 'd', 'e'];

// Expected: Map { 0 => 'a', 1 => 'b', 2 => 'c', ... }
```

### Exercise 2 (Dễ): Unique Characters Count

```javascript
// Đếm số lần xuất hiện của mỗi ký tự trong string
function countChars(str) {
    // Sử dụng Map
}

console.log(countChars('hello'));
// Map { 'h' => 1, 'e' => 1, 'l' => 2, 'o' => 1 }
```

### Exercise 3 (Dễ): Remove Duplicates with Set

```javascript
// Loại bỏ phần tử trùng lặp
function removeDuplicates(arr) {
    // Sử dụng Set
}

console.log(removeDuplicates([1, 2, 2, 3, 3, 3, 4]));
// [1, 2, 3, 4]
```

### Exercise 4 (Dễ): Map Operations

```javascript
// Merge hai Map
function mergeMaps(map1, map2) {
    // Code của bạn
}

const m1 = new Map([['a', 1], ['b', 2]]);
const m2 = new Map([['b', 3], ['c', 4]]);
const merged = mergeMaps(m1, m2);
// Map { 'a' => 1, 'b' => 3, 'c' => 4 }
```

### Exercise 5 (Trung bình): Group Users by Age

```javascript
// Group users theo age
function groupUsersByAge(users) {
    // Sử dụng Map
}

const users = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 },
    { name: 'Bob', age: 30 },
    { name: 'Alice', age: 25 }
];

const grouped = groupUsersByAge(users);
// Map {
//   25 => [{name: 'Jane', age: 25}, {name: 'Alice', age: 25}],
//   30 => [{name: 'John', age: 30}, {name: 'Bob', age: 30}]
// }
```

### Exercise 6 (Trung bình): Two Sum with Set

```javascript
// Tìm hai số có tổng bằng target
function twoSum(arr, target) {
    // Sử dụng Set
}

console.log(twoSum([2, 7, 11, 15], 9)); // [2, 7]
console.log(twoSum([1, 2, 3, 6], 9));  // [3, 6]
```

### Exercise 7 (Trung bình): Word Frequency

```javascript
// Tính tần suất từ trong văn bản
function wordFrequency(text) {
    // Sử dụng Map
}

const text = "the quick brown fox jumps over the lazy dog the quick";
const freq = wordFrequency(text);
// Map { 'the' => 3, 'quick' => 2, ... }
```

### Exercise 8 (Trung bình): LRU Cache Basic

```javascript
// Implement LRU Cache
class LRUCache {
    constructor(capacity) {
        // Code của bạn
    }

    put(key, value) {
        // Code của bạn
    }

    get(key) {
        // Code của bạn
    }
}

const cache = new LRUCache(2);
cache.put(1, 'a');
cache.put(2, 'b');
console.log(cache.get(1)); // 'a'
cache.put(3, 'c');
console.log(cache.get(2)); // -1 (evicted)
```

### Exercise 9 (Khó): Intersection of Arrays

```javascript
// Tìm phần tử chung giữa nhiều arrays
function findIntersection(...arrays) {
    // Sử dụng Set operations
}

console.log(findIntersection([1,2,3,4], [2,3,4,5], [2,3,5]));
// [2, 3]
```

### Exercise 10 (Khó): Private Data Manager

```javascript
// Tạo manager cho private data sử dụng WeakMap
class PrivateDataManager {
    // Code của bạn
}

class User {
    constructor(name, ssn) {
        // Lưu ssn vào WeakMap via manager
    }
}

const user = new User('John', '123-45-6789');
// user.ssn không accessible trực tiếp
```

### Exercise 11 (Khó): Cache with Dependencies

```javascript
// Implement cache tự động invalidate khi dependency thay đổi
class DependentCache {
    // Khi key A thay đổi, invalidate dependent keys
}

const cache = new DependentCache();
cache.set('a', 1);
cache.set('b', 2, ['a']); // b depends on a
cache.set('c', 3, ['b']); // c depends on b

cache.update('a', 10); // Should invalidate b and c
```

### Exercise 12 (Khó): Trie Implementation

```javascript
// Implement Trie để autocomplete
class Trie {
    // Implement insert, search, startsWith, autoComplete
}

const trie = new Trie();
trie.insert('apple');
trie.insert('app');
trie.insert('application');

console.log([...trie.autoComplete('app')]);
// ['app', 'apple', 'application']
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
