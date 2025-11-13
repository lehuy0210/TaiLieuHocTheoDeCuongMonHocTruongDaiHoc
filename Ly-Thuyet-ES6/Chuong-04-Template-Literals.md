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

## 4.10. Advanced Practical Examples

### Example 1: Advanced HTML Template System

```javascript
class TemplateEngine {
    constructor() {
        this.cache = new Map();
    }

    compile(template, data) {
        // Create reusable template function
        const func = new Function('data', `
            with(data) {
                return \`${template}\`;
            }
        `);
        return func(data);
    }

    render(name, template, data) {
        if (!this.cache.has(name)) {
            this.cache.set(name, template);
        }
        return this.compile(this.cache.get(name), data);
    }
}

// Usage
const engine = new TemplateEngine();

const template = `
<div class="user-card">
    <h2>\${name}</h2>
    <p>Email: \${email}</p>
    <p>Role: \${role}</p>
    <div class="stats">
        <span>Posts: \${stats.posts}</span>
        <span>Comments: \${stats.comments}</span>
    </div>
</div>
`;

const html = engine.render('userCard', template, {
    name: 'John Doe',
    email: 'john@example.com',
    role: 'Admin',
    stats: { posts: 42, comments: 128 }
});

console.log(html);
```

### Example 2: Internationalization (i18n) System

```javascript
class I18n {
    constructor(locale = 'en') {
        this.locale = locale;
        this.translations = {
            en: {
                welcome: (name) => `Welcome, ${name}!`,
                items: (count) => `You have ${count} ${count === 1 ? 'item' : 'items'}`,
                orderTotal: (total, currency) => `Total: ${currency}${total.toFixed(2)}`
            },
            vi: {
                welcome: (name) => `Chào mừng, ${name}!`,
                items: (count) => `Bạn có ${count} sản phẩm`,
                orderTotal: (total, currency) => `Tổng: ${total.toFixed(2)}${currency}`
            }
        };
    }

    t(key, ...args) {
        const translation = this.translations[this.locale][key];
        return translation ? translation(...args) : key;
    }

    setLocale(locale) {
        this.locale = locale;
    }
}

// Usage
const i18n = new I18n('en');
console.log(i18n.t('welcome', 'John'));        // "Welcome, John!"
console.log(i18n.t('items', 5));               // "You have 5 items"
console.log(i18n.t('orderTotal', 99.99, '$')); // "Total: $99.99"

i18n.setLocale('vi');
console.log(i18n.t('welcome', 'John'));        // "Chào mừng, John!"
console.log(i18n.t('items', 5));               // "Bạn có 5 sản phẩm"
```

### Example 3: SQL Query Builder with Tagged Templates

```javascript
function sql(strings, ...values) {
    let query = '';
    let params = [];

    strings.forEach((str, i) => {
        query += str;
        if (i < values.length) {
            params.push(values[i]);
            query += `$${params.length}`; // Parameterized query
        }
    });

    return { query, params };
}

// Usage
const userId = 123;
const status = 'active';
const limit = 10;

const { query, params } = sql`
    SELECT * FROM users
    WHERE id = ${userId}
    AND status = ${status}
    ORDER BY created_at DESC
    LIMIT ${limit}
`;

console.log(query);
// "SELECT * FROM users WHERE id = $1 AND status = $2 ORDER BY created_at DESC LIMIT $3"
console.log(params);
// [123, 'active', 10]

// Safe from SQL injection!
```

### Example 4: CSS-in-JS Styled Components

```javascript
function styled(strings, ...values) {
    return function(props) {
        const styles = strings.reduce((result, str, i) => {
            const value = typeof values[i] === 'function'
                ? values[i](props)
                : values[i];
            return result + str + (value || '');
        }, '');

        return styles;
    };
}

// Usage
const Button = styled`
    padding: ${props => props.large ? '15px 30px' : '10px 20px'};
    background: ${props => props.primary ? '#007bff' : '#6c757d'};
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: ${props => props.large ? '18px' : '14px'};

    &:hover {
        opacity: 0.8;
    }
`;

// Generate styles for different button variants
console.log(Button({ primary: true, large: false }));
console.log(Button({ primary: false, large: true }));
```

### Example 5: Markdown to HTML Converter

```javascript
class MarkdownConverter {
    convert(markdown) {
        return markdown
            .split('\n')
            .map(line => this.convertLine(line))
            .join('\n');
    }

    convertLine(line) {
        // Headers
        if (line.startsWith('### ')) {
            return `<h3>${line.slice(4)}</h3>`;
        }
        if (line.startsWith('## ')) {
            return `<h2>${line.slice(3)}</h2>`;
        }
        if (line.startsWith('# ')) {
            return `<h1>${line.slice(2)}</h1>`;
        }

        // Bold and italic
        line = line.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        line = line.replace(/\*(.+?)\*/g, '<em>$1</em>');

        // Links
        line = line.replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2">$1</a>');

        // Code
        line = line.replace(/`(.+?)`/g, '<code>$1</code>');

        return line ? `<p>${line}</p>` : '';
    }

    template(title, content) {
        return `
<!DOCTYPE html>
<html>
<head>
    <title>${title}</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #333; }
        code { background: #f4f4f4; padding: 2px 5px; }
    </style>
</head>
<body>
    ${content}
</body>
</html>
        `;
    }
}

// Usage
const converter = new MarkdownConverter();
const markdown = `
# My Blog Post
## Introduction
This is **bold** and this is *italic*.
Check out [my website](https://example.com).
Here's some \`code\` inline.
`;

const html = converter.convert(markdown);
const fullPage = converter.template('My Blog', html);
console.log(fullPage);
```

### Example 6: Advanced Logger with Formatting

```javascript
class Logger {
    constructor(options = {}) {
        this.prefix = options.prefix || '';
        this.timestamp = options.timestamp !== false;
        this.colors = {
            info: '\x1b[36m',    // Cyan
            warn: '\x1b[33m',    // Yellow
            error: '\x1b[31m',   // Red
            success: '\x1b[32m', // Green
            reset: '\x1b[0m'
        };
    }

    format(level, message, data) {
        const timestamp = this.timestamp
            ? `[${new Date().toISOString()}]`
            : '';
        const prefix = this.prefix ? `[${this.prefix}]` : '';
        const color = this.colors[level] || '';
        const reset = this.colors.reset;

        return `${color}${timestamp}${prefix} ${level.toUpperCase()}: ${message}${reset}`;
    }

    log(level, message, data) {
        const formatted = this.format(level, message, data);
        console.log(formatted, data || '');
    }

