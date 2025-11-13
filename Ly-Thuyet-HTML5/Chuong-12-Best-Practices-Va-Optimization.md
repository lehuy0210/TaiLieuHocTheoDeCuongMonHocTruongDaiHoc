# CHƯƠNG 12: BEST PRACTICES VÀ OPTIMIZATION

## 12.1. HTML Best Practices

### 12.1.1. Document Structure

**Proper DOCTYPE:**
```html
<!DOCTYPE html>
```

**Language declaration:**
```html
<html lang="vi">
```

**Character encoding:**
```html
<meta charset="UTF-8">
```

**Viewport for responsive:**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### 12.1.2. Semantic HTML

**Tốt - Semantic:**
```html
<header>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
        </ul>
    </nav>
</header>

<main>
    <article>
        <h1>Title</h1>
        <p>Content</p>
    </article>
</main>

<footer>
    <p>&copy; 2024</p>
</footer>
```

**Tránh - Non-semantic:**
```html
<div id="header">
    <div id="nav">
        <div class="menu">
            <div class="item"><a href="/">Home</a></div>
        </div>
    </div>
</div>
```

### 12.1.3. Clean Code

**Indentation:**
```html
<ul>
    <li>
        <a href="#">
            <span>Link Text</span>
        </a>
    </li>
</ul>
```

**Lowercase tags và attributes:**
```html
<!-- Tốt -->
<div class="container">

<!-- Tránh -->
<DIV CLASS="container">
```

**Quote attributes:**
```html
<!-- Tốt -->
<img src="image.jpg" alt="Description">

<!-- Tránh -->
<img src=image.jpg alt=Description>
```

**Close all tags:**
```html
<p>Paragraph</p>
<img src="image.jpg" alt="Image">
<br>
```

### 12.1.4. Accessibility

**Alt text cho images:**
```html
<img src="logo.jpg" alt="Company Logo">

<!-- Decorative images -->
<img src="decoration.png" alt="" role="presentation">
```

**Labels cho inputs:**
```html
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

**ARIA attributes:**
```html
<button aria-label="Close" onclick="closeDialog()">×</button>

<nav aria-label="Main Navigation">
    <!-- Menu -->
</nav>
```

**Heading hierarchy:**
```html
<h1>Main Title</h1>
    <h2>Section</h2>
        <h3>Subsection</h3>
```

**Skip links:**
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

## 12.2. Performance Optimization

### 12.2.1. Minimize HTTP Requests

**Combine files:**
```html
<!-- Before -->
<link rel="stylesheet" href="header.css">
<link rel="stylesheet" href="content.css">
<link rel="stylesheet" href="footer.css">

<!-- After -->
<link rel="stylesheet" href="styles.min.css">
```

**CSS Sprites:**
```css
.icon {
    background-image: url('sprites.png');
}
.icon-home { background-position: 0 0; }
.icon-search { background-position: -20px 0; }
```

**Inline critical CSS:**
```html
<head>
    <style>
        /* Critical CSS inline */
        body { margin: 0; font-family: Arial; }
    </style>
    <link rel="stylesheet" href="styles.css">
</head>
```

### 12.2.2. Optimize Images

**Proper format:**
- JPEG: Photos
- PNG: Graphics with transparency
- WebP: Modern format, smaller size
- SVG: Icons, logos

**Responsive images:**
```html
<picture>
    <source media="(min-width: 1200px)" srcset="large.webp" type="image/webp">
    <source media="(min-width: 768px)" srcset="medium.webp" type="image/webp">
    <source srcset="small.webp" type="image/webp">
    <img src="fallback.jpg" alt="Description">
</picture>
```

**Lazy loading:**
```html
<img src="image.jpg" alt="Description" loading="lazy">
```

**Image compression:**
- TinyPNG, ImageOptim
- Target < 200KB for most images

### 12.2.3. Resource Loading

**CSS trong `<head>`:**
```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

**JavaScript trước `</body>`:**
```html
<body>
    <!-- Content -->
    <script src="script.js"></script>
</body>
```

**Async và defer:**
```html
<!-- Async - load và execute ngay -->
<script async src="analytics.js"></script>

<!-- Defer - load song song, execute sau khi DOM ready -->
<script defer src="script.js"></script>
```

**Preload critical resources:**
```html
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="hero.jpg" as="image">
```

**Preconnect:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://external-api.com">
```

### 12.2.4. Minification

**HTML minification:**
```html
<!-- Before -->
<div class="container">
    <h1>Title</h1>
    <p>Paragraph</p>
</div>

<!-- After -->
<div class="container"><h1>Title</h1><p>Paragraph</p></div>
```

**Remove comments:**
```html
<!-- Development -->
<!-- TODO: Fix this section -->
<div>Content</div>

