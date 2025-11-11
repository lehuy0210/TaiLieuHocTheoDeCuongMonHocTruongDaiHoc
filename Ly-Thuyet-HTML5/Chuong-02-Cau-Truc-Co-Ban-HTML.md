# CHƯƠNG 2: CẤU TRÚC CƠ BẢN HTML

## 2.1. Elements (Phần tử HTML)

### 2.1.1. Khái niệm Element

Một HTML element bao gồm:
- **Opening tag** (thẻ mở): `<tagname>`
- **Content** (nội dung): Nội dung bên trong thẻ
- **Closing tag** (thẻ đóng): `</tagname>`

```html
<p>Đây là một đoạn văn bản</p>
```

**Cấu trúc chi tiết:**
```
<p>      Đây là một đoạn văn bản      </p>
↑                ↑                      ↑
Opening tag    Content            Closing tag
```

### 2.1.2. Các loại Elements

#### A. Normal Elements (Thẻ thông thường)
Có opening tag và closing tag:
```html
<p>Paragraph</p>
<div>Division</div>
<span>Span</span>
<h1>Heading 1</h1>
```

#### B. Void Elements (Self-closing tags)
Không có closing tag và không chứa content:
```html
<img src="image.jpg" alt="Description">
<br>
<hr>
<input type="text">
<meta charset="UTF-8">
<link rel="stylesheet" href="style.css">
<area>
<base>
<col>
<embed>
<source>
<track>
<wbr>
```

**Lưu ý về Void Elements trong HTML5:**
```html
<!-- Cả hai cách đều đúng trong HTML5 -->
<img src="image.jpg" alt="Image">
<img src="image.jpg" alt="Image" />

<!-- Nhưng khuyên dùng cách không có dấu / -->
<img src="image.jpg" alt="Image">
```

#### C. Nested Elements (Thẻ lồng nhau)
Elements có thể chứa elements khác:
```html
<div>
    <h1>Tiêu đề</h1>
    <p>Đoạn văn <strong>in đậm</strong> và <em>in nghiêng</em></p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
</div>
```

**Quy tắc lồng nhau:**
```html
<!-- ĐÚNG -->
<div><p>Text</p></div>

<!-- SAI - không đóng đúng thứ tự -->
<div><p>Text</div></p>

<!-- SAI - p không được chứa div -->
<p><div>Text</div></p>

<!-- ĐÚNG - p có thể chứa span -->
<p><span>Text</span></p>
```

### 2.1.3. Block-level vs Inline Elements

#### Block-level Elements
- Chiếm toàn bộ chiều rộng available
- Bắt đầu trên một dòng mới
- Có thể chứa block và inline elements

**Các thẻ block-level phổ biến:**
```html
<div>       <!-- Generic container -->
<p>         <!-- Paragraph -->
<h1>-<h6>   <!-- Headings -->
<ul>, <ol>  <!-- Lists -->
<li>        <!-- List item -->
<table>     <!-- Table -->
<form>      <!-- Form -->
<header>    <!-- Header -->
<footer>    <!-- Footer -->
<section>   <!-- Section -->
<article>   <!-- Article -->
<nav>       <!-- Navigation -->
<aside>     <!-- Aside -->
<main>      <!-- Main content -->
```

**Ví dụ:**
```html
<div style="background: lightblue;">
    <p>Block element 1</p>
    <p>Block element 2</p>
</div>
```

#### Inline Elements
- Chỉ chiếm không gian cần thiết
- Không bắt đầu dòng mới
- Chỉ có thể chứa inline elements và text

**Các thẻ inline phổ biến:**
```html
<span>      <!-- Generic inline container -->
<a>         <!-- Anchor/Link -->
<strong>    <!-- Strong importance -->
<em>        <!-- Emphasis -->
<b>         <!-- Bold -->
<i>         <!-- Italic -->
<u>         <!-- Underline -->
<small>     <!-- Small text -->
<mark>      <!-- Marked text -->
<code>      <!-- Code -->
<sub>       <!-- Subscript -->
<sup>       <!-- Superscript -->
<img>       <!-- Image -->
<input>     <!-- Input -->
<button>    <!-- Button -->
```

**Ví dụ:**
```html
<p>
    Đây là <span style="color: red;">inline element</span> trong văn bản.
    <strong>Text in đậm</strong> và <em>text nghiêng</em>.
</p>
```

#### So sánh Block vs Inline

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .block { background: lightblue; margin: 5px; }
        .inline { background: lightgreen; margin: 5px; }
    </style>
</head>
<body>
    <!-- Block elements -->
    <div class="block">Block Element 1</div>
    <div class="block">Block Element 2</div>

    <!-- Inline elements -->
    <span class="inline">Inline 1</span>
    <span class="inline">Inline 2</span>
    <span class="inline">Inline 3</span>
</body>
</html>
```

## 2.2. Attributes (Thuộc tính)

### 2.2.1. Khái niệm Attribute

Attributes cung cấp thông tin bổ sung về elements:
```html
<tagname attribute="value">Content</tagname>
```

**Cú pháp:**
```html
<element attribute1="value1" attribute2="value2">Content</element>
```

### 2.2.2. Global Attributes

Attributes có thể dùng cho mọi HTML element:

#### class
Xác định một hoặc nhiều class names:
```html
<div class="container">Single class</div>
<div class="header main-header large">Multiple classes</div>
```

#### id
Xác định unique identifier:
```html
<div id="main-content">Unique ID</div>

<!-- LƯU Ý: ID phải unique trong document -->
<!-- SAI -->
<div id="test">Content 1</div>
<div id="test">Content 2</div>

<!-- ĐÚNG -->
<div id="test1">Content 1</div>
<div id="test2">Content 2</div>
```

#### style
Inline CSS:
```html
<p style="color: red; font-size: 16px;">Styled text</p>
```

#### title
Tooltip khi hover:
```html
<p title="This is a tooltip">Hover over me</p>
<abbr title="HyperText Markup Language">HTML</abbr>
```

#### lang
Xác định ngôn ngữ:
```html
<html lang="vi">
<p lang="en">This is English</p>
<p lang="vi">Đây là tiếng Việt</p>
```

#### data-*
Custom data attributes:
```html
<div data-user-id="12345" data-role="admin">User Info</div>
<button data-action="delete" data-id="100">Delete</button>