    info(message, data) {
        this.log('info', message, data);
    }

    warn(message, data) {
        this.log('warn', message, data);
    }

    error(message, data) {
        this.log('error', message, data);
    }

    success(message, data) {
        this.log('success', message, data);
    }
}

// Usage
const logger = new Logger({ prefix: 'APP', timestamp: true });

logger.info('Application started', { port: 3000 });
logger.warn('Memory usage high', { usage: '85%' });
logger.error('Database connection failed', { host: 'localhost' });
logger.success('User logged in', { userId: 123 });
```

### Example 7: Email Template Builder

```javascript
class EmailBuilder {
    constructor() {
        this.styles = {
            container: 'max-width: 600px; margin: 0 auto; font-family: Arial, sans-serif;',
            header: 'background: #007bff; color: white; padding: 20px; text-align: center;',
            body: 'padding: 20px; background: #f8f9fa;',
            footer: 'padding: 20px; text-align: center; color: #6c757d; font-size: 12px;',
            button: 'background: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px; display: inline-block;'
        };
    }

    build({ subject, header, body, buttonText, buttonUrl, footer }) {
        return `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>${subject}</title>
</head>
<body>
    <div style="${this.styles.container}">
        <div style="${this.styles.header}">
            <h1>${header}</h1>
        </div>
        <div style="${this.styles.body}">
            ${body}
            ${buttonText ? `
                <p style="text-align: center; margin-top: 30px;">
                    <a href="${buttonUrl}" style="${this.styles.button}">
                        ${buttonText}
                    </a>
                </p>
            ` : ''}
        </div>
        <div style="${this.styles.footer}">
            ${footer}
        </div>
    </div>
</body>
</html>
        `.trim();
    }

    welcome(user) {
        return this.build({
            subject: 'Welcome to Our Platform',
            header: `Welcome, ${user.name}!`,
            body: `
                <p>Thank you for signing up for our platform.</p>
                <p>We're excited to have you on board!</p>
                <p>Here are some things you can do to get started:</p>
                <ul>
                    <li>Complete your profile</li>
                    <li>Explore our features</li>
                    <li>Connect with other users</li>
                </ul>
            `,
            buttonText: 'Get Started',
            buttonUrl: `https://example.com/dashboard?user=${user.id}`,
            footer: '© 2024 Our Platform. All rights reserved.'
        });
    }

    orderConfirmation(order) {
        const itemsList = order.items
            .map(item => `<li>${item.name} - $${item.price} x ${item.quantity}</li>`)
            .join('');

        return this.build({
            subject: `Order Confirmation #${order.id}`,
            header: 'Order Confirmed!',
            body: `
                <p>Hi ${order.customerName},</p>
                <p>Thank you for your order!</p>
                <p><strong>Order #${order.id}</strong></p>
                <ul>${itemsList}</ul>
                <p><strong>Total: $${order.total.toFixed(2)}</strong></p>
                <p>Estimated delivery: ${order.deliveryDate}</p>
            `,
            buttonText: 'Track Order',
            buttonUrl: `https://example.com/orders/${order.id}`,
            footer: 'Questions? Contact us at support@example.com'
        });
    }
}

// Usage
const emailBuilder = new EmailBuilder();

const welcomeEmail = emailBuilder.welcome({
    id: 123,
    name: 'John Doe'
});

const orderEmail = emailBuilder.orderConfirmation({
    id: 'ORD-2024-001',
    customerName: 'Jane Smith',
    items: [
        { name: 'Laptop', price: 999, quantity: 1 },
        { name: 'Mouse', price: 29, quantity: 2 }
    ],
    total: 1057,
    deliveryDate: '2024-01-20'
});

console.log(welcomeEmail);
console.log(orderEmail);
```

## 4.11. Real-World Use Cases

### Use Case 1: Dynamic Form Builder

```javascript
class FormBuilder {
    constructor() {
        this.fields = [];
    }

    addField(field) {
        this.fields.push(field);
        return this; // Method chaining
    }

    render() {
        return `
<form class="dynamic-form">
    ${this.fields.map(field => this.renderField(field)).join('\n    ')}
    <button type="submit">Submit</button>
</form>
        `.trim();
    }

    renderField(field) {
        const { type, name, label, required, options, placeholder } = field;

        switch(type) {
            case 'text':
            case 'email':
            case 'password':
                return `
<div class="form-group">
    <label for="${name}">${label}${required ? ' *' : ''}</label>
    <input type="${type}"
           id="${name}"
           name="${name}"
           placeholder="${placeholder || ''}"
           ${required ? 'required' : ''}>
</div>`;

            case 'select':
                return `
<div class="form-group">
    <label for="${name}">${label}${required ? ' *' : ''}</label>
    <select id="${name}" name="${name}" ${required ? 'required' : ''}>
        <option value="">-- Select --</option>
        ${options.map(opt => `<option value="${opt.value}">${opt.label}</option>`).join('\n        ')}
    </select>
</div>`;

            case 'textarea':
                return `
<div class="form-group">
    <label for="${name}">${label}${required ? ' *' : ''}</label>
    <textarea id="${name}"
              name="${name}"
              placeholder="${placeholder || ''}"
              ${required ? 'required' : ''}></textarea>
</div>`;

            case 'checkbox':
                return `
<div class="form-group">
    <label>
        <input type="checkbox" id="${name}" name="${name}" ${required ? 'required' : ''}>
        ${label}
    </label>
</div>`;

            default:
                return '';
        }
    }
}

// Usage
const form = new FormBuilder()
    .addField({
        type: 'text',
        name: 'username',
        label: 'Username',
        placeholder: 'Enter username',
        required: true
    })
    .addField({
        type: 'email',
        name: 'email',
        label: 'Email Address',
        placeholder: 'you@example.com',
        required: true
    })
    .addField({
        type: 'select',
        name: 'country',
        label: 'Country',
        required: true,
        options: [
            { value: 'us', label: 'United States' },
            { value: 'uk', label: 'United Kingdom' },
            { value: 'vn', label: 'Vietnam' }
        ]
    })
    .addField({
        type: 'textarea',
        name: 'bio',
        label: 'Biography',
        placeholder: 'Tell us about yourself'
    })
    .addField({
        type: 'checkbox',
        name: 'terms',
        label: 'I agree to the terms and conditions',
        required: true
    });

console.log(form.render());
```

### Use Case 2: REST API Response Formatter

```javascript
class APIFormatter {
    success(data, message = 'Success') {
        return JSON.stringify({
            status: 'success',
            message,
            data,
            timestamp: new Date().toISOString()
        }, null, 2);
    }

