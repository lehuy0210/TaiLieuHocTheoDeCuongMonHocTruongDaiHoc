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