<script>
// Truy cập data attributes
const div = document.querySelector('div');
console.log(div.dataset.userId);  // "12345"
console.log(div.dataset.role);     // "admin"
</script>
```

#### hidden
Ẩn element:
```html
<p hidden>This paragraph is hidden</p>
```

#### contenteditable
Cho phép chỉnh sửa nội dung:
```html
<div contenteditable="true">
    Có thể chỉnh sửa nội dung này
</div>
```

#### draggable
Cho phép kéo thả:
```html
<p draggable="true">Có thể kéo thả</p>
```

#### spellcheck
Kiểm tra chính tả:
```html
<textarea spellcheck="true">
    Nhập văn bản ở đây
</textarea>
```

#### tabindex
Thứ tự tab:
```html
<input type="text" tabindex="1">
<input type="text" tabindex="3">
<input type="text" tabindex="2">
```

#### accesskey
Phím tắt:
```html
<a href="#" accesskey="h">Home (Alt+H)</a>
<button accesskey="s">Save (Alt+S)</button>
```

### 2.2.3. Specific Attributes

Attributes dành riêng cho một số elements:

#### Cho `<a>` (Links)
```html
<a href="https://example.com"
   target="_blank"
   rel="noopener noreferrer"
   download="filename.pdf">
   Link text
</a>
```

#### Cho `<img>` (Images)
```html
<img src="image.jpg"
     alt="Description"
     width="300"
     height="200"
     loading="lazy"
     decoding="async">
```

#### Cho `<input>` (Form inputs)
```html
<input type="text"
       name="username"
       value="default value"
       placeholder="Enter username"
       required
       maxlength="50"
       pattern="[A-Za-z0-9]+"
       autocomplete="off">
```

#### Cho `<form>`
```html
<form action="/submit"
      method="POST"
      enctype="multipart/form-data"
      autocomplete="on"
      novalidate>
</form>
```

### 2.2.4. Boolean Attributes

Attributes không cần value:
```html
<input type="checkbox" checked>
<input type="text" disabled>
<input type="text" readonly>
<input type="text" required>
<option selected>Option</option>
<script async src="script.js"></script>
<script defer src="script.js"></script>
<button autofocus>Click me</button>
<video autoplay controls loop muted>
```

**Lưu ý:**
```html
<!-- Tất cả cách sau đều giống nhau -->
<input type="checkbox" checked>
<input type="checkbox" checked="">
<input type="checkbox" checked="checked">
<input type="checkbox" checked="true">

<!-- Để tắt boolean attribute, bỏ hẳn attribute -->
<input type="checkbox">
```

## 2.3. Comments (Chú thích)

### 2.3.1. Cú pháp Comments

```html
<!-- This is a comment -->

<!--
    This is a
    multi-line comment
-->

<p>Normal content</p> <!-- Inline comment -->
```

### 2.3.2. Best practices cho Comments

**1. Mô tả sections:**
```html
<!-- Header Section Start -->
<header>
    <!-- Navigation -->
    <nav></nav>
</header>
<!-- Header Section End -->
```

**2. Temporary disable code:**
```html
<!-- <div class="old-code">
    <p>This code is temporarily disabled</p>
</div> -->
```

**3. TODO notes:**
```html
<!-- TODO: Add social media links -->
<!-- FIXME: Fix navigation on mobile -->
<!-- NOTE: This section needs review -->
```

**4. Documentation:**
```html
<!--
    Component: User Profile Card
    Author: John Doe
    Last Modified: 2024-01-15
    Description: Displays user information
-->
<div class="user-profile">
    <!-- Content -->
</div>
```

### 2.3.3. Lưu ý về Comments

**Comments không được lồng nhau:**
```html
<!-- ĐÚNG -->
<!-- Comment 1 -->
<!-- Comment 2 -->

<!-- SAI -->
<!-- Comment 1 <!-- Nested comment --> -->
```

**Comments không ẩn JavaScript/CSS hoàn toàn:**
```html
<!-- <script>
    // Code này vẫn chạy trong một số trường hợp
    alert('Hello');
</script> -->
```

**Tránh để thông tin nhạy cảm trong comments:**
```html
<!-- SAI - không nên -->
<!-- Database password: mypassword123 -->
<!-- API Key: abc123xyz -->
```

## 2.4. HTML Entities

### 2.4.1. Khái niệm

HTML entities được dùng để hiển thị các ký tự đặc biệt:
```html
Cú pháp: &entity_name; hoặc &#entity_number;
```

### 2.4.2. Các entities phổ biến

| Ký tự | Entity Name | Entity Number | Mô tả |
|-------|-------------|---------------|-------|
| < | `&lt;` | `&#60;` | Less than |
| > | `&gt;` | `&#62;` | Greater than |
| & | `&amp;` | `&#38;` | Ampersand |
| " | `&quot;` | `&#34;` | Quotation mark |
| ' | `&apos;` | `&#39;` | Apostrophe |
| | `&nbsp;` | `&#160;` | Non-breaking space |
| © | `&copy;` | `&#169;` | Copyright |
| ® | `&reg;` | `&#174;` | Registered |
| ™ | `&trade;` | `&#8482;` | Trademark |
| € | `&euro;` | `&#8364;` | Euro |
| £ | `&pound;` | `&#163;` | Pound |
| ¥ | `&yen;` | `&#165;` | Yen |

### 2.4.3. Ví dụ sử dụng

```html
<!-- Hiển thị HTML code -->
<p>Để tạo đoạn văn, dùng thẻ &lt;p&gt;&lt;/p&gt;</p>

<!-- Ký tự đặc biệt -->
<p>&copy; 2024 Company Name. All rights reserved.</p>

<!-- Spaces -->
<p>Text with&nbsp;&nbsp;&nbsp;multiple spaces</p>

<!-- Math symbols -->
<p>5 &lt; 10 &amp; 10 &gt; 5</p>

<!-- Currency -->
<p>Price: &euro;99.99</p>
```

