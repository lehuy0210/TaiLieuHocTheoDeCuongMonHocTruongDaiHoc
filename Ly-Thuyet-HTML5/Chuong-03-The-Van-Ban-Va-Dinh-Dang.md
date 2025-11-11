# CHƯƠNG 3: CÁC THẺ VĂN BẢN VÀ ĐỊNH DẠNG

## 3.1. Headings (Thẻ tiêu đề)

### 3.1.1. Các cấp độ Heading

HTML có 6 cấp độ heading từ `<h1>` đến `<h6>`:

```html
<h1>Heading Level 1 - Quan trọng nhất</h1>
<h2>Heading Level 2</h2>
<h3>Heading Level 3</h3>
<h4>Heading Level 4</h4>
<h5>Heading Level 5</h5>
<h6>Heading Level 6 - Ít quan trọng nhất</h6>
```

### 3.1.2. Heading hierarchy

**Đúng - Tuân thủ hierarchy:**
```html
<h1>Main Title</h1>
    <h2>Section 1</h2>
        <h3>Subsection 1.1</h3>
        <h3>Subsection 1.2</h3>
    <h2>Section 2</h2>
        <h3>Subsection 2.1</h3>
            <h4>Detail 2.1.1</h4>
```

**Tránh - Không skip levels:**
```html
<!-- Không nên -->
<h1>Title</h1>
<h3>Subsection</h3> <!-- Bỏ qua h2 -->
```

### 3.1.3. Best practices

1. **Mỗi trang chỉ nên có 1 `<h1>`:**
```html
<h1>Page Title</h1>
<!-- Nội dung trang -->
```

2. **Không dùng heading để tạo style:**
```html
<!-- SAI -->
<h3>Text muốn to hơn</h3>

<!-- ĐÚNG -->
<p class="large-text">Text muốn to hơn</p>
```

3. **Sử dụng cho SEO:**
```html
<h1>Sản phẩm chính</h1>
<h2>Tính năng nổi bật</h2>
<h2>Thông số kỹ thuật</h2>
<h2>Đánh giá khách hàng</h2>
```

## 3.2. Paragraphs (Đoạn văn)

### 3.2.1. Thẻ `<p>`

```html
<p>Đây là một đoạn văn bản. Nó có thể chứa nhiều câu.</p>

<p>Đây là đoạn văn thứ hai. Trình duyệt tự động thêm khoảng cách
giữa các đoạn văn.</p>
```

### 3.2.2. Formatting trong paragraph

```html
<p>
    Đoạn văn có thể chứa <strong>text in đậm</strong>,
    <em>text nghiêng</em>, và <mark>text được đánh dấu</mark>.
</p>
```

### 3.2.3. Line breaks trong paragraph

```html
<p>
    Dòng 1<br>
    Dòng 2<br>
    Dòng 3
</p>
```

## 3.3. Text Formatting Tags

### 3.3.1. Bold và Strong

**`<b>` - Bold (chỉ về mặt hiển thị):**
```html
<p>Đây là <b>text in đậm</b> với thẻ b</p>
```

**`<strong>` - Strong importance (có ý nghĩa semantic):**
```html
<p><strong>Cảnh báo:</strong> Nội dung quan trọng</p>
```

**Khi nào dùng gì:**
- `<strong>`: Khi muốn nhấn mạnh ý nghĩa
- `<b>`: Khi chỉ muốn hiển thị đậm không có ý nghĩa đặc biệt

### 3.3.2. Italic và Emphasis

**`<i>` - Italic (chỉ về mặt hiển thị):**
```html
<p>Thuật ngữ <i>responsive design</i> được dùng phổ biến</p>
```

**`<em>` - Emphasis (có ý nghĩa semantic):**
```html
<p>Bạn <em>phải</em> hoàn thành bài tập này</p>
```

**Khi nào dùng gì:**
- `<em>`: Nhấn mạnh ý nghĩa
- `<i>`: Thuật ngữ kỹ thuật, từ nước ngoài, suy nghĩ

### 3.3.3. Underline

**`<u>` - Underline:**
```html
<p>Text có <u>gạch chân</u></p>
```

**Lưu ý:** Tránh dùng `<u>` vì có thể nhầm với links

### 3.3.4. Strikethrough

**`<s>` - Strikethrough (nội dung không còn chính xác):**
```html
<p>Giá gốc: <s>1,000,000đ</s> Giá sale: 800,000đ</p>
```

**`<del>` - Deleted text:**
```html
<p>Tên cũ: <del>ABC Company</del></p>
<p>Tên mới: <ins>XYZ Corporation</ins></p>
```

### 3.3.5. Insert

**`<ins>` - Inserted text:**
```html
<p>Giá: 500,000đ <ins>+ VAT</ins></p>
```

