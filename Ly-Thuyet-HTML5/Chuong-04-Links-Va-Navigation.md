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

## 4.11. Practical Complete Examples

### 4.11.1. Landing Page Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Landing Page</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
        }

        .header {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            z-index: 1000;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 5%;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo a {
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            color: #333;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: #007bff;
        }

        .cta-button {
            background: #007bff;
            color: white !important;
            padding: 0.5rem 1.5rem;
            border-radius: 5px;
        }

        .cta-button:hover {
            background: #0056b3;
            color: white !important;
        }

        main {
            margin-top: 80px;
        }
    </style>
</head>
<body>
    <header class="header">
        <nav class="navbar" aria-label="Main Navigation">
            <div class="logo">
                <a href="#home">ProductName</a>
            </div>
            <ul class="nav-links">
                <li><a href="#features">Features</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><a href="#signup" class="cta-button">Get Started</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home">
            <h1>Welcome to Our Product</h1>
            <p>Amazing features for your business</p>
            <a href="#signup" class="cta-button">Start Free Trial</a>
        </section>

        <section id="features">
            <h2>Features</h2>
            <!-- Features content -->
        </section>

        <section id="pricing">
            <h2>Pricing</h2>
            <!-- Pricing content -->
        </section>

        <section id="testimonials">
            <h2>What Our Customers Say</h2>
            <!-- Testimonials content -->
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <!-- Contact form -->
        </section>
    </main>

    <footer>
        <nav aria-label="Footer Navigation">
            <a href="#privacy">Privacy Policy</a>
            <a href="#terms">Terms of Service</a>
        </nav>
        <p>&copy; 2024 ProductName. All rights reserved.</p>
    </footer>
</body>
</html>
```

### 4.11.2. Blog Navigation System

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Tech Blog</title>
    <style>
        .blog-header {
            background: #1a1a1a;
            color: white;
            padding: 1rem 0;
        }

        .blog-nav {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }

        .blog-nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .blog-nav a {
            color: white;
            text-decoration: none;
            padding: 0.5rem 1rem;
        }

        .blog-nav a:hover,
        .blog-nav a.active {
            background: #007bff;
            border-radius: 5px;
        }

        .breadcrumb {
            background: #f8f9fa;
            padding: 1rem 2rem;
        }

        .breadcrumb ol {
            list-style: none;
            display: flex;
            gap: 0.5rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .breadcrumb li:not(:last-child)::after {
            content: " / ";
            margin-left: 0.5rem;
            color: #6c757d;
        }

        .breadcrumb a {
            color: #007bff;
            text-decoration: none;
        }

        .breadcrumb a:hover {
            text-decoration: underline;
        }

        .sidebar-nav {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
        }

        .sidebar-nav h3 {
            margin-bottom: 1rem;
        }

        .sidebar-nav ul {
            list-style: none;
        }

        .sidebar-nav li {
            padding: 0.5rem 0;
            border-bottom: 1px solid #dee2e6;
        }

        .sidebar-nav a {
            color: #333;
            text-decoration: none;
        }

        .sidebar-nav a:hover {
            color: #007bff;
        }

        .pagination {
            display: flex;
            justify-content: center;
            list-style: none;
            gap: 0.5rem;
            margin: 2rem 0;
        }

        .pagination a {
            padding: 0.5rem 1rem;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            text-decoration: none;
            color: #007bff;
        }

        .pagination a:hover,
        .pagination a.active {
            background: #007bff;
            color: white;
        }

        .container {
            max-width: 1200px;
            margin: 2rem auto;
            display: grid;
            grid-template-columns: 3fr 1fr;
            gap: 2rem;
            padding: 0 2rem;
        }
    </style>
</head>
<body>
    <header class="blog-header">
        <nav class="blog-nav" aria-label="Main Navigation">
            <a href="/" class="logo">TechBlog</a>
            <ul>
                <li><a href="/" class="active">Home</a></li>
                <li><a href="/categories">Categories</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
            <form action="/search" method="GET" role="search">
                <input type="search" name="q" placeholder="Search...">
            </form>
        </nav>
    </header>

    <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
            <li><a href="/">Home</a></li>
            <li><a href="/categories">Categories</a></li>
            <li><a href="/categories/web-development">Web Development</a></li>
            <li aria-current="page">HTML5 Tutorial</li>
        </ol>
    </nav>

    <div class="container">
        <main>
            <article>
                <h1>Complete HTML5 Tutorial</h1>
                <p>Article content here...</p>
            </article>

            <nav class="pagination" aria-label="Pagination">
                <ul class="pagination">
                    <li><a href="?page=1" rel="prev">Previous</a></li>
                    <li><a href="?page=1">1</a></li>
                    <li><a href="?page=2" class="active" aria-current="page">2</a></li>
                    <li><a href="?page=3">3</a></li>
                    <li><a href="?page=4">4</a></li>
                    <li><a href="?page=5">5</a></li>
                    <li><a href="?page=3" rel="next">Next</a></li>
                </ul>
            </nav>
        </main>

        <aside>
            <nav class="sidebar-nav" aria-label="Categories">
                <h3>Categories</h3>
                <ul>
                    <li><a href="/categories/html">HTML (45)</a></li>
                    <li><a href="/categories/css">CSS (38)</a></li>
                    <li><a href="/categories/javascript">JavaScript (52)</a></li>
                    <li><a href="/categories/react">React (29)</a></li>
                </ul>
            </nav>

            <nav class="sidebar-nav" aria-label="Recent Posts">
                <h3>Recent Posts</h3>
                <ul>
                    <li><a href="/posts/1">Getting Started with HTML5</a></li>
                    <li><a href="/posts/2">CSS Grid Layout Guide</a></li>
                    <li><a href="/posts/3">JavaScript ES6 Features</a></li>
                </ul>
            </nav>
        </aside>
    </div>
</body>
</html>
```

### 4.11.3. E-commerce Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Online Store</title>
    <style>
        .top-bar {
            background: #f8f9fa;
            padding: 0.5rem 0;
            font-size: 0.875rem;
        }

        .top-bar-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            padding: 0 2rem;
        }

        .top-bar a {
            color: #6c757d;
            text-decoration: none;
            margin-right: 1rem;
        }

        .main-header {
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: grid;
            grid-template-columns: 200px 1fr auto;
            gap: 2rem;
            align-items: center;
        }

        .logo a {
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
            text-decoration: none;
        }

        .search-bar {
            position: relative;
        }

        .search-bar input {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 2px solid #dee2e6;
            border-radius: 5px;
        }

        .user-actions {
            display: flex;
            gap: 1.5rem;
        }

        .user-actions a {
            color: #333;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .main-nav {
            background: #007bff;
        }

        .main-nav ul {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            list-style: none;
        }

        .main-nav li {
            position: relative;
        }

        .main-nav > ul > li > a {
            display: block;
            padding: 1rem 1.5rem;
            color: white;
            text-decoration: none;
        }

        .main-nav a:hover {
            background: #0056b3;
        }

        .dropdown {
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            min-width: 200px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            display: none;
        }

        .main-nav li:hover .dropdown {
            display: block;
        }

        .dropdown a {
            display: block;
            padding: 0.75rem 1rem;
            color: #333;
            text-decoration: none;
            border-bottom: 1px solid #dee2e6;
        }

        .dropdown a:hover {
            background: #f8f9fa;
        }

        .product-breadcrumb {
            max-width: 1200px;
            margin: 1rem auto;
            padding: 0 2rem;
        }

        .product-breadcrumb ol {
            list-style: none;
            display: flex;
            gap: 0.5rem;
        }

        .product-breadcrumb li:not(:last-child)::after {
            content: "›";
            margin-left: 0.5rem;
            color: #6c757d;
        }

        .product-breadcrumb a {
            color: #007bff;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <!-- Top Bar -->
    <div class="top-bar">
        <div class="top-bar-content">
            <div>
                <a href="/help">Help</a>
                <a href="/track-order">Track Order</a>
                <a href="/stores">Store Locator</a>
            </div>
            <div>
                <a href="/account">My Account</a>
                <a href="/wishlist">Wishlist</a>
            </div>
        </div>
    </div>

    <!-- Main Header -->
    <header class="main-header">
        <div class="header-content">
            <div class="logo">
                <a href="/">StoreName</a>
            </div>

            <form class="search-bar" action="/search" method="GET" role="search">
                <input type="search" name="q" placeholder="Search for products...">
            </form>

            <div class="user-actions">
                <a href="/account">
                    <span>Account</span>
                </a>
                <a href="/wishlist">
                    <span>Wishlist (3)</span>
                </a>
                <a href="/cart">
                    <span>Cart (5)</span>
                </a>
            </div>
        </div>
    </header>

    <!-- Main Navigation -->
    <nav class="main-nav" aria-label="Main Navigation">
        <ul>
            <li>
                <a href="/categories">All Categories</a>
                <div class="dropdown">
                    <a href="/categories/electronics">Electronics</a>
                    <a href="/categories/fashion">Fashion</a>
                    <a href="/categories/home">Home & Garden</a>
                    <a href="/categories/sports">Sports</a>
                </div>
            </li>
            <li>
                <a href="/electronics">Electronics</a>
                <div class="dropdown">
                    <a href="/electronics/laptops">Laptops</a>
                    <a href="/electronics/phones">Smartphones</a>
                    <a href="/electronics/tablets">Tablets</a>
                    <a href="/electronics/accessories">Accessories</a>
                </div>
            </li>
            <li>
                <a href="/fashion">Fashion</a>
                <div class="dropdown">
                    <a href="/fashion/men">Men's Fashion</a>
                    <a href="/fashion/women">Women's Fashion</a>
                    <a href="/fashion/kids">Kids' Fashion</a>
                </div>
            </li>
            <li><a href="/deals">Today's Deals</a></li>
            <li><a href="/new-arrivals">New Arrivals</a></li>
        </ul>
    </nav>

    <!-- Breadcrumb -->
    <nav class="product-breadcrumb" aria-label="Breadcrumb">
        <ol>
            <li><a href="/">Home</a></li>
            <li><a href="/electronics">Electronics</a></li>
            <li><a href="/electronics/laptops">Laptops</a></li>
            <li aria-current="page">Dell XPS 13</li>
        </ol>
    </nav>

    <main>
        <!-- Product content -->
    </main>
</body>
</html>
```

### 4.11.4. Dashboard Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Admin Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
        }

        .dashboard {
            display: grid;
            grid-template-columns: 250px 1fr;
            grid-template-rows: 60px 1fr;
            height: 100vh;
        }

        .top-nav {
            grid-column: 1 / -1;
            background: #1a1a1a;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }

        .top-nav-left {
            display: flex;
            align-items: center;
            gap: 2rem;
        }

        .logo {
            font-size: 1.25rem;
            font-weight: bold;
        }

        .top-nav-right {
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }

        .top-nav a {
            color: white;
            text-decoration: none;
        }

        .sidebar {
            background: #2c3e50;
            color: white;
            overflow-y: auto;
        }

        .sidebar nav {
            padding: 1rem 0;
        }

        .nav-section {
            margin-bottom: 2rem;
        }

        .nav-section-title {
            padding: 0.5rem 1.5rem;
            font-size: 0.75rem;
            text-transform: uppercase;
            color: #95a5a6;
            font-weight: bold;
        }

        .sidebar ul {
            list-style: none;
        }

        .sidebar a {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 0.75rem 1.5rem;
            color: white;
            text-decoration: none;
            transition: background 0.3s;
        }

        .sidebar a:hover,
        .sidebar a.active {
            background: #34495e;
        }

        .main-content {
            background: #ecf0f1;
            padding: 2rem;
            overflow-y: auto;
        }

        .breadcrumb {
            margin-bottom: 1.5rem;
        }

        .breadcrumb ol {
            list-style: none;
            display: flex;
            gap: 0.5rem;
        }

        .breadcrumb li:not(:last-child)::after {
            content: "/";
            margin-left: 0.5rem;
            color: #95a5a6;
        }

        .breadcrumb a {
            color: #3498db;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <!-- Top Navigation -->
        <header class="top-nav">
            <div class="top-nav-left">
                <div class="logo">AdminPanel</div>
                <form action="/search" method="GET">
                    <input type="search" name="q" placeholder="Search...">
                </form>
            </div>
            <div class="top-nav-right">
                <a href="/notifications">Notifications (3)</a>
                <a href="/messages">Messages (5)</a>
                <a href="/profile">Profile</a>
                <a href="/logout">Logout</a>
            </div>
        </header>

        <!-- Sidebar Navigation -->
        <aside class="sidebar">
            <nav aria-label="Main Navigation">
                <div class="nav-section">
                    <div class="nav-section-title">Main</div>
                    <ul>
                        <li><a href="/dashboard" class="active">Dashboard</a></li>
                        <li><a href="/analytics">Analytics</a></li>
                        <li><a href="/reports">Reports</a></li>
                    </ul>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">Management</div>
                    <ul>
                        <li><a href="/users">Users</a></li>
                        <li><a href="/products">Products</a></li>
                        <li><a href="/orders">Orders</a></li>
                        <li><a href="/inventory">Inventory</a></li>
                    </ul>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">Content</div>
                    <ul>
                        <li><a href="/pages">Pages</a></li>
                        <li><a href="/blog">Blog</a></li>
                        <li><a href="/media">Media Library</a></li>
                    </ul>
                </div>

                <div class="nav-section">
                    <div class="nav-section-title">Settings</div>
                    <ul>
                        <li><a href="/settings">General Settings</a></li>
                        <li><a href="/settings/payment">Payment Settings</a></li>
                        <li><a href="/settings/shipping">Shipping</a></li>
                        <li><a href="/settings/email">Email</a></li>
                    </ul>
                </div>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <ol>
                    <li><a href="/dashboard">Dashboard</a></li>
                    <li><a href="/products">Products</a></li>
                    <li aria-current="page">Edit Product</li>
                </ol>
            </nav>

            <h1>Dashboard Content</h1>
            <!-- Dashboard content here -->
        </main>
    </div>
</body>
</html>
```

### 4.11.5. Portfolio Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>John Doe - Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
        }

        .nav-wrapper {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            z-index: 1000;
        }

        .portfolio-nav {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2rem;
        }

        .name a {
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
            text-decoration: none;
        }

        .nav-menu {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-menu a {
            color: #333;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
            position: relative;
        }

        .nav-menu a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: #007bff;
            transition: width 0.3s;
        }

        .nav-menu a:hover::after,
        .nav-menu a.active::after {
            width: 100%;
        }

        .social-links {
            display: flex;
            gap: 1rem;
        }

        .social-links a {
            color: #333;
            text-decoration: none;
        }

        main {
            margin-top: 80px;
        }

        section {
            min-height: 100vh;
            padding: 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-nav {
            position: fixed;
            right: 2rem;
            top: 50%;
            transform: translateY(-50%);
            z-index: 100;
        }

        .section-nav ul {
            list-style: none;
        }

        .section-nav li {
            margin: 1rem 0;
        }

        .section-nav a {
            display: block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #dee2e6;
            transition: all 0.3s;
        }

        .section-nav a:hover,
        .section-nav a.active {
            background: #007bff;
            transform: scale(1.3);
        }

        @media (max-width: 768px) {
            .nav-menu {
                display: none;
            }

            .hamburger {
                display: block;
                cursor: pointer;
            }
        }
    </style>
</head>
<body>
    <!-- Main Navigation -->
    <div class="nav-wrapper">
        <nav class="portfolio-nav" aria-label="Main Navigation">
            <div class="name">
                <a href="#home">John Doe</a>
            </div>

            <ul class="nav-menu">
                <li><a href="#home" class="active">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#experience">Experience</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>

            <div class="social-links">
                <a href="https://github.com/johndoe" target="_blank" rel="noopener" aria-label="GitHub">
                    GitHub
                </a>
                <a href="https://linkedin.com/in/johndoe" target="_blank" rel="noopener" aria-label="LinkedIn">
                    LinkedIn
                </a>
                <a href="https://twitter.com/johndoe" target="_blank" rel="noopener" aria-label="Twitter">
                    Twitter
                </a>
            </div>
        </nav>
    </div>

    <!-- Section Navigation (Dots) -->
    <nav class="section-nav" aria-label="Section Navigation">
        <ul>
            <li><a href="#home" class="active" title="Home"></a></li>
            <li><a href="#about" title="About"></a></li>
            <li><a href="#skills" title="Skills"></a></li>
            <li><a href="#portfolio" title="Portfolio"></a></li>
            <li><a href="#experience" title="Experience"></a></li>
            <li><a href="#contact" title="Contact"></a></li>
        </ul>
    </nav>

    <main>
        <section id="home">
            <h1>Hi, I'm John Doe</h1>
            <p>Full Stack Developer</p>
            <a href="#contact">Get In Touch</a>
            <a href="#portfolio">View My Work</a>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p>About content...</p>
        </section>

        <section id="skills">
            <h2>Skills</h2>
            <p>Skills content...</p>
        </section>

        <section id="portfolio">
            <h2>Portfolio</h2>
            <nav aria-label="Portfolio Filter">
                <button data-filter="all">All</button>
                <button data-filter="web">Web</button>
                <button data-filter="mobile">Mobile</button>
                <button data-filter="design">Design</button>
            </nav>
            <!-- Portfolio items -->
        </section>

        <section id="experience">
            <h2>Experience</h2>
            <p>Experience content...</p>
        </section>

        <section id="contact">
            <h2>Contact Me</h2>
            <!-- Contact form -->
        </section>
    </main>

    <footer>
        <nav aria-label="Footer Navigation">
            <a href="#home">Back to Top</a>
            <a href="/privacy">Privacy Policy</a>
        </nav>
        <p>&copy; 2024 John Doe. All rights reserved.</p>
    </footer>

    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                target.scrollIntoView({ behavior: 'smooth' });
            });
        });

        // Active section highlighting
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.nav-menu a, .section-nav a');

        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (scrollY >= sectionTop - 100) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
        });
    </script>
