# CHƯƠNG 2: CSS3 SELECTORS

## 2.1. Basic Selectors

### 2.1.1. Universal Selector

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

### 2.1.2. Type Selector

```css
p {
    color: blue;
}

h1 {
    font-size: 32px;
}
```

### 2.1.3. Class Selector

```css
.button {
    padding: 10px 20px;
    background-color: blue;
}

.button.primary {
    background-color: green;
}
```

### 2.1.4. ID Selector

```css
#header {
    background-color: #333;
}
```

### 2.1.5. Attribute Selector

```css
/* Has attribute */
[disabled] {
    opacity: 0.5;
}

/* Exact value */
[type="text"] {
    border: 1px solid #ccc;
}

/* Contains value */
[class*="btn"] {
    cursor: pointer;
}

/* Starts with */
[href^="https"] {
    color: green;
}

/* Ends with */
[src$=".pdf"] {
    background: url('pdf-icon.png');
}
```

## 2.2. Combinators

### 2.2.1. Descendant Selector

```css
/* All p inside div */
div p {
    color: red;
}
```

### 2.2.2. Child Selector

```css
/* Direct children only */
div > p {
    color: blue;
}
```

### 2.2.3. Adjacent Sibling

```css
/* p immediately after h1 */
h1 + p {
    font-size: 18px;
}
```

### 2.2.4. General Sibling

```css
/* All p after h1 */
h1 ~ p {
    margin-top: 10px;
}
```

## 2.3. Pseudo-classes

### 2.3.1. Link States

```css
a:link { color: blue; }
a:visited { color: purple; }
a:hover { color: red; }
a:active { color: orange; }
```

### 2.3.2. nth-child

```css
/* Odd rows */
tr:nth-child(odd) {
    background-color: #f2f2f2;
}

/* Even rows */
tr:nth-child(even) {
    background-color: white;
}

/* Every 3rd */
li:nth-child(3n) {
    color: red;
}

/* First 3 */
li:nth-child(-n+3) {
    font-weight: bold;
}
```

### 2.3.3. nth-of-type

```css
p:nth-of-type(2) {
    color: blue;
}

p:nth-of-type(2n) {
    background: yellow;
}
```

### 2.3.4. first/last

```css
p:first-child { margin-top: 0; }
p:last-child { margin-bottom: 0; }

p:first-of-type { font-size: 20px; }
p:last-of-type { font-size: 14px; }
```

### 2.3.5. only-child

```css
p:only-child {
    text-align: center;
}

p:only-of-type {
    font-weight: bold;
}
```

### 2.3.6. :not()

```css
/* All buttons except .primary */
button:not(.primary) {
    background-color: gray;
}

/* All inputs except checkbox */
input:not([type="checkbox"]) {
    padding: 5px;
}
```

### 2.3.7. Form States

```css
input:focus {
    border-color: blue;
    outline: none;
}

input:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

input:checked {
    background-color: green;
}

input:valid {
    border-color: green;
}

input:invalid {
    border-color: red;
}

input:required {
    border-left: 3px solid red;
}

input:optional {
    border-left: 3px solid gray;
}
```

### 2.3.8. :empty

```css
div:empty {
    display: none;
}
```

### 2.3.9. :root

```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2ecc71;
}
```

## 2.4. Pseudo-elements

### 2.4.1. ::before and ::after

```css
.quote::before {
    content: '"';
    font-size: 24px;
}

.quote::after {
    content: '"';
    font-size: 24px;
}

/* Icon before */
.icon::before {
    content: '→';
    margin-right: 5px;
}
```

### 2.4.2. ::first-letter

```css
p::first-letter {
    font-size: 32px;
    font-weight: bold;
    color: red;
}
```

### 2.4.3. ::first-line

```css
p::first-line {
    font-weight: bold;
    color: blue;
}
```

### 2.4.4. ::selection

```css
::selection {
    background-color: yellow;
    color: black;
}
```

### 2.4.5. ::placeholder

```css
input::placeholder {
    color: #999;
    font-style: italic;
}
```

## 2.5. Advanced Selectors

### 2.5.1. :is()

```css
/* Old way */
h1, h2, h3, h4, h5, h6 {
    font-family: Arial;
}

/* New way */
:is(h1, h2, h3, h4, h5, h6) {
    font-family: Arial;
}

/* Complex example */
:is(header, main, footer) p {
    margin: 1em 0;
}
```

### 2.5.2. :where()

```css
/* Same as :is() but with 0 specificity */
:where(h1, h2, h3) {
    margin: 0;
}
```

### 2.5.3. :has()

```css
/* Parent selector! */
div:has(> img) {
    border: 2px solid blue;
}

/* Has specific child */
article:has(h2) {
    background: #f0f0f0;
}

/* Does not have */
div:not(:has(p)) {
    padding: 0;
}
```

## 2.6. Practical Examples

### 2.6.1. Striped Table

```css
table tr:nth-child(even) {
    background-color: #f2f2f2;
}

table tr:hover {
    background-color: #e0e0e0;
}
```

