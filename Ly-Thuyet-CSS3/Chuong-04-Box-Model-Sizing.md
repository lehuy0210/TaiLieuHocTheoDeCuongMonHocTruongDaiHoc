# CHƯƠNG 4: BOX MODEL & SIZING

## 4.1. Box Model

### 4.1.1. Traditional Box Model

```css
.box {
    width: 300px;
    padding: 20px;
    border: 5px solid black;
    margin: 10px;
}
/* Total width = 300 + 20*2 + 5*2 + 10*2 = 370px */
```

### 4.1.2. box-sizing: border-box

```css
/* Modern approach */
*, *::before, *::after {
    box-sizing: border-box;
}

.box {
    box-sizing: border-box;
    width: 300px;  /* Total width including padding and border */
    padding: 20px;
    border: 5px solid black;
}
/* Total width = 300px exactly */
```

## 4.2. Width và Height

### 4.2.1. Fixed Sizing

```css
.box {
    width: 300px;
    height: 200px;
}
```

### 4.2.2. min/max Width/Height

```css
.container {
    width: 100%;
    max-width: 1200px;  /* Never wider than 1200px */
    min-width: 320px;   /* Never narrower than 320px */
    margin: 0 auto;     /* Center */
}

.sidebar {
    min-height: 300px;  /* Minimum height */
    max-height: 600px;  /* Maximum height */
}
```

### 4.2.3. Percentage Sizing

```css
.container {
    width: 80%;
}

.half {
    width: 50%;
}
```

### 4.2.4. Viewport Units

```css
.hero {
    width: 100vw;   /* 100% viewport width */
    height: 100vh;  /* 100% viewport height */
}

.sidebar {
    width: 25vw;
    min-height: 50vh;
}

/* Font sizes with viewport units */
h1 {
    font-size: 5vw;  /* Responsive */
}
```

### 4.2.5. calc()

```css
.content {
    width: calc(100% - 300px);  /* Full width minus sidebar */
    padding: calc(1rem + 5px);
}

.grid {
    width: calc(100% / 3 - 20px);
}

/* Mix units */
.box {
    width: calc(100vw - 2rem);
    height: calc(50vh + 100px);
}
```

## 4.3. Padding

```css
/* All sides */
.box {
    padding: 20px;
}

/* Vertical | Horizontal */
.box {
    padding: 10px 20px;
}

/* Top | Horizontal | Bottom */
.box {
    padding: 10px 20px 15px;
}

/* Top | Right | Bottom | Left */
.box {
    padding: 10px 20px 15px 25px;
}

/* Individual sides */
.box {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 15px;
    padding-left: 25px;
}

/* Logical properties */
.box {
    padding-block: 20px;    /* Top and bottom */
    padding-inline: 10px;   /* Left and right */
}
```

## 4.4. Margin

```css
/* Same syntax as padding */
.box {
    margin: 20px;
    margin: 10px 20px;
    margin: 10px 20px 15px 25px;
}

/* Auto centering */
.centered {
    width: 600px;
    margin: 0 auto;  /* Horizontal center */
}

/* Negative margins */
.overlap {
    margin-top: -20px;
}

/* Margin collapse */
.box1 {
    margin-bottom: 20px;
}
.box2 {
    margin-top: 30px;
}
/* Gap between boxes is 30px (not 50px) */
```

## 4.5. Border

### 4.5.1. Basic Border

```css
.box {
    border: 2px solid black;

    /* Individual sides */
    border-top: 1px solid red;
    border-right: 2px dashed blue;
    border-bottom: 3px dotted green;
    border-left: 4px double yellow;
}

/* Border style */
.box {
    border-style: solid;
    border-style: dashed;
    border-style: dotted;
    border-style: double;
    border-style: groove;
    border-style: ridge;
    border-style: inset;
    border-style: outset;
}
```

### 4.5.2. border-radius

```css
/* All corners */
.box {
    border-radius: 10px;
}

/* Individual corners */
.box {
    border-radius: 10px 20px 30px 40px;
    /* top-left | top-right | bottom-right | bottom-left */
}

/* Specific corners */
.box {
    border-top-left-radius: 10px;
    border-top-right-radius: 20px;
    border-bottom-right-radius: 30px;
    border-bottom-left-radius: 40px;
}

/* Circle */
.circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

/* Pill shape */
.pill {
    border-radius: 9999px;
}

/* Elliptical corners */
.box {
    border-radius: 50px / 25px;  /* horizontal / vertical */
}
```