### 3.3.6. Mark/Highlight

**`<mark>` - Highlighted text:**
```html
<p>Tìm kiếm: "HTML5"</p>
<p>Kết quả: <mark>HTML5</mark> là ngôn ngữ markup...</p>
```

### 3.3.7. Small text

**`<small>` - Smaller text:**
```html
<p>Copyright &copy; 2024 <small>All rights reserved</small></p>
```

### 3.3.8. Subscript và Superscript

**`<sub>` - Subscript:**
```html
<p>H<sub>2</sub>O (Nước)</p>
<p>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> (Glucose)</p>
```

**`<sup>` - Superscript:**
```html
<p>E = mc<sup>2</sup></p>
<p>10<sup>3</sup> = 1000</p>
<p>X<sup>2</sup> + Y<sup>2</sup> = Z<sup>2</sup></p>
```

### 3.3.9. Code và Technical Text

**`<code>` - Inline code:**
```html
<p>Sử dụng hàm <code>console.log()</code> để debug</p>
```

**`<pre>` - Preformatted text:**
```html
<pre>
function hello() {
    console.log("Hello World");
}
</pre>
```

**`<code>` + `<pre>` - Code blocks:**
```html
<pre><code>
const arr = [1, 2, 3];
arr.forEach(item => {
    console.log(item);
});
</code></pre>
```

**`<kbd>` - Keyboard input:**
```html
<p>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy</p>
<p>Press <kbd>Cmd</kbd> + <kbd>V</kbd> to paste</p>
```

**`<samp>` - Sample output:**
```html
<p>Kết quả: <samp>Error 404: Page not found</samp></p>
```

**`<var>` - Variable:**
```html
<p>Phương trình: <var>x</var> + <var>y</var> = 10</p>
```

## 3.4. Quotations

### 3.4.1. Blockquote

**`<blockquote>` - Block quotation:**
```html
<blockquote cite="https://source.com">
    <p>Đây là một đoạn trích dẫn dài từ nguồn khác.
    Blockquote thường được indent và có styling riêng.</p>
</blockquote>
```

**Với citation:**
```html
<blockquote cite="https://www.example.com">
    <p>The only way to do great work is to love what you do.</p>
    <footer>— <cite>Steve Jobs</cite></footer>
</blockquote>
```

### 3.4.2. Inline Quote

**`<q>` - Inline quotation:**
```html
<p>Như Steve Jobs đã nói: <q>Stay hungry, stay foolish</q></p>
```

**Browser tự động thêm dấu ngoặc kép.**

### 3.4.3. Citation

**`<cite>` - Citation/Reference:**
```html
<p>Thông tin được tham khảo từ <cite>HTML5 Specification</cite></p>
<p><cite>The Great Gatsby</cite> by F. Scott Fitzgerald</p>
```

### 3.4.4. Abbreviation

**`<abbr>` - Abbreviation:**
```html
<p>
    <abbr title="HyperText Markup Language">HTML</abbr>
    và
    <abbr title="Cascading Style Sheets">CSS</abbr>
</p>

<p>
    <abbr title="World Health Organization">WHO</abbr>
    was founded in 1948.
</p>
```

## 3.5. Address và Contact Information

**`<address>` - Contact information:**
```html
<address>
    Viết bởi: <a href="mailto:john@example.com">John Doe</a><br>
    Địa chỉ: 123 Đường ABC, Quận 1, TP.HCM<br>
    Điện thoại: <a href="tel:+84123456789">0123-456-789</a>
</address>
```

**Sử dụng trong footer:**
```html
<footer>
    <address>
        <strong>Công ty TNHH ABC</strong><br>
        Email: <a href="mailto:info@abc.com">info@abc.com</a><br>
        Website: <a href="https://abc.com">abc.com</a>
    </address>
</footer>
```

## 3.6. Lists (Danh sách)

### 3.6.1. Unordered Lists

**`<ul>` - Unordered list (bullet points):**
```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

**Nested lists:**
```html
<ul>
    <li>Frontend
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </li>
    <li>Backend
        <ul>
            <li>Node.js</li>
            <li>Python</li>
            <li>PHP</li>
        </ul>
    </li>
</ul>
```

### 3.6.2. Ordered Lists

**`<ol>` - Ordered list (numbered):**
```html
<ol>
    <li>Bước 1: Chuẩn bị</li>
    <li>Bước 2: Thực hiện</li>
    <li>Bước 3: Kiểm tra</li>
</ol>
```

**Attributes của `<ol>`:**

**type** - Kiểu số đếm:
```html
<!-- Số thập phân (mặc định) -->
<ol type="1">
    <li>Item 1</li>
    <li>Item 2</li>
</ol>

<!-- Chữ hoa -->
<ol type="A">
    <li>Item A</li>
    <li>Item B</li>