    error(error, statusCode = 500) {
        return JSON.stringify({
            status: 'error',
            statusCode,
            message: error.message,
            stack: process.env.NODE_ENV === 'development' ? error.stack : undefined,
            timestamp: new Date().toISOString()
        }, null, 2);
    }

    paginated(data, page, limit, total) {
        return JSON.stringify({
            status: 'success',
            data,
            pagination: {
                page,
                limit,
                total,
                totalPages: Math.ceil(total / limit),
                hasNext: page * limit < total,
                hasPrev: page > 1
            },
            timestamp: new Date().toISOString()
        }, null, 2);
    }

    formatList(items, options = {}) {
        const { title = 'Items', showCount = true } = options;

        return `
${title}${showCount ? ` (${items.length})` : ''}
${'='.repeat(50)}
${items.map((item, index) => `${index + 1}. ${item}`).join('\n')}
${'='.repeat(50)}
        `.trim();
    }
}

// Usage
const formatter = new APIFormatter();

// Success response
console.log(formatter.success({
    id: 1,
    name: 'John Doe'
}, 'User retrieved successfully'));

// Error response
console.log(formatter.error(new Error('User not found'), 404));

// Paginated response
console.log(formatter.paginated(
    [
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' }
    ],
    1,    // page
    10,   // limit
    25    // total items
));

// List formatting
console.log(formatter.formatList(
    ['Apple', 'Banana', 'Orange'],
    { title: 'Fruits', showCount: true }
));
```

### Use Case 3: Report Generator

```javascript
class ReportGenerator {
    generateSalesReport(data) {
        const { period, totalSales, totalOrders, topProducts, salesByCategory } = data;

        const topProductsTable = topProducts
            .map((p, i) => `| ${i + 1} | ${p.name} | $${p.revenue.toFixed(2)} | ${p.quantity} |`)
            .join('\n');

        const categoryBreakdown = salesByCategory
            .map(c => `  - ${c.name}: $${c.total.toFixed(2)} (${c.percentage}%)`)
            .join('\n');

        return `
SALES REPORT
${'='.repeat(60)}

Period: ${period}
Generated: ${new Date().toLocaleString()}

SUMMARY
${'─'.repeat(60)}
Total Sales:  $${totalSales.toFixed(2)}
Total Orders: ${totalOrders}
Average Order Value: $${(totalSales / totalOrders).toFixed(2)}

TOP PRODUCTS
${'─'.repeat(60)}
| # | Product | Revenue | Qty Sold |
|---|---------|---------|----------|
${topProductsTable}

SALES BY CATEGORY
${'─'.repeat(60)}
${categoryBreakdown}

${'='.repeat(60)}
        `.trim();
    }

    generateUserActivityReport(users) {
        const active = users.filter(u => u.status === 'active').length;
        const inactive = users.filter(u => u.status === 'inactive').length;
        const total = users.length;

        const userList = users
            .slice(0, 10) // Top 10
            .map((u, i) => `${i + 1}. ${u.name} - Last login: ${u.lastLogin} (${u.actions} actions)`)
            .join('\n');

        return `
USER ACTIVITY REPORT
${'='.repeat(60)}

OVERVIEW
${'─'.repeat(60)}
Total Users: ${total}
Active Users: ${active} (${((active/total)*100).toFixed(1)}%)
Inactive Users: ${inactive} (${((inactive/total)*100).toFixed(1)}%)

MOST ACTIVE USERS (Top 10)
${'─'.repeat(60)}
${userList}

${'='.repeat(60)}
Generated: ${new Date().toLocaleString()}
        `.trim();
    }
}

// Usage
const reportGen = new ReportGenerator();

const salesReport = reportGen.generateSalesReport({
    period: 'January 2024',
    totalSales: 125750.50,
    totalOrders: 342,
    topProducts: [
        { name: 'Laptop Pro', revenue: 45000, quantity: 45 },
        { name: 'Wireless Mouse', revenue: 8500, quantity: 340 },
        { name: 'USB-C Cable', revenue: 3400, quantity: 680 }
    ],
    salesByCategory: [
        { name: 'Electronics', total: 95000, percentage: 75.5 },
        { name: 'Accessories', total: 20750.50, percentage: 16.5 },
        { name: 'Software', total: 10000, percentage: 8.0 }
    ]
});

console.log(salesReport);
```

### Use Case 4: Code Generator

```javascript
class CodeGenerator {
    generateReactComponent(name, props = []) {
        const propsInterface = props.length > 0
            ? `interface ${name}Props {\n  ${props.map(p => `${p.name}: ${p.type};`).join('\n  ')}\n}\n\n`
            : '';

        const propsParam = props.length > 0 ? `{ ${props.map(p => p.name).join(', ')} }: ${name}Props` : '';

        return `
import React from 'react';

${propsInterface}const ${name}: React.FC${props.length > 0 ? `<${name}Props>` : ''} = (${propsParam}) => {
  return (
    <div className="${name.toLowerCase()}">
      <h2>${name}</h2>
      ${props.map(p => `<p>{${p.name}}</p>`).join('\n      ')}
    </div>
  );
};

export default ${name};
        `.trim();
    }

    generateRESTController(modelName) {
        const lower = modelName.toLowerCase();
        const plural = lower + 's';

        return `
const ${modelName} = require('../models/${modelName}');

class ${modelName}Controller {
  // GET /${plural}
  async getAll(req, res) {
    try {
      const ${plural} = await ${modelName}.find();
      res.json({
        success: true,
        data: ${plural}
      });
    } catch (error) {
      res.status(500).json({
        success: false,
        message: error.message
      });
    }
  }

  // GET /${plural}/:id
  async getById(req, res) {
    try {
      const ${lower} = await ${modelName}.findById(req.params.id);
      if (!${lower}) {
        return res.status(404).json({
          success: false,
          message: '${modelName} not found'
        });
      }
      res.json({
        success: true,
        data: ${lower}
      });
    } catch (error) {
      res.status(500).json({
        success: false,
        message: error.message
      });
    }
  }

  // POST /${plural}
  async create(req, res) {
    try {
      const ${lower} = await ${modelName}.create(req.body);
      res.status(201).json({
        success: true,
        data: ${lower}
      });
    } catch (error) {
      res.status(400).json({
        success: false,
        message: error.message
      });
    }
  }

  // PUT /${plural}/:id
  async update(req, res) {
    try {
      const ${lower} = await ${modelName}.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true, runValidators: true }
      );
      if (!${lower}) {
        return res.status(404).json({
          success: false,
          message: '${modelName} not found'
        });
      }
      res.json({
        success: true,
        data: ${lower}
      });
    } catch (error) {
      res.status(400).json({
        success: false,
        message: error.message
      });
    }
  }

  // DELETE /${plural}/:id
  async delete(req, res) {
    try {
      const ${lower} = await ${modelName}.findByIdAndDelete(req.params.id);
      if (!${lower}) {
        return res.status(404).json({
          success: false,
          message: '${modelName} not found'
        });
      }
      res.json({
        success: true,
        message: '${modelName} deleted successfully'
      });
    } catch (error) {
      res.status(500).json({
        success: false,
        message: error.message
      });
    }
  }
}

module.exports = new ${modelName}Controller();
        `.trim();
    }
}