### 2.6.2. Custom Checkbox

```css
input[type="checkbox"] {
    display: none;
}

input[type="checkbox"] + label::before {
    content: '';
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 2px solid #333;
    margin-right: 10px;
}

input[type="checkbox"]:checked + label::before {
    background-color: #333;
}
```

### 2.6.3. Clearfix

```css
.clearfix::after {
    content: '';
    display: table;
    clear: both;
}
```

### 2.6.4. Required Fields

```css
input:required::after {
    content: ' *';
    color: red;
}

input:valid {
    border-color: green;
}

input:invalid {
    border-color: red;
}
```

## 2.7. Real-World Examples

### Example 1: Navigation Menu with Active State

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .nav {
            list-style: none;
            display: flex;
            gap: 20px;
            padding: 0;
            background: #2c3e50;
            padding: 15px 30px;
        }

        .nav li a {
            color: white;
            text-decoration: none;
            padding: 10px 15px;
            border-radius: 4px;
            transition: background 0.3s ease;
        }

        .nav li a:hover {
            background: rgba(255, 255, 255, 0.1);
        }

        .nav li a.active {
            background: #3498db;
        }

        /* First menu item */
        .nav li:first-child a {
            font-weight: bold;
        }

        /* Last menu item */
        .nav li:last-child {
            margin-left: auto;
        }
    </style>
</head>
<body>
    <ul class="nav">
        <li><a href="#" class="active">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
        <li><a href="#">Login</a></li>
    </ul>
</body>
</html>
```

### Example 2: Advanced Table Styling

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-family: Arial, sans-serif;
        }

        /* Header styling */
        thead tr {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        th {
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }

        /* First column bold */
        td:first-child {
            font-weight: bold;
            color: #2c3e50;
        }

        /* Striped rows */
        tbody tr:nth-child(odd) {
            background: #f8f9fa;
        }

        tbody tr:nth-child(even) {
            background: white;
        }

        /* Hover effect */
        tbody tr:hover {
            background: #e3f2fd;
            transform: scale(1.01);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        td {
            padding: 12px 15px;
            border-bottom: 1px solid #dee2e6;
        }

        /* Last row no border */
        tbody tr:last-child td {
            border-bottom: none;
        }

        /* Status column (3rd column) */
        td:nth-child(3) {
            text-align: center;
        }

        /* Active status */
        td:nth-child(3):has(.active)::before {
            content: '✓ ';
            color: green;
        }

        /* Inactive status */
        td:nth-child(3):has(.inactive)::before {
            content: '✗ ';
            color: red;
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Status</th>
                <th>Role</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>John Doe</td>
                <td>john@example.com</td>
                <td><span class="active">Active</span></td>
                <td>Admin</td>
            </tr>
            <tr>
                <td>Jane Smith</td>
                <td>jane@example.com</td>
                <td><span class="active">Active</span></td>
                <td>User</td>
            </tr>
            <tr>
                <td>Bob Johnson</td>
                <td>bob@example.com</td>
                <td><span class="inactive">Inactive</span></td>
                <td>User</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```

### Example 3: Custom Form with Validation

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: #333;
        }

        /* Required indicator */
        input:required + label::after,
        label:has(+ input:required)::after {
            content: ' *';
            color: red;
        }

        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            font-size: 16px;
            transition: all 0.3s ease;
        }

        /* Focus state */
        input:focus {
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
        }

        /* Valid state */
        input:valid:not(:placeholder-shown) {
            border-color: #27ae60;
        }

        input:valid:not(:placeholder-shown)::after {
            content: '✓';
        }

        /* Invalid state */
        input:invalid:not(:placeholder-shown) {
            border-color: #e74c3c;
        }

        /* Disabled state */
        input:disabled {
            background: #f5f5f5;
            cursor: not-allowed;
            opacity: 0.6;
        }

        /* Checkbox styling */
        input[type="checkbox"] {
            width: auto;
            margin-right: 8px;
        }

        input[type="checkbox"]:checked {
            accent-color: #3498db;
        }

        /* Different input types */
        input[type="email"]::placeholder {
            color: #999;
            font-style: italic;
        }

        input[type="password"] {
            letter-spacing: 2px;
        }
    </style>
</head>
<body>
    <form>
        <div class="form-group">
            <label>Name</label>
            <input type="text" required placeholder="Enter your name">
        </div>

        <div class="form-group">
            <label>Email</label>
            <input type="email" required placeholder="your@email.com">
        </div>

        <div class="form-group">
            <label>Password</label>
            <input type="password" required placeholder="••••••••">
        </div>

        <div class="form-group">
            <input type="checkbox" id="terms" required>
            <label for="terms">I agree to terms and conditions</label>
        </div>
    </form>
