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


## 7.10. Practical Examples - Extended

### 7.10.1. Responsive Magazine Layout

Complex grid with varying sizes

```css
.magazine {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 20px;
}

.hero-article {
    grid-column: 1 / 9;
    grid-row: 1 / 3;
}

.sidebar-article {
    grid-column: 9 / 13;
}
```

### 7.10.2. Image Gallery Masonry

Pinterest-style layout

```css
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-auto-rows: 10px;
    gap: 15px;
}

.gallery-item {
    grid-row-end: span 20; /* Adjust based on content */
}
```


## 7.11. Real-World Use Cases

### 7.11.1. Dashboard Analytics

Data widgets in grid

```css
/* Implementation details */
```

### 7.11.2. E-commerce Product Grid

Dynamic product listings

```css
/* Implementation details */
```

### 7.11.3. Calendar/Schedule

Time-based grid layout

```css
/* Implementation details */
```

### 7.11.4. Image Portfolio

Photography showcase

```css
/* Implementation details */
```

### 7.11.5. News Website

Article grid with featured posts

```css
/* Implementation details */
```


## 7.12. Tips & Tricks

### Tip 1: Performance Optimization
Use transform and opacity for smooth animations as they don't trigger layout recalculations.

```css
/* Good - GPU accelerated */
.box {
    transform: translateX(100px);
    opacity: 0.5;
}

/* Avoid - Causes reflow */
.box {
    left: 100px;
    margin-left: 50px;
}
```

### Tip 2: Mobile-First Development
Start with mobile styles and progressively enhance for larger screens.

```css
/* Mobile first */
.container {
    padding: 15px;
}

@media (min-width: 768px) {
    .container {
        padding: 30px;
    }
}
```

### Tip 3: Use CSS Variables for Theming
Create maintainable theme systems with CSS custom properties.

```css
:root {
    --primary: #3498db;
    --spacing-sm: 8px;
    --spacing-md: 16px;
}

.button {
    background: var(--primary);
    padding: var(--spacing-sm) var(--spacing-md);
}
```

### Tip 4: Leverage Browser DevTools
Use browser developer tools to inspect, debug, and optimize CSS in real-time.

### Tip 5: Comment Complex Selectors
Document your CSS for future maintenance and team collaboration.

```css
/* Primary navigation - sticky on scroll */
.navbar {
    position: sticky;
    top: 0;
    z-index: 100;
}
```

### Tip 6: Use Shorthand Properties
Write more concise CSS with shorthand properties.

```css
/* Instead of */
margin-top: 10px;
margin-right: 20px;
margin-bottom: 10px;
margin-left: 20px;

/* Use */
margin: 10px 20px;
```

### Tip 7: Avoid Over-Nesting
Keep specificity low for easier overrides and better performance.

```css
/* Bad */
.header .nav .menu .item .link {}

/* Good */
.nav-link {}
```

### Tip 8: Test Across Browsers
Always test in multiple browsers including Chrome, Firefox, Safari, and Edge.

### Tip 9: Use Autoprefixer
Automate vendor prefix management with build tools.

### Tip 10: Optimize for Accessibility
Ensure sufficient color contrast, keyboard navigation, and screen reader support.

## 7.13. Common Mistakes

### Mistake 1: Not Using Reset/Normalize CSS
Different browsers have different default styles.

```css
/* Add at the start of your CSS */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

### Mistake 2: Ignoring Specificity
High specificity makes styles hard to override.

```css
/* Too specific */
div.container ul.list li.item a.link {}

/* Better */
.nav-link {}
```

### Mistake 3: Using !important
Avoid !important except for utility classes.

```css
/* Bad */
.text {
    color: red !important;
}

/* Good - use higher specificity or better cascade */
.article .text {
    color: red;
}
```

### Mistake 4: Forgetting Fallbacks
Always provide fallback values for modern features.

```css
.box {
    background: blue; /* Fallback */
    background: linear-gradient(to right, blue, purple);
}
```

### Mistake 5: Not Considering Browser Support
Check compatibility before using cutting-edge features.

```css
@supports (display: grid) {
    .layout { display: grid; }
}