<!-- Production -->
<div>Content</div>
```

### 12.2.5. Caching

**Cache-Control headers:**
```html
<!-- Static resources -->
<link rel="stylesheet" href="styles.css?v=1.2.3">
<script src="script.js?v=1.2.3"></script>
```

**Service Worker caching:**
```javascript
// Cache static assets
const CACHE_NAME = 'v1';
const urlsToCache = ['/', '/styles.css', '/script.js'];
```

## 12.3. SEO Best Practices

### 12.3.1. Meta Tags

```html
<head>
    <!-- Title -->
    <title>Page Title - Site Name (max 60 chars)</title>

    <!-- Description -->
    <meta name="description" content="Page description, 150-160 characters">

    <!-- Keywords (ít quan trọng) -->
    <meta name="keywords" content="keyword1, keyword2, keyword3">

    <!-- Author -->
    <meta name="author" content="Author Name">

    <!-- Robots -->
    <meta name="robots" content="index, follow">

    <!-- Canonical URL -->
    <link rel="canonical" href="https://example.com/page">

    <!-- Open Graph (Facebook) -->
    <meta property="og:title" content="Page Title">
    <meta property="og:description" content="Page description">
    <meta property="og:image" content="https://example.com/image.jpg">
    <meta property="og:url" content="https://example.com/page">
    <meta property="og:type" content="website">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Page Title">
    <meta name="twitter:description" content="Page description">
    <meta name="twitter:image" content="https://example.com/image.jpg">
</head>
```

### 12.3.2. Structured Data

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "author": {
    "@type": "Person",
    "name": "John Doe"
  },
  "datePublished": "2024-01-15",
  "image": "https://example.com/image.jpg"
}
</script>
```

### 12.3.3. URL Structure

**Tốt:**
```
https://example.com/products/laptops
https://example.com/blog/html5-tutorial
```

**Tránh:**
```
https://example.com/page.php?id=123&cat=5
```

### 12.3.4. Internal Linking

```html
<article>
    <p>Learn more about <a href="/html5">HTML5</a> and <a href="/css3">CSS3</a></p>
    <p>Related: <a href="/javascript">JavaScript Tutorial</a></p>
</article>
```

## 12.4. Security

### 12.4.1. Content Security Policy

```html
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self' https://trusted.com">
```

### 12.4.2. XSS Protection

```html
<!-- Sanitize user input -->
<!-- Never use innerHTML với user input -->

<!-- Tốt -->
element.textContent = userInput;

<!-- Tránh -->
element.innerHTML = userInput; // XSS vulnerability
```

### 12.4.3. External Links

```html
<a href="https://external-site.com"
   target="_blank"
   rel="noopener noreferrer">
   External Link
</a>
```

### 12.4.4. Form Validation

```html
<form action="/submit" method="POST">
    <input type="email" name="email" required pattern="[^@]+@[^@]+\.[^@]+">
    <input type="password" name="password" required minlength="8">
    <button type="submit">Submit</button>
</form>
```

## 12.5. Mobile Optimization

### 12.5.1. Viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### 12.5.2. Touch-Friendly

**Touch targets (min 44x44 px):**
```css
button, a {
    min-width: 44px;
    min-height: 44px;
    padding: 12px 16px;
}
```

**Prevent zoom on input focus:**
```html
<input type="text" style="font-size: 16px;">
<!-- Font-size >= 16px prevents auto-zoom on iOS -->
```

### 12.5.3. Fast Tap

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
```

### 12.5.4. App-like Experience

```html
<!-- iOS -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="apple-touch-icon" href="icon.png">

<!-- Android -->
<meta name="mobile-web-app-capable" content="yes">
<link rel="manifest" href="/manifest.json">
```

## 12.6. Code Organization

### 12.6.1. File Structure

```
project/
├── index.html
├── css/
│   ├── main.css
│   └── responsive.css
├── js/
│   ├── app.js
│   └── utils.js
├── images/
│   ├── logo.png
│   └── hero.jpg
└── assets/
    ├── fonts/
    └── icons/
```

### 12.6.2. Comments

```html
<!-- Header Section Start -->
<header>
    <!-- Logo -->
    <div class="logo">...</div>

    <!-- Navigation -->
    <nav>...</nav>
</header>
<!-- Header Section End -->

<!-- TODO: Add social media links -->
<!-- FIXME: Fix mobile menu -->
```

### 12.6.3. Naming Conventions

**BEM (Block Element Modifier):**
```html
<div class="card">
    <div class="card__header">
        <h2 class="card__title">Title</h2>
    </div>
    <div class="card__body">
        <p class="card__text card__text--highlighted">Text</p>
    </div>
