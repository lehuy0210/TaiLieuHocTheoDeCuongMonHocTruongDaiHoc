# 100 BÀI TẬP HTML5, CSS3, ES6

## Mục lục
- [Phần 1: HTML5 (35 bài)](#phần-1-html5)
- [Phần 2: CSS3 (35 bài)](#phần-2-css3)
- [Phần 3: ES6 (30 bài)](#phần-3-es6)

---

# PHẦN 1: HTML5 (35 bài)

## 📗 BÀI DỄ (18 bài)

### Bài 1: Trang HTML cơ bản ⭐
**Đề bài:** Tạo file HTML5 hoàn chỉnh với cấu trúc cơ bản, có tiêu đề "Trang web của tôi", và 1 đoạn văn giới thiệu.

**Gợi ý:**
- Dùng `<!DOCTYPE html>`
- Có thẻ `<html>`, `<head>`, `<body>`
- Meta charset UTF-8
- Thẻ `<title>` và `<h1>`

---

### Bài 2: Danh sách sinh viên ⭐
**Đề bài:** Tạo danh sách không có thứ tự (unordered list) gồm 5 tên sinh viên trong lớp.

**Gợi ý:**
- Dùng `<ul>` và `<li>`
- Mỗi sinh viên là 1 `<li>`

---

### Bài 3: Bảng thời khóa biểu ⭐
**Đề bài:** Tạo bảng thời khóa biểu 1 tuần (7 ngày), mỗi ngày có 4 tiết học.

**Gợi ý:**
- Dùng `<table>`, `<thead>`, `<tbody>`
- Dòng đầu là các thứ (Thứ 2, 3, 4...)
- 4 dòng tiếp theo là 4 tiết học

---

### Bài 4: Form đăng ký cơ bản ⭐
**Đề bài:** Tạo form đăng ký với các trường: Họ tên, Email, Mật khẩu, Nút Submit.

**Gợi ý:**
- `<form>` với method="POST"
- `<input type="text">` cho họ tên
- `<input type="email">` cho email
- `<input type="password">` cho mật khẩu
- `<button type="submit">`

---

### Bài 5: Thẻ định dạng văn bản ⭐
**Đề bài:** Tạo đoạn văn có chứa: text in đậm, in nghiêng, gạch dưới, và đánh dấu (highlight).

**Gợi ý:**
- `<strong>` hoặc `<b>` cho in đậm
- `<em>` hoặc `<i>` cho in nghiêng
- `<u>` cho gạch dưới
- `<mark>` cho highlight

---

### Bài 6: Liên kết trang ⭐
**Đề bài:** Tạo 1 trang HTML có 3 links: Facebook, YouTube, Google. Links mở tab mới.

**Gợi ý:**
- `<a href="URL" target="_blank">`
- URLs: facebook.com, youtube.com, google.com

---

### Bài 7: Chèn hình ảnh ⭐
**Đề bài:** Tạo trang HTML hiển thị 3 hình ảnh (có thể dùng URL online), mỗi ảnh có mô tả.

**Gợi ý:**
- `<img src="URL" alt="Mô tả">`
- Dùng placeholder images: picsum.photos hoặc unsplash.com

---

### Bài 8: Video player ⭐
**Đề bài:** Nhúng 1 video YouTube vào trang HTML.

**Gợi ý:**
- Lấy embed code từ YouTube (Share > Embed)
- Dùng `<iframe>`

---

### Bài 9: Audio player ⭐
**Đề bài:** Tạo audio player có thể phát file âm thanh, có controls.

**Gợi ý:**
- `<audio controls>`
- `<source src="file.mp3" type="audio/mpeg">`
- Có thể dùng file audio online

---

### Bài 10: Checkbox và Radio ⭐
**Đề bài:** Tạo form khảo sát với:
- Checkbox: Sở thích (Đọc sách, Xem phim, Chơi game)
- Radio: Giới tính (Nam, Nữ, Khác)

**Gợi ý:**
- `<input type="checkbox">` cho nhiều lựa chọn
- `<input type="radio" name="gender">` cho 1 lựa chọn
- Dùng `<label>` cho mỗi input

---

### Bài 11: Dropdown menu ⭐
**Đề bài:** Tạo dropdown cho phép chọn quốc gia (Việt Nam, Mỹ, Nhật, Hàn Quốc, Trung Quốc).

**Gợi ý:**
- `<select>` và `<option>`
- Mỗi quốc gia là 1 `<option value="code">`

---

### Bài 12: Textarea ⭐
**Đề bài:** Tạo form góp ý với textarea cho phép nhập tối đa 500 ký tự.

**Gợi ý:**
- `<textarea maxlength="500">`
- Có thể thêm `rows` và `cols`

---

### Bài 13: Thẻ semantic ⭐
**Đề bài:** Tạo cấu trúc trang web với header, nav, main, aside, footer.

**Gợi ý:**
- `<header>`: Logo và tiêu đề
- `<nav>`: Menu điều hướng
- `<main>`: Nội dung chính
- `<aside>`: Sidebar
- `<footer>`: Thông tin footer

---

### Bài 14: Figure và Figcaption ⭐
**Đề bài:** Hiển thị 1 hình ảnh với caption "Hình 1: Phong cảnh đẹp".

**Gợi ý:**
- `<figure>`
- `<img>` bên trong
- `<figcaption>` cho caption

---

### Bài 15: Anchor links ⭐
**Đề bài:** Tạo trang dài có mục lục ở đầu, click vào mục lục sẽ nhảy đến section tương ứng.

**Gợi ý:**
- Dùng `<a href="#section1">`
- Thêm `id="section1"` cho section
- Có nút "Back to top"

---

### Bài 16: Email và Phone links ⭐
**Đề bài:** Tạo trang liên hệ với link gửi email và gọi điện thoại.

**Gợi ý:**
- `<a href="mailto:email@example.com">`
- `<a href="tel:+84123456789">`

---

### Bài 17: Details và Summary ⭐
**Đề bài:** Tạo FAQ với 3 câu hỏi, click vào hiển thị câu trả lời.

**Gợi ý:**
- `<details>` và `<summary>`
- Mỗi FAQ là 1 cặp details/summary

---

### Bài 18: Progress bar ⭐
**Đề bài:** Hiển thị thanh progress cho download (70% hoàn thành).

**Gợi ý:**
- `<progress value="70" max="100">`
- Hoặc `<meter>`

---

## 📘 BÀI TRUNG BÌNH (14 bài)

### Bài 19: Form đăng ký đầy đủ ⭐⭐
**Đề bài:** Tạo form đăng ký hoàn chỉnh với validation:
- Họ tên (required, min 3 ký tự)
- Email (required, format email)
- Số điện thoại (10 số)
- Ngày sinh (date picker)
- Giới tính (radio)
- Sở thích (checkbox, ít nhất 1)
- Mật khẩu (min 8 ký tự)
- Xác nhận mật khẩu (phải giống mật khẩu)
- Checkbox đồng ý điều khoản (required)

**Gợi ý:**
- Dùng attributes: `required`, `minlength`, `pattern`
- `pattern="[0-9]{10}"` cho số điện thoại
- JavaScript để check password confirmation

---

### Bài 20: Bảng dữ liệu phức tạp ⭐⭐
**Đề bài:** Tạo bảng điểm của 5 sinh viên, 3 môn học, có cột tổng điểm và xếp loại. Dùng colspan và rowspan.

**Gợi ý:**
- `<table>`, `<thead>`, `<tbody>`, `<tfoot>`
- `colspan` cho merge columns
- `rowspan` cho merge rows
- Tính tổng điểm ở tfoot

---

### Bài 21: Navigation menu responsive ⭐⭐
**Đề bài:** Tạo menu điều hướng ngang với dropdown cho mục "Sản phẩm".

**Gợi ý:**
- `<nav>` với `<ul>` lồng nhau
- Dropdown dùng `<ul>` con
- CSS `:hover` cho dropdown (sẽ làm trong CSS)

---

### Bài 22: Card layout ⭐⭐
**Đề bài:** Tạo 6 product cards, mỗi card có: ảnh, tiêu đề, mô tả, giá, nút "Mua ngay".

**Gợi ý:**
- Dùng `<article>` cho mỗi card
- Cấu trúc semantic
- Prepare cho CSS flexbox/grid

---

### Bài 23: Form tìm kiếm nâng cao ⭐⭐
**Đề bài:** Tạo form tìm kiếm với:
- Từ khóa (search input)
- Danh mục (select)
- Khoảng giá (2 number inputs: min, max)
- Ngày (date range)
- Nút "Tìm kiếm" và "Reset"

**Gợi ý:**
- `<input type="search">`
- `<input type="number" min="0">`
- `<input type="date">`
- `<button type="reset">`

---

### Bài 24: Image gallery ⭐⭐
**Đề bài:** Tạo gallery 12 ảnh, có lazy loading và responsive images.

**Gợi ý:**
- `<img loading="lazy">`
- `srcset` cho responsive
- `<picture>` element

---

### Bài 25: Video gallery ⭐⭐
**Đề bài:** Tạo gallery 4 videos với thumbnails, click vào thumbnail để play video.

**Gợi ý:**
- `<video poster="thumbnail.jpg">`
- `controls` attribute
- JavaScript để play/pause

---

### Bài 26: Multi-step form ⭐⭐
**Đề bài:** Tạo form đăng ký 3 bước:
- Bước 1: Thông tin cá nhân
- Bước 2: Địa chỉ
- Bước 3: Xác nhận

**Gợi ý:**
- Dùng `<fieldset>` cho mỗi bước
- JavaScript để show/hide steps
- Progress indicator

---

### Bài 27: Breadcrumb navigation ⭐⭐
**Đề bài:** Tạo breadcrumb: Home > Sản phẩm > Laptop > Dell XPS 13

**Gợi ý:**
- `<nav aria-label="Breadcrumb">`
- `<ol>` cho ordered list
- Current page với `aria-current="page"`

---

### Bài 28: Accordion FAQ ⭐⭐
**Đề bài:** Tạo accordion với 5 FAQs, chỉ mở 1 item tại 1 thời điểm.

**Gợi ý:**
- Có thể dùng `<details>` + JavaScript
- Hoặc custom với div + button
- ARIA attributes cho accessibility

---

### Bài 29: Modal dialog ⭐⭐
**Đề bài:** Tạo modal dialog hiển thị form đăng nhập khi click nút.

**Gợi ý:**
- `<dialog>` element
- JavaScript: `showModal()`, `close()`
- ESC key để đóng

---

### Bài 30: Accessible form ⭐⭐
**Đề bài:** Tạo form contact hoàn toàn accessible với ARIA labels, error messages, và focus management.

**Gợi ý:**
- `aria-label`, `aria-describedby`
- `aria-invalid` cho errors
- `role="alert"` cho error messages
- Test với screen reader

---

### Bài 31: Data table với sorting ⭐⭐
**Đề bài:** Tạo bảng danh sách sinh viên có thể sort theo tên, điểm, lớp.

**Gợi ý:**
- `<table>` với proper headers
- `<th scope="col">`
- JavaScript cho sorting
- Arrow indicators (▲▼)

---

### Bài 32: Calendar picker ⭐⭐
**Đề bài:** Tạo form booking với date range picker (từ ngày - đến ngày).

**Gợi ý:**
- 2 `<input type="date">`
- Validation: đến ngày >= từ ngày
- Display số ngày selected

---

## 📕 BÀI KHÓ (3 bài)

### Bài 33: Blog layout hoàn chỉnh ⭐⭐⭐
**Đề bài:** Tạo layout blog hoàn chỉnh với:
- Header: Logo, search, user menu
- Navigation: Categories menu
- Main content: 3 blog posts với thumbnail, excerpt, author, date, tags
- Sidebar: Recent posts, categories, tags cloud
- Comments section với nested comments
- Footer: Links, social media, copyright

**Gợi ý:**
- Semantic HTML5 hoàn chỉnh
- Proper heading hierarchy
- Microdata/Schema.org markup
- Accessibility features
- SEO optimization

---

### Bài 34: E-commerce product page ⭐⭐⭐
**Đề bài:** Tạo trang sản phẩm e-commerce với:
- Breadcrumb navigation
- Image gallery (thumbnails + main image)
- Product info: title, price, rating, description
- Specifications table
- Size/color selector
- Quantity selector
- Add to cart button
- Related products
- Reviews section với rating
- Q&A section

**Gợi ý:**
- Schema.org Product markup
- `<picture>` cho responsive images
- Form cho selectors
- Accessible tabs/accordion
- localStorage cho cart

---

### Bài 35: Dashboard admin ⭐⭐⭐
**Đề bài:** Tạo dashboard admin với:
- Sidebar navigation
- Top bar: notifications, user profile
- Stats cards: users, orders, revenue, growth
- Charts placeholders
- Recent orders table (sortable, pagination)
- Activity timeline
- Quick actions
- Responsive design

**Gợi ý:**
- Grid/Flexbox layout
- SVG icons
- Canvas cho charts (placeholder)
- Data tables
- Responsive sidebar (collapse on mobile)

---

# PHẦN 2: CSS3 (35 bài)

## 📗 BÀI DỄ (18 bài)

### Bài 36: Styling text cơ bản ⭐
**Đề bài:** Style đoạn văn với: font Arial, size 16px, line-height 1.6, màu xám đậm, text-align justify.

**Gợi ý:**
```css
p {
    font-family: Arial, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: #333;
    text-align: justify;
}
```

---

### Bài 37: Box model cơ bản ⭐
**Đề bài:** Tạo box có: width 300px, height 200px, padding 20px, border 2px solid, margin 10px, background màu xanh nhạt.

**Gợi ý:**
- `box-sizing: border-box;` để width tính cả padding và border

---

### Bài 38: Button styling ⭐
**Đề bài:** Style button với: background xanh, text trắng, padding 10px 20px, border-radius 5px, không có border, cursor pointer. Hover thì background đậm hơn.

**Gợi ý:**
```css
button:hover {
    background-color: darkblue;
}
```

---

### Bài 39: Link styling ⭐
**Đề bài:** Style links với các states: normal (blue), visited (purple), hover (red, underline), active (green).

**Gợi ý:**
- `a:link`, `a:visited`, `a:hover`, `a:active`

---

### Bài 40: List styling ⭐
**Đề bài:** Remove bullets từ list và thêm custom style: background cho mỗi item, padding, margin-bottom.

**Gợi ý:**
```css
ul {
    list-style: none;
}
li {
    background: #f0f0f0;
    padding: 10px;
    margin-bottom: 5px;
}
```

---

### Bài 41: Image styling ⭐
**Đề bài:** Style images: width 100%, max-width 400px, border-radius 10px, box-shadow.

**Gợi ý:**
```css
img {
    width: 100%;
    max-width: 400px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

---

### Bài 42: Gradient background ⭐
**Đề bài:** Tạo background gradient từ xanh sang tím, từ trái sang phải.

**Gợi ý:**
```css
background: linear-gradient(to right, blue, purple);
```

---

### Bài 43: Border và outline ⭐
**Đề bài:** Tạo box với border solid 2px, border-radius 8px. Khi focus, hiển thị outline màu xanh.

**Gợi ý:**
```css
.box:focus {
    outline: 2px solid blue;
}
```

---

### Bài 44: Transform cơ bản ⭐
**Đề bài:** Tạo square, khi hover thì rotate 45 độ và scale lên 1.2 lần.

**Gợi ý:**
```css
.square:hover {
    transform: rotate(45deg) scale(1.2);
}
```

---

### Bài 45: Transition hiệu ứng ⭐
**Đề bài:** Button thay đổi màu khi hover với transition mượt mà trong 0.3s.

**Gợi ý:**
```css
button {
    transition: background-color 0.3s ease;
}
```

---

### Bài 46: Centering element ⭐
**Đề bài:** Center 1 div (width 300px) theo cả 2 chiều trong viewport.

**Gợi ý:**
```css
/* Flexbox */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
```

---

### Bài 47: Overlay effect ⭐
**Đề bài:** Tạo image với overlay text, khi hover overlay hiện lên.

**Gợi ý:**
- Position relative cho container
- Position absolute cho overlay
- `opacity: 0` ban đầu, `opacity: 1` khi hover

---

### Bài 48: Card hover effect ⭐
**Đề bài:** Card nâng lên (translateY) và shadow đậm hơn khi hover.

**Gợi ý:**
```css
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
```

---

### Bài 49: Loading spinner ⭐
**Đề bài:** Tạo loading spinner quay tròn bằng border và animation.

**Gợi ý:**
```css
.spinner {
    border: 4px solid #f3f3f3;
    border-top: 4px solid blue;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
```

---

### Bài 50: Tooltip ⭐
**Đề bài:** Tạo tooltip hiện khi hover vào element.

**Gợi ý:**
- Dùng pseudo-element `::after`
- `content` attribute
- Position absolute

---

### Bài 51: CSS Variables ⭐
**Đề bài:** Define CSS variables cho colors (primary, secondary, text) và dùng trong page.

**Gợi ý:**
```css
:root {
    --primary-color: #007bff;
    --text-color: #333;
}

.button {
    background: var(--primary-color);
}
```

---

### Bài 52: Sticky header ⭐
**Đề bài:** Tạo header stick ở top khi scroll.

**Gợi ý:**
```css
header {
    position: sticky;
    top: 0;
    z-index: 100;
}
```

---

### Bài 53: Custom checkbox ⭐
**Đề bài:** Tạo custom checkbox style đẹp hơn default.

**Gợi ý:**
- Hide input: `display: none`
- Style label như checkbox
- Dùng `:checked` selector

---

## 📘 BÀI TRUNG BÌNH (14 bài)

### Bài 54: Flexbox navigation ⭐⭐
**Đề bài:** Tạo navbar với flexbox:
- Logo bên trái
- Menu items ở giữa
- User actions bên phải
- Responsive: hamburger menu trên mobile

**Gợi ý:**
```css
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

@media (max-width: 768px) {
    /* Mobile styles */
}
```

---

### Bài 55: Grid gallery ⭐⭐
**Đề bài:** Tạo image gallery với CSS Grid:
- 4 columns trên desktop
- 2 columns trên tablet
- 1 column trên mobile
- Gap 20px
- Các ảnh có size khác nhau

**Gợi ý:**
```css
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```

---

### Bài 56: Card grid layout ⭐⭐
**Đề bài:** Tạo grid 3 columns cho cards, responsive. Card có: image, title, description, button.

**Gợi ý:**
- Grid container
- Card với flexbox (column direction)
- Auto-fit minmax cho responsive

---

### Bài 57: Sidebar layout ⭐⭐
**Đề bài:** Tạo layout với sidebar cố định bên trái (250px) và main content fill phần còn lại.

**Gợi ý:**
```css
.container {
    display: grid;
    grid-template-columns: 250px 1fr;
}
```

---

### Bài 58: Pricing table ⭐⭐
**Đề bài:** Tạo 3 pricing cards với flexbox/grid:
- Basic, Pro, Enterprise
- Featured plan scale lớn hơn
- Hover effects
- Responsive

**Gợi ý:**
- Flexbox hoặc Grid
- `:nth-child(2)` cho featured
- Transform scale on hover

---

### Bài 59: Timeline vertical ⭐⭐
**Đề bài:** Tạo timeline dọc với các event, line giữa, dots và cards.

**Gợi ý:**
- Position relative cho container
- Pseudo-element `::before` cho line
- Alternate cards left/right

---

### Bài 60: Masonry layout ⭐⭐
**Đề bài:** Tạo masonry grid (như Pinterest) với CSS Grid.

**Gợi ý:**
```css
.masonry {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    grid-auto-rows: 10px;
}

.item {
    grid-row-end: span 20; /* Adjust based on height */
}
```

---

### Bài 61: Mega menu ⭐⭐
**Đề bài:** Tạo mega menu dropdown với grid layout, multiple columns.

**Gợi ý:**
- Position absolute cho dropdown
- Grid cho content
- Opacity và transform cho animation

---

### Bài 62: Modal với backdrop ⭐⭐
**Đề bài:** Style modal dialog với backdrop blur, center alignment, slide-in animation.

**Gợi ý:**
```css
.backdrop {
    backdrop-filter: blur(5px);
}

.modal {
    animation: slideIn 0.3s ease;
}

@keyframes slideIn {
    from { transform: translateY(-50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
```

---

### Bài 63: Parallax scrolling ⭐⭐
**Đề bài:** Tạo parallax effect cho background image khi scroll.

**Gợi ý:**
```css
.parallax {
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
```

---

### Bài 64: Animated hamburger menu ⭐⭐
**Đề bài:** Tạo hamburger icon (3 lines) animate thành X khi click.

**Gợi ý:**
- 3 divs cho 3 lines
- Transform rotate cho middle line
- TranslateY cho top/bottom lines

---

### Bài 65: Progress bar animated ⭐⭐
**Đề bài:** Tạo progress bar fill từ 0 đến value với animation khi load page.

**Gợi ý:**
```css
.progress-fill {
    width: 0;
    animation: fillBar 2s ease forwards;
}

@keyframes fillBar {
    to { width: 70%; }
}
```

---

### Bài 66: Image hover effects ⭐⭐
**Đề bài:** Tạo 4 loại hover effects khác nhau cho images:
1. Zoom in
2. Fade overlay
3. Slide caption
4. Rotate + scale

**Gợi ý:**
- Overflow hidden cho container
- Transform scale cho image
- Position absolute cho overlay/caption

---

### Bài 67: Responsive form layout ⭐⭐
**Đề bài:** Style form đẹp với:
- 2 columns trên desktop
- 1 column trên mobile
- Floating labels
- Focus effects
- Error states

**Gợi ý:**
- Grid cho layout
- Transitions cho labels
- `:invalid` pseudo-class

---

## 📕 BÀI KHÓ (3 bài)

### Bài 68: Dashboard layout hoàn chỉnh ⭐⭐⭐
**Đề bài:** Tạo dashboard admin layout với CSS Grid:
- Sidebar collapsible (250px → 60px)
- Top bar sticky
- Grid cho cards (4 columns)
- Responsive: sidebar overlay trên mobile
- Smooth transitions
- Dark mode toggle

**Gợi ý:**
- CSS Grid cho overall layout
- CSS Variables cho colors
- `@media (prefers-color-scheme: dark)`
- JavaScript toggle class

---

### Bài 69: Advanced animations ⭐⭐⭐
**Đề bài:** Tạo landing page animation:
- Hero text fade in + slide up
- Cards stagger animation (lần lượt hiện)
- Parallax sections
- Scroll-triggered animations
- Smooth scroll
- Loading screen animation

**Gợi ý:**
- CSS animations + keyframes
- `animation-delay` cho stagger
- IntersectionObserver API (JavaScript)
- CSS `scroll-behavior: smooth`

---

### Bài 70: Component library ⭐⭐⭐
**Đề bài:** Tạo mini component library với CSS:
- Buttons (5 variants: primary, secondary, success, danger, outline)
- Forms (inputs, selects, checkboxes, radios, switches)
- Cards (basic, image, horizontal)
- Alerts (success, warning, error, info)
- Badges
- Modals
- Tooltips
- Dropdowns
- Tabs
- Accordions

Tất cả components phải:
- Responsive
- Accessible (focus states, keyboard navigation)
- Consistent spacing system
- Dark mode support

**Gợi ý:**
- CSS Variables cho theming
- BEM naming convention
- Utility classes
- Comprehensive documentation

---

# PHẦN 3: ES6 (30 bài)

## 📗 BÀI DỄ (14 bài)

### Bài 71: Let và Const ⭐
**Đề bài:** Chuyển đổi code sau sang ES6 với let/const:
```javascript
var name = 'John';
var age = 30;
var PI = 3.14159;
```

**Gợi ý:**
- Dùng `const` cho values không thay đổi
- Dùng `let` cho values có thay đổi

---

### Bài 72: Arrow function cơ bản ⭐
**Đề bài:** Chuyển function sau sang arrow function:
```javascript
function add(a, b) {
    return a + b;
}

function square(x) {
    return x * x;
}
```

**Gợi ý:**
```javascript
const add = (a, b) => a + b;
const square = x => x * x;
```

---

### Bài 73: Template literals ⭐
**Đề bài:** Chuyển string concatenation sang template literals:
```javascript
var name = 'John';
var age = 30;
var message = 'Hello, ' + name + '. You are ' + age + ' years old.';
```

**Gợi ý:**
```javascript
const message = `Hello, ${name}. You are ${age} years old.`;
```

---

### Bài 74: Destructuring objects ⭐
**Đề bài:** Extract properties từ object với destructuring:
```javascript
const user = {
    name: 'John',
    age: 30,
    email: 'john@example.com'
};
// Extract name, age, email
```

**Gợi ý:**
```javascript
const { name, age, email } = user;
```

---

### Bài 75: Destructuring arrays ⭐
**Đề bài:** Extract elements từ array:
```javascript
const numbers = [1, 2, 3, 4, 5];
// Extract first, second, và rest
```

**Gợi ý:**
```javascript
const [first, second, ...rest] = numbers;
```

---

### Bài 76: Spread operator ⭐
**Đề bài:**
1. Merge 2 arrays
2. Copy array
3. Merge 2 objects

**Gợi ý:**
```javascript
const merged = [...arr1, ...arr2];
const copy = [...original];
const mergedObj = {...obj1, ...obj2};
```

---

### Bài 77: Default parameters ⭐
**Đề bài:** Viết function `greet(name, greeting)` với default greeting là "Hello".

**Gợi ý:**
```javascript
const greet = (name, greeting = 'Hello') => {
    return `${greeting}, ${name}!`;
};
```

---

### Bài 78: Enhanced object literals ⭐
**Đề bài:** Tạo object với shorthand properties và methods:
```javascript
const name = 'John';
const age = 30;

// Tạo object person
```

**Gợi ý:**
```javascript
const person = {
    name,
    age,
    greet() {
        console.log(`Hello, ${this.name}`);
    }
};
```

---

### Bài 79: Array methods ⭐
**Đề bài:** Cho array numbers = [1, 2, 3, 4, 5]:
1. Double mỗi số (map)
2. Lọc số chẵn (filter)
3. Tính tổng (reduce)

**Gợi ý:**
```javascript
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((total, n) => total + n, 0);
```

---

### Bài 80: Promise cơ bản ⭐
**Đề bài:** Tạo promise trả về "Success" sau 1 giây.

**Gợi ý:**
```javascript
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Success');
    }, 1000);
});

promise.then(result => console.log(result));
```

---

### Bài 81: For...of loop ⭐
**Đề bài:** Dùng for...of để iterate array và log mỗi element.

**Gợi ý:**
```javascript
const arr = [1, 2, 3];
for (const item of arr) {
    console.log(item);
}
```

---

### Bài 82: String methods ⭐
**Đề bài:** Dùng ES6 string methods:
1. `startsWith()`
2. `endsWith()`
3. `includes()`
4. `repeat()`

**Gợi ý:**
```javascript
const str = 'Hello World';
str.startsWith('Hello');  // true
str.endsWith('World');    // true
str.includes('lo');       // true
'Hi'.repeat(3);           // 'HiHiHi'
```

---

### Bài 83: Find và findIndex ⭐
**Đề bài:** Trong array users, tìm user có age > 25.

**Gợi ý:**
```javascript
const users = [
    {name: 'John', age: 30},
    {name: 'Jane', age: 20}
];

const user = users.find(u => u.age > 25);
const index = users.findIndex(u => u.age > 25);
```

---

### Bài 84: Object.entries, keys, values ⭐
**Đề bài:** Iterate object properties với Object.entries().

**Gợi ý:**
```javascript
const obj = {name: 'John', age: 30};

for (const [key, value] of Object.entries(obj)) {
    console.log(`${key}: ${value}`);
}
```

---

## 📘 BÀI TRUNG BÌNH (12 bài)

### Bài 85: Class cơ bản ⭐⭐
**Đề bài:** Tạo class `Person` với:
- Constructor: name, age
- Method: greet()
- Getter: info
- Setter: age (validate >= 0)

**Gợi ý:**
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this._age = age;
    }

    greet() {
        return `Hello, I'm ${this.name}`;
    }

    get info() {
        return `${this.name}, ${this._age}`;
    }

    set age(value) {
        if (value >= 0) {
            this._age = value;
        }
    }
}
```

---

### Bài 86: Class inheritance ⭐⭐
**Đề bài:** Tạo class `Student` extends `Person`:
- Thêm property: studentId, grades[]
- Override greet()
- Method: addGrade(grade)
- Method: getAverage()

**Gợi ý:**
- Dùng `super()`
- Override method

---

### Bài 87: Promise chaining ⭐⭐
**Đề bài:** Fetch user, sau đó fetch posts của user, sau đó fetch comments.

**Gợi ý:**
```javascript
fetchUser()
    .then(user => {
        console.log('User:', user);
        return fetchPosts(user.id);
    })
    .then(posts => {
        console.log('Posts:', posts);
        return fetchComments(posts[0].id);
    })
    .then(comments => {
        console.log('Comments:', comments);
    })
    .catch(error => console.error(error));
```

---

### Bài 88: Promise.all ⭐⭐
**Đề bài:** Fetch users, posts, comments đồng thời và chờ tất cả complete.

**Gợi ý:**
```javascript
Promise.all([
    fetchUsers(),
    fetchPosts(),
    fetchComments()
])
    .then(([users, posts, comments]) => {
        console.log({ users, posts, comments });
    });
```

---

### Bài 89: Async/Await cơ bản ⭐⭐
**Đề bài:** Chuyển promise chain thành async/await:
```javascript
function getData() {
    return fetchUser()
        .then(user => fetchPosts(user.id))
        .then(posts => console.log(posts));
}
```

**Gợi ý:**
```javascript
async function getData() {
    try {
        const user = await fetchUser();
        const posts = await fetchPosts(user.id);
        console.log(posts);
    } catch (error) {
        console.error(error);
    }
}
```

---

### Bài 90: Async/Await với Promise.all ⭐⭐
**Đề bài:** Fetch multiple resources đồng thời với async/await.

**Gợi ý:**
```javascript
async function getAllData() {
    try {
        const [users, posts, comments] = await Promise.all([
            fetchUsers(),
            fetchPosts(),
            fetchComments()
        ]);
        return { users, posts, comments };
    } catch (error) {
        console.error(error);
    }
}
```

---

### Bài 91: Array methods advanced ⭐⭐
**Đề bài:** Cho array products:
1. Tìm sản phẩm đắt nhất
2. Tính tổng giá trị
3. Group theo category
4. Sort theo giá

**Gợi ý:**
```javascript
const products = [
    {name: 'A', price: 100, category: 'electronics'},
    {name: 'B', price: 50, category: 'books'}
];

// Max price
const maxPrice = Math.max(...products.map(p => p.price));

// Total
const total = products.reduce((sum, p) => sum + p.price, 0);

// Group by category
const grouped = products.reduce((acc, p) => {
    acc[p.category] = acc[p.category] || [];
    acc[p.category].push(p);
    return acc;
}, {});

// Sort
const sorted = [...products].sort((a, b) => a.price - b.price);
```

---

### Bài 92: Modules ⭐⭐
**Đề bài:** Tạo module `math.js` export functions: add, subtract, multiply, divide. Import và dùng trong file khác.

**Gợi ý:**
```javascript
// math.js
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;

// main.js
import { add, subtract } from './math.js';
```

---

### Bài 93: Default và named exports ⭐⭐
**Đề bài:** Tạo module với default export và named exports.

**Gợi ý:**
```javascript
// user.js
export default class User { }
export const createUser = () => { };

// main.js
import User, { createUser } from './user.js';
```

---

### Bài 94: Fetch API ⭐⭐
**Đề bài:** Fetch data từ API, handle errors, hiển thị loading state.

**Gợi ý:**
```javascript
async function fetchData() {
    try {
        showLoader();
        const response = await fetch('/api/data');
        if (!response.ok) {
            throw new Error('Network error');
        }
        const data = await response.json();
        displayData(data);
    } catch (error) {
        showError(error);
    } finally {
        hideLoader();
    }
}
```

---

### Bài 95: CRUD với Fetch ⭐⭐
**Đề bài:** Implement CRUD operations với Fetch API:
- GET: Fetch all users
- POST: Create user
- PUT: Update user
- DELETE: Delete user

**Gợi ý:**
```javascript
const API_URL = '/api/users';

// GET
const getUsers = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

// POST
const createUser = async (user) => {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(user)
    });
    return response.json();
};