</body>
</html>
```

## 4.12. Use Cases

### 4.12.1. Multi-language Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Multi-language Site</title>
</head>
<body>
    <header>
        <nav aria-label="Main Navigation">
            <ul>
                <li><a href="/vi/">Trang chủ</a></li>
                <li><a href="/vi/about">Giới thiệu</a></li>
                <li><a href="/vi/products">Sản phẩm</a></li>
                <li><a href="/vi/contact">Liên hệ</a></li>
            </ul>
        </nav>

        <nav aria-label="Language Selection">
            <ul>
                <li>
                    <a href="/vi/page" hreflang="vi" aria-current="page">
                        Tiếng Việt
                    </a>
                </li>
                <li>
                    <a href="/en/page" hreflang="en">
                        English
                    </a>
                </li>
                <li>
                    <a href="/fr/page" hreflang="fr">
                        Français
                    </a>
                </li>
            </ul>
        </nav>
    </header>
</body>
</html>
```

### 4.12.2. Documentation Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Documentation</title>
    <style>
        .docs-layout {
            display: grid;
            grid-template-columns: 250px 1fr 200px;
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }

        .sidebar-nav {
            position: sticky;
            top: 2rem;
            height: fit-content;
        }

        .sidebar-nav ul {
            list-style: none;
        }

        .sidebar-nav li {
            margin: 0.5rem 0;
        }

        .sidebar-nav a {
            color: #333;
            text-decoration: none;
            padding: 0.5rem;
            display: block;
            border-left: 3px solid transparent;
        }

        .sidebar-nav a:hover,
        .sidebar-nav a.active {
            border-left-color: #007bff;
            background: #f8f9fa;
        }

        .toc {
            position: sticky;
            top: 2rem;
            height: fit-content;
        }

        .toc ul {
            list-style: none;
        }

        .toc a {
            color: #6c757d;
            text-decoration: none;
            display: block;
            padding: 0.25rem 0;
            font-size: 0.875rem;
        }

        .toc a:hover {
            color: #007bff;
        }

        .doc-pagination {
            display: flex;
            justify-content: space-between;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #dee2e6;
        }

        .doc-pagination a {
            display: flex;
            flex-direction: column;
            text-decoration: none;
            color: #007bff;
        }

        .doc-pagination span {
            font-size: 0.875rem;
            color: #6c757d;
        }
    </style>