### 4.5.3. border-image

```css
.box {
    border: 10px solid;
    border-image: url('border.png') 30 round;
}

.gradient-border {
    border: 5px solid;
    border-image: linear-gradient(45deg, red, blue) 1;
}
```

## 4.6. Outline

```css
.box {
    outline: 2px solid blue;
    outline-offset: 5px;  /* Space between border and outline */
}

/* Focus outline */
button:focus {
    outline: 3px solid blue;
    outline-offset: 2px;
}

/* Remove outline (provide alternative!) */
button {
    outline: none;  /* Bad without alternative focus style */
}

button:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.5);  /* Alternative */
}
```

## 4.7. Box Shadow

```css
.box {
    /* x-offset | y-offset | blur | spread | color */
    box-shadow: 2px 2px 10px 0px rgba(0, 0, 0, 0.3);
}

/* Multiple shadows */
.box {
    box-shadow:
        0 2px 4px rgba(0, 0, 0, 0.1),
        0 4px 8px rgba(0, 0, 0, 0.1),
        0 8px 16px rgba(0, 0, 0, 0.1);
}

/* Inset shadow */
.inset {
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Elevation effect */
.card {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s;
}

.card:hover {
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

/* No shadow */
.flat {
    box-shadow: none;
}
```

## 4.8. Overflow

```css
.box {
    overflow: visible;  /* Default */
    overflow: hidden;   /* Clip content */
    overflow: scroll;   /* Always show scrollbars */
    overflow: auto;     /* Show scrollbars if needed */
}

/* Individual axes */
.box {
    overflow-x: hidden;
    overflow-y: auto;
}

/* Text ellipsis */
.truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Line clamp */
.clamp {
    display: -webkit-box;
    -webkit-line-clamp: 3;  /* Number of lines */
    -webkit-box-orient: vertical;
    overflow: hidden;
}
```

## 4.9. Aspect Ratio

```css
.video-container {
    aspect-ratio: 16 / 9;
}

.square {
    aspect-ratio: 1 / 1;
}

/* Old technique (padding hack) */
.aspect-box {
    position: relative;
    padding-bottom: 56.25%;  /* 16:9 = 9/16 = 0.5625 */
}

.aspect-box > * {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
```

## 4.10. Object Fit

```css
img, video {
    width: 100%;
    height: 300px;

    object-fit: cover;     /* Fill, may crop */
    object-fit: contain;   /* Fit inside, may have gaps */
    object-fit: fill;      /* Stretch to fill */
    object-fit: none;      /* Original size */
    object-fit: scale-down; /* none or contain, whichever is smaller */
}

/* Object position */
img {
    object-fit: cover;
    object-position: top;      /* Crop from top */
    object-position: 50% 50%;  /* Center (default) */
}
```

## 4.11. Practical Examples

### 4.11.1. Card Component

```css
.card {
    box-sizing: border-box;
    width: 100%;
    max-width: 400px;
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin: 20px;
}
```

### 4.11.2. Responsive Container

```css
.container {
    box-sizing: border-box;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```

### 4.11.3. Avatar with Border

```css
.avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 3px solid white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    object-fit: cover;
}
```

---

**Kết luận:** Box model và sizing là nền tảng của CSS layout. Hiểu rõ box-sizing, padding, margin, và các đơn vị đo lường là essential.

**Chương tiếp theo:** Typography & Fonts
## 4.12. Practical Examples - Extended

### 4.12.1. E-commerce Product Grid

```html
<div class="product-grid">
    <div class="product-item">
        <div class="product-image"></div>
        <h3>Product Name</h3>
        <p class="price">$99.99</p>
    </div>
</div>
```

```css
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 20px;
}

.product-item {
    box-sizing: border-box;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 15px;
    transition: all 0.3s ease;
}

.product-item:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    transform: translateY(-5px);
}

.product-image {
    aspect-ratio: 1 / 1;
    background: #f5f5f5;
    border-radius: 4px;
    margin-bottom: 15px;
}
```

### 4.12.2. Notification Card System

```css
.notification {
    box-sizing: border-box;
    max-width: 400px;
    padding: 16px 20px;
    margin-bottom: 12px;
    border-radius: 8px;
    border-left: 4px solid;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.notification-success {
    border-left-color: #2ecc71;
    background: #eafaf1;
}

.notification-error {
    border-left-color: #e74c3c;
    background: #fadbd8;
}

.notification-warning {
    border-left-color: #f39c12;
    background: #fef5e7;
}

.notification-info {
    border-left-color: #3498db;
    background: #ebf5fb;
}
```