// Usage
const codeGen = new CodeGenerator();

// Generate React component
const component = codeGen.generateReactComponent('UserCard', [
    { name: 'name', type: 'string' },
    { name: 'email', type: 'string' },
    { name: 'age', type: 'number' }
]);
console.log(component);

// Generate REST controller
const controller = codeGen.generateRESTController('Product');
console.log(controller);
```

### Use Case 5: Configuration File Generator

```javascript
class ConfigGenerator {
    generateDockerCompose(services) {
        const servicesYaml = services.map(service => `
  ${service.name}:
    image: ${service.image}
    ${service.ports ? `ports:\n      - "${service.ports}"` : ''}
    ${service.environment ? `environment:\n${Object.entries(service.environment).map(([k, v]) => `      - ${k}=${v}`).join('\n')}` : ''}
    ${service.volumes ? `volumes:\n${service.volumes.map(v => `      - ${v}`).join('\n')}` : ''}
    ${service.depends_on ? `depends_on:\n${service.depends_on.map(d => `      - ${d}`).join('\n')}` : ''}
        `.trim()).join('\n\n');

        return `
version: '3.8'

services:
${servicesYaml}

networks:
  default:
    driver: bridge
        `.trim();
    }

    generatePackageJson(config) {
        const { name, version, description, author, dependencies, devDependencies, scripts } = config;

        return JSON.stringify({
            name,
            version,
            description,
            author,
            main: 'index.js',
            scripts: scripts || {
                start: 'node index.js',
                dev: 'nodemon index.js',
                test: 'jest'
            },
            dependencies: dependencies || {},
            devDependencies: devDependencies || {}
        }, null, 2);
    }

    generateEnvFile(variables) {
        return Object.entries(variables)
            .map(([key, value]) => {
                // Add comments for sections
                if (typeof value === 'object' && value.comment) {
                    return `# ${value.comment}\n${key}=${value.value}`;
                }
                return `${key}=${value}`;
            })
            .join('\n\n');
    }
}

// Usage
const configGen = new ConfigGenerator();

// Docker Compose
const dockerCompose = configGen.generateDockerCompose([
    {
        name: 'web',
        image: 'nginx:alpine',
        ports: '80:80',
        volumes: ['./html:/usr/share/nginx/html']
    },
    {
        name: 'api',
        image: 'node:18',
        ports: '3000:3000',
        environment: {
            NODE_ENV: 'production',
            PORT: '3000'
        },
        depends_on: ['db']
    },
    {
        name: 'db',
        image: 'postgres:15',
        environment: {
            POSTGRES_USER: 'admin',
            POSTGRES_PASSWORD: 'secret',
            POSTGRES_DB: 'myapp'
        },
        volumes: ['db_data:/var/lib/postgresql/data']
    }
]);
console.log(dockerCompose);

// .env file
const envFile = configGen.generateEnvFile({
    NODE_ENV: 'production',
    PORT: '3000',
    DATABASE_URL: {
        comment: 'Database Configuration',
        value: 'postgresql://user:pass@localhost:5432/db'
    },
    JWT_SECRET: {
        comment: 'Security',
        value: 'your-secret-key'
    }
});
console.log(envFile);
```

## 4.12. Tips & Tricks

### Tip 1: Multi-line Strings Without Extra Whitespace

```javascript
// Problem: Indentation creates unwanted whitespace
const html = `
    <div>
        <h1>Title</h1>
    </div>
`; // Has leading spaces

// Solution 1: Use trim()
const html = `
    <div>
        <h1>Title</h1>
    </div>
`.trim();

// Solution 2: Start from margin
const html = `
<div>
    <h1>Title</h1>
</div>
`.trim();

// Solution 3: Custom dedent function
function dedent(strings, ...values) {
    let result = strings[0];
    values.forEach((value, i) => {
        result += value + strings[i + 1];
    });

    // Remove common leading whitespace
    const lines = result.split('\n');
    const minIndent = Math.min(
        ...lines
            .filter(line => line.trim())
            .map(line => line.match(/^\s*/)[0].length)
    );

    return lines
        .map(line => line.slice(minIndent))
        .join('\n')
        .trim();
}

const html = dedent`
    <div>
        <h1>Title</h1>
    </div>
`;
```

### Tip 2: Conditional Content with Short-Circuit

```javascript
const user = { name: 'John', isAdmin: true, notifications: 5 };

// Using ternary
const message = `
    Hello, ${user.name}!
    ${user.isAdmin ? 'Admin Panel Available' : ''}
    ${user.notifications ? `You have ${user.notifications} notifications` : ''}
`;

// Using logical AND (cleaner)
const message = `
    Hello, ${user.name}!
    ${user.isAdmin && 'Admin Panel Available'}
    ${user.notifications && `You have ${user.notifications} notifications`}
`;
```

### Tip 3: Dynamic Tag Names

```javascript
function createElement(tag, attributes, content) {
    const attrs = Object.entries(attributes)
        .map(([key, value]) => `${key}="${value}"`)
        .join(' ');

    return `<${tag}${attrs ? ' ' + attrs : ''}>${content}</${tag}>`;
}

// Usage
console.log(createElement('div', { class: 'container', id: 'main' }, 'Content'));
// <div class="container" id="main">Content</div>