</head>
<body>
    <div class="docs-layout">
        <!-- Sidebar Navigation -->
        <nav class="sidebar-nav" aria-label="Documentation Navigation">
            <h3>Getting Started</h3>
            <ul>
                <li><a href="/docs/introduction">Introduction</a></li>
                <li><a href="/docs/installation">Installation</a></li>
                <li><a href="/docs/quick-start" class="active">Quick Start</a></li>
            </ul>

            <h3>Core Concepts</h3>
            <ul>
                <li><a href="/docs/components">Components</a></li>
                <li><a href="/docs/routing">Routing</a></li>
                <li><a href="/docs/state">State Management</a></li>
            </ul>

            <h3>Advanced</h3>
            <ul>
                <li><a href="/docs/performance">Performance</a></li>
                <li><a href="/docs/security">Security</a></li>
                <li><a href="/docs/testing">Testing</a></li>
            </ul>

            <h3>API Reference</h3>
            <ul>
                <li><a href="/docs/api/hooks">Hooks</a></li>
                <li><a href="/docs/api/utilities">Utilities</a></li>
            </ul>
        </nav>

        <!-- Main Content -->
        <main>
            <article>
                <h1 id="quick-start">Quick Start Guide</h1>

                <section id="installation">
                    <h2>Installation</h2>
                    <p>Content...</p>
                </section>

                <section id="basic-usage">
                    <h2>Basic Usage</h2>
                    <p>Content...</p>
                </section>

                <section id="configuration">
                    <h2>Configuration</h2>
                    <p>Content...</p>
                </section>

                <section id="next-steps">
                    <h2>Next Steps</h2>
                    <p>Content...</p>
                </section>
            </article>

            <!-- Documentation Pagination -->
            <nav class="doc-pagination" aria-label="Documentation Pages">
                <a href="/docs/installation" rel="prev">
                    <span>← Previous</span>
                    <strong>Installation</strong>
                </a>
                <a href="/docs/components" rel="next">
                    <span>Next →</span>
                    <strong>Components</strong>
                </a>
            </nav>
        </main>

        <!-- Table of Contents -->
        <nav class="toc" aria-label="Table of Contents">
            <h4>On This Page</h4>
            <ul>
                <li><a href="#installation">Installation</a></li>
                <li><a href="#basic-usage">Basic Usage</a></li>
                <li><a href="#configuration">Configuration</a></li>
                <li><a href="#next-steps">Next Steps</a></li>
            </ul>
        </nav>
    </div>
</body>
</html>
```

### 4.12.3. Social Media Navigation

```html
<footer>
    <nav aria-label="Social Media">
        <ul class="social-nav">
            <li>
                <a href="https://facebook.com/company"
                   target="_blank"
                   rel="noopener noreferrer"
                   aria-label="Visit our Facebook page">
                    <svg><!-- Facebook icon --></svg>
                    <span class="sr-only">Facebook</span>
                </a>
            </li>
            <li>
                <a href="https://twitter.com/company"
                   target="_blank"
                   rel="noopener noreferrer"
                   aria-label="Follow us on Twitter">
                    <svg><!-- Twitter icon --></svg>
                    <span class="sr-only">Twitter</span>
                </a>
            </li>
            <li>
                <a href="https://instagram.com/company"
                   target="_blank"
                   rel="noopener noreferrer"
                   aria-label="Follow us on Instagram">
                    <svg><!-- Instagram icon --></svg>
                    <span class="sr-only">Instagram</span>
                </a>
            </li>
            <li>
                <a href="https://linkedin.com/company/company"
                   target="_blank"
                   rel="noopener noreferrer"
                   aria-label="Connect with us on LinkedIn">
                    <svg><!-- LinkedIn icon --></svg>
                    <span class="sr-only">LinkedIn</span>
                </a>
            </li>
            <li>
                <a href="https://youtube.com/company"
                   target="_blank"
                   rel="noopener noreferrer"
                   aria-label="Subscribe to our YouTube channel">
                    <svg><!-- YouTube icon --></svg>
                    <span class="sr-only">YouTube</span>
                </a>
            </li>
        </ul>
    </nav>

    <style>
        .social-nav {
            display: flex;
            gap: 1rem;
            list-style: none;
        }

        .social-nav a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #333;
            color: white;
            text-decoration: none;
            transition: transform 0.3s, background 0.3s;
        }

        .social-nav a:hover {
            transform: translateY(-3px);
        }

        .social-nav a[href*="facebook"]:hover {
            background: #1877f2;
        }

        .social-nav a[href*="twitter"]:hover {
            background: #1da1f2;
        }

        .social-nav a[href*="instagram"]:hover {
            background: #e4405f;
        }

        .social-nav a[href*="linkedin"]:hover {
            background: #0077b5;
        }

        .social-nav a[href*="youtube"]:hover {
            background: #ff0000;
        }

        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            border: 0;
        }
    </style>
</footer>
```

### 4.12.4. Filter Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Product Catalog</title>
    <style>
        .filter-nav {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .filter-nav button {
            padding: 0.5rem 1.5rem;
            border: 2px solid #dee2e6;
            background: white;
            cursor: pointer;
            border-radius: 25px;
            transition: all 0.3s;
        }

        .filter-nav button:hover {
            border-color: #007bff;
            color: #007bff;
        }

        .filter-nav button.active {
            background: #007bff;
            color: white;
            border-color: #007bff;
        }

        .sort-nav {
            display: flex;
            gap: 1rem;
            align-items: center;
        }

        .sort-nav select {
            padding: 0.5rem 1rem;
            border: 1px solid #dee2e6;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <main>
        <h1>Products</h1>

        <!-- Filter Navigation -->
        <nav aria-label="Product Filter">
            <div class="filter-nav">
                <button class="active" data-filter="all">All Products</button>
                <button data-filter="electronics">Electronics</button>
                <button data-filter="fashion">Fashion</button>
                <button data-filter="home">Home & Garden</button>
                <button data-filter="sports">Sports</button>
                <button data-filter="toys">Toys</button>
            </div>
        </nav>

        <!-- Sort Navigation -->
        <nav aria-label="Sort Options">
            <div class="sort-nav">
                <label for="sort">Sort by:</label>
                <select id="sort" name="sort">
                    <option value="popular">Most Popular</option>
                    <option value="price-low">Price: Low to High</option>
                    <option value="price-high">Price: High to Low</option>
                    <option value="newest">Newest First</option>
                    <option value="rating">Highest Rated</option>
                </select>
            </div>
        </nav>

        <div class="products">
            <!-- Product cards -->
        </div>
    </main>

    <script>
        // Filter functionality
        const filterButtons = document.querySelectorAll('[data-filter]');
        const products = document.querySelectorAll('.product-card');

        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                // Add active class to clicked button
                button.classList.add('active');

                const filter = button.dataset.filter;

                products.forEach(product => {
                    if (filter === 'all' || product.dataset.category === filter) {
                        product.style.display = 'block';
                    } else {
                        product.style.display = 'none';
                    }
                });
            });
        });

        // Sort functionality
        const sortSelect = document.getElementById('sort');
        sortSelect.addEventListener('change', (e) => {
            const sortValue = e.target.value;
            // Implement sorting logic
            console.log('Sorting by:', sortValue);
        });
    </script>
</body>
</html>
```