### 4.12.3. Pricing Table

```css
.pricing-table {
    display: flex;
    gap: 30px;
    padding: 40px 20px;
}

.pricing-card {
    box-sizing: border-box;
    flex: 1;
    padding: 40px 30px;
    border: 2px solid #e0e0e0;
    border-radius: 12px;
    text-align: center;
    transition: all 0.3s ease;
}

.pricing-card.featured {
    border-color: #3498db;
    box-shadow: 0 10px 30px rgba(52, 152, 219, 0.2);
    transform: scale(1.05);
}

.pricing-card:hover {
    border-color: #3498db;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.price {
    font-size: 3rem;
    font-weight: bold;
    margin: 20px 0;
}
```

### 4.12.4. Modal Dialog

```css
.modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.modal {
    box-sizing: border-box;
    width: 100%;
    max-width: 600px;
    max-height: 90vh;
    overflow-y: auto;
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.modal-header {
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 1px solid #e0e0e0;
}

.modal-content {
    margin-bottom: 20px;
}

.modal-footer {
    padding-top: 15px;
    border-top: 1px solid #e0e0e0;
    text-align: right;
}
```

### 4.12.5. Timeline Component

```css
.timeline {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 0;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: #e0e0e0;
    transform: translateX(-50%);
}

.timeline-item {
    position: relative;
    width: calc(50% - 30px);
    padding: 20px;
    box-sizing: border-box;
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 40px;
}

.timeline-item:nth-child(odd) {
    margin-left: 0;
    margin-right: auto;
}

.timeline-item:nth-child(even) {
    margin-left: auto;
    margin-right: 0;
}
```

### 4.12.6. Form Layout

```css
.form-group {
    margin-bottom: 20px;
}

.form-control {
    box-sizing: border-box;
    width: 100%;
    padding: 12px 16px;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-control:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.form-control:invalid {
    border-color: #e74c3c;
}

.form-control:invalid:focus {
    box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.1);
}
```

### 4.12.7. Dashboard Layout

