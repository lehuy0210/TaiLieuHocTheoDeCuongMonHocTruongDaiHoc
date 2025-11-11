# CHƯƠNG 4: LINKS VÀ NAVIGATION

## 4.1. Thẻ Anchor `<a>`

### 4.1.1. Cú pháp cơ bản

```html
<a href="URL">Link Text</a>
```

### 4.1.2. Các loại links

#### External Links (Links ra ngoài)
```html
<a href="https://www.google.com">Google</a>
<a href="https://github.com">GitHub</a>
```

#### Internal Links (Links trong cùng website)
```html
<!-- Absolute path -->
<a href="/about.html">About Us</a>
<a href="/products/laptop.html">Laptops</a>

<!-- Relative path -->
<a href="about.html">About</a>
<a href="../index.html">Home</a>
<a href="./contact.html">Contact</a>
```

#### Same Page Links (Anchor links)
```html
<a href="#section1">Go to Section 1</a>
<a href="#footer">Go to Footer</a>

<!-- Target elements -->
<h2 id="section1">Section 1</h2>
<footer id="footer">Footer content</footer>

<!-- Back to top -->
<a href="#top">Back to Top</a>
<a href="#">Back to Top</a>
```

## 4.2. Attributes của `<a>`

### 4.2.1. href - Hypertext Reference

**Các giá trị của href:**

```html
<!-- URL -->
<a href="https://example.com">Website</a>

<!-- Email -->
<a href="mailto:info@example.com">Send Email</a>

<!-- Phone -->
<a href="tel:+84123456789">Call Us</a>

<!-- SMS -->
<a href="sms:+84123456789">Send SMS</a>

<!-- Download -->
<a href="document.pdf" download>Download PDF</a>

<!-- JavaScript -->
<a href="javascript:void(0)" onclick="myFunction()">Click</a>

<!-- Anchor -->
<a href="#section">Jump to Section</a>

<!-- No link -->
<a>Not a link</a>
```

### 4.2.2. target - Nơi mở link

```html
<!-- Mở trong tab/window mới -->
<a href="https://example.com" target="_blank">Open in New Tab</a>

<!-- Mở trong cùng tab (mặc định) -->
<a href="page.html" target="_self">Open in Same Tab</a>

<!-- Mở trong parent frame -->
<a href="page.html" target="_parent">Open in Parent</a>

<!-- Mở trong top-level window -->
<a href="page.html" target="_top">Open in Top</a>

<!-- Mở trong named window/tab -->
<a href="page1.html" target="myWindow">Page 1</a>
<a href="page2.html" target="myWindow">Page 2</a>
```

### 4.2.3. rel - Relationship

**rel="noopener noreferrer"** (Bảo mật cho target="_blank"):
```html
<a href="https://external-site.com"
   target="_blank"
   rel="noopener noreferrer">
   External Site
</a>
```

**Các giá trị rel khác:**
```html
<!-- Không follow link (SEO) -->
<a href="https://example.com" rel="nofollow">Link</a>

<!-- Sponsored link -->
<a href="https://sponsor.com" rel="sponsored">Sponsor</a>

<!-- User-generated content -->
<a href="https://user-site.com" rel="ugc">User Link</a>

<!-- Alternate version -->
<a href="page-fr.html" rel="alternate" hreflang="fr">French Version</a>

<!-- Author -->
<a href="https://author.com" rel="author">Author Profile</a>

<!-- License -->
<a href="license.html" rel="license">License</a>

<!-- Previous/Next -->
<a href="page1.html" rel="prev">Previous</a>
<a href="page3.html" rel="next">Next</a>
```

### 4.2.4. download - Tải file

```html
<!-- Download với tên gốc -->
<a href="document.pdf" download>Download PDF</a>

<!-- Download với tên mới -->
<a href="document.pdf" download="my-document.pdf">Download</a>

<!-- Download image -->
<a href="image.jpg" download="my-image.jpg">Download Image</a>
```

### 4.2.5. hreflang - Ngôn ngữ

```html
<a href="https://example.com/en" hreflang="en">English</a>
<a href="https://example.com/vi" hreflang="vi">Tiếng Việt</a>
<a href="https://example.com/fr" hreflang="fr">Français</a>
```

### 4.2.6. title - Tooltip

```html
<a href="page.html" title="Go to this page">Link</a>
<a href="document.pdf" title="PDF, 2.5MB">Download</a>
```

## 4.3. Email và Telephone Links

### 4.3.1. Email Links