</body>
</html>
```

### Example 4: Card Grid with nth-child Patterns

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .card-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            padding: 20px;
        }

        .card {
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        /* First card special */
        .card:first-child {
            grid-column: span 2;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        /* Every 3rd card */
        .card:nth-child(3n) {
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
        }

        /* Every 3rd card starting from 2nd */
        .card:nth-child(3n+2) {
            background: #f3e5f5;
            border-left: 4px solid #9c27b0;
        }

        /* Last card */
        .card:last-child {
            background: #fff3e0;
            border-left: 4px solid #ff9800;
        }

        /* Hover effect */
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        }

        /* Cards with images */
        .card:has(img) {
            padding: 0;
            overflow: hidden;
        }

        .card:has(img) img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .card:has(img) .card-content {
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="card-grid">
        <div class="card">
            <h3>Featured Card</h3>
            <p>This is a special featured card.</p>
        </div>
        <div class="card">
            <h3>Card 2</h3>
            <p>Regular card content.</p>
        </div>
        <div class="card">
            <h3>Card 3</h3>
            <p>Every 3rd card style.</p>
        </div>
        <div class="card">
            <h3>Card 4</h3>
            <p>Regular card content.</p>
        </div>
        <div class="card">
            <img src="image.jpg" alt="Image">
            <div class="card-content">
                <h3>Card with Image</h3>
                <p>This card has an image.</p>
            </div>
        </div>
    </div>
</body>
</html>
```

### Example 5: Article Typography with Pseudo-elements

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        article {
            max-width: 700px;
            margin: 50px auto;
            font-family: Georgia, serif;
            line-height: 1.8;
        }

        /* Drop cap */
        article p:first-of-type::first-letter {
            font-size: 4em;
            font-weight: bold;
            float: left;
            line-height: 0.9;
            margin: 0.1em 0.1em 0 0;
            color: #667eea;
        }

        /* First line of first paragraph */
        article p:first-of-type::first-line {
            font-variant: small-caps;
            font-weight: bold;
        }

        /* Blockquote styling */
        blockquote {
            position: relative;
            padding: 20px 40px;
            margin: 30px 0;
            font-style: italic;
            background: #f8f9fa;
            border-left: 4px solid #667eea;
        }

        blockquote::before {
            content: '"';
            font-size: 60px;
            position: absolute;
            top: 10px;
            left: 10px;
            color: #667eea;
            opacity: 0.3;
        }

        /* Links with external indicator */
        article a[href^="http"]::after {
            content: ' ↗';
            font-size: 0.8em;
            color: #3498db;
        }

        /* PDF links */
        article a[href$=".pdf"]::before {
            content: '📄 ';
        }

        /* Highlight selected text */
        article::selection {
            background: #667eea;
            color: white;
        }

        /* Headings with decorative lines */
        article h2 {
            position: relative;
            padding-bottom: 10px;
            margin-top: 40px;
        }

        article h2::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 50px;
            height: 3px;
            background: linear-gradient(90deg, #667eea, transparent);
        }

        /* List styling */
        article ul li::marker {
            color: #667eea;
            font-size: 1.2em;
        }

        /* Code blocks */
        article code {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }

        article code::before,
        article code::after {
            content: '`';
            opacity: 0.5;
        }
    </style>
</head>
<body>
    <article>
        <h1>Article Title</h1>
        <p>This is the first paragraph with a drop cap. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>

        <h2>Subheading</h2>
        <p>Regular paragraph with <a href="https://example.com">external link</a> and <a href="document.pdf">PDF link</a>.</p>

        <blockquote>
            This is a beautiful quote that stands out from the rest of the text.
        </blockquote>

        <ul>
            <li>List item one</li>
            <li>List item two</li>
            <li>List item three</li>
        </ul>

        <p>Here's some <code>inline code</code> example.</p>
    </article>
</body>
</html>
```

### Example 6: Advanced Button States

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .button-group {
            display: flex;
            gap: 15px;
            padding: 20px;
        }

        button {
            padding: 12px 24px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
        }

        /* Primary button */
        button:not([disabled]):not(.secondary):not(.danger) {
            background: #3498db;
            color: white;
        }

        button:not([disabled]):not(.secondary):not(.danger):hover {
            background: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
        }

        button:not([disabled]):not(.secondary):not(.danger):active {
            transform: translateY(0);
            box-shadow: 0 2px 4px rgba(52, 152, 219, 0.4);
        }

        /* Secondary button */
        button.secondary {
            background: white;
            color: #3498db;
            border: 2px solid #3498db;
        }

        button.secondary:hover {
            background: #3498db;
            color: white;
        }

        /* Danger button */
        button.danger {
            background: #e74c3c;
            color: white;
        }

        button.danger:hover {
            background: #c0392b;
        }

        /* Disabled button */
        button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            background: #95a5a6;
        }

        /* Loading state */
        button.loading::after {
            content: '';
            position: absolute;
            width: 16px;
            height: 16px;
            top: 50%;
            right: 10px;
            margin-top: -8px;
            border: 2px solid white;
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 0.6s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Focus visible (keyboard navigation) */
        button:focus-visible {
            outline: 3px solid #3498db;
            outline-offset: 2px;
        }

        /* First button in group */
        .button-group button:first-child {
            margin-left: 0;
        }

        /* Last button in group */
        .button-group button:last-child {
            margin-right: 0;
        }
    </style>
</head>
<body>
    <div class="button-group">
        <button>Primary</button>
        <button class="secondary">Secondary</button>
        <button class="danger">Delete</button>
        <button disabled>Disabled</button>
        <button class="loading">Loading</button>
    </div>
</body>
</html>
```

