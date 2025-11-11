# CHƯƠNG 12: ADVANCED CSS3 TOPICS

## 12.1. CSS Variables (Custom Properties)

### 12.1.1. Defining Variables

```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2ecc71;
    --spacing: 20px;
    --font-size: 16px;
}

.component {
    --local-bg: #f0f0f0;
}
```

### 12.1.2. Using Variables

```css
.button {
    background-color: var(--primary-color);
    padding: var(--spacing);
    font-size: var(--font-size);
}

/* With fallback */
.box {
    color: var(--text-color, #333);
}
```

### 12.1.3. Dynamic Theming

```css
:root {
    --bg-color: white;
    --text-color: black;
}

[data-theme="dark"] {
    --bg-color: #1a1a1a;
    --text-color: white;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    transition: background-color 0.3s, color 0.3s;
}
```

### 12.1.4. JavaScript Integration

```javascript
// Get variable
const root = document.documentElement;
const primaryColor = getComputedStyle(root).getPropertyValue('--primary-color');

// Set variable
root.style.setProperty('--primary-color', '#e74c3c');
```

## 12.2. CSS Functions

### 12.2.1. calc()

```css
.box {
    width: calc(100% - 50px);
    height: calc(100vh - 100px);
    padding: calc(var(--spacing) * 2);
    font-size: calc(1rem + 0.5vw);
}
```

### 12.2.2. min(), max(), clamp()

```css
/* min: smallest value */
.box {
    width: min(100%, 800px);  /* Never wider than 800px */
}

/* max: largest value */
.box {
    width: max(50%, 300px);  /* Never narrower than 300px */
}

/* clamp: between min and max */
.box {
    font-size: clamp(16px, 2vw, 24px);  /* min, preferred, max */
    width: clamp(300px, 50%, 800px);
}
```

### 12.2.3. Color Functions

```css
.box {
    /* RGB */
    color: rgb(255, 0, 0);
    color: rgba(255, 0, 0, 0.5);

    /* HSL */
    background: hsl(200, 50%, 50%);
    background: hsla(200, 50%, 50%, 0.8);

    /* HWB (newer) */
    color: hwb(120 20% 30%);
}
```

## 12.3. CSS Filters

```css
.image {
    /* Blur */
    filter: blur(5px);

    /* Brightness */
    filter: brightness(1.5);  /* 150% */
    filter: brightness(0.5);  /* 50% */

    /* Contrast */
    filter: contrast(200%);

    /* Grayscale */
    filter: grayscale(100%);
    filter: grayscale(0.5);  /* 50% */

    /* Sepia */
    filter: sepia(100%);

    /* Hue rotate */
    filter: hue-rotate(90deg);

    /* Invert */
    filter: invert(100%);

    /* Saturate */
    filter: saturate(200%);

    /* Opacity */
    filter: opacity(50%);

    /* Drop shadow */
    filter: drop-shadow(2px 2px 5px rgba(0, 0, 0, 0.5));

    /* Combine multiple */
    filter: blur(2px) brightness(1.2) contrast(1.1);
}

/* Backdrop filter (blur background) */
.modal {
    backdrop-filter: blur(10px);
    background: rgba(255, 255, 255, 0.8);
}
```

## 12.4. Blend Modes

```css
.blend {
    /* Mix blend mode */
    mix-blend-mode: multiply;
    mix-blend-mode: screen;
    mix-blend-mode: overlay;
    mix-blend-mode: darken;
    mix-blend-mode: lighten;
    mix-blend-mode: color-dodge;
    mix-blend-mode: color-burn;
    mix-blend-mode: difference;
    mix-blend-mode: exclusion;
    mix-blend-mode: hue;
    mix-blend-mode: saturation;
    mix-blend-mode: color;
    mix-blend-mode: luminosity;
}

/* Background blend mode */
.box {
    background-image: url('image.jpg'), linear-gradient(blue, red);
    background-blend-mode: multiply;
}
```

## 12.5. Clip Path

```css
.shape {
    /* Circle */
    clip-path: circle(50%);
    clip-path: circle(100px at center);

    /* Ellipse */
    clip-path: ellipse(100px 50px at center);

    /* Polygon */
    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);

    /* Triangle */
    clip-path: polygon(50% 0%, 0% 100%, 100% 100%);

    /* Hexagon */
    clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);

    /* Path (SVG) */
    clip-path: url(#my-clip-path);
}
```

## 12.6. Scroll Snap

```css
.scroll-container {
    scroll-snap-type: x mandatory;
    overflow-x: scroll;
    display: flex;
}

.scroll-item {
    scroll-snap-align: start;
    scroll-snap-stop: always;
    flex: 0 0 100%;
}

/* Y-axis snap */
.vertical-scroll {
    scroll-snap-type: y proximity;
    overflow-y: scroll;
}
```

## 12.7. CSS Grid Advanced

