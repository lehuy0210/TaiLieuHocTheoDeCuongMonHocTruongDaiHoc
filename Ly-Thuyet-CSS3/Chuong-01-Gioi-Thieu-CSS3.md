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

## 1.11. Real-World Examples

### Example 1: Modern Button Component

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }

        .btn-secondary {
            background: white;
            color: #667eea;
            border: 2px solid #667eea;
        }

        .btn-secondary:hover {
            background: #667eea;
            color: white;
        }
    </style>
</head>
<body>
    <button class="btn btn-primary">Primary Button</button>
    <button class="btn btn-secondary">Secondary Button</button>
</body>
</html>
```

### Example 2: Card Component with Shadow

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .card {
            max-width: 350px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        }

        .card-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .card-content {
            padding: 20px;
        }

        .card-title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }

        .card-description {
            color: #666;
            line-height: 1.6;
            margin-bottom: 15px;
        }

        .card-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 15px;
            border-top: 1px solid #eee;
        }

        .card-price {
            font-size: 20px;
            font-weight: bold;
            color: #667eea;
        }
    </style>
</head>
<body>
    <div class="card">
        <img src="product.jpg" alt="Product" class="card-image">
        <div class="card-content">
            <h3 class="card-title">Product Name</h3>
            <p class="card-description">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            </p>
            <div class="card-footer">
                <span class="card-price">$29.99</span>
                <button class="btn btn-primary">Buy Now</button>
            </div>
        </div>
    </div>
</body>
</html>
```

