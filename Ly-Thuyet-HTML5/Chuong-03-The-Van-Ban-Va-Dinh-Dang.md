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

## 3.13. Use Cases Thực Tế

### 3.13.1. Recipe Page (Trang công thức nấu ăn)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Công Thức Phở Bò</title>
</head>
<body>
    <article>
        <header>
            <h1>Phở Bò Truyền Thống</h1>
            <p>
                <time datetime="2024-01-15">15 tháng 1, 2024</time> |
                Thời gian nấu: <time datetime="PT3H">3 giờ</time> |
                Khẩu phần: <data value="4">4 người</data>
            </p>
        </header>

        <section>
            <h2>Nguyên Liệu</h2>
            <dl>
                <dt><strong>Nước dùng:</strong></dt>
                <dd>
                    <ul>
                        <li>2kg xương bò</li>
                        <li>500g thịt bò</li>
                        <li>2 củ hành tây</li>
                        <li>Gừng: 100g</li>
                    </ul>
                </dd>

                <dt><strong>Gia vị:</strong></dt>
                <dd>
                    <ul>
                        <li>Hồi: 3 viên</li>
                        <li>Quế: 2 thanh</li>
                        <li>Muối, đường</li>
                    </ul>
                </dd>
            </dl>
        </section>

        <section>
            <h2>Cách Làm</h2>
            <ol>
                <li>
                    <p><strong>Sơ chế nguyên liệu</strong></p>
                    <p>Rửa sạch xương bò, chần qua nước sôi. <mark>Lưu ý:</mark> Chần 5 phút rồi vớt ra.</p>
                </li>
                <li>
                    <p><strong>Nấu nước dùng</strong></p>
                    <p>Cho xương vào nồi với <data value="5">5 lít</data> nước, đun sôi rồi hạ lửa nhỏ.</p>
                </li>
                <li>
                    <p><strong>Nêm nếm</strong></p>
                    <p>Thêm <abbr title="Muối">muối</abbr>, đường vừa ăn.</p>
                </li>
            </ol>

            <aside>
                <h3>💡 Mẹo hay</h3>
                <p><em>Rang hành, gừng trước khi cho vào nồi sẽ làm nước dùng thơm hơn.</em></p>
            </aside>
        </section>

        <section>
            <h2>Giá Trị Dinh Dưỡng</h2>
            <table border="1">
                <tr>
                    <th>Thành phần</th>
                    <th>Giá trị</th>
                </tr>
                <tr>
                    <td>Calories</td>
                    <td>450 kcal</td>
                </tr>
                <tr>
                    <td>Protein</td>
                    <td>35g</td>
                </tr>
            </table>
        </section>

        <footer>
            <p><small>&copy; 2024 - Bản quyền thuộc về <cite>Món Ngon Mỗi Ngày</cite></small></p>
        </footer>
    </article>
</body>
</html>
```

### 3.13.2. Scientific Article (Bài báo khoa học)

```html
<article>
    <header>
        <h1>Phương Trình Einstein</h1>
        <p>Bài viết về công thức nổi tiếng nhất trong vật lý</p>
    </header>

    <section>
        <h2>Công Thức</h2>
        <p>Công thức nổi tiếng của Einstein:</p>
        <p style="font-size: 24px; text-align: center;">
            <var>E</var> = <var>m</var><var>c</var><sup>2</sup>
        </p>

        <p>Trong đó:</p>
        <dl>
            <dt><var>E</var></dt>
            <dd>Năng lượng (Energy) đo bằng Joules</dd>

            <dt><var>m</var></dt>
            <dd>Khối lượng (Mass) đo bằng kilogram</dd>

            <dt><var>c</var></dt>
            <dd>Vận tốc ánh sáng (≈ 3 × 10<sup>8</sup> m/s)</dd>
        </dl>
    </section>

    <section>
        <h2>Ví Dụ Tính Toán</h2>
        <p>Tính năng lượng của 1kg vật chất:</p>

        <pre><code>
E = m × c²
E = 1kg × (3 × 10⁸ m/s)²
E = 1kg × 9 × 10¹⁶ m²/s²
E = 9 × 10¹⁶ Joules
        </code></pre>

        <p><mark>Kết quả:</mark> 1kg vật chất tương đương 9 × 10<sup>16</sup> Joules năng lượng!</p>
    </section>

    <section>
        <h2>Trích Dẫn</h2>
        <blockquote cite="https://example.com/einstein">
            <p>"Imagination is more important than knowledge."</p>
            <footer>— <cite>Albert Einstein</cite></footer>
        </blockquote>
    </section>

    <section>
        <h2>Các Công Thức Liên Quan</h2>
        <p>Công thức tính năng lượng động:</p>
        <p><var>KE</var> = ½<var>m</var><var>v</var><sup>2</sup></p>

        <p>Công thức tính thế năng trọng trường:</p>
        <p><var>PE</var> = <var>m</var><var>g</var><var>h</var></p>
    </section>