**Basic email:**
```html
<a href="mailto:info@example.com">Email Us</a>
```

**Email với subject:**
```html
<a href="mailto:info@example.com?subject=Hello">Email with Subject</a>
```

**Email với CC và BCC:**
```html
<a href="mailto:info@example.com?cc=admin@example.com&bcc=boss@example.com">
    Email with CC/BCC
</a>
```

**Email với body:**
```html
<a href="mailto:info@example.com?subject=Feedback&body=Hello,%0D%0A%0D%0AI want to...">
    Send Feedback
</a>
```

**Multiple recipients:**
```html
<a href="mailto:info@example.com,support@example.com">Email Multiple</a>
```

**Complete example:**
```html
<a href="mailto:support@example.com?subject=Support Request&body=Please help with...&cc=admin@example.com">
    Contact Support
</a>
```

### 4.3.2. Telephone Links

**Basic phone:**
```html
<a href="tel:+84123456789">Call: 0123-456-789</a>
```

**International format:**
```html
<a href="tel:+1-555-123-4567">+1 (555) 123-4567</a>
```

**With extension:**
```html
<a href="tel:+84123456789,123">Call (ext. 123)</a>
```

### 4.3.3. SMS Links

```html
<a href="sms:+84123456789">Send SMS</a>

<!-- With body (iOS) -->
<a href="sms:+84123456789&body=Hello">Send SMS with Text</a>

<!-- Android -->
<a href="sms:+84123456789?body=Hello">Send SMS with Text</a>
```

### 4.3.4. Other Protocol Links

**FTP:**
```html
<a href="ftp://ftp.example.com/file.zip">Download via FTP</a>
```

**WhatsApp:**
```html
<a href="https://wa.me/84123456789">Chat on WhatsApp</a>
<a href="https://wa.me/84123456789?text=Hello">WhatsApp with Message</a>
```

**Skype:**
```html
<a href="skype:username?call">Call on Skype</a>
<a href="skype:username?chat">Chat on Skype</a>
```

## 4.4. Navigation Elements

### 4.4.1. Thẻ `<nav>`

```html
<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</nav>
```

### 4.4.2. Horizontal Navigation

```html
<nav>
    <ul class="horizontal-menu">
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</nav>

<style>
.horizontal-menu {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
}

.horizontal-menu li {
    margin-right: 20px;
}

.horizontal-menu a {
    text-decoration: none;
    padding: 10px 15px;
    display: block;
}
</style>
```

### 4.4.3. Dropdown Navigation

```html
<nav>
    <ul class="menu">
        <li><a href="/">Home</a></li>
        <li class="dropdown">
            <a href="/products">Products</a>
            <ul class="submenu">
                <li><a href="/products/laptops">Laptops</a></li>
                <li><a href="/products/phones">Phones</a></li>
                <li><a href="/products/tablets">Tablets</a></li>
            </ul>
        </li>
        <li><a href="/about">About</a></li>
    </ul>
</nav>
```

### 4.4.4. Breadcrumb Navigation

```html
<nav aria-label="Breadcrumb">
    <ol class="breadcrumb">
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/products/laptops">Laptops</a></li>
        <li aria-current="page">Dell XPS 13</li>
    </ol>
</nav>

<style>
.breadcrumb {
    list-style: none;
    display: flex;
    padding: 0;
}

.breadcrumb li:not(:last-child)::after {
    content: " / ";
    margin: 0 5px;
}
</style>
```

### 4.4.5. Pagination

```html
<nav aria-label="Pagination">
    <ul class="pagination">
        <li><a href="?page=1" rel="prev">Previous</a></li>
        <li><a href="?page=1">1</a></li>
        <li><a href="?page=2" aria-current="page">2</a></li>
        <li><a href="?page=3">3</a></li>
        <li><a href="?page=4">4</a></li>
        <li><a href="?page=5">5</a></li>
        <li><a href="?page=3" rel="next">Next</a></li>
    </ul>
</nav>
```

### 4.4.6. Footer Navigation

```html
<footer>
    <nav aria-label="Footer Navigation">
        <div class="footer-links">
            <div class="footer-column">
                <h3>Company</h3>
                <ul>
                    <li><a href="/about">About Us</a></li>
                    <li><a href="/careers">Careers</a></li>
                    <li><a href="/press">Press</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Support</h3>
                <ul>
                    <li><a href="/help">Help Center</a></li>
                    <li><a href="/contact">Contact Us</a></li>
                    <li><a href="/faq">FAQ</a></li>
                </ul>
            </div>
        </div>
    </nav>
</footer>
```