</div>
```

## 12.7. Testing và Validation

### 12.7.1. HTML Validation

**W3C Validator:**
```
https://validator.w3.org/
```

### 12.7.2. Accessibility Testing

**WAVE Tool:**
```
https://wave.webaim.org/
```

**Screen reader testing:**
- NVDA (Windows)
- JAWS (Windows)
- VoiceOver (macOS, iOS)

### 12.7.3. Performance Testing

**Google PageSpeed Insights:**
```
https://pagespeed.web.dev/
```

**Lighthouse (Chrome DevTools):**
- Performance
- Accessibility
- Best Practices
- SEO
- PWA

### 12.7.4. Cross-Browser Testing

**Test on:**
- Chrome
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

**Tools:**
- BrowserStack
- LambdaTest

## 12.8. Use Cases Thực Tế

### Use Case 1: High-Performance E-commerce Site
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>High-Performance E-commerce Store</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="dns-prefetch" href="https://analytics.example.com">
    <style>
        /* Critical CSS inline */
        body { margin: 0; font-family: 'Segoe UI', sans-serif; }
        .hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 40px 20px; }
    </style>
    <link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'">
</head>
<body>
    <header>
        <nav aria-label="Main Navigation">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/products">Products</a></li>
                <li><a href="/cart">Cart</a></li>
            </ul>
        </nav>
    </header>

    <main id="main-content">
        <section class="hero">
            <h1>Welcome to Our Store</h1>
            <p>Browse our products</p>
        </section>

        <section class="products">
            <h2>Featured Products</h2>
            <div id="productGrid" class="grid"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Our Store. All rights reserved.</p>
    </footer>

    <script>
        // Lazy load products
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    loadProductImage(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, {
            rootMargin: '50px'
        });

        function loadProductImage(img) {
            const src = img.dataset.src;
            if (src) {
                img.src = src;
                img.removeAttribute('data-src');
            }
        }

        // Optimize images
        const products = [
            { id: 1, name: 'Laptop', price: 25000000, image: 'laptop.jpg' },
            { id: 2, name: 'Phone', price: 15000000, image: 'phone.jpg' }
        ];

        const grid = document.getElementById('productGrid');
        products.forEach(product => {
            const card = document.createElement('article');
            card.className = 'product-card';
            card.innerHTML = `
                <picture>
                    <source srcset="${product.image.replace('.jpg', '.webp')}" type="image/webp">
                    <img data-src="${product.image}" alt="${product.name}" loading="lazy">
                </picture>
                <h3>${product.name}</h3>
                <p>${product.price.toLocaleString()}đ</p>
            `;
            const img = card.querySelector('img');
            observer.observe(img);
            grid.appendChild(card);
        });
    </script>
</body>
</html>
```

### Use Case 2: Accessible Blog with SEO Optimization
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Best Practices for Web Development - Tech Blog</title>
    <meta name="description" content="Learn about HTML5, CSS3, and JavaScript best practices for modern web development.">
    <meta name="keywords" content="HTML5, CSS3, JavaScript, web development, best practices">
    <meta name="author" content="Tech Blog Team">
    <link rel="canonical" href="https://techblog.example.com/article/best-practices">

    <!-- Open Graph for social sharing -->
    <meta property="og:title" content="Best Practices for Web Development">
    <meta property="og:description" content="Learn about HTML5, CSS3, and JavaScript best practices">
    <meta property="og:image" content="https://techblog.example.com/images/article-hero.jpg">
    <meta property="og:url" content="https://techblog.example.com/article/best-practices">
    <meta property="og:type" content="article">

    <!-- Structured Data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "Best Practices for Web Development",
        "description": "Comprehensive guide to web development best practices",
        "image": "https://techblog.example.com/images/article-hero.jpg",
        "author": {
            "@type": "Person",
            "name": "John Developer"
        },
        "datePublished": "2024-01-15",
        "dateModified": "2024-01-20"
    }
    </script>
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <header>
        <nav aria-label="Main Navigation">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/blog">Blog</a></li>
                <li><a href="/about">About</a></li>
            </ul>
        </nav>
    </header>

    <main id="main-content">
        <article>
            <header>
                <h1>Best Practices for Web Development</h1>
                <p>
                    <time datetime="2024-01-15">January 15, 2024</time>
                    by <span class="author">John Developer</span>
                </p>
            </header>

            <figure>
                <img src="hero.jpg" alt="Web development best practices illustration" loading="lazy">
                <figcaption>Figure 1: Modern web development stack</figcaption>
            </figure>

            <section>
                <h2>Semantic HTML</h2>
                <p>Use semantic HTML elements to improve accessibility and SEO.</p>
                <pre><code>&lt;header&gt;&lt;nav&gt;...&lt;/nav&gt;&lt;/header&gt;
&lt;main&gt;
    &lt;article&gt;...&lt;/article&gt;
&lt;/main&gt;
&lt;footer&gt;...&lt;/footer&gt;</code></pre>
            </section>

            <section>
                <h2>Accessibility</h2>
                <p>Always include alt text for images and proper labels for form elements.</p>
                <ul>
                    <li><strong>Alt text:</strong> Describe images concisely</li>
                    <li><strong>Labels:</strong> Link labels to form inputs</li>
                    <li><strong>Color contrast:</strong> Ensure sufficient contrast ratio</li>
                </ul>
            </section>

            <section>
                <h2>Performance</h2>
                <p>Optimize images, minimize CSS/JS, and use caching strategies.</p>
                <ol>
                    <li>Compress images (target &lt; 200KB)</li>
                    <li>Minify CSS and JavaScript</li>
                    <li>Use lazy loading</li>
                    <li>Implement caching</li>
                </ol>
            </section>
        </article>

        <aside aria-label="Related Articles">
            <h3>Related Articles</h3>
            <ul>
                <li><a href="/blog/html5-guide">HTML5 Comprehensive Guide</a></li>
                <li><a href="/blog/css3-advanced">Advanced CSS3 Techniques</a></li>
                <li><a href="/blog/javascript-tips">JavaScript Performance Tips</a></li>
            </ul>
        </aside>
    </main>

    <footer>
        <p>&copy; 2024 Tech Blog. All rights reserved.</p>
    </footer>

    <style>
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: #000;
            color: white;
            padding: 8px;
            text-decoration: none;
            z-index: 100;
        }

        .skip-link:focus {
            top: 0;
        }

        article img {
            max-width: 100%;
            height: auto;
        }

        code {
            background: #f5f5f5;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
        }
    </style>