</article>
```

### 3.13.3. Technical Documentation (Tài liệu kỹ thuật)

```html
<article class="documentation">
    <h1>API Documentation: Array.map()</h1>

    <section>
        <h2>Mô tả</h2>
        <p>
            Phương thức <code>map()</code> tạo một mảng mới với kết quả của việc
            gọi một hàm được cung cấp trên mọi phần tử trong mảng gọi.
        </p>
    </section>

    <section>
        <h2>Cú pháp</h2>
        <pre><code>array.map(callback(element[, index[, array]])[, thisArg])</code></pre>
    </section>

    <section>
        <h2>Tham số</h2>
        <dl>
            <dt><code>callback</code></dt>
            <dd>
                Hàm được gọi cho mỗi phần tử. Nhận 3 tham số:
                <ul>
                    <li><var>element</var>: Phần tử hiện tại</li>
                    <li><var>index</var> (optional): Chỉ số của phần tử</li>
                    <li><var>array</var> (optional): Mảng gốc</li>
                </ul>
            </dd>

            <dt><code>thisArg</code> (optional)</dt>
            <dd>Giá trị sử dụng làm <code>this</code> khi thực thi callback</dd>
        </dl>
    </section>

    <section>
        <h2>Giá trị trả về</h2>
        <p>Một mảng mới với mỗi phần tử là kết quả của callback function.</p>
    </section>

    <section>
        <h2>Ví dụ</h2>

        <h3>Ví dụ 1: Nhân đôi các số</h3>
        <pre><code>const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
console.log(doubled);
// Output: <samp>[2, 4, 6, 8, 10]</samp></code></pre>

        <h3>Ví dụ 2: Lấy thuộc tính</h3>
        <pre><code>const users = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' }
];
const names = users.map(user => user.name);
console.log(names);
// Output: <samp>['John', 'Jane']</samp></code></pre>
    </section>

    <section>
        <h2>Lưu ý</h2>
        <aside>
            <p><strong>⚠️ Warning:</strong></p>
            <ul>
                <li><code>map()</code> <em>không</em> thay đổi mảng gốc</li>
                <li>Nếu không return trong callback, kết quả sẽ là <code>undefined</code></li>
                <li>Không nên dùng <code>map()</code> nếu không sử dụng kết quả trả về</li>
            </ul>
        </aside>
    </section>

    <section>
        <h2>Tương thích trình duyệt</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Browser</th>
                    <th>Version</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Chrome</td>
                    <td>✓ Tất cả</td>
                </tr>
                <tr>
                    <td>Firefox</td>
                    <td>✓ Tất cả</td>
                </tr>
                <tr>
                    <td>IE</td>
                    <td>✗ < IE9</td>
                </tr>
            </tbody>
        </table>
    </section>

    <section>
        <h2>Xem thêm</h2>
        <ul>
            <li><a href="#filter"><code>Array.filter()</code></a></li>
            <li><a href="#reduce"><code>Array.reduce()</code></a></li>
            <li><a href="#forEach"><code>Array.forEach()</code></a></li>
        </ul>
    </section>