### 2.4.4. Non-breaking space

```html
<!-- Tránh xuống dòng giữa số và đơn vị -->
<p>Giá: 100&nbsp;000 VNĐ</p>
<p>Mr.&nbsp;John Doe</p>
```

## 2.5. Whitespace và Line Breaks

### 2.5.1. Whitespace collapsing

HTML tự động gộp nhiều spaces thành 1:
```html
<p>This    is    a    paragraph</p>
<!-- Hiển thị: This is a paragraph -->

<p>
    This is a
    paragraph with
    line breaks
</p>
<!-- Hiển thị: This is a paragraph with line breaks -->
```

### 2.5.2. Preserving whitespace

**Sử dụng `<pre>` tag:**
```html
<pre>
    This    text
    preserves   spacing
        and line breaks
</pre>
```

**Sử dụng CSS:**
```html
<p style="white-space: pre;">
    This    text
    preserves   spacing
</p>

<p style="white-space: pre-line;">
    This text
    preserves line breaks only
</p>

<p style="white-space: pre-wrap;">
    This text preserves spaces
    and wraps long lines
</p>
```

### 2.5.3. Line breaks

**`<br>` tag:**
```html
<p>
    Line 1<br>
    Line 2<br>
    Line 3
</p>
```

**`<wbr>` tag (Word Break Opportunity):**
```html
<p>
    very<wbr>long<wbr>word<wbr>that<wbr>can<wbr>break
</p>
```

**Horizontal rule `<hr>`:**
```html
<p>Content above</p>
<hr>
<p>Content below</p>
```

## 2.6. HTML Document Structure

### 2.6.1. Document outline

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <!-- Metadata -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Title</title>

    <!-- External Resources -->
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="favicon.ico">

    <!-- SEO -->
    <meta name="description" content="Page description">
    <meta name="keywords" content="keyword1, keyword2">

    <!-- Social Media -->
    <meta property="og:title" content="Title">
    <meta property="og:description" content="Description">
    <meta property="og:image" content="image.jpg">
</head>
<body>
    <!-- Page Structure -->
    <header>
        <nav></nav>
    </header>

    <main>
        <article></article>
        <aside></aside>
    </main>

    <footer></footer>

    <!-- Scripts -->
    <script src="script.js"></script>
</body>
</html>
```

### 2.6.2. Head elements chi tiết

#### Meta tags
```html
<!-- Character encoding -->
<meta charset="UTF-8">

<!-- Viewport for responsive design -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Description -->
<meta name="description" content="Page description for SEO">

<!-- Keywords -->
<meta name="keywords" content="HTML, CSS, JavaScript">

<!-- Author -->
<meta name="author" content="Author Name">

<!-- Robots -->
<meta name="robots" content="index, follow">

<!-- Refresh/Redirect -->
<meta http-equiv="refresh" content="30">
<meta http-equiv="refresh" content="0; url=https://example.com">

<!-- IE Compatibility -->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

#### Link tags
```html
<!-- Stylesheet -->
<link rel="stylesheet" href="styles.css">

<!-- Favicon -->
<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="favicon.ico">

<!-- Apple Touch Icon -->
<link rel="apple-touch-icon" href="apple-icon.png">

<!-- Preload -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>

<!-- Preconnect -->
<link rel="preconnect" href="https://fonts.googleapis.com">

<!-- Alternate (for translations) -->
<link rel="alternate" hreflang="en" href="https://example.com/en/">
```

#### Title
```html
<title>Page Title - Site Name</title>
```

#### Base
```html
<base href="https://example.com/" target="_blank">
```

#### Style (inline CSS)
```html
<style>
    body {
        font-family: Arial, sans-serif;
    }
</style>
```

#### Script
```html
<!-- External -->
<script src="script.js"></script>

<!-- Inline -->
<script>
    console.log('Hello World');
</script>

<!-- Async/Defer -->
<script async src="script.js"></script>
<script defer src="script.js"></script>
```

## 2.7. Nesting rules và Best Practices

### 2.7.1. Quy tắc lồng ghép

**Đúng:**
```html
<div>
    <h1>Title</h1>
    <p>Paragraph with <strong>bold text</strong></p>
</div>
```

**Sai:**
```html
<!-- Không đóng đúng thứ tự -->
<div><p>Text</div></p>

<!-- Block element trong inline element -->
<span><div>Text</div></span>

<!-- p không được chứa p -->
<p><p>Text</p></p>

<!-- a không được chứa a -->
<a href="#"><a href="#">Link</a></a>
```

### 2.7.2. Content models

HTML5 phân loại elements theo content model:

1. **Flow content**: Hầu hết elements
2. **Phrasing content**: Inline elements và text
3. **Heading content**: h1-h6
4. **Sectioning content**: article, aside, nav, section
5. **Embedded content**: audio, canvas, img, video
6. **Interactive content**: a, button, input

**Quy tắc:**
- **Phrasing content** không thể chứa **flow content**
- **Paragraph** chỉ có thể chứa **phrasing content**

### 2.7.3. Indentation và formatting

**Good formatting:**
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Link 1</a></li>
                <li><a href="#">Link 2</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article>
            <h1>Title</h1>
            <p>Paragraph</p>
        </article>
    </main>