```css
.dashboard {
    box-sizing: border-box;
    min-height: 100vh;
    padding: 20px;
    display: grid;
    grid-template-columns: 250px 1fr;
    grid-template-rows: auto 1fr;
    gap: 20px;
}

.dashboard-header {
    grid-column: 1 / -1;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.dashboard-sidebar {
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.dashboard-content {
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

## 4.13. Real-World Use Cases

### 4.13.1. Responsive Container System

```css
/* Base container */
.container {
    box-sizing: border-box;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Container variants */
.container-fluid {
    width: 100%;
    padding: 0 20px;
}

.container-narrow {
    max-width: 800px;
}

.container-wide {
    max-width: 1400px;
}

/* Responsive breakpoints */
@media (max-width: 768px) {
    .container {
        padding: 0 15px;
    }
}
```

### 4.13.2. Card Layout System

```css
.card {
    box-sizing: border-box;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card-header {
    padding: 20px;
    border-bottom: 1px solid #e0e0e0;
}

.card-body {
    padding: 20px;
}

.card-footer {
    padding: 20px;
    border-top: 1px solid #e0e0e0;
    background: #f8f9fa;
}

/* Card sizes */
.card-sm {
    max-width: 300px;
}

.card-md {
    max-width: 500px;
}

.card-lg {
    max-width: 800px;
}
```

### 4.13.3. Sticky Sidebar Navigation

```css
.layout {
    display: flex;
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.sidebar {
    box-sizing: border-box;
    width: 250px;
    flex-shrink: 0;
}

.sidebar-sticky {
    position: sticky;
    top: 20px;
    max-height: calc(100vh - 40px);
    overflow-y: auto;
    padding: 20px;
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
}

.content {
    flex: 1;
    min-width: 0; /* Prevents overflow */
}
```

### 4.13.4. Masonry Grid

```css
.masonry {
    column-count: 3;
    column-gap: 20px;
    padding: 20px;
}

.masonry-item {
    box-sizing: border-box;
    break-inside: avoid;
    margin-bottom: 20px;
    padding: 15px;
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
}

@media (max-width: 992px) {
    .masonry {
        column-count: 2;
    }
}

@media (max-width: 576px) {
    .masonry {
        column-count: 1;
    }
}
```

### 4.13.5. Image Gallery with Captions

```css
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 15px;
    padding: 20px;
}

.gallery-item {
    position: relative;
    aspect-ratio: 1 / 1;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.gallery-item:hover img {
    transform: scale(1.1);
}

.gallery-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 15px;
    background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
    color: white;
    transform: translateY(100%);
    transition: transform 0.3s ease;
}

.gallery-item:hover .gallery-caption {
    transform: translateY(0);
}
```

## 4.14. Tips & Tricks

### Tip 1: Always Use box-sizing: border-box

```css
/* Global reset */
*, *::before, *::after {
    box-sizing: border-box;
}

/* Now widths include padding and border */
.box {
    width: 300px; /* Total width is exactly 300px */
    padding: 20px;
    border: 5px solid black;
}
```

### Tip 2: Use min-width and max-width for Flexibility

```css
.responsive-box {
    width: 100%;
    min-width: 300px;
    max-width: 1200px;
    margin: 0 auto;
}
```

### Tip 3: Negative Margins for Overlapping

```css
.overlap-container {
    position: relative;
}

.overlap-item {
    margin-top: -50px; /* Overlaps with element above */
    position: relative;
    z-index: 1;
}
```

### Tip 4: Use calc() for Precise Sizing

```css
.sidebar-layout {
    width: calc(100% - 300px); /* Full width minus sidebar */
    padding: calc(1rem + 10px); /* Combine units */
}
```

### Tip 5: Aspect Ratio Boxes

```css
/* Old technique: padding hack */
.aspect-box-old {
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 ratio */
    position: relative;
}

/* Modern technique */
.aspect-box-new {
    aspect-ratio: 16 / 9;
}
```

### Tip 6: Center with Auto Margins

```css
.centered {
    width: 600px;
    margin-left: auto;
    margin-right: auto;
    /* Or shorthand */
    margin: 0 auto;
}
```

### Tip 7: Prevent Text Overflow

```css
.text-box {
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

### Tip 8: Full Height Containers

```css
.full-height {
    min-height: 100vh;
    /* Or with fallback */
    min-height: 100svh; /* Small viewport height */
    min-height: 100dvh; /* Dynamic viewport height */
}
```

### Tip 9: Circular Elements

```css
.circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}
```

### Tip 10: Smooth Outline for Accessibility

```css
.button:focus {
    outline: none; /* Remove default */
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.5); /* Custom focus */
}
```

## 4.15. Common Mistakes

### Mistake 1: Forgetting box-sizing

```css
/* Wrong: Total width = 340px */
.box {
    width: 300px;
    padding: 20px;
}

/* Correct: Total width = 300px */
.box {
    box-sizing: border-box;
    width: 300px;
    padding: 20px;
}
```

### Mistake 2: Using Height Instead of min-height

```css
/* Bad: Content overflow */
.box {
    height: 200px;
}

/* Good: Grows with content */
.box {
    min-height: 200px;
}
```

### Mistake 3: Margin Collapse Confusion

```css
/* These margins collapse to 30px, not 50px */
.box1 {
    margin-bottom: 20px;
}

.box2 {
    margin-top: 30px;
}

/* Fix: Use padding or flexbox/grid */
.container {
    display: flex;
    flex-direction: column;
    gap: 50px; /* No collapse! */
}
```

### Mistake 4: Percentage Height Without Parent Height

```css
/* Wrong: Parent has no height */
.parent {
    /* height not set */
}

.child {
    height: 100%; /* Doesn't work! */
}

/* Correct */
.parent {
    height: 500px;
}

.child {
    height: 100%; /* Now works */
}
```

### Mistake 5: Not Accounting for Border in Width

```css
/* Total width = 322px (300 + 2 + 20) */
.box {
    width: 300px;
    border: 1px solid;
    padding: 10px;
}

/* Fix with border-box */
.box {
    box-sizing: border-box;
    width: 300px; /* Includes border and padding */
}
```

### Mistake 6: Ignoring Overflow

```css
/* Content spills out */
.container {
    width: 300px;
    height: 200px;
}

/* Fix */
.container {
    width: 300px;
    height: 200px;
    overflow: auto; /* Add scrollbar if needed */
}
```

### Mistake 7: Using px for Everything

```css
/* Bad: Not flexible */
.box {
    width: 800px;
    padding: 20px;
}

/* Better: Responsive */
.box {
    width: 100%;
    max-width: 800px;
    padding: clamp(15px, 3vw, 30px);
}
```

### Mistake 8: Not Testing Empty States

```css
/* Collapses when empty */
.card {
    padding: 20px;
    border: 1px solid #ccc;
}

/* Fix: Set min-height */
.card {
    min-height: 150px;
    padding: 20px;
}
```

### Mistake 9: Outline vs Border Confusion

```css
/* Outline doesn't affect layout */
.box {
    outline: 5px solid red; /* Doesn't change box size */
}

/* Border does affect layout */
.box {
    border: 5px solid red; /* Increases box size */
}
```

### Mistake 10: Z-index Without Position

```css
/* Wrong: z-index doesn't work */
.box {
    z-index: 10; /* No effect! */
}

/* Correct */
.box {
    position: relative;
    z-index: 10;
}
```

## 4.16. Troubleshooting

### Problem 1: Element Not Centering

**Symptoms:** Element stays on left side

**Solutions:**
```css
/* Method 1: Auto margins */
.center-me {
    width: 600px;
    margin: 0 auto;
}

/* Method 2: Flexbox */
.parent {
    display: flex;
    justify-content: center;
}

/* Method 3: Grid */
.parent {
    display: grid;
    place-items: center;
}
```

### Problem 2: Unexpected Box Size

**Check 1: box-sizing**
```css
/* Add this globally */
*, *::before, *::after {
    box-sizing: border-box;
}
```

**Check 2: Margin collapse**
```css
/* Margins can collapse vertically */
.box1 { margin-bottom: 20px; }
.box2 { margin-top: 20px; }
/* Gap is 20px, not 40px */
```

### Problem 3: Overflow Hidden Not Working

```css
/* Need specific dimensions */
.container {
    width: 300px;
    height: 200px;
    overflow: hidden;
}

/* Or with max dimensions */
.container {
    max-width: 300px;
    max-height: 200px;
    overflow: hidden;
}
```

### Problem 4: Box Shadow Cut Off

```css
/* Problem: Overflow clips shadow */
.parent {
    overflow: hidden;
}

.child {
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

/* Solution: Add padding to parent */
.parent {
    overflow: hidden;
    padding: 20px;
}
```

### Problem 5: Width 100% Causing Horizontal Scroll

```css
/* Problem */
.box {
    width: 100%;
    padding: 20px;
    border: 2px solid;
}

/* Solution */
.box {
    box-sizing: border-box;
    width: 100%;
    padding: 20px;
    border: 2px solid;
}
```

### Problem 6: Margin Not Working on Inline Elements

```css
/* Margins only work left/right on inline elements */
span {
    margin: 20px; /* top/bottom ignored */
}

/* Solution */
span {
    display: inline-block;
    margin: 20px; /* All margins work */
}
```

### Problem 7: Negative Margins Causing Overlap

```css
/* Elements overlap unexpectedly */
.box {
    margin-top: -20px;
}

/* Fix with z-index */
.box {
    margin-top: -20px;
    position: relative;
    z-index: 1;
}
```

### Problem 8: calc() Not Working

```css
/* Wrong: Missing spaces around operator */
.box {
    width: calc(100%-300px);
}

/* Correct: Spaces required */
.box {
    width: calc(100% - 300px);
}
```

### Problem 9: Object-fit Not Working

```css
/* Need specific dimensions */
img {
    width: 100%;
    height: 300px;
    object-fit: cover; /* Now works */
}
```

### Problem 10: Scrollbar Causing Layout Shift

```css
/* Problem: Scrollbar appears and shifts content */
body {
    overflow-y: scroll; /* Always show scrollbar */
}

/* Or reserve space */
html {
    scrollbar-gutter: stable;
}
```

## 4.17. Advanced Topics

### Advanced 1: Logical Properties

```css
/* Instead of physical properties */
.box-old {
    margin-top: 10px;
    margin-left: 20px;
    border-left: 2px solid;
}

/* Use logical properties (RTL-friendly) */
.box-new {
    margin-block-start: 10px;
    margin-inline-start: 20px;
    border-inline-start: 2px solid;
}
```

### Advanced 2: Container Query Units

```css
.card {
    container-type: inline-size;
}

.card-title {
    /* Relative to container, not viewport */
    font-size: 5cqi; /* Container query inline */
    padding: 2cqw; /* Container query width */
}
```

### Advanced 3: Intrinsic Sizing Keywords

```css
.box {
    width: min-content; /* Smallest width that fits content */
    width: max-content; /* Largest width content needs */
    width: fit-content; /* Between min and max */
    width: fit-content(500px); /* With max */
}
```

### Advanced 4: Subgrid for Complex Layouts

```css
.grid-parent {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.grid-child {
    display: grid;
    grid-template-columns: subgrid; /* Inherits parent grid */
    grid-column: span 3;
}
```

### Advanced 5: CSS Containment

```css
.contained {
    contain: layout size paint; /* Optimize rendering */
}

.isolated {
    contain: layout style paint; /* Complete isolation */
}
```

### Advanced 6: Writing Mode and Box Model

```css
.vertical-text {
    writing-mode: vertical-rl;
    /* width becomes height in vertical mode */
    inline-size: 200px; /* width in horizontal, height in vertical */
    block-size: 100%; /* height in horizontal, width in vertical */
}
```

### Advanced 7: Margin Trim

```css
.container {
    margin-trim: block; /* Trim margins of first/last children */
}

.child:first-child {
    margin-top: 20px; /* Trimmed */
}
```

### Advanced 8: Box Decoration Break

```css
.inline-box {
    display: inline;
    padding: 10px;
    background: #3498db;
    box-decoration-break: clone; /* Each line is independent box */
}
```

### Advanced 9: Scroll Padding

```css
html {
    scroll-padding-top: 80px; /* Offset for fixed header */
}

/* When anchor links are clicked, scrolls to element with offset */
```

### Advanced 10: CSS Shapes for Text Wrapping

```css
.float-shape {
    float: left;
    width: 200px;
    height: 200px;
    shape-outside: circle(50%);
    clip-path: circle(50%);
}
```

## 4.18. Bài Tập

### Bài Tập 1: Responsive Card Grid
Tạo responsive card grid với các yêu cầu:
- 4 columns trên desktop (>1200px)
- 3 columns trên tablet (768px-1199px)
- 2 columns trên mobile landscape (576px-767px)
- 1 column trên mobile portrait (<576px)
- Gap 20px giữa các cards
- Mỗi card có aspect ratio 3:4

### Bài Tập 2: Holy Grail Layout
Tạo classic Holy Grail layout với:
- Fixed header (60px height)
- Fixed footer (80px height)
- Left sidebar (250px width)
- Right sidebar (200px width)
- Flexible center content
- Full viewport height

### Bài Tập 3: Masonry Grid
Tạo Pinterest-style masonry grid:
- 4 columns
- Variable height items
- 15px gap
- Smooth transitions
- Responsive (giảm columns trên mobile)

### Bài Tập 4: Modal Dialog
Tạo modal dialog với:
- Centered on viewport
- Max-width 600px
- Padding 30px
- Backdrop blur effect
- Close button (top-right corner)
- Smooth open/close animation

### Bài Tập 5: Sticky Sidebar
Tạo layout với sticky sidebar:
- Sidebar width 300px
- Content area flexible
- Sidebar sticks when scrolling
- Gap 30px
- Works với short và long content

### Bài Tập 6: Pricing Table
Tạo pricing table với 3 tiers:
- Equal width cards
- Featured card highlighted (scaled up 5%)
- Smooth hover effects
- Box shadows
- Responsive stack trên mobile

### Bài Tập 7: Image Gallery
Tạo image gallery với:
- Grid layout
- Aspect ratio boxes
- Overlay captions on hover
- Lightbox effect (scale up)
- Border radius và shadows

### Bài Tập 8: Form Layout
Tạo form với:
- Proper spacing (margin-bottom)
- Full width inputs
- Focus states (outline glow)
- Error states (red border)
- Submit button (full width trên mobile)

### Bài Tập 9: Dashboard Layout
Tạo dashboard với:
- Top navbar
- Left sidebar
- Main content area với widgets
- Widget cards với shadows
- Responsive (sidebar collapse trên mobile)

### Bài Tập 10: Hero Section
Tạo hero section với:
- Full viewport height
- Background image với overlay
- Centered content
- Call-to-action button
- Responsive text sizing

### Bài Tập 11: Timeline Component
Tạo vertical timeline:
- Center line
- Alternating left/right items
- Circle markers on line
- Cards với shadows
- Responsive (single column trên mobile)

### Bài Tập 12: Complex Card Layout
Tạo card với multiple sections:
- Image header (aspect ratio 16:9)
- Content section với padding
- Stats section (horizontal layout)
- Action buttons footer
- Hover effects (lift up)
- Max-width 400px

---

**Kết luận:** Box model và sizing là nền tảng của CSS layout. Master box-sizing, understand margin collapse, và sử dụng modern properties như aspect-ratio và logical properties để tạo layouts mạnh mẽ và maintainable.

**Chương tiếp theo:** Typography & Fonts
