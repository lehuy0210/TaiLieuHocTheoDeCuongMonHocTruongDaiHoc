# CHƯƠNG 6: FLEXBOX

## 6.1. Giới thiệu Flexbox

Flexbox (Flexible Box Layout) là layout model giúp align và distribute space giữa các items trong container.

### 6.1.1. Khi nào dùng Flexbox

- Navigation menus
- Card layouts
- Centering elements
- Equal height columns
- Distributing space

## 6.2. Flex Container

### 6.2.1. Enable Flexbox

```css
.container {
    display: flex;
}

/* or */
.container {
    display: inline-flex;
}
```

### 6.2.2. flex-direction

```css
.container {
    flex-direction: row;            /* default */
    flex-direction: row-reverse;
    flex-direction: column;
    flex-direction: column-reverse;
}
```

### 6.2.3. flex-wrap

```css
.container {
    flex-wrap: nowrap;  /* default */
    flex-wrap: wrap;
    flex-wrap: wrap-reverse;
}
```

### 6.2.4. flex-flow (shorthand)

```css
.container {
    flex-flow: row wrap;
}
```

### 6.2.5. justify-content (Main Axis)

```css
.container {
    justify-content: flex-start;   /* default */
    justify-content: flex-end;
    justify-content: center;
    justify-content: space-between;
    justify-content: space-around;
    justify-content: space-evenly;
}
```

### 6.2.6. align-items (Cross Axis)

```css
.container {
    align-items: stretch;    /* default */
    align-items: flex-start;
    align-items: flex-end;
    align-items: center;
    align-items: baseline;
}
```

### 6.2.7. align-content

```css
.container {
    align-content: stretch;      /* default */
    align-content: flex-start;
    align-content: flex-end;
    align-content: center;
    align-content: space-between;
    align-content: space-around;
}
```

### 6.2.8. gap

```css
.container {
    gap: 20px;
    /* or */
    row-gap: 20px;
    column-gap: 10px;
}
```

## 6.3. Flex Items

### 6.3.1. order

```css
.item {
    order: 0;  /* default */
}

.item-1 { order: 1; }
.item-2 { order: 2; }
.item-3 { order: -1; } /* Appears first */
```

### 6.3.2. flex-grow

```css
.item {
    flex-grow: 0;  /* default */
}

.item-1 { flex-grow: 1; }  /* Takes 1 part */
.item-2 { flex-grow: 2; }  /* Takes 2 parts */
```

### 6.3.3. flex-shrink

```css
.item {
    flex-shrink: 1;  /* default */
}

.item-no-shrink {
    flex-shrink: 0;  /* Won't shrink */
}
```

### 6.3.4. flex-basis

```css
.item {
    flex-basis: auto;  /* default */
    flex-basis: 200px;
    flex-basis: 50%;
}
```

### 6.3.5. flex (shorthand)

```css
.item {
    flex: 1;  /* flex-grow: 1, flex-shrink: 1, flex-basis: 0% */
    flex: 0 1 auto;  /* default */
    flex: 2 1 200px;
}
```

### 6.3.6. align-self

```css
.item {
    align-self: auto;       /* default */
    align-self: flex-start;
    align-self: flex-end;
    align-self: center;
    align-self: baseline;
    align-self: stretch;
}
```

## 6.4. Practical Examples

### 6.4.1. Navbar

```html
<nav class="navbar">
    <div class="logo">Logo</div>
    <ul class="nav-items">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>
```

```css
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
}

.nav-items {
    display: flex;
    gap: 2rem;
    list-style: none;
}
```

### 6.4.2. Card Layout

```html
<div class="cards">
    <div class="card">Card 1</div>
    <div class="card">Card 2</div>
    <div class="card">Card 3</div>
</div>
```

```css
.cards {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.card {
    flex: 1 1 300px;  /* grow, shrink, base */
    min-height: 200px;
}
```

### 6.4.3. Perfect Centering

```css
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
```

### 6.4.4. Holy Grail Layout

```css
body {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

header, footer {
    flex-shrink: 0;
}

main {
    display: flex;
    flex: 1;
}

aside {
    flex: 0 0 200px;
}

article {
    flex: 1;
}
```

## 6.5. Responsive Flexbox

```css
.container {
    display: flex;
    flex-wrap: wrap;
}

.item {
    flex: 1 1 300px;
}

@media (max-width: 768px) {
    .container {
        flex-direction: column;
    }
}
```

---

**Kết luận:** Flexbox là công cụ mạnh mẽ cho 1D layouts (row hoặc column). Kết hợp với Grid cho layouts phức tạp hơn.