</body>
</html>
```

**Lưu ý:**
- Dùng 2 hoặc 4 spaces cho indentation (nhất quán trong cả project)
- Mỗi nested level tăng thêm 1 indent
- Đóng tag cùng level với opening tag

## 2.8. Ví dụ code thực tế

### Ví dụ 1: Business Card với Attributes

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Card - Nguyễn Văn A</title>
    <style>
        .card {
            width: 400px;
            padding: 2rem;
            border: 2px solid #333;
            border-radius: 10px;
            margin: 2rem auto;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-family: Arial, sans-serif;
        }
        .name { font-size: 2rem; font-weight: bold; margin-bottom: 0.5rem; }
        .title { font-size: 1.2rem; margin-bottom: 1.5rem; opacity: 0.9; }
        .contact-info { line-height: 2; }
        .contact-info a { color: white; text-decoration: none; }
    </style>
</head>
<body>
    <!-- Business Card Component -->
    <div class="card"
         id="business-card"
         data-user-id="12345"
         data-department="Sales"
         itemscope
         itemtype="http://schema.org/Person">

        <div class="name" itemprop="name">Nguyễn Văn A</div>
        <div class="title" itemprop="jobTitle">Senior Web Developer</div>

        <div class="contact-info">
            <div itemprop="telephone">
                <strong>Phone:</strong>
                <a href="tel:+84123456789" title="Call me">+84 123 456 789</a>
            </div>
            <div itemprop="email">
                <strong>Email:</strong>
                <a href="mailto:nguyenvana@example.com"
                   title="Send email">nguyenvana@example.com</a>
            </div>
            <div itemprop="url">
                <strong>Website:</strong>
                <a href="https://example.com"
                   target="_blank"
                   rel="noopener noreferrer"
                   title="Visit website">example.com</a>
            </div>
        </div>
    </div>

    <script>
        // Access custom data attributes
        const card = document.getElementById('business-card');
        console.log('User ID:', card.dataset.userId);
        console.log('Department:', card.dataset.department);
    </script>
</body>
</html>
```