</article>
```

### 3.13.4. Product Review (Đánh giá sản phẩm)

```html
<article itemscope itemtype="https://schema.org/Review">
    <header>
        <h1 itemprop="name">Đánh Giá iPhone 15 Pro Max</h1>
        <p>
            <span>Đánh giá bởi:</span>
            <span itemprop="author">Tech Reviewer</span> |
            <time itemprop="datePublished" datetime="2024-01-15">15/01/2024</time>
        </p>
        <p>
            <span>Rating:</span>
            <meter itemprop="ratingValue" min="0" max="5" value="4.5">4.5/5</meter>
            <data itemprop="ratingValue" value="4.5">4.5</data>/5 sao
        </p>
    </header>

    <section>
        <h2>Điểm Nổi Bật</h2>
        <ul>
            <li><strong>Màn hình:</strong> Super Retina XDR 6.7"</li>
            <li><strong>Chip:</strong> A17 Pro <small>(3nm)</small></li>
            <li><strong>Camera:</strong> 48MP Main + 12MP Ultra Wide</li>
            <li><strong>Pin:</strong> Dùng cả ngày</li>
        </ul>
    </section>

    <section>
        <h2>Ưu Điểm</h2>
        <ol>
            <li>
                <p><strong>Hiệu năng mạnh mẽ</strong></p>
                <p>Chip A17 Pro xử lý <em>cực kỳ</em> mượt mà, đa nhiệm <mark>không lag</mark>.</p>
            </li>
            <li>
                <p><strong>Camera xuất sắc</strong></p>
                <p>Chụp ảnh ban đêm cải thiện <ins>đáng kể</ins> so với thế hệ trước.</p>
            </li>
            <li>
                <p><strong>Thiết kế cao cấp</strong></p>
                <p>Khung Titanium, nhẹ hơn nhưng vẫn <strong>rất chắc chắn</strong>.</p>
            </li>
        </ol>
    </section>

    <section>
        <h2>Nhược Điểm</h2>
        <ul>
            <li><del>Port Lightning</del> → USB-C (một số người chưa quen)</li>
            <li>Giá cao: <s>$1,199</s> → Hiện: <strong>$1,099</strong></li>
            <li>Không có sạc nhanh kèm theo</li>
        </ul>
    </section>

    <section>
        <h2>Thông Số Kỹ Thuật</h2>
        <table border="1">
            <tr>
                <th>Màn hình</th>
                <td>6.7" OLED, 120Hz</td>
            </tr>
            <tr>
                <th>CPU</th>
                <td>A17 Pro (6-core)</td>
            </tr>
            <tr>
                <th>RAM</th>
                <td>8GB</td>
            </tr>
            <tr>
                <th>Dung lượng</th>
                <td>256GB / 512GB / 1TB</td>
            </tr>
            <tr>
                <th>Pin</th>
                <td>4,422 mAh</td>
            </tr>
        </table>
    </section>

    <section>
        <h2>Kết Luận</h2>
        <blockquote>
            <p>
                iPhone 15 Pro Max là <q>chiếc điện thoại tốt nhất năm 2024</q>
                với hiệu năng đỉnh cao và camera xuất sắc.
            </p>
        </blockquote>

        <p><strong>Đánh giá cuối cùng:</strong></p>
        <dl>
            <dt>Hiệu năng</dt>
            <dd><progress value="95" max="100">95%</progress> 95/100</dd>

            <dt>Camera</dt>
            <dd><progress value="90" max="100">90%</progress> 90/100</dd>

            <dt>Pin</dt>
            <dd><progress value="85" max="100">85%</progress> 85/100</dd>

            <dt>Giá trị</dt>
            <dd><progress value="75" max="100">75%</progress> 75/100</dd>
        </dl>
    </section>

    <section>
        <h2>Khuyến Nghị</h2>
        <p>
            <mark>NÊN MUA</mark> nếu bạn:
            <ul>
                <li>Cần hiệu năng cao nhất</li>
                <li>Chụp ảnh, quay video nhiều</li>
                <li>Muốn dùng lâu dài (5+ năm)</li>
            </ul>
        </p>

        <p>
            <mark>KHÔNG NÊN MUA</mark> nếu bạn:
            <ul>
                <li>Ngân sách hạn chế</li>
                <li>Chỉ dùng cơ bản (gọi, nhắn tin, mạng xã hội)</li>
                <li>Đã có iPhone 14 Pro Max</li>
            </ul>
        </p>
    </section>

    <footer>
        <p><small>Cảm ơn đã đọc! Bài viết có hữu ích không? <a href="#comments">Để lại bình luận</a></small></p>
    </footer>