</body>
</html>
```

### Use Case 3: Mobile-First Responsive Site
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>Mobile-First Design</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 16px;
        }

        /* Mobile First - Base styles */
        .container {
            width: 100%;
            padding: 0 16px;
            max-width: 100%;
        }

        .button, a {
            min-width: 44px;
            min-height: 44px;
            padding: 12px 16px;
            display: inline-block;
        }

        .grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 16px;
        }

        nav ul {
            display: flex;
            flex-direction: column;
            list-style: none;
        }

        nav a {
            display: block;
            padding: 16px;
            text-decoration: none;
            border-bottom: 1px solid #eee;
        }

        /* Tablet: 768px+ */
        @media (min-width: 768px) {
            .container {
                max-width: 720px;
                margin: 0 auto;
            }

            .grid {
                grid-template-columns: repeat(2, 1fr);
            }

            nav ul {
                flex-direction: row;
            }

            nav a {
                border-bottom: none;
                border-right: 1px solid #eee;
            }
        }

        /* Desktop: 1024px+ */
        @media (min-width: 1024px) {
            .container {
                max-width: 960px;
            }

            .grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        /* Large Desktop: 1440px+ */
        @media (min-width: 1440px) {
            .container {
                max-width: 1200px;
            }

            .grid {
                grid-template-columns: repeat(4, 1fr);
            }
        }

        /* Print styles */
        @media print {
            nav, aside, .no-print {
                display: none;
            }

            article {
                max-width: 100%;
                font-size: 12pt;
            }
        }

        /* Dark mode */
        @media (prefers-color-scheme: dark) {
            body {
                background: #1a1a1a;
                color: #fff;
            }

            nav a {
                border-color: #333;
            }
        }

        /* Accessibility: Reduce motion */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Mobile-First Site</h1>
            <nav aria-label="Main Navigation">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/services">Services</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
        </header>

        <main id="main-content">
            <div class="grid">
                <div>Item 1</div>
                <div>Item 2</div>
                <div>Item 3</div>
            </div>
        </main>

        <footer>
            <p>&copy; 2024. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>
```