// PUT
const updateUser = async (id, user) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(user)
    });
    return response.json();
};

// DELETE
const deleteUser = async (id) => {
    await fetch(`${API_URL}/${id}`, {
        method: 'DELETE'
    });
};
```

---

### Bài 96: LocalStorage với ES6 ⭐⭐
**Đề bài:** Tạo utility functions cho localStorage:
- save(key, value)
- get(key)
- remove(key)
- clear()
Handle JSON stringify/parse tự động.

**Gợi ý:**
```javascript
const storage = {
    save(key, value) {
        localStorage.setItem(key, JSON.stringify(value));
    },
    get(key) {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : null;
    },
    remove(key) {
        localStorage.removeItem(key);
    },
    clear() {
        localStorage.clear();
    }
};
```

---

## 📕 BÀI KHÓ (4 bài)

### Bài 97: Todo App hoàn chỉnh ⭐⭐⭐
**Đề bài:** Tạo Todo App với ES6:
- Class TodoApp
- Add, edit, delete, toggle todos
- Filter: all, active, completed
- Save to localStorage
- Search functionality
- Drag & drop để reorder
- Undo/redo

**Gợi ý:**
```javascript
class TodoApp {
    constructor() {
        this.todos = this.loadTodos();
        this.filter = 'all';
        this.history = [];
    }

