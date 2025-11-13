# CHƯƠNG 14: SYMBOLS

## 14.1. Giới thiệu Symbols

Symbol là primitive data type mới trong ES6, tạo unique identifiers.

### 14.1.1. Creating Symbols

```javascript
// Create unique symbol
const sym1 = Symbol();
const sym2 = Symbol();

console.log(sym1 === sym2);  // false (always unique)

// With description
const sym = Symbol('mySymbol');
console.log(sym.toString());  // "Symbol(mySymbol)"
```

### 14.1.2. Symbols are Unique

```javascript
const sym1 = Symbol('id');
const sym2 = Symbol('id');

console.log(sym1 === sym2);  // false (different symbols)
console.log(sym1 == sym2);   // false
```

## 14.2. Symbol Properties

### 14.2.1. As Object Keys

```javascript
const id = Symbol('id');

const user = {
    name: 'John',
    [id]: 123  // Symbol as property key
};

console.log(user[id]);    // 123
console.log(user.id);     // undefined (not the same)
console.log(user['id']);  // undefined
```

### 14.2.2. Hidden Properties

```javascript
const user = {
    name: 'John',
    age: 30
};

const id = Symbol('id');
user[id] = 123;

// Symbol properties not in for...in
for (let key in user) {
    console.log(key);  // "name", "age" (no id)
}

// Not in Object.keys()
console.log(Object.keys(user));  // ['name', 'age']

// Not in JSON.stringify()
console.log(JSON.stringify(user));  // {"name":"John","age":30}
```

### 14.2.3. Getting Symbol Properties

```javascript
const user = {
    name: 'John',
    [Symbol('id')]: 123,
    [Symbol('role')]: 'admin'
};

// Get symbol keys
const symbols = Object.getOwnPropertySymbols(user);
console.log(symbols);  // [Symbol(id), Symbol(role)]

// Get all keys (including symbols)
const allKeys = Reflect.ownKeys(user);
console.log(allKeys);  // ['name', Symbol(id), Symbol(role)]
```

## 14.3. Global Symbol Registry

### 14.3.1. Symbol.for()

```javascript
// Create global symbol
const sym1 = Symbol.for('app.id');
const sym2 = Symbol.for('app.id');

console.log(sym1 === sym2);  // true (same symbol from registry)

// vs local symbol
const sym3 = Symbol('app.id');
console.log(sym1 === sym3);  // false
```

### 14.3.2. Symbol.keyFor()

```javascript
const globalSym = Symbol.for('app.id');
const localSym = Symbol('app.id');

console.log(Symbol.keyFor(globalSym));  // "app.id"
console.log(Symbol.keyFor(localSym));   // undefined (not in registry)
```

## 14.4. Well-known Symbols

### 14.4.1. Symbol.iterator

```javascript
const obj = {
    data: [1, 2, 3],

    [Symbol.iterator]() {
        let index = 0;
        return {
            next: () => {
                if (index < this.data.length) {
                    return { value: this.data[index++], done: false };
                }
                return { done: true };
            }
        };
    }
};

// Now iterable
for (const value of obj) {
    console.log(value);  // 1, 2, 3
}

console.log([...obj]);  // [1, 2, 3]
```

### 14.4.2. Symbol.toStringTag

```javascript
class MyClass {
    get [Symbol.toStringTag]() {
        return 'MyClass';
    }
}

const instance = new MyClass();
console.log(instance.toString());  // "[object MyClass]"
console.log(Object.prototype.toString.call(instance));  // "[object MyClass]"
```

### 14.4.3. Symbol.toPrimitive

```javascript
const obj = {
    value: 100,

    [Symbol.toPrimitive](hint) {
        if (hint === 'number') {
            return this.value;
        }
        if (hint === 'string') {
            return `Value: ${this.value}`;
        }
        return this.value;
    }
};

console.log(+obj);           // 100 (number)
console.log(`${obj}`);       // "Value: 100" (string)
console.log(obj + 50);       // 150 (default)
```

### 14.4.4. Symbol.hasInstance

```javascript
class MyArray {
    static [Symbol.hasInstance](instance) {
        return Array.isArray(instance);
    }
}

console.log([] instanceof MyArray);     // true
console.log({} instanceof MyArray);     // false
```

### 14.4.5. Symbol.species

```javascript
class MyArray extends Array {
    static get [Symbol.species]() {
        return Array;
    }
}

const arr = new MyArray(1, 2, 3);
const mapped = arr.map(x => x * 2);

console.log(mapped instanceof MyArray);  // false
console.log(mapped instanceof Array);    // true
```

## 14.5. Practical Use Cases

### 14.5.1. Private-like Properties

```javascript
const _balance = Symbol('balance');
const _password = Symbol('password');

class BankAccount {
    constructor(balance, password) {
        this[_balance] = balance;
        this[_password] = password;
    }

    getBalance(password) {
        if (password === this[_password]) {
            return this[_balance];
        }
        throw new Error('Invalid password');
    }

    deposit(amount, password) {
        if (password === this[_password]) {
            this[_balance] += amount;
        }
    }
}

const account = new BankAccount(1000, 'secret');
console.log(account.getBalance('secret'));  // 1000
// account._balance  // undefined
// account[_balance]  // Can access if have symbol reference
```

### 14.5.2. Enum-like Values

