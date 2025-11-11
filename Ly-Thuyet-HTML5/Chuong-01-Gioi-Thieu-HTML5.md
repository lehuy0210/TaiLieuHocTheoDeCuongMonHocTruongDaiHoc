# CHƯƠNG 1: GIỚI THIỆU HTML5

## 1.1. HTML5 là gì?

HTML5 (HyperText Markup Language version 5) là phiên bản mới nhất của ngôn ngữ đánh dấu siêu văn bản HTML, được sử dụng để tạo và cấu trúc nội dung trên web. HTML5 được W3C (World Wide Web Consortium) và WHATWG (Web Hypertext Application Technology Working Group) phát triển.

### 1.1.1. Định nghĩa

HTML5 là một ngôn ngữ đánh dấu dùng để:
- Xác định cấu trúc và nội dung của các trang web
- Tạo ra các ứng dụng web phong phú và tương tác
- Cung cấp các API mạnh mẽ cho việc phát triển web hiện đại
- Hỗ trợ đa phương tiện (audio, video) mà không cần plugin

### 1.1.2. Vai trò trong phát triển web

HTML5 đóng vai trò nền tảng trong bộ ba công nghệ web:
- **HTML5**: Cấu trúc và nội dung
- **CSS3**: Trình bày và thiết kế
- **JavaScript**: Tương tác và logic

## 1.2. Lịch sử phát triển

### 1.2.1. Timeline phát triển

- **1991**: HTML đầu tiên được Tim Berners-Lee tạo ra
- **1995**: HTML 2.0 - phiên bản chuẩn hóa đầu tiên
- **1997**: HTML 3.2 và HTML 4.0
- **1999**: HTML 4.01 - phiên bản ổn định
- **2000**: XHTML 1.0 - kết hợp HTML với XML
- **2004**: WHATWG bắt đầu phát triển HTML5
- **2008**: HTML5 draft đầu tiên được công bố
- **2014**: HTML5 trở thành W3C Recommendation
- **2016**: HTML 5.1 được công bố
- **2017**: HTML 5.2 được công bố
- **2021**: HTML Living Standard (cập nhật liên tục)

### 1.2.2. Sự khác biệt giữa HTML4 và HTML5

| Đặc điểm | HTML4 | HTML5 |
|----------|-------|-------|
| Doctype | Phức tạp và dài | Đơn giản: `<!DOCTYPE html>` |
| Semantic Elements | Hạn chế | Phong phú (header, nav, footer, article, section...) |
| Multimedia | Cần plugin (Flash) | Native support (audio, video) |
| Canvas/SVG | Không hỗ trợ | Hỗ trợ đầy đủ |
| Storage | Cookies | LocalStorage, SessionStorage, IndexedDB |
| Geolocation | Không có | Có API hỗ trợ |
| Offline Support | Không có | Application Cache, Service Workers |
| Forms | Hạn chế | Nhiều input types mới, validation |
| API | Hạn chế | Nhiều API mới (Drag & Drop, Web Workers, WebSocket...) |

## 1.3. Tại sao nên học HTML5?

### 1.3.1. Lý do học HTML5

1. **Nền tảng của Web Development**
   - HTML5 là kiến thức cơ bản bắt buộc cho mọi web developer
   - Hiểu HTML5 giúp làm việc tốt hơn với frameworks (React, Vue, Angular)

2. **Cải thiện SEO**
   - Semantic elements giúp search engines hiểu nội dung tốt hơn
   - Structured data và accessibility tốt hơn

3. **Khả năng tương thích**
   - Hỗ trợ đa nền tảng (desktop, mobile, tablet)
   - Tương thích với mọi trình duyệt hiện đại

4. **Tính năng đa phương tiện**
   - Tích hợp audio, video mà không cần plugin
   - Canvas và SVG cho đồ họa

5. **Hiệu suất cao**
   - Giảm phụ thuộc vào plugin bên thứ ba
   - Tối ưu hóa cho mobile devices

### 1.3.2. Ứng dụng thực tế

HTML5 được sử dụng rộng rãi trong:
- Websites và web applications
- Progressive Web Apps (PWAs)
- Mobile applications (với frameworks như Ionic, Cordova)
- Game development (với Canvas API)
- Ứng dụng đa phương tiện
- Email templates
- E-learning platforms

## 1.4. Cấu trúc cơ bản của một tài liệu HTML5

### 1.4.1. Document type declaration

```html
<!DOCTYPE html>
```

- Khai báo document type ở đầu file
- Cho trình duyệt biết đây là HTML5
- Không phân biệt chữ hoa/thường
- Bắt buộc phải có