    addTodo(text) {
        const todo = {
            id: Date.now(),
            text,
            completed: false,
            createdAt: new Date()
        };
        this.todos.push(todo);
        this.save();
    }

    // ... other methods
}
```

---

### Bài 98: Shopping Cart với ES6 ⭐⭐⭐
**Đề bài:** Tạo Shopping Cart system:
- Class Product
- Class CartItem
- Class ShoppingCart với methods:
  - addItem(product, quantity)
  - removeItem(productId)
  - updateQuantity(productId, quantity)
  - getTotal()
  - applyDiscount(code)
  - checkout()
- Save cart to localStorage
- Apply coupon codes
- Calculate tax, shipping

**Gợi ý:**
```javascript
class Product {
    constructor(id, name, price, stock) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.stock = stock;
    }
}

class CartItem {
    constructor(product, quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    get subtotal() {
        return this.product.price * this.quantity;
    }
}

class ShoppingCart {
    constructor() {
        this.items = [];
        this.discountCode = null;
    }

    addItem(product, quantity) {
        const existingItem = this.items.find(
            item => item.product.id === product.id
        );

        if (existingItem) {
            existingItem.quantity += quantity;
        } else {
            this.items.push(new CartItem(product, quantity));
        }

        this.save();
    }

    getTotal() {
        const subtotal = this.items.reduce(
            (sum, item) => sum + item.subtotal,
            0
        );
        const discount = this.calculateDiscount(subtotal);
        const tax = (subtotal - discount) * 0.1;
        return subtotal - discount + tax;
    }