```javascript
const Direction = {
    UP: Symbol('up'),
    DOWN: Symbol('down'),
    LEFT: Symbol('left'),
    RIGHT: Symbol('right')
};

function move(direction) {
    switch (direction) {
        case Direction.UP:
            console.log('Moving up');
            break;
        case Direction.DOWN:
            console.log('Moving down');
            break;
        // ...
    }
}

move(Direction.UP);
```

### 14.5.3. Avoiding Name Collisions

```javascript
// Library code
const myLib = (function() {
    const _internal = Symbol('internal');

    return {
        [_internal]: 'internal data',

        publicMethod() {
            return this[_internal];
        }
    };
})();

// User code can't accidentally override
const obj = {
    ...myLib,
    _internal: 'user data'  // Different property
};
```

### 14.5.4. Metadata

```javascript
const TYPE = Symbol('type');
const VALIDATE = Symbol('validate');

class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
        this[TYPE] = 'User';
    }

    [VALIDATE]() {
        return this.name && this.email;
    }

    isValid() {
        return this[VALIDATE]();
    }
}
```

### 14.5.5. Constants

```javascript
const STATUS = {
    PENDING: Symbol('pending'),
    APPROVED: Symbol('approved'),
    REJECTED: Symbol('rejected')
};

class Request {
    constructor() {
        this.status = STATUS.PENDING;
    }

    approve() {
        this.status = STATUS.APPROVED;
    }

    reject() {
        this.status = STATUS.REJECTED;
    }

    isPending() {
        return this.status === STATUS.PENDING;
    }
}
```

## 14.6. Custom Iterator

### 14.6.1. Range Iterator

```javascript
const range = {
    from: 1,
    to: 5,

    [Symbol.iterator]() {
        return {
            current: this.from,
            last: this.to,

            next() {
                if (this.current <= this.last) {
                    return { value: this.current++, done: false };
                }
                return { done: true };
            }
        };
    }
};

console.log([...range]);  // [1, 2, 3, 4, 5]

for (const num of range) {
    console.log(num);  // 1, 2, 3, 4, 5
}
```

### 14.6.2. Reverse Iterator

```javascript
Array.prototype[Symbol.for('reverseIterator')] = function() {
    let index = this.length - 1;
    return {
        next: () => {
            if (index >= 0) {
                return { value: this[index--], done: false };
            }
            return { done: true };
        }
    };
};

const arr = [1, 2, 3, 4, 5];
const reverseIter = arr[Symbol.for('reverseIterator')]();

console.log(reverseIter.next().value);  // 5
console.log(reverseIter.next().value);  // 4
```

## 14.7. Well-known Symbols List

```javascript
Symbol.iterator        // Make object iterable
Symbol.toStringTag     // Customize Object.prototype.toString()
Symbol.toPrimitive     // Customize type conversion
Symbol.hasInstance     // Customize instanceof
Symbol.species         // Customize derived objects
Symbol.isConcatSpreadable  // Control Array.concat()
Symbol.unscopables     // Hide properties from with
Symbol.match           // Used by String.match()
Symbol.replace         // Used by String.replace()
Symbol.search          // Used by String.search()
Symbol.split           // Used by String.split()
Symbol.asyncIterator   // Make object async iterable
```

## 14.8. Best Practices

### 14.8.1. Use for Private Properties

```javascript
// Good: Use symbols for internal properties
const _private = Symbol('private');

class MyClass {
    constructor() {
        this[_private] = 'internal data';
    }
}

// Not truly private but harder to access
```

### 14.8.2. Use for Constants

```javascript
// Good: Unique constants
const STATUS = {
    ACTIVE: Symbol('active'),
    INACTIVE: Symbol('inactive')
};

// vs strings (can have collisions)
const STATUS = {
    ACTIVE: 'active',
    INACTIVE: 'inactive'
};
```

### 14.8.3. Document Symbol Usage

```javascript
// Good: Clear documentation
const ID = Symbol('id');  // Unique identifier

class User {
    constructor(id, name) {
        this[ID] = id;  // Private ID
        this.name = name;
    }
}
```

## 14.9. Common Mistakes

### 14.9.1. Using Symbol() vs Symbol.for()

```javascript
// Different symbols
const sym1 = Symbol('test');
const sym2 = Symbol('test');
console.log(sym1 === sym2);  // false

// Same symbol
const sym1 = Symbol.for('test');
const sym2 = Symbol.for('test');
console.log(sym1 === sym2);  // true
```

### 14.9.2. Symbols Not Enumerable

```javascript
const obj = {
    [Symbol('key')]: 'value'
};

// Won't work
console.log(Object.keys(obj));  // []

// Use this
console.log(Object.getOwnPropertySymbols(obj));
```

### 14.9.3. Symbols Not Strings

```javascript
const sym = Symbol('test');

// Error
const key = 'test';
console.log(obj[key]);  // Not the symbol property

// Correct
console.log(obj[sym]);
```

## 14.6. Real-world Use Cases

### Use Case 1: Private Instance Variables

```javascript
const _secret = Symbol('secret');
const _counter = Symbol('counter');

class SecureObject {
    constructor(secret) {
        this[_secret] = secret;
        this[_counter] = 0;
    }

    getSecret(password) {
        this[_counter]++;
        if (password !== 'mypassword') {
            throw new Error('Invalid password');
        }
        return this[_secret];
    }

    getAccessCount() {
        return this[_counter];
    }
}

// Usage
const obj = new SecureObject('sensitive data');
console.log(obj.getSecret('mypassword')); // 'sensitive data'
console.log(obj.getAccessCount()); // 1
// obj[_secret]; // undefined - not directly accessible
// obj.secret; // undefined
```

