# CHƯƠNG 10: CSS3 TRANSFORMS

## 10.1. 2D Transforms

### 10.1.1. translate()

```css
.box {
    /* Move element */
    transform: translate(50px, 100px);  /* x, y */
    transform: translateX(50px);        /* x only */
    transform: translateY(100px);       /* y only */

    /* Percentage (relative to element size) */
    transform: translate(50%, 50%);

    /* Center positioning trick */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

### 10.1.2. scale()

```css
.box {
    /* Scale both axes */
    transform: scale(1.5);          /* 150% */
    transform: scale(2, 0.5);       /* x: 200%, y: 50% */

    /* Individual axes */
    transform: scaleX(1.5);
    transform: scaleY(0.8);

    /* Flip */
    transform: scaleX(-1);  /* Horizontal flip */
    transform: scaleY(-1);  /* Vertical flip */
}
```

### 10.1.3. rotate()

```css
.box {
    transform: rotate(45deg);      /* Clockwise */
    transform: rotate(-45deg);     /* Counter-clockwise */
    transform: rotate(0.5turn);    /* Half turn */
    transform: rotate(180deg);     /* 180 degrees */
}
```

### 10.1.4. skew()

```css
.box {
    transform: skew(20deg, 10deg);  /* x, y */
    transform: skewX(20deg);
    transform: skewY(10deg);
}
```

### 10.1.5. Multiple Transforms

```css
.box {
    /* Order matters! */
    transform: translate(50px, 50px) rotate(45deg) scale(1.5);

    /* Different order = different result */
    transform: rotate(45deg) translate(50px, 50px) scale(1.5);
}
```

## 10.2. 3D Transforms

### 10.2.1. perspective

```css
.container {
    perspective: 1000px;  /* Set 3D perspective */
}

.box {
    transform: rotateY(45deg);
}

/* Or on element itself */
.box {
    transform: perspective(1000px) rotateY(45deg);
}
```

### 10.2.2. rotateX(), rotateY(), rotateZ()

```css
.box {
    transform: rotateX(45deg);   /* Around X axis */
    transform: rotateY(45deg);   /* Around Y axis */
    transform: rotateZ(45deg);   /* Around Z axis (same as rotate()) */

    /* 3D rotation */
    transform: rotate3d(1, 1, 1, 45deg);  /* x, y, z, angle */
}
```

### 10.2.3. translateZ() và translate3d()

```css
.box {
    transform: translateZ(100px);  /* Move toward viewer */

    /* 3D translate */
    transform: translate3d(50px, 100px, 200px);  /* x, y, z */
}
```

### 10.2.4. scaleZ() và scale3d()

```css
.box {
    transform: scaleZ(2);
    transform: scale3d(1.5, 1.5, 2);  /* x, y, z */
}
```

## 10.3. Transform Properties

### 10.3.1. transform-origin

```css
.box {
    /* Default: center */
    transform-origin: center center;

    /* Keywords */
    transform-origin: top left;
    transform-origin: bottom right;
    transform-origin: center;

    /* Percentages */
    transform-origin: 50% 50%;

    /* Pixels */
    transform-origin: 10px 20px;

    /* 3D */
    transform-origin: 50% 50% 100px;
}

/* Example: Rotate from corner */
.box {
    transform-origin: top left;
    transform: rotate(45deg);
}
```

### 10.3.2. transform-style

```css
.parent {
    transform-style: flat;          /* Default */
    transform-style: preserve-3d;   /* Children in 3D space */
}
```

### 10.3.3. perspective-origin

```css
.container {
    perspective: 1000px;
    perspective-origin: 50% 50%;    /* Default: center */
    perspective-origin: left top;
    perspective-origin: 100px 200px;
}
```

### 10.3.4. backface-visibility

```css
.box {
    backface-visibility: visible;   /* Default */
    backface-visibility: hidden;    /* Hide when rotated */
}

/* Card flip example */
.card-front,
.card-back {
    backface-visibility: hidden;
}
```

## 10.4. Practical Examples

### 10.4.1. Hover Grow

```css
.button {
    transition: transform 0.3s ease;
}

.button:hover {
    transform: scale(1.1);
}
```

### 10.4.2. Card Flip

```css
.card-container {
    perspective: 1000px;
}

.card {
    width: 300px;
    height: 400px;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.6s;
}

.card:hover {
    transform: rotateY(180deg);
}

.card-front,
.card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
}

.card-back {
    transform: rotateY(180deg);
}
```

### 10.4.3. 3D Cube

```css
.cube-container {
    perspective: 1000px;
}

.cube {
    width: 200px;
    height: 200px;
    position: relative;
    transform-style: preserve-3d;
    animation: rotateCube 10s infinite linear;
}

