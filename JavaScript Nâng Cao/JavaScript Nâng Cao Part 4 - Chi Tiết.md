# JavaScript Nâng Cao Part 4 - Chi Tiết 📚

> **Mục tiêu**: Nắm vững IIFE, call/apply/bind, JavaScript Engine, và Garbage Collection
>
> **Đối tượng**: Sinh viên học lực trung bình khá
>
> **Thời gian**: 6-8 giờ học

---

## 📋 Mục Lục

1. [IIFE (Immediately Invoked Function Expression)](#1-iife)
   - 1.1 IIFE là gì?
   - 1.2 Tại sao cần IIFE?
   - 1.3 IIFE với Parameters
   - 1.4 IIFE Patterns (Module, Revealing Module, Singleton)
   - 1.5 IIFE trong Loops
   - 1.6 Arrow Functions và IIFE
   - 1.7 Best Practices
   - 1.8 Modern Alternatives
   - 🎯 Bài tập thực hành

2. [call(), apply(), bind()](#2-call-apply-bind)
   - 2.1 Hiểu về `this` Context
   - 2.2 call() Method
   - 2.3 apply() Method
   - 2.4 bind() Method
   - 2.5 So sánh call, apply, bind
   - 2.6 Practical Examples
   - 2.7 Best Practices
   - 🎯 Bài tập thực hành

3. [Interpreter / Compiler / JIT Compiler](#3-interpreter-compiler-jit)
   - 3.1 Interpreted vs Compiled Languages
   - 3.2 JavaScript Engine Pipeline
   - 3.3 Parser và AST
   - 3.4 Interpreter (Ignition)
   - 3.5 JIT (Just-In-Time) Compiler
   - 3.6 Optimization Examples
   - 3.7 Writing Optimization-Friendly Code
   - 3.8 Profiling và Debugging
   - 🎯 Bài tập thực hành

4. [Garbage Collection](#4-garbage-collection)
   - 4.1 Garbage Collection là gì?
   - 4.2 Reachability (Khả năng truy cập)
   - 4.3 Mark-and-Sweep Algorithm
   - 4.4 Generational Garbage Collection
   - 4.5 Memory Leaks
   - 4.6 Detecting Memory Leaks
   - 4.7 Best Practices
   - 🎯 Bài tập thực hành

5. [Tổng kết và Bài tập tổng hợp](#tong-ket)

---

## 1. IIFE (Immediately Invoked Function Expression) {#1-iife}

### 🤔 Tư Duy: Tại Sao Cần IIFE?

**Problem 1: Global Scope Pollution**

```javascript
// ❌ Code cũ: Variables trong global scope
var counter = 0;
var increment = function() {
  counter++;
};

// Problem: counter có thể bị conflict
var counter = 100; // Overwrite! Bug khó tìm
```

**Problem 2: Không có private variables**

```javascript
// ❌ Tất cả variables đều public
var bankBalance = 1000;
bankBalance = -999; // Ai cũng có thể modify! ⚠️
```

**Solution: IIFE**

```javascript
// ✅ IIFE tạo scope riêng
var BankModule = (function() {
  var balance = 1000; // Private!

  return {
    getBalance: function() {
      return balance;
    },
    deposit: function(amount) {
      if (amount > 0) balance += amount;
    }
  };
})();

// balance = -999; // ❌ ReferenceError - cannot access private variable
BankModule.deposit(500);
console.log(BankModule.getBalance()); // 1500 ✅
```

**💡 Lợi ích IIFE**:
- ✅ Tránh pollution global scope
- ✅ Tạo private variables/functions
- ✅ Module pattern (trước ES6 modules)
- ✅ Execute code ngay lập tức
- ✅ Avoid naming conflicts

---

### 1.1 IIFE là gì?

**Định nghĩa**: IIFE (Immediately Invoked Function Expression) là function được định nghĩa và thực thi **ngay lập tức**, không cần gọi riêng.

#### 📌 Cú Pháp Cơ Bản

```javascript
// Cú pháp 1: (function() { })()
(function() {
  console.log("IIFE thực thi ngay!");
})();

// Cú pháp 2: (function() { }())
(function() {
  console.log("IIFE cú pháp thứ 2");
}());

// Cú pháp 3: Unary operators
!function() {
  console.log("IIFE với !");
}();

+function() {
  console.log("IIFE với +");
}();

void function() {
  console.log("IIFE với void");
}();

// So sánh với function thông thường
function normalFunction() {
  console.log("Function thông thường");
}
normalFunction(); // ❌ Phải gọi manual

// IIFE
(function() {
  console.log("IIFE");
})(); // ✅ Execute ngay!
```

#### 💡 Giải Thích

```
SYNTAX BREAKDOWN:

(function() {
  // code
})();

1. (function() { })  ← Function Expression (wrapped trong parens)
2. ()                ← Invoke immediately

Tại sao cần parens?
- function() {} là Function DECLARATION
- (function() {}) là Function EXPRESSION
- Chỉ expressions mới có thể invoke immediately!

Các cách tạo expression:
- Grouping: (function() {})()
- Unary operators: !function() {}(), +function() {}()
- void operator: void function() {}()
```

---

### 1.2 Tại Sao Cần IIFE?

#### ❌ Problem 1: Global Scope Pollution

```javascript
// ❌ BAD: Tất cả variables trong global scope
var counter = 0;
var temp = "temporary";
var helper = function() { };

// Tất cả những variables trên pollute global scope
console.log(window.counter);  // 0
console.log(window.temp);     // "temporary"
console.log(window.helper);   // function

// Risk: Naming conflicts
// File 1:
var config = { mode: "dev" };

// File 2:
var config = { mode: "prod" }; // ❌ Overwrite!

// ✅ GOOD: Dùng IIFE để encapsulate
(function() {
  var counter = 0;        // Private
  var temp = "temporary"; // Private
  var helper = function() { }; // Private

  // Only expose what's needed
  window.MyApp = {
    getCounter: function() {
      return counter;
    }
  };
})();

// console.log(counter); // ❌ ReferenceError
console.log(MyApp.getCounter()); // ✅ 0
```

#### ❌ Problem 2: Không Có Private Variables

```javascript
// ❌ BAD: Không có cách tạo private variables (trước ES6)
var BankAccount = {
  balance: 1000, // Public!

  deposit: function(amount) {
    this.balance += amount;
  }
};

// Ai cũng có thể access và modify
BankAccount.balance = 999999; // ❌ Hack!

// ✅ GOOD: IIFE tạo private variables
var BankAccount = (function() {
  var balance = 1000; // Private!
  var accountNumber = "123456"; // Private!

  return {
    deposit: function(amount) {
      if (amount > 0) {
        balance += amount;
        return `✅ Nạp ${amount}đ. Số dư: ${balance}đ`;
      }
      return "❌ Số tiền không hợp lệ";
    },

    withdraw: function(amount) {
      if (amount > 0 && amount <= balance) {
        balance -= amount;
        return `✅ Rút ${amount}đ. Số dư: ${balance}đ`;
      }
      return "❌ Không thể rút tiền";
    },

    getBalance: function() {
      return balance;
    }
  };
})();

console.log(BankAccount.deposit(500));     // "✅ Nạp 500đ. Số dư: 1500đ"
console.log(BankAccount.withdraw(200));    // "✅ Rút 200đ. Số dư: 1300đ"
console.log(BankAccount.getBalance());     // 1300
// console.log(BankAccount.balance);       // undefined (private!) ✅
// BankAccount.balance = 999999;           // Không effect vào private variable
```

---

### 1.3 IIFE với Parameters

IIFE có thể nhận parameters giống function thông thường.

```javascript
// Basic parameters
(function(name, age) {
  console.log(`Tôi là ${name}, ${age} tuổi`);
})("An", 25);

// Output: "Tôi là An, 25 tuổi"

// Practical: Inject dependencies
var $ = (function(window, document, undefined) {
  // undefined được pass nhưng không có argument
  // → đảm bảo undefined thực sự là undefined (IE8 bug)

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

// Inject global objects
(function(global, $) {
  // global có thể là window (browser) hoặc global (Node.js)
  // $ là jQuery

  global.MyLibrary = {
    init: function() {
      console.log("Initialized with jQuery version:", $.fn.jquery);
    }
  };
})(typeof window !== 'undefined' ? window : global, jQuery);

// Configuration IIFE
var AppConfig = (function() {
  var env = "development"; // Could read from process.env

  var configs = {
    development: {
      apiUrl: "http://localhost:3000",
      debug: true,
      logLevel: "verbose"
    },
    production: {
      apiUrl: "https://api.production.com",
      debug: false,
      logLevel: "error"
    }
  };

  return configs[env];
})();

console.log(AppConfig.apiUrl);  // "http://localhost:3000"
console.log(AppConfig.debug);   // true
```

---

### 1.4 IIFE Patterns

#### 📌 Pattern 1: Module Pattern

```javascript
var ShoppingCart = (function() {
  // Private variables
  var items = [];
  var total = 0;
  var taxRate = 0.1;

  // Private functions
  function calculateTotal() {
    total = items.reduce((sum, item) => {
      return sum + (item.price * item.quantity);
    }, 0);
  }

  function applyTax() {
    return total * (1 + taxRate);
  }

  // Public API
  return {
    addItem: function(name, price, quantity = 1) {
      items.push({ name, price, quantity });
      calculateTotal();
      console.log(`✅ Đã thêm ${name}`);
    },

    removeItem: function(name) {
      const initialLength = items.length;
      items = items.filter(item => item.name !== name);

      if (items.length < initialLength) {
        calculateTotal();
        console.log(`✅ Đã xóa ${name}`);
      } else {
        console.log(`❌ Không tìm thấy ${name}`);
      }
    },

    getTotal: function() {
      return total;
    },

    getTotalWithTax: function() {
      return applyTax();
    },

    getItems: function() {
      return [...items]; // Return copy để không thay đổi được original
    },

    getItemCount: function() {
      return items.reduce((count, item) => count + item.quantity, 0);
    },

    clear: function() {
      items = [];
      total = 0;
      console.log("✅ Giỏ hàng đã được làm trống");
    }
  };
})();

// Test
ShoppingCart.addItem("Laptop", 1000, 1);
ShoppingCart.addItem("Mouse", 50, 2);
ShoppingCart.addItem("Keyboard", 100, 1);

console.log("Total items:", ShoppingCart.getItemCount());      // 4
console.log("Subtotal:", ShoppingCart.getTotal());             // 1200
console.log("Total with tax:", ShoppingCart.getTotalWithTax()); // 1320

ShoppingCart.removeItem("Mouse");
console.log("Items:", ShoppingCart.getItems());

// ❌ Không thể access private variables
// console.log(ShoppingCart.items);       // undefined
// console.log(ShoppingCart.taxRate);     // undefined
// ShoppingCart.items.push({});           // Error
```

#### 📌 Pattern 2: Revealing Module Pattern

```javascript
var Calculator = (function() {
  var result = 0;
  var history = [];

  // Private helper
  function log(operation, value) {
    var entry = `${operation} ${value}, result: ${result}`;
    history.push(entry);
    console.log(`[Calculator] ${entry}`);
  }

  // All functions (public and private)
  function add(x) {
    result += x;
    log("Added", x);
    return this;
  }

  function subtract(x) {
    result -= x;
    log("Subtracted", x);
    return this;
  }

  function multiply(x) {
    result *= x;
    log("Multiplied by", x);
    return this;
  }

  function divide(x) {
    if (x === 0) {
      console.error("❌ Cannot divide by zero");
      return this;
    }
    result /= x;
    log("Divided by", x);
    return this;
  }

  function getResult() {
    return result;
  }

  function reset() {
    result = 0;
    log("Reset", "to 0");
    return this;
  }

  function getHistory() {
    return [...history];
  }

  function clearHistory() {
    history = [];
    console.log("History cleared");
    return this;
  }

  // Reveal only what should be public
  return {
    add: add,
    subtract: subtract,
    multiply: multiply,
    divide: divide,
    getResult: getResult,
    reset: reset,
    getHistory: getHistory,
    clearHistory: clearHistory
  };
})();

// Usage: Method chaining
Calculator
  .add(10)
  .multiply(2)
  .subtract(5)
  .divide(3);

console.log("Result:", Calculator.getResult()); // 5
console.log("History:", Calculator.getHistory());

Calculator.reset();
console.log("After reset:", Calculator.getResult()); // 0
```

#### 📌 Pattern 3: Singleton Pattern

```javascript
var Database = (function() {
  var instance; // Private variable giữ singleton instance

  function createInstance() {
    // Private constructor
    var connection = "DB_CONNECTION_STRING";
    var data = [];
    var isConnected = false;

    return {
      connect: function() {
        if (!isConnected) {
          console.log("🔌 Connected to database");
          isConnected = true;
        } else {
          console.log("⚠️ Already connected");
        }
      },

      disconnect: function() {
        if (isConnected) {
          console.log("🔌 Disconnected from database");
          isConnected = false;
        }
      },

      insert: function(record) {
        if (!isConnected) {
          console.error("❌ Not connected to database");
          return;
        }
        data.push(record);
        console.log("✅ Inserted:", record);
      },

      getAll: function() {
        if (!isConnected) {
          console.error("❌ Not connected to database");
          return [];
        }
        return [...data];
      },

      query: function(filter) {
        if (!isConnected) {
          console.error("❌ Not connected to database");
          return [];
        }
        return data.filter(filter);
      },

      clear: function() {
        data = [];
        console.log("🗑️ Database cleared");
      }
    };
  }

  return {
    getInstance: function() {
      if (!instance) {
        instance = createInstance();
        console.log("🆕 New database instance created");
      } else {
        console.log("♻️ Returning existing database instance");
      }
      return instance;
    }
  };
})();

// Test Singleton
var db1 = Database.getInstance(); // "🆕 New database instance created"
var db2 = Database.getInstance(); // "♻️ Returning existing database instance"

console.log(db1 === db2); // true (cùng instance) ✅

db1.connect();
db1.insert({ id: 1, name: "User 1" });
db1.insert({ id: 2, name: "User 2" });

// db2 cũng thấy data vì cùng instance
console.log(db2.getAll()); // [{ id: 1, name: "User 1" }, { id: 2, name: "User 2" }]
```

---

### 1.5 IIFE trong Loops (Classic Problem)

Đây là một trong những use cases quan trọng nhất của IIFE!

#### ❌ Problem: Closure với var trong loop

```javascript
// ❌ BAD: Tất cả log ra 5
console.log("Với var:");
for (var i = 0; i < 5; i++) {
  setTimeout(function() {
    console.log(i); // 5, 5, 5, 5, 5
  }, 100);
}

/*
💭 Tại sao?
1. var là function-scoped (không phải block-scoped)
2. Loop chạy nhanh, tạo 5 setTimeout callbacks
3. Khi callbacks execute (sau 100ms), loop đã kết thúc
4. i = 5 (giá trị cuối cùng)
5. Tất cả callbacks đều reference cùng một i → log ra 5

Timeline:
t=0ms:   Loop chạy, i=0,1,2,3,4,5 (kết thúc)
t=100ms: Callback 1 chạy, i=5 → log 5
t=100ms: Callback 2 chạy, i=5 → log 5
t=100ms: Callback 3 chạy, i=5 → log 5
t=100ms: Callback 4 chạy, i=5 → log 5
t=100ms: Callback 5 chạy, i=5 → log 5
*/
```

#### ✅ Solution 1: IIFE

```javascript
// ✅ GOOD: IIFE tạo closure riêng cho mỗi iteration
console.log("\nVới IIFE:");
for (var i = 0; i < 5; i++) {
  (function(index) {
    setTimeout(function() {
      console.log(index); // 0, 1, 2, 3, 4 ✅
    }, 100);
  })(i); // Pass giá trị i vào IIFE
}

/*
💡 Tại sao works?
1. Mỗi iteration, IIFE được gọi với giá trị i hiện tại
2. IIFE tạo scope mới với parameter 'index'
3. 'index' capture giá trị của i tại thời điểm đó
4. Callback closure giữ reference đến 'index' riêng của nó

Memory:
Iteration 0: IIFE(index=0) → setTimeout(fn captures index=0)
Iteration 1: IIFE(index=1) → setTimeout(fn captures index=1)
Iteration 2: IIFE(index=2) → setTimeout(fn captures index=2)
Iteration 3: IIFE(index=3) → setTimeout(fn captures index=3)
Iteration 4: IIFE(index=4) → setTimeout(fn captures index=4)
*/
```

#### ✅ Solution 2: let (ES6+, Preferred)

```javascript
// ✅ MODERN: Dùng let (block-scoped)
console.log("\nVới let:");
for (let i = 0; i < 5; i++) {
  setTimeout(function() {
    console.log(i); // 0, 1, 2, 3, 4 ✅
  }, 100);
}

/*
💡 let tạo binding mới cho mỗi iteration!
- let là block-scoped
- Mỗi iteration của loop tạo scope mới
- i mới được tạo cho mỗi iteration

No need IIFE! Modern và clean hơn.
*/
```

#### 📌 Real-World Example: Event Listeners

```javascript
// ❌ BAD: Với var
var buttons = document.querySelectorAll('.button');

for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    console.log('Button ' + i + ' clicked');
    // Luôn log index cuối! ❌
  });
}

// ✅ GOOD: Với IIFE
for (var i = 0; i < buttons.length; i++) {
  (function(index) {
    buttons[index].addEventListener('click', function() {
      console.log('Button ' + index + ' clicked'); // Đúng index ✅
    });
  })(i);
}

// ✅ MODERN: Với let
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    console.log('Button ' + i + ' clicked'); // Đúng index ✅
  });
}

// ✅ ALTERNATIVE: forEach (no loop variable issue)
buttons.forEach(function(button, index) {
  button.addEventListener('click', function() {
    console.log('Button ' + index + ' clicked'); // ✅
  });
});
```

---

### 1.6 Arrow Functions và IIFE

ES6 arrow functions cũng có thể dùng với IIFE.

```javascript
// Basic arrow IIFE
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

// ✅ Async IIFE (Very useful!)
(async () => {
  try {
    console.log("Fetching data...");
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log("Data:", data);
  } catch (error) {
    console.error('Error:', error);
  }
})();

// Top-level await alternative (before ES2022)
(async function() {
  const users = await fetchUsers();
  const posts = await fetchPosts();

  console.log("Users:", users.length);
  console.log("Posts:", posts.length);
})();

// Multiple async operations
(async () => {
  const [users, posts, comments] = await Promise.all([
    fetchUsers(),
    fetchPosts(),
    fetchComments()
  ]);

  console.log(`Loaded ${users.length} users, ${posts.length} posts, ${comments.length} comments`);
})();
```

---

### 1.7 Best Practices

```javascript
// ✅ 1. SEMICOLON trước IIFE (tránh lỗi concatenation)
var x = 10

// ❌ BAD: Không có semicolon
(function() {
  console.log("IIFE");
})();
// Lỗi: 10 is not a function
// Vì JavaScript hiểu: var x = 10(function() {})();

// ✅ GOOD: Có semicolon
var x = 10
;(function() {
  console.log("Safe IIFE");
})();

// ✅ 2. USE STRICT MODE
(function() {
  'use strict'; // Strict mode chỉ apply trong IIFE

  undeclaredVar = 10; // ❌ ReferenceError (good!)
  // Ngăn accidental globals

  with (obj) { } // ❌ SyntaxError
  delete Object.prototype; // ❌ TypeError

  // More restrictions...
})();

// Outside IIFE vẫn là sloppy mode
undeclaredGlobal = 20; // OK (but bad practice)

// ✅ 3. NAMED IIFE (dễ debug)
(function myIIFE() {
  console.log("Named IIFE");

  // Function name hiện trong stack trace
  // throw new Error("Error in myIIFE"); // Stack trace shows "myIIFE"
})();

// Compare stack traces:
// Anonymous IIFE: "at <anonymous>:1:1"
// Named IIFE: "at myIIFE:1:1" ← Easier to debug!

// ✅ 4. RETURN VALUES
var config = (function() {
  var env = "development"; // Could read from process.env.NODE_ENV

  var configs = {
    development: {
      apiUrl: 'http://localhost:3000',
      debug: true,
      maxRetries: 3
    },
    production: {
      apiUrl: 'https://api.production.com',
      debug: false,
      maxRetries: 5
    }
  };

  return configs[env];
})();

console.log(config.apiUrl); // "http://localhost:3000"

// ✅ 5. INJECT DEPENDENCIES
var MyModule = (function($, _, Backbone) {
  // Private
  var cache = {};

  // Public API
  return {
    init: function() {
      console.log("Initialized with:", {
        jQuery: $.fn.jquery,
        Lodash: _.VERSION,
        Backbone: Backbone.VERSION
      });
    },

    fetchData: function(url) {
      if (cache[url]) {
        return Promise.resolve(cache[url]);
      }

      return $.ajax(url).then(function(data) {
        cache[url] = data;
        return data;
      });
    }
  };
})(jQuery, _, Backbone); // Inject dependencies

// ✅ 6. AVOID NESTED IIFE (hard to read)
// ❌ BAD
(function() {
  (function() {
    (function() {
      console.log("Too nested!");
    })();
  })();
})();

// ✅ GOOD: One level, clear purpose
(function() {
  console.log("Clear and readable");
})();
```

---

### 1.8 Modern Alternatives to IIFE

IIFE was essential before ES6, but now we have better alternatives.

```javascript
// ============================================
// 1. ES6 MODULES (Preferred!)
// ============================================

// module.js
export const version = "1.0.0";
const privateVar = "secret"; // Not exported = private

export function add(a, b) {
  return a + b;
}

// app.js
import { version, add } from './module.js';

console.log(version); // "1.0.0"
console.log(add(1, 2)); // 3
// console.log(privateVar); // ❌ Not accessible

// ============================================
// 2. BLOCK SCOPE với let/const
// ============================================

// Old IIFE way
(function() {
  var temp = "temporary";
  console.log(temp);
})();
// console.log(temp); // ReferenceError

// Modern way
{
  let temp = "temporary";
  console.log(temp);
}
// console.log(temp); // ReferenceError

// Even simpler for single use
{
  const result = calculateSomething();
  console.log(result);
}

// ============================================
// 3. CLASS với PRIVATE FIELDS (ES2022)
// ============================================

// Old IIFE way
var Counter = (function() {
  var count = 0;

  return {
    increment: function() {
      count++;
    },
    getCount: function() {
      return count;
    }
  };
})();

// Modern way
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
// console.log(counter.#count); // ❌ SyntaxError

// ============================================
// 4. ASYNC/AWAIT (Top-level await ES2022)
// ============================================

// Old IIFE way
(async function() {
  const data = await fetchData();
  console.log(data);
})();

// Modern way (ES2022 modules)
// app.mjs
const data = await fetchData();
console.log(data);
```

**💡 Khi nào vẫn dùng IIFE?**
- Legacy code maintenance
- Browser compatibility (IE support)
- Quick scripts/snippets
- Avoiding global pollution trong HTML `<script>` tags

**📌 Summary Table**

| Feature | IIFE | ES6 Modules | Block Scope | Classes |
|---------|------|-------------|-------------|---------|
| Private variables | ✅ | ✅ | ✅ | ✅ (ES2022) |
| Immediate execution | ✅ | ⚠️ (on import) | ✅ | ❌ |
| Browser support | ✅ All | ⚠️ Modern | ✅ Modern | ✅ Modern |
| Recommended | ❌ Legacy | ✅ Yes | ✅ Yes | ✅ Yes |

---

### 🎯 Bài Tập 1: IIFE

#### Bài 1: Counter Module

Tạo counter module với:
- Private count variable
- increment(), decrement(), reset(), getCount() methods
- Không cho phép set count trực tiếp

<details>
<summary>✅ Giải pháp</summary>

```javascript
var Counter = (function() {
  var count = 0;
  var history = [];

  function logChange(operation, newValue) {
    history.push({
      operation: operation,
      value: newValue,
      timestamp: new Date()
    });
  }

  return {
    increment: function(step = 1) {
      count += step;
      logChange('increment', count);
      console.log(`✅ Count increased by ${step} to ${count}`);
      return this; // For chaining
    },

    decrement: function(step = 1) {
      count -= step;
      logChange('decrement', count);
      console.log(`✅ Count decreased by ${step} to ${count}`);
      return this;
    },

    reset: function() {
      count = 0;
      logChange('reset', 0);
      console.log("✅ Count reset to 0");
      return this;
    },

    getCount: function() {
      return count;
    },

    getHistory: function() {
      return [...history]; // Return copy
    }
  };
})();

// Test
Counter.increment().increment(5).decrement(2);
console.log("Current count:", Counter.getCount()); // 4
console.log("History:", Counter.getHistory());
Counter.reset();
console.log("After reset:", Counter.getCount()); // 0
```

</details>

---

#### Bài 2: Fix Loop Bug

Fix bug trong code sau:

```javascript
// ❌ Bug: All buttons alert "Button 3"
var buttons = document.querySelectorAll('.btn');
for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    alert('Button ' + i);
  });
}
```

<details>
<summary>💡 Gợi ý</summary>

1. Dùng IIFE để capture giá trị i
2. Hoặc dùng let thay vì var
3. Hoặc dùng forEach

</details>

<details>
<summary>✅ Giải pháp</summary>

```javascript
// Solution 1: IIFE
var buttons = document.querySelectorAll('.btn');
for (var i = 0; i < buttons.length; i++) {
  (function(index) {
    buttons[index].addEventListener('click', function() {
      alert('Button ' + index); // ✅ Correct index
    });
  })(i);
}

// Solution 2: let
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    alert('Button ' + i); // ✅
  });
}

// Solution 3: forEach (recommended)
buttons.forEach(function(button, i) {
  button.addEventListener('click', function() {
    alert('Button ' + i); // ✅
  });
});

// Solution 4: Modern arrow function + dataset
buttons.forEach((button, i) => {
  button.dataset.index = i;
  button.addEventListener('click', (e) => {
    alert('Button ' + e.target.dataset.index);
  });
});
```

</details>

---

## 2. call(), apply(), bind() {#2-call-apply-bind}

### 🤔 Tư Duy: Tại Sao Cần Kiểm Soát `this`?

**Problem**: `this` trong JavaScript bị "mất" trong nhiều tình huống

```javascript
const person = {
  name: "An",
  greet: function() {
    console.log(`Hello, I'm ${this.name}`);
  }
};

person.greet(); // "Hello, I'm An" ✅

// ❌ Problem 1: Assign to variable
const greetFn = person.greet;
greetFn(); // "Hello, I'm undefined" ❌
// this bị mất khi assign sang variable!

// ❌ Problem 2: Callback
setTimeout(person.greet, 1000); // "Hello, I'm undefined" ❌

// ❌ Problem 3: Event handler
button.addEventListener('click', person.greet); // this = button element! ❌
```

**Solution**: `call()`, `apply()`, `bind()` để kiểm soát `this`

```javascript
// ✅ Solution với bind()
const greetBound = person.greet.bind(person);
greetBound(); // "Hello, I'm An" ✅

setTimeout(person.greet.bind(person), 1000); // ✅
button.addEventListener('click', person.greet.bind(person)); // ✅
```

---

### 2.1 Hiểu về `this` Context

Trước khi học call/apply/bind, cần hiểu `this` trong các contexts khác nhau.

```javascript
// ============================================
// 1. GLOBAL CONTEXT
// ============================================
console.log(this);
// Browser: Window object
// Node.js: global object (or module.exports trong modules)

// ============================================
// 2. OBJECT METHOD
// ============================================
const person = {
  name: "An",
  greet: function() {
    console.log(`Hello, I'm ${this.name}`);
  }
};

person.greet(); // this = person object

// ============================================
// 3. FUNCTION CALL (Regular function)
// ============================================
function showThis() {
  console.log(this);
}

showThis();
// Non-strict mode: window/global
// Strict mode: undefined

function strictFunction() {
  'use strict';
  console.log(this);
}

strictFunction(); // undefined

// ============================================
// 4. CONSTRUCTOR FUNCTION
// ============================================
function Person(name) {
  this.name = name; // this = new object being created
}

const p = new Person("An");
console.log(p.name); // "An"

// ============================================
// 5. ARROW FUNCTION (Không có this riêng!)
// ============================================
const obj = {
  name: "An",
  regularFn: function() {
    console.log("Regular:", this.name); // "An"
  },
  arrowFn: () => {
    console.log("Arrow:", this.name); // undefined!
    // this từ outer scope (global)
  }
};

obj.regularFn(); // "Regular: An"
obj.arrowFn();   // "Arrow: undefined"

// Arrow functions inherit this from parent scope
const outer = {
  name: "Outer",
  createInner: function() {
    return {
      name: "Inner",
      regularFn: function() {
        console.log(this.name); // "Inner"
      },
      arrowFn: () => {
        console.log(this.name); // "Outer" (từ createInner)
      }
    };
  }
};

const inner = outer.createInner();
inner.regularFn(); // "Inner"
inner.arrowFn();   // "Outer"

// ============================================
// 6. EVENT HANDLERS
// ============================================
button.addEventListener('click', function() {
  console.log(this); // button element
});

button.addEventListener('click', () => {
  console.log(this); // window/global (arrow function)
});
```

---

(Content continues with sections 2.2-4.7...)

---

**Chúc bạn học tốt! 🚀**

