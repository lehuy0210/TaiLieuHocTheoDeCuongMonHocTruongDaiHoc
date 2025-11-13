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

## 1.9. Ví dụ code thực tế

### Ví dụ 1: Landing Page cơ bản

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Khóa học lập trình web cho người mới bắt đầu">
    <meta name="keywords" content="học lập trình, HTML5, CSS3, JavaScript">
    <title>Học Lập Trình Web - Khóa Học Miễn Phí</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        header { background: #333; color: #fff; padding: 2rem; text-align: center; }
        .hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white; padding: 4rem 2rem; text-align: center; }
        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 2rem; padding: 3rem 2rem; }
        .feature-card { background: #f4f4f4; padding: 2rem; border-radius: 8px; }
        footer { background: #333; color: #fff; text-align: center; padding: 2rem; }
    </style>
</head>
<body>
    <header>
        <nav>
            <h1>WebLearn Academy</h1>
        </nav>
    </header>

    <section class="hero">
        <h2>Học Lập Trình Web Từ Cơ Bản Đến Nâng Cao</h2>
        <p>Khóa học miễn phí, học theo lộ trình chuẩn quốc tế</p>
        <button style="padding: 1rem 2rem; font-size: 1.1rem; margin-top: 1rem;
                       background: white; border: none; border-radius: 5px; cursor: pointer;">
            Đăng Ký Ngay
        </button>
    </section>

    <main>
        <section class="features">
            <article class="feature-card">
                <h3>HTML5 Cơ Bản</h3>
                <p>Học cấu trúc web với HTML5 semantic elements</p>
            </article>
            <article class="feature-card">
                <h3>CSS3 Styling</h3>
                <p>Thiết kế giao diện đẹp với CSS3 và Flexbox/Grid</p>
            </article>
            <article class="feature-card">
                <h3>JavaScript ES6+</h3>
                <p>Làm chủ JavaScript hiện đại và DOM manipulation</p>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 WebLearn Academy. All rights reserved.</p>
    </footer>
</body>
</html>
```

### Ví dụ 2: Blog Post Template

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="10 mẹo học HTML5 hiệu quả cho người mới bắt đầu">
    <meta name="author" content="Nguyễn Văn A">
    <meta property="og:title" content="10 Mẹo Học HTML5 Hiệu Quả">
    <meta property="og:description" content="Khám phá những mẹo hay giúp bạn học HTML5 nhanh hơn">
    <meta property="og:type" content="article">
    <title>10 Mẹo Học HTML5 Hiệu Quả | Tech Blog</title>
    <style>
        body { font-family: Georgia, serif; max-width: 800px; margin: 0 auto; padding: 2rem; }
        article { line-height: 1.8; }
        header { border-bottom: 3px solid #333; padding-bottom: 1rem; margin-bottom: 2rem; }
        .meta { color: #666; font-size: 0.9rem; margin: 1rem 0; }
        .content p { margin-bottom: 1.5rem; }
        .author-bio { background: #f9f9f9; padding: 1.5rem; margin-top: 3rem; border-radius: 8px; }
    </style>
</head>
<body>
    <article>
        <header>
            <h1>10 Mẹo Học HTML5 Hiệu Quả Cho Người Mới Bắt Đầu</h1>
            <div class="meta">
                <time datetime="2024-01-15">15 tháng 1, 2024</time> |
                <span>Bởi <strong>Nguyễn Văn A</strong></span> |
                <span>5 phút đọc</span>
            </div>
        </header>

        <section class="content">
            <p>
                <strong>HTML5</strong> là ngôn ngữ nền tảng cho mọi trang web hiện đại.
                Nếu bạn đang bắt đầu hành trình trở thành web developer, việc nắm vững
                HTML5 là bước đầu tiên quan trọng nhất.
            </p>

            <h2>1. Thực hành hàng ngày</h2>
            <p>
                Không có cách nào tốt hơn để học HTML5 ngoài việc thực hành mỗi ngày.
                Hãy dành ít nhất 30 phút mỗi ngày để code HTML, dù chỉ là những trang web đơn giản.
            </p>

            <h2>2. Sử dụng Developer Tools</h2>
            <p>
                Trình duyệt Chrome và Firefox đều có Developer Tools mạnh mẽ.
                Nhấn F12 và khám phá cách các website khác được xây dựng.
            </p>

            <h2>3. Validate code thường xuyên</h2>
            <p>
                Sử dụng W3C Validator để kiểm tra code của bạn. Điều này giúp bạn
                phát hiện lỗi sớm và học cách viết code chuẩn.
            </p>
        </section>

        <aside class="author-bio">
            <h3>Về tác giả</h3>
            <p>
                <strong>Nguyễn Văn A</strong> là web developer với 5 năm kinh nghiệm.
                Anh đam mê chia sẻ kiến thức về web development cho cộng đồng.
            </p>
        </aside>
    </article>

    <nav>
        <h3>Bài viết liên quan:</h3>
        <ul>
            <li><a href="#">CSS3 cho người mới bắt đầu</a></li>
            <li><a href="#">JavaScript ES6 cơ bản</a></li>
            <li><a href="#">Responsive Design với HTML5</a></li>
        </ul>
    </nav>
</body>
</html>
```

### Ví dụ 3: E-commerce Product Page

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Laptop Dell XPS 13 - Hiệu năng cao, thiết kế sang trọng">
    <meta name="keywords" content="laptop dell, dell xps 13, mua laptop">
    <title>Dell XPS 13 - Laptop Cao Cấp | TechStore</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
        .product { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; }
        .product-image { width: 100%; border-radius: 8px; }
        .price { color: #e74c3c; font-size: 2rem; font-weight: bold; margin: 1rem 0; }
        .add-to-cart { background: #27ae60; color: white; padding: 1rem 2rem;
                       border: none; border-radius: 5px; font-size: 1.1rem; cursor: pointer; }
        .specs { margin-top: 2rem; }
        .spec-item { display: flex; justify-content: space-between;
                     padding: 0.5rem 0; border-bottom: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <nav aria-label="breadcrumb">
            <a href="/">Trang chủ</a> &gt;
            <a href="/laptops">Laptop</a> &gt;
            <span>Dell XPS 13</span>
        </nav>

        <main class="product">
            <figure>
                <img src="dell-xps-13.jpg" alt="Laptop Dell XPS 13" class="product-image">
                <figcaption>Dell XPS 13 - Thiết kế InfinityEdge</figcaption>
            </figure>

            <article>
                <h1>Laptop Dell XPS 13 (2024)</h1>
                <p class="price">29.990.000₫</p>

                <section>
                    <h2>Mô tả sản phẩm</h2>
                    <p>
                        Dell XPS 13 là dòng laptop cao cấp với thiết kế siêu mỏng nhẹ,
                        màn hình InfinityEdge tràn viền, hiệu năng mạnh mẽ với chip Intel
                        thế hệ mới nhất. Hoàn hảo cho doanh nhân và sáng tạo nội dung.
                    </p>
                </section>

                <section class="specs">
                    <h2>Thông số kỹ thuật</h2>
                    <div class="spec-item">
                        <span>CPU:</span>
                        <strong>Intel Core i7-1365U</strong>
                    </div>
                    <div class="spec-item">
                        <span>RAM:</span>
                        <strong>16GB LPDDR5</strong>
                    </div>
                    <div class="spec-item">
                        <span>Storage:</span>
                        <strong>512GB NVMe SSD</strong>
                    </div>
                    <div class="spec-item">
                        <span>Display:</span>
                        <strong>13.4" FHD+ (1920x1200)</strong>
                    </div>
                    <div class="spec-item">
                        <span>Weight:</span>
                        <strong>1.2kg</strong>
                    </div>
                </section>

                <button class="add-to-cart" type="button">
                    Thêm vào giỏ hàng
                </button>

                <details style="margin-top: 2rem;">
                    <summary style="cursor: pointer; font-weight: bold;">Chính sách bảo hành</summary>
                    <ul style="margin-top: 1rem; line-height: 2;">
                        <li>Bảo hành 12 tháng chính hãng</li>
                        <li>Đổi mới trong 7 ngày nếu có lỗi từ nhà sản xuất</li>
                        <li>Hỗ trợ kỹ thuật miễn phí trọn đời</li>
                    </ul>
                </details>
            </article>
        </main>
    </div>
</body>
</html>
```

### Ví dụ 4: Portfolio Website

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Portfolio của Nguyễn Văn A - Web Developer & Designer">
    <meta name="author" content="Nguyễn Văn A">
    <title>Nguyễn Văn A - Web Developer Portfolio</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', sans-serif; }
        header { background: #2c3e50; color: white; padding: 4rem 2rem; text-align: center; }
        .avatar { width: 150px; height: 150px; border-radius: 50%;
                  border: 5px solid white; margin-bottom: 1rem; }
        nav { background: #34495e; padding: 1rem; position: sticky; top: 0; z-index: 100; }
        nav ul { list-style: none; display: flex; justify-content: center; gap: 2rem; }
        nav a { color: white; text-decoration: none; font-weight: bold; }
        section { padding: 4rem 2rem; max-width: 1200px; margin: 0 auto; }
        .projects { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
        .project-card { background: #f8f9fa; padding: 1.5rem; border-radius: 8px;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        footer { background: #2c3e50; color: white; text-align: center; padding: 2rem; }
    </style>
</head>
<body>
    <header>
        <img src="avatar.jpg" alt="Nguyễn Văn A" class="avatar">
        <h1>Nguyễn Văn A</h1>
        <p>Web Developer | UI/UX Designer | Tech Enthusiast</p>
    </header>

    <nav>
        <ul>
            <li><a href="#about">Về tôi</a></li>
            <li><a href="#skills">Kỹ năng</a></li>
            <li><a href="#projects">Dự án</a></li>
            <li><a href="#contact">Liên hệ</a></li>
        </ul>
    </nav>

    <main>
        <section id="about">
            <h2>Về tôi</h2>
            <p style="line-height: 1.8; margin-top: 1rem;">
                Xin chào! Tôi là một Web Developer với 3 năm kinh nghiệm trong việc
                xây dựng các ứng dụng web hiện đại. Tôi đam mê công nghệ và luôn
                tìm kiếm cơ hội để học hỏi và phát triển kỹ năng mới.
            </p>
        </section>

        <section id="skills">
            <h2>Kỹ năng</h2>
            <div style="margin-top: 2rem;">
                <article style="margin-bottom: 1.5rem;">
                    <h3>Frontend Development</h3>
                    <p>HTML5, CSS3, JavaScript (ES6+), React, Vue.js, Responsive Design</p>
                </article>
                <article style="margin-bottom: 1.5rem;">
                    <h3>Backend Development</h3>
                    <p>Node.js, Express, MongoDB, RESTful APIs</p>
                </article>
                <article style="margin-bottom: 1.5rem;">
                    <h3>Tools & Others</h3>
                    <p>Git, VS Code, Figma, Adobe XD, Agile/Scrum</p>
                </article>
            </div>
        </section>

        <section id="projects">
            <h2>Dự án nổi bật</h2>
            <div class="projects">
                <article class="project-card">
                    <h3>E-commerce Platform</h3>
                    <p>Website thương mại điện tử hoàn chỉnh với giỏ hàng, thanh toán và quản lý đơn hàng</p>
                    <p><strong>Tech:</strong> React, Node.js, MongoDB</p>
                </article>
                <article class="project-card">
                    <h3>Task Management App</h3>
                    <p>Ứng dụng quản lý công việc với drag-and-drop, real-time updates</p>
                    <p><strong>Tech:</strong> Vue.js, Firebase</p>
                </article>
                <article class="project-card">
                    <h3>Weather Dashboard</h3>
                    <p>Dashboard hiển thị thông tin thời tiết với charts và maps tương tác</p>
                    <p><strong>Tech:</strong> HTML5, CSS3, JavaScript, Weather API</p>
                </article>
            </div>
        </section>

        <section id="contact">
            <h2>Liên hệ</h2>
            <form style="max-width: 600px; margin: 2rem auto;">
                <div style="margin-bottom: 1rem;">
                    <label for="name" style="display: block; margin-bottom: 0.5rem;">Tên:</label>
                    <input type="text" id="name" name="name" required
                           style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
                </div>
                <div style="margin-bottom: 1rem;">
                    <label for="email" style="display: block; margin-bottom: 0.5rem;">Email:</label>
                    <input type="email" id="email" name="email" required
                           style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
                </div>
                <div style="margin-bottom: 1rem;">
                    <label for="message" style="display: block; margin-bottom: 0.5rem;">Tin nhắn:</label>
                    <textarea id="message" name="message" rows="5" required
                              style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;"></textarea>
                </div>
                <button type="submit"
                        style="background: #3498db; color: white; padding: 0.75rem 2rem;
                               border: none; border-radius: 4px; cursor: pointer;">
                    Gửi tin nhắn
                </button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Nguyễn Văn A. All rights reserved.</p>
        <p>
            <a href="#" style="color: #3498db; margin: 0 0.5rem;">GitHub</a> |
            <a href="#" style="color: #3498db; margin: 0 0.5rem;">LinkedIn</a> |
            <a href="#" style="color: #3498db; margin: 0 0.5rem;">Twitter</a>
        </p>
    </footer>
</body>
</html>
```

### Ví dụ 5: Dashboard Admin

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - Analytics</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f6fa; }
        .dashboard { display: grid; grid-template-columns: 250px 1fr; min-height: 100vh; }
        .sidebar { background: #2c3e50; color: white; padding: 2rem 1rem; }
        .sidebar h2 { margin-bottom: 2rem; }
        .sidebar nav a { display: block; color: white; text-decoration: none;
                        padding: 0.75rem 1rem; margin-bottom: 0.5rem; border-radius: 4px; }
        .sidebar nav a:hover { background: #34495e; }
        .main-content { padding: 2rem; }
        .header { display: flex; justify-content: space-between; align-items: center;
                  background: white; padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem; margin-bottom: 2rem; }
        .stat-card { background: white; padding: 1.5rem; border-radius: 8px;
                     box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .stat-value { font-size: 2rem; font-weight: bold; margin: 0.5rem 0; }
        .table-container { background: white; padding: 1.5rem; border-radius: 8px;
                          box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 1rem; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #f8f9fa; font-weight: 600; }
    </style>
</head>
<body>
    <div class="dashboard">
        <aside class="sidebar">
            <h2>Admin Panel</h2>
            <nav>
                <a href="#dashboard">Dashboard</a>
                <a href="#users">Users</a>
                <a href="#products">Products</a>
                <a href="#orders">Orders</a>
                <a href="#analytics">Analytics</a>
                <a href="#settings">Settings</a>
            </nav>
        </aside>

        <main class="main-content">
            <header class="header">
                <h1>Dashboard Overview</h1>
                <div>
                    <span>Welcome, Admin</span>
                    <button style="margin-left: 1rem; padding: 0.5rem 1rem; background: #e74c3c;
                                   color: white; border: none; border-radius: 4px; cursor: pointer;">
                        Logout
                    </button>
                </div>
            </header>

            <section class="stats">
                <article class="stat-card">
                    <h3>Total Users</h3>
                    <p class="stat-value">1,234</p>
                    <p style="color: #27ae60;">+12% from last month</p>
                </article>
                <article class="stat-card">
                    <h3>Total Orders</h3>
                    <p class="stat-value">567</p>
                    <p style="color: #27ae60;">+8% from last month</p>
                </article>
                <article class="stat-card">
                    <h3>Revenue</h3>
                    <p class="stat-value">$45,678</p>
                    <p style="color: #e74c3c;">-3% from last month</p>
                </article>
                <article class="stat-card">
                    <h3>Products</h3>
                    <p class="stat-value">89</p>
                    <p style="color: #95a5a6;">No change</p>
                </article>
            </section>

            <section class="table-container">
                <h2 style="margin-bottom: 1.5rem;">Recent Orders</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Order ID</th>
                            <th>Customer</th>
                            <th>Product</th>
                            <th>Amount</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>#12345</td>
                            <td>Nguyễn Văn A</td>
                            <td>Laptop Dell XPS 13</td>
                            <td>$1,299</td>
                            <td><span style="background: #27ae60; color: white; padding: 0.25rem 0.75rem;
                                             border-radius: 12px; font-size: 0.85rem;">Completed</span></td>
                            <td><button style="padding: 0.25rem 0.75rem; border: 1px solid #3498db;
                                               background: white; color: #3498db; border-radius: 4px;
                                               cursor: pointer;">View</button></td>
                        </tr>
                        <tr>
                            <td>#12346</td>
                            <td>Trần Thị B</td>
                            <td>iPhone 15 Pro</td>
                            <td>$999</td>
                            <td><span style="background: #f39c12; color: white; padding: 0.25rem 0.75rem;
                                             border-radius: 12px; font-size: 0.85rem;">Pending</span></td>
                            <td><button style="padding: 0.25rem 0.75rem; border: 1px solid #3498db;
                                               background: white; color: #3498db; border-radius: 4px;
                                               cursor: pointer;">View</button></td>
                        </tr>
                        <tr>
                            <td>#12347</td>
                            <td>Lê Văn C</td>
                            <td>Samsung Galaxy S24</td>
                            <td>$899</td>
                            <td><span style="background: #3498db; color: white; padding: 0.25rem 0.75rem;
                                             border-radius: 12px; font-size: 0.85rem;">Processing</span></td>
                            <td><button style="padding: 0.25rem 0.75rem; border: 1px solid #3498db;
                                               background: white; color: #3498db; border-radius: 4px;
                                               cursor: pointer;">View</button></td>
                        </tr>
                    </tbody>
                </table>
            </section>
        </main>
    </div>
</body>
</html>
```

### Ví dụ 6: Form Validation Page

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration Form</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
               min-height: 100vh; display: flex; justify-content: center; align-items: center; }
        .form-container { background: white; padding: 2.5rem; border-radius: 10px;
                         box-shadow: 0 10px 40px rgba(0,0,0,0.2); max-width: 500px; width: 100%; }
        h2 { text-align: center; margin-bottom: 2rem; color: #333; }
        .form-group { margin-bottom: 1.5rem; }
        label { display: block; margin-bottom: 0.5rem; color: #555; font-weight: 500; }
        input, select, textarea { width: 100%; padding: 0.75rem; border: 2px solid #ddd;
                                  border-radius: 5px; font-size: 1rem; transition: border-color 0.3s; }
        input:focus, select:focus, textarea:focus { outline: none; border-color: #667eea; }
        input:valid { border-color: #27ae60; }
        input:invalid:not(:placeholder-shown) { border-color: #e74c3c; }
        .error-message { color: #e74c3c; font-size: 0.875rem; margin-top: 0.25rem; display: none; }
        input:invalid:not(:placeholder-shown) + .error-message { display: block; }
        button { width: 100%; padding: 1rem; background: #667eea; color: white; border: none;
                border-radius: 5px; font-size: 1.1rem; cursor: pointer; transition: background 0.3s; }
        button:hover { background: #5568d3; }
        .success { background: #d4edda; color: #155724; padding: 1rem; border-radius: 5px;
                   margin-bottom: 1rem; display: none; }
    </style>
</head>
<body>
    <div class="form-container">
        <div class="success" id="successMessage">
            Registration successful! Welcome aboard!
        </div>

        <h2>Create Account</h2>

        <form id="registrationForm" novalidate>
            <div class="form-group">
                <label for="fullname">Full Name *</label>
                <input type="text" id="fullname" name="fullname"
                       placeholder="Enter your full name"
                       required minlength="3" maxlength="50">
                <span class="error-message">Please enter your full name (3-50 characters)</span>
            </div>

            <div class="form-group">
                <label for="email">Email Address *</label>
                <input type="email" id="email" name="email"
                       placeholder="example@email.com" required>
                <span class="error-message">Please enter a valid email address</span>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number *</label>
                <input type="tel" id="phone" name="phone"
                       placeholder="0123456789"
                       pattern="[0-9]{10}" required>
                <span class="error-message">Please enter a valid 10-digit phone number</span>
            </div>

            <div class="form-group">
                <label for="password">Password *</label>
                <input type="password" id="password" name="password"
                       placeholder="Minimum 8 characters"
                       required minlength="8">
                <span class="error-message">Password must be at least 8 characters</span>
            </div>

            <div class="form-group">
                <label for="confirmPassword">Confirm Password *</label>
                <input type="password" id="confirmPassword" name="confirmPassword"
                       placeholder="Re-enter password" required>
                <span class="error-message">Passwords do not match</span>
            </div>

            <div class="form-group">
                <label for="dob">Date of Birth *</label>
                <input type="date" id="dob" name="dob" required max="2006-01-01">
                <span class="error-message">You must be at least 18 years old</span>
            </div>

            <div class="form-group">
                <label for="gender">Gender *</label>
                <select id="gender" name="gender" required>
                    <option value="">-- Select Gender --</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>
                <span class="error-message">Please select your gender</span>
            </div>

            <div class="form-group">
                <label>
                    <input type="checkbox" name="terms" required>
                    I agree to the Terms and Conditions *
                </label>
            </div>

            <button type="submit">Register Now</button>
        </form>
    </div>

    <script>
        document.getElementById('registrationForm').addEventListener('submit', function(e) {
            e.preventDefault();

            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }

            document.getElementById('successMessage').style.display = 'block';
            this.reset();

            setTimeout(() => {
                document.getElementById('successMessage').style.display = 'none';
            }, 5000);
        });
    </script>
</body>
</html>
```

### Ví dụ 7: Responsive Navigation Menu

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Navigation</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; }

        .navbar { background: #333; position: sticky; top: 0; z-index: 1000; }
        .nav-container { max-width: 1200px; margin: 0 auto; display: flex;
                        justify-content: space-between; align-items: center; padding: 1rem; }
        .logo { color: white; font-size: 1.5rem; font-weight: bold; text-decoration: none; }

        .nav-menu { display: flex; list-style: none; gap: 2rem; }
        .nav-menu a { color: white; text-decoration: none; padding: 0.5rem 1rem;
                     transition: background 0.3s; border-radius: 4px; }
        .nav-menu a:hover { background: #555; }

        .hamburger { display: none; flex-direction: column; cursor: pointer; }
        .hamburger span { width: 25px; height: 3px; background: white; margin: 3px 0;
                         transition: 0.3s; }

        @media (max-width: 768px) {
            .nav-menu { position: absolute; left: -100%; top: 70px; flex-direction: column;
                       background: #333; width: 100%; text-align: center; transition: 0.3s;
                       padding: 2rem 0; }
            .nav-menu.active { left: 0; }
            .hamburger { display: flex; }
        }

        .hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
               color: white; padding: 6rem 2rem; text-align: center; }
        .content { max-width: 1200px; margin: 0 auto; padding: 3rem 2rem; }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="#" class="logo">MyWebsite</a>

            <ul class="nav-menu" id="navMenu">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>

            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <header class="hero" id="home">
        <h1>Welcome to My Website</h1>
        <p>This is a responsive navigation example</p>
    </header>

    <main class="content">
        <section id="about">
            <h2>About Section</h2>
            <p>Responsive navigation that works on all devices.</p>
        </section>
    </main>

    <script>
        const hamburger = document.getElementById('hamburger');
        const navMenu = document.getElementById('navMenu');

        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking on a link
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });
    </script>
</body>
</html>
```

## 1.10. Use Cases Thực Tế

### 1.10.1. E-commerce Website
HTML5 được sử dụng để xây dựng:
- Product listing pages với semantic markup
- Shopping cart với localStorage
- Checkout forms với HTML5 validation
- Product galleries với figure/figcaption
- Customer reviews với article elements

### 1.10.2. Blog/News Website
- Article structure với semantic elements
- Comment sections
- Author bio boxes
- Related posts navigation
- Social media sharing buttons
- RSS feeds

### 1.10.3. Corporate Website
- Company profile pages
- Service descriptions
- Team member profiles
- Contact forms
- Location maps với iframe
- Client testimonials

### 1.10.4. Educational Platform
- Course listings
- Video lectures với HTML5 video
- Quiz/test interfaces
- Student dashboards
- Progress tracking
- Resource libraries

### 1.10.5. Landing Pages
- Hero sections
- Feature highlights
- Call-to-action buttons
- Newsletter signup forms
- Testimonials
- Pricing tables

## 1.11. Tips & Tricks

### 1.11.1. Development Tips

**Tip 1: Sử dụng Emmet trong VS Code**
```
! + Tab → Tạo HTML5 boilerplate
div.container + Tab → <div class="container"></div>
ul>li*5 + Tab → Tạo ul với 5 li items
```

**Tip 2: Live Server cho development**
- Cài extension Live Server trong VS Code
- Right-click file HTML → Open with Live Server
- Auto-reload khi save file

**Tip 3: Comment code hiệu quả**
```html
<!-- ==================== HEADER SECTION ==================== -->
<header>
    <!-- Logo and navigation -->
</header>
<!-- ==================== END HEADER ==================== -->
```

**Tip 4: Organize files properly**
```
project/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── images/
│   └── logo.png
└── assets/
    └── fonts/
```

**Tip 5: Use placeholder services**
```html
<!-- Placeholder images -->
<img src="https://via.placeholder.com/300x200" alt="Placeholder">
<img src="https://picsum.photos/300/200" alt="Random image">

<!-- Placeholder text (Lorem Ipsum generator) -->
lorem50 + Tab (in VS Code with Emmet)
```

### 1.11.2. Performance Tips

**Tip 6: Optimize images**
- Use WebP format when possible
- Compress images before uploading
- Use appropriate image sizes
- Implement lazy loading

**Tip 7: Minify resources**
```html
<!-- Development -->
<link rel="stylesheet" href="style.css">

<!-- Production -->
<link rel="stylesheet" href="style.min.css">
```

**Tip 8: Use CDN for libraries**
```html
<!-- Faster loading from CDN -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
```

### 1.11.3. SEO Tips

**Tip 9: Meta tags đầy đủ**
```html
<head>
    <title>Page Title - Site Name</title>
    <meta name="description" content="Page description (155-160 characters)">
    <meta name="keywords" content="keyword1, keyword2, keyword3">
    <meta name="author" content="Author Name">

    <!-- Open Graph for social media -->
    <meta property="og:title" content="Page Title">
    <meta property="og:description" content="Page description">
    <meta property="og:image" content="image-url.jpg">
    <meta property="og:url" content="https://example.com">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
</head>
```

**Tip 10: Structured data**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "author": "Author Name",
  "datePublished": "2024-01-15"
}
</script>
```

## 1.12. Common Mistakes và Cách Tránh

### 1.12.1. Lỗi về Cấu trúc

**Mistake 1: Quên DOCTYPE**
```html
<!-- WRONG -->
<html>
<head>
    <title>Page</title>
</head>

<!-- CORRECT -->
<!DOCTYPE html>
<html>
<head>
    <title>Page</title>
</head>
```

**Mistake 2: Không đóng tags**
```html
<!-- WRONG -->
<div>
    <p>Text
    <p>Another text
</div>

<!-- CORRECT -->
<div>
    <p>Text</p>
    <p>Another text</p>
</div>
```

**Mistake 3: Nested tags sai**
```html
<!-- WRONG -->
<p><div>Text</div></p>

<!-- CORRECT -->
<div><p>Text</p></div>
```

### 1.12.2. Lỗi về Semantic

**Mistake 4: Lạm dụng div**
```html
<!-- WRONG -->
<div class="header">
    <div class="nav">
        <div class="menu">Menu</div>
    </div>
</div>

<!-- CORRECT -->
<header>
    <nav>
        <ul class="menu">
            <li>Menu</li>
        </ul>
    </nav>
</header>
```

**Mistake 5: Sử dụng sai heading hierarchy**
```html
<!-- WRONG -->
<h1>Main Title</h1>
<h3>Subtitle</h3>  <!-- Skipped h2 -->
<h2>Section</h2>    <!-- Wrong order -->

<!-- CORRECT -->
<h1>Main Title</h1>
<h2>Subtitle</h2>
<h3>Section</h3>
```

### 1.12.3. Lỗi về Accessibility

**Mistake 6: Không có alt text**
```html
<!-- WRONG -->
<img src="logo.jpg">

<!-- CORRECT -->
<img src="logo.jpg" alt="Company Logo">
```

**Mistake 7: Không có label cho form**
```html
<!-- WRONG -->
<input type="text" placeholder="Email">

<!-- CORRECT -->
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

### 1.12.4. Lỗi về Performance

**Mistake 8: Inline styles everywhere**
```html
<!-- WRONG -->
<div style="color: red; font-size: 16px; margin: 10px;">
    <p style="color: blue;">Text</p>
</div>

<!-- CORRECT -->
<div class="container">
    <p class="text">Text</p>
</div>
```

**Mistake 9: JavaScript trong head block rendering**
```html
<!-- WRONG -->
<head>
    <script src="large-script.js"></script>
</head>

<!-- CORRECT -->
<body>
    <!-- Content -->
    <script src="large-script.js"></script>
</body>
```

## 1.13. Troubleshooting

### 1.13.1. Display Issues

**Problem: Page hiển thị ký tự lạ (mojibake)**
```html
<!-- Solution: Add charset UTF-8 -->
<head>
    <meta charset="UTF-8">
</head>
```

**Problem: Mobile không responsive**
```html
<!-- Solution: Add viewport meta tag -->
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

**Problem: CSS không load**
```html
<!-- Check file path -->
<!-- WRONG -->
<link rel="stylesheet" href="style.css"> <!-- file ở thư mục khác -->

<!-- CORRECT -->
<link rel="stylesheet" href="css/style.css">
<!-- OR absolute path -->
<link rel="stylesheet" href="/css/style.css">
```

### 1.13.2. Validation Errors

**Problem: Validation errors**
- Use W3C Validator: https://validator.w3.org/
- Common errors:
  - Unclosed tags
  - Invalid nesting
  - Missing required attributes
  - Duplicate IDs

**Problem: SEO issues**
- Missing title tag
- Missing meta description
- Missing alt text on images
- Broken links
- Duplicate content

### 1.13.3. Browser Compatibility

**Problem: Khác biệt giữa browsers**
```html
<!-- Use CSS reset or normalize.css -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">

<!-- Check compatibility on caniuse.com -->
```

**Problem: Old browser support**
```html
<!-- Use polyfills -->
<!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
```

## 1.14. Advanced Topics

### 1.14.1. HTML5 Custom Data Attributes

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Data Attributes Example</title>
</head>
<body>
    <ul id="productList">
        <li data-product-id="101"
            data-product-name="Laptop"
            data-product-price="999"
            data-product-category="Electronics">
            Laptop - $999
        </li>
        <li data-product-id="102"
            data-product-name="Mouse"
            data-product-price="29"
            data-product-category="Accessories">
            Mouse - $29
        </li>
    </ul>

    <script>
        // Access data attributes
        const products = document.querySelectorAll('#productList li');
        products.forEach(product => {
            console.log('ID:', product.dataset.productId);
            console.log('Name:', product.dataset.productName);
            console.log('Price:', product.dataset.productPrice);
            console.log('Category:', product.dataset.productCategory);
        });
    </script>
</body>
</html>
```

### 1.14.2. Microdata và Schema.org

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Microdata Example</title>
</head>
<body>
    <div itemscope itemtype="http://schema.org/Product">
        <h1 itemprop="name">Dell XPS 13</h1>
        <img itemprop="image" src="laptop.jpg" alt="Dell XPS 13">
        <p itemprop="description">High-performance ultrabook</p>
        <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
            <span itemprop="price" content="1299">$1,299</span>
            <meta itemprop="priceCurrency" content="USD">
            <link itemprop="availability" href="http://schema.org/InStock">In Stock
        </div>
        <div itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating">
            Rating: <span itemprop="ratingValue">4.5</span>/5
            based on <span itemprop="reviewCount">230</span> reviews
        </div>
    </div>
</body>
</html>
```

### 1.14.3. HTML5 Templates

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Template Example</title>
</head>
<body>
    <div id="container"></div>

    <template id="productTemplate">
        <article class="product-card">
            <img src="" alt="">
            <h3 class="product-name"></h3>
            <p class="product-price"></p>
            <button>Add to Cart</button>
        </article>
    </template>

    <script>
        const products = [
            {name: 'Laptop', price: '$999', image: 'laptop.jpg'},
            {name: 'Mouse', price: '$29', image: 'mouse.jpg'}
        ];

        const template = document.getElementById('productTemplate');
        const container = document.getElementById('container');

        products.forEach(product => {
            const clone = template.content.cloneNode(true);
            clone.querySelector('img').src = product.image;
            clone.querySelector('.product-name').textContent = product.name;
            clone.querySelector('.product-price').textContent = product.price;
            container.appendChild(clone);
        });
    </script>
</body>
</html>
```

### 1.14.4. Progressive Enhancement

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Progressive Enhancement</title>
    <style>
        /* Base styles - work without JavaScript */
        .no-js .advanced-feature { display: none; }
        .js .basic-feature { display: none; }
    </style>
</head>
<body class="no-js">
    <!-- Basic version (works without JS) -->
    <div class="basic-feature">
        <a href="products.html">View Products</a>
    </div>

    <!-- Enhanced version (requires JS) -->
    <div class="advanced-feature">
        <button id="loadProducts">Load Products Dynamically</button>
        <div id="productContainer"></div>
    </div>

    <script>
        // Enable JS features
        document.body.classList.remove('no-js');
        document.body.classList.add('js');

        document.getElementById('loadProducts').addEventListener('click', function() {
            // Load products via AJAX
            console.log('Loading products...');
        });
    </script>
</body>
</html>
```

### 1.14.5. Web Components (Custom Elements)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Web Components Example</title>
</head>
<body>
    <user-card
        name="Nguyễn Văn A"
        avatar="avatar.jpg"
        email="user@example.com">
    </user-card>

    <script>
        class UserCard extends HTMLElement {
            connectedCallback() {
                const name = this.getAttribute('name');
                const avatar = this.getAttribute('avatar');
                const email = this.getAttribute('email');

                this.innerHTML = `
                    <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 8px;">
                        <img src="${avatar}" alt="${name}" style="width: 100px; border-radius: 50%;">
                        <h3>${name}</h3>
                        <p>Email: ${email}</p>
                    </div>
                `;
            }
        }

        customElements.define('user-card', UserCard);
    </script>
</body>
</html>
```

## 1.15. Bài tập thực hành

### Bài 1: Setup môi trường (Dễ)
1. Cài đặt Visual Studio Code
2. Cài đặt extension Live Server
3. Tạo file `index.html` đầu tiên với cấu trúc HTML5 cơ bản
4. Mở với Live Server và xem kết quả

### Bài 2: Trang HTML5 đơn giản (Dễ)
Tạo một trang HTML5 với:
- DOCTYPE khai báo đúng
- Meta tags đầy đủ (charset, viewport, description)
- Title có ý nghĩa
- Heading h1
- Một đoạn văn bản
- Validate bằng W3C Validator

### Bài 3: So sánh HTML4 vs HTML5 (Dễ)
Viết hai file HTML giống nhau về nội dung:
- File 1: Sử dụng HTML4 syntax
- File 2: Sử dụng HTML5 syntax
So sánh và ghi chú sự khác biệt

### Bài 4: Personal Card (Dễ)
Tạo một business card cá nhân với:
- Tên, chức danh
- Avatar (có thể dùng placeholder)
- Email, phone
- Links đến social media
- CSS inline để styling

### Bài 5: Simple Landing Page (Trung bình)
Tạo landing page cho một sản phẩm với:
- Header với logo và navigation
- Hero section với heading và CTA button
- Features section (3 features)
- Footer với copyright
- Responsive design cơ bản

### Bài 6: Blog Article Page (Trung bình)
Tạo trang bài viết blog với:
- Article structure semantic
- Author info và published date
- Table of contents
- Related articles sidebar
- Comment section (HTML only)

### Bài 7: Product Catalog (Trung bình)
Tạo trang danh sách sản phẩm với:
- Grid layout cho products (ít nhất 6 products)
- Product card gồm: image, name, price, rating
- Filter sidebar (HTML structure only)
- Sử dụng data attributes cho product info

### Bài 8: Contact Form (Trung bình)
Tạo form liên hệ với:
- Fields: name, email, phone, subject, message
- HTML5 validation attributes
- Required fields được đánh dấu
- Submit button
- Success message area

### Bài 9: Dashboard Template (Khó)
Tạo admin dashboard với:
- Sidebar navigation
- Top header với user menu
- Stats cards (4 cards)
- Data table với sample data
- Charts placeholder
- Responsive layout

### Bài 10: Complete Website Structure (Khó)
Tạo cấu trúc hoàn chỉnh cho website gồm:
- Homepage với multiple sections
- About page
- Services/Products page
- Contact page
- Consistent navigation across pages
- Footer với sitemap
- Semantic HTML throughout
- Meta tags đầy đủ cho SEO

### Bài 11: Microdata Implementation (Khó)
Tạo product page với:
- Schema.org microdata
- Product information (name, price, availability)
- Reviews với structured data
- Breadcrumb navigation
- Validate với Google Rich Results Test

### Bài 12: Accessible Form (Khó)
Tạo form với accessibility features:
- ARIA labels và descriptions
- Proper label associations
- Error messages
- Keyboard navigation support
- Screen reader friendly
- Test với accessibility tools

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