### 1.4.2. Cấu trúc tổng quát

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Mô tả trang web">
    <meta name="keywords" content="từ khóa, keywords">
    <meta name="author" content="Tên tác giả">
    <title>Tiêu đề trang</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Nội dung trang web -->
    <header>
        <h1>Tiêu đề chính</h1>
    </header>

    <nav>
        <!-- Menu điều hướng -->
    </nav>

    <main>
        <!-- Nội dung chính -->
        <article>
            <!-- Bài viết -->
        </article>

        <aside>
            <!-- Nội dung phụ -->
        </aside>
    </main>

    <footer>
        <!-- Chân trang -->
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

### 1.4.3. Giải thích các thành phần

#### Thẻ `<html>`
```html
<html lang="vi">
```
- Thẻ gốc của document
- Attribute `lang` xác định ngôn ngữ (vi: tiếng Việt, en: tiếng Anh)
- Giúp screen readers và search engines

#### Thẻ `<head>`
Chứa metadata và thông tin về document:
- `<meta charset="UTF-8">`: Khai báo encoding
- `<meta name="viewport">`: Responsive design cho mobile
- `<title>`: Tiêu đề hiển thị trên tab trình duyệt
- `<link>`: Liên kết CSS, favicon
- `<meta>`: Thông tin SEO

#### Thẻ `<body>`
Chứa toàn bộ nội dung hiển thị trên trang web

## 1.5. Các công cụ cần thiết

### 1.5.1. Text Editors và IDEs

**Text Editors phổ biến:**
1. **Visual Studio Code** (Khuyên dùng)
   - Miễn phí, mã nguồn mở
   - Hỗ trợ extensions phong phú
   - IntelliSense, debugging tốt

2. **Sublime Text**
   - Nhẹ và nhanh
   - Nhiều plugins

3. **Atom**
   - Miễn phí, mã nguồn mở
   - Tùy biến cao

4. **Notepad++**
   - Nhẹ, đơn giản
   - Chỉ cho Windows

**IDEs:**
- WebStorm (trả phí, mạnh mẽ)
- Brackets (Adobe, miễn phí)

### 1.5.2. Trình duyệt web

**Trình duyệt nên sử dụng:**
1. **Google Chrome**
   - Chrome DevTools mạnh mẽ
   - Cập nhật thường xuyên

2. **Mozilla Firefox**
   - Firefox Developer Tools tốt
   - Privacy-focused

3. **Microsoft Edge** (Chromium-based)
   - Hiệu suất tốt
   - Tích hợp Windows

4. **Safari** (cho macOS)
   - Testing trên macOS/iOS

**Developer Tools:**
- Inspect Element (F12)
- Console
- Network tab
- Performance monitoring
- Mobile device simulation

### 1.5.3. Công cụ online

