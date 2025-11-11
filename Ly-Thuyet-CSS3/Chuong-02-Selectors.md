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

---

**Kết luận:** CSS3 selectors rất powerful, cho phép target elements chính xác mà không cần thêm classes.

**Chương tiếp theo:** Colors & Backgrounds
