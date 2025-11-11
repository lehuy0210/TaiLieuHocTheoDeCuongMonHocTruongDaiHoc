# CHƯƠNG 7: GRID LAYOUT

## 7.1. Giới thiệu CSS Grid

CSS Grid là layout system 2D mạnh mẽ nhất trong CSS.

### 7.1.1. Grid vs Flexbox

- **Flexbox:** 1D (row HOẶC column)
- **Grid:** 2D (row VÀ column đồng thời)

## 7.2. Grid Container

### 7.2.1. Enable Grid

```css
.container {
    display: grid;
}
```

### 7.2.2. grid-template-columns

```css
.container {
    display: grid;
    /* 3 columns với width cố định */
    grid-template-columns: 200px 200px 200px;

    /* Sử dụng fr (fraction) */
    grid-template-columns: 1fr 1fr 1fr;

    /* Mix units */
    grid-template-columns: 200px 1fr 2fr;

    /* repeat() */
    grid-template-columns: repeat(3, 1fr);

    /* auto-fill */
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));

    /* auto-fit */
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```

### 7.2.3. grid-template-rows

```css
.container {
    grid-template-rows: 100px 200px 100px;
    grid-template-rows: repeat(3, 100px);
}
```

### 7.2.4. gap

```css
.container {
    gap: 20px;
    /* or */
    row-gap: 20px;
    column-gap: 10px;
}
```

### 7.2.5. grid-template-areas

```css
.container {
    display: grid;
    grid-template-columns: 1fr 3fr 1fr;
    grid-template-rows: auto 1fr auto;
    grid-template-areas:
        "header header header"
        "sidebar main aside"
        "footer footer footer";
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.aside   { grid-area: aside; }
.footer  { grid-area: footer; }
```

## 7.3. Grid Items

### 7.3.1. grid-column

```css
.item {
    /* Span from line 1 to line 3 */
    grid-column: 1 / 3;

    /* Span 2 columns */
    grid-column: span 2;

    /* Shorthand */
    grid-column-start: 1;
    grid-column-end: 3;
}
```

### 7.3.2. grid-row

```css
.item {
    grid-row: 1 / 3;
    grid-row: span 2;
}
```

### 7.3.3. grid-area

```css
.item {
    /* row-start / col-start / row-end / col-end */
    grid-area: 1 / 1 / 3 / 3;
}
```

## 7.4. Alignment

### 7.4.1. justify-items (horizontal)

```css
.container {
    justify-items: stretch;  /* default */
    justify-items: start;
    justify-items: center;
    justify-items: end;
}
```

### 7.4.2. align-items (vertical)

```css
.container {
    align-items: stretch;  /* default */
    align-items: start;
    align-items: center;
    align-items: end;
}
```

### 7.4.3. justify-content (grid trong container)

```css
.container {
    justify-content: start;
    justify-content: center;
    justify-content: end;
    justify-content: space-between;
    justify-content: space-around;
    justify-content: space-evenly;
}
```

### 7.4.4. align-content

```css
.container {
    align-content: start;
    align-content: center;
    align-content: end;
    align-content: space-between;
}
```

### 7.4.5. Individual Item Alignment

```css
.item {
    justify-self: center;
    align-self: center;
}
```

## 7.5. Practical Examples

### 7.5.1. Basic Grid Layout

```html
<div class="grid">
    <div class="item">1</div>
    <div class="item">2</div>
    <div class="item">3</div>
    <div class="item">4</div>
</div>
```

```css
.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}
```

### 7.5.2. Responsive Grid

```css
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```

### 7.5.3. Holy Grail Layout

```css
.container {
    display: grid;
    grid-template-columns: 200px 1fr 200px;
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
    gap: 20px;
}

header {
    grid-column: 1 / -1;
}

footer {
    grid-column: 1 / -1;
}
```

### 7.5.4. Magazine Layout

```css
.gallery {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}

.item-1 {
    grid-column: span 2;
    grid-row: span 2;
}

.item-4 {
    grid-column: span 2;
}
```

### 7.5.5. Dashboard Layout

```css
.dashboard {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 20px;
}

.header {
    grid-column: 1 / -1;
}

.sidebar {
    grid-column: 1 / 3;
    grid-row: 2 / 4;
}

.main {
    grid-column: 3 / -1;
}
```

## 7.6. Advanced Features

### 7.6.1. Named Lines

```css
.container {
    grid-template-columns:
        [sidebar-start] 200px
        [sidebar-end main-start] 1fr
        [main-end];
}

.item {
    grid-column: sidebar-start / main-end;
}
```

### 7.6.2. Minmax()

```css
.container {
    grid-template-columns: repeat(3, minmax(200px, 1fr));
}
```

### 7.6.3. auto-fill vs auto-fit

```css
/* auto-fill: keeps empty tracks */
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));

/* auto-fit: collapses empty tracks */
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
```

## 7.7. Grid vs Flexbox - Khi nào dùng gì?

**Dùng Flexbox khi:**
- Layout 1D (row hoặc column)
- Content-first design
- Small-scale layouts

**Dùng Grid khi:**
- Layout 2D (rows và columns)
- Layout-first design
- Large-scale layouts

**Kết hợp cả hai:**
```css
.page {
    display: grid;
    grid-template-columns: 200px 1fr;
}

.navbar {
    display: flex;
    justify-content: space-between;
}
```

---

**Kết luận:** CSS Grid là công cụ mạnh mẽ cho 2D layouts phức tạp. Kết hợp với Flexbox để tạo ra layouts linh hoạt và responsive.
