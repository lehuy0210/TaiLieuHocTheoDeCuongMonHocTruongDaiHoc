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

## 8.9. Bài tập thực hành

### Bài 1: Convert non-semantic to semantic
Chuyển đổi layout `<div>` sang semantic elements

### Bài 2: Blog Layout
Tạo blog layout hoàn chỉnh với semantic HTML

### Bài 3: Landing Page
Tạo landing page với header, sections, aside, footer

### Bài 4: E-commerce Product Page
Tạo trang sản phẩm với semantic markup và microdata

---

**Kết luận:** Semantic HTML5 elements giúp code dễ đọc, maintain, tốt cho SEO và accessibility. Luôn ưu tiên sử dụng semantic elements thay vì `<div>` khi có thể. Chương tiếp theo sẽ tìm hiểu về HTML5 APIs.