### 4.12.5. Contextual Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Article with Context Nav</title>
    <style>
        .article-nav {
            position: sticky;
            top: 2rem;
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
        }

        .article-nav h3 {
            margin-bottom: 1rem;
        }

        .article-nav ul {
            list-style: none;
        }

        .article-nav a {
            display: block;
            padding: 0.5rem 0;
            color: #6c757d;
            text-decoration: none;
            border-left: 3px solid transparent;
            padding-left: 1rem;
        }

        .article-nav a:hover,
        .article-nav a.active {
            color: #007bff;
            border-left-color: #007bff;
        }

        .related-articles {
            margin-top: 3rem;
            padding: 2rem;
            background: #f8f9fa;
            border-radius: 8px;
        }

        .related-articles h3 {
            margin-bottom: 1rem;
        }

        .related-articles ul {
            list-style: none;
        }

        .related-articles li {
            margin: 1rem 0;
        }

        .related-articles a {
            color: #007bff;
            text-decoration: none;
        }

        .related-articles a:hover {
            text-decoration: underline;
        }

        .article-actions {
            display: flex;
            gap: 1rem;
            margin: 2rem 0;
        }

        .article-actions button {
            padding: 0.5rem 1rem;
            border: 1px solid #dee2e6;
            background: white;
            cursor: pointer;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <main>
            <article>
                <h1>Complete HTML5 Guide</h1>

                <nav class="article-actions" aria-label="Article Actions">
                    <button onclick="print()">Print</button>
                    <button onclick="shareArticle()">Share</button>
                    <a href="/pdf/article.pdf" download>Download PDF</a>
                    <button onclick="saveArticle()">Save for Later</button>
                </nav>

                <section id="introduction">
                    <h2>Introduction</h2>
                    <p>Content...</p>
                </section>

                <section id="basics">
                    <h2>HTML5 Basics</h2>
                    <p>Content...</p>
                </section>

                <section id="semantic">
                    <h2>Semantic Elements</h2>
                    <p>Content...</p>
                </section>

                <section id="apis">
                    <h2>HTML5 APIs</h2>
                    <p>Content...</p>
                </section>

                <section id="conclusion">
                    <h2>Conclusion</h2>
                    <p>Content...</p>
                </section>
            </article>

            <!-- Related Articles -->
            <nav class="related-articles" aria-label="Related Articles">
                <h3>Related Articles</h3>
                <ul>
                    <li>
                        <a href="/articles/css3-guide">Complete CSS3 Guide</a>
                        <p>Learn modern CSS techniques</p>
                    </li>
                    <li>
                        <a href="/articles/javascript-es6">JavaScript ES6 Features</a>
                        <p>Master modern JavaScript</p>
                    </li>
                    <li>
                        <a href="/articles/responsive-design">Responsive Web Design</a>
                        <p>Create mobile-friendly websites</p>
                    </li>
                </ul>
            </nav>
        </main>

        <aside>
            <nav class="article-nav" aria-label="Article Navigation">
                <h3>Contents</h3>
                <ul>
                    <li><a href="#introduction" class="active">Introduction</a></li>
                    <li><a href="#basics">HTML5 Basics</a></li>
                    <li><a href="#semantic">Semantic Elements</a></li>
                    <li><a href="#apis">HTML5 APIs</a></li>
                    <li><a href="#conclusion">Conclusion</a></li>
                </ul>
            </nav>
        </aside>
    </div>
</body>
</html>
```

## 4.13. Tips & Tricks

### Development Tips

**1. Use Descriptive Link Text**
```html
<!-- Tốt -->
<a href="/report.pdf">Download the Q4 2023 Sales Report (PDF, 2.5MB)</a>

<!-- Tránh -->
<a href="/report.pdf">Click here</a>
```

**2. Group Related Links**
```html
<nav aria-label="Product Categories">
    <ul>
        <li><a href="/electronics">Electronics</a></li>
        <li><a href="/fashion">Fashion</a></li>
        <li><a href="/home">Home</a></li>
    </ul>
</nav>
```

**3. Use Relative URLs for Internal Links**
```html
<!-- Tốt - Relative URL -->
<a href="/about">About Us</a>

<!-- Tránh - Absolute URL cho internal links -->
<a href="https://example.com/about">About Us</a>
```

### Performance Tips

**4. Prefetch Important Pages**
```html
<link rel="prefetch" href="/products">
<link rel="preload" href="/styles/main.css" as="style">
```

**5. Use rel="noopener" for External Links**
```html
<a href="https://external-site.com" target="_blank" rel="noopener noreferrer">
    External Link
</a>
```

**6. Optimize Navigation for Mobile**
```html
<nav class="mobile-nav">
    <button class="hamburger" aria-label="Toggle menu" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
    </button>
</nav>

<style>
    @media (max-width: 768px) {
        .nav-menu {
            display: none;
        }

        .nav-menu.active {
            display: block;
        }
    }
</style>
```

### SEO Tips

**7. Use Semantic Navigation**
```html
<nav aria-label="Main Navigation">
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/services">Services</a></li>
    </ul>
</nav>
```

**8. Create XML Sitemap Links**
```html
<head>
    <link rel="sitemap" type="application/xml" href="/sitemap.xml">
</head>
```

**9. Use Breadcrumbs with Schema.org**
```html
<nav aria-label="Breadcrumb">
    <ol itemscope itemtype="https://schema.org/BreadcrumbList">
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
            <a itemprop="item" href="/">
                <span itemprop="name">Home</span>
            </a>
            <meta itemprop="position" content="1" />
        </li>
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
            <a itemprop="item" href="/products">
                <span itemprop="name">Products</span>
            </a>
            <meta itemprop="position" content="2" />
        </li>
    </ol>
</nav>
```

**10. Internal Linking Strategy**
```html
<article>
    <p>Learn more about <a href="/html5-semantic-elements">semantic HTML5 elements</a>.</p>
    <p>Related: <a href="/css3-flexbox">CSS3 Flexbox Guide</a></p>
</article>
```

## 4.14. Common Mistakes

### Mistake 1: Using JavaScript for Links
```html
<!-- SAI -->
<div onclick="location.href='/page'">Go to Page</div>

<!-- ĐÚNG -->
<a href="/page">Go to Page</a>
```
**Tại sao:** Links phải là `<a>` elements để hoạt động với keyboard navigation và screen readers.

### Mistake 2: Missing href Attribute
```html
<!-- SAI -->
<a>Click here</a>

<!-- ĐÚNG -->
<a href="/page">Click here</a>
```
**Tại sao:** `<a>` không có `href` không phải là link và không thể navigate.

### Mistake 3: Using # as href
```html
<!-- SAI -->
<a href="#">Link</a>

<!-- ĐÚNG -->
<a href="/actual-page">Link</a>
<!-- Hoặc nếu dùng JavaScript -->
<button type="button" onclick="doSomething()">Action</button>
```
**Tại sao:** `href="#"` gây scroll về top và không có mục đích rõ ràng.

### Mistake 4: Forgetting target="_blank" Security
```html
<!-- SAI -->
<a href="https://external-site.com" target="_blank">External Link</a>

<!-- ĐÚNG -->
<a href="https://external-site.com" target="_blank" rel="noopener noreferrer">
    External Link
</a>
```
**Tại sao:** Không có `rel="noopener"` có thể gây security vulnerability (tabnabbing).

### Mistake 5: Non-descriptive Link Text
```html
<!-- SAI -->
<a href="/report.pdf">Click here</a>
<a href="/products">Read more</a>

<!-- ĐÚNG -->
<a href="/report.pdf">Download Annual Report (PDF, 2MB)</a>
<a href="/products">View all products</a>
```
**Tại sao:** Screen readers đọc link text riêng biệt, cần context rõ ràng.

### Mistake 6: Too Many Navigation Levels
```html
<!-- SAI - Quá nhiều nested levels -->
<nav>
    <ul>
        <li>
            <a href="#">Level 1</a>
            <ul>
                <li>
                    <a href="#">Level 2</a>
                    <ul>
                        <li>
                            <a href="#">Level 3</a>
                            <ul>
                                <li><a href="#">Level 4</a></li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</nav>

<!-- ĐÚNG - Max 2-3 levels -->
<nav>
    <ul>
        <li>
            <a href="/products">Products</a>
            <ul>
                <li><a href="/products/laptops">Laptops</a></li>
                <li><a href="/products/phones">Phones</a></li>
            </ul>
        </li>
    </ul>
</nav>
```
**Tại sao:** Quá nhiều levels làm navigation phức tạp và khó sử dụng.

### Mistake 7: Inconsistent Navigation
```html
<!-- SAI - Khác nhau giữa các pages -->
<!-- Page 1 -->
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/contact">Contact</a>
</nav>

<!-- Page 2 - Different order/items -->
<nav>
    <a href="/about">About</a>
    <a href="/">Home</a>
    <a href="/services">Services</a>
</nav>

<!-- ĐÚNG - Consistent across all pages -->
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/services">Services</a>
    <a href="/contact">Contact</a>
</nav>
```
**Tại sao:** Navigation phải consistent để users dễ nhớ và sử dụng.

### Mistake 8: Missing Active State
```html
<!-- SAI - Không có active indicator -->
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/products">Products</a>
</nav>

<!-- ĐÚNG - Show active page -->
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/products" aria-current="page" class="active">Products</a>
</nav>

<style>
    .active {
        font-weight: bold;
        color: #007bff;
        border-bottom: 2px solid #007bff;
    }
</style>
```
**Tại sao:** Users cần biết họ đang ở page nào.

### Mistake 9: Using Divs Instead of Nav
```html
<!-- SAI -->
<div class="navigation">
    <div class="menu">
        <a href="/">Home</a>
    </div>
</div>

<!-- ĐÚNG -->
<nav aria-label="Main Navigation">
    <ul>
        <li><a href="/">Home</a></li>
    </ul>
</nav>
```
**Tại sao:** `<nav>` element semantic và tốt cho accessibility.

### Mistake 10: Missing Skip Links
```html
<!-- SAI - Không có skip link -->
<body>
    <header>
        <nav><!-- Long navigation --></nav>
    </header>
    <main><!-- Content --></main>
</body>

<!-- ĐÚNG - Có skip link -->
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <header>
        <nav><!-- Long navigation --></nav>
    </header>
    <main id="main-content"><!-- Content --></main>
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
**Tại sao:** Skip links giúp keyboard users và screen reader users bỏ qua navigation.

## 4.15. Troubleshooting

### Issue 1: Links Not Working
**Problem:** Links không navigate khi click

**Cause:**
- Missing or invalid `href` attribute
- JavaScript error preventing default behavior
- CSS `pointer-events: none`

**Solution:**
```html
<!-- Check href -->
<a href="/page">Link</a>

<!-- Check JavaScript -->
<script>
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', (e) => {
        // Don't use e.preventDefault() unless necessary
        console.log('Link clicked:', link.href);
    });
});
</script>

<!-- Check CSS -->
<style>
a {
    /* Remove pointer-events: none */
    pointer-events: auto;
}
</style>
```

### Issue 2: Dropdown Menu Not Working on Mobile
**Problem:** Dropdown menu không mở trên mobile devices

**Cause:**
- Hover-only activation
- Missing touch event handlers
- Z-index issues

**Solution:**
```html
<nav class="dropdown-nav">
    <button class="dropdown-toggle" aria-expanded="false">
        Menu
    </button>
    <ul class="dropdown-menu">
        <li><a href="/page1">Page 1</a></li>
        <li><a href="/page2">Page 2</a></li>
    </ul>
</nav>

<script>
const toggle = document.querySelector('.dropdown-toggle');
const menu = document.querySelector('.dropdown-menu');

toggle.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', !expanded);
    menu.classList.toggle('open');
});

// Close when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.dropdown-nav')) {
        toggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('open');
    }
});
</script>

<style>
.dropdown-menu {
    display: none;
}

.dropdown-menu.open {
    display: block;
}

/* Don't rely on hover only */
@media (hover: hover) {
    .dropdown-nav:hover .dropdown-menu {
        display: block;
    }
}
</style>
```

### Issue 3: Active Link Not Highlighting
**Problem:** Current page link không có visual indicator

**Cause:**
- Missing active class
- JavaScript not running
- CSS specificity issues

**Solution:**
```javascript
// Automatic active link detection
const currentPath = window.location.pathname;
const navLinks = document.querySelectorAll('nav a');

navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
        link.setAttribute('aria-current', 'page');
    }
});
```

```css
/* Ensure active styles have high specificity */
nav a.active {
    font-weight: bold;
    color: #007bff !important;
    border-bottom: 2px solid #007bff;
}
```

### Issue 4: Smooth Scrolling Not Working
**Problem:** Anchor links không smooth scroll

**Cause:**
- Browser không support CSS smooth scrolling
- JavaScript not implemented
- Conflicting JavaScript

**Solution:**
```css
/* CSS solution */
html {
    scroll-behavior: smooth;
}
```

```javascript
// JavaScript fallback
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));

        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
```

### Issue 5: Breadcrumb Not Showing Correctly
**Problem:** Breadcrumb separators không hiển thị hoặc sai vị trí

**Cause:**
- CSS ::after issue
- Flexbox/Grid layout problems

**Solution:**
```html
<nav class="breadcrumb" aria-label="Breadcrumb">
    <ol>
        <li><a href="/">Home</a></li>
        <li><a href="/category">Category</a></li>
        <li aria-current="page">Product</li>
    </ol>
</nav>

<style>
.breadcrumb ol {
    display: flex;
    flex-wrap: wrap;
    list-style: none;
    padding: 0;
    margin: 0;
}

.breadcrumb li {
    display: flex;
    align-items: center;
}

.breadcrumb li:not(:last-child)::after {
    content: "/";
    margin: 0 0.5rem;
    color: #6c757d;
}
</style>
```

### Issue 6: Skip Link Not Visible on Focus
**Problem:** Skip link không xuất hiện khi tab

**Cause:**
- CSS positioning issues
- Z-index too low
- Focus styles removed

**Solution:**
```html
<a href="#main-content" class="skip-link">Skip to main content</a>

<style>
.skip-link {
    position: absolute;
    top: -100px;
    left: 0;
    background: #000;
    color: #fff;
    padding: 0.75rem 1.5rem;
    text-decoration: none;
    z-index: 9999; /* Very high z-index */
    transition: top 0.3s;
}

.skip-link:focus {
    top: 0;
    outline: 3px solid #007bff;
    outline-offset: 2px;
}
</style>
```

### Issue 7: Navigation Overlapping Content
**Problem:** Fixed navigation che content phía dưới

**Cause:**
- Missing padding/margin on body/main
- Z-index conflicts

**Solution:**
```css
/* Fixed header */
header {
    position: fixed;
    top: 0;
    width: 100%;
    height: 60px;
    z-index: 1000;
}

/* Add padding to body/main */
body {
    padding-top: 60px; /* Same as header height */
}

/* Or use margin on main */
main {
    margin-top: 60px;
}
```

### Issue 8: Email Links Opening in Wrong App
**Problem:** Mailto links mở wrong email client

**Cause:**
- Browser/OS default email client settings
- URL encoding issues

**Solution:**
```html
<!-- Properly encoded mailto link -->
<a href="mailto:support@example.com?subject=Support%20Request&body=Hello%2C%0D%0A%0D%0AI%20need%20help%20with...">
    Email Support
</a>

<!-- JavaScript to check if email client is available -->
<script>
function sendEmail() {
    const email = 'support@example.com';
    const subject = 'Support Request';
    const body = 'Hello,\n\nI need help with...';

    const mailto = `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

    const link = document.createElement('a');
    link.href = mailto;
    link.click();
}
</script>
```

### Issue 9: Phone Links Not Working on Desktop
**Problem:** Tel links không làm gì trên desktop

**Cause:**
- This is expected behavior
- No phone calling app on desktop

**Solution:**
```html
<!-- Provide alternative for desktop users -->
<div class="phone-contact">
    <a href="tel:+84123456789" class="phone-link">
        Call: 0123-456-789
    </a>
    <span class="phone-note">(Click to call on mobile)</span>