</article>
```

### 3.13.5. FAQ Page (Trang câu hỏi thường gặp)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>FAQ - Câu Hỏi Thường Gặp</title>
</head>
<body>
    <h1>Câu Hỏi Thường Gặp về HTML5</h1>

    <details open>
        <summary><strong>HTML5 là gì?</strong></summary>
        <p>
            <dfn>HTML5</dfn> (<abbr title="HyperText Markup Language 5">HTML5</abbr>)
            là phiên bản thứ 5 của ngôn ngữ đánh dấu siêu văn bản, được sử dụng
            để tạo và cấu trúc nội dung trên <em>World Wide Web</em>.
        </p>
    </details>

    <details>
        <summary><strong>Sự khác biệt giữa HTML4 và HTML5?</strong></summary>
        <p>HTML5 có nhiều cải tiến so với HTML4:</p>
        <ul>
            <li>Semantic elements mới: <code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;article&gt;</code></li>
            <li>Native video và audio: <code>&lt;video&gt;</code>, <code>&lt;audio&gt;</code></li>
            <li>Canvas và SVG cho đồ họa</li>
            <li>LocalStorage và sessionStorage</li>
            <li>Geolocation API</li>
        </ul>
    </details>

    <details>
        <summary><strong>Làm thế nào để sử dụng thẻ <code>&lt;strong&gt;</code> và <code>&lt;b&gt;</code>?</strong></summary>
        <dl>
            <dt><code>&lt;strong&gt;</code></dt>
            <dd>Dùng khi muốn <strong>nhấn mạnh ý nghĩa quan trọng</strong> của nội dung</dd>

            <dt><code>&lt;b&gt;</code></dt>
            <dd>Dùng khi chỉ muốn <b>làm đậm text</b> mà không có ý nghĩa đặc biệt</dd>
        </dl>

        <p><mark>Ví dụ:</mark></p>
        <pre><code>&lt;p&gt;&lt;strong&gt;Cảnh báo:&lt;/strong&gt; Hành động này không thể hoàn tác!&lt;/p&gt;
&lt;p&gt;Từ khoá: &lt;b&gt;HTML5&lt;/b&gt;, &lt;b&gt;CSS3&lt;/b&gt;, &lt;b&gt;JavaScript&lt;/b&gt;&lt;/p&gt;</code></pre>
    </details>

    <details>
        <summary><strong>Khi nào dùng <code>&lt;em&gt;</code> và khi nào dùng <code>&lt;i&gt;</code>?</strong></summary>
        <table border="1">
            <thead>
                <tr>
                    <th>Thẻ</th>
                    <th>Sử dụng khi</th>
                    <th>Ví dụ</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>&lt;em&gt;</code></td>
                    <td>Nhấn mạnh</td>
                    <td>Bạn <em>phải</em> hoàn thành bài tập</td>
                </tr>
                <tr>
                    <td><code>&lt;i&gt;</code></td>
                    <td>Thuật ngữ, từ nước ngoài</td>
                    <td>Thiết kế <i>responsive</i></td>
                </tr>
            </tbody>
        </table>
    </details>

    <details>
        <summary><strong>Làm sao viết công thức toán học trong HTML?</strong></summary>
        <p>Sử dụng <code>&lt;sup&gt;</code> và <code>&lt;sub&gt;</code>:</p>

        <ul>
            <li>Bình phương: x<sup>2</sup> → <code>x&lt;sup&gt;2&lt;/sup&gt;</code></li>
            <li>Công thức nước: H<sub>2</sub>O → <code>H&lt;sub&gt;2&lt;/sub&gt;O</code></li>
            <li>Einstein: E = mc<sup>2</sup> → <code>E = mc&lt;sup&gt;2&lt;/sup&gt;</code></li>
        </ul>

        <p>Hoặc sử dụng <code>&lt;var&gt;</code> cho biến số:</p>
        <p><var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> = <var>c</var><sup>2</sup></p>
    </details>

    <details>
        <summary><strong>Làm sao tạo danh sách lồng nhau?</strong></summary>
        <p>Đặt <code>&lt;ul&gt;</code> hoặc <code>&lt;ol&gt;</code> bên trong <code>&lt;li&gt;</code>:</p>

        <pre><code>&lt;ul&gt;
    &lt;li&gt;Frontend
        &lt;ul&gt;
            &lt;li&gt;HTML&lt;/li&gt;
            &lt;li&gt;CSS&lt;/li&gt;
            &lt;li&gt;JavaScript&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/li&gt;
    &lt;li&gt;Backend
        &lt;ul&gt;
            &lt;li&gt;Node.js&lt;/li&gt;
            &lt;li&gt;Python&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/li&gt;
&lt;/ul&gt;</code></pre>
    </details>

    <details>
        <summary><strong>Thẻ <code>&lt;mark&gt;</code> dùng để làm gì?</strong></summary>
        <p>
            Thẻ <code>&lt;mark&gt;</code> dùng để <mark>đánh dấu</mark> hoặc
            <mark>highlight</mark> text quan trọng, thường được dùng trong
            kết quả tìm kiếm.
        </p>

        <p><strong>Ví dụ tìm kiếm:</strong></p>
        <p>Tìm kiếm: "<kbd>HTML5</kbd>"</p>
        <p>Kết quả: Học <mark>HTML5</mark> và CSS3 để làm web developer</p>
    </details>

    <hr>

    <section>
        <h2>Vẫn Còn Câu Hỏi?</h2>
        <p>Liên hệ với chúng tôi:</p>
        <address>
            Email: <a href="mailto:support@example.com">support@example.com</a><br>
            Điện thoại: <a href="tel:+84123456789">0123-456-789</a>
        </address>
    </section>
</body>
</html>
```