### Use Case 2: Plugin System with Well-known Symbols

```javascript
const PLUGIN_TYPE = Symbol.for('plugin.type');
const PLUGIN_INIT = Symbol.for('plugin.init');
const PLUGIN_EXECUTE = Symbol.for('plugin.execute');

class PluginManager {
    constructor() {
        this.plugins = new Map();
    }

    register(name, plugin) {
        if (typeof plugin[PLUGIN_INIT] !== 'function') {
            throw new Error('Plugin must implement init method');
        }
        plugin[PLUGIN_INIT]();
        this.plugins.set(name, plugin);
    }

    execute(name, ...args) {
        const plugin = this.plugins.get(name);
        if (!plugin) throw new Error('Plugin not found');
        if (typeof plugin[PLUGIN_EXECUTE] !== 'function') {
            throw new Error('Plugin must implement execute method');
        }
        return plugin[PLUGIN_EXECUTE](...args);
    }
}

// Plugin implementation
const myPlugin = {
    [PLUGIN_INIT]() {
        console.log('Plugin initialized');
    },
    [PLUGIN_EXECUTE](data) {
        return data.toUpperCase();
    }
};

const manager = new PluginManager();
manager.register('text-plugin', myPlugin);
console.log(manager.execute('text-plugin', 'hello')); // 'HELLO'
```

### Use Case 3: Event Type Constants

```javascript
const EventType = {
    CLICK: Symbol('click'),
    FOCUS: Symbol('focus'),
    BLUR: Symbol('blur'),
    CHANGE: Symbol('change'),
    SUBMIT: Symbol('submit')
};

class EventBus {
    constructor() {
        this.events = new Map();
    }

    on(eventType, handler) {
        if (!this.events.has(eventType)) {
            this.events.set(eventType, new Set());
        }
        this.events.get(eventType).add(handler);

        // Return unsubscribe function
        return () => this.off(eventType, handler);
    }

    off(eventType, handler) {
        if (this.events.has(eventType)) {
            this.events.get(eventType).delete(handler);
        }
    }

    emit(eventType, data) {
        if (this.events.has(eventType)) {
            this.events.get(eventType).forEach(handler => handler(data));
        }
    }
}

// Usage
const bus = new EventBus();
bus.on(EventType.CLICK, (data) => console.log('Clicked:', data));
bus.on(EventType.CHANGE, (data) => console.log('Changed:', data));

bus.emit(EventType.CLICK, { x: 10, y: 20 });
bus.emit(EventType.CHANGE, { newValue: 'test' });
```

### Use Case 4: Metadata Tagging with Symbol.toStringTag

```javascript
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    get [Symbol.toStringTag]() {
        return 'User';
    }

    toJSON() {
        return { name: this.name, email: this.email };
    }
}

class Admin extends User {
    constructor(name, email, permissions) {
        super(name, email);
        this.permissions = permissions;
    }

    get [Symbol.toStringTag]() {
        return 'Admin';
    }
}

// Usage
const user = new User('John', 'john@example.com');
const admin = new Admin('Jane', 'jane@example.com', ['read', 'write', 'delete']);

console.log(Object.prototype.toString.call(user)); // "[object User]"
console.log(Object.prototype.toString.call(admin)); // "[object Admin]"
console.log(JSON.stringify(user)); // {"name":"John","email":"john@example.com"}
```

### Use Case 5: Configuration with Symbol Keys

```javascript
const CONFIG_KEYS = {
    API_KEY: Symbol('api_key'),
    DATABASE_URL: Symbol('database_url'),
    SECRET: Symbol('secret'),
    TIMEOUT: Symbol('timeout')
};

class Configuration {
    constructor() {
        this.config = {};
    }

    set(key, value) {
        this.config[key] = value;
    }

    get(key) {
        return this.config[key];
    }

    // Only return non-symbol keys for public API
    getPublicConfig() {
        const result = {};
        for (const [key, value] of Object.entries(this.config)) {
            result[key] = value;
        }
        return result;
    }

    // Include symbol keys for internal use
    getAllConfig() {
        const result = {};
        for (const key in this.config) {
            result[key] = this.config[key];
        }
        // Add symbols
        for (const sym of Object.getOwnPropertySymbols(this.config)) {
            result[sym] = this.config[sym];
        }
        return result;
    }
}

const config = new Configuration();
config.set('appName', 'MyApp');
config.set(CONFIG_KEYS.API_KEY, 'secret-key-123');
config.set(CONFIG_KEYS.SECRET, 'very-secret');

console.log(config.getPublicConfig()); // { appName: 'MyApp' }
console.log(config.get(CONFIG_KEYS.API_KEY)); // 'secret-key-123'
```

## 14.7. Tips & Tricks

### Tip 1: Symbol Description for Debugging

```javascript
// Good: Use meaningful descriptions
const userId = Symbol('user:id');
const userData = Symbol('user:data');

console.log(userId.description); // 'user:id'
console.log(userId.toString()); // 'Symbol(user:id)'

// Helpful for debugging
const symbols = [userId, userData];
symbols.forEach(sym => {
    console.log(`Symbol: ${sym.description}`);
});
```

### Tip 2: Global Symbol Registry

