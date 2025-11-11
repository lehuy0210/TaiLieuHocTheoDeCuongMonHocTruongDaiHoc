# CHƯƠNG 1: GIỚI THIỆU CSS3

## 1.1. CSS3 là gì?

CSS3 (Cascading Style Sheets Level 3) là phiên bản mới nhất của ngôn ngữ stylesheet, được dùng để thiết kế và trình bày giao diện web.

### 1.1.1. Vai trò của CSS3

**HTML** = Cấu trúc (Structure)
**CSS** = Trình bày (Presentation)
**JavaScript** = Hành vi (Behavior)

```html
<!-- HTML: Cấu trúc -->
<div class="card">
    <h2>Title</h2>
    <p>Content</p>
</div>

<!-- CSS: Styling -->
<style>
.card {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
```

## 1.2. Cú pháp CSS

### 1.2.1. Basic Syntax

```css
selector {
    property: value;
    property: value;
}
```

**Ví dụ:**
```css
h1 {
    color: blue;
    font-size: 24px;
    font-weight: bold;
}
```

### 1.2.2. Comments

```css
/* Single line comment */

/*
   Multi-line
   comment
*/
```

## 1.3. Cách thêm CSS

### 1.3.1. Inline CSS

```html
<p style="color: red; font-size: 16px;">Text</p>
```

**Ưu điểm:** Áp dụng nhanh
**Nhược điểm:** Khó maintain, không tái sử dụng

### 1.3.2. Internal CSS

```html
<head>
    <style>
        p {
            color: blue;
        }
    </style>
</head>
```

**Ưu điểm:** Tất cả CSS trong 1 file HTML
**Nhược điểm:** Không tái sử dụng cho pages khác

### 1.3.3. External CSS (Khuyên dùng)

```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

**styles.css:**
```css
p {
    color: green;
}
```

**Ưu điểm:** Tái sử dụng, dễ maintain
**Nhược điểm:** HTTP request thêm

## 1.4. CSS Selectors Cơ bản

### 1.4.1. Element Selector

```css
p {
    color: blue;
}
```

### 1.4.2. Class Selector

```css
.container {
    width: 1200px;
    margin: 0 auto;
}
```

```html
<div class="container">Content</div>
```

### 1.4.3. ID Selector

```css
#header {
    background: navy;
}
```

```html
<header id="header">Header</header>
```

### 1.4.4. Universal Selector

```css
* {
    margin: 0;
    padding: 0;
}
```

## 1.5. Colors

### 1.5.1. Color Values

```css
/* Named colors */
color: red;
color: blue;

/* Hex */
color: #FF0000;
color: #F00;

/* RGB */
color: rgb(255, 0, 0);

/* RGBA (with transparency) */
color: rgba(255, 0, 0, 0.5);

/* HSL */
color: hsl(0, 100%, 50%);

/* HSLA */
color: hsla(0, 100%, 50%, 0.5);
```

## 1.6. Units

### 1.6.1. Absolute Units

```css
/* Pixels */
width: 100px;

/* Points */
font-size: 12pt;

/* Inches */
width: 2in;
```

### 1.6.2. Relative Units

```css
/* Em (relative to parent) */
font-size: 1.5em;

/* Rem (relative to root) */
font-size: 1.5rem;

/* Percentage */
width: 50%;

/* Viewport units */
width: 100vw;  /* viewport width */
height: 100vh; /* viewport height */
```

## 1.7. CSS3 Features

### 1.7.1. New Features

- **Border Radius**
- **Box Shadow**
- **Gradients**
- **Transforms**
- **Transitions**
- **Animations**
- **Flexbox**
- **Grid**
- **Variables**
- **Media Queries**

### 1.7.2. Examples

**Border Radius:**
```css
.box {
    border-radius: 10px;
}
```

**Box Shadow:**
```css
.card {
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

**Gradients:**
```css
.gradient {
    background: linear-gradient(to right, red, blue);
}
```

## 1.8. Browser Support

**Checking compatibility:**
- Can I Use: https://caniuse.com/
- MDN Browser Compatibility

**Vendor Prefixes (ít cần thiết hiện nay):**
```css
.element {
    -webkit-transform: rotate(45deg); /* Safari, Chrome */
    -moz-transform: rotate(45deg);    /* Firefox */
    -ms-transform: rotate(45deg);     /* IE */
    -o-transform: rotate(45deg);      /* Opera */
    transform: rotate(45deg);         /* Standard */
}
```

## 1.9. Development Tools

### 1.9.1. Browser DevTools

**Chrome DevTools:**
- Inspect Element (F12)
- Edit CSS live
- Computed styles
- CSS coverage

### 1.9.2. Extensions

- CSS Peek (VS Code)
- CSS Navigation (VS Code)
- Live Server
- Prettier

## 1.10. Best Practices

### 1.10.1. Organization

```css
/* 1. Reset/Normalize */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* 2. Variables */
:root {
    --primary-color: #007bff;
    --font-size: 16px;
}

/* 3. Global Styles */
body {
    font-family: Arial, sans-serif;
}

/* 4. Components */
.button {
    /* styles */
}
```

### 1.10.2. Naming Conventions

**BEM (Block Element Modifier):**
```css
.card { }
.card__title { }
.card__body { }
.card--featured { }
```

## 1.11. Resources

- MDN CSS Documentation
- CSS-Tricks
- W3Schools CSS
- Codrops CSS Reference

---

**Chương tiếp theo:** Selectors và Specificity