</div>

<style>
.phone-note {
    display: none;
    font-size: 0.875rem;
    color: #6c757d;
}

@media (min-width: 768px) {
    .phone-note {
        display: inline;
    }
}
</style>
```

### Issue 10: Pagination Links Confusing
**Problem:** Users không biết đang ở page nào

**Cause:**
- Missing aria-current
- No visual distinction for current page

**Solution:**
```html
<nav aria-label="Pagination" class="pagination">
    <a href="?page=1" rel="prev">Previous</a>
    <a href="?page=1">1</a>
    <a href="?page=2" aria-current="page" class="active">2</a>
    <a href="?page=3">3</a>
    <a href="?page=4">4</a>
    <a href="?page=5">5</a>
    <a href="?page=3" rel="next">Next</a>
</nav>

<style>
.pagination {
    display: flex;
    gap: 0.5rem;
}

.pagination a {
    padding: 0.5rem 1rem;
    border: 1px solid #dee2e6;
    text-decoration: none;
    color: #007bff;
    border-radius: 4px;
}

.pagination a.active {
    background: #007bff;
    color: white;
    border-color: #007bff;
    font-weight: bold;
    pointer-events: none; /* Prevent clicking current page */
}

.pagination a:hover:not(.active) {
    background: #f8f9fa;
}
</style>
```

## 4.16. Advanced Topics

### 4.16.1. Dynamic Navigation with JavaScript

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Dynamic Navigation</title>
</head>
<body>
    <nav id="dynamic-nav"></nav>

    <script>
        // Navigation data
        const navData = [
            {
                title: 'Home',
                url: '/',
                children: null
            },
            {
                title: 'Products',
                url: '/products',
                children: [
                    { title: 'Electronics', url: '/products/electronics' },
                    { title: 'Fashion', url: '/products/fashion' },
                    { title: 'Home & Garden', url: '/products/home' }
                ]
            },
            {
                title: 'About',
                url: '/about',
                children: [
                    { title: 'Our Story', url: '/about/story' },
                    { title: 'Team', url: '/about/team' }
                ]
            },
            {
                title: 'Contact',
                url: '/contact',
                children: null
            }
        ];

        // Generate navigation HTML
        function generateNav(data) {
            const nav = document.getElementById('dynamic-nav');
            const ul = document.createElement('ul');
            ul.className = 'nav-menu';

            data.forEach(item => {
                const li = document.createElement('li');

                const a = document.createElement('a');
                a.href = item.url;
                a.textContent = item.title;

                // Check if current page
                if (window.location.pathname === item.url) {
                    a.classList.add('active');
                    a.setAttribute('aria-current', 'page');
                }

                li.appendChild(a);

                // Add submenu if exists
                if (item.children && item.children.length > 0) {
                    const submenu = document.createElement('ul');
                    submenu.className = 'submenu';

                    item.children.forEach(child => {
                        const subLi = document.createElement('li');
                        const subA = document.createElement('a');
                        subA.href = child.url;
                        subA.textContent = child.title;

                        if (window.location.pathname === child.url) {
                            subA.classList.add('active');
                            subA.setAttribute('aria-current', 'page');
                        }

                        subLi.appendChild(subA);
                        submenu.appendChild(subLi);
                    });

                    li.appendChild(submenu);
                }

                ul.appendChild(li);
            });

            nav.appendChild(ul);
        }

        // Initialize navigation
        generateNav(navData);
    </script>

    <style>
        .nav-menu {
            display: flex;
            list-style: none;
            gap: 1rem;
        }

        .nav-menu > li {
            position: relative;
        }

        .nav-menu a {
            display: block;
            padding: 0.75rem 1rem;
            color: #333;
            text-decoration: none;
        }

        .nav-menu a.active {
            color: #007bff;
            font-weight: bold;
        }

        .submenu {
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            list-style: none;
            min-width: 200px;
            display: none;
        }

        .nav-menu > li:hover .submenu {
            display: block;
        }

        .submenu a {
            border-bottom: 1px solid #dee2e6;
        }
    </style>
</body>
</html>
```