## 3.14. Tips & Tricks

### Tip 1: Sử dụng Semantic Elements đúng cách
```html
<!-- ✓ TỐT: Semantic và có ý nghĩa -->
<article>
    <h2>Tiêu đề bài viết</h2>
    <p>Nội dung...</p>
</article>

<!-- ✗ TRÁNH: Non-semantic -->
<div class="article">
    <div class="title">Tiêu đề bài viết</div>
    <div class="content">Nội dung...</div>
</div>
```

### Tip 2: Abbreviations nên có title attribute
```html
<!-- Cung cấp nghĩa đầy đủ cho người dùng -->
<p>
    <abbr title="Cascading Style Sheets">CSS</abbr> được dùng để styling.
    <abbr title="World Wide Web Consortium">W3C</abbr> quản lý các web standards.
</p>
```

### Tip 3: Sử dụng Description Lists cho metadata
```html
<!-- Tốt cho thông tin dạng key-value -->
<dl>
    <dt>Tác giả</dt>
    <dd>John Doe</dd>

    <dt>Ngày xuất bản</dt>
    <dd><time datetime="2024-01-15">15/01/2024</time></dd>

    <dt>Danh mục</dt>
    <dd>Web Development</dd>
</dl>
```

### Tip 4: Nested Lists cho cấu trúc phân cấp
```html
<ol>
    <li>Chuẩn bị môi trường
        <ol type="a">
            <li>Cài đặt Node.js</li>
            <li>Cài đặt VS Code</li>
            <li>Cài đặt Git</li>
        </ol>
    </li>
    <li>Tạo project</li>
    <li>Code và test</li>
</ol>
```

### Tip 5: Combine formatting tags
```html
<p>
    Đây là <strong><em>text vừa in đậm vừa nghiêng</em></strong>.
    Bạn có thể <mark><strong>highlight và in đậm</strong></mark> cùng lúc.
</p>
```

### Tip 6: Sử dụng <code> với <pre> cho code blocks
```html
<!-- Giữ nguyên format và indentation -->
<pre><code>function greet(name) {
    console.log(`Hello, ${name}!`);
}

greet('World');</code></pre>
```

### Tip 7: Ruby annotations cho ngôn ngữ Châu Á
```html
<!-- Phù hợp cho tiếng Nhật, Trung -->
<ruby>
    漢字 <rt>Kanji</rt>
</ruby>
```

### Tip 8: <kbd> cho keyboard shortcuts
```html
<p>
    Lưu file: <kbd>Ctrl</kbd> + <kbd>S</kbd><br>
    Copy: <kbd>Ctrl</kbd> + <kbd>C</kbd><br>
    Paste: <kbd>Ctrl</kbd> + <kbd>V</kbd>
</p>
```

### Tip 9: <samp> cho computer output
```html
<p>Khi bạn chạy lệnh, output sẽ là:</p>
<samp>
Hello, World!
Process finished with exit code 0
</samp>
```

### Tip 10: <wbr> cho line break hints
```html
<!-- Gợi ý cho browser nơi có thể ngắt dòng -->
<p>
    http://example.com/<wbr>very/<wbr>long/<wbr>url/<wbr>path/<wbr>filename.html
</p>
```

## 3.15. Common Mistakes (Lỗi Thường Gặp)

### Mistake 1: Bỏ qua Heading Hierarchy
```html
<!-- ✗ SAI: Skip từ h1 xuống h3 -->
<h1>Main Title</h1>
<h3>Subsection</h3> <!-- Bỏ qua h2 -->

<!-- ✓ ĐÚNG: Tuân theo hierarchy -->
<h1>Main Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
```

### Mistake 2: Dùng <br> thay vì <p>
```html
<!-- ✗ SAI: Lạm dụng <br> -->
Line 1<br>
Line 2<br>
Line 3<br>

<!-- ✓ ĐÚNG: Dùng paragraphs -->
<p>Line 1</p>
<p>Line 2</p>
<p>Line 3</p>
```

### Mistake 3: Dùng heading để styling
```html
<!-- ✗ SAI: Dùng h3 vì muốn text nhỏ hơn -->
<h3>This is not really a heading</h3>

<!-- ✓ ĐÚNG: Dùng CSS để style -->
<p class="large-text">Styled with CSS</p>
```