### Example 7: Responsive Image Gallery with nth-child

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .gallery {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            padding: 20px;
        }

        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 8px;
            cursor: pointer;
        }

        /* First item spans 2x2 */
        .gallery-item:first-child {
            grid-column: span 2;
            grid-row: span 2;
        }

        /* Every 5th item (after first) */
        .gallery-item:nth-child(5n+2) {
            grid-column: span 2;
        }

        /* Every 7th item */
        .gallery-item:nth-child(7n) {
            grid-row: span 2;
        }

        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .gallery-item:hover img {
            transform: scale(1.1);
        }

        /* Overlay */
        .gallery-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(
                to bottom,
                transparent 0%,
                rgba(0,0,0,0.7) 100%
            );
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .gallery-item:hover::before {
            opacity: 1;
        }

        /* Title overlay */
        .gallery-item::after {
            content: attr(data-title);
            position: absolute;
            bottom: 20px;
            left: 20px;
            color: white;
            font-size: 18px;
            font-weight: bold;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
        }

        .gallery-item:hover::after {
            opacity: 1;
            transform: translateY(0);
        }

        /* Special styling for items with video */
        .gallery-item:has([data-type="video"])::after {
            content: '▶ ' attr(data-title);
        }
    </style>
</head>
<body>
    <div class="gallery">
        <div class="gallery-item" data-title="Image 1">
            <img src="image1.jpg" alt="Image 1">
        </div>
        <div class="gallery-item" data-title="Image 2">
            <img src="image2.jpg" alt="Image 2">
        </div>
        <div class="gallery-item" data-title="Image 3">
            <img src="image3.jpg" alt="Image 3">
        </div>
        <!-- More items... -->
    </div>
</body>
</html>
```

## 2.8. Tips & Tricks

### Tip 1: Use :is() for Cleaner Code

```css
/* Instead of this: */
header a:hover,
main a:hover,
footer a:hover {
    color: blue;
}

/* Use this: */
:is(header, main, footer) a:hover {
    color: blue;
}
```

### Tip 2: :not() with Multiple Selectors

```css
/* Exclude multiple elements */
button:not(.primary):not(.secondary):not(:disabled) {
    background: gray;
}

/* Or use :not with :is */
button:not(:is(.primary, .secondary, :disabled)) {
    background: gray;
}
```

### Tip 3: Attribute Selectors for Styling by State

```css
/* Style links based on protocol */
a[href^="https"] { color: green; }
a[href^="http://"] { color: orange; }
a[href^="mailto:"] { color: blue; }

/* Style by file type */
a[href$=".pdf"]::after { content: " (PDF)"; }
a[href$=".doc"]::after { content: " (Word)"; }
```

### Tip 4: nth-child Formulas

```css
/* First 3 items */
li:nth-child(-n+3) { color: red; }

/* Last 3 items */
li:nth-last-child(-n+3) { color: blue; }

/* All except first 2 */
li:nth-child(n+3) { margin-top: 10px; }

/* Alternate groups of 3 */
li:nth-child(6n+1),
li:nth-child(6n+2),
li:nth-child(6n+3) {
    background: #f0f0f0;
}
```

### Tip 5: Combine Multiple Pseudo-classes

```css
/* First item on hover */
li:first-child:hover {
    background: yellow;
}

/* Valid and focused input */
input:valid:focus {
    border-color: green;
    box-shadow: 0 0 5px green;
}

/* Not first, not last */
li:not(:first-child):not(:last-child) {
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
}
```

### Tip 6: Use ::before and ::after for Icons

```css
.icon-home::before {
    content: '🏠';
    margin-right: 5px;
}

.icon-email::before {
    content: '✉';
    margin-right: 5px;
}

.external-link::after {
    content: ' ↗';
    font-size: 0.8em;
}
```

### Tip 7: Custom Checkbox/Radio Without Images

```css
/* Hide default */
input[type="checkbox"] {
    appearance: none;
    width: 20px;
    height: 20px;
    border: 2px solid #333;
    border-radius: 3px;
    cursor: pointer;
}

/* Checked state */
input[type="checkbox"]:checked {
    background: #333;
    position: relative;
}