### 4.16.2. Infinite Scroll Pagination

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Infinite Scroll</title>
    <style>
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 2rem;
            padding: 2rem;
        }

        .product-card {
            border: 1px solid #dee2e6;
            padding: 1rem;
            border-radius: 8px;
        }

        .loading {
            text-align: center;
            padding: 2rem;
            display: none;
        }

        .loading.active {
            display: block;
        }
    </style>
</head>
<body>
    <div class="product-grid" id="productGrid">
        <!-- Products will be loaded here -->
    </div>

    <div class="loading" id="loading">
        Loading more products...
    </div>

    <script>
        let page = 1;
        let loading = false;
        let hasMore = true;

        async function loadProducts() {
            if (loading || !hasMore) return;

            loading = true;
            document.getElementById('loading').classList.add('active');

            try {
                const response = await fetch(`/api/products?page=${page}`);
                const data = await response.json();

                const grid = document.getElementById('productGrid');

                data.products.forEach(product => {
                    const card = document.createElement('div');
                    card.className = 'product-card';
                    card.innerHTML = `
                        <img src="${product.image}" alt="${product.name}">
                        <h3><a href="/products/${product.id}">${product.name}</a></h3>
                        <p>${product.price}</p>
                    `;
                    grid.appendChild(card);
                });

                page++;
                hasMore = data.hasMore;

            } catch (error) {
                console.error('Error loading products:', error);
            } finally {
                loading = false;
                document.getElementById('loading').classList.remove('active');
            }
        }

        // Load initial products
        loadProducts();

        // Intersection Observer for infinite scroll
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    loadProducts();
                }
            });
        }, {
            rootMargin: '100px'
        });

        observer.observe(document.getElementById('loading'));
    </script>
</body>
</html>
```

### 4.16.3. Sticky Navigation with Scroll Behavior

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Sticky Navigation</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .header {
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
            transition: all 0.3s;
        }

        .header.scrolled {
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            padding: 0.5rem 0;
        }

        .header.hidden {
            transform: translateY(-100%);
        }

        .nav {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2rem;
        }

        .nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
            margin: 0;
        }

        .nav a {
            color: #333;
            text-decoration: none;
            transition: color 0.3s;
        }

        .nav a:hover {
            color: #007bff;
        }

        .content {
            height: 3000px;
            padding: 2rem;
        }
    </style>
</head>
<body>
    <header class="header" id="header">
        <nav class="nav" aria-label="Main Navigation">
            <a href="/" class="logo">Logo</a>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <div class="content">
        <h1>Scroll down to see sticky navigation</h1>
        <p>Content...</p>
    </div>

    <script>
        const header = document.getElementById('header');
        let lastScroll = 0;
        let scrollThreshold = 100;

        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;

            // Add scrolled class after threshold
            if (currentScroll > scrollThreshold) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }

            // Hide header on scroll down, show on scroll up
            if (currentScroll > lastScroll && currentScroll > scrollThreshold) {
                // Scrolling down
                header.classList.add('hidden');
            } else {
                // Scrolling up
                header.classList.remove('hidden');
            }

            lastScroll = currentScroll;
        });
    </script>
</body>
</html>
```

### 4.16.4. Accessible Mega Menu

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Accessible Mega Menu</title>
    <style>
        .mega-menu-wrapper {
            background: #1a1a1a;
            position: relative;
        }

        .mega-menu {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            list-style: none;
            padding: 0;
        }

        .mega-menu > li {
            position: relative;
        }

        .mega-menu > li > a {
            display: block;
            padding: 1rem 1.5rem;
            color: white;
            text-decoration: none;
        }

        .mega-menu > li > a:hover,
        .mega-menu > li > a:focus {
            background: #007bff;
        }

        .mega-dropdown {
            position: absolute;
            top: 100%;
            left: 0;
            width: 100vw;
            background: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            display: none;
            padding: 2rem;
        }

        .mega-menu > li:hover .mega-dropdown,
        .mega-menu > li > a:focus + .mega-dropdown,
        .mega-dropdown:hover {
            display: block;
        }

        .mega-dropdown-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
        }

        .mega-column h3 {
            margin-bottom: 1rem;
            color: #333;
        }

        .mega-column ul {
            list-style: none;
            padding: 0;
        }

        .mega-column li {
            margin: 0.5rem 0;
        }

        .mega-column a {
            color: #6c757d;
            text-decoration: none;
        }

        .mega-column a:hover,
        .mega-column a:focus {
            color: #007bff;
        }
    </style>
