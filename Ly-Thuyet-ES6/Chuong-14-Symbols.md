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

## 14.10. Exercises

### Exercise 1: Private Properties

```javascript
// Create a class with symbol-based private properties
class Person {
    // Use symbols for private name and age
}
```

### Exercise 2: Custom Iterator

```javascript
// Create iterable object that yields squares
const squares = {
    // Implement Symbol.iterator
};

console.log([...squares]);  // [1, 4, 9, 16, 25]
```

### Exercise 3: Enum

```javascript
// Create enum-like object using symbols
const Color = {
    // RED, GREEN, BLUE as symbols
};
```

---

**Kết luận:** Symbols cung cấp unique identifiers, hữu ích cho private properties, constants, và customizing object behavior với well-known symbols.

**Chương tiếp theo:** Iterators & Generators