@supports not (display: grid) {
    .layout { display: flex; }
}
```

### Mistake 6: Inline Styles Everywhere
Keep styling in CSS files for maintainability.

### Mistake 7: Not Optimizing Images
Use appropriate formats and sizes for images.

### Mistake 8: Forgetting Mobile Users
Mobile traffic often exceeds desktop.

### Mistake 9: Hardcoding Values
Use variables and relative units for flexibility.

### Mistake 10: Not Documenting Code
Add comments for complex logic and hacks.

## 7.14. Troubleshooting

### Problem 1: Styles Not Applying
**Check**: Specificity, load order, typos in class names

```css
/* Check inspector to see computed styles */
/* Verify selector matches element */
```

### Problem 2: Layout Breaking on Different Screens
**Solution**: Test at various breakpoints and use responsive units

```css
/* Use relative units */
.container {
    width: 90%;
    max-width: 1200px;
}
```

### Problem 3: Performance Issues
**Solution**: Minimize reflows, use will-change sparingly

```css
.animated-element {
    will-change: transform;
}

/* Remove after animation */
.animated-element:not(.animating) {
    will-change: auto;
}
```

### Problem 4: Z-index Not Working
**Solution**: Element needs position property

```css
.modal {
    position: fixed;
    z-index: 1000;
}
```

### Problem 5: Flexbox/Grid Gaps Not Working
**Solution**: Check browser support, use margin as fallback

```css
.flex-container {
    display: flex;
    gap: 20px;
}

/* Fallback */
@supports not (gap: 20px) {
    .flex-container > * {
        margin-right: 20px;
    }
}
```

### Problem 6: Colors Look Different Across Browsers
**Solution**: Use consistent color spaces and test extensively

### Problem 7: Font Not Loading
**Check**: File path, CORS headers, font format support

```css
@font-face {
    font-family: 'CustomFont';
    src: url('font.woff2') format('woff2'),
         url('font.woff') format('woff'); /* Fallback */
}
```

### Problem 8: Animations Janky
**Solution**: Use transform and opacity, avoid animating layout properties

### Problem 9: CSS Not Updating
**Clear**: Browser cache, check file path, verify server is running

### Problem 10: Hover Not Working on Touch
**Solution**: Add :active state for touch devices

```css
@media (hover: none) {
    .button:active {
        /* Touch device styling */
    }
}
```

## 7.15. Advanced Topics

### Advanced 1: CSS Architecture (BEM, SMACSS)
Organize large-scale CSS projects with methodology.

```css
/* BEM (Block Element Modifier) */
.card {}
.card__header {}
.card__body {}
.card--featured {}
```

### Advanced 2: CSS-in-JS
Explore styled-components, emotion, and other solutions.

### Advanced 3: Custom Properties Manipulation
Use calc() and var() for dynamic theming.

```css
:root {
    --base-size: 16px;
    --scale: 1.5;
}

