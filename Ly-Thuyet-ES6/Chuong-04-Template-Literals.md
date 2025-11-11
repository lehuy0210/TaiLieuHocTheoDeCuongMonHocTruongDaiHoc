# CHƯƠNG 4: TEMPLATE LITERALS

## 4.1. Giới thiệu Template Literals

Template literals (template strings) là cách mới để làm việc với strings trong ES6, sử dụng backticks (\`) thay vì quotes.

### 4.1.1. Basic Syntax

**ES5:**
```javascript
var message = "Hello, World!";
var multiline = "Line 1\nLine 2";
```

**ES6:**
```javascript
const message = `Hello, World!`;
const multiline = `Line 1
Line 2`;
```

## 4.2. String Interpolation

### 4.2.1. Embedding Expressions

**ES5:**
```javascript
var name = 'John';
var age = 30;
var message = 'My name is ' + name + ' and I am ' + age + ' years old.';
```

**ES6:**
```javascript
const name = 'John';
const age = 30;
const message = `My name is ${name} and I am ${age} years old.`;
```

### 4.2.2. Expressions in ${}

```javascript
const a = 5;
const b = 10;

console.log(`Sum: ${a + b}`);        // "Sum: 15"
console.log(`Product: ${a * b}`);    // "Product: 50"
console.log(`Average: ${(a + b) / 2}`); // "Average: 7.5"
```

### 4.2.3. Function Calls

```javascript
function getGreeting() {
    return 'Hello';
}

const name = 'John';
console.log(`${getGreeting()}, ${name}!`); // "Hello, John!"

// Method calls
const user = {
    name: 'Jane',
    getName() {
        return this.name;
    }
};

console.log(`User: ${user.getName()}`); // "User: Jane"
```

### 4.2.4. Nested Template Literals

```javascript
const isActive = true;
const status = `Status: ${isActive ? `Active` : `Inactive`}`;
console.log(status); // "Status: Active"

// Complex nesting
const items = ['a', 'b', 'c'];
const list = `Items: ${items.map(item => `<${item}>`).join(', ')}`;
console.log(list); // "Items: <a>, <b>, <c>"
```

## 4.3. Multiline Strings

### 4.3.1. Basic Multiline

**ES5:**
```javascript
var html = '<div>\n' +
           '  <h1>Title</h1>\n' +
           '  <p>Content</p>\n' +
           '</div>';
```

**ES6:**
```javascript
const html = `
<div>
  <h1>Title</h1>
  <p>Content</p>
</div>
`;
```

### 4.3.2. Whitespace Handling

```javascript
// Whitespace is preserved
const text = `
    Line 1
        Line 2
    Line 3
`;
// Includes leading/trailing newlines and indentation

// Trim if needed
const trimmed = `
    Line 1
    Line 2
`.trim();
```

### 4.3.3. Practical HTML

```javascript
const user = { name: 'John', age: 30 };

const card = `
<div class="card">
  <h2>${user.name}</h2>
  <p>Age: ${user.age}</p>
</div>
`;

document.body.innerHTML = card;
```

## 4.4. Tagged Templates

### 4.4.1. Basic Tagged Template

```javascript
function tag(strings, ...values) {
    console.log('Strings:', strings);
    console.log('Values:', values);
}

const name = 'John';
const age = 30;

tag`Hello ${name}, you are ${age} years old.`;
// Strings: ['Hello ', ', you are ', ' years old.']
// Values: ['John', 30]
```

### 4.4.2. Processing with Tag Functions

```javascript
function highlight(strings, ...values) {
    return strings.reduce((result, str, i) => {
        return `${result}${str}<strong>${values[i] || ''}</strong>`;
    }, '');
}

const name = 'John';
const age = 30;

const result = highlight`Name: ${name}, Age: ${age}`;
console.log(result);
// "Name: <strong>John</strong>, Age: <strong>30</strong>"
```

### 4.4.3. HTML Escaping

```javascript
function escapeHTML(strings, ...values) {
    const escape = (str) => String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');

    return strings.reduce((result, str, i) => {
        return result + str + (values[i] ? escape(values[i]) : '');
    }, '');
}

const userInput = '<script>alert("XSS")</script>';
const safe = escapeHTML`User said: ${userInput}`;
console.log(safe);
// "User said: &lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;"
```

### 4.4.4. Currency Formatting

```javascript
function currency(strings, ...values) {
    return strings.reduce((result, str, i) => {
        const value = values[i];
        const formatted = value !== undefined
            ? `$${value.toFixed(2)}`
            : '';
        return result + str + formatted;
    }, '');
}

const price = 19.99;
const tax = 1.5;

console.log(currency`Price: ${price}, Tax: ${tax}`);
// "Price: $19.99, Tax: $1.50"
```

## 4.5. Practical Examples

### 4.5.1. Dynamic HTML Generation

```javascript
const products = [
    { name: 'Laptop', price: 999 },
    { name: 'Mouse', price: 29 },
    { name: 'Keyboard', price: 79 }
];

const productList = `
<ul class="products">
    ${products.map(p => `
        <li>
            <span class="name">${p.name}</span>
            <span class="price">$${p.price}</span>
        </li>
    `).join('')}
</ul>
`;
```

### 4.5.2. SQL Queries

```javascript
function query(userId, status) {
    return `
        SELECT * FROM users
        WHERE id = ${userId}
        AND status = '${status}'
        ORDER BY created_at DESC
    `;
}

// Note: In production, use parameterized queries!
```

### 4.5.3. Email Templates

```javascript
function createEmail(user, order) {
    return `
        Hi ${user.name},

        Thank you for your order #${order.id}!

        Order Details:
        ${order.items.map(item => `
            - ${item.name}: $${item.price}
        `).join('')}

        Total: $${order.total}

        Best regards,
        The Team
    `.trim();
}
```

### 4.5.4. Console Logging

```javascript
function log(level, message, data) {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${level.toUpperCase()}: ${message}`, data);
}

log('info', 'User logged in', { userId: 123 });
// "[2024-01-15T10:30:00.000Z] INFO: User logged in" { userId: 123 }
```

### 4.5.5. URL Building

```javascript
function buildURL(base, params) {
    const query = Object.entries(params)
        .map(([key, value]) => `${key}=${encodeURIComponent(value)}`)
        .join('&');

    return `${base}?${query}`;
}

const url = buildURL('https://api.example.com/search', {
    q: 'javascript',
    page: 1,
    limit: 10
});
// "https://api.example.com/search?q=javascript&page=1&limit=10"
```

## 4.6. Advanced Patterns

### 4.6.1. Conditional Content

```javascript
const user = { name: 'John', isAdmin: true };

const greeting = `
    Hello, ${user.name}!
    ${user.isAdmin ? `
        <div class="admin-panel">
            Admin Controls
        </div>
    ` : ''}
`;
```

### 4.6.2. Array Mapping

```javascript
const numbers = [1, 2, 3, 4, 5];

const list = `
    Numbers:
    ${numbers.map(n => `- ${n} squared is ${n * n}`).join('\n    ')}
`;
```

### 4.6.3. Nested Objects

```javascript
const data = {
    user: {
        name: 'John',
        address: {
            city: 'NYC',
            country: 'USA'
        }
    }
};

const info = `
    User: ${data.user.name}
    Location: ${data.user.address.city}, ${data.user.address.country}
`;
```

## 4.7. Common Patterns

### 4.7.1. Debug Logging

```javascript
const debug = (label, value) => {
    console.log(`[DEBUG] ${label}:`, value);
};

const user = { id: 1, name: 'John' };
debug('User object', user);
// [DEBUG] User object: { id: 1, name: 'John' }
```

### 4.7.2. String Repetition

```javascript
const repeat = (str, times) => {
    return `${str.repeat(times)}`;
};

console.log(`${'='.repeat(20)}`); // "===================="
```

### 4.7.3. Table Formatting

```javascript
const users = [
    { id: 1, name: 'John', age: 30 },
    { id: 2, name: 'Jane', age: 25 }
];

const table = `
| ID | Name | Age |
|----|------|-----|
${users.map(u => `| ${u.id}  | ${u.name} | ${u.age}  |`).join('\n')}
`;

console.log(table);
```

## 4.8. Best Practices

### 4.8.1. Readability

```javascript
// Good: Clear and readable
const message = `Hello, ${name}!`;

// Bad: Too complex
const complex = `${a ? b ? c : d : e ? f : g}`;

// Better: Break down complex expressions
const value = a ? (b ? c : d) : (e ? f : g);
const result = `Result: ${value}`;
```

### 4.8.2. Security

```javascript
// Dangerous: XSS vulnerability
const userInput = '<script>alert("XSS")</script>';
element.innerHTML = `<div>${userInput}</div>`; // ❌

// Safe: Escape user input
const escaped = escapeHTML(userInput);
element.innerHTML = `<div>${escaped}</div>`; // ✅

// Or use textContent
element.textContent = userInput; // ✅
```

### 4.8.3. Performance

```javascript
// Good: Simple template
const str = `Hello, ${name}!`;

// Bad: Complex computation in template
const bad = `${array.filter(x => x > 10).map(x => x * 2).join(', ')}`;

// Better: Compute separately
const result = array.filter(x => x > 10).map(x => x * 2).join(', ');
const good = `Numbers: ${result}`;
```

## 4.9. Common Mistakes

### 4.9.1. Forgetting ${}

```javascript
const name = 'John';

// Wrong
console.log(`Hello, name!`); // "Hello, name!"

// Correct
console.log(`Hello, ${name}!`); // "Hello, John!"
```

### 4.9.2. Quotes vs Backticks

```javascript
// This is a regular string
const str1 = "Hello, ${name}"; // "${name}" as literal text

// This is a template literal
const str2 = `Hello, ${name}`; // Interpolates name
```

### 4.9.3. Undefined Values

```javascript
const user = { name: 'John' };

console.log(`Age: ${user.age}`); // "Age: undefined"

// Better: Provide default
console.log(`Age: ${user.age || 'N/A'}`); // "Age: N/A"
```

## 4.10. Exercises

### Exercise 1: Convert to Template Literals

```javascript
// Convert these to template literals
var name = 'John';
var age = 30;
var message = 'Hello, ' + name + '. You are ' + age + ' years old.';
```

### Exercise 2: Create HTML Card

```javascript
// Create a function that generates an HTML card
function createCard(product) {
    // product = { name: 'Laptop', price: 999, image: 'url' }
    // Return HTML string
}
```

### Exercise 3: Build Query String

```javascript
// Create a function that builds URL query strings
function toQueryString(params) {
    // params = { search: 'javascript', page: 2 }
    // Return: "search=javascript&page=2"
}
```

---

**Kết luận:** Template literals làm string manipulation dễ dàng hơn với interpolation, multiline, và tagged templates. Luôn cẩn thận với security khi dùng user input.

**Chương tiếp theo:** Destructuring