### Use Case 4: Form with Comprehensive Validation
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Advanced Form</title>
    <style>
        form { max-width: 600px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; font-weight: bold; }
        input, select, textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            font-family: inherit;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        .error {
            color: #f44336;
            font-size: 14px;
            margin-top: 4px;
        }
        .success {
            background: #4CAF50;
            color: white;
            padding: 16px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <form id="contactForm" novalidate>
        <div id="successMessage" class="success" style="display: none;"></div>

        <div class="form-group">
            <label for="name">Họ tên:</label>
            <input type="text" id="name" name="name" required minlength="3">
            <div class="error" id="nameError"></div>
        </div>

        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <div class="error" id="emailError"></div>
        </div>

        <div class="form-group">
            <label for="phone">Điện thoại:</label>
            <input type="tel" id="phone" name="phone" pattern="[0-9\-\+\(\)\s]+" required>
            <div class="error" id="phoneError"></div>
        </div>

        <div class="form-group">
            <label for="message">Tin nhắn:</label>
            <textarea id="message" name="message" rows="5" required minlength="10"></textarea>
            <div class="error" id="messageError"></div>
        </div>

        <button type="submit">Gửi</button>
        <button type="reset" style="margin-left: 10px;">Xóa</button>
    </form>

    <script>
        const form = document.getElementById('contactForm');

        // Validation rules
        const validators = {
            name: (value) => {
                if (!value.trim()) return 'Vui lòng nhập họ tên';
                if (value.length < 3) return 'Họ tên phải ít nhất 3 ký tự';
                return '';
            },
            email: (value) => {
                const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!value) return 'Vui lòng nhập email';
                if (!regex.test(value)) return 'Email không hợp lệ';
                return '';
            },
            phone: (value) => {
                const regex = /^[\d\-\+\(\)\s]+$/;
                if (!value) return 'Vui lòng nhập số điện thoại';
                if (!regex.test(value)) return 'Số điện thoại không hợp lệ';
                return '';
            },
            message: (value) => {
                if (!value.trim()) return 'Vui lòng nhập tin nhắn';
                if (value.length < 10) return 'Tin nhắn phải ít nhất 10 ký tự';
                return '';
            }
        };

        // Validate single field
        function validateField(name, value) {
            const error = validators[name](value);
            const errorEl = document.getElementById(`${name}Error`);

            if (error) {
                errorEl.textContent = error;
                return false;
            } else {
                errorEl.textContent = '';
                return true;
            }
        }

        // Validate on blur
        Object.keys(validators).forEach(name => {
            const input = document.getElementById(name);
            input.addEventListener('blur', () => {
                validateField(name, input.value);
            });
        });

        // Form submission
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            // Validate all fields
            let isValid = true;
            Object.keys(validators).forEach(name => {
                const input = document.getElementById(name);
                if (!validateField(name, input.value)) {
                    isValid = false;
                }
            });

            if (isValid) {
                // Submit to server
                const data = new FormData(form);
                fetch('/api/contact', {
                    method: 'POST',
                    body: data
                })
                .then(r => r.json())
                .then(result => {
                    document.getElementById('successMessage').textContent = 'Gửi thành công!';
                    document.getElementById('successMessage').style.display = 'block';
                    form.reset();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        });
    </script>
</body>
</html>
```

### Use Case 5: Progressive Web App Manifest
```json
{
  "name": "My Progressive Web App",
  "short_name": "MyPWA",
  "description": "A complete progressive web application",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "theme_color": "#667eea",
  "background_color": "#ffffff",
  "orientation": "portrait-primary",
  "icons": [
    {
      "src": "/images/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/images/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/images/icon-maskable-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable"
    }
  ],
  "categories": ["productivity", "utilities"],
  "screenshots": [
    {
      "src": "/images/screenshot1.png",
      "sizes": "540x720",
      "type": "image/png"
    },
    {
      "src": "/images/screenshot2.png",
      "sizes": "540x720",
      "type": "image/png"
    }
  ],
  "shortcuts": [
    {
      "name": "Create Note",
      "short_name": "New Note",
      "description": "Create a new note quickly",
      "url": "/new-note",
      "icons": [{ "src": "/images/new-note.png", "sizes": "192x192" }]
    }
  ]
}
```

## 12.9. Tips & Tricks

### Tip 1: Critical CSS Optimization
```html
<head>
    <!-- Critical CSS inline -->
    <style>
        /* Only critical styles needed for above-the-fold content */
        body { margin: 0; font-family: Arial; }
        header { background: #667eea; color: white; }
        h1 { font-size: 32px; }
    </style>

    <!-- Defer non-critical CSS -->
    <link rel="preload" href="styles.css" as="style">
    <link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'">

    <!-- Fallback for older browsers -->
    <noscript>
        <link rel="stylesheet" href="styles.css">
    </noscript>
</head>
```

### Tip 2: Resource Hints for Performance
```html
<head>
    <!-- Preload critical resources -->
    <link rel="preload" href="fonts/main.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="css/critical.css" as="style">

    <!-- Preconnect to external APIs -->
    <link rel="preconnect" href="https://api.example.com">
    <link rel="dns-prefetch" href="https://cdn.example.com">

    <!-- Prefetch non-critical resources -->
    <link rel="prefetch" href="next-page.html">
    <link rel="prefetch" href="images/future-image.jpg">
</head>
```

### Tip 3: Web Font Optimization
```html
<head>
    <style>
        @font-face {
            font-family: 'CustomFont';
            src: url('font.woff2') format('woff2'),
                 url('font.woff') format('woff');
            font-display: swap; /* Show fallback immediately */
            font-weight: normal;
            font-style: normal;
        }

        @font-face {
            font-family: 'CustomFont';
            src: url('font-bold.woff2') format('woff2');
            font-weight: bold;
            font-display: swap;
        }

        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
        h1, h2, h3 { font-family: 'CustomFont', sans-serif; }
    </style>

    <!-- Or use system fonts -->
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
    </style>
</head>
```

### Tip 4: Image Optimization Strategy
```html
<!-- Use picture for art direction -->
<picture>
    <!-- Modern format for modern browsers -->
    <source media="(min-width: 1200px)" srcset="large.avif" type="image/avif">
    <source media="(min-width: 1200px)" srcset="large.webp" type="image/webp">

    <!-- Medium size -->
    <source media="(min-width: 768px)" srcset="medium.webp" type="image/webp">

    <!-- Mobile first -->
    <source srcset="small.webp" type="image/webp">

    <!-- Fallback -->
    <img src="fallback.jpg" alt="Responsive image" loading="lazy" width="1200" height="800">
</picture>
```

### Tip 5: Attribute Optimization
```html
<!-- Eager load for above-fold -->
<img src="hero.jpg" alt="Hero" loading="eager" fetchpriority="high" width="1200" height="400">

<!-- Lazy load for below-fold -->
<img src="gallery.jpg" alt="Gallery" loading="lazy" width="400" height="300">

<!-- Async decoding for performance -->
<img src="large.jpg" alt="Large" decoding="async" loading="lazy">

<!-- Async script for non-critical JS -->
<script src="analytics.js" async></script>

<!-- Defer script for DOM-dependent JS -->
<script src="app.js" defer></script>
```

### Tip 6: Form Performance
```html
<!-- Disable autocomplete if sensitive -->
<input type="password" autocomplete="off">

<!-- Use correct input types for mobile keyboards -->
<input type="email" placeholder="Email">
<input type="tel" placeholder="Phone">
<input type="date" placeholder="Date">
<input type="number" placeholder="Amount">
<input type="search" placeholder="Search">

<!-- Prevent auto-zoom on input focus (16px font) -->
<input type="text" style="font-size: 16px;">
```

### Tip 7: Viewport Size Classes
```css
/* CSS variables for responsive design */
:root {
    --mobile: 320px;
    --tablet: 768px;
    --desktop: 1024px;
    --large: 1440px;
}

@media (max-width: 767px) {
    body.mobile-view { /* Show mobile menu */ }
}

@media (min-width: 768px) and (max-width: 1023px) {
    body.tablet-view { /* Tablet layout */ }
}

@media (min-width: 1024px) {
    body.desktop-view { /* Desktop layout */ }
}
```

### Tip 8: Lazy Loading Best Practices
```html
<!-- Intersection Observer for more control -->
<script>
const images = document.querySelectorAll('img[data-src]');

const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
            observer.unobserve(img);
        }
    });
}, {
    rootMargin: '50px'
});