h1 {
    font-size: calc(var(--base-size) * var(--scale) * var(--scale));
}
```

### Advanced 4: CSS Containment
Optimize rendering with contain property.

```css
.independent-widget {
    contain: layout style paint;
}
```

### Advanced 5: Scroll-Linked Animations
Create scroll-based animations with scroll-timeline (future).

### Advanced 6: Subgrid
Create complex grid alignments.

```css
.parent {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

.child {
    display: grid;
    grid-template-columns: subgrid;
}
```

### Advanced 7: CSS Layers (@layer)
Manage cascade with explicit layers.

```css
@layer reset, base, components, utilities;

@layer reset {
    * { margin: 0; padding: 0; }
}
```

### Advanced 8: View Transitions API
Smooth page transitions.

```css
::view-transition-old(root),
::view-transition-new(root) {
    animation-duration: 0.3s;
}
```

### Advanced 9: Scroll Snap
Create carousel-like experiences.

```css
.scroller {
    scroll-snap-type: x mandatory;
}

.scroller > * {
    scroll-snap-align: start;
}
```

### Advanced 10: CSS Math Functions
Use min(), max(), clamp() for responsive design.

```css
.fluid {
    width: clamp(300px, 50vw, 800px);
    padding: min(5vw, 40px);
}
```

## 7.16. Bài Tập

### Bài Tập 1: Basic Implementation
Implement the core concepts from this chapter in a simple project.

**Requirements:**
- Use semantic HTML
- Apply responsive design
- Test in multiple browsers
- Validate CSS

### Bài Tập 2: Responsive Component
Create a fully responsive component that works on all screen sizes.

**Requirements:**
- Mobile-first approach
- Smooth transitions
- Accessible markup
- Cross-browser compatible

### Bài Tập 3: Animation Challenge
Build an engaging animated UI element.

**Requirements:**
- Smooth 60fps animations
- Fallbacks for reduced motion
- Optimized performance
- Creative and delightful

### Bài Tập 4: Layout Exercise
Construct a complex layout using concepts from this chapter.

**Requirements:**
- Semantic structure
- Flexible and responsive
- No layout breaks
- Clean code

### Bài Tập 5: Theming System
Implement a complete theming system with light and dark modes.

**Requirements:**
- CSS variables
- Smooth transitions
- Persistent preference
- Accessible colors

### Bài Tập 6: Interactive Component
Build an interactive UI component (accordion, tabs, modal, etc).

**Requirements:**
- Keyboard accessible
- ARIA attributes
- Smooth animations
- Mobile-friendly

### Bài Tập 7: Performance Optimization
Take an existing project and optimize its CSS performance.

**Requirements:**
- Reduce file size
- Minimize reflows
- Optimize animations
- Measure improvements

### Bài Tập 8: Cross-Browser Testing
Test a component across all major browsers and fix issues.

**Requirements:**
- Test IE11, Chrome, Firefox, Safari, Edge
- Document issues
- Implement fixes
- Add fallbacks

### Bài Tập 9: Accessibility Audit
Review and improve accessibility of a CSS layout.

**Requirements:**
- Color contrast checks
- Keyboard navigation
- Screen reader testing
- WCAG compliance

### Bài Tập 10: Design System Component
Create a component for a design system.

**Requirements:**
- Reusable and flexible
- Well-documented
- Multiple variants
- Consistent with system

### Bài Tập 11: Advanced Feature
Implement an advanced CSS feature from this chapter.

**Requirements:**
- Modern syntax
- Progressive enhancement
- Fallback support
- Well-tested

### Bài Tập 12: Real-World Project
Build a complete section/page applying all concepts learned.

**Requirements:**
- Professional quality
- Production-ready
- Fully responsive
- Documented code

---

**Kết luận:** This chapter covered essential concepts for modern CSS development. Master these techniques to build beautiful, performant, and maintainable web interfaces.

**Chương tiếp theo:** Transitions


## 7.10. Advanced Grid Techniques

### 7.10.1. Dense Grid Packing
```css
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    grid-auto-flow: dense; /* Fill gaps */
    gap: 10px;
}

.gallery-item.large {
    grid-column: span 2;
    grid-row: span 2;
}
```

### 7.10.2. Asymmetric Grid Layouts
```css
.asymmetric {
    display: grid;
    grid-template-columns: 2fr 3fr 1fr;
    grid-template-rows: auto 1fr auto;
    gap: 20px;
    min-height: 100vh;
}
```

### 7.10.3. Overlapping Grid Items
```css
.overlap-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
}

.item-1 {
    grid-column: 1 / 2;
    grid-row: 1;
    z-index: 1;
}

.item-2 {
    grid-column: 1 / 3;
    grid-row: 1;
    z-index: 0;
}
```

### 7.10.4. Grid Item Spanning
```css
.span-container {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 20px;
}

.span-6 { grid-column: span 6; }
.span-4 { grid-column: span 4; }
.span-8 { grid-column: span 8; }

/* Specific placement */
.placed-item {
    grid-column: 3 / 9;
    grid-row: 2 / 4;
}
```

### 7.10.5. Named Grid Lines with Repeat
```css
.grid {
    display: grid;
    grid-template-columns: repeat(3, [col-start] 1fr [col-end]);
    grid-template-rows: repeat(4, [row-start] 100px [row-end]);
}

.item {
    grid-column: col-start 2 / col-end 3;
    grid-row: row-start 1 / row-end 2;
}
```

### 7.10.6. Grid with Flexible Track Sizes
```css
.flexible-grid {
    display: grid;
    grid-template-columns:
        minmax(min-content, 200px)  /* Sidebar */
        minmax(400px, 1fr)          /* Main content */
        minmax(200px, 300px);       /* Aside */
}
```

### 7.10.7. Subgrid for Nested Grids
```css
.parent-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 20px;
}

.nested-grid {
    grid-column: span 3;
    display: grid;
    grid-template-columns: subgrid; /* Inherits parent columns */
    gap: 10px;
}
```

### 7.10.8. Grid Auto-Placement Algorithm
```css
.auto-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-flow: row; /* Default */
    grid-auto-rows: 100px;
}

/* Column-based auto-flow */
.column-flow {
    grid-auto-flow: column;
    grid-auto-columns: 200px;
}
```

### 7.10.9. Masonry Layout Approximation
```css
.masonry-like {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    grid-auto-rows: 10px;
}

