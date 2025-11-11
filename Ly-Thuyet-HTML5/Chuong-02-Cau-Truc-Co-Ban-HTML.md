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

## 2.8. Bài tập thực hành

### Bài 1: Elements và Attributes
Tạo file HTML với:
- 5 block-level elements khác nhau
- 5 inline elements khác nhau
- Mỗi element có ít nhất 2 attributes
- Sử dụng class, id, style

### Bài 2: Comments và Documentation
Tạo một trang HTML và thêm:
- Section comments
- Inline comments
- TODO comments
- Documentation comments cho components

### Bài 3: HTML Entities
Tạo trang hiển thị:
- Một đoạn code HTML (dùng entities)
- Copyright notice
- Math expressions (< > =)
- Currency symbols

### Bài 4: Complete HTML Document
Tạo trang HTML hoàn chỉnh với:
- Proper DOCTYPE
- Complete head section với đầy đủ meta tags
- Properly nested body structure
- Comments describing each section
- Validate với W3C Validator

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