### 12.7.1. Named Grid Lines

```css
.grid {
    display: grid;
    grid-template-columns: [sidebar-start] 200px [sidebar-end content-start] 1fr [content-end];
    grid-template-rows: [header-start] 100px [header-end main-start] 1fr [main-end];
}

.sidebar {
    grid-column: sidebar-start / sidebar-end;
}
```

### 12.7.2. Grid Template Areas

```css
.layout {
    display: grid;
    grid-template-areas:
        "header header header"
        "sidebar content content"
        "footer footer footer";
    grid-template-columns: 200px 1fr 1fr;
    grid-template-rows: auto 1fr auto;
    gap: 20px;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.content { grid-area: content; }
.footer { grid-area: footer; }
```

### 12.7.3. Auto-fill vs Auto-fit

```css
/* Auto-fill: Creates as many tracks as fit */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}

/* Auto-fit: Collapses empty tracks */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```

## 12.8. CSS Shapes

```css
.float-shape {
    float: left;
    shape-outside: circle(50%);
    clip-path: circle(50%);
}

.polygon-shape {
    shape-outside: polygon(0 0, 100% 0, 100% 100%);
}

.image-shape {
    shape-outside: url('shape.png');
    shape-image-threshold: 0.5;
}
```

## 12.9. Writing Modes

```css
.vertical {
    writing-mode: vertical-rl;  /* Vertical, right to left */
    writing-mode: vertical-lr;  /* Vertical, left to right */
}

.horizontal {
    writing-mode: horizontal-tb;  /* Default */
}

/* Logical properties */
.box {
    margin-block-start: 20px;   /* Top in LTR, bottom in RTL */
    margin-block-end: 20px;     /* Bottom in LTR, top in RTL */
    margin-inline-start: 10px;  /* Left in LTR, right in RTL */
    margin-inline-end: 10px;    /* Right in LTR, left in RTL */
}
```

## 12.10. Object Fit & Position

```css
img, video {
    width: 100%;
    height: 400px;

    object-fit: cover;     /* Fill, crop if needed */
    object-fit: contain;   /* Fit inside, maintain aspect */
    object-fit: fill;      /* Stretch */
    object-fit: none;      /* Original size */
    object-fit: scale-down; /* none or contain */

    object-position: center;
    object-position: top right;
    object-position: 50% 50%;
}
```

## 12.11. CSS Counters

```css
body {
    counter-reset: section;
}

h2::before {
    counter-increment: section;
    content: "Section " counter(section) ": ";
}

/* Nested counters */
ol {
    counter-reset: item;
    list-style: none;
}

li::before {
    counter-increment: item;
    content: counters(item, ".") " ";
}
```

## 12.12. Feature Queries

```css
/* Check if browser supports Grid */
@supports (display: grid) {
    .layout {
        display: grid;
    }
}

/* Fallback for old browsers */
@supports not (display: grid) {
    .layout {
        display: flex;
    }
}

/* Multiple conditions */
@supports (display: grid) and (gap: 20px) {
    .grid {
        display: grid;
        gap: 20px;
    }
}

@supports (display: flex) or (display: grid) {
    .container {
        /* Modern layout */
    }
}
```

## 12.13. Scroll Behavior

```css
html {
    scroll-behavior: smooth;
}

.container {
    scroll-behavior: auto;
}
```

## 12.14. Content Visibility

```css
.section {
    content-visibility: auto;  /* Improve render performance */
}

.hidden {
    content-visibility: hidden;
}
```

## 12.15. Aspect Ratio

```css
.video-container {
    aspect-ratio: 16 / 9;
}

.square {
    aspect-ratio: 1;
}
```

## 12.16. Gap (for Flexbox)

```css
.flex-container {
    display: flex;
    gap: 20px;  /* Works in modern browsers */
    row-gap: 20px;
    column-gap: 10px;
}
```

## 12.17. Practical Example: Dark Mode

```css
:root {
    --bg: white;
    --text: #333;
    --border: #ddd;
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg: #1a1a1a;
        --text: #f0f0f0;
        --border: #444;
    }
}

/* Or with class toggle */
body {
    background: var(--bg);
    color: var(--text);
}

body.dark-mode {
    --bg: #1a1a1a;
    --text: #f0f0f0;
}
```

## 12.18. Modern CSS Reset

```css
*, *::before, *::after {
    box-sizing: border-box;
}

* {
    margin: 0;
    padding: 0;
}

body {
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
}

img, picture, video, canvas, svg {
    display: block;
    max-width: 100%;
}

input, button, textarea, select {
    font: inherit;
}

p, h1, h2, h3, h4, h5, h6 {
    overflow-wrap: break-word;
}
```

---

**Kết luận:** Modern CSS cực kỳ powerful với variables, functions, filters, và nhiều features khác. Luôn check browser support và provide fallbacks khi cần.

**Hoàn thành tất cả chương CSS3!**