.masonry-item {
    /* Calculate span based on content height */
    grid-row-end: span 20;
}
```

### 7.10.10. Responsive Grid without Media Queries
```css
.responsive-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
    gap: 20px;
}
```

## 7.11. Grid Layout Patterns

### 7.11.1. Magazine Layout
```css
.magazine {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    grid-auto-rows: minmax(100px, auto);
    gap: 20px;
}

.hero { grid-column: 1 / 9; grid-row: 1 / 3; }
.featured { grid-column: 9 / 13; grid-row: 1 / 2; }
.sidebar { grid-column: 9 / 13; grid-row: 2 / 4; }
.article-1 { grid-column: 1 / 5; }
.article-2 { grid-column: 5 / 9; }
```

### 7.11.2. Dashboard Layout
```css
.dashboard {
    display: grid;
    grid-template-columns: 250px 1fr;
    grid-template-rows: 60px 1fr;
    grid-template-areas:
        "sidebar header"
        "sidebar content";
    min-height: 100vh;
    gap: 20px;
}

.sidebar { grid-area: sidebar; }
.header { grid-area: header; }
.content { grid-area: content; }
```

### 7.11.3. Photo Grid with Varying Sizes
```css
.photo-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 200px;
    gap: 10px;
}

.photo-item:nth-child(1) {
    grid-column: span 2;
    grid-row: span 2;
}

.photo-item:nth-child(5) {
    grid-column: span 2;
}
```

## Extended Practical Applications

### Real-World Implementation Example

```html
<!-- Complete implementation markup -->
<div class="implementation-container">
    <header class="header">
        <h1>Professional Implementation</h1>
    </header>
    <main class="main-content">
        <section class="content-section">
            <article class="article-card">
                <div class="card-image"></div>
                <div class="card-content">
                    <h2 class="card-title">Title</h2>
                    <p class="card-description">Description text goes here</p>
                </div>
                <div class="card-actions">
                    <button class="btn btn-primary">Action</button>
                    <button class="btn btn-secondary">Cancel</button>
                </div>
            </article>
        </section>
    </main>
    <footer class="footer">
        <p>&copy; 2025 All rights reserved</p>
    </footer>
</div>
```

```css
/* Professional implementation styles */
.implementation-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.header {
    padding: 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-align: center;
}

.main-content {
    flex: 1;
    padding: 2rem;
    background: #f5f7fa;
}

.content-section {
    max-width: 1200px;
    margin: 0 auto;
}

.article-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.article-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.15);
}