### Mistake 4: Quên alt attribute cho images trong content
```html
<!-- ✗ SAI: Không có alt -->
<img src="chart.jpg">

<!-- ✓ ĐÚNG: Có alt mô tả -->
<img src="chart.jpg" alt="Sales chart showing 25% growth">
```

### Mistake 5: Lồng <p> trong <p>
```html
<!-- ✗ SAI: Nested paragraphs -->
<p>
    Outer paragraph
    <p>Inner paragraph</p>
</p>

<!-- ✓ ĐÚNG: Separate paragraphs -->
<p>First paragraph</p>
<p>Second paragraph</p>
```

### Mistake 6: Dùng <b> và <i> thay vì <strong> và <em>
```html
<!-- ✗ SAI: Không semantic -->
<p><b>Warning:</b> This is important</p>

<!-- ✓ ĐÚNG: Semantic và có nghĩa -->
<p><strong>Warning:</strong> This is important</p>
```

### Mistake 7: Không đóng tags
```html
<!-- ✗ SAI: Không đóng <li> -->
<ul>
    <li>Item 1
    <li>Item 2
</ul>

<!-- ✓ ĐÚNG: Đóng đầy đủ tags -->
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
```

### Mistake 8: Sử dụng <u> cho underline
```html
<!-- ✗ SAI: <u> có thể nhầm với links -->
<p>This is <u>underlined</u> text</p>

<!-- ✓ ĐÚNG: Dùng CSS -->
<p>This is <span class="underline">underlined</span> text</p>
<!-- CSS: .underline { text-decoration: underline; } -->
```

### Mistake 9: Lạm dụng <div> và <span>
```html
<!-- ✗ SAI: Div soup -->
<div class="article">
    <div class="title">Title</div>
    <div class="content">Content</div>
</div>

<!-- ✓ ĐÚNG: Semantic elements -->
<article>
    <h2>Title</h2>
    <p>Content</p>
</article>
```

### Mistake 10: Không encode special characters
```html
<!-- ✗ SAI: Không encode -->
<p>5 < 10 && 10 > 5</p>

<!-- ✓ ĐÚNG: Encode HTML entities -->
<p>5 &lt; 10 &amp;&amp; 10 &gt; 5</p>
```

## 3.16. Troubleshooting (Xử Lý Sự Cố)

### Issue 1: Text không xuống dòng
**Vấn đề:** Text dài không tự động wrap

**Nguyên nhân:** CSS `white-space: nowrap` hoặc container quá hẹp

**Giải pháp:**
```css
p {
    word-wrap: break-word;
    overflow-wrap: break-word;
    word-break: break-word;
}
```

### Issue 2: Khoảng trắng bị collapse
**Vấn đề:** Multiple spaces hiển thị thành 1 space

**Nguyên nhân:** HTML collapse whitespace by default

**Giải pháp:**
```html
<!-- Option 1: Dùng <pre> -->
<pre>This  has    multiple   spaces</pre>

<!-- Option 2: Dùng CSS -->
<p style="white-space: pre;">This  has    multiple   spaces</p>

<!-- Option 3: Non-breaking space -->
<p>This&nbsp;&nbsp;has&nbsp;&nbsp;&nbsp;&nbsp;spaces</p>
```

### Issue 3: List bullets không hiển thị
**Vấn đề:** Bullet points của `<ul>` không nhìn thấy

**Nguyên nhân:** CSS reset hoặc padding bị remove

**Giải pháp:**
```css
ul {
    list-style: disc;
    padding-left: 40px;
}
```

### Issue 4: Heading hierarchy lỗi
**Vấn đề:** SEO và accessibility bị ảnh hưởng

**Giải pháp:** Kiểm tra hierarchy với browser DevTools
```html
<!-- Đúng hierarchy -->
<h1>Page Title</h1>
    <h2>Section</h2>
        <h3>Subsection</h3>
        <h3>Subsection</h3>
    <h2>Section</h2>
```

### Issue 5: Special characters hiển thị sai
**Vấn đề:** Ký tự đặc biệt như <, >, & hiển thị sai

**Giải pháp:** Sử dụng HTML entities
```html
<!-- HTML entities -->
&lt;    <!-- < -->
&gt;    <!-- > -->
&amp;   <!-- & -->
&quot;  <!-- " -->
&apos;  <!-- ' -->
&nbsp;  <!-- non-breaking space -->
&copy;  <!-- © -->
```