```javascript
// Symbol.for - shared across all realms
const globalSymbol1 = Symbol.for('app.id');
const globalSymbol2 = Symbol.for('app.id');

console.log(globalSymbol1 === globalSymbol2); // true

// Getting key back from global symbol
console.log(Symbol.keyFor(globalSymbol1)); // 'app.id'

// Useful for cross-window/cross-context communication
// Works even in different iframes or workers
```

### Tip 3: Symbol with Objects Pattern

```javascript
// Store symbol separately for security
const privateData = Symbol('privateData');

class MyClass {
    constructor() {
        this[privateData] = { secret: 'value' };
    }

    getData() {
        return this[privateData];
    }
}

// Export only the symbol to trusted code
export { MyClass, privateData };
```

### Tip 4: Custom Iterator with Multiple Symbols

```javascript
const iteratorProtocol = Symbol.iterator;
const asyncIterator = Symbol.asyncIterator;

class DualIterator {
    constructor(items) {
        this.items = items;
    }

    [iteratorProtocol]() {
        return {
            index: 0,
            items: this.items,
            next() {
                if (this.index < this.items.length) {
                    return { value: this.items[this.index++], done: false };
                }
                return { done: true };
            }
        };
    }

    async *[asyncIterator]() {
        for (const item of this.items) {
            await new Promise(resolve => setTimeout(resolve, 100));
            yield item;
        }
    }
}

// Usage
const iter = new DualIterator([1, 2, 3]);
console.log([...iter]); // [1, 2, 3]

// For async: for await (const item of iter) { ... }
```

### Tip 5: Symbol Masquerading Prevention

```javascript
// Prevent Symbol spoofing by using Object.freeze
const mySymbol = Symbol('important');
const obj = Object.freeze({
    [mySymbol]: 'value'
});

// Can't modify
obj[mySymbol] = 'new value'; // Silently fails (or error in strict mode)

// Can still read
console.log(obj[mySymbol]); // 'value'
```

### Tip 6: Enum Pattern with Symbols

```javascript
const Status = Object.freeze({
    PENDING: Symbol('pending'),
    PROCESSING: Symbol('processing'),
    SUCCESS: Symbol('success'),
    FAILED: Symbol('failed')
});

// Type-safe enum
class Task {
    constructor(name) {
        this.name = name;
        this.status = Status.PENDING;
    }

    setStatus(status) {
        // Ensure it's a valid status
        if (![Status.PENDING, Status.PROCESSING, Status.SUCCESS, Status.FAILED].includes(status)) {
            throw new Error('Invalid status');
        }
        this.status = status;
    }

    isStatus(status) {
        return this.status === status;
    }
}
```

### Tip 7: Symbol Namespacing

```javascript
// Create namespaced symbols
const MyLib = (() => {
    const internal = {
        VERSION: Symbol('version'),
        STATE: Symbol('state'),
        CONFIG: Symbol('config')
    };

    return {
        internal,
        createObject() {
            return {
                [internal.VERSION]: '1.0.0',
                [internal.STATE]: {},
                [internal.CONFIG]: {}
            };
        }
    };
})();

const obj = MyLib.createObject();
console.log(obj[MyLib.internal.VERSION]); // '1.0.0'
```

### Tip 8: Symbol with WeakMap for Private Data

```javascript
const privateDataMap = new WeakMap();
const instanceId = Symbol('instanceId');

class SecureClass {
    constructor(data) {
        privateDataMap.set(this, { data, id: Math.random() });
        this[instanceId] = Math.random(); // Additional identifier
    }

    getData() {
        const priv = privateDataMap.get(this);
        return priv ? priv.data : null;
    }
}

// Multiple layers of privacy
const instance = new SecureClass('secret');
console.log(instance[instanceId]); // Random number (public but obscured)
console.log(instance.getData()); // 'secret' (via method)
// Direct access to privateDataMap is not possible without reference
```

### Tip 9: Type Checking with Symbol.toStringTag

```javascript
const getType = (obj) => Object.prototype.toString.call(obj).slice(8, -1);

class CustomObject {
    get [Symbol.toStringTag]() {
        return 'CustomObject';
    }
}

const obj = new CustomObject();
console.log(getType(obj)); // 'CustomObject'

// Use for type checking
function processData(data) {
    switch (getType(data)) {
        case 'CustomObject':
            console.log('Processing custom object');
            break;
        case 'Array':
            console.log('Processing array');
            break;
        default:
            console.log('Unknown type');
    }
}
```

### Tip 10: Symbol in Validation

```javascript
const validSymbols = new Set([
    Symbol.for('valid.payment'),
    Symbol.for('valid.user'),
    Symbol.for('valid.product')
]);

class Validator {
    static validate(obj, symbolType) {
        return validSymbols.has(symbolType) && Symbol.keyFor(symbolType);
    }

    static mark(obj, symbolType) {
        if (this.validate(obj, symbolType)) {
            obj[symbolType] = true;
            return true;
        }
        return false;
    }

    static hasValidation(obj, symbolType) {
        return obj[symbolType] === true;
    }
}

// Usage
const payment = {};
Validator.mark(payment, Symbol.for('valid.payment'));
console.log(Validator.hasValidation(payment, Symbol.for('valid.payment'))); // true
```

## 14.8. Common Mistakes

### Mistake 1: Symbols are Not Strings

```javascript
// WRONG
const id = Symbol('id');
const key = 'id';

const obj = {};
obj[id] = 123;
obj[key] = 456;

console.log(obj[id]); // 123 (symbol property)
console.log(obj[key]); // 456 (string property)
console.log(obj.id); // 456 (accesses string property)

// They are different!
```