</ol>

<!-- Chữ thường -->
<ol type="a">
    <li>Item a</li>
    <li>Item b</li>
</ol>

<!-- Số La Mã hoa -->
<ol type="I">
    <li>Item I</li>
    <li>Item II</li>
</ol>

<!-- Số La Mã thường -->
<ol type="i">
    <li>Item i</li>
    <li>Item ii</li>
</ol>
```

**start** - Bắt đầu từ số:
```html
<ol start="5">
    <li>Item 5</li>
    <li>Item 6</li>
    <li>Item 7</li>
</ol>
```

**reversed** - Đếm ngược:
```html
<ol reversed>
    <li>Item 3</li>
    <li>Item 2</li>
    <li>Item 1</li>
</ol>
```

**value** - Giá trị cụ thể cho `<li>`:
```html
<ol>
    <li value="10">Item 10</li>
    <li>Item 11</li>
    <li value="20">Item 20</li>
    <li>Item 21</li>
</ol>
```

### 3.6.3. Description Lists

**`<dl>`, `<dt>`, `<dd>` - Description list:**
```html
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language - Ngôn ngữ đánh dấu siêu văn bản</dd>

    <dt>CSS</dt>
    <dd>Cascading Style Sheets - Bảng định dạng theo tầng</dd>

    <dt>JavaScript</dt>
    <dd>Ngôn ngữ lập trình cho web</dd>
</dl>
```

**Multiple definitions:**
```html
<dl>
    <dt>Frontend</dt>
    <dt>Client-side</dt>
    <dd>Phần giao diện người dùng của website</dd>

    <dt>Backend</dt>
    <dt>Server-side</dt>
    <dd>Phần xử lý logic và database</dd>
</dl>
```

**Với styling:**
```html
<dl>
    <dt><strong>Tên:</strong></dt>
    <dd>John Doe</dd>

    <dt><strong>Email:</strong></dt>
    <dd><a href="mailto:john@example.com">john@example.com</a></dd>

    <dt><strong>Địa chỉ:</strong></dt>
    <dd>123 Main Street, City</dd>
</dl>
```

### 3.6.4. List Best Practices

1. **Semantic correctness:**
```html
<!-- Dùng ul cho danh sách không có thứ tự -->
<ul>
    <li>Táo</li>
    <li>Cam</li>
    <li>Chuối</li>
</ul>

<!-- Dùng ol cho danh sách có thứ tự -->
<ol>
    <li>Mở file</li>
    <li>Chỉnh sửa</li>
    <li>Lưu file</li>
</ol>
```

2. **List items phải là direct children:**
```html
<!-- ĐÚNG -->
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<!-- SAI -->
<ul>
    <div>
        <li>Item 1</li>
    </div>
</ul>
```

## 3.7. Horizontal Rules

**`<hr>` - Horizontal rule:**
```html
<p>Section 1</p>
<hr>
<p>Section 2</p>
```

**Styling hr:**
```html
<hr style="border: 2px solid red;">
<hr style="border: none; height: 2px; background: #333;">
```

## 3.8. Line Breaks

**`<br>` - Line break:**
```html
<p>
    Line 1<br>
    Line 2<br>
    Line 3
</p>
```

**Address example:**
```html
<address>
    John Doe<br>
    123 Main Street<br>
    City, State 12345<br>
    USA
</address>
```

**Word Break Opportunity `<wbr>`:**
```html
<p>
    http://example.com/<wbr>very/<wbr>long/<wbr>url/<wbr>path
</p>
```

## 3.9. Text Direction

### 3.9.1. BDI - Bi-Directional Isolation

**`<bdi>` - Isolate text direction:**
```html
<ul>
    <li>User <bdi>اسم</bdi>: 123 points</li>
    <li>User <bdi>John</bdi>: 456 points</li>
</ul>
```

### 3.9.2. BDO - Bi-Directional Override

**`<bdo>` - Override text direction:**
```html
<p><bdo dir="rtl">This text will be right-to-left</bdo></p>
<p><bdo dir="ltr">This text will be left-to-right</bdo></p>
```

## 3.10. Other Text Elements

### 3.10.1. Definition

**`<dfn>` - Definition term:**
```html
<p>
    <dfn>HTML</dfn> là ngôn ngữ đánh dấu siêu văn bản.
</p>

<p>
    <dfn id="html-def">
        <abbr title="HyperText Markup Language">HTML</abbr>
    </dfn>
    là ngôn ngữ được sử dụng để tạo các trang web.
</p>
```

### 3.10.2. Time

**`<time>` - Date/Time:**
```html
<p>Sự kiện diễn ra vào <time datetime="2024-12-25">25/12/2024</time></p>

<p>Giờ mở cửa: <time datetime="09:00">9:00 AM</time></p>