### Issue 6: <code> text quá dài overflow
**Vấn đề:** Code blocks tràn ra ngoài container

**Giải pháp:**
```css
pre {
    overflow-x: auto;
    white-space: pre;
}

code {
    word-wrap: break-word;
}
```

### Issue 7: Quote marks không đúng
**Vấn đề:** Dùng straight quotes thay vì curly quotes

**Giải pháp:**
```html
<!-- Dùng HTML entities cho curly quotes -->
<p>&ldquo;This is a quote&rdquo;</p>
<!-- Or let <q> handle it -->
<p><q>This is a quote</q></p>
```

### Issue 8: Text rendering khác nhau giữa các browsers
**Vấn đề:** Font, size, spacing khác nhau

**Giải pháp:**
```css
/* CSS reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.6;
}
```

## 3.17. Advanced Topics

### 3.17.1. Custom Data Attributes với Text Elements
```html
<p data-translation="vi" data-category="tutorial">
    Nội dung bằng tiếng Việt
</p>

<script>
const para = document.querySelector('p');
console.log(para.dataset.translation); // "vi"
console.log(para.dataset.category); // "tutorial"
</script>
```

### 3.17.2. Contenteditable Text
```html
<p contenteditable="true">
    Bạn có thể edit text này trực tiếp trong browser
</p>

<div contenteditable="true" style="border: 1px solid #ccc; padding: 10px;">
    <h2>Editable Heading</h2>
    <p>Editable paragraph</p>
</div>
```

### 3.17.3. Text Direction (RTL/LTR)
```html
<!-- Left-to-Right (default) -->
<p dir="ltr">This is English text</p>

<!-- Right-to-Left (Arabic, Hebrew) -->
<p dir="rtl">هذا نص عربي</p>

<!-- Auto direction -->
<p dir="auto">Automatic direction based on content</p>

<!-- BDI for mixed content -->
<ul>
    <li>User <bdi>إيان</bdi>: 123 points</li>
    <li>User <bdi>John</bdi>: 456 points</li>
</ul>
```

### 3.17.4. Text với Microdata
```html
<div itemscope itemtype="https://schema.org/Person">
    <h1 itemprop="name">John Doe</h1>
    <p>Email: <span itemprop="email">john@example.com</span></p>
    <p>Job: <span itemprop="jobTitle">Web Developer</span></p>
    <p>Company: <span itemprop="worksFor">ABC Corp</span></p>
</div>
```

### 3.17.5. Text Annotations với data-* attributes
```html
<p>
    The price is
    <data value="19.99" data-currency="USD">$19.99</data>
</p>

<p>
    Temperature:
    <data value="25" data-unit="celsius">25°C</data>
</p>
```

### 3.17.6. Progressive Enhancement với <time>
```html
<time datetime="2024-01-15T14:30:00Z" data-format="relative">
    15 Jan 2024, 2:30 PM
</time>

<script>
// JavaScript có thể convert sang "2 days ago"
const timeEl = document.querySelector('time');
const date = new Date(timeEl.getAttribute('datetime'));
// ... format as relative time
</script>
```

### 3.17.7. Typography với CSS
```html
<style>
/* Hyphenation */
p {
    hyphens: auto;
    -webkit-hyphens: auto;
    -ms-hyphens: auto;
}

/* Text ellipsis */
.truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Line clamping */
.clamp-3-lines {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
</style>

<p class="truncate">This is a very long text that will be truncated...</p>
<p class="clamp-3-lines">Long paragraph that will be limited to 3 lines...</p>
```

### 3.17.8. Text Selection Control
```html
<style>
/* Disable text selection */
.no-select {
    user-select: none;
    -webkit-user-select: none;
    -moz-user-select: none;
}

/* Custom selection color */
::selection {
    background-color: #ffeb3b;
    color: #000;
}
</style>

<p class="no-select">You cannot select this text</p>
<p>This text has custom selection color</p>
```

### 3.17.9. Accessibility Enhancements
```html
<!-- Screen reader only text -->
<style>
.sr-only {
    position: absolute;
    left: -10000px;
    width: 1px;
    height: 1px;
    overflow: hidden;
}
</style>

<a href="/download">
    Download
    <span class="sr-only">(PDF, 2.5MB)</span>
</a>

<!-- ARIA labels -->
<p>
    Price: <data value="99.99" aria-label="Ninety nine dollars and ninety nine cents">$99.99</data>
</p>
```

