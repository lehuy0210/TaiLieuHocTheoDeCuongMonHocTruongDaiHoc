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


## 6.10. Practical Examples - Extended

### 6.10.1. Navigation Menu

Responsive navbar with flexbox

```css
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-links {
    display: flex;
    gap: 2rem;
    list-style: none;
}

@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
    }
}
```

### 6.10.2. Card Grid with Flexbox

Equal height cards

```css
.card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.card {
    flex: 1 1 calc(33.333% - 20px);
    min-width: 250px;
    display: flex;
    flex-direction: column;
}

.card-content {
    flex-grow: 1;
}
```


## 6.11. Real-World Use Cases

### 6.11.1. Shopping Cart Layout

Product list with quantity controls

```css
/* Implementation details */
```

### 6.11.2. Social Media Feed

Post cards with dynamic content

```css
/* Implementation details */
```

### 6.11.3. Dashboard Widgets

Flexible widget arrangement

```css
/* Implementation details */
```

### 6.11.4. Footer Layout

Multi-column responsive footer

```css
/* Implementation details */
```

### 6.11.5. Mobile App Bottom Navigation

Icon navigation bar

```css
/* Implementation details */
```


## 6.12. Tips & Tricks

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

## 6.13. Common Mistakes

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

## 6.14. Troubleshooting

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

## 6.15. Advanced Topics

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

## 6.16. Bài Tập

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

**Chương tiếp theo:** Grid Layout


## 6.10. Advanced Flexbox Patterns

### 6.10.1. Equal Height Columns with Different Content
```css
.equal-height-container {
    display: flex;
    gap: 20px;
}

.equal-height-column {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.equal-height-column > * {
    flex-grow: 1;
}
```

### 6.10.2. Sticky Footer with Flexbox
```css
body {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

main {
    flex: 1;
}

footer {
    flex-shrink: 0;
}
```

### 6.10.3. Media Object Pattern
```css
.media {
    display: flex;
    gap: 20px;
}

.media-figure {
    flex-shrink: 0;
}

.media-body {
    flex: 1;
    min-width: 0; /* Prevents overflow */
}
```

### 6.10.4. Vertical Centering Techniques
```css
/* Method 1: Flexbox */
.center-flex {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

/* Method 2: Margin auto */
.center-margin {
    display: flex;
    min-height: 100vh;
}

.centered-item {
    margin: auto;
}
```

### 6.10.5. Responsive Flexbox Grid
```css
.flex-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.flex-grid-item {
    flex: 1 1 calc(33.333% - 20px);
    min-width: 250px;
}

@media (max-width: 768px) {
    .flex-grid-item {
        flex-basis: calc(50% - 20px);
    }
}

@media (max-width: 480px) {
    .flex-grid-item {
        flex-basis: 100%;
    }
}
```

### 6.10.6. Input Groups
```css
.input-group {
    display: flex;
}

.input-group input {
    flex: 1;
    border-radius: 4px 0 0 4px;
}

.input-group button {
    flex-shrink: 0;
    border-radius: 0 4px 4px 0;
}
```

### 6.10.7. Pricing Table with Flexbox
```css
.pricing-container {
    display: flex;
    gap: 30px;
    align-items: stretch;
}

.pricing-card {
    flex: 1;
    display: flex;
    flex-direction: column;
    border: 1px solid #ddd;
    border-radius: 8px;
}

.pricing-header {
    padding: 30px;
    text-align: center;
}

.pricing-features {
    flex: 1;
    padding: 20px;
}

.pricing-footer {
    padding: 30px;
    margin-top: auto;
}
```

### 6.10.8. Split Screen Layout
```css
.split-screen {
    display: flex;
    min-height: 100vh;
}

.split-left,
.split-right {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px;
}

@media (max-width: 768px) {
    .split-screen {
        flex-direction: column;
    }
}
```

### 6.10.9. Flex Basis Tricks
```css
/* Fixed sidebar, flexible content */
.layout {
    display: flex;
}

.sidebar {
    flex: 0 0 300px; /* No grow, no shrink, 300px wide */
}

.content {
    flex: 1; /* Takes remaining space */
    min-width: 0; /* Prevents overflow */
}
```

### 6.10.10. Flexbox Order Property Use Cases
```css
/* Reorder items on mobile */
.flex-container {
    display: flex;
}

.content {
    order: 2;
}

.sidebar {
    order: 1;
}

@media (min-width: 768px) {
    .content { order: 1; }
    .sidebar { order: 2; }
}
```

## 6.11. Flexbox Performance Optimization

### 6.11.1. Avoid Nested Flex Containers
```css
/* Less performant */
.outer {
    display: flex;
}

.inner {
    display: flex;
}

/* Better: Use Grid for 2D layouts */
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}
```

### 6.11.2. Use flex Shorthand
```css
/* Instead of */
.item {
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: 0%;
}

/* Use */
.item {
    flex: 1;
}
```

### 6.11.3. Minimize Flex Item Count
```css
/* Avoid too many flex items in one container */
/* If you have 100+ items, consider virtualization */
```

## 6.25. Flexbox Complete Reference

### 6.25.1. Container Properties Reference

#### display
```css
.container {
    display: flex;        /* Block-level flex container */
    display: inline-flex; /* Inline-level flex container */
}
```

#### flex-direction
```css
.container {
    flex-direction: row;            /* Default: left to right */
    flex-direction: row-reverse;    /* Right to left */
    flex-direction: column;         /* Top to bottom */
    flex-direction: column-reverse; /* Bottom to top */
}
```

#### flex-wrap
```css
.container {
    flex-wrap: nowrap;       /* Default: single line */
    flex-wrap: wrap;         /* Multi-line */
    flex-wrap: wrap-reverse; /* Multi-line, reverse order */
}
```