@keyframes rotateCube {
    from { transform: rotateX(0deg) rotateY(0deg); }
    to { transform: rotateX(360deg) rotateY(360deg); }
}

.cube-face {
    position: absolute;
    width: 200px;
    height: 200px;
    border: 2px solid #333;
}

.cube-face.front  { transform: rotateY(0deg) translateZ(100px); }
.cube-face.back   { transform: rotateY(180deg) translateZ(100px); }
.cube-face.right  { transform: rotateY(90deg) translateZ(100px); }
.cube-face.left   { transform: rotateY(-90deg) translateZ(100px); }
.cube-face.top    { transform: rotateX(90deg) translateZ(100px); }
.cube-face.bottom { transform: rotateX(-90deg) translateZ(100px); }
```

### 10.4.4. Parallax Effect

```css
.parallax-layer {
    transform: translateZ(-500px) scale(1.5);
}

.parallax-container {
    perspective: 1000px;
    overflow-x: hidden;
    overflow-y: auto;
}
```

### 10.4.5. Skewed Section

```css
.section {
    position: relative;
    background: #3498db;
    padding: 100px 0;
}

.section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: inherit;
    transform: skewY(-3deg);
    transform-origin: top left;
}
```

### 10.4.6. Image Zoom on Hover

```css
.image-container {
    overflow: hidden;
}

.image-container img {
    transition: transform 0.5s ease;
}

.image-container:hover img {
    transform: scale(1.2);
}
```

### 10.4.7. Rotating Badge

```css
.badge {
    position: absolute;
    top: 20px;
    right: -40px;
    background: red;
    color: white;
    padding: 5px 40px;
    transform: rotate(45deg);
}
```

## 10.5. Animation with Transforms

```css
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
}

@keyframes flip {
    0% { transform: rotateY(0deg); }
    100% { transform: rotateY(360deg); }
}

.spinning {
    animation: spin 2s linear infinite;
}
```

## 10.6. Performance Tips

```css
/* Good: Use transform for movement */
.box {
    transform: translate(100px, 100px);
}

/* Avoid: Position properties (cause reflow) */
.box {
    top: 100px;
    left: 100px;
}

/* Use will-change for complex transforms */
.box {
    will-change: transform;
}

/* Use transform: translate3d for hardware acceleration */
.box {
    transform: translate3d(100px, 100px, 0);
}
```

## 10.7. Matrix Transform

```css
/* Advanced: matrix transformation */
.box {
    transform: matrix(a, b, c, d, tx, ty);
    transform: matrix3d(...); /* 16 values */
}

/* Equivalent transformations */
transform: translate(50px, 100px);
/* Same as */
transform: matrix(1, 0, 0, 1, 50, 100);
```

---

**Kết luận:** Transforms cho phép manipulate elements trong 2D và 3D space. Essential cho animations và interactive effects. Transform and opacity là hai properties performant nhất để animate.

**Chương tiếp theo:** Media Queries & Responsive Design


## 10.10. Practical Examples - Extended

### 10.10.1. 3D Card Stack

Layered card effect

```css
.card-stack {
    perspective: 1000px;
}

.card {
    transform-style: preserve-3d;
    transition: transform 0.5s;
}

.card:nth-child(1) { transform: translateZ(0px) translateY(0px); }
.card:nth-child(2) { transform: translateZ(-50px) translateY(-20px); }
.card:nth-child(3) { transform: translateZ(-100px) translateY(-40px); }
```

### 10.10.2. Isometric Grid

3D grid layout

```css
.isometric-grid {
    display: grid;
    grid-template-columns: repeat(3, 150px);
    gap: 10px;
    transform: rotateX(60deg) rotateZ(-45deg);
}

.iso-item {
    height: 150px;
    transform: translateZ(0);
}
```


## 10.11. Real-World Use Cases

### 10.11.1. Product Showcases

360-degree product views

```css
/* Implementation details */
```

### 10.11.2. Interactive Diagrams

Rotatable 3D diagrams

```css
/* Implementation details */
```

### 10.11.3. Game UIs

Transform-based game interfaces

```css
/* Implementation details */
```

### 10.11.4. Data Visualization

3D charts and graphs

```css
/* Implementation details */
```

### 10.11.5. Creative Portfolios

Unique presentation styles

```css
/* Implementation details */
```


## 10.12. Tips & Tricks

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

## 10.13. Common Mistakes

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

## 10.14. Troubleshooting

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

## 10.15. Advanced Topics

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

## 10.16. Bài Tập

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

**Chương tiếp theo:** Media Queries & Responsive


## 10.20. Advanced Transform Techniques

### 10.20.1. 3D Carousel
```css
.carousel-3d {
    perspective: 1000px;
    width: 300px;
    height: 200px;
    position: relative;
}

