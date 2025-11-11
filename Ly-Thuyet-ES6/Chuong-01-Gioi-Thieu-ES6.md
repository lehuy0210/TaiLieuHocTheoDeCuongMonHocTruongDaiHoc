# CHƯƠNG 1: GIỚI THIỆU ES6

## 1.1. ES6 (ES2015) là gì?

ES6 (ECMAScript 2015) là phiên bản lớn nhất của JavaScript, được release năm 2015 với nhiều tính năng mới.

### 1.1.1. Lịch sử

- **1995**: JavaScript được tạo ra bởi Brendan Eich
- **1997**: ES1 - First edition
- **1999**: ES3
- **2009**: ES5
- **2015**: ES6/ES2015 - Major update
- **2016+**: Yearly releases (ES2016, ES2017, ...)

### 1.1.2. Tại sao học ES6?

- Modern JavaScript syntax
- Cleaner và readable code
- Powerful features
- Industry standard
- Required cho frameworks (React, Vue, Angular)

## 1.2. Browser Support

**Modern Browsers:**
- Chrome 51+
- Firefox 54+
- Safari 10+
- Edge 15+

**Transpilers (cho old browsers):**
- Babel
- TypeScript

## 1.3. ES6 Features Overview

### 1.3.1. Các tính năng chính

1. **let & const** - Block-scoped variables
2. **Arrow Functions** - Shorter function syntax
3. **Template Literals** - String interpolation
4. **Destructuring** - Extract values from objects/arrays
5. **Spread & Rest** - Spread/collect elements
6. **Classes** - OOP syntax
7. **Modules** - Import/Export
8. **Promises** - Async operations
9. **Default Parameters** - Function parameters
10. **Enhanced Object Literals** - Object shortcuts

## 1.4. Quick Comparison: ES5 vs ES6

### 1.4.1. Variables

**ES5:**
```javascript
var name = 'John';
```

**ES6:**
```javascript
let name = 'John';
const AGE = 30;
```

### 1.4.2. Functions

**ES5:**
```javascript
function add(a, b) {
    return a + b;
}
```

**ES6:**
```javascript
const add = (a, b) => a + b;
```

### 1.4.3. String Concatenation

**ES5:**
```javascript
var greeting = 'Hello, ' + name + '!';
```

**ES6:**
```javascript
const greeting = `Hello, ${name}!`;
```

### 1.4.4. Objects

**ES5:**
```javascript
var obj = {
    name: name,
    age: age,
    greet: function() {
        console.log('Hello');
    }
};
```

**ES6:**
```javascript
const obj = {
    name,
    age,
    greet() {
        console.log('Hello');
    }
};
```

## 1.5. Setup Environment

### 1.5.1. Node.js

```bash
# Check Node version
node --version

# Run ES6 code
node script.js
```

### 1.5.2. Browser Console

```javascript
// Chrome DevTools Console
console.log('ES6 works!');
```

### 1.5.3. VS Code

**Recommended extensions:**
- ESLint
- Prettier
- JavaScript (ES6) code snippets

## 1.6. Hello World

```javascript
// ES6 Hello World
const message = 'Hello, ES6!';
console.log(message);

// Arrow function
const greet = (name) => {
    console.log(`Hello, ${name}!`);
};

greet('World');
```

## 1.7. Strict Mode

```javascript
'use strict';

// Prevents common mistakes
x = 10; // Error: x is not defined
```

## 1.8. Resources

- MDN JavaScript Documentation
- javascript.info
- ES6 Features (github.com/lukehoban/es6features)
- Babel REPL (để test code)

---

**Chương tiếp theo:** Let, Const và Block Scope