images.forEach(img => imageObserver.observe(img));
</script>

<!-- Native lazy loading as fallback -->
<img src="placeholder.jpg" data-src="actual.jpg" loading="lazy" alt="Image">
```

### Tip 9: CSS Sprites for Icons
```css
/* Combine multiple images into one */
.icon {
    background-image: url('sprites.png');
    background-repeat: no-repeat;
}

.icon-home {
    background-position: 0 0;
    width: 32px;
    height: 32px;
}

.icon-search {
    background-position: -32px 0;
    width: 32px;
    height: 32px;
}

.icon-menu {
    background-position: -64px 0;
    width: 32px;
    height: 32px;
}
```

### Tip 10: Minification and Compression
```html
<!-- Enable gzip compression on server -->
<!-- HTML minification -->
<!-- Remove unnecessary attributes and whitespace -->

<!-- CSS minification -->
<link rel="stylesheet" href="styles.min.css">

<!-- JS minification -->
<script src="app.min.js"></script>

<!-- Inline small CSS/JS to reduce requests -->
<style>
    .critical { /* Critical styles */ }
</style>
```

## 12.10. Common Mistakes

### Mistake 1: Not Optimizing Images
```html
<!-- Lỗi -->
<img src="huge-5mb-photo.jpg" alt="Photo">

<!-- Đúng -->
<picture>
    <source srcset="photo.webp" type="image/webp">
    <img src="photo.jpg" alt="Photo" loading="lazy" width="800" height="600">
</picture>
```

### Mistake 2: Blocking Render with CSS/JS
```html
<!-- Lỗi -->
<link rel="stylesheet" href="all-styles.css">
<script src="all-scripts.js"></script>

<!-- Đúng -->
<style>/* Critical CSS inline */</style>
<link rel="stylesheet" href="styles.min.css" media="print" onload="this.media='all'">
<script src="app.min.js" defer></script>
```

### Mistake 3: Poor Font Strategy
```html
<!-- Lỗi -->
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700" rel="stylesheet">

<!-- Đúng -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
```

### Mistake 4: Missing Alt Text
```html
<!-- Lỗi -->
<img src="product.jpg">

<!-- Đúng -->
<img src="product.jpg" alt="Blue wireless headphones, side view">

<!-- Decorative images -->
<img src="border.png" alt="" role="presentation">
```

### Mistake 5: Not Setting Viewport
```html
<!-- Lỗi -->
<!DOCTYPE html>
<html>

<!-- Đúng -->
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

### Mistake 6: JavaScript in Head
```html
<!-- Lỗi -->
<head>
    <script src="large-script.js"></script>
</head>
<body>...</body>

<!-- Đúng -->
<body>
    ...
    <script src="app.js" defer></script>
</body>
```

### Mistake 7: External Links Without Security
```html
<!-- Lỗi -->
<a href="https://external-site.com" target="_blank">Link</a>

<!-- Đúng -->
<a href="https://external-site.com" target="_blank" rel="noopener noreferrer">Link</a>
```

### Mistake 8: No Form Validation
```html
<!-- Lỗi -->
<form action="/submit">
    <input type="text" name="email">
</form>

<!-- Đúng -->
<form action="/submit" novalidate>
    <input type="email" name="email" required pattern="[^@]+@[^@]+\.[^@]+">
</form>
```

### Mistake 9: Ignoring Mobile Users
```html
<!-- Lỗi -->
<div style="width: 1200px;">Desktop only</div>

<!-- Đúng -->
<div style="width: 100%; max-width: 1200px;">Responsive</div>
```

### Mistake 10: Inline Styles
```html
<!-- Lỗi -->
<h1 style="color: red; font-size: 32px; margin: 20px;">Title</h1>

<!-- Đúng -->
<h1 class="page-title">Title</h1>
<style>
    .page-title {
        color: red;
        font-size: 32px;
        margin: 20px;
    }
</style>
```

