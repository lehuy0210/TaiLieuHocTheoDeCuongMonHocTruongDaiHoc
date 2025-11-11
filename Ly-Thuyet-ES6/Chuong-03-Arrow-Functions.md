# CHƯƠNG 3: ARROW FUNCTIONS

## 3.1. Giới thiệu Arrow Functions

Arrow functions là cú pháp ngắn gọn hơn cho function expressions.

### 3.1.1. Syntax

**ES5:**
```javascript
var add = function(a, b) {
    return a + b;
};
```

**ES6:**
```javascript
const add = (a, b) => {
    return a + b;
};

// Implicit return (1 expression)
const add = (a, b) => a + b;
```

## 3.2. Syntax Variations

### 3.2.1. No Parameters

```javascript
// ES5
var greet = function() {
    return 'Hello';
};

// ES6
const greet = () => 'Hello';
```

### 3.2.2. One Parameter

```javascript
// Có thể bỏ parentheses
const double = n => n * 2;

// Hoặc giữ parentheses (recommended)
const double = (n) => n * 2;
```

### 3.2.3. Multiple Parameters

```javascript
const add = (a, b) => a + b;

const fullName = (first, last) => `${first} ${last}`;
```

### 3.2.4. Multiple Statements

```javascript
const calculate = (a, b) => {
    const sum = a + b;
    const product = a * b;
    return { sum, product };
};
```

### 3.2.5. Returning Object Literals

```javascript
// Wrap in parentheses
const makeUser = (name, age) => ({ name, age });

// NOT this (interpreted as function body)
const makeUser = (name, age) => { name, age };  // ERROR
```

## 3.3. this Binding

### 3.3.1. Traditional Functions

```javascript
function Person() {
    this.age = 0;

    setInterval(function() {
        this.age++;  // 'this' refers to global/undefined
    }, 1000);
}

// Fix với .bind()
function Person() {
    this.age = 0;

    setInterval(function() {
        this.age++;
    }.bind(this), 1000);
}

// Fix với variable
function Person() {
    this.age = 0;
    var self = this;

    setInterval(function() {
        self.age++;
    }, 1000);
}
```

### 3.3.2. Arrow Functions

```javascript
// Arrow function inherits 'this'
function Person() {
    this.age = 0;

    setInterval(() => {
        this.age++;  // 'this' từ Person
    }, 1000);
}
```

### 3.3.3. Practical Example

```javascript
const team = {
    members: ['John', 'Jane'],
    teamName: 'Super Squad',

    // Traditional function
    printMembers() {
        this.members.forEach(function(member) {
            // 'this' is undefined here
            console.log(this.teamName + ': ' + member);  // ERROR
        });
    },

    // Arrow function
    printMembersArrow() {
        this.members.forEach(member => {
            // 'this' from team object
            console.log(`${this.teamName}: ${member}`);  // Works!
        });
    }
};
```

## 3.4. When NOT to Use Arrow Functions

### 3.4.1. Object Methods

```javascript
// BAD
const person = {
    name: 'John',
    greet: () => {
        console.log(`Hello, ${this.name}`);  // 'this' is undefined
    }
};

// GOOD
const person = {
    name: 'John',
    greet() {
        console.log(`Hello, ${this.name}`);
    }
};
```

### 3.4.2. Prototype Methods

```javascript
// BAD
Person.prototype.greet = () => {
    console.log(this.name);  // 'this' is undefined
};

// GOOD
Person.prototype.greet = function() {
    console.log(this.name);
};
```

### 3.4.3. Event Handlers (when need 'this')

```javascript
// BAD
button.addEventListener('click', () => {
    this.classList.toggle('active');  // 'this' is not the button
});

// GOOD
button.addEventListener('click', function() {
    this.classList.toggle('active');  // 'this' is the button
});
```

### 3.4.4. Constructors

```javascript
// Cannot use arrow function as constructor
const Person = (name) => {
    this.name = name;
};

const john = new Person('John');  // ERROR: not a constructor
```

## 3.5. Practical Examples

### 3.5.1. Array Methods

```javascript
const numbers = [1, 2, 3, 4, 5];

// map
const doubled = numbers.map(n => n * 2);

// filter
const evens = numbers.filter(n => n % 2 === 0);

// reduce
const sum = numbers.reduce((total, n) => total + n, 0);

// find
const firstEven = numbers.find(n => n % 2 === 0);

// sort
const sorted = numbers.sort((a, b) => b - a);
```

### 3.5.2. Promises

```javascript
fetch('/api/users')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
```

### 3.5.3. setTimeout/setInterval

```javascript
setTimeout(() => {
    console.log('Delayed message');
}, 1000);

const interval = setInterval(() => {
    console.log('Repeating message');
}, 1000);
```

### 3.5.4. Chaining

```javascript
const users = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 },
    { name: 'Bob', age: 35 }
];

const result = users
    .filter(user => user.age >= 30)
    .map(user => user.name)
    .join(', ');

console.log(result);  // "John, Bob"
```

## 3.6. Arguments Object

### 3.6.1. Traditional Functions

```javascript
function sum() {
    console.log(arguments);  // [1, 2, 3]
    return Array.from(arguments).reduce((a, b) => a + b);
}

sum(1, 2, 3);  // 6
```

### 3.6.2. Arrow Functions (no arguments)

```javascript
// Arrow functions don't have 'arguments'
const sum = () => {
    console.log(arguments);  // ReferenceError
};

// Use rest parameters instead
const sum = (...args) => {
    return args.reduce((a, b) => a + b);
};

sum(1, 2, 3);  // 6
```

## 3.7. Best Practices

### 3.7.1. Khi nào dùng Arrow Functions

**Use arrow functions for:**
- Callbacks
- Array methods
- Promises
- Short functions
- When you need lexical 'this'

**Use traditional functions for:**
- Object methods
- Prototype methods
- Constructors
- When you need 'arguments'
- When you need dynamic 'this'

### 3.7.2. Readability

```javascript
// Clear and concise
const double = n => n * 2;

// Too concise (less readable)
const complex = (a,b,c,d) => a+b>c?d:a;

// Better (more readable)
const complex = (a, b, c, d) => {
    return a + b > c ? d : a;
};
```

## 3.8. Exercises

### Exercise 1: Convert to Arrow Functions

```javascript
// Convert these to arrow functions
function square(x) {
    return x * x;
}

function isEven(num) {
    return num % 2 === 0;
}
```

### Exercise 2: Fix 'this' Issue

```javascript
// Fix this code using arrow function
const counter = {
    count: 0,
    increment() {
        setInterval(function() {
            this.count++;
            console.log(this.count);
        }, 1000);
    }
};
```

---

**Kết luận:** Arrow functions làm code ngắn gọn và giải quyết vấn đề 'this' binding. Tuy nhiên, cần biết khi nào nên dùng và khi nào không nên dùng.