.card-image {
    height: 250px;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.card-content {
    padding: 2rem;
}

.card-title {
    font-size: 1.75rem;
    margin-bottom: 1rem;
    color: #2c3e50;
}

.card-description {
    color: #546e7a;
    line-height: 1.6;
}

.card-actions {
    padding: 1.5rem 2rem;
    border-top: 1px solid #eceff1;
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
}

.btn {
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-primary {
    background: #3498db;
    color: white;
}

.btn-primary:hover {
    background: #2980b9;
    transform: translateY(-1px);
}

.btn-secondary {
    background: #ecf0f1;
    color: #34495e;
}

.btn-secondary:hover {
    background: #bdc3c7;
}

.footer {
    padding: 2rem;
    background: #2c3e50;
    color: white;
    text-align: center;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .main-content {
        padding: 1rem;
    }

    .card-content {
        padding: 1.5rem;
    }

    .card-actions {
        flex-direction: column;
    }

    .btn {
        width: 100%;
    }
}
```

### Production-Ready Component Library

```css
/* Button variants */
.button-group {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.btn-xs { padding: 0.25rem 0.5rem; font-size: 0.75rem; }
.btn-sm { padding: 0.5rem 1rem; font-size: 0.875rem; }
.btn-md { padding: 0.75rem 1.5rem; font-size: 1rem; }
.btn-lg { padding: 1rem 2rem; font-size: 1.125rem; }
.btn-xl { padding: 1.25rem 2.5rem; font-size: 1.25rem; }

.btn-success { background: #2ecc71; }
.btn-warning { background: #f39c12; }
.btn-danger { background: #e74c3c; }
.btn-info { background: #3498db; }

.btn-outline {
    background: transparent;
    border: 2px solid currentColor;
}

.btn-rounded { border-radius: 9999px; }

.btn-icon {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

/* Card variations */
.card-elevated {
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.card-bordered {
    border: 2px solid #e0e0e0;
}

.card-horizontal {
    display: flex;
    flex-direction: row;
}

.card-horizontal .card-image {
    width: 40%;
    height: auto;
}

.card-horizontal .card-content {
    flex: 1;
}

/* Form elements */
.form-floating {
    position: relative;
}

.form-floating input {
    padding-top: 1.5rem;
}

.form-floating label {
    position: absolute;
    top: 0.5rem;
    left: 1rem;
    font-size: 0.75rem;
    color: #666;
    transition: all 0.2s;
}

.form-floating input:placeholder-shown + label {
    top: 50%;
    transform: translateY(-50%);
    font-size: 1rem;
}

.form-floating input:focus + label {
    top: 0.5rem;
    font-size: 0.75rem;
    color: #3498db;
}

/* Alert components */
.alert {
    padding: 1rem 1.5rem;
    border-radius: 8px;
    border-left: 4px solid;
    margin-bottom: 1rem;
}

.alert-success {
    background: #d5f4e6;
    border-left-color: #2ecc71;
    color: #27ae60;
}

.alert-info {
    background: #dce9f9;
    border-left-color: #3498db;
    color: #2980b9;
}

.alert-warning {
    background: #fef5e7;
    border-left-color: #f39c12;
    color: #e67e22;
}

.alert-error {
    background: #fadbd8;
    border-left-color: #e74c3c;
    color: #c0392b;
}

/* Badge components */
.badge {
    display: inline-flex;
    align-items: center;
    padding: 0.25rem 0.75rem;
    font-size: 0.875rem;
    font-weight: 600;
    border-radius: 9999px;
    color: white;
}

.badge-primary { background: #3498db; }
.badge-success { background: #2ecc71; }
.badge-warning { background: #f39c12; }
.badge-danger { background: #e74c3c; }

.badge-dot::before {
    content: '';
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: currentColor;
    margin-right: 0.5rem;
    animation: pulse 2s ease infinite;
}

@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
}

/* Skeleton loaders */
.skeleton {
    background: linear-gradient(
        90deg,
        #f0f0f0 25%,
        #e0e0e0 50%,
        #f0f0f0 75%
    );
    background-size: 200% 100%;
    animation: loading 1.5s ease-in-out infinite;
    border-radius: 4px;
}

.skeleton-text {
    height: 1rem;
    margin-bottom: 0.5rem;
}

.skeleton-title {
    height: 1.5rem;
    width: 60%;
    margin-bottom: 1rem;
}

.skeleton-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
}

.skeleton-image {
    aspect-ratio: 16/9;
    width: 100%;
}

/* Tooltip system */
[data-tooltip] {
    position: relative;
}

[data-tooltip]::before {
    content: attr(data-tooltip);
    position: absolute;
    bottom: calc(100% + 8px);
    left: 50%;
    transform: translateX(-50%);
    padding: 0.5rem 1rem;
    background: #333;
    color: white;
    font-size: 0.875rem;
    border-radius: 6px;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
}

[data-tooltip]:hover::before {
    opacity: 1;
}

/* Progress indicators */
.progress {
    height: 8px;
    background: #e0e0e0;
    border-radius: 9999px;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #3498db, #2ecc71);
    border-radius: inherit;
    transition: width 0.3s ease;
}

.progress-bar.animated {
    position: relative;
    overflow: hidden;
}

.progress-bar.animated::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,0.3),
        transparent
    );
    animation: shimmer 1.5s infinite;
}
```

## Performance Optimization Best Practices

### CSS Performance Tips

1. **Minimize Reflows and Repaints**
```css
/* Bad - causes reflow */
.element {
    width: 200px;
    margin-left: 50px;
}

/* Good - uses transform */
.element {
    transform: translateX(50px);
}
```

2. **Use will-change Sparingly**
```css
/* Only use when animating */
.animating {
    will-change: transform, opacity;
}

/* Remove after animation */
.element:not(.animating) {
    will-change: auto;
}
```

3. **Optimize Selectors**
```css
/* Bad - expensive */
div > ul > li > a { }

/* Good - specific class */
.nav-link { }
```

4. **Use contain Property**
```css
.independent-component {
    contain: layout style paint;
}
```

5. **Leverage CSS Containment**
```css
.widget {
    contain: content;
}
```

---

**Final thoughts:** Mastering these techniques and patterns will make you a proficient CSS developer capable of building production-ready, maintainable, and performant web applications.