## 12.11. Troubleshooting

### Issue 1: Low Lighthouse Score
**Giải pháp:**
- Optimize images aggressively
- Minify CSS/JS
- Reduce render-blocking resources
- Implement caching strategy

### Issue 2: FOUC (Flash of Unstyled Content)
**Giải pháp:**
```html
<style>
    html { visibility: hidden; }
</style>

<link rel="stylesheet" href="styles.css" onload="document.documentElement.style.visibility='visible'">

<noscript>
    <style>
        html { visibility: visible; }
    </style>
</noscript>
```

### Issue 3: Layout Shift
**Giải pháp:**
```html
<!-- Set explicit dimensions -->
<img src="image.jpg" width="800" height="600" alt="Image">
<video width="640" height="360"></video>
<div style="aspect-ratio: 16/9;"></div>
```

### Issue 4: Slow Page Load
**Giải pháp:**
- Enable compression (gzip, brotli)
- Use CDN for assets
- Implement caching headers
- Optimize critical rendering path

### Issue 5: Poor Accessibility
**Giải pháp:**
```html
<!-- Add ARIA labels -->
<nav aria-label="Main Navigation">
<button aria-label="Close Menu">×</button>
<img alt="Descriptive text">
<label for="input">Label Text</label>
```

### Issue 6: SEO Issues
**Giải pháp:**
```html
<title>Unique, descriptive title</title>
<meta name="description" content="150-160 characters">
<link rel="canonical" href="https://example.com/page">
<script type="application/ld+json">Structured data</script>
```

### Issue 7: Third-party Script Performance
**Giải pháp:**
```html
<!-- Load third-party scripts asynchronously -->
<script src="analytics.js" async></script>

<!-- Or use facade/placeholder -->
<div id="youtube-placeholder" onclick="loadYouTube()"></div>
```

### Issue 8: Font Loading Issues
**Giải pháp:**
```css
@font-face {
    font-display: swap; /* Show fallback immediately */
}

/* Ensure fallback fonts are web-safe */
font-family: 'CustomFont', -apple-system, sans-serif;
```

### Issue 9: Mobile Rendering Issues
**Giải pháp:**
```html
<!-- Ensure proper viewport -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">

<!-- Use min-height: 44px for touch targets -->
<button style="min-height: 44px;">Button</button>

<!-- Font size >= 16px prevents iOS zoom -->
<input type="text" style="font-size: 16px;">
```

### Issue 10: HTTPS/Mixed Content
**Giải pháp:**
```html
<!-- Use HTTPS for all resources -->
<img src="https://cdn.example.com/image.jpg">

<!-- Or use protocol-relative URLs -->
<img src="//cdn.example.com/image.jpg">
```

## 12.12. Advanced Topics

### Topic 1: Build Optimization Pipeline
```bash
# Webpack configuration for optimization
{
  entry: 'src/index.js',
  output: {
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].js'
  },
  optimization: {
    minimize: true,
    splitChunks: {
      chunks: 'all'
    }
  },
  plugins: [
    new TerserPlugin(), // JS minification
    new CssMinimizerPlugin(), // CSS minification
    new ImageMinimizerPlugin(), // Image compression
    new CompressionPlugin() // Gzip compression
  ]
}
```

### Topic 2: Core Web Vitals Optimization
```javascript
// Measure Core Web Vitals
const getCWVMetrics = () => {
    // Largest Contentful Paint (LCP)
    const observer = new PerformanceObserver((list) => {
        list.getEntries().forEach(entry => {
            console.log('LCP:', entry.renderTime || entry.loadTime);
        });
    });
    observer.observe({ entryTypes: ['largest-contentful-paint'] });

    // First Input Delay (FID) / Interaction to Next Paint (INP)
    const fidObserver = new PerformanceObserver((list) => {
        list.getEntries().forEach(entry => {
            console.log('FID:', entry.processingDuration);
        });
    });
    fidObserver.observe({ entryTypes: ['first-input'] });

    // Cumulative Layout Shift (CLS)
    let clsValue = 0;
    const clsObserver = new PerformanceObserver((list) => {
        list.getEntries().forEach(entry => {
            if (!entry.hadRecentInput) {
                clsValue += entry.value;
                console.log('CLS:', clsValue);
            }
        });
    });
    clsObserver.observe({ entryTypes: ['layout-shift'] });
};
```

### Topic 3: Service Worker Cache Strategy
```javascript
// Network First, Cache Fallback
self.addEventListener('fetch', event => {
    if (event.request.method !== 'GET') {
        return;
    }

    event.respondWith(
        fetch(event.request)
            .then(response => {
                if (response.status === 200) {
                    const responseClone = response.clone();
                    caches.open('v1').then(cache => {
                        cache.put(event.request, responseClone);
                    });
                }
                return response;
            })
            .catch(() => caches.match(event.request))
    );
});
```