### Mistake 2: Symbols Not Enumerable

```javascript
// WRONG: Forgetting that symbols aren't enumerable
const sym = Symbol('key');
const obj = {
    name: 'John',
    [sym]: 'value'
};

// This doesn't include the symbol
const keys = Object.keys(obj); // ['name']
const entries = Object.entries(obj); // [['name', 'John']]

// RIGHT: Use Reflect.ownKeys or getOwnPropertySymbols
const allKeys = Reflect.ownKeys(obj); // ['name', Symbol(key)]
const symbols = Object.getOwnPropertySymbols(obj); // [Symbol(key)]
```

### Mistake 3: Symbol.for vs Symbol() Confusion

```javascript
// WRONG: Mixing global and local symbols
const global = Symbol.for('test');
const local = Symbol('test');

console.log(global === local); // false - different!
console.log(Symbol.keyFor(global)); // 'test'
console.log(Symbol.keyFor(local)); // undefined - not global

// RIGHT: Be consistent
const sharedSymbol = Symbol.for('config.shared');
const internalSymbol = Symbol('internal');
```

### Mistake 4: Serialization Issues

```javascript
// WRONG: Symbols can't be serialized
const obj = {
    name: 'John',
    [Symbol('id')]: 123
};

const json = JSON.stringify(obj);
console.log(json); // {"name":"John"} - symbol lost!

// RIGHT: Extract non-symbol data
const serialize = (obj) => {
    return JSON.stringify(
        Object.fromEntries(
            Object.entries(obj)
        )
    );
};
```

### Mistake 5: Symbol in Property Destructuring

```javascript
// WRONG: Can't destructure symbols easily
const id = Symbol('id');
const obj = { [id]: 123, name: 'John' };

const { id: extractedId } = obj; // Tries to destructure string 'id'
console.log(extractedId); // undefined

// RIGHT: Access directly
const extractedId = obj[id]; // 123
```

### Mistake 6: Well-known Symbol Override

```javascript
// WRONG: Accidentally breaking built-in behavior
const obj = {
    [Symbol.iterator]() {
        return [1, 2, 3];  // Should return iterator, not array!
    }
};

// for (const x of obj) { } // Error!

// RIGHT: Implement properly
const correctObj = {
    [Symbol.iterator]() {
        let i = 0;
        const data = [1, 2, 3];
        return {
            next() {
                return i < data.length ? { value: data[i++] } : { done: true };
            }
        };
    }
};

for (const x of correctObj) { console.log(x); } // 1, 2, 3
```

### Mistake 7: Symbol with Spread Operator

```javascript
// WRONG: Spread doesn't copy symbols
const id = Symbol('id');
const original = { name: 'John', [id]: 123 };
const copy = { ...original };

console.log(copy[id]); // undefined - symbol lost!

// RIGHT: Copy symbols separately
const fullCopy = {
    ...original,
    ...Object.getOwnPropertySymbols(original).reduce((acc, sym) => {
        acc[sym] = original[sym];
        return acc;
    }, {})
};

console.log(fullCopy[id]); // 123
```

### Mistake 8: Symbol.for in Closures

```javascript
// WRONG: Assuming Symbol.for creates new symbols
function createModule() {
    const id = Symbol.for('module.id');
    return { id };
}

const mod1 = createModule();
const mod2 = createModule();

console.log(mod1.id === mod2.id); // true! Same symbol
// This might not be intended behavior

// RIGHT: Use local symbols for unique instances
function createModule() {
    const id = Symbol('module.id');
    return { id };
}

const mod1 = createModule();
const mod2 = createModule();

console.log(mod1.id === mod2.id); // false - unique per instance
```

### Mistake 9: Symbol Comparison

```javascript
// WRONG: Comparing symbols incorrectly
const id1 = Symbol('id');
const id2 = Symbol('id');

if (id1 == id2) { } // Always false
if (typeof id1 === 'symbol') { } // Correct type checking

// RIGHT: Always use ===
const sym = Symbol('test');
if (objectId === sym) { // Correct comparison
    // ...
}
```

### Mistake 10: Missing Error Handling for Symbol Conversion

```javascript
// WRONG: Trying to convert symbol to string
const sym = Symbol('test');
const str = String(sym); // Works: 'Symbol(test)'
const num = Number(sym); // TypeError!

// RIGHT: Handle conversion carefully
const sym = Symbol('test');
const str = sym.toString(); // 'Symbol(test)'
// Don't try to convert to number
```

## 14.9. Troubleshooting Issues

### Issue 1: Symbol Leakage in Object Inspection

**Problem:**
```javascript
const privateId = Symbol('id');

class User {
    constructor(id) {
        this[privateId] = id;
    }
}

const user = new User(123);

// Symbols visible in dev tools
console.log(user); // Can see the symbol

// Symbols accessible via reflection
Object.getOwnPropertySymbols(user); // [Symbol(id)]
```

**Solution:**
```javascript
// Use WeakMap for better encapsulation
const userData = new WeakMap();

class SecureUser {
    constructor(id) {
        userData.set(this, { id });
    }

    getId() {
        return userData.get(this).id;
    }
}

const user = new SecureUser(123);
// user.id // undefined
// userData is not directly accessible
```

### Issue 2: Well-known Symbol Not Working