    // ... other methods
}
```

---

### Bài 99: API Service Layer ⭐⭐⭐
**Đề bài:** Tạo API service layer với:
- Base API class với common methods
- Error handling
- Request/response interceptors
- Retry logic
- Caching
- Rate limiting

Tạo specific services:
- UserService
- PostService
- CommentService

**Gợi ý:**
```javascript
class APIService {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.cache = new Map();
        this.requestQueue = [];
    }

    async request(url, options = {}) {
        const fullURL = `${this.baseURL}${url}`;

        // Check cache
        if (options.method === 'GET' && this.cache.has(fullURL)) {
            return this.cache.get(fullURL);
        }

        try {
            const response = await fetch(fullURL, {
                ...options,
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();

            // Cache GET requests
            if (options.method === 'GET') {
                this.cache.set(fullURL, data);
            }

            return data;
        } catch (error) {
            return this.handleError(error);
        }
    }

    async get(url) {
        return this.request(url);
    }

    async post(url, data) {
        return this.request(url, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    handleError(error) {
        console.error('API Error:', error);
        throw error;
    }
}

class UserService extends APIService {
    constructor() {
        super('/api');
    }

    getUsers() {
        return this.get('/users');
    }

    getUser(id) {
        return this.get(`/users/${id}`);
    }

    createUser(user) {
        return this.post('/users', user);
    }
}
```

---

### Bài 100: Mini Framework ⭐⭐⭐
**Đề bài:** Tạo mini reactive framework như Vue/React:
- Component class
- State management (reactive)
- Template rendering
- Event handling
- Lifecycle hooks
- Two-way data binding

**Gợi ý:**
```javascript
class Component {
    constructor(selector, options) {
        this.el = document.querySelector(selector);
        this.state = this.reactive(options.data());
        this.template = options.template;
        this.methods = options.methods || {};

        this.mount();
    }

    reactive(obj) {
        const self = this;
        return new Proxy(obj, {
            set(target, key, value) {
                target[key] = value;
                self.render();
                return true;
            }
        });
    }

    mount() {
        this.render();
        this.attachEvents();
    }

    render() {
        const html = this.template(this.state);
        this.el.innerHTML = html;
    }

    attachEvents() {
        this.el.addEventListener('click', (e) => {
            const method = e.target.dataset.method;
            if (method && this.methods[method]) {
                this.methods[method].call(this);
            }
        });
    }
}

// Usage
const app = new Component('#app', {
    data() {
        return {
            count: 0,
            message: 'Hello'
        };
    },
    template(state) {
        return `
            <div>
                <h1>${state.message}</h1>
                <p>Count: ${state.count}</p>
                <button data-method="increment">Increment</button>
            </div>
        `;
    },
    methods: {
        increment() {
            this.state.count++;
        }
    }
});
```

---

# HƯỚNG DẪN SỬ DỤNG

## Cách học hiệu quả

### 1. Làm theo thứ tự
- Bắt đầu từ bài dễ → trung bình → khó
- Đừng skip bài, mỗi bài xây dựng trên bài trước

### 2. Đọc đề kỹ
- Hiểu yêu cầu trước khi xem gợi ý
- Thử tự làm trước khi xem solution

### 3. Gợi ý
- Chỉ xem gợi ý khi thực sự stuck
- Hiểu tại sao solution hoạt động

### 4. Thực hành
- Viết code thật, không chỉ đọc
- Test code trong browser/Node.js
- Modify và experiment

### 5. Review
- Sau khi hoàn thành, review lại code
- Refactor để code tốt hơn
- Nghĩ cách optimize

## Tiêu chí đánh giá

### Bài dễ ⭐
- Hoàn thành trong 10-15 phút
- Syntax cơ bản
- Concepts đơn giản

### Bài trung bình ⭐⭐
- Hoàn thành trong 20-30 phút
- Kết hợp nhiều concepts
- Cần suy nghĩ logic

### Bài khó ⭐⭐⭐
- Hoàn thành trong 45-60 phút
- Complex logic
- Real-world application
- Best practices

## Checklist hoàn thành

### HTML5
- [ ] Hoàn thành 18/18 bài dễ
- [ ] Hoàn thành 14/14 bài trung bình
- [ ] Hoàn thành 3/3 bài khó

### CSS3
- [ ] Hoàn thành 18/18 bài dễ
- [ ] Hoàn thành 14/14 bài trung bình
- [ ] Hoàn thành 3/3 bài khó

### ES6
- [ ] Hoàn thành 14/14 bài dễ
- [ ] Hoàn thành 12/12 bài trung bình
- [ ] Hoàn thành 4/4 bài khó

## Mẹo học tập

1. **Consistency** - Làm ít nhất 3-5 bài mỗi ngày
2. **Practice** - Code thật, không chỉ đọc
3. **Debug** - Học cách debug khi gặp lỗi
4. **Document** - Viết notes cho concepts quan trọng
5. **Build** - Áp dụng vào project thực tế

## Tài nguyên hỗ trợ

- **MDN Web Docs** - Documentation chi tiết
- **Stack Overflow** - Q&A community
- **CodePen** - Test code online
- **GitHub** - Xem code người khác

---

**Chúc bạn học tốt! 🚀**

_Nếu gặp khó khăn với bài nào, hãy đọc lại tài liệu chương tương ứng hoặc tìm kiếm thêm resources online._