### Topic 4: Critical Resource Hints
```html
<head>
    <!-- Preload critical resources -->
    <link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="critical.css" as="style">
    <link rel="preload" href="critical.js" as="script">

    <!-- Preconnect to critical origins -->
    <link rel="preconnect" href="https://cdn.example.com">
    <link rel="preconnect" href="https://api.example.com">

    <!-- DNS prefetch for secondary origins -->
    <link rel="dns-prefetch" href="https://analytics.example.com">
</head>
```

### Topic 5: Performance Monitoring
```javascript
// Real User Monitoring (RUM)
const rum = {
    recordMetrics() {
        // Navigation timing
        window.addEventListener('load', () => {
            const navigation = performance.getEntriesByType('navigation')[0];
            console.log({
                FCP: navigation.domInteractive - navigation.fetchStart,
                LCP: navigation.loadEventEnd - navigation.fetchStart,
                TTI: navigation.domInteractive - navigation.fetchStart
            });
        });

        // Resource timing
        const resources = performance.getEntriesByType('resource');
        resources.forEach(resource => {
            console.log(`${resource.name}: ${resource.duration}ms`);
        });
    }
};

rum.recordMetrics();
```

## 12.13. Bài tập thực hành

### Bài 1 (Dễ): HTML Validation
Yêu cầu: Validate HTML file sử dụng W3C Validator

### Bài 2 (Dễ): Accessibility Audit
Yêu cầu: Check accessibility với WAVE tool

### Bài 3 (Dễ): Mobile Responsiveness
Yêu cầu: Test site trên 3 devices khác nhau

### Bài 4 (Dễ): Performance Baseline
Yêu cầu: Run Lighthouse, record baseline scores

### Bài 5 (Trung bình): Image Optimization
Yêu cầu: Optimize 10 images, measure size reduction

### Bài 6 (Trung bình): Responsive Design
Yêu cầu: Create responsive site, 3+ breakpoints

### Bài 7 (Trung bình): SEO Optimization
Yêu cầu: Add meta tags, structured data, sitemap

### Bài 8 (Trung bình): Form Validation
Yêu cầu: Create form with validation, accessibility

### Bài 9 (Trung bình): Performance Audit
Yêu cầu: Identify bottlenecks, improve metrics

### Bài 10 (Khó): Full Page Optimization
Yêu cầu: Optimize entire page, target 90+ Lighthouse

### Bài 11 (Khó): PWA Implementation
Yêu cầu: Create PWA with manifest, Service Worker

### Bài 12 (Khó): Monitoring Setup
Yêu cầu: Setup RUM, track Core Web Vitals

---

## 12.8. Checklist

### 12.8.1. Before Launch

**HTML:**
- [ ] Valid HTML
- [ ] Semantic elements
- [ ] Proper heading hierarchy
- [ ] All images have alt text
- [ ] Forms have labels

**Performance:**
- [ ] Images optimized
- [ ] CSS/JS minified
- [ ] Lazy loading enabled
- [ ] Caching configured

**SEO:**
- [ ] Title và meta description
- [ ] Structured data
- [ ] Sitemap.xml
- [ ] Robots.txt

**Accessibility:**
- [ ] Keyboard navigation works
- [ ] Color contrast OK
- [ ] Screen reader friendly
- [ ] ARIA labels where needed

**Security:**
- [ ] HTTPS enabled
- [ ] CSP configured
- [ ] External links with rel="noopener"
- [ ] Form validation

**Mobile:**
- [ ] Responsive design
- [ ] Touch-friendly targets
- [ ] Fast page load
- [ ] Works offline (if PWA)

## 12.9. Tools và Resources

### 12.9.1. Development Tools

- VS Code, Sublime Text
- Chrome DevTools
- Firefox Developer Tools

### 12.9.2. Testing Tools

- W3C Validator
- WAVE Accessibility
- PageSpeed Insights
- Lighthouse

### 12.9.3. Optimization Tools

- TinyPNG (image compression)
- Squoosh (image converter)
- Webpack, Gulp (build tools)
- Terser (JS minification)

### 12.9.4. Learning Resources

- MDN Web Docs
- W3Schools
- Can I Use
- Web.dev

## 12.10. Future of HTML

### 12.10.1. Upcoming Features

- Native lazy loading improvements
- Better form controls
- Enhanced media capabilities
- More semantic elements

### 12.10.2. Modern Web Standards

- Web Components
- Shadow DOM
- Custom Elements
- ES Modules in HTML

## 12.11. Tổng kết

**Key Takeaways:**

1. **Semantic HTML** - Dùng đúng elements cho đúng mục đích
2. **Accessibility** - Trang web cho tất cả mọi người
3. **Performance** - Optimize images, code, resources
4. **SEO** - Meta tags, structured data, semantic markup
5. **Mobile-First** - Responsive, touch-friendly
6. **Security** - Validate input, secure forms, HTTPS
7. **Best Practices** - Clean code, validation, testing

**Remember:**
- Write HTML for humans and machines
- Test on real devices
- Keep learning and improving
- Follow web standards

---

**KẾT THÚC TÀI LIỆU HTML5**

Chúc bạn thành công trong việc học và áp dụng HTML5!