### Ví dụ 2: Interactive Product Card

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Product Card Demo</title>
    <style>
        .product {
            max-width: 350px;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 1.5rem;
            margin: 2rem auto;
        }
        .product img {
            width: 100%;
            border-radius: 8px;
        }
        .badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.85rem;
            margin: 0.5rem 0;
        }
        .badge-new { background: #27ae60; color: white; }
        .badge-sale { background: #e74c3c; color: white; }
        .price {
            font-size: 1.5rem;
            font-weight: bold;
            color: #e74c3c;
            margin: 1rem 0;
        }
        .old-price {
            text-decoration: line-through;
            color: #999;
            margin-right: 0.5rem;
        }
        button {
            width: 100%;
            padding: 0.75rem;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
        }
        button:hover {
            background: #2980b9;
        }
        button:disabled {
            background: #95a5a6;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <article class="product"
             id="product-001"
             data-product-id="001"
             data-product-name="Smartphone XYZ"
             data-product-price="9990000"
             data-product-stock="50"
             data-product-category="Electronics">

        <!-- Product Image -->
        <figure>
            <img src="https://via.placeholder.com/300"
                 alt="Smartphone XYZ - High-end smartphone"
                 loading="lazy"
                 width="300"
                 height="300">
            <figcaption hidden>Product image of Smartphone XYZ</figcaption>
        </figure>

        <!-- Product Badges -->
        <div>
            <span class="badge badge-new" title="New arrival">New</span>
            <span class="badge badge-sale" title="On sale">Sale 20%</span>
        </div>

        <!-- Product Info -->
        <h2>Smartphone XYZ</h2>
        <p>High-performance smartphone with advanced camera system and long battery life</p>

        <!-- Specifications -->
        <details>
            <summary style="cursor: pointer; font-weight: bold; margin: 1rem 0;">
                Technical Specifications
            </summary>
            <ul style="line-height: 2;">
                <li>RAM: 8GB</li>
                <li>Storage: 128GB</li>
                <li>Display: 6.5" OLED</li>
                <li>Battery: 5000mAh</li>
            </ul>
        </details>

        <!-- Price -->
        <div class="price">
            <span class="old-price">12&nbsp;490&nbsp;000₫</span>
            <span>9&nbsp;990&nbsp;000₫</span>
        </div>

        <!-- Actions -->
        <button type="button"
                id="addToCartBtn"
                data-action="add-to-cart"
                aria-label="Add Smartphone XYZ to cart"
                accesskey="a">
            Add to Cart (Alt+A)
        </button>

        <!-- Hidden metadata -->
        <meta itemprop="sku" content="SMARTPHONE-XYZ-001">
        <meta itemprop="availability" content="https://schema.org/InStock">
    </article>

    <script>
        const button = document.getElementById('addToCartBtn');
        const product = document.getElementById('product-001');

        button.addEventListener('click', function() {
            // Get product data
            const productData = {
                id: product.dataset.productId,
                name: product.dataset.productName,
                price: product.dataset.productPrice,
                stock: product.dataset.productStock
            };

            console.log('Adding to cart:', productData);
            alert(`Added ${productData.name} to cart!`);

            // Simulate stock decrease
            product.dataset.productStock = parseInt(product.dataset.productStock) - 1;

            // Disable if out of stock
            if (product.dataset.productStock <= 0) {
                button.disabled = true;
                button.textContent = 'Out of Stock';
            }
        });
    </script>
</body>
</html>
```

### Ví dụ 3: Form với Multiple Attributes

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Form Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        input, select, textarea {
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: #3498db;
        }
        input:valid {
            border-color: #27ae60;
        }
        input:invalid:not(:focus):not(:placeholder-shown) {
            border-color: #e74c3c;
        }
        .error {
            color: #e74c3c;
            font-size: 0.875rem;
            margin-top: 0.25rem;
            display: none;
        }
        button {
            padding: 1rem 2rem;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
        }
        [contenteditable] {
            border: 2px dashed #ddd;
            padding: 1rem;
            min-height: 100px;
            background: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Advanced Form with Attributes</h1>

    <form id="advancedForm"
          action="/submit"
          method="POST"
          autocomplete="on"
          novalidate>

        <!-- Text Input with Multiple Attributes -->
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text"
                   id="username"
                   name="username"
                   class="form-control"
                   placeholder="Enter username (3-20 characters)"
                   required
                   minlength="3"
                   maxlength="20"
                   pattern="[A-Za-z0-9_]+"
                   autocomplete="username"
                   autofocus
                   spellcheck="false"
                   title="Username can only contain letters, numbers, and underscores"
                   aria-label="Username"
                   aria-describedby="username-help"
                   data-validate="username">
            <small id="username-help">Only letters, numbers, and underscores allowed</small>
            <div class="error">Please enter a valid username</div>
        </div>

        <!-- Email with Autocomplete -->
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email"
                   id="email"
                   name="email"
                   placeholder="your.email@example.com"
                   required
                   autocomplete="email"
                   aria-label="Email address"
                   data-validate="email">
        </div>

        <!-- Password -->
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password"
                   id="password"
                   name="password"
                   placeholder="Minimum 8 characters"
                   required
                   minlength="8"
                   autocomplete="new-password"
                   aria-label="Password"
                   data-validate="password">
        </div>

        <!-- Select with Multiple -->
        <div class="form-group">
            <label for="skills">Skills (hold Ctrl to select multiple):</label>
            <select id="skills"
                    name="skills"
                    multiple
                    size="5"
                    aria-label="Select your skills"
                    data-category="professional">
                <optgroup label="Frontend">
                    <option value="html">HTML5</option>
                    <option value="css">CSS3</option>
                    <option value="js">JavaScript</option>
                </optgroup>
                <optgroup label="Backend">
                    <option value="node">Node.js</option>
                    <option value="python">Python</option>
                    <option value="php">PHP</option>
                </optgroup>
            </select>
        </div>

        <!-- Textarea -->
        <div class="form-group">
            <label for="bio">Bio:</label>
            <textarea id="bio"
                      name="bio"
                      rows="5"
                      cols="50"
                      placeholder="Tell us about yourself..."
                      maxlength="500"
                      spellcheck="true"
                      wrap="soft"
                      aria-label="Biography"
                      data-max-chars="500"></textarea>
            <small><span id="charCount">0</span>/500 characters</small>
        </div>

        <!-- Contenteditable -->
        <div class="form-group">
            <label>Rich Text Editor (editable):</label>
            <div contenteditable="true"
                 spellcheck="true"
                 role="textbox"
                 aria-label="Rich text editor"
                 data-placeholder="Start typing...">
                You can <strong>format</strong> text here with <em>HTML</em>
            </div>
        </div>

        <!-- Draggable -->
        <div class="form-group">
            <p>Draggable items (try to drag these):</p>
            <div draggable="true"
                 style="padding: 1rem; background: #3498db; color: white;
                        margin: 0.5rem 0; cursor: move; border-radius: 5px;">
                Drag me!
            </div>
        </div>

        <!-- Hidden Fields -->
        <input type="hidden" name="user_id" value="12345">
        <input type="hidden" name="timestamp" value="2024-01-15T10:30:00">

        <!-- Submit Button -->
        <button type="submit"
                id="submitBtn"
                accesskey="s"
                title="Submit form (Alt+S)">
            Submit Form
        </button>
    </form>

    <script>
        // Character counter
        const bio = document.getElementById('bio');
        const charCount = document.getElementById('charCount');

        bio.addEventListener('input', function() {
            charCount.textContent = this.value.length;
        });

        // Form validation
        const form = document.getElementById('advancedForm');
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get all form data including data attributes
            const formData = new FormData(form);
            const allInputs = form.querySelectorAll('[data-validate]');

            allInputs.forEach(input => {
                console.log(`${input.name}:`, input.value);
                console.log(`Validation type:`, input.dataset.validate);
            });

            alert('Form submitted! Check console for data.');
        });

        // Drag and drop demo
        const draggable = document.querySelector('[draggable="true"]');

        draggable.addEventListener('dragstart', function(e) {
            e.dataTransfer.effectAllowed = 'move';
            e.dataTransfer.setData('text/html', this.innerHTML);
            this.style.opacity = '0.5';
        });

        draggable.addEventListener('dragend', function() {
            this.style.opacity = '1';
        });
    </script>
</body>
</html>
```

### Ví dụ 4: SEO-Optimized Article

```html
<!DOCTYPE html>
<html lang="vi" prefix="og: http://ogp.me/ns#">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Primary Meta Tags -->
    <title>Complete Guide to HTML5 Attributes | Web Development Tutorial</title>
    <meta name="title" content="Complete Guide to HTML5 Attributes">
    <meta name="description" content="Learn everything about HTML5 attributes with practical examples, best practices, and real-world use cases. Perfect for beginners and professionals.">
    <meta name="keywords" content="HTML5, attributes, web development, tutorial, guide">
    <meta name="author" content="Nguyễn Văn A">
    <meta name="robots" content="index, follow">
    <meta name="language" content="Vietnamese">
    <meta name="revisit-after" content="7 days">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://example.com/html5-attributes-guide">
    <meta property="og:title" content="Complete Guide to HTML5 Attributes">
    <meta property="og:description" content="Learn everything about HTML5 attributes with practical examples">
    <meta property="og:image" content="https://example.com/images/html5-guide.jpg">
    <meta property="og:site_name" content="Web Dev Tutorials">
    <meta property="article:published_time" content="2024-01-15T08:00:00+00:00">
    <meta property="article:modified_time" content="2024-01-15T08:00:00+00:00">
    <meta property="article:author" content="Nguyễn Văn A">
    <meta property="article:section" content="Tutorial">
    <meta property="article:tag" content="HTML5">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://example.com/html5-attributes-guide">
    <meta property="twitter:title" content="Complete Guide to HTML5 Attributes">
    <meta property="twitter:description" content="Learn everything about HTML5 attributes">
    <meta property="twitter:image" content="https://example.com/images/html5-guide.jpg">
    <meta name="twitter:creator" content="@username">

    <!-- Canonical URL -->
    <link rel="canonical" href="https://example.com/html5-attributes-guide">

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">

    <!-- Preconnect to external domains -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="dns-prefetch" href="https://fonts.googleapis.com">

    <!-- Structured Data (JSON-LD) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "Complete Guide to HTML5 Attributes",
      "description": "Learn everything about HTML5 attributes with practical examples",
      "image": "https://example.com/images/html5-guide.jpg",
      "author": {
        "@type": "Person",
        "name": "Nguyễn Văn A",
        "url": "https://example.com/author/nguyenvana"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Web Dev Tutorials",
        "logo": {
          "@type": "ImageObject",
          "url": "https://example.com/logo.png"
        }
      },
      "datePublished": "2024-01-15",
      "dateModified": "2024-01-15"
    }
    </script>

    <style>
        body {
            font-family: Georgia, serif;
            line-height: 1.8;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        article {
            margin-bottom: 3rem;
        }
        time {
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <!-- Breadcrumb Navigation -->
    <nav aria-label="Breadcrumb">
        <ol itemscope itemtype="https://schema.org/BreadcrumbList">
            <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a itemprop="item" href="/">
                    <span itemprop="name">Home</span>
                </a>
                <meta itemprop="position" content="1">
            </li>
            &gt;
            <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a itemprop="item" href="/tutorials">
                    <span itemprop="name">Tutorials</span>
                </a>
                <meta itemprop="position" content="2">
            </li>
            &gt;
            <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <span itemprop="name">HTML5 Attributes</span>
                <meta itemprop="position" content="3">
            </li>
        </ol>
    </nav>

    <!-- Main Article -->
    <article itemscope itemtype="https://schema.org/Article">
        <header>
            <h1 itemprop="headline">Complete Guide to HTML5 Attributes</h1>

            <div class="meta">
                <time datetime="2024-01-15T08:00:00+00:00" itemprop="datePublished">
                    Published: January 15, 2024
                </time>
                |
                <span itemprop="author" itemscope itemtype="https://schema.org/Person">
                    By <span itemprop="name">Nguyễn Văn A</span>
                </span>
                |
                <span>Reading time: 10 minutes</span>
            </div>
        </header>

        <div itemprop="articleBody">
            <p>
                <strong>HTML attributes</strong> are special words used inside the opening tag
                to control the element's behavior or provide additional information about elements.
            </p>

            <h2>What are Attributes?</h2>
            <p>
                Attributes provide additional information about HTML elements. They are always
                specified in the opening tag and usually come in name/value pairs like
                <code>name="value"</code>.
            </p>

            <!-- More content here -->
        </div>
    </article>

    <!-- Author Bio -->
    <aside itemscope itemtype="https://schema.org/Person">
        <h3>About the Author</h3>
        <p>
            <strong itemprop="name">Nguyễn Văn A</strong> is a
            <span itemprop="jobTitle">Senior Web Developer</span> with over 10 years
            of experience in web development. He specializes in HTML5, CSS3, and JavaScript.
        </p>
        <p>
            Contact: <a href="mailto:nguyenvana@example.com" itemprop="email">
            nguyenvana@example.com</a>
        </p>
    </aside>
</body>
</html>
```

### Ví dụ 5: Accessibility-Focused Page

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessible Web Page Example</title>
    <style>
        :focus {
            outline: 3px solid #3498db;
            outline-offset: 2px;
        }
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: #000;
            color: #fff;
            padding: 8px;
            text-decoration: none;
        }
        .skip-link:focus {
            top: 0;
        }
        [aria-hidden="true"] {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Skip Navigation Link -->
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <!-- Accessible Navigation -->
    <nav role="navigation" aria-label="Main navigation">
        <ul role="menubar">
            <li role="none">
                <a href="/" role="menuitem" aria-current="page">Home</a>
            </li>
            <li role="none">
                <a href="/about" role="menuitem">About</a>
            </li>
            <li role="none">
                <a href="/contact" role="menuitem">Contact</a>
            </li>
        </ul>
    </nav>

    <!-- Main Content with ARIA Landmarks -->
    <main id="main-content" role="main" aria-labelledby="page-title">
        <h1 id="page-title">Accessible Web Page</h1>

        <!-- Form with Accessibility -->
        <form role="form" aria-label="Contact form">
            <div>
                <label for="name" id="name-label">
                    Name <span aria-label="required">*</span>
                </label>
                <input type="text"
                       id="name"
                       name="name"
                       required
                       aria-required="true"
                       aria-labelledby="name-label"
                       aria-describedby="name-error">
                <span id="name-error"
                      role="alert"
                      aria-live="polite"
                      hidden>
                    Please enter your name
                </span>
            </div>

            <!-- Button with ARIA -->
            <button type="submit"
                    aria-label="Submit contact form">
                Submit
            </button>
        </form>

        <!-- Alert Box -->
        <div role="alert"
             aria-live="assertive"
             aria-atomic="true"
             hidden
             id="notification">
            Form submitted successfully!
        </div>

        <!-- Progress Bar -->
        <div role="progressbar"
             aria-valuenow="75"
             aria-valuemin="0"
             aria-valuemax="100"
             aria-label="Upload progress">
            75% Complete
        </div>

        <!-- Tab Panel -->
        <div role="tablist" aria-label="Content tabs">
            <button role="tab"
                    aria-selected="true"
                    aria-controls="tab1-panel"
                    id="tab1"
                    tabindex="0">
                Tab 1
            </button>
            <button role="tab"
                    aria-selected="false"
                    aria-controls="tab2-panel"
                    id="tab2"
                    tabindex="-1">
                Tab 2
            </button>
        </div>

        <div role="tabpanel"
             id="tab1-panel"
             aria-labelledby="tab1"
             tabindex="0">
            Content for Tab 1
        </div>

        <div role="tabpanel"
             id="tab2-panel"
             aria-labelledby="tab2"
             hidden
             tabindex="0">
            Content for Tab 2
        </div>

        <!-- Hidden content for screen readers only -->
        <span class="sr-only" aria-label="Additional information">
            This page is optimized for screen readers
        </span>

        <!-- Decorative image (hidden from screen readers) -->
        <img src="decoration.jpg" alt="" aria-hidden="true" role="presentation">

        <!-- Informative image (important for screen readers) -->
        <img src="chart.jpg"
             alt="Sales chart showing 20% increase in Q4 2024"
             aria-describedby="chart-desc">
        <p id="chart-desc" hidden>
            Detailed description: The chart shows monthly sales data...
        </p>
    </main>

    <aside role="complementary" aria-label="Related content">
        <h2>Related Articles</h2>
        <!-- Content -->
    </aside>

    <footer role="contentinfo" aria-label="Site footer">
        <p>&copy; 2024 Example Site</p>
    </footer>
</body>
</html>
```

## 2.9. Use Cases Thực Tế

### 2.9.1. E-commerce Product Listing
```html
<!-- Product with structured data and attributes -->
<article class="product"
         data-product-id="SKU-12345"
         data-category="electronics"
         data-price="999.99"
         itemscope
         itemtype="https://schema.org/Product">
    <h3 itemprop="name">Product Name</h3>
    <img src="product.jpg" alt="Product" itemprop="image">
    <p itemprop="description">Product description</p>
    <span itemprop="offers" itemscope itemtype="https://schema.org/Offer">
        <meta itemprop="priceCurrency" content="USD">
        <span itemprop="price">$999.99</span>
    </span>
</article>
```

### 2.9.2. Blog with Comments
```html
<!-- Article with semantic structure -->
<article class="blog-post"
         data-post-id="123"
         data-author-id="456"
         data-category="technology">
    <header>
        <h1>Article Title</h1>
        <time datetime="2024-01-15">January 15, 2024</time>
    </header>
    <div class="content">
        <!-- Article content -->
    </div>
    <footer>
        <div class="tags">
            <a href="#" rel="tag">HTML5</a>
            <a href="#" rel="tag">Tutorial</a>
        </div>
    </footer>
</article>

<!-- Comments section -->
<section class="comments" aria-label="Comments">
    <div class="comment"
         data-comment-id="1"
         data-author="user123"
         itemscope
         itemtype="https://schema.org/Comment">
        <p itemprop="text">Great article!</p>
        <meta itemprop="datePublished" content="2024-01-15">
    </div>
</section>
```

### 2.9.3. Dashboard with Interactive Elements
```html
<!-- Widget with data attributes for JavaScript -->
<div class="widget"
     id="sales-widget"
     data-widget-type="chart"
     data-refresh-interval="5000"
     data-api-endpoint="/api/sales"
     data-chart-type="line"
     role="region"
     aria-label="Sales chart">
    <h3>Sales Overview</h3>
    <canvas id="sales-chart" aria-label="Sales data visualization"></canvas>
</div>
```

### 2.9.4. Form with Validation
```html
<!-- Contact form with comprehensive attributes -->
<form action="/contact"
      method="POST"
      id="contact-form"
      data-form-type="contact"
      data-validation="true"
      novalidate>

    <input type="text"
           name="name"
           id="name"
           required
           minlength="2"
           maxlength="50"
           pattern="[A-Za-z\s]+"
           data-error-message="Please enter a valid name"
           aria-label="Full name"
           aria-required="true">

    <input type="email"
           name="email"
           id="email"
           required
           data-validate="email"
           aria-label="Email address">

    <button type="submit"
            data-action="submit-contact"
            aria-label="Submit contact form">
        Send Message
    </button>
</form>
```

## 2.10. Tips & Tricks

### 2.10.1. Attributes Tips

**Tip 1: Use data attributes for JavaScript**
```html
<!-- Instead of classes for JavaScript -->
<!-- BAD -->
<button class="js-delete-btn">Delete</button>

<!-- GOOD -->
<button data-action="delete" data-id="123">Delete</button>
```

**Tip 2: Boolean attributes shorthand**
```html
<!-- All equivalent -->
<input type="checkbox" checked>
<input type="checkbox" checked="">
<input type="checkbox" checked="checked">

<!-- Use shortest form -->
<input type="checkbox" checked>
```

**Tip 3: Multiple classes**
```html
<!-- Separate concerns -->
<div class="component component--large component--active theme-dark">
    Content
</div>
```

**Tip 4: Accessible links**
```html
<!-- Always include aria-label for icon-only links -->
<a href="/settings" aria-label="Go to settings">
    <i class="icon-settings" aria-hidden="true"></i>
</a>
```

**Tip 5: Custom validation messages**
```html
<input type="email"
       required
       title="Please enter a valid email address"
       pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$">
```

### 2.10.2. Performance Tips

**Tip 6: Lazy loading images**
```html
<img src="image.jpg"
     alt="Description"
     loading="lazy"
     decoding="async">
```

**Tip 7: Preconnect to external domains**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://cdn.example.com">
```

**Tip 8: Async/Defer for scripts**
```html
<!-- Async: Download in parallel, execute when ready -->
<script async src="analytics.js"></script>

<!-- Defer: Download in parallel, execute after HTML parsed -->
<script defer src="app.js"></script>
```

### 2.10.3. SEO Tips

**Tip 9: Proper meta tags**
```html
<meta name="description" content="Concise description (155-160 chars)">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://example.com/page">
```

**Tip 10: Structured data**
```html
<!-- Use schema.org markup -->
<div itemscope itemtype="https://schema.org/Article">
    <h1 itemprop="headline">Title</h1>
    <time itemprop="datePublished" datetime="2024-01-15">Jan 15, 2024</time>
</div>
```

## 2.11. Common Mistakes

### 2.11.1. Attribute Mistakes

**Mistake 1: Duplicate IDs**
```html
<!-- WRONG -->
<div id="container">Content 1</div>
<div id="container">Content 2</div>

<!-- CORRECT -->
<div id="container1">Content 1</div>
<div id="container2">Content 2</div>
```

**Mistake 2: Missing quotes**
```html
<!-- WRONG -->
<img src=image.jpg alt=My Image>

<!-- CORRECT -->
<img src="image.jpg" alt="My Image">
```

**Mistake 3: Wrong attribute usage**
```html
<!-- WRONG - href on div -->
<div href="/page">Link</div>

<!-- CORRECT -->
<a href="/page">Link</a>
```

**Mistake 4: Invalid nesting**
```html
<!-- WRONG -->
<p><div>Content</div></p>

<!-- CORRECT -->
<div><p>Content</p></div>
```

### 2.11.2. Comment Mistakes

**Mistake 5: Nested comments**
```html
<!-- WRONG -->
<!-- Outer comment <!-- Inner comment --> -->

<!-- CORRECT -->
<!-- Comment 1 -->
<!-- Comment 2 -->
```

**Mistake 6: Sensitive info in comments**
```html
<!-- WRONG -->
<!-- TODO: Change password from admin123 -->

<!-- CORRECT -->
<!-- TODO: Update authentication -->
```

### 2.11.3. Entity Mistakes

**Mistake 7: Not escaping HTML**
```html
<!-- WRONG - will break layout -->
<p>Use <div> for containers</p>

<!-- CORRECT -->
<p>Use &lt;div&gt; for containers</p>
```

## 2.12. Troubleshooting

### Problem 1: Attribute not working
**Solution:**
- Check spelling
- Verify browser support
- Check if attribute is valid for that element
- Use browser DevTools to inspect

### Problem 2: ID selector not working
**Solution:**
```javascript
// Check for duplicate IDs
const ids = document.querySelectorAll('[id]');
const idMap = {};
ids.forEach(el => {
    if (idMap[el.id]) {
        console.error('Duplicate ID:', el.id);
    }
    idMap[el.id] = true;
});
```

### Problem 3: Data attributes not accessible
**Solution:**
```javascript
// Use dataset API
const element = document.getElementById('myElement');
console.log(element.dataset.userId); // data-user-id
console.log(element.dataset.productName); // data-product-name
```

### Problem 4: Boolean attributes confusion
**Solution:**
```html
<!-- To enable boolean attribute -->
<input type="checkbox" checked>

<!-- To disable, remove completely -->
<input type="checkbox">

<!-- DON'T use ="false" -->
<input type="checkbox" checked="false"> <!-- Still checked! -->
```

## 2.13. Advanced Topics

### 2.13.1. Custom Elements with Attributes
```html
<my-component
    data-config='{"theme": "dark", "size": "large"}'
    data-initialized="false">
</my-component>

<script>
class MyComponent extends HTMLElement {
    connectedCallback() {
        const config = JSON.parse(this.dataset.config);
        console.log(config);
    }
}
customElements.define('my-component', MyComponent);
</script>
```

### 2.13.2. Attribute Observers
```javascript
// Watch for attribute changes
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.type === 'attributes') {
            console.log('Attribute changed:', mutation.attributeName);
        }
    });
});

const element = document.getElementById('watched');
observer.observe(element, {
    attributes: true,
    attributeOldValue: true
});
```

### 2.13.3. Dynamic Attributes
```javascript
// Dynamically set attributes
const img = document.createElement('img');
img.setAttribute('src', 'image.jpg');
img.setAttribute('alt', 'Description');
img.setAttribute('loading', 'lazy');
img.dataset.imageId = '123';

// Get attribute
console.log(img.getAttribute('src'));

// Remove attribute
img.removeAttribute('loading');

// Check if attribute exists
if (img.hasAttribute('alt')) {
    console.log('Alt text exists');
}
```

## 2.14. Bài tập thực hành

### Bài 1: Elements và Attributes (Dễ)
Tạo file HTML với:
- 5 block-level elements khác nhau
- 5 inline elements khác nhau
- Mỗi element có ít nhất 2 attributes
- Sử dụng class, id, style

### Bài 2: Comments và Documentation (Dễ)
Tạo một trang HTML và thêm:
- Section comments
- Inline comments
- TODO comments
- Documentation comments cho components

### Bài 3: HTML Entities (Dễ)
Tạo trang hiển thị:
- Một đoạn code HTML (dùng entities)
- Copyright notice
- Math expressions (< > =)
- Currency symbols

### Bài 4: Data Attributes (Dễ)
Tạo danh sách sản phẩm với:
- Mỗi sản phẩm có data-product-id, data-price, data-category
- Button để hiển thị thông tin sản phẩm
- JavaScript để đọc data attributes

### Bài 5: Global Attributes (Trung bình)
Tạo trang demo các global attributes:
- contenteditable div
- draggable elements
- hidden elements (toggle với button)
- Elements với title tooltips
- tabindex demo

### Bài 6: Form với Attributes (Trung bình)
Tạo form đăng ký với:
- Tất cả input types có validation attributes
- Placeholder, pattern, required
- Autocomplete attributes
- Custom data attributes
- ARIA attributes cho accessibility

### Bài 7: SEO-Optimized Page (Trung bình)
Tạo trang với:
- Complete meta tags (description, keywords, author)
- Open Graph tags
- Twitter Card tags
- Structured data (JSON-LD)
- Canonical URL

### Bài 8: Accessible Form (Trung bình)
Tạo form với đầy đủ accessibility:
- ARIA labels
- aria-required, aria-invalid
- aria-describedby cho error messages
- Proper label associations
- Role attributes

### Bài 9: Interactive Dashboard Widget (Khó)
Tạo widget dashboard với:
- Multiple data attributes cho configuration
- Dynamic attribute updates với JavaScript
- Attribute-based styling với CSS
- Event handling dựa trên attributes
- LocalStorage để save state

### Bài 10: Complete HTML Document (Khó)
Tạo trang HTML hoàn chỉnh với:
- Proper DOCTYPE
- Complete head section với đầy đủ meta tags
- Semantic HTML structure
- Data attributes cho JavaScript
- ARIA attributes cho accessibility
- Structured data
- Comments document hóa code
- Validate với W3C Validator

### Bài 11: Custom Data Attributes System (Khó)
Tạo hệ thống quản lý:
- Product catalog với data attributes
- Filter system dựa trên attributes
- Sort functionality
- Cart system sử dụng data attributes
- LocalStorage integration

### Bài 12: Advanced Accessibility (Khó)
Tạo trang với:
- Complete ARIA implementation
- Keyboard navigation support
- Screen reader optimization
- Focus management
- Live regions cho dynamic content
- Test với accessibility tools

## 2.9. Câu hỏi ôn tập

1. Sự khác biệt giữa block-level và inline elements là gì?
2. Void elements là gì? Cho 5 ví dụ.
3. Global attributes là gì? Liệt kê 5 global attributes quan trọng.
4. Data attributes được dùng như thế nào?
5. Tại sao phải dùng HTML entities?
6. Whitespace collapsing là gì?
7. Quy tắc nesting elements ra sao?
8. Sự khác biệt giữa id và class?
9. Boolean attributes hoạt động như thế nào?
10. Meta tags quan trọng cho SEO là gì?

---

**Kết luận Chương 2:**
Trong chương này, chúng ta đã học về cấu trúc cơ bản của HTML bao gồm elements, attributes, comments, entities và các quy tắc viết HTML. Đây là nền tảng quan trọng để viết HTML code đúng chuẩn và dễ bảo trì. Chương tiếp theo sẽ đi vào chi tiết về các thẻ văn bản và định dạng.
