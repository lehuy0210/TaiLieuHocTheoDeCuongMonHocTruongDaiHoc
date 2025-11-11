# CHƯƠNG 8: HTML5 SEMANTIC ELEMENTS

## 8.1. Giới thiệu Semantic HTML

### 8.1.1. Semantic là gì?

**Semantic Elements** = Elements có ý nghĩa rõ ràng cho cả browser và developer

**Non-semantic:**
```html
<div id="header"></div>
<div class="navigation"></div>
<div id="content"></div>
<div class="sidebar"></div>
<div id="footer"></div>
```

**Semantic:**
```html
<header></header>
<nav></nav>
<main></main>
<aside></aside>
<footer></footer>
```

### 8.1.2. Lợi ích của Semantic HTML

1. **SEO tốt hơn** - Search engines hiểu cấu trúc tốt hơn
2. **Accessibility** - Screen readers đọc tốt hơn
3. **Maintainability** - Code dễ đọc và bảo trì
4. **Consistency** - Chuẩn hóa cấu trúc

## 8.2. Page Structure Elements

### 8.2.1. `<header>`

```html
<!-- Page header -->
<header>
    <h1>Website Name</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </nav>
</header>

<!-- Article header -->
<article>
    <header>
        <h2>Article Title</h2>
        <p>By Author Name | January 1, 2024</p>
    </header>
    <p>Article content...</p>
</article>
```

### 8.2.2. `<nav>`

```html
<!-- Main navigation -->
<nav aria-label="Main Navigation">
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</nav>

<!-- Breadcrumb navigation -->
<nav aria-label="Breadcrumb">
    <ol>
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li aria-current="page">Laptops</li>
    </ol>
</nav>

<!-- Footer navigation -->
<footer>
    <nav aria-label="Footer Navigation">
        <a href="/privacy">Privacy</a>
        <a href="/terms">Terms</a>
    </nav>
</footer>
```

### 8.2.3. `<main>`

```html
<body>
    <header><!-- Site header --></header>
    <nav><!-- Navigation --></nav>

    <!-- Main content - chỉ một <main> trong document -->
    <main>
        <h1>Main Content Title</h1>
        <article><!-- Primary content --></article>
    </main>

    <footer><!-- Site footer --></footer>
</body>
```

**Lưu ý:**
- Chỉ có **một** `<main>` trong document
- Không được là descendant của `<article>`, `<aside>`, `<footer>`, `<header>`, `<nav>`

### 8.2.4. `<section>`

```html
<main>
    <h1>About Our Company</h1>

    <section>
        <h2>Our Mission</h2>
        <p>Mission statement...</p>
    </section>

    <section>
        <h2>Our Team</h2>
        <p>Team information...</p>
    </section>

    <section>
        <h2>Contact Us</h2>
        <p>Contact information...</p>
    </section>
</main>
```

**Khi nào dùng `<section>`:**
- Nhóm nội dung có liên quan
- Thường có heading
- Có thể đứng độc lập về mặt ngữ nghĩa

### 8.2.5. `<article>`

```html
<!-- Blog post -->
<article>
    <header>
        <h2>Article Title</h2>
        <p><time datetime="2024-01-15">January 15, 2024</time></p>
    </header>
    <p>Article content...</p>
    <footer>
        <p>Tags: HTML, CSS, JavaScript</p>
    </footer>
</article>

<!-- News feed -->
<main>
    <h1>Latest News</h1>
    <article>
        <h2>News 1</h2>
        <p>News content...</p>
    </article>
    <article>
        <h2>News 2</h2>
        <p>News content...</p>
    </article>
</main>

<!-- Nested articles -->
<article>
    <h2>Blog Post</h2>
    <p>Post content...</p>

    <section>
        <h3>Comments</h3>
        <article>
            <p>Comment 1...</p>
        </article>
        <article>
            <p>Comment 2...</p>
        </article>
    </section>
</article>
```

**Khi nào dùng `<article>`:**
- Nội dung độc lập, có thể tái sử dụng
- Blog posts, news articles, forum posts
- Product cards, user comments

### 8.2.6. `<aside>`

```html
<!-- Sidebar -->
<aside>
    <h3>Related Articles</h3>
    <ul>
        <li><a href="#">Article 1</a></li>
        <li><a href="#">Article 2</a></li>
    </ul>
</aside>

<!-- Tangentially related content -->
<article>
    <h2>Main Article</h2>
    <p>Article content...</p>

    <aside>
        <h3>Did you know?</h3>
        <p>Related information...</p>
    </aside>
</article>

<!-- Advertisement -->
<aside class="advertisement">
    <h3>Sponsored</h3>
    <p>Ad content...</p>
</aside>
```

### 8.2.7. `<footer>`

```html
<!-- Page footer -->
<footer>
    <p>&copy; 2024 Company Name</p>
    <nav>
        <a href="/privacy">Privacy</a>
        <a href="/terms">Terms</a>
    </nav>
</footer>

<!-- Article footer -->
<article>
    <header>
        <h2>Article Title</h2>
    </header>
    <p>Article content...</p>
    <footer>
        <p>Author: John Doe</p>
        <p>Published: <time datetime="2024-01-15">Jan 15, 2024</time></p>
        <p>Tags: HTML5, Semantic, Web Development</p>
    </footer>
</article>
```

## 8.3. Content Grouping Elements

### 8.3.1. `<figure>` và `<figcaption>`

```html
<!-- Image with caption -->
<figure>
    <img src="chart.png" alt="Sales Chart">
    <figcaption>Figure 1: Sales growth in 2023</figcaption>
</figure>

<!-- Code listing -->
<figure>
    <pre><code>
function hello() {
    console.log("Hello World");
}
    </code></pre>
    <figcaption>Listing 1: Hello World function in JavaScript</figcaption>
</figure>

<!-- Quote -->
<figure>
    <blockquote>
        <p>The only way to do great work is to love what you do.</p>
    </blockquote>
    <figcaption>— Steve Jobs</figcaption>
</figure>

<!-- Multiple images -->
<figure>
    <img src="photo1.jpg" alt="Photo 1">
    <img src="photo2.jpg" alt="Photo 2">
    <img src="photo3.jpg" alt="Photo 3">
    <figcaption>Photo gallery from vacation</figcaption>
</figure>
```

### 8.3.2. `<details>` và `<summary>`

```html
<!-- Basic details -->
<details>
    <summary>Click to expand</summary>
    <p>Hidden content that can be toggled.</p>
</details>

<!-- Open by default -->
<details open>
    <summary>Expanded by default</summary>
    <p>This is visible initially.</p>
</details>

<!-- FAQ -->
<section>
    <h2>Frequently Asked Questions</h2>

    <details>
        <summary>What is HTML5?</summary>
        <p>HTML5 is the latest version of HTML...</p>
    </details>

    <details>
        <summary>What are semantic elements?</summary>
        <p>Semantic elements are elements with meaning...</p>
    </details>
</section>
```

### 8.3.3. `<dialog>`

```html
<dialog id="myDialog">
    <h2>Dialog Title</h2>
    <p>Dialog content...</p>
    <button onclick="closeDialog()">Close</button>
</dialog>

<button onclick="showDialog()">Open Dialog</button>

<script>
const dialog = document.getElementById('myDialog');

function showDialog() {
    dialog.showModal(); // Modal dialog
    // or dialog.show(); // Non-modal
}

function closeDialog() {
    dialog.close();
}
</script>
```

## 8.4. Text-level Semantic Elements

### 8.4.1. `<mark>`

```html
<p>Search results for "HTML5":</p>
<p>Learn <mark>HTML5</mark> and CSS3 for modern web development.</p>
```

### 8.4.2. `<time>`

```html
<p>Published on <time datetime="2024-01-15">January 15, 2024</time></p>
<p>Event starts at <time datetime="2024-12-25T20:00">8:00 PM on Christmas</time></p>
```

### 8.4.3. `<progress>`

```html
<label for="upload">Upload progress:</label>
<progress id="upload" value="70" max="100">70%</progress>
```

### 8.4.4. `<meter>`

```html
<label for="storage">Disk usage:</label>
<meter id="storage" min="0" max="100" low="20" high="80" optimum="50" value="65">
    65%
</meter>
```

## 8.5. Complete Page Structure

### 8.5.1. Blog Layout

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>My Blog</title>
</head>
<body>
    <header>
        <h1>My Blog</h1>
        <nav aria-label="Main Navigation">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article>
            <header>
                <h2>Blog Post Title</h2>
                <p>
                    By <a href="/author/john">John Doe</a> |
                    <time datetime="2024-01-15">January 15, 2024</time>
                </p>
            </header>

            <section>
                <h3>Introduction</h3>
                <p>Post content...</p>
            </section>

            <section>
                <h3>Main Content</h3>
                <p>More content...</p>

                <figure>
                    <img src="image.jpg" alt="Description">
                    <figcaption>Figure 1: Image caption</figcaption>
                </figure>
            </section>

            <footer>
                <p>Tags: <a href="/tag/html">HTML</a>, <a href="/tag/css">CSS</a></p>
            </footer>
        </article>

        <section id="comments">
            <h3>Comments</h3>
            <article>
                <header>
                    <p>By Jane | <time datetime="2024-01-16">Jan 16, 2024</time></p>
                </header>
                <p>Great article!</p>
            </article>
        </section>
    </main>

    <aside>
        <section>
            <h3>About Author</h3>
            <p>Author bio...</p>
        </section>

        <section>
            <h3>Recent Posts</h3>
            <ul>
                <li><a href="#">Post 1</a></li>
                <li><a href="#">Post 2</a></li>
            </ul>
        </section>
    </aside>

    <footer>
        <p>&copy; 2024 My Blog. All rights reserved.</p>
        <nav aria-label="Footer Navigation">
            <a href="/privacy">Privacy</a> |
            <a href="/terms">Terms</a>
        </nav>
    </footer>