### Example 3: Navigation Bar

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .navbar {
            background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
            padding: 15px 0;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }

        .logo {
            color: white;
            font-size: 24px;
            font-weight: bold;
            text-decoration: none;
        }

        .nav-menu {
            display: flex;
            list-style: none;
            gap: 30px;
        }

        .nav-link {
            color: white;
            text-decoration: none;
            font-size: 16px;
            transition: color 0.3s ease;
            position: relative;
        }

        .nav-link::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: white;
            transition: width 0.3s ease;
        }

        .nav-link:hover::after {
            width: 100%;
        }

        .nav-link:hover {
            color: #ffd700;
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="#" class="logo">MyBrand</a>
            <ul class="nav-menu">
                <li><a href="#" class="nav-link">Home</a></li>
                <li><a href="#" class="nav-link">About</a></li>
                <li><a href="#" class="nav-link">Services</a></li>
                <li><a href="#" class="nav-link">Contact</a></li>
            </ul>
        </div>
    </nav>
</body>
</html>
```

### Example 4: Hero Section with Background

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .hero {
            height: 100vh;
            background: linear-gradient(
                135deg,
                rgba(102, 126, 234, 0.9),
                rgba(118, 75, 162, 0.9)
            ),
            url('hero-bg.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
        }

        .hero-content {
            max-width: 800px;
            padding: 20px;
        }

        .hero-title {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }

        .hero-subtitle {
            font-size: 24px;
            margin-bottom: 30px;
            opacity: 0.9;
        }

        .hero-cta {
            display: inline-block;
            padding: 15px 40px;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            font-size: 18px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        .hero-cta:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <section class="hero">
        <div class="hero-content">
            <h1 class="hero-title">Welcome to Our Website</h1>
            <p class="hero-subtitle">Create amazing experiences with CSS3</p>
            <a href="#" class="hero-cta">Get Started</a>
        </div>
    </section>
</body>
</html>
```

### Example 5: Form Styling

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .form-container {
            max-width: 400px;
            margin: 50px auto;
            padding: 30px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }

        .form-title {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 28px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 600;
        }

        .form-input {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }

        .form-input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        .form-input::placeholder {
            color: #999;
        }

        .form-submit {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        .form-submit:hover {
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2 class="form-title">Sign Up</h2>
        <form>
            <div class="form-group">
                <label class="form-label">Full Name</label>
                <input type="text" class="form-input" placeholder="John Doe">
            </div>
            <div class="form-group">
                <label class="form-label">Email</label>
                <input type="email" class="form-input" placeholder="john@example.com">
            </div>
            <div class="form-group">
                <label class="form-label">Password</label>
                <input type="password" class="form-input" placeholder="••••••••">
            </div>
            <button type="submit" class="form-submit">Create Account</button>
        </form>
    </div>
</body>
</html>
```

### Example 6: Pricing Table

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .pricing-container {
            display: flex;
            gap: 30px;
            padding: 50px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .pricing-card {
            flex: 1;
            background: white;
            border-radius: 12px;
            padding: 40px 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            text-align: center;
            transition: transform 0.3s ease;
        }

        .pricing-card:hover {
            transform: translateY(-10px);
        }

        .pricing-card.featured {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: scale(1.05);
        }

        .pricing-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .pricing-price {
            font-size: 48px;
            font-weight: bold;
            margin: 20px 0;
        }

        .pricing-price span {
            font-size: 20px;
            font-weight: normal;
        }

        .pricing-features {
            list-style: none;
            padding: 0;
            margin: 30px 0;
        }

        .pricing-features li {
            padding: 12px 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        }

        .pricing-card.featured .pricing-features li {
            border-bottom-color: rgba(255, 255, 255, 0.2);
        }

        .pricing-button {
            padding: 12px 30px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .pricing-card.featured .pricing-button {
            background: white;
            color: #667eea;
        }
    </style>
</head>
<body>
    <div class="pricing-container">
        <div class="pricing-card">
            <h3 class="pricing-title">Basic</h3>
            <div class="pricing-price">$9<span>/month</span></div>
            <ul class="pricing-features">
                <li>10 GB Storage</li>
                <li>100 GB Bandwidth</li>
                <li>Email Support</li>
                <li>Basic Features</li>
            </ul>
            <button class="pricing-button">Choose Plan</button>
        </div>

        <div class="pricing-card featured">
            <h3 class="pricing-title">Pro</h3>
            <div class="pricing-price">$29<span>/month</span></div>
            <ul class="pricing-features">
                <li>100 GB Storage</li>
                <li>Unlimited Bandwidth</li>
                <li>Priority Support</li>
                <li>All Features</li>
            </ul>
            <button class="pricing-button">Choose Plan</button>
        </div>

        <div class="pricing-card">
            <h3 class="pricing-title">Enterprise</h3>
            <div class="pricing-price">$99<span>/month</span></div>
            <ul class="pricing-features">
                <li>Unlimited Storage</li>
                <li>Unlimited Bandwidth</li>
                <li>24/7 Support</li>
                <li>Custom Features</li>
            </ul>
            <button class="pricing-button">Choose Plan</button>
        </div>
    </div>
</body>
</html>
```

### Example 7: Image Gallery Grid

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }

        .gallery-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .gallery-item:hover .gallery-image {
            transform: scale(1.1);
        }

        .gallery-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(102, 126, 234, 0.9);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .gallery-item:hover .gallery-overlay {
            opacity: 1;
        }

        .gallery-title {
            color: white;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="gallery">
        <div class="gallery-item">
            <img src="image1.jpg" alt="Image 1" class="gallery-image">
            <div class="gallery-overlay">
                <h3 class="gallery-title">Project 1</h3>
            </div>
        </div>
        <!-- Repeat for more items -->
    </div>
</body>
</html>
```

## 1.12. Tips & Tricks

### Tip 1: Use CSS Variables for Consistency

```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --spacing-unit: 8px;
    --border-radius: 8px;
    --transition-speed: 0.3s;
}

.button {
    background: var(--primary-color);
    padding: calc(var(--spacing-unit) * 2);
    border-radius: var(--border-radius);
    transition: all var(--transition-speed) ease;
}
```

### Tip 2: Box-Sizing Border-Box

```css
/* Apply to all elements */
*, *::before, *::after {
    box-sizing: border-box;
}

/* Now padding and border are included in width/height */
.box {
    width: 200px;
    padding: 20px;
    border: 5px solid black;
    /* Total width is still 200px, not 250px */
}
```

### Tip 3: Use rem Instead of px for Accessibility

```css
/* Set base font size on html */
html {
    font-size: 16px;
}

/* Use rem for scalable sizes */
h1 { font-size: 3rem; }      /* 48px */
h2 { font-size: 2.5rem; }    /* 40px */
p { font-size: 1rem; }       /* 16px */
small { font-size: 0.875rem; } /* 14px */
```

### Tip 4: Responsive Images

```css
img {
    max-width: 100%;
    height: auto;
    display: block;
}
```

### Tip 5: Center Elements Easily

```css
/* Method 1: Flexbox */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Method 2: Grid */
.container {
    display: grid;
    place-items: center;
    height: 100vh;
}

/* Method 3: Absolute + Transform */
.element {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

### Tip 6: Smooth Scrolling

```css
html {
    scroll-behavior: smooth;
}
```

### Tip 7: Custom Scrollbar

```css
/* Webkit browsers (Chrome, Safari) */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: #555;
}
```

### Tip 8: Truncate Text with Ellipsis

```css
/* Single line */
.truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Multiple lines (requires -webkit) */
.truncate-multiline {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
```

### Tip 9: Aspect Ratio

```css
/* Modern way */
.video-container {
    aspect-ratio: 16 / 9;
}

/* Old way (still works) */
.video-container-old {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 ratio */
    height: 0;
}

.video-container-old iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
```

### Tip 10: Object-fit for Images

```css
.image-cover {
    width: 300px;
    height: 200px;
    object-fit: cover; /* Crop to fill */
}

.image-contain {
    width: 300px;
    height: 200px;
    object-fit: contain; /* Fit inside without cropping */
}
```

## 1.13. Common Mistakes

### Mistake 1: Forgetting Box-Sizing

**Problem:**
```css
.box {
    width: 200px;
    padding: 20px;
    border: 5px solid black;
    /* Total width = 200 + 40 + 10 = 250px! */
}
```

**Solution:**
```css
.box {
    box-sizing: border-box;
    width: 200px;
    padding: 20px;
    border: 5px solid black;
    /* Total width = 200px */
}
```

### Mistake 2: Not Using Relative Units

**Problem:**
```css
/* Fixed sizes don't scale */
body {
    font-size: 16px;
}

h1 {
    font-size: 32px; /* Doesn't scale if user changes browser font size */
}
```

**Solution:**
```css
html {
    font-size: 16px;
}

body {
    font-size: 1rem;
}

h1 {
    font-size: 2rem; /* Scales with user preferences */
}
```

### Mistake 3: Too Many !important

**Problem:**
```css
.button {
    color: red !important;
    background: blue !important;
    padding: 10px !important;
    /* Makes CSS hard to maintain */
}
```

**Solution:**
```css
/* Use more specific selectors instead */
.header .navigation .button {
    color: red;
    background: blue;
    padding: 10px;
}
```

### Mistake 4: Not Using Shorthand

**Problem:**
```css
.box {
    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 10px;
    margin-left: 20px;
}
```

**Solution:**
```css
.box {
    margin: 10px 20px; /* top/bottom left/right */
}
```

### Mistake 5: Inline Styles Everywhere

**Problem:**
```html
<div style="color: red; font-size: 16px; padding: 20px;">
    Content
</div>
```

**Solution:**
```html
<div class="content-box">Content</div>

<style>
.content-box {
    color: red;
    font-size: 16px;
    padding: 20px;
}
</style>
```

### Mistake 6: Not Resetting Default Styles

**Problem:**
```css
/* Browser default margins/paddings cause issues */
```

**Solution:**
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

### Mistake 7: Overusing Divs

**Problem:**
```html
<div class="header">
    <div class="navigation">
        <div class="menu-item">Home</div>
    </div>
</div>
```

**Solution:**
```html
<header>
    <nav>
        <a href="#">Home</a>
    </nav>
</header>
```

### Mistake 8: Not Using CSS Variables

**Problem:**
```css
.button-primary { background: #667eea; }
.link-primary { color: #667eea; }
.border-primary { border-color: #667eea; }
/* Hard to maintain if color changes */
```

**Solution:**
```css
:root {
    --primary-color: #667eea;
}

.button-primary { background: var(--primary-color); }
.link-primary { color: var(--primary-color); }
.border-primary { border-color: var(--primary-color); }
```

### Mistake 9: Not Considering Performance

**Problem:**
```css
* {
    box-shadow: 0 0 50px rgba(0,0,0,0.5);
    animation: spin 1s infinite;
}
/* Too many expensive properties */
```

**Solution:**
```css
/* Apply animations only where needed */
.animated-element {
    animation: spin 1s infinite;
    will-change: transform; /* Hint to browser */
}
```

### Mistake 10: Ignoring Accessibility

**Problem:**
```css
a {
    color: inherit; /* Links look like regular text */
}

button:focus {
    outline: none; /* Removes keyboard navigation indicator */
}
```

**Solution:**
```css
a {
    color: blue;
    text-decoration: underline;
}

button:focus {
    outline: 2px solid blue;
    outline-offset: 2px;
}
```

## 1.14. Troubleshooting

### Problem 1: Styles Not Applied

**Symptoms:** CSS doesn't seem to work

**Possible Causes:**
1. Typo in selector
2. CSS file not linked correctly
3. Specificity issue
4. Browser cache

**Solutions:**
```html
<!-- Check file path -->
<link rel="stylesheet" href="styles.css">

<!-- Clear browser cache: Ctrl+Shift+R (Chrome) -->

<!-- Check selector spelling -->
<style>
.buttom { } /* WRONG */
.button { } /* CORRECT */
</style>

<!-- Increase specificity -->
<style>
.container .button { } /* More specific */
</style>
```

### Problem 2: Box Model Issues

**Symptoms:** Element wider than expected

**Solution:**
```css
/* Always use border-box */
*, *::before, *::after {
    box-sizing: border-box;
}
```

### Problem 3: Z-Index Not Working

**Symptoms:** Elements overlap incorrectly

**Solution:**
```css
/* Z-index only works on positioned elements */
.element {
    position: relative; /* or absolute, fixed, sticky */
    z-index: 10;
}
```

### Problem 4: Flexbox Items Overflowing

**Symptoms:** Flex items too wide

**Solution:**
```css
.flex-item {
    min-width: 0; /* Allow flexbox to shrink items */
    overflow: hidden; /* Hide overflow */
}
```

### Problem 5: Vertical Centering Not Working

**Symptoms:** vertical-align doesn't work

**Solution:**
```css
/* vertical-align only works on inline/table-cell elements */

/* Use flexbox instead */
.container {
    display: flex;
    align-items: center;
}
```

### Problem 6: Margin Collapse

**Symptoms:** Margins between elements don't add up

**Solution:**
```css
/* Use padding instead of margin */
.parent {
    padding: 20px;
}

/* Or use flexbox/grid (no margin collapse) */
.container {
    display: flex;
    gap: 20px;
}
```

### Problem 7: Text Overflow

**Symptoms:** Text breaks layout

**Solution:**
```css
.text-container {
    word-wrap: break-word;
    overflow-wrap: break-word;
    hyphens: auto;
}
```

### Problem 8: Hover Not Working on Mobile

**Symptoms:** :hover doesn't work on touch devices

**Solution:**
```css
/* Add touch-friendly states */
.button:hover,
.button:active,
.button:focus {
    background: blue;
}

/* Or use JavaScript for better touch support */
```

### Problem 9: Colors Look Different in Browsers

**Symptoms:** Colors render differently

**Solution:**
```css
/* Use consistent color spaces */
color: rgb(102, 126, 234); /* More consistent than named colors */

/* Define color profile */
@media (color-gamut: srgb) {
    :root {
        --primary: rgb(102, 126, 234);
    }
}
```

### Problem 10: Animations Janky/Laggy

**Symptoms:** Animations stutter

**Solution:**
```css
/* Only animate transform and opacity */
.smooth-animation {
    transition: transform 0.3s ease, opacity 0.3s ease;
    will-change: transform;
}

/* Avoid animating: */
/* - width/height */
/* - top/left */
/* - margin/padding */
```

## 1.15. Advanced Topics

### 1.15.1. CSS Custom Properties (Variables) Deep Dive

```css
:root {
    /* Define global variables */
    --primary-color: #667eea;
    --spacing: 8px;
}

/* Use calc() with variables */
.element {
    padding: calc(var(--spacing) * 2);
    margin: calc(var(--spacing) * 3);
}

/* Override variables in specific contexts */
.dark-theme {
    --primary-color: #8b9eff;
}

/* Use fallback values */
.element {
    color: var(--text-color, #333); /* Falls back to #333 */
}

/* Dynamic variables with JavaScript */
<script>
document.documentElement.style.setProperty('--primary-color', '#ff0000');
</script>
```

### 1.15.2. CSS Functions

```css
/* calc() - Mathematical calculations */
.element {
    width: calc(100% - 50px);
    height: calc(100vh - 60px);
    font-size: calc(16px + 0.5vw);
}

/* min() and max() */
.element {
    width: min(90%, 1200px); /* Smaller of the two */
    font-size: max(16px, 1vw); /* Larger of the two */
}

/* clamp() - Set min, preferred, and max */
.element {
    font-size: clamp(14px, 2vw, 24px);
    /* min: 14px, preferred: 2vw, max: 24px */
}

/* var() - CSS variables */
.element {
    color: var(--primary-color);
}

/* attr() - Get attribute value */
a::after {
    content: " (" attr(href) ")";
}

/* url() - Link resources */
.element {
    background-image: url('image.jpg');
}
```

### 1.15.3. CSS Cascade and Specificity

```css
/* Specificity calculation:
   Inline style = 1000
   ID = 100
   Class/Attribute/Pseudo-class = 10
   Element/Pseudo-element = 1
*/

/* Examples: */
h1 { }                    /* 1 */
.title { }                /* 10 */
#header { }               /* 100 */
div.container { }         /* 11 */
div#main .content { }     /* 111 */
a:hover { }               /* 11 */
li:first-child { }        /* 11 */

/* Specificity wars - avoid !important */
.button { color: blue; }
.button.primary { color: red; } /* More specific, wins */

/* Cascade order:
   1. User agent (browser) styles
   2. User styles
   3. Author styles (your CSS)
   4. !important author styles
   5. !important user styles
*/
```

### 1.15.4. CSS Inheritance

```css
/* Inherited properties (automatically pass to children): */
/* - color */
/* - font-* */
/* - line-height */
/* - text-* */
/* - visibility */
/* - cursor */

/* Non-inherited properties: */
/* - margin, padding */
/* - border */
/* - background */
/* - width, height */
/* - position */

/* Force inheritance */
.child {
    margin: inherit;
    background: inherit;
}

/* Reset to initial value */
.element {
    color: initial;
}

/* Use computed value of parent */
.element {
    color: inherit;
}

/* Use value of property in cascade */
.element {
    color: unset;
}
```

### 1.15.5. CSS @import vs <link>

```css
/* @import (slower, blocks rendering) */
@import url('styles.css');
@import url('print.css') print;

/* Prefer <link> instead */
```

```html
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="print.css" media="print">
```

### 1.15.6. Performance Optimization

```css
/* 1. Use efficient selectors */
/* BAD - Universal selector */
* { margin: 0; }

/* GOOD - Specific selector */
.reset-element { margin: 0; }

/* 2. Avoid deep nesting */
/* BAD */
.header .nav .menu .item .link { }

/* GOOD */
.nav-link { }

/* 3. Use will-change for animations */
.animated {
    will-change: transform;
}

/* Remove after animation */
.animated.done {
    will-change: auto;
}

/* 4. Use contain for isolated components */
.component {
    contain: layout style paint;
}

/* 5. Minimize repaints/reflows */
/* BAD - Triggers reflow */
.element {
    width: 100px;
    transition: width 0.3s;
}

/* GOOD - GPU accelerated */
.element {
    transform: scaleX(1);
    transition: transform 0.3s;
}
```

### 1.15.7. CSS Methodologies

```css
/* BEM (Block Element Modifier) */
.card { }
.card__title { }
.card__body { }
.card--featured { }

/* OOCSS (Object-Oriented CSS) */
/* Structure */
.box { }
/* Skin */
.box-primary { }
.box-secondary { }

/* SMACSS (Scalable and Modular Architecture) */
/* Base */
html, body { }

/* Layout */
.l-header { }
.l-sidebar { }

/* Module */
.button { }
.card { }

/* State */
.is-active { }
.is-hidden { }

/* Theme */
.theme-dark { }
```

### 1.15.8. CSS Preprocessors Concepts

```css
/* SASS/SCSS concepts */

/* Nesting */
.card {
    padding: 20px;

    .title {
        font-size: 24px;
    }

    &:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
}

/* Mixins */
@mixin button-style($color) {
    background: $color;
    padding: 10px 20px;
    border-radius: 4px;
}

.btn-primary {
    @include button-style(blue);
}

/* Variables */
$primary-color: #667eea;

.element {
    color: $primary-color;
}
```

### 1.15.9. Modern CSS Features

```css
/* Logical Properties */
.element {
    margin-inline-start: 20px; /* LTR: left, RTL: right */
    margin-inline-end: 20px;   /* LTR: right, RTL: left */
    margin-block-start: 10px;  /* top */
    margin-block-end: 10px;    /* bottom */
}

/* :is() and :where() */
:is(h1, h2, h3) {
    margin-block: 1em;
}

/* :has() - Parent selector */
.card:has(img) {
    padding: 0;
}

/* Container Queries (upcoming) */
@container (min-width: 400px) {
    .card {
        display: flex;
    }
}

/* Cascade Layers */
@layer reset, base, components, utilities;

@layer base {
    h1 { font-size: 2rem; }
}

@layer components {
    .button { padding: 10px; }
}
```

### 1.15.10. CSS Architecture

```css
/* Folder structure example:
styles/
├── abstracts/
│   ├── _variables.css
│   └── _mixins.css
├── base/
│   ├── _reset.css
│   └── _typography.css
├── components/
│   ├── _button.css
│   ├── _card.css
│   └── _navbar.css
├── layout/
│   ├── _header.css
│   ├── _footer.css
│   └── _grid.css
├── pages/
│   ├── _home.css
│   └── _about.css
└── main.css
*/

/* main.css - Import order matters! */
@import 'abstracts/variables';
@import 'base/reset';
@import 'base/typography';
@import 'layout/grid';
@import 'components/button';
@import 'pages/home';
```

## 1.16. Resources

### Official Documentation
- MDN CSS Documentation: https://developer.mozilla.org/en-US/docs/Web/CSS
- W3C CSS Specifications: https://www.w3.org/Style/CSS/
- CSS Working Group: https://www.w3.org/Style/CSS/members

### Learning Resources
- CSS-Tricks: https://css-tricks.com/
- W3Schools CSS: https://www.w3schools.com/css/
- Codrops CSS Reference: https://tympanus.net/codrops/css_reference/
- Smashing Magazine CSS: https://www.smashingmagazine.com/category/css

### Tools & Utilities
- Can I Use: https://caniuse.com/
- CSS Validator: https://jigsaw.w3.org/css-validator/
- Autoprefixer: https://autoprefixer.github.io/
- CSS Stats: https://cssstats.com/

### Playgrounds
- CodePen: https://codepen.io/
- JSFiddle: https://jsfiddle.net/
- CSS Diner (Learning Game): https://flukeout.github.io/

### Color Tools
- Coolors: https://coolors.co/
- Adobe Color: https://color.adobe.com/
- Color Hunt: https://colorhunt.co/

### Books
- CSS: The Definitive Guide
- CSS Secrets by Lea Verou
- Every Layout by Heydon Pickering

## 1.17. Bài Tập Thực Hành

### Bài 1: Personal Profile Card
Tạo một card hiển thị thông tin cá nhân với ảnh đại diện, tên, nghề nghiệp, và các nút social media.

**Yêu cầu:**
- Border radius cho card và avatar
- Box shadow
- Hover effects trên buttons
- Responsive text

### Bài 2: Navigation Menu
Tạo một thanh navigation bar với logo và menu items.

**Yêu cầu:**
- Horizontal layout
- Active state cho current page
- Hover effects với underline animation
- Sticky positioning

### Bài 3: Login Form
Tạo form đăng nhập với username, password, và remember me checkbox.

**Yêu cầu:**
- Input focus states
- Button hover effects
- Label styling
- Validation styles (optional)

### Bài 4: Image Gallery
Tạo gallery hiển thị 6-9 ảnh trong grid layout.

**Yêu cầu:**
- Equal height images
- Hover overlay effects
- Gap between images
- Rounded corners

### Bài 5: Pricing Table
Tạo bảng giá với 3 plans (Basic, Pro, Enterprise).

**Yêu cầu:**
- Featured plan highlighted
- Hover effects
- List of features
- Call-to-action buttons

### Bài 6: Hero Section
Tạo hero section với background image và centered content.

**Yêu cầu:**
- Full viewport height
- Background overlay
- Centered text
- Call-to-action button

### Bài 7: Blog Post Card
Tạo card hiển thị bài blog với thumbnail, title, excerpt, và metadata.

**Yêu cầu:**
- Image at top
- Text truncation for excerpt
- Date and author info
- Read more button

### Bài 8: Footer Section
Tạo footer với 4 columns: About, Links, Services, Contact.

**Yêu cầu:**
- Multi-column layout
- Social media icons
- Copyright text
- Background color

### Bài 9: Testimonial Component
Tạo component hiển thị customer testimonial với quote, name, và rating.

**Yêu cầu:**
- Quote styling
- Profile image
- Star rating
- Background and shadow

### Bài 10: Alert/Notification Box
Tạo 4 loại alert boxes: success, error, warning, info.

**Yêu cầu:**
- Different colors for each type
- Icon (using emoji or text)
- Close button
- Border and background

### Bài 11: Feature Grid
Tạo grid hiển thị 6 features với icon, title, và description.

**Yêu cầu:**
- 3 columns on desktop
- Icon styling
- Hover effects
- Consistent spacing

### Bài 12: Complete Landing Page
Tạo một landing page hoàn chỉnh kết hợp tất cả các components đã học.

**Yêu cầu:**
- Navigation bar
- Hero section
- Features section
- Pricing section
- Testimonials
- Footer
- Consistent styling throughout

---

**Chương tiếp theo:** Selectors và Specificity