**Editors online:**
- CodePen (https://codepen.io)
- JSFiddle (https://jsfiddle.net)
- JSBin (https://jsbin.com)
- Repl.it (https://replit.com)

**Validators:**
- W3C Markup Validation Service (https://validator.w3.org)
- HTML5 Validator (https://html5.validator.nu)

**Testing tools:**
- BrowserStack (cross-browser testing)
- Can I Use (https://caniuse.com) - kiểm tra browser support

### 1.5.4. Extensions hữu ích cho VS Code

1. **Live Server**
   - Auto-reload khi save file
   - Local development server

2. **HTML CSS Support**
   - IntelliSense cho HTML/CSS

3. **Auto Rename Tag**
   - Tự động đổi tên closing tag

4. **Prettier - Code formatter**
   - Format code tự động

5. **HTML Snippets**
   - Code snippets cho HTML

6. **Path Intellisense**
   - Autocomplete cho file paths

## 1.6. Browser Support và Compatibility

### 1.6.1. Trình duyệt hỗ trợ HTML5

Tất cả trình duyệt hiện đại đều hỗ trợ HTML5:
- Chrome 4.0+
- Firefox 3.5+
- Safari 4.0+
- Edge (tất cả versions)
- Opera 10.5+

### 1.6.2. Kiểm tra browser support

**Sử dụng Can I Use:**
```
https://caniuse.com
```

**Feature detection với Modernizr:**
```html
<script src="modernizr.js"></script>
<script>
if (Modernizr.canvas) {
    // Trình duyệt hỗ trợ Canvas
} else {
    // Không hỗ trợ
}
</script>
```

### 1.6.3. Polyfills cho trình duyệt cũ

**HTML5 Shiv** (cho IE8 và cũ hơn):
```html
<!--[if lt IE 9]>
    <script src="html5shiv.js"></script>
<![endif]-->
```

**Respond.js** (cho media queries trong IE):
```html
<!--[if lt IE 9]>
    <script src="respond.min.js"></script>
<![endif]-->
```

## 1.7. Best Practices khi viết HTML5

### 1.7.1. Nguyên tắc cơ bản

1. **Luôn khai báo DOCTYPE**
```html
<!DOCTYPE html>
```

2. **Sử dụng lowercase cho tags và attributes**
```html
<!-- Tốt -->
<div class="container">

<!-- Không nên -->
<DIV CLASS="container">
```

3. **Đóng tất cả tags**
```html
<!-- Tốt -->
<p>Paragraph</p>
<img src="image.jpg" alt="Description">

<!-- Không nên (nhưng HTML5 cho phép) -->
<p>Paragraph
<img src="image.jpg">
```

4. **Luôn dùng quotes cho attribute values**
```html
<!-- Tốt -->
<img src="image.jpg" alt="Description">

<!-- Không nên -->
<img src=image.jpg alt=Description>
```

5. **Khai báo charset**
```html
<meta charset="UTF-8">
```

### 1.7.2. Semantic HTML

Sử dụng thẻ có ý nghĩa:
```html
<!-- Tốt - Semantic -->
<header>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
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

<!-- Không nên - Non-semantic -->
<div id="header">
    <div id="nav">
        <div>
            <div><a href="#home">Home</a></div>
        </div>
    </div>
</div>
```

### 1.7.3. Accessibility (a11y)

1. **Alt text cho images**
```html
<img src="logo.jpg" alt="Company Logo">
```

2. **Label cho form inputs**
```html
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

3. **ARIA attributes khi cần**
```html
<button aria-label="Close" onclick="closeDialog()">
    <span aria-hidden="true">×</span>
</button>
```

### 1.7.4. Performance

1. **CSS trong `<head>`, JavaScript trước `</body>`**
```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Content -->
    <script src="script.js"></script>
</body>
```

2. **Optimize images**
- Sử dụng định dạng phù hợp (WebP, JPEG, PNG)
- Compress images
- Lazy loading

3. **Minify HTML, CSS, JavaScript**

### 1.7.5. SEO Best Practices

1. **Title tags**
```html
<title>Trang chủ - Tên website</title>
```

2. **Meta descriptions**
```html
<meta name="description" content="Mô tả ngắn gọn về trang web">
```

3. **Heading hierarchy**
```html
<h1>Main Title</h1>
    <h2>Section Title</h2>
        <h3>Subsection</h3>
```

4. **Semantic URLs**
```html
<a href="/san-pham/laptop">Laptop</a>
```

## 1.8. Chuẩn bị cho các chương tiếp theo

Trong các chương tiếp theo, chúng ta sẽ học:
- **Chương 2**: Cấu trúc cơ bản HTML - thẻ, attributes, comments
- **Chương 3**: Các thẻ văn bản và định dạng
- **Chương 4**: Links và Navigation
- **Chương 5**: Hình ảnh và Multimedia
- **Chương 6**: Tables
- **Chương 7**: Forms và Input
- **Chương 8**: HTML5 Semantic Elements
- **Chương 9**: HTML5 APIs
- **Chương 10**: Canvas và SVG
- **Chương 11**: Storage và Offline
- **Chương 12**: Best Practices và Optimization

## 1.9. Bài tập thực hành

### Bài 1: Setup môi trường
1. Cài đặt Visual Studio Code
2. Cài đặt extension Live Server
3. Tạo file `index.html` đầu tiên với cấu trúc HTML5 cơ bản

### Bài 2: Trang HTML5 đơn giản
Tạo một trang HTML5 với:
- DOCTYPE khai báo đúng
- Meta tags đầy đủ (charset, viewport, description)
- Title có ý nghĩa
- Heading h1
- Một đoạn văn bản
- Validate bằng W3C Validator

### Bài 3: So sánh HTML4 vs HTML5
Viết hai file HTML giống nhau về nội dung:
- File 1: Sử dụng HTML4 syntax
- File 2: Sử dụng HTML5 syntax
So sánh và ghi chú sự khác biệt

## 1.10. Tài liệu tham khảo

### 1.10.1. Tài liệu chính thức
- W3C HTML5 Specification: https://www.w3.org/TR/html52/
- WHATWG HTML Living Standard: https://html.spec.whatwg.org/
- MDN Web Docs: https://developer.mozilla.org/en-US/docs/Web/HTML

### 1.10.2. Tutorials và guides
- W3Schools HTML Tutorial: https://www.w3schools.com/html/
- HTML.com: https://html.com/
- HTML5 Doctor: http://html5doctor.com/

### 1.10.3. Tools và validators
- W3C Markup Validation Service: https://validator.w3.org/
- Can I Use: https://caniuse.com/
- HTML5 Test: https://html5test.com/

### 1.10.4. Community và forums
- Stack Overflow: https://stackoverflow.com/questions/tagged/html5
- Reddit r/webdev: https://www.reddit.com/r/webdev/
- Dev.to: https://dev.to/t/html

---

**Kết luận Chương 1:**
Trong chương này, chúng ta đã tìm hiểu về HTML5, lịch sử phát triển, tầm quan trọng, và cách setup môi trường phát triển. Đây là nền tảng quan trọng để bắt đầu hành trình học HTML5. Ở chương tiếp theo, chúng ta sẽ đi sâu vào cấu trúc cơ bản của HTML và các thẻ HTML.