input[type="checkbox"]:checked::after {
    content: '✓';
    position: absolute;
    color: white;
    font-size: 14px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

### Tip 8: Target Empty Elements

```css
/* Hide empty paragraphs */
p:empty {
    display: none;
}

/* Style divs without content */
div:empty {
    min-height: 50px;
    background: #f0f0f0;
}

/* Add message to empty elements */
.list:empty::before {
    content: 'No items to display';
    color: #999;
}
```

### Tip 9: Use :has() for Parent Styling

```css
/* Style form based on validation */
form:has(input:invalid) button {
    opacity: 0.5;
    cursor: not-allowed;
}

/* Card with image vs without */
.card:has(img) {
    padding: 0;
}

.card:not(:has(img)) {
    padding: 20px;
}

/* Container with multiple children */
.container:has(> *:nth-child(3)) {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}
```

### Tip 10: Combinator Chains

```css
/* Select all li that follow the first li */
li:first-child ~ li {
    margin-top: 10px;
}

/* Direct child paragraph after h2 */
article h2 + p {
    font-size: 1.2em;
    color: #666;
}

/* All paragraphs after h2 in article */
article h2 ~ p {
    margin-left: 20px;
}
```

## 2.9. Common Mistakes

### Mistake 1: Confusing :nth-child and :nth-of-type

**Problem:**
```css
/* This doesn't work as expected if div has mixed children */
div p:nth-child(2) {
    color: red;
}
```

**Solution:**
```css
/* Use nth-of-type for specific element types */
div p:nth-of-type(2) {
    color: red;
}
```

### Mistake 2: Overusing Universal Selector

**Problem:**
```css
* {
    border: 1px solid red; /* Affects ALL elements */
}
```

**Solution:**
```css
/* Be more specific */
.debug * {
    border: 1px solid red;
}

/* Or target specific elements */
div, p, span {
    border: 1px solid red;
}
```

### Mistake 3: Forgetting Specificity Rules

**Problem:**
```css
.button {
    background: blue;
}

button {
    background: red; /* This won't override .button */
}
```

**Solution:**
```css
/* Increase specificity or use same specificity */
button.button {
    background: red;
}

/* Or reorder (later rules with same specificity win) */
button {
    background: red;
}

.button {
    background: blue; /* This now overrides */
}
```

### Mistake 4: Misusing :not()

**Problem:**
```css
/* This doesn't work in older browsers */
button:not(.primary, .secondary) {
    background: gray;
}
```

**Solution:**
```css
/* Use multiple :not() for better compatibility */
button:not(.primary):not(.secondary) {
    background: gray;
}
```

### Mistake 5: Incorrect Pseudo-element Syntax

**Problem:**
```css
/* Single colon (old syntax) */
p:before {
    content: 'Hello';
}
```

**Solution:**
```css
/* Use double colon (CSS3 syntax) */
p::before {
    content: 'Hello';
}
```

### Mistake 6: Forgetting content Property

**Problem:**
```css
.element::before {
    color: red; /* Won't show without content */
}
```

**Solution:**
```css
.element::before {
    content: ''; /* Required for ::before/::after */
    color: red;
}
```

### Mistake 7: Adjacent Sibling Issues

**Problem:**
```css
/* Only affects immediate next sibling */
h1 + p {
    font-size: 20px;
}
/* Second p won't be affected */
```

**Solution:**
```css
/* Use general sibling for all following siblings */
h1 ~ p {
    font-size: 20px;
}
```

### Mistake 8: Attribute Selector Case Sensitivity

**Problem:**
```css
/* Won't match class="Button" */
[class="button"] {
    color: red;
}
```

**Solution:**
```css
/* Use case-insensitive flag */
[class="button" i] {
    color: red;
}

/* Or use class selector */
.button {
    color: red;
}
```

### Mistake 9: :hover on Touch Devices

**Problem:**
```css
button:hover {
    background: blue; /* Sticky on touch devices */
}
```

**Solution:**
```css
/* Add active and focus states */
button:hover,
button:active,
button:focus {
    background: blue;
}

/* Or use media query */
@media (hover: hover) {
    button:hover {
        background: blue;
    }
}
```

### Mistake 10: Specificity Wars with ID Selectors

**Problem:**
```css
#header {
    background: blue; /* Very high specificity */
}

.header-dark {
    background: black; /* Won't override */
}
```

**Solution:**
```css
/* Avoid IDs for styling, use classes */
.header {
    background: blue;
}

.header-dark {
    background: black;
}
```

## 2.10. Troubleshooting

### Problem 1: Selector Not Working

**Symptoms:** Styles not applied

**Debugging Steps:**
```css
/* 1. Check selector syntax */
div.class { } /* ✓ Correct */
div .class { } /* ✓ Different (descendant) */
div, .class { } /* ✓ Different (multiple) */

/* 2. Check specificity */
/* Use browser DevTools to see computed styles */

/* 3. Verify element exists */
/* Check HTML structure matches selector */
```

### Problem 2: nth-child Not Working as Expected

**Symptoms:** Wrong elements selected

**Solution:**
```css
/* Check if parent has mixed children */
/* BAD - counts all children */
div p:nth-child(2) { }

/* GOOD - counts only <p> elements */
div p:nth-of-type(2) { }
```

### Problem 3: ::before/::after Not Showing

**Symptoms:** Pseudo-elements invisible

**Checklist:**
```css
.element::before {
    content: ''; /* 1. Must have content */
    display: block; /* 2. Check display */
    width: 20px; /* 3. Must have dimensions */
    height: 20px;
}

/* Some elements can't have pseudo-elements: */
/* img, input, br, hr */
```

### Problem 4: :hover Not Working

**Symptoms:** Hover effect not triggering

**Solutions:**
```css
/* 1. Check if element is pointer-events: none */
.element {
    pointer-events: auto; /* Enable pointer events */
}

/* 2. Check z-index stacking */
.element {
    position: relative;
    z-index: 1;
}

/* 3. Ensure element has dimensions */
.element {
    min-width: 50px;
    min-height: 50px;
}
```

### Problem 5: :focus Outline Removed

**Symptoms:** No keyboard navigation indicator

**Solution:**
```css
/* Don't do this */
*:focus {
    outline: none; /* Accessibility issue */
}

/* Do this instead */
*:focus {
    outline: 2px solid blue;
    outline-offset: 2px;
}

/* Or use :focus-visible */
*:focus-visible {
    outline: 2px solid blue;
}
```

### Problem 6: Attribute Selector Not Matching

**Symptoms:** [attr="value"] doesn't work

**Solutions:**
```css
/* Exact match */
[class="button"] { } /* Must be exactly "button" */

/* Contains */
[class*="button"] { } /* Matches "button primary" */

/* Starts with */
[class^="btn"] { } /* Matches "btn-primary" */

/* Ends with */
[class$="primary"] { } /* Matches "btn-primary" */

/* Word match (space-separated) */
[class~="button"] { } /* Matches "button primary" */
```

### Problem 7: Specificity Issues

**Symptoms:** Style doesn't override another

**Solutions:**
```css
/* Calculate specificity: */
/* Inline style = 1000 */
/* ID = 100 */
/* Class/Attribute/Pseudo-class = 10 */
/* Element = 1 */

/* Increase specificity */
.container .button { } /* 20 */
.container .button.primary { } /* 30 */

/* Or use :where() for 0 specificity */
:where(.container) .button { } /* 10 */
```

### Problem 8: :not() Limitations

**Symptoms:** Complex :not() not working

**Solutions:**
```css
/* Old browsers: one selector only */
:not(.primary) { }

/* Modern browsers: multiple selectors */
:not(.primary, .secondary) { }

/* Workaround for old browsers */
:not(.primary):not(.secondary) { }
```

### Problem 9: Pseudo-class Order Matters

**Symptoms:** Link styles not working correctly

**Solution:**
```css
/* Remember LVHA order (LoVe HAte) */
a:link { } /* 1. Unvisited links */
a:visited { } /* 2. Visited links */
a:hover { } /* 3. Hover state */
a:active { } /* 4. Active (clicked) state */

/* Wrong order breaks styles */
```

### Problem 10: :has() Browser Support

**Symptoms:** :has() not working

**Solutions:**
```css
/* Check browser support */
@supports selector(:has(*)) {
    .card:has(img) {
        padding: 0;
    }
}

/* Fallback */
@supports not selector(:has(*)) {
    .card-with-image {
        padding: 0;
    }
}
```

## 2.11. Advanced Topics

### 2.11.1. Specificity Calculator

```css
/* Understanding specificity weights:

   Style attribute: 1000
   ID: 100
   Class, pseudo-class, attribute: 10
   Element, pseudo-element: 1
*/

/* Examples with calculations: */
h1 { }                          /* 0,0,0,1 = 1 */
.title { }                      /* 0,0,1,0 = 10 */
#header { }                     /* 0,1,0,0 = 100 */
div.container { }               /* 0,0,1,1 = 11 */
#nav ul li a { }                /* 0,1,0,3 = 103 */
.menu .item:hover { }           /* 0,0,3,0 = 30 */
ul > li:first-child { }         /* 0,0,1,2 = 12 */
div#main .content::before { }   /* 0,1,1,2 = 112 */

/* !important overrides everything (avoid!) */
color: red !important;
```

### 2.11.2. Modern CSS Selectors

```css
/* :is() - Matches any selector in list */
:is(h1, h2, h3):is(.title, .heading) {
    font-family: Arial;
}

/* :where() - Same as :is() but 0 specificity */
:where(h1, h2, h3) {
    margin: 0; /* Easy to override */
}

/* :has() - Parent/previous sibling selector */
.card:has(> img) { padding: 0; }
.card:has(.badge) { border: 2px solid gold; }
form:has(:invalid) { outline: 2px solid red; }

/* :not() with complex selectors */
button:not(:is(.primary, .secondary, :disabled)) {
    background: gray;
}

/* :focus-within - Has focused descendant */
form:focus-within {
    box-shadow: 0 0 10px blue;
}

/* :placeholder-shown */
input:not(:placeholder-shown) {
    border-color: green;
}

/* :in-range and :out-of-range */
input[type="number"]:in-range {
    border-color: green;
}

input[type="number"]:out-of-range {
    border-color: red;
}

/* :target - URL fragment target */
section:target {
    background: yellow;
}
```

### 2.11.3. Attribute Selector Deep Dive

```css
/* Exact match */
[attr="value"] { }

/* Contains word (space-separated) */
[attr~="value"] { }

/* Starts with (including hyphenated) */
[attr|="value"] { } /* Matches "value" or "value-*" */

/* Starts with (any) */
[attr^="value"] { }

/* Ends with */
[attr$="value"] { }

/* Contains substring */
[attr*="value"] { }

/* Case-insensitive flag */
[attr="value" i] { }

/* Case-sensitive flag (default) */
[attr="value" s] { }

/* Practical examples */
a[href^="https"] { /* Secure links */ }
a[href$=".pdf"] { /* PDF links */ }
a[href*="google"] { /* Links containing "google" */ }
img[alt~="photo"] { /* alt contains word "photo" */ }
[lang|="en"] { /* English variants: en, en-US, en-GB */ }
[data-status="active" i] { /* Case-insensitive */ }
```

### 2.11.4. Combinators Advanced Usage

```css
/* Multiple combinators */
article > h2 + p {
    /* <p> immediately after <h2> that is direct child of <article> */
}

/* Complex selectors */
.sidebar nav > ul > li:not(:last-child) > a {
    /* Direct child links of list items in sidebar nav, except last */
}

/* Combining with pseudo-classes */
.menu > li:hover > a::after {
    content: '';
    display: block;
    width: 100%;
    height: 2px;
    background: blue;
}

/* Sibling selection tricks */
/* Select all siblings between first and last */
li:first-child ~ li:not(:last-child) {
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
}

/* Adjacent sibling chain */
h1 + p + p {
    /* Second paragraph after h1 */
}
```

### 2.11.5. Functional Pseudo-classes

```css
/* :nth-child() advanced formulas */
:nth-child(odd) { } /* 1, 3, 5, 7, ... */
:nth-child(even) { } /* 2, 4, 6, 8, ... */
:nth-child(3) { } /* 3rd child */
:nth-child(2n) { } /* Even: 2, 4, 6, ... */
:nth-child(2n+1) { } /* Odd: 1, 3, 5, ... */
:nth-child(3n) { } /* Every 3rd: 3, 6, 9, ... */
:nth-child(3n+1) { } /* 1, 4, 7, 10, ... */
:nth-child(-n+3) { } /* First 3 */
:nth-child(n+4) { } /* 4th and after */
:nth-last-child(2) { } /* 2nd from end */

/* :nth-of-type() with selectors */
p:nth-of-type(2n) { } /* Even paragraphs */
div:nth-of-type(3n+1) { } /* Every 3rd div starting from 1st */

/* Multiple conditions */
li:nth-child(odd):not(:first-child) { }
```

### 2.11.6. Pseudo-element Advanced Techniques

```css
/* Counter with pseudo-elements */
.list {
    counter-reset: item;
}

.list-item::before {
    counter-increment: item;
    content: counter(item) ". ";
    font-weight: bold;
}

/* Multiple pseudo-elements (indirectly) */
.element::before {
    content: '';
    /* Create first pseudo-element */
}

.element::after {
    content: '';
    /* Create second pseudo-element */
}

/* Nested counters */
ol {
    counter-reset: section;
}

li::before {
    counter-increment: section;
    content: counters(section, ".") " ";
}

/* Attribute content */
.tooltip::after {
    content: attr(data-tooltip);
    position: absolute;
    background: black;
    color: white;
    padding: 5px 10px;
}

/* URL content */
.pdf-link::before {
    content: url('pdf-icon.svg');
    margin-right: 5px;
}
```

### 2.11.7. State Selectors

```css
/* Form validation states */
input:valid { border-color: green; }
input:invalid { border-color: red; }
input:required { border-left: 3px solid orange; }
input:optional { border-left: 3px solid gray; }
input:disabled { opacity: 0.5; }
input:enabled { opacity: 1; }
input:read-only { background: #f0f0f0; }
input:read-write { background: white; }

/* Checkbox/Radio states */
input:checked { background: blue; }
input:indeterminate { opacity: 0.5; }
input:default { box-shadow: 0 0 3px blue; }

/* Range states */
input:in-range { border-color: green; }
input:out-of-range { border-color: red; }

/* Link states */
a:any-link { /* Matches :link and :visited */ }
a:link { /* Unvisited */ }
a:visited { /* Visited */ }
a:local-link { /* Same domain */ }

/* User interaction states */
:hover { }
:active { }
:focus { }
:focus-within { /* Has focused child */ }
:focus-visible { /* Keyboard focus */ }
:target { /* URL fragment target */ }

/* Content states */
:empty { /* No children */ }
:blank { /* Empty or whitespace only */ }
```

### 2.11.8. Logical Selectors

```css
/* :is() - Selector list */
:is(header, main, footer) p {
    line-height: 1.5;
}

/* Specificity = highest in list */
:is(#id, .class) { } /* Specificity = 100 (from #id) */

/* :where() - Zero specificity */
:where(header, main, footer) p {
    line-height: 1.5;
}

/* Specificity = 0 (always) */
:where(#id, .class) { } /* Specificity = 0 */

/* :not() - Negation */
button:not(.primary) { }

/* Multiple :not() */
button:not(.primary):not(.secondary) { }

/* :not() with :is() */
button:not(:is(.primary, .secondary, .tertiary)) { }

/* :has() - Relational */
.card:has(img) { }
.card:has(> img) { /* Direct child only */ }
.card:has(+ .card) { /* Has next sibling */ }
form:has(:invalid) { /* Has invalid input */ }
```

### 2.11.9. Grid and Flex Child Selectors

```css
/* Grid children */
.grid > *:nth-child(3n+1) {
    grid-column: span 2;
}

.grid > *:last-child:nth-child(odd) {
    grid-column: 1 / -1; /* Full width if odd number of items */
}

/* Flexbox children */
.flex > *:first-child {
    margin-left: 0;
}

.flex > *:last-child {
    margin-right: 0;
    margin-left: auto; /* Push to right */
}

.flex > *:only-child {
    margin: 0 auto; /* Center single item */
}

/* Quantity queries */
/* Select items when there are exactly 3 */
.item:first-child:nth-last-child(3),
.item:first-child:nth-last-child(3) ~ .item {
    width: calc(100% / 3);
}

/* Select items when there are 4 or more */
.item:first-child:nth-last-child(n+4),
.item:first-child:nth-last-child(n+4) ~ .item {
    width: 50%;
}
```

### 2.11.10. Performance Considerations

```css
/* SLOW - Right-to-left parsing */
* { }
body * { }
div * p { }
[class*="btn"] { }

/* FAST - More specific */
.button { }
.container > .item { }
#header .nav { }

/* Avoid deep nesting */
/* BAD */
.header .nav .menu .item .link { }

/* GOOD */
.nav-link { }

/* Avoid expensive selectors */
/* SLOW */
:nth-child(n) { }
[class*="prefix"] { }

/* FAST */
.specific-class { }
#specific-id { }

/* Use class selectors when possible */
/* Instead of: */
div:first-child:last-child { }

/* Use: */
.single-item { }
```

## 2.12. Bài Tập Thực Hành

### Bài 1: Styled Table
Tạo một bảng với striped rows, hover effects, và styled header.

**Yêu cầu:**
- Sử dụng :nth-child cho striped rows
- Hover effect trên rows
- First và last column có styling khác
- Header row có màu đậm

### Bài 2: Custom Form Controls
Tạo custom checkbox và radio buttons không dùng hình ảnh.

**Yêu cầu:**
- Dùng ::before/::after
- Checked state
- Disabled state
- Focus state

### Bài 3: Navigation with Active State
Tạo navigation menu với active page indicator.

**Yêu cầu:**
- Hover effects
- Active state
- First và last items có styling khác
- Underline animation

### Bài 4: Article Typography
Tạo styled article với drop cap và decorative elements.

**Yêu cầu:**
- ::first-letter drop cap
- ::first-line styling
- Blockquote với ::before quote marks
- Links với external indicators

### Bài 5: Card Grid
Tạo grid of cards với varying sizes sử dụng nth-child.

**Yêu cầu:**
- First card spans 2 columns
- Every 3rd card có màu khác
- Hover effects
- Empty cards có placeholder text

### Bài 6: Form Validation Styles
Tạo form với visual validation feedback.

**Yêu cầu:**
- :valid và :invalid states
- :required indicator
- :focus styles
- :disabled styling

### Bài 7: Breadcrumb Navigation
Tạo breadcrumb với separators sử dụng ::before.

**Yêu cầu:**
- ::before cho separators
- :first-child không có separator
- :last-child là current page
- Hover states

### Bài 8: Image Gallery với Overlay
Tạo gallery với hover overlay effects.

**Yêu cầu:**
- ::before cho overlay
- ::after cho title
- Different sizes cho first và last items
- Smooth transitions

### Bài 9: Button States
Tạo buttons với tất cả states (normal, hover, active, disabled).

**Yêu cầu:**
- :hover effects
- :active state
- :disabled styling
- :focus-visible cho accessibility

### Bài 10: Advanced List Styling
Tạo custom numbered list với counters.

**Yêu cầu:**
- CSS counters
- ::before cho numbers
- Different styling cho first 3 items
- Nested lists

### Bài 11: Dropdown Menu
Tạo dropdown menu với pure CSS.

**Yêu cầu:**
- :hover để show/hide
- > (child combinator)
- :first-child và :last-child
- Smooth transitions

### Bài 12: Product Card với States
Tạo product card với multiple states (sale, new, out of stock).

**Yêu cầu:**
- Attribute selectors [data-status]
- ::before badges
- :has() cho conditional styling (nếu supported)
- Hover effects

---

**Kết luận:** CSS3 selectors rất powerful, cho phép target elements chính xác mà không cần thêm classes. Hiểu rõ selectors giúp viết CSS hiệu quả và maintainable hơn.

**Chương tiếp theo:** Colors & Backgrounds