</head>
<body>
    <nav class="mega-menu-wrapper" aria-label="Main Navigation">
        <ul class="mega-menu">
            <li>
                <a href="/products"
                   aria-haspopup="true"
                   aria-expanded="false"
                   id="products-menu">
                    Products
                </a>
                <div class="mega-dropdown" role="region" aria-labelledby="products-menu">
                    <div class="mega-dropdown-content">
                        <div class="mega-column">
                            <h3>Electronics</h3>
                            <ul>
                                <li><a href="/products/laptops">Laptops</a></li>
                                <li><a href="/products/phones">Smartphones</a></li>
                                <li><a href="/products/tablets">Tablets</a></li>
                                <li><a href="/products/accessories">Accessories</a></li>
                            </ul>
                        </div>
                        <div class="mega-column">
                            <h3>Fashion</h3>
                            <ul>
                                <li><a href="/fashion/men">Men's Fashion</a></li>
                                <li><a href="/fashion/women">Women's Fashion</a></li>
                                <li><a href="/fashion/kids">Kids' Fashion</a></li>
                                <li><a href="/fashion/accessories">Accessories</a></li>
                            </ul>
                        </div>
                        <div class="mega-column">
                            <h3>Home & Garden</h3>
                            <ul>
                                <li><a href="/home/furniture">Furniture</a></li>
                                <li><a href="/home/kitchen">Kitchen</a></li>
                                <li><a href="/home/decor">Home Decor</a></li>
                                <li><a href="/home/garden">Garden</a></li>
                            </ul>
                        </div>
                        <div class="mega-column">
                            <h3>Featured</h3>
                            <ul>
                                <li><a href="/featured/new">New Arrivals</a></li>
                                <li><a href="/featured/bestsellers">Best Sellers</a></li>
                                <li><a href="/featured/deals">Today's Deals</a></li>
                                <li><a href="/featured/clearance">Clearance</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </li>
            <li><a href="/deals">Deals</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </nav>

    <script>
        // Enhance accessibility with JavaScript
        const menuItems = document.querySelectorAll('.mega-menu > li > a[aria-haspopup]');

        menuItems.forEach(item => {
            const parent = item.parentElement;
            const dropdown = parent.querySelector('.mega-dropdown');

            // Toggle on click (for touch devices)
            item.addEventListener('click', (e) => {
                e.preventDefault();
                const isExpanded = item.getAttribute('aria-expanded') === 'true';

                // Close all other dropdowns
                menuItems.forEach(otherItem => {
                    otherItem.setAttribute('aria-expanded', 'false');
                });

                // Toggle current dropdown
                item.setAttribute('aria-expanded', !isExpanded);
            });

            // Keyboard navigation
            item.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    const isExpanded = item.getAttribute('aria-expanded') === 'true';
                    item.setAttribute('aria-expanded', !isExpanded);
                }

                if (e.key === 'Escape') {
                    item.setAttribute('aria-expanded', 'false');
                    item.focus();
                }
            });
        });

        // Close dropdowns when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.mega-menu')) {
                menuItems.forEach(item => {
                    item.setAttribute('aria-expanded', 'false');
                });
            }
        });
    </script>
</body>
</html>
```

### 4.16.5. Search-Enhanced Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Search Navigation</title>
    <style>
        .search-nav {
            background: #f8f9fa;
            padding: 1rem;
        }

        .search-container {
            max-width: 600px;
            margin: 0 auto;
            position: relative;
        }

        .search-input {
            width: 100%;
            padding: 1rem;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            font-size: 1rem;
        }

        .search-input:focus {
            outline: none;
            border-color: #007bff;
        }

        .search-suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #dee2e6;
            border-top: none;
            border-radius: 0 0 8px 8px;
            max-height: 400px;
            overflow-y: auto;
            display: none;
            z-index: 1000;
        }

        .search-suggestions.active {
            display: block;
        }

        .search-section {
            padding: 1rem;
            border-bottom: 1px solid #dee2e6;
        }

        .search-section h4 {
            margin: 0 0 0.5rem 0;
            font-size: 0.875rem;
            color: #6c757d;
            text-transform: uppercase;
        }

        .search-section ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .search-section li {
            padding: 0.5rem 0;
        }

        .search-section a {
            color: #333;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .search-section a:hover {
            color: #007bff;
        }

        .search-highlight {
            background: #fff3cd;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <nav class="search-nav" aria-label="Search Navigation">
        <div class="search-container">
            <input
                type="search"
                class="search-input"
                placeholder="Search products, categories, pages..."
                aria-label="Search"
                id="searchInput"
                autocomplete="off"
            >
            <div class="search-suggestions" id="searchSuggestions" role="listbox">
                <!-- Suggestions will be populated here -->
            </div>
        </div>
    </nav>

    <script>
        const searchInput = document.getElementById('searchInput');
        const searchSuggestions = document.getElementById('searchSuggestions');

        // Sample search data
        const searchData = {
            products: [
                { name: 'Dell XPS 13 Laptop', url: '/products/dell-xps-13' },
                { name: 'iPhone 15 Pro', url: '/products/iphone-15-pro' },
                { name: 'Samsung Galaxy S24', url: '/products/samsung-s24' },
            ],
            categories: [
                { name: 'Electronics', url: '/categories/electronics' },
                { name: 'Fashion', url: '/categories/fashion' },
                { name: 'Home & Garden', url: '/categories/home' },
            ],
            pages: [
                { name: 'About Us', url: '/about' },
                { name: 'Contact', url: '/contact' },
                { name: 'FAQ', url: '/faq' },
            ]
        };

        let debounceTimer;

        searchInput.addEventListener('input', (e) => {
            clearTimeout(debounceTimer);

            const query = e.target.value.trim().toLowerCase();

            if (query.length < 2) {
                searchSuggestions.classList.remove('active');
                return;
            }

            debounceTimer = setTimeout(() => {
                performSearch(query);
            }, 300);
        });

        function performSearch(query) {
            let html = '';
            let hasResults = false;

            // Search products
            const productResults = searchData.products.filter(item =>
                item.name.toLowerCase().includes(query)
            );

            if (productResults.length > 0) {
                hasResults = true;
                html += '<div class="search-section">';
                html += '<h4>Products</h4>';
                html += '<ul>';
                productResults.forEach(item => {
                    const highlightedName = item.name.replace(
                        new RegExp(query, 'gi'),
                        match => `<span class="search-highlight">${match}</span>`
                    );
                    html += `<li><a href="${item.url}">${highlightedName}</a></li>`;
                });
                html += '</ul></div>';
            }

            // Search categories
            const categoryResults = searchData.categories.filter(item =>
                item.name.toLowerCase().includes(query)
            );

            if (categoryResults.length > 0) {
                hasResults = true;
                html += '<div class="search-section">';
                html += '<h4>Categories</h4>';
                html += '<ul>';
                categoryResults.forEach(item => {
                    const highlightedName = item.name.replace(
                        new RegExp(query, 'gi'),
                        match => `<span class="search-highlight">${match}</span>`
                    );
                    html += `<li><a href="${item.url}">${highlightedName}</a></li>`;
                });
                html += '</ul></div>';
            }

            // Search pages
            const pageResults = searchData.pages.filter(item =>
                item.name.toLowerCase().includes(query)
            );

            if (pageResults.length > 0) {
                hasResults = true;
                html += '<div class="search-section">';
                html += '<h4>Pages</h4>';
                html += '<ul>';
                pageResults.forEach(item => {
                    const highlightedName = item.name.replace(
                        new RegExp(query, 'gi'),
                        match => `<span class="search-highlight">${match}</span>`
                    );
                    html += `<li><a href="${item.url}">${highlightedName}</a></li>`;
                });
                html += '</ul></div>';
            }

            if (!hasResults) {
                html = '<div class="search-section"><p>No results found</p></div>';
            }

            searchSuggestions.innerHTML = html;
            searchSuggestions.classList.add('active');
        }

        // Close suggestions when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.search-container')) {
                searchSuggestions.classList.remove('active');
            }
        });

        // Keyboard navigation
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                searchSuggestions.classList.remove('active');
            }
        });
    </script>
</body>
</html>
```

### 4.16.6. Progressive Disclosure Navigation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Progressive Disclosure Navigation</title>
    <style>
        .disclosure-nav {
            max-width: 400px;
            margin: 2rem auto;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            overflow: hidden;
        }

        .disclosure-item {
            border-bottom: 1px solid #dee2e6;
        }

        .disclosure-item:last-child {
            border-bottom: none;
        }

        .disclosure-button {
            width: 100%;
            padding: 1rem;
            background: white;
            border: none;
            text-align: left;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1rem;
            transition: background 0.3s;
        }

        .disclosure-button:hover {
            background: #f8f9fa;
        }

        .disclosure-button[aria-expanded="true"] {
            background: #e9ecef;
            font-weight: bold;
        }

        .disclosure-icon {
            transition: transform 0.3s;
        }

        .disclosure-button[aria-expanded="true"] .disclosure-icon {
            transform: rotate(180deg);
        }

        .disclosure-panel {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
        }

        .disclosure-panel.open {
            max-height: 500px;
            transition: max-height 0.5s ease-in;
        }

        .disclosure-content {
            padding: 1rem;
            background: #f8f9fa;
        }

        .disclosure-content ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .disclosure-content li {
            padding: 0.5rem 0;
        }

        .disclosure-content a {
            color: #007bff;
            text-decoration: none;
        }

        .disclosure-content a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <nav class="disclosure-nav" aria-label="Categories">
        <div class="disclosure-item">
            <button
                class="disclosure-button"
                aria-expanded="false"
                aria-controls="electronics-panel">
                <span>Electronics</span>
                <span class="disclosure-icon">▼</span>
            </button>
            <div id="electronics-panel" class="disclosure-panel" role="region">
                <div class="disclosure-content">
                    <ul>
                        <li><a href="/electronics/laptops">Laptops</a></li>
                        <li><a href="/electronics/phones">Smartphones</a></li>
                        <li><a href="/electronics/tablets">Tablets</a></li>
                        <li><a href="/electronics/accessories">Accessories</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="disclosure-item">
            <button
                class="disclosure-button"
                aria-expanded="false"
                aria-controls="fashion-panel">
                <span>Fashion</span>
                <span class="disclosure-icon">▼</span>
            </button>
            <div id="fashion-panel" class="disclosure-panel" role="region">
                <div class="disclosure-content">
                    <ul>
                        <li><a href="/fashion/men">Men's Fashion</a></li>
                        <li><a href="/fashion/women">Women's Fashion</a></li>
                        <li><a href="/fashion/kids">Kids' Fashion</a></li>
                        <li><a href="/fashion/accessories">Accessories</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="disclosure-item">
            <button
                class="disclosure-button"
                aria-expanded="false"
                aria-controls="home-panel">
                <span>Home & Garden</span>
                <span class="disclosure-icon">▼</span>
            </button>
            <div id="home-panel" class="disclosure-panel" role="region">
                <div class="disclosure-content">
                    <ul>
                        <li><a href="/home/furniture">Furniture</a></li>
                        <li><a href="/home/kitchen">Kitchen</a></li>
                        <li><a href="/home/decor">Home Decor</a></li>
                        <li><a href="/home/garden">Garden</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>

    <script>
        const disclosureButtons = document.querySelectorAll('.disclosure-button');

        disclosureButtons.forEach(button => {
            button.addEventListener('click', () => {
                const expanded = button.getAttribute('aria-expanded') === 'true';
                const panel = document.getElementById(button.getAttribute('aria-controls'));

                // Toggle current panel
                button.setAttribute('aria-expanded', !expanded);
                panel.classList.toggle('open');
            });
        });

        // Keyboard navigation
        disclosureButtons.forEach((button, index) => {
            button.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    if (index < disclosureButtons.length - 1) {
                        disclosureButtons[index + 1].focus();
                    }
                }

                if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    if (index > 0) {
                        disclosureButtons[index - 1].focus();
                    }
                }

                if (e.key === 'Home') {
                    e.preventDefault();
                    disclosureButtons[0].focus();
                }

                if (e.key === 'End') {
                    e.preventDefault();
                    disclosureButtons[disclosureButtons.length - 1].focus();
                }
            });
        });
    </script>