## 4.5. Link States và Styling

### 4.5.1. CSS Pseudo-classes

```css
/* Unvisited link */
a:link {
    color: blue;
}

/* Visited link */
a:visited {
    color: purple;
}

/* Mouse hover */
a:hover {
    color: red;
    text-decoration: underline;
}

/* Active (being clicked) */
a:active {
    color: orange;
}

/* Focused (keyboard navigation) */
a:focus {
    outline: 2px solid blue;
}
```

### 4.5.2. Styling Examples

**Remove underline:**
```css
a {
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```

**Button-style link:**
```css
.btn-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
}

.btn-link:hover {
    background-color: #0056b3;
}
```

**Icon links:**
```html
<a href="/download" class="icon-link">
    <i class="icon-download"></i>
    Download
</a>
```

## 4.6. Accessibility Best Practices

### 4.6.1. Descriptive Link Text

**Tốt:**
```html
<a href="/products">View our products</a>
<a href="report.pdf">Download the annual report (PDF, 2MB)</a>
```

**Tránh:**
```html
<a href="/products">Click here</a>
<a href="report.pdf">Download</a>
```

### 4.6.2. External Link Indication

```html
<a href="https://external-site.com" target="_blank" rel="noopener">
    External Site <span class="sr-only">(opens in new tab)</span>
</a>

<style>
.sr-only {
    position: absolute;
    left: -10000px;
    width: 1px;
    height: 1px;
    overflow: hidden;
}
</style>
```

### 4.6.3. aria-label và aria-labelledby

```html
<!-- aria-label -->
<a href="#" aria-label="Close dialog">
    <span aria-hidden="true">×</span>
</a>

<!-- aria-labelledby -->
<h2 id="section-title">Products</h2>
<a href="/products" aria-labelledby="section-title">View all</a>
```

### 4.6.4. Skip Links

```html
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <nav><!-- Navigation --></nav>

    <main id="main-content">
        <!-- Main content -->
    </main>
</body>

<style>
.skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: #000;
    color: #fff;
    padding: 8px;
    z-index: 100;
}

.skip-link:focus {
    top: 0;
}
</style>
```

## 4.7. Advanced Link Techniques

### 4.7.1. Image Links

```html
<a href="/products">
    <img src="product.jpg" alt="View our products">
</a>
```

### 4.7.2. Block-level Links (HTML5)

```html
<a href="/article">
    <article>
        <h2>Article Title</h2>
        <p>Article description...</p>
        <img src="thumbnail.jpg" alt="Article image">
    </article>
</a>
```

### 4.7.3. Base URL

```html
<head>
    <base href="https://www.example.com/" target="_blank">
</head>
<body>
    <!-- Tất cả links sẽ relative to base URL -->
    <a href="products">Products</a>
    <!-- Becomes: https://www.example.com/products -->
</body>
```

### 4.7.4. Link Prefetching

```html
<!-- Prefetch -->
<link rel="prefetch" href="next-page.html">

<!-- Preload -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>

<!-- Preconnect -->
<link rel="preconnect" href="https://fonts.googleapis.com">

<!-- DNS Prefetch -->
<link rel="dns-prefetch" href="https://external-site.com">
```

## 4.8. Navigation Patterns

### 4.8.1. Mega Menu

```html
<nav class="mega-menu">
    <ul class="main-menu">
        <li>
            <a href="/products">Products</a>
            <div class="mega-dropdown">
                <div class="mega-column">
                    <h3>Laptops</h3>
                    <ul>
                        <li><a href="/laptops/dell">Dell</a></li>
                        <li><a href="/laptops/hp">HP</a></li>
                        <li><a href="/laptops/lenovo">Lenovo</a></li>
                    </ul>
                </div>
                <div class="mega-column">
                    <h3>Phones</h3>
                    <ul>
                        <li><a href="/phones/iphone">iPhone</a></li>
                        <li><a href="/phones/samsung">Samsung</a></li>
                        <li><a href="/phones/xiaomi">Xiaomi</a></li>
                    </ul>
                </div>
            </div>
        </li>
    </ul>
</nav>
```

### 4.8.2. Mobile Navigation (Hamburger)

```html
<nav class="mobile-nav">
    <button class="hamburger" aria-label="Toggle menu">
        <span></span>
        <span></span>
        <span></span>
    </button>

    <ul class="mobile-menu">
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</nav>
```

