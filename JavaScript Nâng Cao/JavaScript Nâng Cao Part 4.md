# JavaScript Nâng Cao 4 - Tài Liệu Học Tập

## Mục Lục
1. [IIFE (Immediately Invoked Function Expression)](#1-iife-immediately-invoked-function-expression)
2. [call(), apply(), bind()](#2-call-apply-bind)
3. [Interpreter / Compiler / JIT Compiler](#3-interpreter--compiler--jit-compiler)
4. [Garbage Collection](#4-garbage-collection)

---

## 1. IIFE (Immediately Invoked Function Expression)

### 1.1 IIFE là gì?

IIFE là function được định nghĩa và thực thi ngay lập tức, không cần gọi riêng.

```javascript
// Cú pháp cơ bản
(function() {
  console.log("IIFE được thực thi ngay!");
})();

// Hoặc
(function() {
  console.log("IIFE cú pháp khác");
}());

// Output ngay lập tức:
// "IIFE được thực thi ngay!"
// "IIFE cú pháp khác"

// So sánh với function thông thường
function normalFunction() {
  console.log("Function thông thường");
}
normalFunction(); // Phải gọi manual
```

### 1.2 Tại Sao Cần IIFE?

```javascript
// ============================================
// 1. TRÁNH POLLUTION GLOBAL SCOPE
// ============================================

// ❌ BAD: Variables trong global scope
var counter = 0;
var increment = function() {
  counter++;
};
var getCounter = function() {
  return counter;
};

// Tất cả variables trên pollute global scope
console.log(window.counter); // 0 (có thể conflict)

// ✅ GOOD: Dùng IIFE để encapsulate
var CounterModule = (function() {
  var counter = 0; // Private variable
  
  return {
    increment: function() {
      counter++;
    },
    getCounter: function() {
      return counter;
    }
  };
})();

CounterModule.increment();
console.log(CounterModule.getCounter()); // 1
// console.log(counter); // ReferenceError: counter is not defined

// ============================================
// 2. TẠO PRIVATE VARIABLES
// ============================================

var BankAccount = (function() {
  var balance = 0; // Private
  var accountNumber = "123456"; // Private
  
  return {
    deposit: function(amount) {
      if (amount > 0) {
        balance += amount;
        return `Đã nạp ${amount}. Số dư: ${balance}`;
      }
      return "Số tiền không hợp lệ";
    },
    
    withdraw: function(amount) {
      if (amount > 0 && amount <= balance) {
        balance -= amount;
        return `Đã rút ${amount}. Số dư: ${balance}`;
      }
      return "Không thể rút tiền";
    },
    
    getBalance: function() {
      return balance;
    },
    
    getAccountNumber: function() {
      return accountNumber;
    }
  };
})();

console.log(BankAccount.deposit(1000)); // Đã nạp 1000. Số dư: 1000
console.log(BankAccount.withdraw(500)); // Đã rút 500. Số dư: 500
console.log(BankAccount.getBalance()); // 500
// console.log(BankAccount.balance); // undefined (private!)
```

### 1.3 IIFE với Parameters

```javascript
// Passing parameters vào IIFE
(function(name, age) {
  console.log(`Tôi là ${name}, ${age} tuổi`);
})("An", 25);

// Practical example: jQuery-like pattern
var $ = (function(window, document) {
  var version = "1.0.0";
  
  function select(selector) {
    return document.querySelector(selector);
  }
  
  function selectAll(selector) {
    return document.querySelectorAll(selector);
  }
  
  return {
    version: version,
    select: select,
    selectAll: selectAll
  };
})(window, document);

console.log($.version); // "1.0.0"
// var element = $.select("#myId");

// IIFE với global objects
(function(global) {
  global.MyLibrary = {
    version: "1.0.0",
    init: function() {
      console.log("Library initialized");
    }
  };
})(typeof window !== 'undefined' ? window : global);
```

### 1.4 IIFE Patterns

```javascript
// ============================================
// 1. MODULE PATTERN
// ============================================
var ShoppingCart = (function() {
  // Private
  var items = [];
  var total = 0;
  
  function calculateTotal() {
    total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  }
  
  // Public API
  return {
    addItem: function(name, price, quantity = 1) {
      items.push({ name, price, quantity });
      calculateTotal();
    },
    
    removeItem: function(name) {
      items = items.filter(item => item.name !== name);
      calculateTotal();
    },
    
    getTotal: function() {
      return total;
    },
    
    getItems: function() {
      return [...items]; // Return copy
    },
    
    clear: function() {
      items = [];
      total = 0;
    }
  };
})();

ShoppingCart.addItem("Laptop", 1000);
ShoppingCart.addItem("Mouse", 50, 2);
console.log(ShoppingCart.getTotal()); // 1100
console.log(ShoppingCart.getItems());

// ============================================
// 2. REVEALING MODULE PATTERN
// ============================================
var Calculator = (function() {
  var result = 0;
  
  function log(message) {
    console.log(`[Calculator] ${message}`);
  }
  
  function add(x) {
    result += x;
    log(`Added ${x}, result: ${result}`);
    return this;
  }
  
  function subtract(x) {
    result -= x;
    log(`Subtracted ${x}, result: ${result}`);
    return this;
  }
  
  function multiply(x) {
    result *= x;
    log(`Multiplied by ${x}, result: ${result}`);
    return this;
  }
  
  function getResult() {
    return result;
  }
  
  function reset() {
    result = 0;
    log("Reset");
    return this;
  }
  
  // Reveal public methods
  return {
    add: add,
    subtract: subtract,
    multiply: multiply,
    getResult: getResult,
    reset: reset
  };
})();

Calculator.add(5).multiply(2).subtract(3);
console.log(Calculator.getResult()); // 7

// ============================================
// 3. SINGLETON PATTERN
// ============================================
var Database = (function() {
  var instance;
  
  function createInstance() {
    var connection = "DB_CONNECTION_STRING";
    var data = [];
    
    return {
      connect: function() {
        console.log("Connected to database");
      },
      
      insert: function(record) {
        data.push(record);
        console.log("Inserted:", record);
      },
      
      getAll: function() {
        return [...data];
      }
    };
  }
  
  return {
    getInstance: function() {
      if (!instance) {
        instance = createInstance();
      }
      return instance;
    }
  };
})();

var db1 = Database.getInstance();
var db2 = Database.getInstance();

console.log(db1 === db2); // true (cùng instance)

db1.insert({ id: 1, name: "User 1" });
console.log(db2.getAll()); // [{ id: 1, name: "User 1" }]
```

### 1.5 IIFE trong Loops (Classic Problem)

```javascript
// ============================================
// PROBLEM: Closure trong loop với var
// ============================================

// ❌ BAD: Tất cả log ra 5
console.log("Với var:");
for (var i = 0; i < 5; i++) {
  setTimeout(function() {
    console.log(i); // 5, 5, 5, 5, 5
  }, 100);
}

// Tại sao? Vì var là function-scoped
// Khi setTimeout chạy, loop đã kết thúc, i = 5

// ✅ SOLUTION 1: IIFE
console.log("\nVới IIFE:");
for (var i = 0; i < 5; i++) {
  (function(index) {
    setTimeout(function() {
      console.log(index); // 0, 1, 2, 3, 4
    }, 100);
  })(i); // Pass i vào IIFE
}

// ✅ SOLUTION 2: let (ES6+)
console.log("\nVới let:");
for (let i = 0; i < 5; i++) {
  setTimeout(function() {
    console.log(i); // 0, 1, 2, 3, 4
  }, 100);
}

// IIFE tạo closure riêng cho mỗi iteration
console.log("\nVí dụ thực tế:");
var buttons = document.querySelectorAll('.button');

// ❌ BAD
for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    console.log('Button ' + i + ' clicked'); // Luôn log index cuối
  });
}

// ✅ GOOD với IIFE
for (var i = 0; i < buttons.length; i++) {
  (function(index) {
    buttons[index].addEventListener('click', function() {
      console.log('Button ' + index + ' clicked'); // Đúng index
    });
  })(i);
}

// ✅ GOOD với let
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    console.log('Button ' + i + ' clicked'); // Đúng index
  });
}
```

### 1.6 Arrow Functions và IIFE

```javascript
// IIFE với arrow function
(() => {
  console.log("Arrow IIFE");
})();

// Với parameters
((name, age) => {
  console.log(`${name}, ${age} tuổi`);
})("An", 25);

// Return value
const result = (() => {
  const x = 10;
  const y = 20;
  return x + y;
})();

console.log(result); // 30

// Async IIFE
(async () => {
  try {
    const data = await fetch('https://api.example.com/data');
    const json = await data.json();
    console.log(json);
  } catch (error) {
    console.error('Error:', error);
  }
})();

// Top-level await alternative
(async function() {
  const users = await fetchUsers();
  const posts = await fetchPosts();
  console.log(users, posts);
})();
```

### 1.7 IIFE Best Practices

```javascript
// ✅ GOOD: Semicolon trước IIFE
var x = 10
;(function() {
  console.log("Safe IIFE");
})();

// ❌ BAD: Không có semicolon
var x = 10
(function() {
  console.log("Có thể lỗi!");
})();
// Lỗi: 10 is not a function

// ✅ GOOD: Use strict mode
(function() {
  'use strict';
  
  // Strict mode chỉ apply trong IIFE này
  undeclaredVar = 10; // ReferenceError
})();

// ✅ GOOD: Named IIFE (dễ debug)
(function myIIFE() {
  console.log("Named IIFE");
  
  // Function name hiện trong stack trace
  throw new Error("Error in myIIFE");
})();

// ✅ GOOD: Return values
var config = (function() {
  var env = process.env.NODE_ENV || 'development';
  
  var configs = {
    development: {
      apiUrl: 'http://localhost:3000',
      debug: true
    },
    production: {
      apiUrl: 'https://api.production.com',
      debug: false
    }
  };
  
  return configs[env];
})();

console.log(config);

// ✅ GOOD: Module pattern với dependencies
var MyModule = (function($, _) {
  // Private
  var data = [];
  
  // Public
  return {
    init: function() {
      console.log("Initialized with jQuery and Lodash");
    },
    
    process: function(items) {
      data = _.map(items, function(item) {
        return $(item).text();
      });
      return data;
    }
  };
})(jQuery, _); // Inject dependencies
```

### 1.8 Modern Alternatives to IIFE

```javascript
// ============================================
// ES6 MODULES (Preferred in modern code)
// ============================================

// module.js
export const version = "1.0.0";

export function add(a, b) {
  return a + b;
}

// app.js
import { version, add } from './module.js';

// ============================================
// BLOCK SCOPE với let/const
// ============================================

// IIFE style (old)
(function() {
  var temp = "temporary";
  console.log(temp);
})();

// Modern style
{
  let temp = "temporary";
  console.log(temp);
}
// console.log(temp); // ReferenceError

// ============================================
// CLASS với PRIVATE FIELDS (ES2022)
// ============================================

class Counter {
  #count = 0; // Private field
  
  increment() {
    this.#count++;
  }
  
  getCount() {
    return this.#count;
  }
}

const counter = new Counter();
counter.increment();
console.log(counter.getCount()); // 1
// console.log(counter.#count); // SyntaxError
```

---

## 2. call(), apply(), bind()

### 2.1 Hiểu về `this` Context

```javascript
// this trong các context khác nhau

// 1. Global context
console.log(this); // window (browser) hoặc global (Node.js)

// 2. Object method
const person = {
  name: "An",
  greet: function() {
    console.log(`Xin chào, tôi là ${this.name}`);
  }
};

person.greet(); // "Xin chào, tôi là An" (this = person)

// 3. Function call
function showThis() {
  console.log(this);
}

showThis(); // window/global (non-strict) hoặc undefined (strict)

// 4. Constructor
function Person(name) {
  this.name = name;
}

const p = new Person("An");
console.log(p.name); // "An" (this = new object)

// 5. Arrow function (không có this riêng)
const obj = {
  name: "An",
  greet: () => {
    console.log(this); // this từ outer scope
  }
};

obj.greet(); // window/global (không phải obj!)
```

### 2.2 call() Method

`call()` gọi function với `this` value được chỉ định và các arguments riêng lẻ.

```javascript
// Cú pháp: func.call(thisArg, arg1, arg2, ...)

function greet(greeting, punctuation) {
  console.log(`${greeting}, tôi là ${this.name}${punctuation}`);
}

const user1 = { name: "An" };
const user2 = { name: "Bình" };

greet.call(user1, "Xin chào", "!"); // "Xin chào, tôi là An!"
greet.call(user2, "Hi", "."); // "Hi, tôi là Bình."

// Practical example: Borrowing methods
const person = {
  firstName: "Nguyễn",
  lastName: "An",
  getFullName: function() {
    return `${this.firstName} ${this.lastName}`;
  }
};

const anotherPerson = {
  firstName: "Trần",
  lastName: "Bình"
};

// Borrow method từ person
console.log(person.getFullName.call(anotherPerson)); // "Trần Bình"

// Array-like objects
function logArguments() {
  // arguments không phải array, nhưng có thể dùng array methods
  const args = Array.prototype.slice.call(arguments);
  console.log(args);
}

logArguments(1, 2, 3, 4); // [1, 2, 3, 4]

// Modern equivalent
function logArgumentsModern() {
  const args = Array.from(arguments);
  // hoặc: const args = [...arguments];
  console.log(args);
}

// Math.max với array
const numbers = [5, 6, 2, 3, 7];
const max = Math.max.call(null, ...numbers);
console.log(max); // 7

// Hoặc dùng apply (xem section sau)
const max2 = Math.max.apply(null, numbers);
console.log(max2); // 7
```

### 2.3 apply() Method

`apply()` giống `call()` nhưng nhận arguments dưới dạng array.

```javascript
// Cú pháp: func.apply(thisArg, [arg1, arg2, ...])

function greet(greeting, punctuation) {
  console.log(`${greeting}, tôi là ${this.name}${punctuation}`);
}

const user = { name: "An" };

greet.apply(user, ["Xin chào", "!"]); // "Xin chào, tôi là An!"

// Sự khác biệt call vs apply
function sum(a, b, c) {
  return a + b + c;
}

// call - arguments riêng lẻ
console.log(sum.call(null, 1, 2, 3)); // 6

// apply - arguments trong array
console.log(sum.apply(null, [1, 2, 3])); // 6

// Practical: Math.max/min với array
const numbers = [5, 6, 2, 3, 7, 8, 1];

const max = Math.max.apply(null, numbers);
const min = Math.min.apply(null, numbers);

console.log(`Max: ${max}, Min: ${min}`); // Max: 8, Min: 1

// Modern way với spread operator
console.log(Math.max(...numbers)); // 8
console.log(Math.min(...numbers)); // 1

// Array concatenation
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

Array.prototype.push.apply(arr1, arr2);
console.log(arr1); // [1, 2, 3, 4, 5, 6]

// Modern way
arr1.push(...arr2);

// Function composition
function multiply(a, b) {
  return a * b;
}

function multiplyAndAdd(a, b, c) {
  const product = multiply.apply(this, [a, b]);
  return product + c;
}

console.log(multiplyAndAdd(2, 3, 4)); // 10 (2*3 + 4)
```

### 2.4 bind() Method

`bind()` tạo function mới với `this` value cố định.

```javascript
// Cú pháp: func.bind(thisArg, arg1, arg2, ...)

function greet() {
  console.log(`Xin chào, tôi là ${this.name}`);
}

const user1 = { name: "An" };
const user2 = { name: "Bình" };

const greetUser1 = greet.bind(user1);
const greetUser2 = greet.bind(user2);

greetUser1(); // "Xin chào, tôi là An"
greetUser2(); // "Xin chào, tôi là Bình"

// Gọi nhiều lần
greetUser1(); // Vẫn "Xin chào, tôi là An"
greetUser1(); // Vẫn "Xin chào, tôi là An"

// Partial application
function multiply(a, b) {
  return a * b;
}

const double = multiply.bind(null, 2);
const triple = multiply.bind(null, 3);

console.log(double(5)); // 10
console.log(triple(5)); // 15

// Event handlers
const button = {
  content: "OK",
  click: function() {
    console.log(`Button "${this.content}" clicked`);
  }
};

// ❌ Problem: this bị mất
// document.getElementById('btn').addEventListener('click', button.click);
// → "Button undefined clicked"

// ✅ Solution: bind
// document.getElementById('btn').addEventListener('click', button.click.bind(button));
// → "Button OK clicked"

// Object methods
const person = {
  firstName: "Nguyễn",
  lastName: "An",
  getFullName: function() {
    return `${this.firstName} ${this.lastName}`;
  }
};

const getName = person.getFullName;
// console.log(getName()); // undefined undefined (this bị mất)

const getBoundName = person.getFullName.bind(person);
console.log(getBoundName()); // "Nguyễn An"

// setTimeout
const obj = {
  message: "Hello",
  showMessage: function() {
    console.log(this.message);
  }
};

// ❌ Problem
setTimeout(obj.showMessage, 1000); // undefined

// ✅ Solution 1: bind
setTimeout(obj.showMessage.bind(obj), 1000); // "Hello"

// ✅ Solution 2: arrow function
setTimeout(() => obj.showMessage(), 1000); // "Hello"

// ✅ Solution 3: wrapper function
setTimeout(function() {
  obj.showMessage();
}, 1000); // "Hello"
```

### 2.5 So Sánh call, apply, bind

```javascript
const person = {
  name: "An",
  age: 25
};

function introduce(greeting, punctuation) {
  console.log(`${greeting}, tôi là ${this.name}, ${this.age} tuổi${punctuation}`);
}

// call - gọi ngay, args riêng lẻ
introduce.call(person, "Xin chào", "!");
// "Xin chào, tôi là An, 25 tuổi!"

// apply - gọi ngay, args trong array
introduce.apply(person, ["Xin chào", "!"]);
// "Xin chào, tôi là An, 25 tuổi!"

// bind - return function mới, không gọi ngay
const boundIntroduce = introduce.bind(person, "Xin chào", "!");
boundIntroduce(); // Gọi sau
// "Xin chào, tôi là An, 25 tuổi!"

/*
┌──────────┬────────────┬──────────────┬─────────────────┐
│ Method   │ Gọi ngay?  │ Arguments    │ Return          │
├──────────┼────────────┼──────────────┼─────────────────┤
│ call()   │ Có         │ Riêng lẻ     │ Kết quả         │
│ apply()  │ Có         │ Array        │ Kết quả         │
│ bind()   │ Không      │ Riêng lẻ     │ Function mới    │
└──────────┴────────────┴──────────────┴─────────────────┘
*/

// Performance comparison
const iterations = 1000000;

// call
console.time('call');
for (let i = 0; i < iterations; i++) {
  introduce.call(person, "Hi", ".");
}
console.timeEnd('call');

// apply
console.time('apply');
for (let i = 0; i < iterations; i++) {
  introduce.apply(person, ["Hi", "."]);
}
console.timeEnd('apply');

// bind
const bound = introduce.bind(person, "Hi", ".");
console.time('bind');
for (let i = 0; i < iterations; i++) {
  bound();
}
console.timeEnd('bind');

// Thường: call ≈ apply, bind nhanh hơn nếu gọi nhiều lần
```

### 2.6 Practical Examples

```javascript
// ============================================
// 1. METHOD BORROWING
// ============================================

// Array methods trên array-like objects
const arrayLike = {
  0: 'a',
  1: 'b',
  2: 'c',
  length: 3
};

// Borrow array methods
const realArray = Array.prototype.slice.call(arrayLike);
console.log(realArray); // ['a', 'b', 'c']

Array.prototype.forEach.call(arrayLike, function(item) {
  console.log(item);
});

// Modern way
const realArray2 = Array.from(arrayLike);
const realArray3 = [...arrayLike]; // Chỉ với iterables

// ============================================
// 2. FUNCTION CURRYING
// ============================================

function multiply(a, b) {
  return a * b;
}

const multiplyByTwo = multiply.bind(null, 2);
const multiplyByTen = multiply.bind(null, 10);

console.log(multiplyByTwo(5)); // 10
console.log(multiplyByTen(5)); // 50

// Complex example
function greetPerson(greeting, name, age) {
  console.log(`${greeting}, ${name}! You are ${age} years old.`);
}

const greetHello = greetPerson.bind(null, "Hello");
const greetHelloJohn = greetPerson.bind(null, "Hello", "John");

greetHello("Alice", 25); // "Hello, Alice! You are 25 years old."
greetHelloJohn(30); // "Hello, John! You are 30 years old."

// ============================================
// 3. CLASS METHODS
// ============================================

class Button {
  constructor(label) {
    this.label = label;
    this.clickCount = 0;
  }
  
  click() {
    this.clickCount++;
    console.log(`${this.label} clicked ${this.clickCount} times`);
  }
}

const saveButton = new Button("Save");

// ❌ Problem với event listeners
// document.getElementById('save').addEventListener('click', saveButton.click);
// → this sẽ là button element, không phải saveButton object

// ✅ Solution 1: bind trong constructor
class ButtonBound {
  constructor(label) {
    this.label = label;
    this.clickCount = 0;
    this.click = this.click.bind(this); // Bind trong constructor
  }
  
  click() {
    this.clickCount++;
    console.log(`${this.label} clicked ${this.clickCount} times`);
  }
}

// ✅ Solution 2: Arrow function class field
class ButtonArrow {
  constructor(label) {
    this.label = label;
    this.clickCount = 0;
  }
  
  click = () => {
    this.clickCount++;
    console.log(`${this.label} clicked ${this.clickCount} times`);
  }
}

// ============================================
// 4. CALLBACK FUNCTIONS
// ============================================

const user = {
  name: "An",
  friends: ["Bình", "Chi", "Dũng"],
  
  listFriends: function() {
    // ❌ Problem với regular function
    this.friends.forEach(function(friend) {
      // console.log(this.name + " knows " + friend);
      // → undefined knows Bình (this không đúng)
    });
    
    // ✅ Solution 1: bind
    this.friends.forEach(function(friend) {
      console.log(this.name + " knows " + friend);
    }.bind(this));
    
    // ✅ Solution 2: arrow function (preferred)
    this.friends.forEach(friend => {
      console.log(this.name + " knows " + friend);
    });
    
    // ✅ Solution 3: thisArg parameter
    this.friends.forEach(function(friend) {
      console.log(this.name + " knows " + friend);
    }, this); // forEach accepts thisArg as 2nd param
  }
};

user.listFriends();

// ============================================
// 5. FUNCTION COMPOSITION
// ============================================

function log(level, message) {
  console.log(`[${level}] ${message}`);
}

const logInfo = log.bind(null, "INFO");
const logWarning = log.bind(null, "WARNING");
const logError = log.bind(null, "ERROR");

logInfo("Application started"); // [INFO] Application started
logWarning("Low memory"); // [WARNING] Low memory
logError("Failed to connect"); // [ERROR] Failed to connect

// ============================================
// 6. THROTTLE/DEBOUNCE
// ============================================

function throttle(func, limit) {
  let inThrottle;
  return function() {
    const args = arguments;
    const context = this;
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

const obj = {
  name: "Scroll Handler",
  handleScroll: function() {
    console.log(`${this.name} triggered`);
  }
};

const throttledScroll = throttle(obj.handleScroll.bind(obj), 1000);
// window.addEventListener('scroll', throttledScroll);
```

### 2.7 Best Practices

```javascript
// ✅ GOOD: Dùng arrow functions cho callbacks
class Component {
  constructor() {
    this.state = { count: 0 };
  }
  
  // Arrow function - auto-bind
  handleClick = () => {
    this.state.count++;
  }
}

// ❌ BAD: Bind mỗi lần render
class BadComponent {
  render() {
    return (
      // Tạo function mới mỗi lần!
      <button onClick={this.handleClick.bind(this)}>Click</button>
    );
  }
}

// ✅ GOOD: Bind trong constructor
class GoodComponent {
  constructor() {
    this.handleClick = this.handleClick.bind(this);
  }
  
  render() {
    return <button onClick={this.handleClick}>Click</button>;
  }
}

// ✅ GOOD: Explicit context
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce(function(acc, num) {
  return acc + num;
}, 0);

// ✅ GOOD: Use call for one-time execution
function setup() {
  console.log("Setup for", this.name);
}
setup.call({ name: "MyApp" });

// ✅ GOOD: Use apply for arrays
Math.max.apply(null, [1, 2, 3, 4, 5]);

// ✅ GOOD: Use bind for delayed/reused execution
const boundSetup = setup.bind({ name: "MyApp" });
setTimeout(boundSetup, 1000);
```

---

## 3. Interpreter / Compiler / JIT Compiler

### 3.1 Interpreted vs Compiled Languages

```javascript
/*
┌─────────────────────────────────────────────────────┐
│              INTERPRETED LANGUAGE                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Source Code → Interpreter → Execute (Line by Line)│
│                                                     │
│  Ưu điểm:                                          │
│  - Flexible                                        │
│  - Platform independent                            │
│  - Faster development                              │
│                                                     │
│  Nhược điểm:                                       │
│  - Slower execution                                │
│  - No optimization                                 │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│               COMPILED LANGUAGE                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Source Code → Compiler → Machine Code → Execute   │
│                                                     │
│  Ưu điểm:                                          │
│  - Faster execution                                │
│  - Optimizations                                   │
│  - Type checking                                   │
│                                                     │
│  Nhược điểm:                                       │
│  - Build step required                             │
│  - Platform specific                               │
│  - Slower development                              │
└─────────────────────────────────────────────────────┘
*/

// JavaScript là INTERPRETED nhưng modern engines dùng JIT compilation
```

### 3.2 JavaScript Engine Pipeline

```javascript
/*
┌───────────────────────────────────────────────────────┐
│           JAVASCRIPT ENGINE (V8) PIPELINE             │
├───────────────────────────────────────────────────────┤
│                                                       │
│  1. Source Code                                       │
│     ↓                                                 │
│  2. Parser → AST (Abstract Syntax Tree)               │
│     ↓                                                 │
│  3. Interpreter (Ignition) → Bytecode                 │
│     ↓                                                 │
│  4. Execute Bytecode (Profiler theo dõi)              │
│     ↓                                                 │
│  5. Hot Functions → JIT Compiler (TurboFan)           │
│     ↓                                                 │
│  6. Optimized Machine Code                            │
│     ↓                                                 │
│  7. Execute (Fast!)                                   │
│                                                       │
└───────────────────────────────────────────────────────┘
*/

// Ví dụ: Function được optimize
function add(a, b) {
  return a + b;
}

// Lần đầu: Interpreted
add(1, 2);

// Gọi nhiều lần → Engine profile
for (let i = 0; i < 10000; i++) {
  add(i, i + 1);
}

// Engine nhận ra: "hot function" với pattern cố định (number + number)
// → Compile thành optimized machine code

// Nếu đột ngột thay đổi type:
add("hello", "world"); // Deoptimization! Phải recompile
```

### 3.3 Parser và AST

```javascript
// Source code
function greet(name) {
  return "Hello, " + name;
}

/*
Parser chuyển thành AST (Abstract Syntax Tree):

{
  type: "Program",
  body: [
    {
      type: "FunctionDeclaration",
      id: { type: "Identifier", name: "greet" },
      params: [
        { type: "Identifier", name: "name" }
      ],
      body: {
        type: "BlockStatement",
        body: [
          {
            type: "ReturnStatement",
            argument: {
              type: "BinaryExpression",
              operator: "+",
              left: {
                type: "Literal",
                value: "Hello, "
              },
              right: {
                type: "Identifier",
                name: "name"
              }
            }
          }
        ]
      }
    }
  ]
}
*/

// Tools để xem AST:
// - https://astexplorer.net/
// - esprima, acorn, babel-parser

// AST được dùng để:
// 1. Syntax checking
// 2. Code transformation (Babel, TypeScript)
// 3. Code analysis (ESLint)
// 4. Code generation
```

### 3.4 Interpreter (Ignition trong V8)

```javascript
/*
INTERPRETER converts AST to BYTECODE

┌─────────────────────────────────────────┐
│              BYTECODE                   │
├─────────────────────────────────────────┤
│                                         │
│  Lda [arg0]        ; Load argument 0    │
│  Star r0           ; Store to register  │
│  LdaConstant "Hello, "                  │
│  Add r0            ; Add r0             │
│  Return            ; Return result      │
│                                         │
└─────────────────────────────────────────┘

Bytecode:
- Trung gian giữa source code và machine code
- Platform independent
- Dễ interpret hơn machine code
- Compact hơn AST
*/

// Function này sẽ được convert thành bytecode
function multiply(a, b) {
  return a * b;
}

// Bytecode được execute bởi interpreter
// Nếu function "hot" → optimize bởi compiler
```

### 3.5 JIT (Just-In-Time) Compiler

```javascript
/*
┌──────────────────────────────────────────────────────┐
│                   JIT COMPILER                       │
├──────────────────────────────────────────────────────┤
│                                                      │
│  1. PROFILER theo dõi code execution                 │
│     - Đếm số lần function được gọi                   │
│     - Phân tích types của arguments                  │
│     - Tìm hot paths                                  │
│                                                      │
│  2. Khi function "hot":                              │
│     - Gọi nhiều lần (threshold)                      │
│     - Type stable                                    │
│     → Compile thành OPTIMIZED MACHINE CODE           │
│                                                      │
│  3. OPTIMIZATIONS:                                   │
│     - Inline functions                               │
│     - Dead code elimination                          │
│     - Type specialization                            │
│     - Loop optimizations                             │
│                                                      │
│  4. DEOPTIMIZATION:                                  │
│     - Nếu assumptions sai (type thay đổi)            │
│     → Rollback về bytecode                           │
│                                                      │
└──────────────────────────────────────────────────────┘
*/

// ✅ JIT-friendly code: Type stable
function add(a, b) {
  return a + b;
}

// Luôn gọi với numbers
for (let i = 0; i < 100000; i++) {
  add(i, i + 1); // Engine optimize cho number + number
}

// ❌ JIT-unfriendly: Type unstable
function addBad(a, b) {
  return a + b;
}

addBad(1, 2);           // number + number
addBad("hello", "world"); // string + string → Deoptimization!
addBad(1, 2);           // Phải recompile

// ✅ Write JIT-friendly code
function calculate(x) {
  // Type consistent
  return x * 2 + 10;
}

// Gọi với cùng type
for (let i = 0; i < 100000; i++) {
  calculate(i);
}
```

### 3.6 Optimization Examples

```javascript
// ============================================
// 1. FUNCTION INLINING
// ============================================

// Original code
function add(a, b) {
  return a + b;
}

function calculate(x, y) {
  return add(x, y) * 2;
}

// After optimization (inlining)
function calculateOptimized(x, y) {
  return (x + y) * 2; // add() được inline
}

// ============================================
// 2. DEAD CODE ELIMINATION
// ============================================

// Original
function process(x) {
  const temp = x * 2;
  const unused = temp + 10; // Không được dùng
  return temp;
}

// After optimization
function processOptimized(x) {
  return x * 2; // unused bị remove
}

// ============================================
// 3. TYPE SPECIALIZATION
// ============================================

// Generic code
function multiply(a, b) {
  return a * b;
}

// JIT tạo specialized version
// multiply_int(a: int, b: int) → optimized machine code
// multiply_double(a: double, b: double) → optimized machine code

// ============================================
// 4. LOOP OPTIMIZATIONS
// ============================================

// Original
const arr = [1, 2, 3, 4, 5];
let sum = 0;
for (let i = 0; i < arr.length; i++) {
  sum += arr[i];
}

// Optimization: Loop unrolling
// Compiler có thể unroll loop:
let sumOptimized = 0;
sumOptimized += arr[0];
sumOptimized += arr[1];
sumOptimized += arr[2];
sumOptimized += arr[3];
sumOptimized += arr[4];

// ============================================
// 5. HIDDEN CLASSES
// ============================================

// ❌ BAD: Properties added in different order
function Point(x, y) {
  this.x = x;
  this.y = y;
}

const p1 = new Point(1, 2);
const p2 = new Point(3, 4);

p1.z = 5; // Thêm property → p1 và p2 có hidden classes khác nhau!

// ✅ GOOD: Same hidden class
function PointOptimized(x, y) {
  this.x = x;
  this.y = y;
  this.z = 0; // Khai báo sẵn
}

const p3 = new PointOptimized(1, 2);
const p4 = new PointOptimized(3, 4);
// p3 và p4 có cùng hidden class → optimized!
```

### 3.7 Writing Optimization-Friendly Code

```javascript
// ============================================
// 1. MONOMORPHIC FUNCTIONS (1 type)
// ============================================

// ✅ GOOD: Always same types
function addNumbers(a, b) {
  return a + b;
}

addNumbers(1, 2);
addNumbers(3, 4);
addNumbers(5, 6);
// Engine: "Ah, luôn là number + number, optimize!"

// ❌ BAD: Polymorphic (nhiều types)
function addAnything(a, b) {
  return a + b;
}

addAnything(1, 2);           // number + number
addAnything("hello", "world"); // string + string
addAnything([1], [2]);       // array + array
// Engine: "Không thể optimize, types thay đổi liên tục"

// ============================================
// 2. CONSISTENT OBJECT SHAPES
// ============================================

// ✅ GOOD: Same properties, same order
class User {
  constructor(name, age, email) {
    this.name = name;
    this.age = age;
    this.email = email;
  }
}

const users = [
  new User("An", 25, "an@example.com"),
  new User("Bình", 30, "binh@example.com")
];

// ❌ BAD: Different shapes
const user1 = { name: "An", age: 25 };
const user2 = { age: 30, name: "Bình" }; // Different order!
const user3 = { name: "Chi", age: 28, email: "chi@example.com" }; // Extra property!

// ============================================
// 3. AVOID DELETE
// ============================================

// ❌ BAD: delete changes hidden class
const obj = { x: 1, y: 2, z: 3 };
delete obj.z; // Changes hidden class!

// ✅ GOOD: Set to undefined/null
const obj2 = { x: 1, y: 2, z: 3 };
obj2.z = undefined; // Keeps hidden class

// ============================================
// 4. INITIALIZE IN CONSTRUCTOR
// ============================================

// ❌ BAD
function Point(x, y) {
  this.x = x;
  this.y = y;
}

const p = new Point(1, 2);
p.z = 3; // Added later → deoptimization

// ✅ GOOD
function PointOptimized(x, y, z = 0) {
  this.x = x;
  this.y = y;
  this.z = z; // Initialized in constructor
}

// ============================================
// 5. USE ARRAYS FOR HOMOGENEOUS DATA
// ============================================

// ✅ GOOD: Same types
const numbers = [1, 2, 3, 4, 5];

// ❌ BAD: Mixed types
const mixed = [1, "two", 3, "four", 5];

// ============================================
// 6. AVOID SPARSE ARRAYS
// ============================================

// ❌ BAD: Sparse array
const sparse = [];
sparse[0] = 1;
sparse[1000] = 2; // Sparse!

// ✅ GOOD: Dense array
const dense = [1, 2, 3, 4, 5];

// ============================================
// 7. SMALL FUNCTIONS
// ============================================

// ✅ GOOD: Small, focused functions (easier to inline)
function add(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}

// ❌ BAD: Large functions (harder to optimize)
function calculate(a, b, operation) {
  let result;
  if (operation === 'add') {
    result = a + b;
  } else if (operation === 'subtract') {
    result = a - b;
  } else if (operation === 'multiply') {
    result = a * b;
  }
  // ... 100 more lines
  return result;
}
```

### 3.8 Profiling và Debugging

```javascript
// Chrome DevTools Performance Tab
// 1. Record
// 2. Perform actions
// 3. Stop
// 4. Analyze:
//    - Call tree
//    - Bottom-up
//    - Event log

// V8 flags để debug optimization
// node --trace-opt script.js     → Show optimized functions
// node --trace-deopt script.js   → Show deoptimized functions
// node --trace-ic script.js      → Show inline caches

// Benchmark code
function benchmark(fn, iterations = 1000000) {
  const start = performance.now();
  for (let i = 0; i < iterations; i++) {
    fn(i);
  }
  const end = performance.now();
  console.log(`Time: ${(end - start).toFixed(2)}ms`);
}

// Test optimization
function add(a, b) {
  return a + b;
}

benchmark(() => add(1, 2));

// Check if function is optimized
// %OptimizeFunctionOnNextCall(add); // V8 native syntax
// add(1, 2);
// %GetOptimizationStatus(add); // Check status
```

---

## 4. Garbage Collection

### 4.1 Garbage Collection là gì?

```javascript
/*
GARBAGE COLLECTION (GC) tự động giải phóng memory không còn dùng.

┌──────────────────────────────────────────────────────┐
│                  MEMORY LIFECYCLE                    │
├──────────────────────────────────────────────────────┤
│                                                      │
│  1. ALLOCATE                                         │
│     → Tạo variable, object, function                 │
│                                                      │
│  2. USE                                              │
│     → Read/write memory                              │
│                                                      │
│  3. RELEASE (Automatic by GC)                        │
│     → Khi memory không còn được reference            │
│                                                      │
└──────────────────────────────────────────────────────┘
*/

// Example
function createUser() {
  const user = {
    name: "An",
    age: 25,
    data: new Array(1000000) // Large data
  };
  
  return user.name; // Return primitive
  
  // Object 'user' không còn được reference
  // → GC sẽ thu hồi memory
}

const name = createUser();
// Memory của object user đã được giải phóng
```

### 4.2 Reachability (Khả năng truy cập)

```javascript
/*
REACHABILITY: Object có thể được "reach" từ root?

ROOTS (điểm xuất phát):
- Global variables
- Currently executing function (local variables)
- Call stack
*/

// Example 1: Reachable
let user = {
  name: "An"
};

// user reachable từ global scope
console.log(user.name); // OK

// Example 2: Unreachable
let user2 = {
  name: "Bình"
};

user2 = null; // Không còn reference
// Object { name: "Bình" } unreachable → GC

// Example 3: Multiple references
let admin = {
  name: "Admin"
};

let superAdmin = admin; // 2 references

admin = null; // 1 reference còn lại
// Object vẫn reachable qua superAdmin

superAdmin = null; // 0 references
// Bây giờ mới unreachable → GC

// Example 4: Circular references (GC xử lý được)
function createCircular() {
  let a = {};
  let b = {};
  
  a.ref = b;
  b.ref = a; // Circular!
  
  return "done";
}

createCircular();
// a và b không reachable từ bên ngoài → GC (modern engines)
```

### 4.3 Mark-and-Sweep Algorithm

```javascript
/*
┌──────────────────────────────────────────────────────┐
│             MARK-AND-SWEEP ALGORITHM                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│  PHASE 1: MARK                                       │
│  1. Bắt đầu từ roots                                 │
│  2. Visit tất cả objects accessible từ roots         │
│  3. Mark những objects đã visit                      │
│                                                      │
│  PHASE 2: SWEEP                                      │
│  1. Scan toàn bộ heap                                │
│  2. Unmarked objects → thu hồi memory                │
│  3. Marked objects → unmark (chuẩn bị cho lần sau)   │
│                                                      │
└──────────────────────────────────────────────────────┘
*/

// Visualization
/*
BEFORE GC:

Roots → [obj1] → [obj2]
         ↓
       [obj3]
       
[obj4] [obj5] (unreachable)


MARK PHASE:
✓ [obj1] → ✓ [obj2]
   ↓
✓ [obj3]

[obj4] [obj5] (unmarked)


SWEEP PHASE:
✓ [obj1] → ✓ [obj2]
   ↓
✓ [obj3]

❌ [obj4] ❌ [obj5] → Freed
*/

// Code example
let root = {
  child: {
    grandchild: {}
  }
};

let orphan = {}; // Không được reference từ root

// GC runs:
// 1. Mark: root, child, grandchild (reachable)
// 2. Sweep: orphan (unreachable) → freed
```

### 4.4 Generational Garbage Collection

```javascript
/*
V8 chia heap thành 2 generations:

┌──────────────────────────────────────────────────────┐
│                  YOUNG GENERATION                    │
│                   (New Space, ~8MB)                  │
├──────────────────────────────────────────────────────┤
│                                                      │
│  - Objects mới tạo                                   │
│  - GC thường xuyên (Minor GC / Scavenge)             │
│  - Nhanh (~1-10ms)                                   │
│  - Hầu hết objects chết sớm (90%+)                   │
│                                                      │
│  Divided into:                                       │
│  - Nursery (From-space)                              │
│  - Intermediate (To-space)                           │
│                                                      │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│                   OLD GENERATION                     │
│                   (Old Space, ~1.4GB)                │
├──────────────────────────────────────────────────────┤
│                                                      │
│  - Objects sống lâu                                  │
│  - GC ít thường xuyên (Major GC / Mark-Sweep)        │
│  - Chậm hơn (~100-1000ms)                            │
│  - Objects survived nhiều GC cycles                  │
│                                                      │
└──────────────────────────────────────────────────────┘
*/

// Short-lived objects → Young generation
function createTemp() {
  const temp = { data: new Array(1000) };
  return temp.data.length;
}

for (let i = 0; i < 1000; i++) {
  createTemp(); // temp objects chết ngay → Young GC
}

// Long-lived objects → Old generation
const cache = new Map();

function storeInCache(key, value) {
  cache.set(key, value); // Sống lâu → promoted to Old generation
}

// Minor GC (Young generation) - fast
// Major GC (Old generation) - slow but infrequent
```

### 4.5 Memory Leaks

```javascript
// ============================================
// 1. GLOBAL VARIABLES
// ============================================

// ❌ Memory leak
function createLeak() {
  leakyVar = new Array(1000000); // Quên var/let/const → global
}

createLeak();
// leakyVar tồn tại mãi trong global scope

// ✅ Fixed
function createNoLeak() {
  const localVar = new Array(1000000);
}

createNoLeak();
// localVar được GC sau khi function kết thúc

// ============================================
// 2. TIMERS NOT CLEARED
// ============================================

// ❌ Memory leak
function startLeak() {
  const bigData = new Array(1000000);
  
  setInterval(() => {
    console.log(bigData.length);
  }, 1000);
  
  // Timer chạy mãi → bigData không bao giờ được GC
}

// ✅ Fixed
function startNoLeak() {
  const bigData = new Array(1000000);
  
  const timerId = setInterval(() => {
    console.log(bigData.length);
  }, 1000);
  
  // Clear sau 10s
  setTimeout(() => {
    clearInterval(timerId);
  }, 10000);
  
  return timerId; // Để caller có thể clear
}

// ============================================
// 3. EVENT LISTENERS NOT REMOVED
// ============================================

// ❌ Memory leak
function attachLeak() {
  const bigData = new Array(1000000);
  
  document.getElementById('btn').addEventListener('click', function() {
    console.log(bigData.length);
  });
  
  // Listener không được remove → bigData bị giữ lại
}

// ✅ Fixed
function attachNoLeak() {
  const bigData = new Array(1000000);
  const button = document.getElementById('btn');
  
  const handler = function() {
    console.log(bigData.length);
  };
  
  button.addEventListener('click', handler);
  
  // Cleanup function
  return function cleanup() {
    button.removeEventListener('click', handler);
  };
}

const cleanup = attachNoLeak();
// Later: cleanup();

// ============================================
// 4. CLOSURES
// ============================================

// ❌ Memory leak
function createClosure() {
  const largeData = new Array(1000000);
  const smallData = "small";
  
  return function() {
    console.log(smallData);
    // largeData không được dùng nhưng vẫn bị closure giữ lại!
  };
}

// ✅ Fixed: Separate closures
function createClosureFixed() {
  const largeData = new Array(1000000);
  const result = largeData.length;
  const smallData = "small";
  
  return function() {
    console.log(smallData, result);
    // Chỉ smallData và result được giữ lại
  };
}

// ============================================
// 5. DETACHED DOM NODES
// ============================================

// ❌ Memory leak
const detachedNodes = [];

function createDetached() {
  const div = document.createElement('div');
  div.innerHTML = new Array(1000).join('x');
  document.body.appendChild(div);
  
  detachedNodes.push(div); // Save reference
}

function removeDivs() {
  document.body.innerHTML = ''; // Remove from DOM
  // Nhưng detachedNodes vẫn giữ references → leak!
}

// ✅ Fixed
const managedNodes = [];

function createManaged() {
  const div = document.createElement('div');
  div.innerHTML = new Array(1000).join('x');
  document.body.appendChild(div);
  managedNodes.push(div);
}

function removeManaged() {
  managedNodes.forEach(node => node.remove());
  managedNodes.length = 0; // Clear references
}

// ============================================
// 6. FORGOTTEN CACHE
// ============================================

// ❌ Memory leak
const cache = new Map();

function cacheUser(id, user) {
  cache.set(id, user);
  // Cache không bao giờ được clear!
}

// ✅ Fixed: WeakMap
const weakCache = new WeakMap();

function cacheUserWeak(userObj, data) {
  weakCache.set(userObj, data);
  // Khi userObj không còn references khác, tự động GC
}

// ✅ Fixed: Cache với TTL
class CacheWithTTL {
  constructor(ttl = 60000) {
    this.cache = new Map();
    this.ttl = ttl;
  }
  
  set(key, value) {
    const expiry = Date.now() + this.ttl;
    this.cache.set(key, { value, expiry });
  }
  
  get(key) {
    const item = this.cache.get(key);
    
    if (!item) return null;
    
    if (Date.now() > item.expiry) {
      this.cache.delete(key);
      return null;
    }
    
    return item.value;
  }
  
  cleanup() {
    const now = Date.now();
    for (const [key, item] of this.cache) {
      if (now > item.expiry) {
        this.cache.delete(key);
      }
    }
  }
}

const smartCache = new CacheWithTTL(60000);
setInterval(() => smartCache.cleanup(), 60000);
```

### 4.6 Detecting Memory Leaks

```javascript
// ============================================
// 1. CHROME DEVTOOLS MEMORY PROFILER
// ============================================

/*
Steps:
1. Open DevTools → Memory tab
2. Take Heap Snapshot
3. Perform actions (create objects, etc.)
4. Take another Heap Snapshot
5. Compare snapshots
   - Look for objects that shouldn't be retained
   - Check "Detached DOM tree"
   - Look for unexpected object counts
*/

// ============================================
// 2. MEMORY MONITORING
// ============================================

function monitorMemory() {
  if (performance.memory) {
    const used = performance.memory.usedJSHeapSize;
    const total = performance.memory.totalJSHeapSize;
    const limit = performance.memory.jsHeapSizeLimit;
    
    console.log({
      used: `${(used / 1048576).toFixed(2)} MB`,
      total: `${(total / 1048576).toFixed(2)} MB`,
      limit: `${(limit / 1048576).toFixed(2)} MB`,
      percentage: `${((used / limit) * 100).toFixed(2)}%`
    });
  }
}

// Monitor every 5 seconds
setInterval(monitorMemory, 5000);

// ============================================
// 3. LEAK DETECTION TEST
// ============================================

class LeakDetector {
  constructor() {
    this.snapshots = [];
  }
  
  takeSnapshot(label) {
    if (performance.memory) {
      this.snapshots.push({
        label,
        timestamp: Date.now(),
        memory: performance.memory.usedJSHeapSize
      });
    }
  }
  
  analyze() {
    console.log('\n=== Memory Leak Analysis ===');
    
    for (let i = 1; i < this.snapshots.length; i++) {
      const prev = this.snapshots[i - 1];
      const curr = this.snapshots[i];
      
      const diff = curr.memory - prev.memory;
      const diffMB = (diff / 1048576).toFixed(2);
      const timeDiff = curr.timestamp - prev.timestamp;
      
      console.log(`${prev.label} → ${curr.label}:`);
      console.log(`  Memory change: ${diffMB} MB`);
      console.log(`  Time: ${timeDiff}ms`);
      
      if (diff > 10485760) { // > 10MB
        console.warn('  ⚠️ Potential memory leak detected!');
      }
    }
  }
  
  reset() {
    this.snapshots = [];
  }
}

// Usage
const detector = new LeakDetector();

detector.takeSnapshot('Initial');

// Run suspicious code
for (let i = 0; i < 1000; i++) {
  suspiciousFunction();
}

detector.takeSnapshot('After 1000 iterations');

// Force GC if available (Chrome with --expose-gc flag)
if (global.gc) {
  global.gc();
}

detector.takeSnapshot('After GC');

detector.analyze();
```

### 4.7 Best Practices

```javascript
// ✅ 1. ALWAYS CLEANUP
class Component {
  constructor() {
    this.timers = [];
    this.listeners = [];
  }
  
  mount() {
    const timer = setInterval(() => this.update(), 1000);
    this.timers.push(timer);
    
    const handler = () => this.onClick();
    document.addEventListener('click', handler);
    this.listeners.push({ element: document, event: 'click', handler });
  }
  
  unmount() {
    this.timers.forEach(id => clearInterval(id));
    this.timers = [];
    
    this.listeners.forEach(({ element, event, handler }) => {
      element.removeEventListener(event, handler);
    });
    this.listeners = [];
  }
}

// ✅ 2. USE WEAKMAP/WEAKSET
const metadata = new WeakMap();

function attachMetadata(obj, data) {
  metadata.set(obj, data);
  // Khi obj được GC, metadata cũng tự động bị xóa
}

// ✅ 3. LIMIT CACHE SIZE
class LRUCache {
  constructor(maxSize = 100) {
    this.cache = new Map();
    this.maxSize = maxSize;
  }
  
  set(key, value) {
    if (this.cache.size >= this.maxSize) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    this.cache.set(key, value);
  }
  
  get(key) {
    const value = this.cache.get(key);
    if (value !== undefined) {
      // Move to end (LRU)
      this.cache.delete(key);
      this.cache.set(key, value);
    }
    return value;
  }
}

// ✅ 4. NULLIFY LARGE OBJECTS
function processLargeData() {
  let largeArray = new Array(1000000).fill(0);
  
  // Process data
  const result = largeArray.reduce((sum, val) => sum + val, 0);
  
  // Nullify to help GC
  largeArray = null;
  
  return result;
}

// ✅ 5. AVOID ACCIDENTAL GLOBALS
function myFunction() {
  'use strict'; // Prevents accidental globals
  
  const localVar = 10; // Must use let/const/var
}

// ✅ 6. USE ABORTCONTROLLER
async function fetchWithTimeout(url, timeout = 5000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);
  
  try {
    const response = await fetch(url, {
      signal: controller.signal
    });
    clearTimeout(timeoutId);
    return await response.json();
  } catch (error) {
    clearTimeout(timeoutId);
    throw error;
  }
}
```

---

## Tổng Kết

### Checklist Kiến Thức

- [ ] Hiểu IIFE và khi nào sử dụng
- [ ] Nắm vững call(), apply(), bind()
- [ ] Biết sự khác biệt Interpreter vs Compiler vs JIT
- [ ] Hiểu JavaScript Engine pipeline (Parser → AST → Bytecode → Machine Code)
- [ ] Viết optimization-friendly code
- [ ] Hiểu Garbage Collection (Mark-and-Sweep)
- [ ] Nhận biết và fix memory leaks
- [ ] Sử dụng DevTools để profile memory

### Key Takeaways

1. **IIFE**: Module pattern, private variables, avoid global pollution
2. **call/apply/bind**: Kiểm soát `this` context
3. **JIT Compiler**: Write type-stable, monomorphic code để optimize
4. **Garbage Collection**: Cleanup resources, avoid memory leaks

### Bài Tập Thực Hành

Tạo một **Task Manager Application**:

1. **IIFE**: Dùng Module Pattern để tạo private state
2. **bind()**: Handle event listeners đúng context
3. **Optimization**: Viết code JIT-friendly (type stable)
4. **Memory**: Cleanup timers, listeners khi remove tasks

### Tips Performance

```javascript
// 1. Keep functions small and focused
// 2. Use consistent types
// 3. Initialize objects completely in constructor
// 4. Avoid delete operator
// 5. Use typed arrays for numeric data
// 6. Profile before optimizing
// 7. Cleanup resources properly
// 8. Use WeakMap/WeakSet cho metadata
```

---

**Chúc bạn học tốt! 🚀**

*"Premature optimization is the root of all evil" - Donald Knuth*
*Nhưng understanding optimization principles là quan trọng!*