</body>
</html>
```

### 4.16.7. Context-Aware Navigation

```javascript
// Navigation that adapts based on user context
class ContextAwareNavigation {
    constructor() {
        this.userRole = this.getUserRole();
        this.currentPage = window.location.pathname;
        this.init();
    }

    getUserRole() {
        // Get user role from session/localStorage
        return localStorage.getItem('userRole') || 'guest';
    }

    init() {
        this.generateNavigation();
        this.highlightCurrentPage();
        this.addEventListeners();
    }

    generateNavigation() {
        const navData = this.getNavDataForRole(this.userRole);
        const nav = document.getElementById('contextNav');

        let html = '<ul class="context-nav">';
        navData.forEach(item => {
            html += `
                <li>
                    <a href="${item.url}" ${item.url === this.currentPage ? 'aria-current="page"' : ''}>
                        ${item.label}
                    </a>
                </li>
            `;
        });
        html += '</ul>';

        nav.innerHTML = html;
    }

    getNavDataForRole(role) {
        const navConfig = {
            guest: [
                { label: 'Home', url: '/' },
                { label: 'Products', url: '/products' },
                { label: 'Sign In', url: '/signin' }
            ],
            user: [
                { label: 'Home', url: '/' },
                { label: 'Products', url: '/products' },
                { label: 'My Orders', url: '/orders' },
                { label: 'Profile', url: '/profile' }
            ],
            admin: [
                { label: 'Dashboard', url: '/admin/dashboard' },
                { label: 'Users', url: '/admin/users' },
                { label: 'Products', url: '/admin/products' },
                { label: 'Orders', url: '/admin/orders' },
                { label: 'Settings', url: '/admin/settings' }
            ]
        };

        return navConfig[role] || navConfig.guest;
    }

    highlightCurrentPage() {
        const links = document.querySelectorAll('.context-nav a');
        links.forEach(link => {
            if (link.getAttribute('href') === this.currentPage) {
                link.classList.add('active');
            }
        });
    }

    addEventListeners() {
        // Track navigation events
        const links = document.querySelectorAll('.context-nav a');
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                this.trackNavigation(link.getAttribute('href'));
            });
        });
    }

    trackNavigation(url) {
        // Analytics tracking
        console.log(`Navigation tracked: ${url}`);
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    new ContextAwareNavigation();
});
```

## 4.17. Bài tập thực hành

### Bài 1: Basic Links (Dễ)
**Yêu cầu:**
- Tạo trang HTML với các loại links khác nhau
- External links (3 links)
- Internal links (5 links)
- Email link với subject và body
- Telephone link
- Download link cho PDF file
- Anchor links (3 sections)

**Đánh giá:**
- Đúng syntax: 20%
- Đầy đủ attributes: 30%
- Accessibility: 30%
- Styling: 20%

### Bài 2: Horizontal Navigation Menu (Dễ)
**Yêu cầu:**
- Tạo horizontal navigation bar
- 5 menu items
- Active state cho current page
- Hover effects
- Responsive cho mobile

**Đánh giá:**
- HTML structure: 25%
- CSS styling: 25%
- Hover/active states: 25%
- Responsive: 25%

### Bài 3: Dropdown Menu (Trung bình)
**Yêu cầu:**
- Tạo navigation với dropdown submenu
- 2 levels: main menu và submenu
- Hover và click functionality
- Keyboard accessible
- Mobile-friendly

**Đánh giá:**
- Functionality: 30%
- Accessibility: 30%
- Mobile support: 20%
- Code quality: 20%

### Bài 4: Breadcrumb Navigation (Dễ)
**Yêu cầu:**
- Tạo breadcrumb navigation
- Schema.org structured data
- Separators giữa items
- Current page styling
- Responsive

**Đánh giá:**
- Correct structure: 30%
- Structured data: 30%
- Styling: 20%
- Accessibility: 20%

### Bài 5: Pagination (Trung bình)
**Yêu cầu:**
- Tạo pagination component
- Previous/Next buttons
- Page numbers (1-10)
- Ellipsis cho nhiều pages (...)
- Current page highlight
- Disabled state cho first/last page

**Đánh giá:**
- Functionality: 35%
- Visual design: 25%
- Edge cases handling: 20%
- Accessibility: 20%

### Bài 6: Sticky Navigation (Trung bình)
**Yêu cầu:**
- Navigation cố định ở top khi scroll
- Smooth appearance/disappearance
- Different styling khi scrolled
- Performance optimized

**Đánh giá:**
- Implementation: 35%
- Smooth animations: 25%
- Performance: 20%
- Styling: 20%

### Bài 7: Mega Menu (Khó)
**Yêu cầu:**
- Large dropdown menu với multiple columns
- 3-4 categories, mỗi category có subcategories
- Images và descriptions
- Hover và keyboard navigation
- Fully accessible

**Đánh giá:**
- Complexity: 30%
- Accessibility: 30%
- Design: 20%
- Functionality: 20%

### Bài 8: Mobile Navigation (Hamburger Menu) (Trung bình)
**Yêu cầu:**
- Hamburger icon toggle
- Slide-in menu animation
- Overlay background
- Close button
- Touch-friendly

**Đánh giá:**
- Mobile functionality: 30%
- Animations: 25%
- Touch interactions: 25%
- Code quality: 20%

### Bài 9: Tab Navigation (Trung bình)
**Yêu cầu:**
- Tab interface với 4-5 tabs
- Content switching
- Keyboard navigation (Arrow keys)
- Active tab styling
- ARIA attributes

**Đánh giá:**
- Tab switching: 30%
- Keyboard navigation: 30%
- Accessibility: 20%
- Styling: 20%

### Bài 10: Dashboard Sidebar Navigation (Khó)
**Yêu cầu:**
- Collapsible sidebar
- Multi-level menu
- Icons for menu items
- Active section highlighting
- Responsive collapse on mobile

**Đánh giá:**
- Multi-level functionality: 30%
- Collapse mechanism: 25%
- Visual design: 25%
- Responsive behavior: 20%

### Bài 11: Complete Website Navigation System (Khó)
**Yêu cầu:**
- Header với logo và main menu
- Dropdown submenus
- Search bar trong navigation
- User account menu
- Shopping cart link (với badge)
- Footer navigation với multiple columns
- Breadcrumb
- Social media links
- Fully responsive
- Accessibility compliant

**Đánh giá:**
- Completeness: 25%
- Functionality: 25%
- Accessibility: 25%
- Design: 25%

### Bài 12: Advanced Dynamic Navigation (Rất khó)
**Yêu cầu:**
- Navigation tạo từ JSON data
- User role-based menu items
- Infinite scroll pagination
- Search with autocomplete
- History API integration
- Analytics tracking
- Performance optimized
- Full test coverage

**Đánh giá:**
- Dynamic generation: 25%
- Advanced features: 30%
- Performance: 20%
- Code quality: 25%

---

**Kết luận:** Trong chương này, chúng ta đã học về links và navigation trong HTML5, bao gồm cách tạo links, navigation patterns, accessibility, SEO best practices, và các kỹ thuật advanced. Navigation là một trong những yếu tố quan trọng nhất của website, ảnh hưởng trực tiếp đến user experience và SEO. Chương tiếp theo sẽ tìm hiểu về Images và Multimedia.