**Problem:**
```javascript
class MyIterable {
    [Symbol.iterator] = function() { // Arrow function!
        return [1, 2, 3];
    };
}

const obj = new MyIterable();
[...obj]; // TypeError
```

**Solution:**
```javascript
class MyIterable {
    [Symbol.iterator]() { // Method syntax
        let i = 0;
        const data = [1, 2, 3];
        return {
            next: () => i < data.length ? { value: data[i++] } : { done: true }
        };
    }
}

const obj = new MyIterable();
console.log([...obj]); // [1, 2, 3]
```

### Issue 3: Symbol Not Found in Object

**Problem:**
```javascript
const id = Symbol('id');
const name = Symbol.for('name');

const obj = {
    [id]: 'value1'
    // Missing [name] property
};

console.log(obj[name]); // undefined - confusing!
```

**Solution:**
```javascript
const id = Symbol('id');
const name = Symbol.for('name');

const obj = {
    [id]: 'value1',
    [name]: 'value2'
};

console.log(obj[name]); // 'value2'

// Or check before accessing
if (obj.hasOwnProperty(name)) {
    console.log(obj[name]);
} else {
    console.log('Not found');
}
```

### Issue 4: Symbol Registry Pollution

**Problem:**
```javascript
// Global registry can cause conflicts
const userIdSymbol = Symbol.for('user.id');

// Different code elsewhere
const userId = Symbol.for('user.id');

// Now they're the same - might cause issues if not intended
```

**Solution:**
```javascript
// Use namespaced keys in registry
const userIdSymbol = Symbol.for('myapp.user.id');
const userNameSymbol = Symbol.for('myapp.user.name');

// Or stick to local symbols for internal use
const internalId = Symbol('internal.id');
const internalName = Symbol('internal.name');

// Use global registry only for inter-module communication
const PUBLIC_ID = Symbol.for('public.component.id');
```

### Issue 5: Symbol Loss in Serialization

**Problem:**
```javascript
const id = Symbol('id');

const data = {
    userId: 123,
    [id]: 'secret'
};

const json = JSON.stringify(data);
const restored = JSON.parse(json);

console.log(restored[id]); // undefined - lost!
```

**Solution:**
```javascript
class SymbolPreservingMap {
    constructor(obj) {
        this.data = obj;
        this.symbols = new Map();
        this._captureSymbols(obj);
    }

    _captureSymbols(obj) {
        Object.getOwnPropertySymbols(obj).forEach(sym => {
            this.symbols.set(Symbol.keyFor(sym) || sym.toString(), obj[sym]);
        });
    }

    toJSON() {
        return {
            data: this.data,
            symbolData: Array.from(this.symbols.entries())
        };
    }

    static fromJSON(json) {
        const obj = { ...json.data };
        json.symbolData.forEach(([key, value]) => {
            const sym = Symbol.for(key);
            obj[sym] = value;
        });
        return obj;
    }
}
```

### Issue 6: Symbol Not Working as Map Key

**Problem:**
```javascript
const idSymbol = Symbol('id');

const map = new Map();
map.set(idSymbol, 'value');
map.set('id', 'different value'); // Same key visually, different in map

console.log(map.size); // 2 - both stored separately
```

**Solution:**
```javascript
const idSymbol = Symbol('id');

const map = new Map();
map.set(idSymbol, 'value1');
map.set('id', 'value2');

// Correct access
console.log(map.get(idSymbol)); // 'value1'
console.log(map.get('id')); // 'value2'

// Be explicit about which you're using
const getById = (key) => {
    if (typeof key === 'symbol') {
        return map.get(key);
    } else {
        return map.get(String(key));
    }
};
```

### Issue 7: Class Methods with Symbols

**Problem:**
```javascript
const execute = Symbol('execute');

class Task {
    [execute]() {
        console.log('Executing');
    }
}

const task = new Task();
task.execute(); // Error - method not found
task[execute](); // Works but ugly
```

**Solution:**
```javascript
const _execute = Symbol('execute');
const _validate = Symbol('validate');

class Task {
    [_execute]() {
        if (this[_validate]()) {
            console.log('Executing');
        }
    }

    [_validate]() {
        return true;
    }

    // Public method calls private
    execute() {
        this[_execute]();
    }
}

const task = new Task();
task.execute(); // Clean public API
```

### Issue 8: Symbol and instanceof

**Problem:**
```javascript
const type = Symbol('type');

class MyClass {
    constructor() {
        this[type] = 'MyClass';
    }
}

const obj = new MyClass();

console.log(obj instanceof MyClass); // true
console.log(obj[type]); // 'MyClass'

// But Symbol doesn't help with instanceof checks
const obj2 = { [type]: 'MyClass' };
console.log(obj2 instanceof MyClass); // false
```

**Solution:**
```javascript
const TYPE = Symbol.for('type');

class Validator {
    static isType(obj, typeName) {
        return obj[TYPE] === typeName;
    }
}

class MyClass {
    constructor() {
        this[TYPE] = 'MyClass';
    }
}

const obj = new MyClass();
console.log(Validator.isType(obj, 'MyClass')); // true
```

### Issue 9: Symbol Description Unavailable

**Problem:**
```javascript
// In older environments
const sym = Symbol('test');
console.log(sym.description); // undefined (pre-ES2019)
```