### 3.17.10. Multi-language Support
```html
<html lang="vi">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <p>Đây là tiếng Việt</p>

    <p lang="en">This is English</p>

    <p lang="fr">C'est français</p>

    <blockquote lang="de">
        <p>Das ist Deutsch</p>
    </blockquote>
</body>
</html>
```

## 3.18. Bài Tập Thực Hành (Mở Rộng)

### Bài 1: Basic Text Formatting
**Mục tiêu:** Làm quen với các thẻ text formatting cơ bản

**Yêu cầu:**
- Tạo trang HTML với tất cả 6 levels headings
- Sử dụng ít nhất 5 thẻ formatting khác nhau (strong, em, mark, code, etc.)
- Include subscript và superscript
- Tạo ít nhất 2 paragraphs có formatting

### Bài 2: Lists và Nested Lists
**Mục tiêu:** Thực hành với các loại lists

**Yêu cầu:**
- Tạo unordered list với 5 items
- Tạo ordered list với type="A" và start="3"
- Tạo nested list (list trong list) ít nhất 2 levels
- Tạo description list với 4 terms

### Bài 3: Scientific Article
**Mục tiêu:** Áp dụng formatting cho nội dung khoa học

**Yêu cầu:**
- Viết một bài về công thức toán học hoặc hóa học
- Sử dụng sup và sub cho công thức
- Sử dụng var cho biến số
- Include code examples với pre và code
- Tạo ít nhất 1 blockquote

### Bài 4: Recipe Page
**Mục tiêu:** Tạo trang công thức nấu ăn

**Yêu cầu:**
- Header với tên món ăn
- Unordered list cho nguyên liệu
- Ordered list cho các bước làm
- Sử dụng time cho thời gian nấu
- Include tips với aside hoặc mark

### Bài 5: Product Description
**Mục tiêu:** Tạo mô tả sản phẩm chi tiết

**Yêu cầu:**
- Product name với h1
- Description với paragraphs
- Features list
- Specifications với description list
- Price với data element
- Include customer reviews với blockquote

### Bài 6: Technical Documentation
**Mục tiêu:** Viết documentation cho một function

**Yêu cầu:**
- Function name và description
- Parameters với dl
- Return value
- Code examples với pre và code
- Sử dụng kbd cho keyboard shortcuts
- Sử dụng samp cho output examples

### Bài 7: FAQ Page
**Mục tiêu:** Tạo trang câu hỏi thường gặp

**Yêu cầu:**
- Tạo ít nhất 6 câu hỏi
- Sử dụng details và summary
- Include code examples nếu cần
- Sử dụng abbr cho viết tắt
- Add contact information với address

### Bài 8: Blog Post
**Mục tiêu:** Tạo blog post hoàn chỉnh

**Yêu cầu:**
- Title, author, date với proper elements
- Multiple sections với h2, h3
- Formatted content với strong, em, mark
- Include quotes với blockquote
- Lists cho bullet points
- Code examples nếu phù hợp
- Footer với tags hoặc categories

### Bài 9: Comparison Article
**Mục tiêu:** So sánh 2-3 items

**Yêu cầu:**
- Introduction section
- Pros/cons lists cho mỗi item
- Use case descriptions
- Final recommendation
- Rating với progress hoặc meter
- Include table cho comparison

### Bài 10: News Article
**Mục tiêu:** Viết bài tin tức

**Yêu cầu:**
- Headline với h1
- Byline (author, date)
- Lead paragraph
- Body với multiple paragraphs
- Quotes từ sources
- Related articles list
- Tags hoặc categories

### Bài 11: Tutorial Page
**Mục tiêu:** Tạo tutorial hoàn chỉnh

**Yêu cầu:**
- Introduction
- Prerequisites list
- Step-by-step instructions với ordered list
- Code examples cho mỗi step
- Tips và warnings với mark
- Troubleshooting section
- Conclusion

### Bài 12: Portfolio Page
**Mục tiêu:** Tạo trang portfolio cá nhân

**Yêu cầu:**
- About me section
- Skills list (nested list)
- Project descriptions
- Contact information với address
- Resume/CV info với dl
- Use semantic elements throughout

## 3.19. Tổng Kết

Trong chương này chúng ta đã học:
- Headings và importance của hierarchy
- Text formatting tags (bold, italic, underline, etc.)
- Quotations và citations
- Lists (ordered, unordered, description)
- Special elements (time, progress, meter)
- Best practices cho text content

---

**Chương tiếp theo:** Chúng ta sẽ tìm hiểu về Links và Navigation trong HTML5.