.carousel-container {
    width: 100%;
    height: 100%;
    position: absolute;
    transform-style: preserve-3d;
    animation: rotate-carousel 20s linear infinite;
}

.carousel-item {
    position: absolute;
    width: 250px;
    height: 150px;
    left: 25px;
    top: 25px;
    backface-visibility: hidden;
}

.carousel-item:nth-child(1) { transform: rotateY(0deg) translateZ(300px); }
.carousel-item:nth-child(2) { transform: rotateY(60deg) translateZ(300px); }
.carousel-item:nth-child(3) { transform: rotateY(120deg) translateZ(300px); }
.carousel-item:nth-child(4) { transform: rotateY(180deg) translateZ(300px); }
.carousel-item:nth-child(5) { transform: rotateY(240deg) translateZ(300px); }
.carousel-item:nth-child(6) { transform: rotateY(300deg) translateZ(300px); }

@keyframes rotate-carousel {
    to { transform: rotateY(360deg); }
}
```

### 10.20.2. Folding Panel
```css
.fold-panel {
    perspective: 1000px;
}

.fold-section {
    transform-origin: top;
    transform-style: preserve-3d;
    transition: transform 0.6s;
}

.fold-panel:hover .fold-section:nth-child(1) {
    transform: rotateX(-20deg);
}

.fold-panel:hover .fold-section:nth-child(2) {
    transform: rotateX(-40deg);
}

.fold-panel:hover .fold-section:nth-child(3) {
    transform: rotateX(-60deg);
}
```

### 10.20.3. Perspective Text
```css
.perspective-text {
    perspective: 500px;
    display: inline-block;
}

.perspective-text span {
    display: inline-block;
    transform: rotateY(15deg);
    transform-origin: left;
    transition: transform 0.3s;
}

.perspective-text:hover span {
    transform: rotateY(0deg);
}
```

### 10.20.4. Zoom on Hover
```css
.zoom-container {
    overflow: hidden;
}

.zoom-image {
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.zoom-container:hover .zoom-image {
    transform: scale(1.2);
}
```

### 10.20.5. Rotating Cube Navigation
```css
.cube-nav {
    width: 200px;
    height: 200px;
    perspective: 1000px;
}

.cube {
    width: 100%;
    height: 100%;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.6s;
}

.cube-face {
    position: absolute;
    width: 200px;
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    backface-visibility: hidden;
}

.cube-face.front  { transform: rotateY(0deg) translateZ(100px); }
.cube-face.right  { transform: rotateY(90deg) translateZ(100px); }
.cube-face.back   { transform: rotateY(180deg) translateZ(100px); }
.cube-face.left   { transform: rotateY(-90deg) translateZ(100px); }
.cube-face.top    { transform: rotateX(90deg) translateZ(100px); }
.cube-face.bottom { transform: rotateX(-90deg) translateZ(100px); }

.cube-nav[data-face="right"] .cube { transform: rotateY(-90deg); }
.cube-nav[data-face="back"] .cube { transform: rotateY(-180deg); }
.cube-nav[data-face="left"] .cube { transform: rotateY(90deg); }
```

### 10.20.6. Skewed Section Dividers
```css
.section {
    position: relative;
    padding: 100px 0;
}

.section::before,
.section::after {
    content: '';
    position: absolute;
    left: 0;
    right: 0;
    height: 100px;
    background: inherit;
    z-index: -1;
}

.section::before {
    top: 0;
    transform: skewY(-3deg);
    transform-origin: top left;
}

.section::after {
    bottom: 0;
    transform: skewY(3deg);
    transform-origin: bottom right;
}
```

### 10.20.7. Wobble Effect
```css
.wobble {
    animation: wobble 1s ease-in-out;
}

@keyframes wobble {
    0%, 100% { transform: translateX(0%) rotate(0deg); }
    15% { transform: translateX(-25px) rotate(-5deg); }
    30% { transform: translateX(20px) rotate(3deg); }
    45% { transform: translateX(-15px) rotate(-3deg); }
    60% { transform: translateX(10px) rotate(2deg); }
    75% { transform: translateX(-5px) rotate(-1deg); }
}
```

### 10.20.8. Parallax Scrolling Effect
```css
.parallax-container {
    perspective: 1px;
    height: 100vh;
    overflow-x: hidden;
    overflow-y: auto;
}

.parallax-layer-back {
    transform: translateZ(-1px) scale(2);
}

.parallax-layer-base {
    transform: translateZ(0);
}

.parallax-layer-front {
    transform: translateZ(1px) scale(0.5);
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