<p>
    <time datetime="2024-12-25T20:00">
        25 Tháng 12, 2024 lúc 8:00 PM
    </time>
</p>
```

### 3.10.3. Progress

**`<progress>` - Progress bar:**
```html
<label for="file">Downloading progress:</label>
<progress id="file" value="70" max="100">70%</progress>

<progress value="0.7">70%</progress>
```

### 3.10.4. Meter

**`<meter>` - Scalar measurement:**
```html
<label for="disk">Disk usage:</label>
<meter id="disk" value="0.6">60%</meter>

<meter min="0" max="100" low="25" high="75" optimum="50" value="80">
    80 out of 100
</meter>
```

## 3.11. Ruby Annotations (Chú thích phiên âm)

**`<ruby>`, `<rt>`, `<rp>` - Ruby annotations:**
```html
<ruby>
    漢 <rp>(</rp><rt>Kan</rt><rp>)</rp>
    字 <rp>(</rp><rt>ji</rt><rp>)</rp>
</ruby>

<p>
    <ruby>
        明日 <rt>Ashita</rt>
    </ruby>
    là "ngày mai" trong tiếng Nhật
</p>
```

## 3.12. Practical Examples

### 3.12.1. Blog Post

```html
<article>
    <header>
        <h1>HTML5 Semantic Elements</h1>
        <p>
            <time datetime="2024-01-15">January 15, 2024</time>
            by <address><a href="mailto:john@example.com">John Doe</a></address>
        </p>
    </header>

    <p>
        <strong>HTML5</strong> giới thiệu nhiều <em>semantic elements</em>
        mới giúp cải thiện cấu trúc trang web.
    </p>

    <blockquote>
        <p>Semantic HTML makes your code more readable and accessible.</p>
        <footer>— <cite>MDN Web Docs</cite></footer>
    </blockquote>

    <h2>Các elements quan trọng:</h2>
    <ul>
        <li><code>&lt;article&gt;</code></li>
        <li><code>&lt;section&gt;</code></li>
        <li><code>&lt;nav&gt;</code></li>
    </ul>
</article>
```

### 3.12.2. Product Description

```html
<div class="product">
    <h2>Laptop ABC Model X</h2>

    <p class="price">
        <s>$1,200</s>
        <strong>$999</strong>
        <small>(Tiết kiệm $201)</small>
    </p>

    <dl>
        <dt>CPU</dt>
        <dd>Intel Core i7</dd>

        <dt>RAM</dt>
        <dd>16GB DDR4</dd>

        <dt>Storage</dt>
        <dd>512GB SSD</dd>
    </dl>

    <p><mark>Còn hàng</mark> - Giao hàng trong 24h</p>
</div>
```

### 3.12.3. Code Documentation

```html
<section class="api-docs">
    <h2>Function: <code>calculateTotal()</code></h2>

    <p>
        <strong>Description:</strong> Tính tổng giá trị của mảng.
    </p>

    <h3>Syntax</h3>
    <pre><code>calculateTotal(array, tax)</code></pre>

    <h3>Parameters</h3>
    <dl>
        <dt><var>array</var></dt>
        <dd>Mảng số cần tính tổng</dd>

        <dt><var>tax</var></dt>
        <dd>Tỷ lệ thuế (mặc định: 0.1)</dd>
    </dl>

    <h3>Example</h3>
    <pre><code>
const prices = [100, 200, 300];
const total = calculateTotal(prices, 0.08);
console.log(total); // Output: <samp>648</samp>
    </code></pre>
</section>
```

## 3.13. Bài tập thực hành

### Bài 1: Text Formatting
Tạo trang HTML với:
- Tất cả 6 levels của headings
- Paragraphs với các text formatting khác nhau
- Ví dụ về subscript và superscript
- Code examples với `<code>` và `<pre>`

### Bài 2: Lists
Tạo:
- Unordered list với nested items
- Ordered list với type và start attributes
- Description list cho thuật ngữ kỹ thuật

### Bài 3: Quotations và Citations
Tạo trang với:
- Blockquote với citation
- Inline quotes
- Abbreviations với tooltips
- Address information

### Bài 4: Complete Article
Tạo một bài viết blog hoàn chỉnh với:
- Proper heading hierarchy
- Formatted text (bold, italic, etc.)
- Lists
- Blockquotes
- Code examples
- Time và author information

## 3.14. Tổng kết

Trong chương này chúng ta đã học:
- Headings và importance của hierarchy
- Text formatting tags (bold, italic, underline, etc.)
- Quotations và citations
- Lists (ordered, unordered, description)
- Special elements (time, progress, meter)
- Best practices cho text content

---

**Chương tiếp theo:** Chúng ta sẽ tìm hiểu về Links và Navigation trong HTML5.