console.log(createElement('button', { type: 'submit', disabled: 'true' }, 'Submit'));
// <button type="submit" disabled="true">Submit</button>
```

### Tip 4: Number Formatting in Templates

```javascript
function formatNumber(num, decimals = 0) {
    return num.toFixed(decimals).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

const price = 1234567.89;
const discount = 0.15;

const message = `
    Price: $${formatNumber(price, 2)}
    Discount: ${(discount * 100).toFixed(0)}%
    You Save: $${formatNumber(price * discount, 2)}
    Final Price: $${formatNumber(price * (1 - discount), 2)}
`;

console.log(message);
// Price: $1,234,567.89
// Discount: 15%
// You Save: $185,185.18
// Final Price: $1,049,382.71
```

### Tip 5: Escaping Backticks in Templates

```javascript
// To include a backtick, use backslash
const code = `
function example() {
    const str = \`template literal\`;
    return str;
}
`;

console.log(code);

// Or use String.raw for raw strings
const raw = String.raw`This is a \n new line (not interpreted)`;
console.log(raw); // "This is a \n new line (not interpreted)"
```

### Tip 6: Reusable Templates with Functions

```javascript
// Template factory
const createListTemplate = (className) => (items) => `
<ul class="${className}">
    ${items.map(item => `<li>${item}</li>`).join('\n    ')}
</ul>
`;

// Create specialized templates
const todoList = createListTemplate('todo-list');
const shoppingList = createListTemplate('shopping-list');

console.log(todoList(['Buy milk', 'Clean house']));
console.log(shoppingList(['Apples', 'Bread', 'Cheese']));
```

### Tip 7: Tagged Templates for Type Safety

```javascript
function typedTemplate(strings, ...values) {
    return strings.reduce((result, str, i) => {
        let value = values[i];

        if (value !== undefined) {
            // Type checking
            if (typeof value === 'number' && !isFinite(value)) {
                throw new Error('Invalid number');
            }
            if (typeof value === 'string' && value.length === 0) {
                value = '[empty]';
            }
        }

        return result + str + (value !== undefined ? value : '');
    }, '');
}

// Usage
try {
    console.log(typedTemplate`Value: ${123}`);        // OK
    console.log(typedTemplate`Value: ${'hello'}`);    // OK
    console.log(typedTemplate`Value: ${''}`);         // "[empty]"
    console.log(typedTemplate`Value: ${NaN}`);        // Error!
} catch (error) {
    console.error(error.message);
}
```

### Tip 8: Performance with Large Templates

```javascript
// Slow: String concatenation in loop
let html = '';
for (let i = 0; i < 10000; i++) {
    html += `<div>${i}</div>`;
}

// Faster: Array join
const parts = [];
for (let i = 0; i < 10000; i++) {
    parts.push(`<div>${i}</div>`);
}
const html = parts.join('');

// Fastest: Template with map
const html = `
<div>
    ${Array.from({ length: 10000 }, (_, i) => `<div>${i}</div>`).join('')}
</div>
`;
```

### Tip 9: Debug Helper with Tagged Template

```javascript
function debug(strings, ...values) {
    console.group('Debug Info');

    strings.forEach((str, i) => {
        if (str.trim()) {
            console.log(str.trim());
        }
        if (i < values.length) {
            console.log('Value:', values[i]);
            console.log('Type:', typeof values[i]);
        }
    });

    console.groupEnd();

    // Return normal template result
    return strings.reduce((result, str, i) => {
        return result + str + (values[i] !== undefined ? values[i] : '');
    }, '');
}

// Usage
const name = 'John';
const age = 30;
const result = debug`User ${name} is ${age} years old`;
// Logs detailed debug info
console.log(result); // "User John is 30 years old"
```

### Tip 10: Template Caching for Performance

```javascript
class TemplateCache {
    constructor() {
        this.cache = new Map();
    }

    compile(name, template) {
        if (!this.cache.has(name)) {
            // Cache the template function
            this.cache.set(name, (data) => {
                return template.replace(/\$\{(\w+)\}/g, (match, key) => {
                    return data[key] || '';
                });
            });
        }
        return this.cache.get(name);
    }

    render(name, template, data) {
        const compiled = this.compile(name, template);
        return compiled(data);
    }
}

// Usage
const cache = new TemplateCache();

const userTemplate = '<div>${name} - ${email}</div>';

// First call: compiles and caches
console.log(cache.render('user', userTemplate, {
    name: 'John',
    email: 'john@example.com'
}));

// Subsequent calls: uses cached version (faster)
console.log(cache.render('user', userTemplate, {
    name: 'Jane',
    email: 'jane@example.com'
}));
```

## 4.13. Common Mistakes

### Mistake 1: Forgetting to Escape HTML

```javascript
// DANGEROUS: XSS vulnerability
const userInput = '<script>alert("XSS")</script>';
element.innerHTML = `<div>${userInput}</div>`; // ❌

// SAFE: Escape HTML
function escapeHTML(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

element.innerHTML = `<div>${escapeHTML(userInput)}</div>`; // ✅

// SAFEST: Use textContent
element.textContent = userInput; // ✅
```

### Mistake 2: Not Handling undefined/null Values

```javascript
const user = { name: 'John' };

// Bad: Shows "undefined"
console.log(`Age: ${user.age}`); // "Age: undefined" ❌

// Good: Provide defaults
console.log(`Age: ${user.age || 'N/A'}`);        // "Age: N/A" ✅
console.log(`Age: ${user.age ?? 'Unknown'}`);    // "Age: Unknown" ✅
```

### Mistake 3: Excessive Nesting

```javascript
// Bad: Hard to read
const html = `
<div>
    ${items.map(item => `
        <div>
            ${item.tags.map(tag => `
                <span>${tag}</span>
            `).join('')}
        </div>
    `).join('')}
</div>
`; // ❌

// Good: Break into functions
const renderTag = (tag) => `<span>${tag}</span>`;
const renderTags = (tags) => tags.map(renderTag).join('');
const renderItem = (item) => `<div>${renderTags(item.tags)}</div>`;

const html = `
<div>
    ${items.map(renderItem).join('')}
</div>
`; // ✅
```

### Mistake 4: Ignoring Whitespace

```javascript
// Unexpected whitespace
const list = `
    <ul>
        ${items.map(item => `
            <li>${item}</li>
        `).join('')}
    </ul>
`; // Has extra newlines ❌

// Clean whitespace
const list = `
<ul>
    ${items.map(item => `<li>${item}</li>`).join('\n    ')}
</ul>
`.trim(); // ✅
```

### Mistake 5: Performance Issues with Large Data

```javascript
// Bad: Creating huge strings in memory
const hugeHTML = `
<div>
    ${Array.from({ length: 100000 }, (_, i) => `<div>${i}</div>`).join('')}
</div>
`; // ❌ Can cause memory issues

// Better: Stream or paginate
function* generateHTML(count) {
    yield '<div>';
    for (let i = 0; i < count; i++) {
        yield `<div>${i}</div>`;
    }
    yield '</div>';
}

// Or use virtual scrolling in UI
```

### Mistake 6: SQL Injection

```javascript
// DANGEROUS: SQL injection vulnerability
const userId = "1 OR 1=1";
const query = `SELECT * FROM users WHERE id = ${userId}`; // ❌
// Results in: "SELECT * FROM users WHERE id = 1 OR 1=1"

// SAFE: Use parameterized queries
const query = 'SELECT * FROM users WHERE id = ?';
db.query(query, [userId]); // ✅

// Or tagged template for escaping
function sql(strings, ...values) {
    // Properly escape and parameterize
    let query = strings[0];
    const params = [];

    values.forEach((value, i) => {
        params.push(value);
        query += `$${params.length}` + strings[i + 1];
    });

    return { query, params };
}

const { query, params } = sql`SELECT * FROM users WHERE id = ${userId}`;
// query: "SELECT * FROM users WHERE id = $1"
// params: ["1 OR 1=1"]
```

### Mistake 7: Not Trimming Multiline Strings

```javascript
// Unexpected leading/trailing newlines
const html = `
<div>
    <p>Content</p>
</div>
`;

console.log(html.length); // Includes leading/trailing newlines ❌

// Always trim when needed
const html = `
<div>
    <p>Content</p>
</div>
`.trim(); // ✅
```

### Mistake 8: Confusing Backticks with Quotes

```javascript
// Not interpolated (single/double quotes)
console.log("Value: ${value}"); // "Value: ${value}" ❌
console.log('Value: ${value}'); // "Value: ${value}" ❌

// Interpolated (backticks)
console.log(`Value: ${value}`); // "Value: 42" ✅
```

## 4.14. Troubleshooting

### Issue 1: Template Not Interpolating

```javascript
// Problem: Using wrong quotes
const name = "John";
const msg1 = "Hello, ${name}";  // "Hello, ${name}"
const msg2 = 'Hello, ${name}';  // "Hello, ${name}"

// Solution: Use backticks
const msg3 = `Hello, ${name}`;  // "Hello, John" ✅
```

### Issue 2: Unexpected Whitespace

```javascript
// Problem: Template has unwanted whitespace
const html = `
    <div>
        <p>Text</p>
    </div>
`;
// Includes leading spaces and newlines

// Solution 1: Use trim()
const html = `
    <div>
        <p>Text</p>
    </div>
`.trim();

// Solution 2: Custom dedent function (see Tip 1)

// Solution 3: Start from left margin
const html = `
<div>
    <p>Text</p>
</div>
`.trim();
```

### Issue 3: Expression Errors

```javascript
// Problem: Complex expressions breaking
const data = null;
const msg = `Value: ${data.property}`; // TypeError: Cannot read property 'property' of null

// Solution 1: Optional chaining
const msg = `Value: ${data?.property ?? 'N/A'}`; // "Value: N/A" ✅

// Solution 2: Guard clause
const msg = `Value: ${data ? data.property : 'N/A'}`;

// Solution 3: Try-catch for complex expressions
function safeGet(fn, defaultValue = 'N/A') {
    try {
        return fn();
    } catch {
        return defaultValue;
    }
}

const msg = `Value: ${safeGet(() => data.nested.deep.property)}`;
```

### Issue 4: Performance with Large Templates

```javascript
// Problem: Creating huge strings is slow
const items = Array.from({ length: 10000 }, (_, i) => ({ id: i, name: `Item ${i}` }));

console.time('template');
const html = `
<ul>
    ${items.map(item => `<li>${item.id}: ${item.name}</li>`).join('')}
</ul>
`;
console.timeEnd('template'); // Slow

// Solution 1: Use array join instead of repeated concatenation
console.time('optimized');
const parts = ['<ul>'];
for (const item of items) {
    parts.push(`<li>${item.id}: ${item.name}</li>`);
}
parts.push('</ul>');
const html = parts.join('');
console.timeEnd('optimized'); // Faster

// Solution 2: Use DocumentFragment for DOM manipulation
const fragment = document.createDocumentFragment();
items.forEach(item => {
    const li = document.createElement('li');
    li.textContent = `${item.id}: ${item.name}`;
    fragment.appendChild(li);
});
document.querySelector('ul').appendChild(fragment);
```

### Issue 5: Tagged Template Function Errors

```javascript
// Problem: Misunderstanding strings and values arrays
function tag(strings, ...values) {
    console.log(strings);  // Array of string parts
    console.log(values);   // Array of interpolated values
}

const name = 'John';
const age = 30;
tag`Hello ${name}, you are ${age}!`;
// strings: ['Hello ', ', you are ', '!']
// values: ['John', 30]

// Solution: Remember strings.length = values.length + 1
function tag(strings, ...values) {
    let result = '';
    for (let i = 0; i < values.length; i++) {
        result += strings[i] + values[i];
    }
    result += strings[strings.length - 1]; // Don't forget last string!
    return result;
}

// Or use reduce
function tag(strings, ...values) {
    return strings.reduce((result, str, i) => {
        return result + str + (values[i] || '');
    }, '');
}
```

### Issue 6: Memory Leaks with Cached Templates

```javascript
// Problem: Cache grows indefinitely
class TemplateCache {
    constructor() {
        this.cache = new Map();
    }

    compile(template) {
        if (!this.cache.has(template)) {
            this.cache.set(template, /* compiled template */);
        }
        return this.cache.get(template);
    }
}
// ❌ Cache never cleared, memory leak!

// Solution: Implement cache eviction
class TemplateCache {
    constructor(maxSize = 100) {
        this.cache = new Map();
        this.maxSize = maxSize;
    }

    compile(template) {
        if (!this.cache.has(template)) {
            // Evict oldest if cache is full
            if (this.cache.size >= this.maxSize) {
                const firstKey = this.cache.keys().next().value;
                this.cache.delete(firstKey);
            }

            this.cache.set(template, /* compiled template */);
        }

        return this.cache.get(template);
    }

    clear() {
        this.cache.clear();
    }
}
```

## 4.15. Advanced Topics

### Advanced Topic 1: Custom DSL with Tagged Templates

```javascript
// Create a mini query language
function query(strings, ...values) {
    const sql = {
        text: '',
        params: []
    };

    strings.forEach((str, i) => {
        sql.text += str;

        if (i < values.length) {
            const value = values[i];

            if (Array.isArray(value)) {
                // Handle IN clauses
                const placeholders = value.map((_, idx) => {
                    sql.params.push(value[idx]);
                    return `$${sql.params.length}`;
                }).join(', ');
                sql.text += `(${placeholders})`;
            } else if (typeof value === 'object' && value !== null) {
                // Handle WHERE conditions object
                const conditions = Object.entries(value).map(([key, val]) => {
                    sql.params.push(val);
                    return `${key} = $${sql.params.length}`;
                }).join(' AND ');
                sql.text += conditions;
            } else {
                // Regular parameter
                sql.params.push(value);
                sql.text += `$${sql.params.length}`;
            }
        }
    });

    return sql;
}

// Usage
const ids = [1, 2, 3];
const filters = { status: 'active', type: 'user' };

const { text, params } = query`
    SELECT * FROM users
    WHERE id IN ${ids}
    AND ${filters}
    ORDER BY created_at DESC
`;

console.log(text);
// SELECT * FROM users WHERE id IN ($1, $2, $3) AND status = $4 AND type = $5 ORDER BY created_at DESC

console.log(params);
// [1, 2, 3, 'active', 'user']
```

### Advanced Topic 2: Template Literals with Proxies

```javascript
// Create a template system with automatic escaping
const html = new Proxy({}, {
    get(target, tag) {
        return function(strings, ...values) {
            const content = strings.reduce((result, str, i) => {
                let value = values[i];

                if (value !== undefined) {
                    // Auto-escape HTML
                    value = String(value)
                        .replace(/&/g, '&amp;')
                        .replace(/</g, '&lt;')
                        .replace(/>/g, '&gt;')
                        .replace(/"/g, '&quot;')
                        .replace(/'/g, '&#39;');
                }

                return result + str + (value || '');
            }, '');

            return `<${tag}>${content}</${tag}>`;
        };
    }
});

// Usage: Automatic tag names and escaping
const userInput = '<script>alert("XSS")</script>';
const element = html.div`User said: ${userInput}`;
// <div>User said: &lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;</div>

const heading = html.h1`Welcome to ${userInput}`;
// <h1>Welcome to &lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;</h1>
```

### Advanced Topic 3: Asynchronous Template Rendering

```javascript
class AsyncTemplateRenderer {
    async render(template, data) {
        // Find all async placeholders: ${async:key}
        const asyncPattern = /\$\{async:(\w+)\}/g;
        const promises = [];
        const keys = [];

        let match;
        while ((match = asyncPattern.exec(template)) !== null) {
            keys.push(match[1]);
            promises.push(data[match[1]]);
        }

        // Await all async operations
        const results = await Promise.all(promises);

        // Replace placeholders with results
        let rendered = template;
        keys.forEach((key, i) => {
            rendered = rendered.replace(`\${async:${key}}`, results[i]);
        });

        return rendered;
    }
}

// Usage
const renderer = new AsyncTemplateRenderer();

const template = `
<div>
    <h1>User Profile</h1>
    <p>Name: \${async:userName}</p>
    <p>Email: \${async:userEmail}</p>
    <p>Posts: \${async:postCount}</p>
</div>
`;

const data = {
    userName: fetch('/api/user/name').then(r => r.text()),
    userEmail: fetch('/api/user/email').then(r => r.text()),
    postCount: fetch('/api/user/posts/count').then(r => r.text())
};

renderer.render(template, data).then(html => {
    console.log(html);
});
```

### Advanced Topic 4: Template Composition

```javascript
class TemplateComposer {
    constructor() {
        this.partials = new Map();
    }

    register(name, template) {
        this.partials.set(name, template);
    }

    compose(template, data) {
        // Replace {{> partialName}} with partial content
        let result = template;

        const partialPattern = /\{\{>\s*(\w+)\s*\}\}/g;
        let match;

        while ((match = partialPattern.exec(template)) !== null) {
            const partialName = match[1];
            const partial = this.partials.get(partialName);

            if (partial) {
                // Recursively compose nested partials
                const composed = this.compose(partial, data);
                result = result.replace(match[0], composed);
            }
        }

        // Interpolate variables: {{variableName}}
        result = result.replace(/\{\{(\w+)\}\}/g, (match, key) => {
            return data[key] !== undefined ? data[key] : match;
        });

        return result;
    }
}

// Usage
const composer = new TemplateComposer();

// Register partials
composer.register('header', `
<header>
    <h1>{{title}}</h1>
    <nav>{{> navigation}}</nav>
</header>
`);

composer.register('navigation', `
<ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
</ul>
`);

composer.register('footer', `
<footer>
    <p>&copy; {{year}} {{company}}</p>
</footer>
`);

// Compose full page
const page = composer.compose(`
<!DOCTYPE html>
<html>
<head>
    <title>{{title}}</title>
</head>
<body>
    {{> header}}
    <main>{{content}}</main>
    {{> footer}}
</body>
</html>
`, {
    title: 'My Website',
    content: 'Welcome to my site!',
    year: 2024,
    company: 'ACME Inc.'
});

console.log(page);
```

### Advanced Topic 5: Template Literals with Localization

```javascript
class LocalizedTemplate {
    constructor(locale = 'en') {
        this.locale = locale;
        this.translations = new Map();
        this.formatters = {
            en: {
                date: (date) => date.toLocaleDateString('en-US'),
                currency: (amount) => `$${amount.toFixed(2)}`,
                number: (num) => num.toLocaleString('en-US')
            },
            vi: {
                date: (date) => date.toLocaleDateString('vi-VN'),
                currency: (amount) => `${amount.toFixed(0)}đ`,
                number: (num) => num.toLocaleString('vi-VN')
            }
        };
    }

    addTranslation(locale, key, value) {
        if (!this.translations.has(locale)) {
            this.translations.set(locale, new Map());
        }
        this.translations.get(locale).set(key, value);
    }

    t(key) {
        const translations = this.translations.get(this.locale);
        return translations ? translations.get(key) || key : key;
    }

    format(type, value) {
        const formatter = this.formatters[this.locale][type];
        return formatter ? formatter(value) : value;
    }

    render(strings, ...values) {
        return strings.reduce((result, str, i) => {
            let value = values[i];

            if (value && typeof value === 'object') {
                if (value.type === 'translate') {
                    value = this.t(value.key);
                } else if (value.type === 'format') {
                    value = this.format(value.format, value.value);
                }
            }

            return result + str + (value !== undefined ? value : '');
        }, '');
    }
}

// Usage
const template = new LocalizedTemplate('en');

template.addTranslation('en', 'welcome', 'Welcome');
template.addTranslation('en', 'total', 'Total');
template.addTranslation('vi', 'welcome', 'Chào mừng');
template.addTranslation('vi', 'total', 'Tổng');

const message = template.render`
    ${{ type: 'translate', key: 'welcome' }}, John!
    ${{ type: 'translate', key: 'total' }}: ${{ type: 'format', format: 'currency', value: 1234.56 }}
    Date: ${{ type: 'format', format: 'date', value: new Date() }}
`;

console.log(message);
// English: "Welcome, John! Total: $1234.56 Date: 1/15/2024"

template.locale = 'vi';
console.log(template.render`
    ${{ type: 'translate', key: 'welcome' }}, John!
    ${{ type: 'translate', key: 'total' }}: ${{ type: 'format', format: 'currency', value: 1234.56 }}
`);
// Vietnamese: "Chào mừng, John! Tổng: 1235đ"
```

## 4.16. Exercises (Extended)

### Exercise 1: Convert to Template Literals

```javascript
// Convert these ES5 strings to ES6 template literals
var name = 'John';
var age = 30;
var city = 'NYC';
var message = 'Hello, ' + name + '. You are ' + age + ' years old and live in ' + city + '.';

// Your solution:
// const message = ?
```

### Exercise 2: Create HTML Card Generator

```javascript
// Create a function that generates product cards
function createProductCard(product) {
    // product = {
    //   name: 'Laptop',
    //   price: 999,
    //   image: 'laptop.jpg',
    //   rating: 4.5,
    //   inStock: true
    // }
    // Return HTML string with proper structure
}

// Test:
// console.log(createProductCard({
//     name: 'MacBook Pro',
//     price: 1999,
//     image: 'macbook.jpg',
//     rating: 4.8,
//     inStock: true
// }));
```

### Exercise 3: Build Query String Builder

```javascript
// Create a function that builds URL query strings
function buildQueryString(params) {
    // params = { search: 'javascript', page: 2, sort: 'date', order: 'desc' }
    // Return: "search=javascript&page=2&sort=date&order=desc"
    // Handle encoding and null/undefined values
}

// Test:
// console.log(buildQueryString({ q: 'hello world', page: 1 }));
// Expected: "q=hello%20world&page=1"
```

### Exercise 4: Create Tagged Template for HTML Escaping

```javascript
// Implement an escapeHTML tagged template
function escapeHTML(strings, ...values) {
    // Escape HTML entities in values
    // Your code here
}

// Test:
// const userInput = '<script>alert("XSS")</script>';
// const safe = escapeHTML`<div>${userInput}</div>`;
// console.log(safe);
// Expected: "<div>&lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;</div>"
```

### Exercise 5: Multiline Email Template

```javascript
// Create an email template function
function createWelcomeEmail(user) {
    // user = { name: 'John', email: 'john@example.com', activationLink: 'https://...' }
    // Return formatted email with:
    // - Greeting
    // - Welcome message
    // - Activation link
    // - Footer
}

// Test your function
```

### Exercise 6: Table Formatter

```javascript
// Create a function that formats arrays as ASCII tables
function formatTable(data, headers) {
    // data = [
    //   { id: 1, name: 'John', age: 30 },
    //   { id: 2, name: 'Jane', age: 25 }
    // ]
    // headers = ['ID', 'Name', 'Age']
    // Return:
    // | ID | Name | Age |
    // |----|------|-----|
    // | 1  | John | 30  |
    // | 2  | Jane | 25  |
}
```

### Exercise 7: SQL Query Builder

```javascript
// Create a safe SQL query builder using tagged templates
function sql(strings, ...values) {
    // Build parameterized query
    // Return { query: string, params: array }
}

// Test:
// const userId = 123;
// const status = 'active';
// const result = sql`SELECT * FROM users WHERE id = ${userId} AND status = ${status}`;
// console.log(result);
// Expected: { query: "SELECT * FROM users WHERE id = $1 AND status = $2", params: [123, 'active'] }
```

### Exercise 8: Markdown to HTML

```javascript
// Convert markdown to HTML using template literals
function markdownToHTML(markdown) {
    // Support:
    // # Header 1
    // ## Header 2
    // **bold**
    // *italic*
    // [link text](url)
    // `code`
}

// Test:
// const md = `
// # Title
// This is **bold** and *italic*.
// `;
// console.log(markdownToHTML(md));
```

### Exercise 9: CSV Generator

```javascript
// Create a CSV generator from objects
function generateCSV(data) {
    // data = [
    //   { name: 'John', age: 30, city: 'NYC' },
    //   { name: 'Jane', age: 25, city: 'LA' }
    // ]
    // Return:
    // name,age,city
    // John,30,NYC
    // Jane,25,LA
}
```

### Exercise 10: Template with Conditionals

```javascript
// Create a template function that handles conditionals
function renderUserProfile(user) {
    // user = {
    //   name: 'John',
    //   email: 'john@example.com',
    //   isAdmin: true,
    //   avatar: 'avatar.jpg' // might be null
    // }
    // Show admin badge if isAdmin
    // Show default avatar if avatar is null
}
```

### Exercise 11: Internationalization

```javascript
// Create an i18n template system
class I18nTemplate {
    constructor(locale) {
        // Initialize with locale
    }

    t(key) {
        // Return translation for key
    }

    render(template, data) {
        // Render template with translations
    }
}

// Test:
// const i18n = new I18nTemplate('en');
// i18n.addTranslation('en', 'welcome', 'Welcome');
// console.log(i18n.render`${i18n.t('welcome')}, ${'John'}!`);
```

### Exercise 12: Advanced Challenge - Template Engine

```javascript
// Create a full-featured template engine
class TemplateEngine {
    compile(template) {
        // Compile template into reusable function
    }

    render(template, data) {
        // Support:
        // - Variables: {{name}}
        // - Conditionals: {{if condition}} ... {{/if}}
        // - Loops: {{each items}} ... {{/each}}
        // - Partials: {{> partialName}}
    }
}

// Test:
// const engine = new TemplateEngine();
// const template = `
// <ul>
//   {{each users}}
//     <li>{{name}} {{if isAdmin}}(Admin){{/if}}</li>
//   {{/each}}
// </ul>
// `;
// console.log(engine.render(template, {
//     users: [
//         { name: 'John', isAdmin: true },
//         { name: 'Jane', isAdmin: false }
//     ]
// }));
```

---

**Kết luận:** Template literals là công cụ mạnh mẽ cho string manipulation trong ES6. Với interpolation, multiline strings, và tagged templates, chúng giúp code ngắn gọn và dễ bảo trì hơn. Luôn chú ý đến security (XSS), performance, và readability khi sử dụng.

**Chương tiếp theo:** Destructuring