#### justify-content
```css
.container {
    justify-content: flex-start;    /* Align to start (default) */
    justify-content: flex-end;      /* Align to end */
    justify-content: center;        /* Center alignment */
    justify-content: space-between; /* Even distribution */
    justify-content: space-around;  /* Equal space around */
    justify-content: space-evenly;  /* Equal space between */
}
```

#### align-items
```css
.container {
    align-items: stretch;    /* Fill container (default) */
    align-items: flex-start; /* Align to start */
    align-items: flex-end;   /* Align to end */
    align-items: center;     /* Center alignment */
    align-items: baseline;   /* Baseline alignment */
}
```

### 6.25.2. Item Properties Reference

#### order
```css
.item {
    order: 0;  /* Default */
    order: -1; /* Appears first */
    order: 1;  /* Appears later */
}
```

#### flex-grow
```css
.item {
    flex-grow: 0; /* Default: doesn't grow */
    flex-grow: 1; /* Grows to fill space */
    flex-grow: 2; /* Grows twice as much */
}
```

#### flex-shrink
```css
.item {
    flex-shrink: 1; /* Default: can shrink */
    flex-shrink: 0; /* Doesn't shrink */
    flex-shrink: 2; /* Shrinks twice as much */
}
```

#### flex-basis
```css
.item {
    flex-basis: auto;   /* Default: based on content */
    flex-basis: 200px;  /* Fixed width */
    flex-basis: 50%;    /* Percentage width */
    flex-basis: 0;      /* Zero base width */
}
```

### 6.25.3. Complete Flexbox Examples

#### E-commerce Product Grid
```css
.product-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    padding: 40px 20px;
}

.product-card {
    flex: 1 1 calc(25% - 30px);
    min-width: 250px;
    display: flex;
    flex-direction: column;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}

.product-image {
    aspect-ratio: 1/1;
    background: #f5f5f5;
    border-radius: 12px 12px 0 0;
}

.product-info {
    flex: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
}

.product-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 10px;
}

.product-price {
    font-size: 1.5rem;
    color: #e74c3c;
    font-weight: bold;
    margin-top: auto;
}

.product-actions {
    padding: 20px;
    border-top: 1px solid #e0e0e0;
    display: flex;
    gap: 10px;
}

.add-to-cart {
    flex: 1;
    padding: 12px;
    background: #3498db;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

@media (max-width: 1200px) {
    .product-card {
        flex-basis: calc(33.333% - 30px);
    }
}

@media (max-width: 768px) {
    .product-card {
        flex-basis: calc(50% - 30px);
    }
}

@media (max-width: 480px) {
    .product-card {
        flex-basis: 100%;
    }
}
```

#### Social Media Feed Layout
```css
.feed-container {
    display: flex;
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.feed-main {
    flex: 1;
    min-width: 0;
}

.feed-sidebar {
    flex: 0 0 300px;
    position: sticky;
    top: 20px;
    height: fit-content;
}

.feed-post {
    display: flex;
    flex-direction: column;
    background: white;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.post-header {
    display: flex;
    align-items: center;
    padding: 15px 20px;
    gap: 12px;
}

.post-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #3498db;
}

.post-author {
    flex: 1;
    min-width: 0;
}

.post-name {
    font-weight: 600;
    margin-bottom: 2px;
}

.post-time {
    font-size: 0.875rem;
    color: #666;
}

.post-content {
    padding: 0 20px 15px;
}

.post-image {
    width: 100%;
    aspect-ratio: 16/9;
    object-fit: cover;
}

.post-actions {
    display: flex;
    padding: 15px 20px;
    gap: 20px;
    border-top: 1px solid #e0e0e0;
}

.post-action {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 8px;
    border-radius: 6px;
    cursor: pointer;
    transition: background 0.2s;
}

.post-action:hover {
    background: #f0f0f0;
}

@media (max-width: 768px) {
    .feed-container {
        flex-direction: column;
    }

    .feed-sidebar {
        position: static;
        flex: 1;
    }
}
```

#### Mobile App Bottom Navigation
```css
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: white;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    display: flex;
    padding: 8px 0;
    z-index: 1000;
}

.nav-item {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    padding: 8px;
    cursor: pointer;
    color: #666;
    transition: color 0.2s;
}

.nav-item.active {
    color: #3498db;
}

.nav-icon {
    width: 24px;
    height: 24px;
}

.nav-label {
    font-size: 0.75rem;
    font-weight: 500;
}
```

#### Flexbox Form Layout
```css
.flex-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    max-width: 600px;
    margin: 0 auto;
}

.form-row {
    display: flex;
    gap: 15px;
}

.form-group {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.form-label {
    font-weight: 500;
    color: #333;
}

.form-input {
    padding: 12px 16px;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    font-size: 1rem;
    transition: border-color 0.2s;
}

.form-input:focus {
    outline: none;
    border-color: #3498db;
}

.form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 20px;
}

.form-button {
    padding: 12px 24px;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}

.form-button.primary {
    background: #3498db;
    color: white;
}

.form-button.secondary {
    background: #e0e0e0;
    color: #333;
}

@media (max-width: 600px) {
    .form-row {
        flex-direction: column;
    }
}
```

---

**Kết luận mở rộng:** Flexbox là một trong những tools quan trọng nhất trong modern CSS. Nắm vững Flexbox giúp bạn tạo ra layouts linh hoạt, responsive, và maintainable một cách dễ dàng. Kết hợp với CSS Grid, bạn có thể giải quyết hầu hết mọi layout challenge trong web development.

**Chương tiếp theo:** Grid Layout