### 4.8.3. Tab Navigation

```html
<nav class="tabs">
    <ul role="tablist">
        <li role="presentation">
            <a href="#tab1" role="tab" aria-selected="true">Tab 1</a>
        </li>
        <li role="presentation">
            <a href="#tab2" role="tab">Tab 2</a>
        </li>
        <li role="presentation">
            <a href="#tab3" role="tab">Tab 3</a>
        </li>
    </ul>
</nav>

<div id="tab1" role="tabpanel">Tab 1 content</div>
<div id="tab2" role="tabpanel" hidden>Tab 2 content</div>
<div id="tab3" role="tabpanel" hidden>Tab 3 content</div>
```

## 4.9. SEO Best Practices

### 4.9.1. Internal Linking

```html
<!-- Liên kết các trang liên quan -->
<article>
    <h1>HTML5 Tutorial</h1>
    <p>Learn about <a href="/html5-semantic">semantic elements</a>...</p>
    <p>Related: <a href="/css3-tutorial">CSS3 Tutorial</a></p>
</article>
```

### 4.9.2. Anchor Text Optimization

```html
<!-- Tốt - descriptive anchor text -->
<a href="/html5-course">HTML5 complete course</a>

<!-- Tránh - generic anchor text -->
<a href="/html5-course">click here</a>
```

### 4.9.3. Canonical Links

```html
<head>
    <link rel="canonical" href="https://www.example.com/page">
</head>
```

## 4.10. Practical Examples

### 4.10.1. Complete Header Navigation

```html
<header>
    <div class="logo">
        <a href="/">
            <img src="logo.png" alt="Company Logo">
        </a>
    </div>

    <nav aria-label="Main Navigation">
        <ul class="main-menu">
            <li><a href="/" aria-current="page">Home</a></li>
            <li><a href="/about">About</a></li>
            <li class="has-dropdown">
                <a href="/services">Services</a>
                <ul class="dropdown">
                    <li><a href="/services/web-design">Web Design</a></li>
                    <li><a href="/services/seo">SEO</a></li>
                    <li><a href="/services/marketing">Marketing</a></li>
                </ul>
            </li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </nav>
</header>
```

### 4.10.2. Complete Footer

```html
<footer>
    <div class="footer-content">
        <div class="footer-section">
            <h3>About Us</h3>
            <p>Company description...</p>
        </div>

        <nav class="footer-section" aria-label="Footer Navigation">
            <h3>Quick Links</h3>
            <ul>
                <li><a href="/about">About</a></li>
                <li><a href="/services">Services</a></li>
                <li><a href="/blog">Blog</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>

        <div class="footer-section">
            <h3>Contact</h3>
            <address>
                <p><a href="tel:+84123456789">0123-456-789</a></p>
                <p><a href="mailto:info@example.com">info@example.com</a></p>
            </address>
        </div>

        <div class="footer-section">
            <h3>Follow Us</h3>
            <ul class="social-links">
                <li>
                    <a href="https://facebook.com/company"
                       target="_blank"
                       rel="noopener"
                       aria-label="Facebook">
                        Facebook
                    </a>
                </li>
                <li>
                    <a href="https://twitter.com/company"
                       target="_blank"
                       rel="noopener"
                       aria-label="Twitter">
                        Twitter
                    </a>
                </li>
            </ul>
        </div>
    </div>

    <div class="footer-bottom">
        <p>&copy; 2024 Company Name. All rights reserved.</p>
        <nav aria-label="Legal">
            <a href="/privacy">Privacy Policy</a> |
            <a href="/terms">Terms of Service</a>
        </nav>
    </div>
</footer>
```

## 4.11. Bài tập thực hành

### Bài 1: Basic Links
Tạo trang với:
- External links
- Internal links
- Email và telephone links
- Anchor links
- Download links

### Bài 2: Navigation Menu
Tạo:
- Horizontal navigation bar
- Dropdown menu
- Breadcrumb navigation
- Pagination

### Bài 3: Accessible Links
Tạo trang với:
- Descriptive link text
- Skip links
- ARIA labels
- External link indicators

### Bài 4: Complete Website Navigation
Tạo:
- Header với logo và main menu
- Footer với multiple sections
- Mobile-friendly menu
- Social media links

---

**Kết luận:** Trong chương này, chúng ta đã học về links và navigation trong HTML5, bao gồm cách tạo links, navigation patterns, accessibility, và SEO best practices. Chương tiếp theo sẽ tìm hiểu về Images và Multimedia.