</body>
</html>
```

### 8.5.2. E-commerce Product Page

```html
<main>
    <nav aria-label="Breadcrumb">
        <ol>
            <li><a href="/">Home</a></li>
            <li><a href="/products">Products</a></li>
            <li><a href="/products/laptops">Laptops</a></li>
            <li aria-current="page">Dell XPS 13</li>
        </ol>
    </nav>

    <article itemscope itemtype="https://schema.org/Product">
        <header>
            <h1 itemprop="name">Dell XPS 13</h1>
        </header>

        <figure>
            <img src="laptop.jpg" alt="Dell XPS 13" itemprop="image">
            <figcaption>Dell XPS 13 - Premium Ultrabook</figcaption>
        </figure>

        <section>
            <h2>Product Details</h2>
            <p itemprop="description">High-performance laptop...</p>

            <dl>
                <dt>Price</dt>
                <dd itemprop="price">$999</dd>

                <dt>Availability</dt>
                <dd itemprop="availability">In Stock</dd>

                <dt>SKU</dt>
                <dd itemprop="sku">DXPS13-001</dd>
            </dl>
        </section>

        <section>
            <h2>Specifications</h2>
            <table>
                <tr>
                    <th>Processor</th>
                    <td>Intel Core i7</td>
                </tr>
                <tr>
                    <th>RAM</th>
                    <td>16GB</td>
                </tr>
            </table>
        </section>

        <section id="reviews">
            <h2>Customer Reviews</h2>
            <article>
                <header>
                    <h3>Great laptop!</h3>
                    <p>By John | <time datetime="2024-01-10">Jan 10, 2024</time></p>
                </header>
                <p>Review content...</p>
            </article>
        </section>
    </article>

    <aside>
        <section>
            <h3>Related Products</h3>
            <!-- Product cards -->
        </section>
    </aside>
</main>
```

## 8.6. Section vs Article vs Div

### 8.6.1. Khi nào dùng gì?

**`<article>`**: Nội dung độc lập, có thể phân phối lại
```html
<article>
    <h2>Blog Post</h2>
    <p>Content...</p>
</article>
```

**`<section>`**: Nhóm nội dung có liên quan với heading
```html
<section>
    <h2>Chapter 1</h2>
    <p>Content...</p>
</section>
```

**`<div>`**: Không có ý nghĩa semantic, chỉ cho styling/scripting
```html
<div class="container">
    <div class="row">
        <div class="col">Content</div>
    </div>
</div>
```

### 8.6.2. Decision Flow

```
Nội dung có thể độc lập?
├─ Yes → <article>
└─ No → Có heading và nhóm nội dung liên quan?
         ├─ Yes → <section>
         └─ No → <div>
```

## 8.7. Best Practices

### 8.7.1. Heading Hierarchy

```html
<!-- ĐÚNG -->
<article>
    <h1>Main Title</h1>
    <section>
        <h2>Section Title</h2>
        <h3>Subsection</h3>
    </section>
</article>

<!-- SAI - Skip heading levels -->
<article>
    <h1>Main Title</h1>
    <h3>Subsection</h3> <!-- Bỏ qua h2 -->
</article>
```

### 8.7.2. Landmark Roles

```html
<!-- HTML5 elements tự động có ARIA roles -->
<header> <!-- role="banner" -->
<nav> <!-- role="navigation" -->
<main> <!-- role="main" -->
<aside> <!-- role="complementary" -->
<footer> <!-- role="contentinfo" -->
<article> <!-- role="article" -->
<section> <!-- role="region" -->

<!-- Thêm label khi có nhiều cùng loại -->
<nav aria-label="Main Navigation">
<nav aria-label="Footer Navigation">
```

### 8.7.3. Avoid Over-nesting

```html
<!-- Tránh -->
<section>
    <article>
        <section>
            <article>
                <section>
                    <p>Content</p>
                </section>
            </article>
        </section>
    </article>
</section>

<!-- Tốt hơn -->
<article>
    <h2>Title</h2>
    <p>Content</p>
</article>
```

## 8.8. Browser Support và Polyfills

### 8.8.1. HTML5 Shiv (IE8 và cũ hơn)

```html
<!--[if lt IE 9]>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js"></script>
<![endif]-->
```

### 8.8.2. CSS cho older browsers

```css
/* Đảm bảo block display */
header, nav, main, section, article, aside, footer {
    display: block;
}
```

## 8.9. Use Cases Thực Tế

### Use Case 1: Blog Platform với Semantic Structure
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Blog - Chia sẻ kiến thức lập trình</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; color: #333; }
        header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px 0; }
        header h1 { max-width: 1200px; margin: 0 auto; padding: 20px; font-size: 2.5em; }
        nav ul { max-width: 1200px; margin: 0 auto; list-style: none; display: flex; gap: 30px; padding: 0 20px; }
        nav a { color: white; text-decoration: none; transition: opacity 0.3s; }
        nav a:hover { opacity: 0.8; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; display: grid; grid-template-columns: 1fr 300px; gap: 30px; }
        main { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        article { margin-bottom: 40px; padding-bottom: 40px; border-bottom: 1px solid #eee; }
        article:last-child { border-bottom: none; }
        article header { background: none; color: #333; padding: 0; margin-bottom: 20px; }
        article h2 { margin: 0 0 10px 0; color: #667eea; font-size: 1.8em; }
        article .meta { color: #666; font-size: 0.9em; margin-bottom: 15px; }
        article .meta time { font-weight: bold; }
        figure { margin: 20px 0; }
        figure img { max-width: 100%; height: auto; border-radius: 8px; }
        figcaption { background: #f5f5f5; padding: 10px 15px; border-radius: 0 0 8px 8px; color: #666; font-size: 0.9em; font-style: italic; }
        aside { position: sticky; top: 20px; height: fit-content; }
        aside section { background: #f9f9f9; padding: 20px; border-radius: 8px; margin-bottom: 20px; border-left: 4px solid #667eea; }
        aside h3 { color: #667eea; margin-bottom: 15px; font-size: 1.1em; }
        aside ul { list-style: none; }
        aside li { margin-bottom: 10px; }
        aside a { color: #667eea; text-decoration: none; transition: color 0.3s; }
        aside a:hover { color: #764ba2; }
        footer { background: #333; color: white; text-align: center; padding: 30px 20px; margin-top: 50px; }
        #comments article { border-bottom: 1px solid #eee; padding-bottom: 20px; margin-bottom: 20px; background: #fafafa; padding: 15px; border-radius: 6px; border-left: 3px solid #ddd; }
        #comments article:last-child { border-bottom: none; }
        @media (max-width: 768px) {
            .container { grid-template-columns: 1fr; }
            aside { position: static; }
            nav ul { flex-direction: column; gap: 10px; }
        }
    </style>
</head>
<body>
    <header>
        <h1>Tech Blog - Chia sẻ kiến thức</h1>
        <nav aria-label="Main Navigation">
            <ul>
                <li><a href="/">Trang chủ</a></li>
                <li><a href="/tutorials">Hướng dẫn</a></li>
                <li><a href="/tips">Mẹo & Thủ thuật</a></li>
                <li><a href="/about">Về tôi</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <main>
            <article itemscope itemtype="https://schema.org/BlogPosting">
                <header>
                    <h2 itemprop="headline">Hướng dẫn hoàn chỉnh HTML5 Semantic Elements</h2>
                    <div class="meta">
                        <span>Bởi <a href="/author/john" itemprop="author">John Developer</a></span> •
                        <time datetime="2024-01-15" itemprop="datePublished">15 tháng 1, 2024</time> •
                        <span>Thời gian đọc: 8 phút</span>
                    </div>
                </header>

                <figure>
                    <img src="semantic-html.jpg"
                         alt="HTML5 Semantic Elements"
                         itemprop="image"
                         style="width: 100%; height: 300px; object-fit: cover;">
                    <figcaption>Cấu trúc semantic HTML giúp code dễ đọc hơn</figcaption>
                </figure>

                <section itemprop="articleBody">
                    <h3>Giới thiệu</h3>
                    <p>HTML5 semantic elements cung cấp ý nghĩa rõ ràng cho cả browser và developer. Bài viết này sẽ hướng dẫn bạn cách sử dụng chúng đúng cách.</p>

                    <h3>Những yếu tố chính</h3>
                    <p>Các semantic elements chủ yếu bao gồm: header, nav, main, section, article, aside, footer, figure, v.v.</p>
                    <p>Mỗi phần tử có mục đích riêng và giúp cấu trúc trang web một cách hợp lý.</p>
                </section>

                <footer style="background: #f5f5f5; padding: 15px; margin-top: 20px; border-radius: 6px;">
                    <p><strong>Tags:</strong>
                        <a href="/tag/html5">#HTML5</a>
                        <a href="/tag/semantic">#Semantic</a>
                        <a href="/tag/webdev">#WebDev</a>
                    </p>
                    <p>Chia sẻ: <a href="#">Facebook</a> | <a href="#">Twitter</a></p>
                </footer>
            </article>

            <section id="comments">
                <h3>Bình luận (2)</h3>

                <article>
                    <header>
                        <strong>Nguyễn Văn A</strong>
                        <time datetime="2024-01-16">16 tháng 1, 2024</time>
                    </header>
                    <p>Bài viết rất hữu ích! Cảm ơn bạn đã giải thích chi tiết về semantic HTML.</p>
                </article>

                <article>
                    <header>
                        <strong>Trần Thị B</strong>
                        <time datetime="2024-01-17">17 tháng 1, 2024</time>
                    </header>
                    <p>Tôi đã áp dụng những kiến thức này vào dự án của mình và thấy code dễ bảo trì hơn rất nhiều.</p>
                </article>
            </section>
        </main>

        <aside>
            <section>
                <h3>Về tác giả</h3>
                <img src="author.jpg" alt="John Developer" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
                <p>John là một developer full-stack với 8 năm kinh nghiệm. Anh yêu thích chia sẻ kiến thức lập trình.</p>
            </section>

            <section>
                <h3>Bài viết mới nhất</h3>
                <ul>
                    <li><a href="#">CSS Grid - Thiết kế responsive</a></li>
                    <li><a href="#">JavaScript ES6 Features</a></li>
                    <li><a href="#">Tối ưu hóa ảnh cho web</a></li>
                    <li><a href="#">SEO Best Practices 2024</a></li>
                </ul>
            </section>

            <section>
                <h3>Danh mục</h3>
                <ul>
                    <li><a href="/html">HTML (12)</a></li>
                    <li><a href="/css">CSS (18)</a></li>
                    <li><a href="/javascript">JavaScript (25)</a></li>
                    <li><a href="/webdev">Web Dev (45)</a></li>
                </ul>
            </section>

            <section>
                <h3>Theo dõi</h3>
                <p>Đăng ký nhận thông báo bài viết mới.</p>
                <input type="email" placeholder="Email của bạn" style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 4px;">
                <button style="width: 100%; padding: 8px; background: #667eea; color: white; border: none; border-radius: 4px; cursor: pointer;">Đăng ký</button>
            </section>
        </aside>
    </div>

    <footer>
        <p>&copy; 2024 Tech Blog. Bảo lưu mọi quyền. |
            <nav aria-label="Footer Navigation">
                <a href="/privacy" style="color: white; text-decoration: none;">Chính sách riêng tư</a> •
                <a href="/terms" style="color: white; text-decoration: none;">Điều khoản sử dụng</a>
            </nav>
        </p>
    </footer>
</body>
</html>
```

