# CHƯƠNG 2: LET, CONST VÀ BLOCK SCOPE

## 2.1. Vấn đề với VAR

### 2.1.1. Function Scope

```javascript
// var is function-scoped
function example() {
    var x = 1;
    if (true) {
        var x = 2;  // Same variable!
        console.log(x);  // 2
    }
    console.log(x);  // 2 (not 1!)
}
```

### 2.1.2. Hoisting

```javascript
console.log(x);  // undefined (not error!)
var x = 5;

// Được interpret như:
var x;
console.log(x);  // undefined
x = 5;
```

### 2.1.3. Global Scope Pollution

```javascript
var name = 'John';
var name = 'Jane';  // No error, overwrites

// Loop variable leaks
for (var i = 0; i < 5; i++) {
    // ...
}
console.log(i);  // 5 (still accessible!)
```

## 2.2. LET

### 2.2.1. Block Scope

```javascript
// let is block-scoped
{
    let x = 1;
    console.log(x);  // 1
}
console.log(x);  // ReferenceError: x is not defined
```

### 2.2.2. If Statements

```javascript
if (true) {
    let x = 1;
    console.log(x);  // 1
}
console.log(x);  // ReferenceError
```

### 2.2.3. For Loops

```javascript
// ES5 - var problem
for (var i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i);  // 3, 3, 3
    }, 1000);
}

// ES6 - let solution
for (let i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i);  // 0, 1, 2
    }, 1000);
}
```

### 2.2.4. Temporal Dead Zone (TDZ)

```javascript
// Cannot access before declaration
console.log(x);  // ReferenceError: Cannot access before initialization
let x = 5;

// TDZ example
let x = 1;
{
    console.log(x);  // ReferenceError (TDZ)
    let x = 2;
}
```

### 2.2.5. No Redeclaration

```javascript
let x = 1;
let x = 2;  // SyntaxError: Identifier 'x' has already been declared

// But reassignment is OK
let y = 1;
y = 2;  // OK
```

## 2.3. CONST

### 2.3.1. Constant Values

```javascript
const PI = 3.14159;
console.log(PI);  // 3.14159

PI = 3.14;  // TypeError: Assignment to constant variable
```

### 2.3.2. Must Initialize

```javascript
const x;  // SyntaxError: Missing initializer

const y = 10;  // OK
```

### 2.3.3. Block Scope

```javascript
const MAX = 100;
{
    const MAX = 50;
    console.log(MAX);  // 50
}
console.log(MAX);  // 100
```

### 2.3.4. Objects & Arrays with CONST

**Important:** const prevents reassignment, not mutation!

```javascript
// Objects
const person = { name: 'John' };

person.name = 'Jane';  // OK (mutation)
person.age = 30;       // OK (adding property)

person = {};  // TypeError: Assignment to constant

// Arrays
const numbers = [1, 2, 3];

numbers.push(4);     // OK
numbers[0] = 10;     // OK

numbers = [];  // TypeError: Assignment to constant
```

### 2.3.5. Freezing Objects

```javascript
const person = Object.freeze({ name: 'John' });

person.name = 'Jane';  // Silently fails (strict mode: error)
person.age = 30;       // Silently fails

console.log(person);  // { name: 'John' }

// Deep freeze
const obj = Object.freeze({
    name: 'John',
    address: Object.freeze({
        city: 'NYC'
    })
});
```

## 2.4. VAR vs LET vs CONST

| Feature | var | let | const |
|---------|-----|-----|-------|
| Scope | Function | Block | Block |
| Hoisting | Yes (undefined) | No (TDZ) | No (TDZ) |
| Redeclaration | Yes | No | No |
| Reassignment | Yes | Yes | No |
| Global Object | Yes | No | No |

### 2.4.1. Scope Comparison

```javascript
function scopeTest() {
    var a = 1;
    let b = 2;
    const c = 3;

    if (true) {
        var a = 10;    // Same variable
        let b = 20;    // Different variable
        const c = 30;  // Different variable
        console.log(a, b, c);  // 10, 20, 30
    }

    console.log(a, b, c);  // 10, 2, 3
}
```

### 2.4.2. Hoisting Comparison

```javascript
// var - hoisted to undefined
console.log(a);  // undefined
var a = 1;

// let - TDZ
console.log(b);  // ReferenceError
let b = 2;

// const - TDZ
console.log(c);  // ReferenceError
const c = 3;
```