**Solution:**
```javascript
// Polyfill for older environments
if (!Symbol.prototype.description) {
    Object.defineProperty(Symbol.prototype, 'description', {
        get() {
            const match = this.toString().match(/Symbol\((.*)\)/);
            return match ? match[1] : undefined;
        }
    });
}

const sym = Symbol('test');
console.log(sym.description); // 'test'
```

### Issue 10: Iterating Over Symbols

**Problem:**
```javascript
const id = Symbol('id');
const obj = { name: 'John', [id]: 123 };

for (const key in obj) {
    console.log(key); // Only 'name', symbol not included
}

// Also doesn't include symbols
Object.keys(obj); // ['name']
Object.entries(obj); // [['name', 'John']]
```

**Solution:**
```javascript
const id = Symbol('id');
const obj = { name: 'John', [id]: 123 };

// Get all keys including symbols
const allKeys = Reflect.ownKeys(obj);
console.log(allKeys); // ['name', Symbol(id)]

// Or just symbols
const symbols = Object.getOwnPropertySymbols(obj);
console.log(symbols); // [Symbol(id)]

// Iterate over all
allKeys.forEach(key => {
    console.log(key, obj[key]);
});
```

## 14.10. Advanced Topics

### Advanced Topic 1: Symbol Iterator Protocol

```javascript
class Range {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    [Symbol.iterator]() {
        let current = this.start;
        const end = this.end;

        return {
            next() {
                if (current <= end) {
                    return { value: current++, done: false };
                }
                return { done: true };
            }
        };
    }
}

// Can now use in for...of, spread, destructuring
for (const num of new Range(1, 5)) {
    console.log(num); // 1, 2, 3, 4, 5
}

const [first, second, ...rest] = new Range(1, 10);
console.log([first, second, rest]); // [1, 2, [3, 4, 5, 6, 7, 8, 9, 10]]
```

### Advanced Topic 2: Custom Object Behavior with Symbol.toPrimitive

```javascript
class Price {
    constructor(amount, currency = 'USD') {
        this.amount = amount;
        this.currency = currency;
    }

    [Symbol.toPrimitive](hint) {
        switch (hint) {
            case 'number':
                return this.amount;
            case 'string':
                return `${this.currency} ${this.amount}`;
            default:
                return this.amount;
        }
    }

    toString() {
        return `${this.currency} ${this.amount}`;
    }

    valueOf() {
        return this.amount;
    }
}

const price = new Price(99.99, 'EUR');

console.log(`Price: ${price}`); // "Price: EUR 99.99"
console.log(price + 10); // 109.99 (number hint)
console.log(Number(price)); // 99.99
console.log(String(price)); // "EUR 99.99"
console.log(price == 99.99); // true
```

### Advanced Topic 3: Symbol and Property Descriptors

```javascript
const secret = Symbol('secret');

class SecureData {
    constructor(data) {
        Object.defineProperty(this, secret, {
            value: data,
            writable: false,
            enumerable: false,
            configurable: false
        });
    }

    getData(password) {
        if (password !== 'correct') {
            throw new Error('Unauthorized');
        }
        return this[secret];
    }
}

const secure = new SecureData('classified');

// Can't enumerate
Object.getOwnPropertySymbols(secure); // [Symbol(secret)]

// Can't modify
secure[secret] = 'hacked'; // Fails silently or error in strict mode

// Can read via method
console.log(secure.getData('correct')); // 'classified'

// Property descriptor shows restrictions
const desc = Object.getOwnPropertyDescriptor(secure, secret);
console.log(desc.writable); // false
```

### Advanced Topic 4: Meta-programming with Well-known Symbols

```javascript
class Observable {
    constructor(items) {
        this.items = items;
    }

    [Symbol.iterator]() {
        return this.items[Symbol.iterator]();
    }

    [Symbol.toStringTag] = 'Observable';

    static [Symbol.species] = Array;

    filter(predicate) {
        const filtered = this.items.filter(predicate);
        return new this.constructor[Symbol.species](...filtered);
    }

    map(fn) {
        const mapped = this.items.map(fn);
        return new this.constructor[Symbol.species](...mapped);
    }
}

const obs = new Observable([1, 2, 3, 4, 5]);
console.log(Object.prototype.toString.call(obs)); // "[object Observable]"

const filtered = obs.filter(x => x > 2);
console.log(filtered instanceof Array); // true
console.log(filtered); // [3, 4, 5]
```

### Advanced Topic 5: Branded Type Pattern with Symbols

```javascript
// Create unique brands for different types
const userId = Symbol('userId');
const orderId = Symbol('orderId');

class BrandedType {
    static create(brand, value) {
        return { [brand]: value };
    }

    static extract(brand, obj) {
        if (!(brand in obj)) {
            throw new Error('Invalid branded type');
        }
        return obj[brand];
    }
}

// Usage - type-safe wrapper
const user123 = BrandedType.create(userId, 123);
const order456 = BrandedType.create(orderId, 456);

console.log(BrandedType.extract(userId, user123)); // 123

// Can't mix up types
try {
    BrandedType.extract(orderId, user123); // Error
} catch (e) {
    console.log('Type mismatch detected');
}
```

## 14.11. Exercises

### Exercise 1 (Dễ): Create Symbol Properties

```javascript
// Create object with symbol properties
function createSecureObj() {
    const SECRET = Symbol('secret');
    return {
        [SECRET]: 'hidden value',
        getSecret() {
            // Return value of SECRET
        }
    };
}

const obj = createSecureObj();
console.log(obj.getSecret()); // 'hidden value'
```

### Exercise 2 (Dễ): Symbol Description