### Use Case 2: E-Commerce Product Navigation
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Shop - Cửa hàng trực tuyến</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; }
        header { background: white; border-bottom: 1px solid #ddd; padding: 15px 0; }
        .header-content { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; }
        header h1 { font-size: 1.5em; color: #333; }
        nav { flex: 1; margin: 0 30px; }
        nav ul { list-style: none; display: flex; gap: 20px; }
        nav a { color: #666; text-decoration: none; transition: color 0.3s; }
        nav a:hover { color: #e74c3c; }
        .breadcrumb { max-width: 1200px; margin: 20px auto; padding: 0 20px; font-size: 0.9em; }
        .breadcrumb ol { list-style: none; display: flex; gap: 5px; }
        .breadcrumb a { color: #0066cc; text-decoration: none; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; display: grid; grid-template-columns: 250px 1fr; gap: 30px; }
        aside { background: #f9f9f9; padding: 20px; border-radius: 8px; height: fit-content; }
        aside h3 { margin: 20px 0 10px; font-size: 1.1em; color: #333; }
        aside ul { list-style: none; }
        aside li { padding: 8px 0; }
        aside a { color: #666; text-decoration: none; }
        aside a:hover { color: #e74c3c; }
        .products { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }
        .product-card { border: 1px solid #ddd; border-radius: 8px; overflow: hidden; transition: transform 0.3s, box-shadow 0.3s; }
        .product-card:hover { transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
        .product-image { width: 100%; height: 200px; object-fit: cover; }
        .product-info { padding: 15px; }
        .product-info h4 { margin-bottom: 10px; color: #333; }
        .price { color: #e74c3c; font-size: 1.3em; font-weight: bold; margin-bottom: 10px; }
        button { background: #e74c3c; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
        button:hover { background: #c0392b; }
        footer { background: #333; color: white; text-align: center; padding: 30px 20px; margin-top: 50px; }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>Shop</h1>
            <nav aria-label="Main Navigation">
                <ul>
                    <li><a href="/">Trang chủ</a></li>
                    <li><a href="/products">Sản phẩm</a></li>
                    <li><a href="/about">Về chúng tôi</a></li>
                    <li><a href="/contact">Liên hệ</a></li>
                </ul>
            </nav>
            <div>🛒 Giỏ hàng (3)</div>
        </div>
    </header>

    <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
            <li><a href="/">Trang chủ</a></li>
            <li><span>›</span></li>
            <li><a href="/products">Sản phẩm</a></li>
            <li><span>›</span></li>
            <li><a href="/products/electronics">Điện tử</a></li>
            <li><span>›</span></li>
            <li aria-current="page">Laptop</li>
        </ol>
    </nav>

    <div class="container">
        <aside>
            <nav aria-label="Product Categories">
                <h3>Danh mục</h3>
                <ul>
                    <li><a href="/electronics">📱 Điện tử</a></li>
                    <li><a href="/computers">💻 Máy tính</a></li>
                    <li><a href="/accessories">🎧 Phụ kiện</a></li>
                    <li><a href="/software">📦 Phần mềm</a></li>
                </ul>

                <h3>Bộ lọc</h3>
                <h4>Giá</h4>
                <ul>
                    <li><input type="checkbox"> Dưới 5 triệu</li>
                    <li><input type="checkbox"> 5-10 triệu</li>
                    <li><input type="checkbox"> 10-20 triệu</li>
                    <li><input type="checkbox"> Trên 20 triệu</li>
                </ul>

                <h4>Hãng</h4>
                <ul>
                    <li><input type="checkbox"> Dell</li>
                    <li><input type="checkbox"> HP</li>
                    <li><input type="checkbox"> Lenovo</li>
                    <li><input type="checkbox"> Apple</li>
                </ul>

                <h4>Đánh giá</h4>
                <ul>
                    <li><input type="checkbox"> ⭐⭐⭐⭐⭐ (5 sao)</li>
                    <li><input type="checkbox"> ⭐⭐⭐⭐ (4 sao)</li>
                    <li><input type="checkbox"> ⭐⭐⭐ (3 sao)</li>
                </ul>
            </nav>
        </aside>

        <main>
            <h2 style="margin-bottom: 20px;">Laptop (24 sản phẩm)</h2>

            <div class="products">
                <article class="product-card" itemscope itemtype="https://schema.org/Product">
                    <img src="laptop1.jpg" alt="Dell XPS 13" class="product-image" itemprop="image">
                    <div class="product-info">
                        <h4 itemprop="name">Dell XPS 13</h4>
                        <p itemprop="description">Siêu mỏng, mạnh mẽ và nhẹ</p>
                        <div class="price" itemprop="price">25,990,000đ</div>
                        <p>⭐ 4.5/5 (120 đánh giá)</p>
                        <button>Thêm vào giỏ</button>
                    </div>
                </article>

                <article class="product-card" itemscope itemtype="https://schema.org/Product">
                    <img src="laptop2.jpg" alt="HP Pavilion 15" class="product-image" itemprop="image">
                    <div class="product-info">
                        <h4 itemprop="name">HP Pavilion 15</h4>
                        <p itemprop="description">Hiệu năng tốt, giá hợp lý</p>
                        <div class="price" itemprop="price">15,990,000đ</div>
                        <p>⭐ 4.2/5 (85 đánh giá)</p>
                        <button>Thêm vào giỏ</button>
                    </div>
                </article>

                <article class="product-card" itemscope itemtype="https://schema.org/Product">
                    <img src="laptop3.jpg" alt="Lenovo ThinkPad" class="product-image" itemprop="image">
                    <div class="product-info">
                        <h4 itemprop="name">Lenovo ThinkPad</h4>
                        <p itemprop="description">Chuyên dụng cho văn phòng</p>
                        <div class="price" itemprop="price">18,990,000đ</div>
                        <p>⭐ 4.7/5 (200 đánh giá)</p>
                        <button>Thêm vào giỏ</button>
                    </div>
                </article>

                <article class="product-card" itemscope itemtype="https://schema.org/Product">
                    <img src="laptop4.jpg" alt="MacBook Pro" class="product-image" itemprop="image">
                    <div class="product-info">
                        <h4 itemprop="name">MacBook Pro</h4>
                        <p itemprop="description">Thiết kế sang trọng, hiệu năng đỉnh</p>
                        <div class="price" itemprop="price">45,990,000đ</div>
                        <p>⭐ 4.8/5 (350 đánh giá)</p>
                        <button>Thêm vào giỏ</button>
                    </div>
                </article>

                <article class="product-card" itemscope itemtype="https://schema.org/Product">
                    <img src="laptop5.jpg" alt="ASUS VivoBook" class="product-image" itemprop="image">
                    <div class="product-info">
                        <h4 itemprop="name">ASUS VivoBook</h4>
                        <p itemprop="description">Cân bằng giá - hiệu năng tốt</p>
                        <div class="price" itemprop="price">12,990,000đ</div>
                        <p>⭐ 4.3/5 (95 đánh giá)</p>
                        <button>Thêm vào giỏ</button>
                    </div>
                </article>

                <article class="product-card" itemscope itemtype="https://schema.org/Product">
                    <img src="laptop6.jpg" alt="MSI Gaming Laptop" class="product-image" itemprop="image">
                    <div class="product-info">
                        <h4 itemprop="name">MSI Gaming Laptop</h4>
                        <p itemprop="description">Dành cho gaming cao cấp</p>
                        <div class="price" itemprop="price">35,990,000đ</div>
                        <p>⭐ 4.6/5 (150 đánh giá)</p>
                        <button>Thêm vào giỏ</button>
                    </div>
                </article>
            </div>
        </main>
    </div>

    <footer>
        <p>&copy; 2024 Shop. Bảo lưu mọi quyền. |
            <a href="/privacy" style="color: white; text-decoration: none;">Chính sách riêng tư</a> •
            <a href="/terms" style="color: white; text-decoration: none;">Điều khoản</a>
        </p>
    </footer>
</body>
</html>
```

### Use Case 3: Documentation Website
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>HTML5 Documentation</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Courier New', monospace; background: #f5f5f5; }
        header { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: white; padding: 30px 20px; }
        .doc-container { display: grid; grid-template-columns: 250px 1fr 300px; gap: 20px; max-width: 1400px; margin: 20px auto; }
        nav { background: white; padding: 20px; border-radius: 8px; height: fit-content; position: sticky; top: 20px; }
        nav h3 { margin-bottom: 15px; color: #2c3e50; }
        nav ul { list-style: none; }
        nav li { margin-bottom: 8px; }
        nav a { color: #0066cc; text-decoration: none; font-size: 0.9em; }
        nav a.active { color: #e74c3c; font-weight: bold; }
        nav a:hover { text-decoration: underline; }
        main { background: white; padding: 30px; border-radius: 8px; }
        main h2 { color: #2c3e50; margin-top: 30px; margin-bottom: 15px; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        main h3 { color: #34495e; margin-top: 20px; margin-bottom: 10px; }
        section { margin-bottom: 30px; }
        code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: 'Courier New', monospace; }
        pre { background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 8px; overflow-x: auto; margin: 15px 0; }
        figure { margin: 20px 0; }
        figcaption { background: #f9f9f9; padding: 10px; border-left: 4px solid #3498db; margin-top: 10px; font-style: italic; color: #666; }
        aside { background: #fff3cd; padding: 20px; border-radius: 8px; height: fit-content; position: sticky; top: 20px; }
        aside h3 { color: #856404; margin-bottom: 15px; }
        aside ul { list-style: none; font-size: 0.9em; }
        aside li { margin-bottom: 8px; padding-left: 20px; position: relative; }
        aside li:before { content: "▸"; position: absolute; left: 0; color: #ff9800; }
        footer { background: #2c3e50; color: white; text-align: center; padding: 20px; margin-top: 50px; }
        @media (max-width: 1024px) {
            .doc-container { grid-template-columns: 1fr; }
            nav { position: static; }
            aside { position: static; }
        }
    </style>
</head>
<body>
    <header>
        <h1>HTML5 Documentation</h1>
        <p>Hướng dẫn hoàn chỉnh về HTML5 Semantic Elements</p>
    </header>

    <div class="doc-container">
        <nav aria-label="Documentation Navigation">
            <h3>Mục lục</h3>
            <ul>
                <li><a href="#introduction">Giới thiệu</a></li>
                <li>
                    <a href="#structure">Cấu trúc trang</a>
                    <ul style="margin-left: 15px;">
                        <li><a href="#header">Header</a></li>
                        <li><a href="#nav">Nav</a></li>
                        <li><a href="#main">Main</a></li>
                        <li><a href="#footer">Footer</a></li>
                    </ul>
                </li>
                <li>
                    <a href="#content">Content</a>
                    <ul style="margin-left: 15px;">
                        <li><a href="#article">Article</a></li>
                        <li><a href="#section">Section</a></li>
                        <li><a href="#aside">Aside</a></li>
                    </ul>
                </li>
                <li><a href="#best-practices">Best Practices</a></li>
            </ul>
        </nav>

        <main>
            <section id="introduction">
                <h2>Giới thiệu HTML5 Semantic Elements</h2>
                <p>HTML5 semantic elements cung cấp ý nghĩa rõ ràng cho cả browser và developer. Chúng giúp:</p>
                <ul>
                    <li>Cải thiện SEO</li>
                    <li>Tăng accessibility</li>
                    <li>Làm code dễ bảo trì hơn</li>
                    <li>Chuẩn hóa cấu trúc</li>
                </ul>
            </section>

            <section id="structure">
                <h2>Cấu trúc trang web</h2>

                <section id="header">
                    <h3>&lt;header&gt;</h3>
                    <p>Phần header của trang, thường chứa logo, tiêu đề, và navigation.</p>
                    <pre>
&lt;header&gt;
    &lt;h1&gt;Website Name&lt;/h1&gt;
    &lt;nav&gt;
        &lt;ul&gt;
            &lt;li&gt;&lt;a href="/"&gt;Home&lt;/a&gt;&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/nav&gt;
&lt;/header&gt;</pre>
                </section>

                <section id="nav">
                    <h3>&lt;nav&gt;</h3>
                    <p>Phần navigation của trang.</p>
                    <pre>
&lt;nav aria-label="Main Navigation"&gt;
    &lt;ul&gt;
        &lt;li&gt;&lt;a href="/"&gt;Home&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="/about"&gt;About&lt;/a&gt;&lt;/li&gt;
    &lt;/ul&gt;
&lt;/nav&gt;</pre>
                </section>

                <section id="main">
                    <h3>&lt;main&gt;</h3>
                    <p>Nội dung chính của trang. Chỉ có một &lt;main&gt; trong document.</p>
                    <pre>
&lt;main&gt;
    &lt;h1&gt;Main Content&lt;/h1&gt;
    &lt;article&gt;
        &lt;p&gt;Article content...&lt;/p&gt;
    &lt;/article&gt;
&lt;/main&gt;</pre>
                </section>

                <section id="footer">
                    <h3>&lt;footer&gt;</h3>
                    <p>Phần footer của trang.</p>
                    <pre>
&lt;footer&gt;
    &lt;p&gt;&copy; 2024 Company Name&lt;/p&gt;
    &lt;nav&gt;
        &lt;a href="/privacy"&gt;Privacy&lt;/a&gt;
    &lt;/nav&gt;
&lt;/footer&gt;</pre>
                </section>
            </section>

            <section id="content">
                <h2>Content Elements</h2>

                <section id="article">
                    <h3>&lt;article&gt;</h3>
                    <p>Nội dung độc lập, có thể tái sử dụng.</p>
                    <figure>
                        <pre>
&lt;article&gt;
    &lt;header&gt;
        &lt;h2&gt;Article Title&lt;/h2&gt;
        &lt;time datetime="2024-01-15"&gt;Jan 15&lt;/time&gt;
    &lt;/header&gt;
    &lt;p&gt;Content...&lt;/p&gt;
&lt;/article&gt;</pre>
                        <figcaption>Ví dụ cấu trúc article</figcaption>
                    </figure>
                </section>

                <section id="section">
                    <h3>&lt;section&gt;</h3>
                    <p>Nhóm nội dung có liên quan.</p>
                </section>

                <section id="aside">
                    <h3>&lt;aside&gt;</h3>
                    <p>Nội dung phụ, sidebar.</p>
                </section>
            </section>

            <section id="best-practices">
                <h2>Best Practices</h2>
                <ul>
                    <li>Luôn dùng semantic elements thay vì &lt;div&gt;</li>
                    <li>Duy trì heading hierarchy (h1 &gt; h2 &gt; h3)</li>
                    <li>Chỉ có một &lt;main&gt; trong document</li>
                    <li>Sử dụng &lt;section&gt; cho các phần logic</li>
                    <li>Sử dụng &lt;article&gt; cho nội dung độc lập</li>
                </ul>
            </section>
        </main>

        <aside>
            <h3>Quick Links</h3>
            <ul>
                <li><a href="#">MDN Web Docs</a></li>
                <li><a href="#">W3C HTML5 Spec</a></li>
                <li><a href="#">Can I Use</a></li>
                <li><a href="#">SEO Best Practices</a></li>
            </ul>

            <h3 style="margin-top: 30px;">Resources</h3>
            <details>
                <summary>Tools</summary>
                <ul style="margin-top: 10px;">
                    <li><a href="#">HTML Validator</a></li>
                    <li><a href="#">Accessibility Checker</a></li>
                    <li><a href="#">SEO Analyzer</a></li>
                </ul>
            </details>

            <h3 style="margin-top: 30px;">Recent Updates</h3>
            <ul>
                <li><time datetime="2024-01-20">Jan 20</time> - Cập nhật tài liệu</li>
                <li><time datetime="2024-01-15">Jan 15</time> - Thêm examples</li>
                <li><time datetime="2024-01-10">Jan 10</time> - Rework content</li>
            </ul>
        </aside>
    </div>

    <footer>
        <p>&copy; 2024 HTML5 Documentation. All rights reserved.</p>
    </footer>
</body>
</html>
```

### Use Case 4: News Website dengan Multiple Articles
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Tin tức công nghệ</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Georgia, serif; background: #f0f0f0; }
        header { background: white; border-bottom: 3px solid #d00; padding: 20px 0; }
        .header-content { max-width: 1000px; margin: 0 auto; padding: 0 20px; }
        header h1 { color: #d00; font-size: 2.5em; margin-bottom: 10px; }
        header p { color: #666; font-style: italic; }
        nav { background: #333; }
        nav ul { max-width: 1000px; margin: 0 auto; list-style: none; display: flex; }
        nav li { flex: 1; }
        nav a { display: block; color: white; text-decoration: none; padding: 15px 20px; text-align: center; transition: background 0.3s; }
        nav a:hover { background: #d00; }
        .main-container { max-width: 1000px; margin: 20px auto; padding: 0 20px; display: grid; grid-template-columns: 1fr 300px; gap: 30px; }
        main { background: white; }
        article { border-bottom: 2px solid #eee; padding-bottom: 30px; margin-bottom: 30px; }
        article:last-child { border-bottom: none; }
        article header { padding: 0; margin-bottom: 20px; }
        article h2 { color: #d00; font-size: 1.8em; margin-bottom: 10px; }
        .article-meta { color: #666; font-size: 0.9em; }
        article img { width: 100%; height: 300px; object-fit: cover; margin-bottom: 20px; border-radius: 4px; }
        article p { margin-bottom: 15px; line-height: 1.8; }
        aside { background: white; padding: 20px; border-radius: 4px; height: fit-content; }
        aside section { margin-bottom: 30px; }
        aside h3 { color: #d00; margin-bottom: 15px; font-size: 1.1em; }
        aside ul { list-style: none; }
        aside li { margin-bottom: 10px; }
        aside a { color: #0066cc; text-decoration: none; line-height: 1.4; }
        aside a:hover { text-decoration: underline; }
        .featured { background: #fff0f0; padding: 15px; border-left: 4px solid #d00; margin-bottom: 15px; }
        footer { background: #333; color: white; text-align: center; padding: 30px 20px; margin-top: 50px; }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>📰 Tin tức Công nghệ</h1>
            <p>Những tin tức mới nhất về công nghệ và digital</p>
        </div>
    </header>

    <nav aria-label="Main Navigation">
        <ul>
            <li><a href="/latest">Mới nhất</a></li>
            <li><a href="/tech">Công nghệ</a></li>
            <li><a href="/business">Kinh doanh</a></li>
            <li><a href="/science">Khoa học</a></li>
            <li><a href="/startups">Startup</a></li>
        </ul>
    </nav>

    <div class="main-container">
        <main>
            <article itemscope itemtype="https://schema.org/NewsArticle">
                <header>
                    <h2 itemprop="headline">AI sắp vượt qua khả năng của con người</h2>
                    <div class="article-meta">
                        <strong>Nguyễn Văn A</strong> •
                        <time datetime="2024-01-20" itemprop="datePublished">20 tháng 1, 2024</time> •
                        <span>5 phút đọc</span>
                    </div>
                </header>

                <img src="ai-news.jpg" alt="AI Technology" itemprop="image">

                <section itemprop="articleBody">
                    <p>Các nhà khoa học cho rằng trí tuệ nhân tạo đang phát triển với tốc độ chưa từng có. Trong những năm tới, AI sẽ có khả năng vượt qua khả năng của con người trong nhiều lĩnh vực.</p>
                    <p>Các công ty công nghệ lớn như OpenAI, Google, và Meta đang đầu tư hàng tỷ đô la vào nghiên cứu AI. Họ tin rằng AI sẽ là tương lai của công nghệ và thế giới.</p>
                </section>

                <footer style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;">
                    <p><strong>Tags:</strong>
                        <a href="/tag/ai">#AI</a>
                        <a href="/tag/technology">#Technology</a>
                        <a href="/tag/future">#Future</a>
                    </p>
                </footer>
            </article>

            <article itemscope itemtype="https://schema.org/NewsArticle">
                <header>
                    <h2 itemprop="headline">Apple ra mắt iPhone 15 Pro Max với chip A18 Bionic</h2>
                    <div class="article-meta">
                        <strong>Trần Thị B</strong> •
                        <time datetime="2024-01-19" itemprop="datePublished">19 tháng 1, 2024</time> •
                        <span>8 phút đọc</span>
                    </div>
                </header>

                <img src="iphone-news.jpg" alt="iPhone 15 Pro Max" itemprop="image">

                <section itemprop="articleBody">
                    <p>Apple vừa chính thức công bố iPhone 15 Pro Max với chip xử lý mới A18 Bionic. Đây là điện thoại thông minh mạnh nhất mà Apple từng sản xuất.</p>
                    <p>Chiếc điện thoại này có giá khởi điểm là 1.199 USD và sẽ có sẵn từ tháng 9.</p>
                </section>

                <footer style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;">
                    <p><strong>Tags:</strong>
                        <a href="/tag/apple">#Apple</a>
                        <a href="/tag/iphone">#iPhone</a>
                        <a href="/tag/devices">#Devices</a>
                    </p>
                </footer>
            </article>

            <article itemscope itemtype="https://schema.org/NewsArticle">
                <header>
                    <h2 itemprop="headline">Tesla giảm giá xe điện để cạnh tranh với BYD</h2>
                    <div class="article-meta">
                        <strong>Hoàng Văn C</strong> •
                        <time datetime="2024-01-18" itemprop="datePublished">18 tháng 1, 2024</time> •
                        <span>6 phút đọc</span>
                    </div>
                </header>

                <img src="tesla-news.jpg" alt="Tesla Electric Vehicles" itemprop="image">

                <section itemprop="articleBody">
                    <p>Tesla đã công bố giảm giá các mẫu xe điện của mình nhằm cạnh tranh với BYD, nhà sản xuất xe điện hàng đầu ở Trung Quốc.</p>
                    <p>Động thái này cho thấy cuộc cạnh tranh ngày càng gay gắt trong thị trường xe điện toàn cầu.</p>
                </section>

                <footer style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;">
                    <p><strong>Tags:</strong>
                        <a href="/tag/tesla">#Tesla</a>
                        <a href="/tag/ev">#EV</a>
                        <a href="/tag/business">#Business</a>
                    </p>
                </footer>
            </article>
        </main>

        <aside>
            <section class="featured">
                <h3>Tin nổi bật</h3>
                <ul>
                    <li><a href="#">Crypto suy thoái? Bitcoin rơi xuống 35K USD</a></li>
                    <li><a href="#">Meta cắt giảm 10.000 nhân viên</a></li>
                </ul>
            </section>

            <section>
                <h3>Danh mục</h3>
                <ul>
                    <li><a href="/tech">👨‍💻 Công nghệ (156)</a></li>
                    <li><a href="/business">💼 Kinh doanh (89)</a></li>
                    <li><a href="/science">🔬 Khoa học (45)</a></li>
                    <li><a href="/startups">🚀 Startup (72)</a></li>
                </ul>
            </section>

            <section>
                <h3>Thịnh hành</h3>
                <ul>
                    <li><a href="#">#AI</a></li>
                    <li><a href="#">#Web3</a></li>
                    <li><a href="#">#Metaverse</a></li>
                    <li><a href="#">#Blockchain</a></li>
                </ul>
            </section>

            <section>
                <h3>Theo dõi</h3>
                <p>Nhận thông báo về tin tức mới nhất.</p>
                <input type="email" placeholder="Email" style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 4px;">
                <button style="width: 100%; padding: 10px; background: #d00; color: white; border: none; border-radius: 4px; cursor: pointer;">Subscribe</button>
            </section>
        </aside>
    </div>

    <footer>
        <p>&copy; 2024 Tin tức Công nghệ. Bảo lưu mọi quyền. |
            <a href="/privacy" style="color: white; text-decoration: none;">Chính sách riêng tư</a> •
            <a href="/terms" style="color: white; text-decoration: none;">Điều khoản</a>
        </p>
    </footer>
</body>
</html>
```

### Use Case 5: FAQ Page with Details Element
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>FAQ - Câu hỏi thường gặp</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 40px 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        header { text-align: center; color: white; margin-bottom: 50px; }
        header h1 { font-size: 2.5em; margin-bottom: 10px; }
        header p { font-size: 1.1em; opacity: 0.9; }
        section { background: white; border-radius: 12px; padding: 0; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); overflow: hidden; }
        section h2 { background: #f8f9fa; padding: 20px; font-size: 1.5em; color: #333; border-bottom: 2px solid #667eea; }
        details { border-bottom: 1px solid #eee; }
        details:last-child { border-bottom: none; }
        summary { padding: 20px; cursor: pointer; font-weight: 600; color: #333; transition: all 0.3s; user-select: none; display: flex; align-items: center; justify-content: space-between; }
        summary:hover { background: #f8f9fa; }
        summary::after { content: '▼'; transition: transform 0.3s; font-size: 0.8em; color: #667eea; }
        details[open] summary::after { transform: rotate(180deg); }
        details[open] summary { background: #f8f9fa; color: #667eea; }
        .answer { padding: 0 20px 20px 20px; color: #666; line-height: 1.6; }
        .answer p { margin-bottom: 10px; }
        .answer code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: 'Courier New', monospace; }
        .answer ul { margin-left: 20px; margin-bottom: 10px; }
        .answer li { margin-bottom: 5px; }
        .category { margin-top: 30px; }
        .contact { background: white; border-radius: 12px; padding: 30px; text-align: center; margin-top: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
        .contact h2 { color: #333; margin-bottom: 15px; border: none; }
        .contact p { color: #666; margin-bottom: 15px; }
        .contact button { background: #667eea; color: white; padding: 12px 30px; border: none; border-radius: 6px; font-size: 1em; cursor: pointer; transition: background 0.3s; }
        .contact button:hover { background: #764ba2; }
        footer { text-align: center; color: white; margin-top: 40px; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>❓ Câu hỏi thường gặp</h1>
            <p>Tìm câu trả lời cho những câu hỏi phổ biến của bạn</p>
        </header>

        <section class="category">
            <h2>Về dịch vụ</h2>

            <details>
                <summary>Dịch vụ của bạn cung cấp những gì?</summary>
                <div class="answer">
                    <p>Chúng tôi cung cấp một bộ đầy đủ các dịch vụ web development bao gồm:</p>
                    <ul>
                        <li>Thiết kế web responsive</li>
                        <li>Phát triển front-end với HTML5, CSS3, JavaScript</li>
                        <li>Phát triển back-end với Node.js, Python, PHP</li>
                        <li>Tối ưu hóa SEO</li>
                        <li>Bảo trì và hỗ trợ kỹ thuật</li>
                    </ul>
                </div>
            </details>

            <details>
                <summary>Bạn có hỗ trợ website cũ không?</summary>
                <div class="answer">
                    <p>Có, chúng tôi hỗ trợ cập nhật, bảo trì, và nâng cấp website cũ. Chúng tôi có thể:</p>
                    <ul>
                        <li>Hiện đại hóa codebase</li>
                        <li>Cải thiện hiệu năng</li>
                        <li>Thêm tính năng mới</li>
                        <li>Sửa lỗi bảo mật</li>
                    </ul>
                </div>
            </details>

            <details>
                <summary>Bạn có cung cấp dịch vụ hosting không?</summary>
                <div class="answer">
                    <p>Không trực tiếp, nhưng chúng tôi có hợp tác với các nhà cung cấp hosting đáng tin cậy. Chúng tôi có thể:</p>
                    <ul>
                        <li>Giới thiệu hosting phù hợp</li>
                        <li>Giúp cài đặt và cấu hình</li>
                        <li>Quản lý domain</li>
                        <li>Cấu hình email</li>
                    </ul>
                </div>
            </details>
        </section>

        <section class="category">
            <h2>Giá cả và chi phí</h2>

            <details>
                <summary>Chi phí phát triển website bao nhiêu?</summary>
                <div class="answer">
                    <p>Chi phí phụ thuộc vào độ phức tạp và yêu cầu của dự án:</p>
                    <ul>
                        <li><strong>Website tĩnh:</strong> 1-3 triệu đồng</li>
                        <li><strong>Website động:</strong> 3-8 triệu đồng</li>
                        <li><strong>E-commerce:</strong> 8-20 triệu đồng</li>
                        <li><strong>Web app:</strong> 15+ triệu đồng</li>
                    </ul>
                </div>
            </details>

            <details>
                <summary>Có chi phí ẩn nào không?</summary>
                <div class="answer">
                    <p>Không. Chúng tôi cung cấp báo giá rõ ràng và chi tiết trước khi bắt đầu dự án. Tất cả chi phí đều được nêu rõ trong hợp đồng.</p>
                </div>
            </details>

            <details>
                <summary>Bạn có thanh toán trả góp không?</summary>
                <div class="answer">
                    <p>Có. Chúng tôi thường chia các dự án lớn thành nhiều giai đoạn với thanh toán 30-30-40:</p>
                    <ul>
                        <li>30% khi ký hợp đồng</li>
                        <li>30% khi hoàn thành 50% dự án</li>
                        <li>40% khi hoàn thành hoàn toàn</li>
                    </ul>
                </div>
            </details>
        </section>

        <section class="category">
            <h2>Kỹ thuật</h2>

            <details>
                <summary>Website của tôi sẽ tương thích với mobile không?</summary>
                <div class="answer">
                    <p>Có, tất cả website mà chúng tôi phát triển đều có design responsive, tương thích hoàn toàn với điện thoại, tablet, và máy tính để bàn.</p>
                </div>
            </details>

            <details>
                <summary>Website sẽ nhanh bao nhiêu?</summary>
                <div class="answer">
                    <p>Chúng tôi tối ưu hóa hiệu năng để đạt:</p>
                    <ul>
                        <li>Page load time dưới 2 giây</li>
                        <li>Lighthouse score 90+</li>
                        <li>Mobile performance tối ưu</li>
                    </ul>
                </div>
            </details>

            <details>
                <summary>Bạn có hỗ trợ HTTPS/SSL không?</summary>
                <div class="answer">
                    <p>Có, chúng tôi cấu hình HTTPS/SSL miễn phí cho tất cả dự án. Bảo mật là ưu tiên hàng đầu của chúng tôi.</p>
                </div>
            </details>

            <details>
                <summary>Thời gian phát triển cần bao lâu?</summary>
                <div class="answer">
                    <p>Phụ thuộc vào độ phức tạp:</p>
                    <ul>
                        <li><strong>Website tĩnh:</strong> 1-2 tuần</li>
                        <li><strong>Website động:</strong> 3-6 tuần</li>
                        <li><strong>E-commerce:</strong> 6-12 tuần</li>
                        <li><strong>Web app:</strong> 3-6 tháng</li>
                    </ul>
                </div>
            </details>
        </section>

        <section class="category">
            <h2>Hỗ trợ và bảo trì</h2>

            <details>
                <summary>Sau khi hoàn thành, bạn có hỗ trợ không?</summary>
                <div class="answer">
                    <p>Có. Chúng tôi cung cấp hỗ trợ miễn phí 30 ngày sau khi ra mắt, và có các gói hỗ trợ dài hạn khác nhau.</p>
                </div>
            </details>

            <details>
                <summary>Gói bảo trì hàng tháng bao gồm những gì?</summary>
                <div class="answer">
                    <p>Gói bảo trì bao gồm:</p>
                    <ul>
                        <li>Cập nhật bảo mật</li>
                        <li>Sửa lỗi nhỏ</li>
                        <li>Backup hàng tuần</li>
                        <li>Giám sát 24/7</li>
                        <li>Hỗ trợ kỹ thuật qua email/phone</li>
                    </ul>
                </div>
            </details>
        </section>

        <div class="contact">
            <h2>Vẫn có câu hỏi?</h2>
            <p>Hãy liên hệ với chúng tôi. Chúng tôi sẽ sẵn lòng giúp đỡ.</p>
            <button>📧 Liên hệ ngay</button>
        </div>

        <footer>
            <p>&copy; 2024 Company Name. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>
```

## 8.10. Tips & Tricks

### Tip 1: Landmark Navigation cho Screen Readers
```html
<!-- Giúp screen readers điều hướng dễ dàng -->
<a href="#main-content" class="skip-link">Bỏ qua đến nội dung chính</a>

<header role="banner">
    <h1>Website</h1>
</header>

<nav aria-label="Main Navigation" role="navigation">
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
    </ul>
</nav>

<main id="main-content" role="main">
    <!-- Main content -->
</main>

<aside role="complementary" aria-label="Sidebar">
    <!-- Sidebar content -->
</aside>

<footer role="contentinfo">
    <!-- Footer -->
</footer>

<style>
.skip-link {
    position: absolute;
    left: -10000px;
    top: auto;
    width: 1px;
    height: 1px;
    overflow: hidden;
}

.skip-link:focus {
    position: static;
    width: auto;
    height: auto;
}
</style>
```

### Tip 2: Nested Articles cho Comments
```html
<article>
    <h2>Blog Post</h2>
    <p>Post content...</p>

    <section>
        <h3>Comments</h3>
        <!-- Nested articles cho comments -->
        <article>
            <header>
                <strong>Commenter Name</strong>
                <time datetime="2024-01-20">Jan 20</time>
            </header>
            <p>Comment text...</p>

            <!-- Reply comment -->
            <article style="margin-left: 30px;">
                <header>
                    <strong>Reply</strong>
                    <time datetime="2024-01-21">Jan 21</time>
                </header>
                <p>Reply text...</p>
            </article>
        </article>
    </section>
</article>
```

### Tip 3: Using Section for Grouping Content
```html
<article>
    <h2>Article Title</h2>

    <!-- Multiple sections within article -->
    <section>
        <h3>Introduction</h3>
        <p>Intro content...</p>
    </section>

    <section>
        <h3>Main Content</h3>
        <p>Main content...</p>
    </section>

    <section>
        <h3>Conclusion</h3>
        <p>Conclusion content...</p>
    </section>
</article>
```

### Tip 4: Microdata cho SEO
```html
<article itemscope itemtype="https://schema.org/BlogPosting">
    <h2 itemprop="headline">Article Title</h2>

    <p>By <span itemprop="author">John Doe</span></p>

    <time datetime="2024-01-15" itemprop="datePublished">Jan 15, 2024</time>

    <img src="image.jpg" alt="Image" itemprop="image">

    <p itemprop="articleBody">Article content...</p>
</article>
```

### Tip 5: Details Element cho FAQs
```html
<section>
    <h2>FAQ</h2>

    <details>
        <summary>Question 1?</summary>
        <p>Answer 1...</p>
    </details>

    <details>
        <summary>Question 2?</summary>
        <p>Answer 2...</p>
    </details>

    <details>
        <summary>Question 3?</summary>
        <p>Answer 3...</p>
    </details>
</section>
```

### Tip 6: Figure with Code
```html
<figure>
    <pre><code>
&lt;header&gt;
    &lt;h1&gt;Title&lt;/h1&gt;
&lt;/header&gt;
    </code></pre>
    <figcaption>Listing 1: Semantic HTML structure</figcaption>
</figure>
```

### Tip 7: Multi-level Navigation
```html
<nav aria-label="Main Navigation">
    <ul>
        <li>
            <a href="/products">Products</a>
            <ul>
                <li><a href="/products/laptops">Laptops</a></li>
                <li><a href="/products/phones">Phones</a></li>
            </ul>
        </li>
        <li>
            <a href="/services">Services</a>
        </li>
    </ul>
</nav>
```

### Tip 8: Dialog Elements
```html
<!-- Simple dialog -->
<button onclick="openDialog()">Open Dialog</button>

<dialog id="myDialog">
    <h2>Dialog Title</h2>
    <p>Dialog content...</p>
    <button onclick="closeDialog()">Close</button>
</dialog>

<script>
function openDialog() {
    document.getElementById('myDialog').showModal();
}

function closeDialog() {
    document.getElementById('myDialog').close();
}
</script>
```

### Tip 9: Progress and Meter Elements
```html
<!-- Show progress -->
<label for="download">Download:</label>
<progress id="download" value="65" max="100">65%</progress>

<!-- Show measurement -->
<label for="disk">Disk usage:</label>
<meter id="disk" value="6" min="0" max="10" optimum="2" low="3" high="8">
    6 out of 10
</meter>
```

### Tip 10: Semantic Forms
```html
<form>
    <fieldset>
        <legend>Personal Information</legend>

        <label for="name">Name:</label>
        <input id="name" type="text" required>

        <label for="email">Email:</label>
        <input id="email" type="email" required>
    </fieldset>

    <fieldset>
        <legend>Preferences</legend>

        <label>
            <input type="checkbox"> Subscribe to newsletter
        </label>
    </fieldset>

    <button type="submit">Submit</button>
</form>
```

## 8.11. Common Mistakes

### Mistake 1: Overusing Sections
```html
<!-- ❌ SAI: Quá nhiều section -->
<div class="container">
    <section>
        <section>
            <section>
                <p>Content</p>
            </section>
        </section>
    </section>
</div>

<!-- ✅ ĐÚNG: Cấu trúc rõ ràng -->
<article>
    <h2>Main Title</h2>
    <section>
        <h3>Section Title</h3>
        <p>Content...</p>
    </section>
</article>
```

### Mistake 2: Multiple Main Elements
```html
<!-- ❌ SAI: Nhiều main elements -->
<main>
    <h1>First main content</h1>
</main>

<main>
    <h2>Second main content</h2>
</main>

<!-- ✅ ĐÚNG: Chỉ một main element -->
<main>
    <h1>Main Title</h1>
    <section>
        <h2>Section 1</h2>
    </section>
    <section>
        <h2>Section 2</h2>
    </section>
</main>
```

### Mistake 3: Misusing Aside
```html
<!-- ❌ SAI: Aside không liên quan đến nội dung -->
<main>
    <article>
        <h2>Blog Post</h2>
        <p>Content...</p>
    </article>
    <aside>
        <h3>Random sidebar</h3>
        <p>Completely unrelated content</p>
    </aside>
</main>

<!-- ✅ ĐÚNG: Aside liên quan hoặc sidebar chính thức -->
<main>
    <article>
        <h2>Blog Post</h2>
        <p>Content...</p>
    </article>
</main>

<aside>
    <h3>Related Articles</h3>
    <ul>
        <li><a href="#">Related post 1</a></li>
        <li><a href="#">Related post 2</a></li>
    </ul>
</aside>
```

### Mistake 4: Wrong Heading Hierarchy
```html
<!-- ❌ SAI: Skip heading levels -->
<article>
    <h1>Main Title</h1>
    <h3>Subsection</h3> <!-- Bỏ qua h2 -->
    <p>Content...</p>
</article>

<!-- ✅ ĐÚNG: Proper heading hierarchy -->
<article>
    <h1>Main Title</h1>
    <h2>Main Section</h2>
    <h3>Subsection</h3>
    <p>Content...</p>
</article>
```

### Mistake 5: Using Section Instead of Article
```html
<!-- ❌ SAI: Section cho nội dung độc lập -->
<section>
    <h2>Blog Post Title</h2>
    <p>Blog post content...</p>
</section>

<!-- ✅ ĐÚNG: Article cho nội dung độc lập -->
<article>
    <h2>Blog Post Title</h2>
    <p>Blog post content...</p>
</article>
```

### Mistake 6: Empty Sections
```html
<!-- ❌ SAI: Section không có heading -->
<section>
    <p>Some content without heading</p>
</section>

<!-- ✅ ĐÚNG: Section với heading -->
<section>
    <h2>Section Title</h2>
    <p>Some content...</p>
</section>
```

### Mistake 7: Forgetting aria-labels
```html
<!-- ❌ SAI: Nhiều nav, không có label -->
<nav>
    <ul>
        <li><a href="/">Home</a></li>
    </ul>
</nav>

<footer>
    <nav>
        <a href="/privacy">Privacy</a>
    </nav>
</footer>

<!-- ✅ ĐÚNG: Aria-labels cho mỗi nav -->
<nav aria-label="Main Navigation">
    <ul>
        <li><a href="/">Home</a></li>
    </ul>
</nav>

<footer>
    <nav aria-label="Footer Links">
        <a href="/privacy">Privacy</a>
    </nav>
</footer>
```

### Mistake 8: Not Using Figure for Images
```html
<!-- ❌ SAI: Image mà không có context -->
<h2>How to cook pasta</h2>
<img src="pasta.jpg" alt="cooked pasta">
<p>This is delicious...</p>

<!-- ✅ ĐÚNG: Figure với figcaption -->
<h2>How to cook pasta</h2>
<figure>
    <img src="pasta.jpg" alt="cooked pasta">
    <figcaption>Figure 1: Perfectly cooked pasta</figcaption>
</figure>
<p>This is delicious...</p>
```

### Mistake 9: Div Instead of Section/Article
```html
<!-- ❌ SAI: Overuse of div -->
<div class="article">
    <div class="header">
        <h2>Title</h2>
    </div>
    <div class="content">
        <p>Content...</p>
    </div>
</div>

<!-- ✅ ĐÚNG: Semantic elements -->
<article>
    <header>
        <h2>Title</h2>
    </header>
    <p>Content...</p>
</article>
```

### Mistake 10: Misplacing Header/Footer
```html
<!-- ❌ SAI: Header/Footer chỉ ở top/bottom -->
<article>
    <h2>Article Title</h2>
    <p>Content...</p>
    <!-- Quên footer -->
</article>

<!-- ✅ ĐÚNG: Header/Footer có thể ở bất kỳ đâu -->
<article>
    <header>
        <h2>Article Title</h2>
        <p>By Author | Date</p>
    </header>
    <p>Content...</p>
    <footer>
        <p>Tags: #html5 #semantic</p>
    </footer>
</article>
```

## 8.12. Troubleshooting Issues

### Issue 1: Screen Readers không đọc section
**Triệu chứng:** Section content không được đọc

**Nguyên nhân:**
- Section không có heading
- Section bị hidden bởi CSS

**Giải pháp:**
```html
<!-- Đảm bảo section có heading -->
<section>
    <h2>Section Title</h2> <!-- Bắt buộc -->
    <p>Content...</p>
</section>

<!-- Nếu cần ẩn nhưng vẫn readable -->
<section aria-hidden="false">
    <h2>Hidden Section</h2>
    <p>Content...</p>
</section>
```

### Issue 2: Multiple Main Elements
**Triệu chứng:** HTML validator báo lỗi

**Nguyên nhân:**
- Có nhiều `<main>` elements

**Giải pháp:**
```html
<!-- Chỉ có một main -->
<body>
    <header></header>
    <nav></nav>
    <main>
        <!-- Tất cả nội dung chính ở đây -->
    </main>
    <footer></footer>
</body>
```

### Issue 3: Nested Article Problems
**Triệu chứng:** Content organization không rõ

**Giải pháp:**
```html
<!-- Nested articles cho comments là OK -->
<article>
    <h2>Main Article</h2>
    <p>Article content...</p>

    <section>
        <h3>Comments</h3>
        <article>
            <header>
                <strong>Commenter</strong>
            </header>
            <p>Comment...</p>
        </article>
    </section>
</article>
```

### Issue 4: Dialog Not Closing
**Triệu chứng:** Dialog modal không đóng được

**Giải pháp:**
```javascript
const dialog = document.getElementById('myDialog');

// Đóng bằng nút
document.getElementById('closeBtn').addEventListener('click', () => {
    dialog.close();
});

// Đóng khi click backdrop
dialog.addEventListener('click', (e) => {
    if (e.target === dialog) {
        dialog.close();
    }
});

// Đóng bằng ESC key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && dialog.open) {
        dialog.close();
    }
});
```

### Issue 5: Figure Not Displaying Properly
**Triệu chứng:** Figure caption không aligned

**Giải pháp:**
```css
figure {
    margin: 20px 0;
    text-align: center;
}

figure img {
    max-width: 100%;
    height: auto;
    display: block;
}

figcaption {
    background: #f5f5f5;
    padding: 10px;
    font-size: 0.9em;
    font-style: italic;
    color: #666;
}
```

### Issue 6: Landmark Overload
**Triệu chứng:** Screen readers confused với nhiều landmarks

**Giải pháp:**
```html
<!-- Sử dụng aria-label để phân biệt -->
<nav aria-label="Main Navigation">
    <!-- Main nav -->
</nav>

<nav aria-label="Breadcrumb">
    <!-- Breadcrumb nav -->
</nav>

<aside aria-label="Sidebar">
    <!-- Sidebar -->
</aside>
```

### Issue 7: Empty Header
**Triệu chứng:** Header không có content

**Giải pháp:**
```html
<!-- ❌ SAI: Header trống -->
<article>
    <header></header> <!-- Không nên -->
    <p>Content...</p>
</article>

<!-- ✅ ĐÚNG: Header có content -->
<article>
    <header>
        <h2>Article Title</h2>
        <time datetime="2024-01-15">Jan 15, 2024</time>
    </header>
    <p>Content...</p>
</article>
```

### Issue 8: Section vs Article Confusion
**Triệu chứng:** Cấu trúc không rõ ràng

**Giải pháp:**
```javascript
// Quy tắc:
// - Nội dung độc lập? → <article>
// - Nội dung + heading liên quan? → <section>
// - Chỉ styling/layout? → <div>

// Ví dụ:
// Blog post (độc lập) → <article>
// Chapter (nhóm nội dung) → <section>
// Container styling → <div>
```

### Issue 9: Microdata Not Validating
**Triệu chứng:** Schema validation errors

**Giải pháp:**
```html
<!-- Đảm bảo proper itemscope/itemtype -->
<article itemscope itemtype="https://schema.org/BlogPosting">
    <h2 itemprop="headline">Title</h2>
    <img src="image.jpg" itemprop="image" alt="Image">
    <p itemprop="articleBody">Content...</p>
    <time datetime="2024-01-15" itemprop="datePublished">Jan 15</time>
    <span itemprop="author">Author Name</span>
</article>
```

### Issue 10: Accessibility Score Low
**Triệu chứng:** Lighthouse accessibility score thấp

**Giải pháp:**
```html
<!-- Sử dụng semantic elements -->
<header></header> <!-- Tự động có role="banner" -->
<nav></nav>       <!-- Tự động có role="navigation" -->
<main></main>     <!-- Tự động có role="main" -->
<footer></footer> <!-- Tự động có role="contentinfo" -->

<!-- Thêm aria-labels khi cần -->
<nav aria-label="Main Navigation"></nav>
<aside aria-label="Sidebar"></aside>

<!-- Đảm bảo heading hierarchy -->
<h1>Main Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
```

## 8.13. Advanced Topics

### Topic 1: Semantic SEO Strategy
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="description" content="Hướng dẫn HTML5 Semantic Elements">
    <title>HTML5 Semantic Elements - Hướng dẫn hoàn chỉnh</title>
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "HTML5 Semantic Elements Guide",
        "description": "Comprehensive guide to HTML5 semantic elements",
        "image": "https://example.com/image.jpg",
        "datePublished": "2024-01-15",
        "dateModified": "2024-01-20",
        "author": {
            "@type": "Person",
            "name": "John Doe"
        }
    }
    </script>
</head>
<body>
    <article itemscope itemtype="https://schema.org/BlogPosting">
        <header>
            <h1 itemprop="headline">HTML5 Semantic Elements</h1>
            <meta itemprop="description" content="Complete guide to HTML5 semantic elements">
            <img src="image.jpg" itemprop="image" alt="Semantic HTML">
        </header>

        <main itemprop="articleBody">
            <section>
                <h2>Introduction</h2>
                <p>Semantic HTML elements provide meaning to your content...</p>
            </section>

            <section>
                <h2>Elements</h2>
                <p>Common semantic elements include...</p>
            </section>
        </main>

        <footer>
            <meta itemprop="datePublished" content="2024-01-15">
            <meta itemprop="dateModified" content="2024-01-20">
            <span itemprop="author" itemscope itemtype="https://schema.org/Person">
                <meta itemprop="name" content="John Doe">
            </span>
        </footer>
    </article>
</body>
</html>
```

### Topic 2: Complex Layout with Semantic Elements
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Complex Semantic Layout</title>
    <style>
        body { display: grid; grid-template-columns: 200px 1fr 200px; grid-template-rows: auto 1fr auto; min-height: 100vh; }
        header { grid-column: 1 / -1; background: #333; color: white; padding: 20px; }
        nav { background: #f5f5f5; padding: 20px; }
        main { padding: 20px; background: white; }
        aside { background: #f5f5f5; padding: 20px; }
        footer { grid-column: 1 / -1; background: #333; color: white; padding: 20px; }
    </style>
</head>
<body>
    <header>
        <h1>Website</h1>
    </header>

    <nav aria-label="Primary Navigation">
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </nav>

    <main>
        <section>
            <h2>Main Content</h2>
            <article>
                <h3>Article 1</h3>
                <p>Content...</p>
            </article>
            <article>
                <h3>Article 2</h3>
                <p>Content...</p>
            </article>
        </section>
    </main>

    <aside aria-label="Complementary">
        <section>
            <h3>Related</h3>
            <ul>
                <li><a href="#">Link 1</a></li>
                <li><a href="#">Link 2</a></li>
            </ul>
        </section>
    </aside>

    <footer>
        <p>&copy; 2024</p>
    </footer>
</body>
</html>
```

### Topic 3: ARIA Enhancements
```html
<!-- Complex components with ARIA -->
<div role="region" aria-label="Live updates">
    <h2>Latest Updates</h2>
    <ul aria-live="polite" aria-atomic="true">
        <li>Update 1</li>
        <li>Update 2</li>
    </ul>
</div>

<!-- Tabs pattern -->
<div role="tablist">
    <button role="tab" aria-selected="true" aria-controls="panel1">Tab 1</button>
    <button role="tab" aria-selected="false" aria-controls="panel2">Tab 2</button>
</div>

<section role="tabpanel" id="panel1">Content 1</section>
<section role="tabpanel" id="panel2">Content 2</section>

<!-- Accordion pattern -->
<button aria-expanded="false" aria-controls="panel">Expand</button>
<section id="panel" hidden>Content</section>
```

### Topic 4: Progressive Enhancement
```html
<!-- Base semantic structure -->
<article>
    <header>
        <h2>Article</h2>
        <details>
            <summary>More info</summary>
            <p>Additional information</p>
        </details>
    </header>
</article>

<!-- JavaScript enhancement -->
<script>
if (!HTMLDetailsElement.prototype) {
    // Polyfill for older browsers
    const details = document.querySelectorAll('details');
    details.forEach(detail => {
        detail.addEventListener('click', function() {
            this.classList.toggle('open');
        });
    });
}
</script>
```

### Topic 5: Internationalization with Semantic HTML
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="language" content="Vietnamese">
</head>
<body>
    <header>
        <h1 lang="vi">Tiêu đề tiếng Việt</h1>
    </header>

    <main>
        <article lang="vi">
            <h2>Bài viết tiếng Việt</h2>
            <p>Nội dung tiếng Việt...</p>
        </article>

        <article lang="en">
            <h2>English Article</h2>
            <p>English content...</p>
        </article>
    </main>

    <footer>
        <nav aria-label="Language Selection">
            <ul>
                <li><a href="/?lang=vi" lang="vi">Tiếng Việt</a></li>
                <li><a href="/?lang=en" lang="en">English</a></li>
            </ul>
        </nav>
    </footer>
</body>
</html>
```

## 8.14. Bài tập thực hành

### Bài 1 (Dễ): Convert Div-based Layout to Semantic HTML
Chuyển đổi layout này sang semantic elements:
```html
<div id="header">
    <h1>Website</h1>
</div>
<div class="nav">
    <a href="/">Home</a>
</div>
<div id="content">
    <p>Content</p>
</div>
<div class="sidebar">
    <p>Sidebar</p>
</div>
<div id="footer">
    <p>Footer</p>
</div>
```

### Bài 2 (Dễ): Create a Simple Blog Post
Tạo bài đăng blog với semantic structure bao gồm:
- Header (tiêu đề, tác giả, ngày tháng)
- Nội dung chính
- Figure (hình ảnh + caption)
- Footer (tags)

### Bài 3 (Dễ): Build an FAQ Section
Tạo FAQ section sử dụng `<details>` và `<summary>` với ít nhất 5 câu hỏi

### Bài 4 (Dễ): Semantic Product Page
Tạo trang sản phẩm với:
- Breadcrumb navigation
- Product details
- Related products
- Customer reviews

### Bài 5 (Trung bình): Multi-section Article
Tạo bài viết dài với nhiều sections, subsections, và figures

### Bài 6 (Trung bình): News Portal Layout
Tạo trang tin tức với:
- Header và navigation
- Featured article
- Multiple article listings
- Sidebar with categories
- Footer

### Bài 7 (Trung bình): Documentation Site Structure
Tạo structure của documentation website với:
- Hierarchical navigation
- Table of contents
- Multiple sections
- Code examples (using figure)

### Bài 8 (Trung bình): E-commerce Category Page
Tạo trang danh mục sản phẩm với:
- Breadcrumb
- Filter sidebar
- Product grid
- Pagination

### Bài 9 (Trung bình): Forum Thread Layout
Tạo layout forum với:
- Thread header
- Original post
- Nested replies
- Comment form

### Bài 10 (Khó): Complete Website Mockup
Tạo một website hoàn chỉnh (5+ pages) với semantic HTML:
- Homepage
- About page
- Blog (multiple articles)
- Contact page
- Footer

### Bài 11 (Khó): Accessible Dashboard
Tạo dashboard với:
- Complex navigation
- Multiple sections
- Widgets
- ARIA labels
- Keyboard navigation

### Bài 12 (Khó): Progressive Enhancement with Details
Tạo interactive component sử dụng `<details>` với:
- CSS animations
- JavaScript enhancements
- Fallback cho browsers cũ
- Accessibility features

---

**Kết luận:** Semantic HTML5 elements là nền tảng của modern web development. Chúng giúp cải thiện SEO, accessibility, và code maintainability. Luôn ưu tiên sử dụng semantic elements thay vì `<div>` khi có thể. Chương tiếp theo sẽ tìm hiểu về HTML5 APIs.