## 2.5. Block Scope Examples

### 2.5.1. Switch Statements

```javascript
switch (value) {
    case 1: {
        let result = 'One';
        console.log(result);
        break;
    }
    case 2: {
        let result = 'Two';  // Different variable
        console.log(result);
        break;
    }
}
```

### 2.5.2. Try-Catch

```javascript
try {
    let x = 1;
    throw new Error('Test');
} catch (e) {
    let x = 2;  // Different variable
    console.log(x);  // 2
}
```

### 2.5.3. Nested Blocks

```javascript
{
    let x = 1;
    {
        let x = 2;
        {
            let x = 3;
            console.log(x);  // 3
        }
        console.log(x);  // 2
    }
    console.log(x);  // 1
}
```

## 2.6. Practical Examples

### 2.6.1. Loop Closures

```javascript
// Problem with var
const buttons = document.querySelectorAll('button');

for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
        console.log(i);  // Always logs buttons.length
    });
}

// Solution with let
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
        console.log(i);  // Logs correct index
    });
}
```

### 2.6.2. Configuration

```javascript
// Use const for config values
const CONFIG = {
    API_URL: 'https://api.example.com',
    TIMEOUT: 5000,
    MAX_RETRIES: 3
};

// Can modify properties (if needed)
CONFIG.TIMEOUT = 10000;  // OK

// But cannot reassign
CONFIG = {};  // TypeError
```

### 2.6.3. Function Parameters

```javascript
function example(x) {
    // x is like let
    x = 10;  // OK

    let x = 20;  // SyntaxError: duplicate
}
```

## 2.7. Best Practices

### 2.7.1. When to Use Each

**Use const by default:**
```javascript
const name = 'John';
const age = 30;
const users = [];
```

**Use let when you need to reassign:**
```javascript
let counter = 0;
counter++;

let message = 'Loading...';
message = 'Done!';
```

**Avoid var:**
```javascript
// DON'T use var in modern code
var x = 1;  // ❌

// Use let or const
let x = 1;   // ✅
const y = 2; // ✅
```

### 2.7.2. Naming Conventions

```javascript
// Constants (truly constant values)
const MAX_SIZE = 100;
const API_KEY = 'abc123';

// Regular const (can be mutated)
const user = { name: 'John' };
const items = [1, 2, 3];
```

### 2.7.3. Block Scope Strategy

```javascript
// Keep variables in smallest scope possible
{
    const temp = calculate();
    processResult(temp);
}
// temp not accessible here

// Instead of:
const temp = calculate();
processResult(temp);
// temp still accessible (not needed)
```

## 2.8. Common Mistakes

### 2.8.1. Thinking const is Immutable

```javascript
// WRONG assumption
const arr = [1, 2, 3];
arr.push(4);  // This works! arr is not immutable

// const prevents reassignment only
arr = [5, 6, 7];  // TypeError
```

### 2.8.2. Using let in Global Scope

```javascript
// Avoid
let globalVar = 'value';

// Better: use const if not reassigning
const GLOBAL_CONST = 'value';

// Or: use modules (later chapter)
```

### 2.8.3. TDZ Confusion

```javascript
const x = 1;

function test() {
    console.log(x);  // ReferenceError (TDZ)
    const x = 2;
}
```

## 2.9. Exercises

### Exercise 1: Fix the Loop

```javascript
// Fix this code
for (var i = 1; i <= 3; i++) {
    setTimeout(function() {
        console.log(i);
    }, i * 1000);
}
// Current output: 4, 4, 4
// Expected output: 1, 2, 3
```

### Exercise 2: Choose Correct Declaration

```javascript
// Declare these variables correctly
// 1. A counter that increases
// 2. A user's name (won't change)
// 3. An array of items (items can be added)
// 4. Pi constant
```

### Exercise 3: Block Scope

```javascript
// What will this output?
const x = 1;
{
    const x = 2;
    {
        const x = 3;
        console.log(x);
    }
    console.log(x);
}
console.log(x);
```

---

**Kết luận:** Sử dụng `const` mặc định, `let` khi cần reassign, tránh `var`. Block scope giúp code dễ hiểu và tránh bugs.

**Chương tiếp theo:** Arrow Functions