```javascript
// Create symbols with descriptions
const userId = Symbol('user:id');
const userData = Symbol('user:data');

// Get descriptions
console.log(userId.description); // 'user:id'
console.log(userData.description); // 'user:data'
```

### Exercise 3 (Dễ): Symbol.for vs Symbol()

```javascript
// Compare global and local symbols
const global1 = Symbol.for('test');
const global2 = Symbol.for('test');
const local1 = Symbol('test');
const local2 = Symbol('test');

console.log(global1 === global2); // true
console.log(local1 === local2);   // false
```

### Exercise 4 (Dễ): Custom toString with Symbol.toStringTag

```javascript
// Create class with custom toString
class MyClass {
    get [Symbol.toStringTag]() {
        // Return custom tag
    }
}

const obj = new MyClass();
console.log(Object.prototype.toString.call(obj)); // "[object MyClass]"
```

### Exercise 5 (Trung bình): Private Properties with Symbols

```javascript
// Create class with private properties
class BankAccount {
    constructor(balance) {
        // Use symbol for balance
    }

    getBalance() {
        // Return balance
    }

    deposit(amount) {
        // Add to balance
    }
}

const account = new BankAccount(1000);
console.log(account.getBalance()); // 1000
account.deposit(500);
console.log(account.getBalance()); // 1500
```

### Exercise 6 (Trung bình): Custom Iterator with Symbol

```javascript
// Create iterable class
class Fibonacci {
    constructor(limit) {
        this.limit = limit;
    }

    [Symbol.iterator]() {
        // Implement fibonacci iteration
    }
}

const fib = new Fibonacci(10);
console.log([...fib]); // [1, 1, 2, 3, 5, 8]
```

### Exercise 7 (Trung bình): Enum Pattern

```javascript
// Create enum using symbols
const Status = {
    PENDING: Symbol('pending'),
    APPROVED: Symbol('approved'),
    REJECTED: Symbol('rejected')
};

class Request {
    constructor() {
        this.status = Status.PENDING;
    }

    approve() {
        this.status = Status.APPROVED;
    }

    isApproved() {
        return this.status === Status.APPROVED;
    }
}

const req = new Request();
console.log(req.isApproved()); // false
req.approve();
console.log(req.isApproved()); // true
```

### Exercise 8 (Trung bình): Symbol Registry

```javascript
// Use Symbol.for for shared symbols
const API_KEY = Symbol.for('app.api.key');
const APP_NAME = Symbol.for('app.name');

class Config {
    constructor() {
        this[API_KEY] = 'secret-key-123';
        this[APP_NAME] = 'MyApp';
    }

    getKey() {
        return this[API_KEY];
    }
}

const config = new Config();
console.log(config.getKey()); // 'secret-key-123'
```

### Exercise 9 (Khó): Plugin System

```javascript
// Implement plugin system using symbols
const INIT = Symbol.for('plugin.init');
const EXECUTE = Symbol.for('plugin.execute');

class PluginSystem {
    constructor() {
        this.plugins = new Map();
    }

    register(name, plugin) {
        // Register plugin
    }

    execute(name, ...args) {
        // Execute plugin
    }
}

// Create a plugin
const plugin = {
    [INIT]() { console.log('Plugin initialized'); },
    [EXECUTE](data) { return data.toUpperCase(); }
};

const system = new PluginSystem();
system.register('text', plugin);
console.log(system.execute('text', 'hello')); // 'HELLO'
```

### Exercise 10 (Khó): Event System

```javascript
// Create event system with symbol-based event types
const EventType = {
    CLICK: Symbol('click'),
    FOCUS: Symbol('focus'),
    CHANGE: Symbol('change')
};

class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    on(type, handler) {
        // Subscribe to event
    }

    off(type, handler) {
        // Unsubscribe
    }

    emit(type, data) {
        // Emit event
    }
}

const emitter = new EventEmitter();
emitter.on(EventType.CLICK, (data) => console.log('Clicked:', data));
emitter.emit(EventType.CLICK, { x: 10, y: 20 });
```

### Exercise 11 (Khó): Secure Object Wrapper

```javascript
// Create wrapper for secure object access
class SecureWrapper {
    constructor(data) {
        // Store data with symbol keys
    }

    getProperty(propertyName, password) {
        // Return property if password is correct
    }

    setProperty(propertyName, value, password) {
        // Set property if password is correct
    }
}

const secure = new SecureWrapper({ name: 'John', email: 'john@example.com' });
console.log(secure.getProperty('name', 'correct')); // 'John'
console.log(secure.getProperty('name', 'wrong')); // Error or undefined
```

### Exercise 12 (Khó): Symbol Metadata System

```javascript
// Create metadata system using symbols
class MetadataManager {
    constructor() {
        this.metadata = new Map();
    }

    setMetadata(target, key, value) {
        // Store metadata with symbols
    }

    getMetadata(target, key) {
        // Retrieve metadata
    }

    getAllMetadata(target) {
        // Get all metadata for target
    }
}

const manager = new MetadataManager();
const obj = {};

manager.setMetadata(obj, 'type', 'User');
manager.setMetadata(obj, 'version', 1);

console.log(manager.getMetadata(obj, 'type')); // 'User'
```

---

**Kết luận:** Symbols cung cấp unique identifiers, hữu ích cho private properties, constants, và customizing object behavior với well-known symbols.

**Chương tiếp theo:** Iterators & Generators
