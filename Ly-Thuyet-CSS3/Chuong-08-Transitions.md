# CHƯƠNG 8: CSS3 TRANSITIONS

## 8.1. Giới thiệu Transitions

Transitions cho phép thay đổi property values một cách smooth over a duration.

### 8.1.1. Basic Syntax

```css
.box {
    transition: property duration timing-function delay;
}

/* Example */
.button {
    background-color: blue;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: red;
}
```

## 8.2. Transition Properties

### 8.2.1. transition-property

```css
.box {
    /* Single property */
    transition-property: background-color;

    /* Multiple properties */
    transition-property: background-color, transform, opacity;

    /* All properties */
    transition-property: all;
}
```

### 8.2.2. transition-duration

```css
.box {
    /* Seconds */
    transition-duration: 0.3s;
    transition-duration: 2s;

    /* Milliseconds */
    transition-duration: 300ms;

    /* Multiple durations */
    transition-duration: 0.3s, 0.5s, 1s;
}
```

### 8.2.3. transition-timing-function

```css
.box {
    /* Keywords */
    transition-timing-function: ease;        /* Slow start, fast, slow end */
    transition-timing-function: linear;      /* Constant speed */
    transition-timing-function: ease-in;     /* Slow start */
    transition-timing-function: ease-out;    /* Slow end */
    transition-timing-function: ease-in-out; /* Slow start and end */

    /* Cubic bezier */
    transition-timing-function: cubic-bezier(0.42, 0, 0.58, 1);

    /* Steps */
    transition-timing-function: steps(4, end);
    transition-timing-function: step-start;
    transition-timing-function: step-end;
}
```

### 8.2.4. transition-delay

```css
.box {
    /* Delay before transition starts */
    transition-delay: 0.5s;
    transition-delay: 200ms;

    /* Multiple delays */
    transition-delay: 0s, 0.2s, 0.4s;
}
```

### 8.2.5. Transition Shorthand

```css
.box {
    /* property | duration | timing-function | delay */
    transition: background-color 0.3s ease 0s;
    transition: all 0.5s cubic-bezier(0.42, 0, 0.58, 1);

    /* Multiple transitions */
    transition:
        background-color 0.3s ease,
        transform 0.5s ease-out,
        opacity 0.2s linear;
}
```

## 8.3. Transitionable Properties

```css
/* Color properties */
.box {
    transition: color 0.3s, background-color 0.3s, border-color 0.3s;
}

/* Transform */
.box {
    transition: transform 0.3s;
}

/* Opacity */
.box {
    transition: opacity 0.3s;
}

/* Dimensions */
.box {
    transition: width 0.3s, height 0.3s;
}

/* Position */
.box {
    transition: top 0.3s, left 0.3s;
}

/* Box shadow */
.box {
    transition: box-shadow 0.3s;
}

/* Not transitionable: display, position, font-family */
```

## 8.4. Practical Examples

### 8.4.1. Button Hover Effect

```css
.button {
    background-color: #3498db;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.button:hover {
    background-color: #2980b9;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.button:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
```

### 8.4.2. Card Hover

```css
.card {
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
```

### 8.4.3. Smooth Color Change

```css
.link {
    color: #3498db;
    text-decoration: none;
    position: relative;
    transition: color 0.3s ease;
}

.link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background-color: #3498db;
    transition: width 0.3s ease;
}

.link:hover {
    color: #2980b9;
}

.link:hover::after {
    width: 100%;
}
```

### 8.4.4. Expandable Search

```css
.search-input {
    width: 40px;
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 20px;
    transition: width 0.3s ease, padding 0.3s ease;
}

.search-input:focus {
    width: 200px;
    padding: 10px 20px;
    outline: none;
    border-color: #3498db;
}
```

### 8.4.5. Image Zoom

```css
.image-container {
    overflow: hidden;
    border-radius: 8px;
}

.image-container img {
    width: 100%;
    transition: transform 0.5s ease;
}

.image-container:hover img {
    transform: scale(1.1);
}
```

### 8.4.6. Loading Spinner

```css
.spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #f3f3f3;
    border-top: 5px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

/* Using transition for smoothness */
.progress-bar {
    width: 0%;
    height: 4px;
    background-color: #3498db;
    transition: width 0.5s ease;
}

.progress-bar.complete {
    width: 100%;
}
```

## 8.5. Timing Functions Explained

```css
/* ease: slow start, fast middle, slow end */
.ease {
    transition: transform 1s ease;
}

/* linear: constant speed */
.linear {
    transition: transform 1s linear;
}

/* ease-in: slow start */
.ease-in {
    transition: transform 1s ease-in;
}

/* ease-out: slow end */
.ease-out {
    transition: transform 1s ease-out;
}

/* ease-in-out: slow start and end */
.ease-in-out {
    transition: transform 1s ease-in-out;
}

/* Custom cubic-bezier */
.custom {
    /* Bouncy effect */
    transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
```

## 8.6. Multiple Transitions

```css
.box {
    transition:
        background-color 0.3s ease,
        transform 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) 0.1s,
        opacity 0.2s linear,
        box-shadow 0.3s ease;
}

.box:hover {
    background-color: #3498db;
    transform: scale(1.05) rotate(5deg);
    opacity: 0.9;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}
```

## 8.7. Best Practices

```css
/* Good: Transition specific properties */
.button {
    transition: background-color 0.3s, transform 0.3s;
}

/* Avoid: all (performance) */
.button {
    transition: all 0.3s;  /* Can be slow */
}

/* Use transform and opacity for best performance */
.box {
    transition: transform 0.3s, opacity 0.3s;
}

/* Avoid transitioning width/height (use transform: scale instead) */
.box {
    /* Bad */
    transition: width 0.3s;

    /* Good */
    transition: transform 0.3s;
}
.box:hover {
    transform: scaleX(1.2);
}
```

## 8.8. Common Patterns

### 8.8.1. Fade In/Out

```css
.fade {
    opacity: 0;
    transition: opacity 0.3s ease;
}

.fade.show {
    opacity: 1;
}
```

### 8.8.2. Slide

```css
.slide {
    transform: translateX(-100%);
    transition: transform 0.3s ease;
}

.slide.active {
    transform: translateX(0);
}
```

### 8.8.3. Grow

```css
.grow {
    transform: scale(1);
    transition: transform 0.3s ease;
}

.grow:hover {
    transform: scale(1.1);
}
```

### 8.8.4. Rotate

```css
.rotate {
    transition: transform 0.5s ease;
}

.rotate:hover {
    transform: rotate(360deg);
}
```

---

**Kết luận:** Transitions làm UI mượt mà và professional. Prefer transitioning transform và opacity cho performance tốt nhất.

**Chương tiếp theo:** Animations


## 8.10. Practical Examples - Extended

### 8.10.1. Menu Slide-in

Smooth menu animation

```css
.menu {
    position: fixed;
    top: 0;
    left: -300px;
    width: 300px;
    height: 100vh;
    background: white;
    transition: left 0.3s ease;
}

.menu.active {
    left: 0;
}
```

### 8.10.2. Progress Bar Animation

Smooth progress fill

```css
.progress-bar {
    width: 0%;
    height: 4px;
    background: #3498db;
    transition: width 1s ease-out;
}

.progress-bar.loaded {
    width: 100%;
}
```


## 8.11. Real-World Use Cases

### 8.11.1. Loading States

Smooth state transitions

```css
/* Implementation details */
```

### 8.11.2. Form Validation

Error message animations

```css
/* Implementation details */
```

### 8.11.3. Image Galleries

Hover effects on images

```css
/* Implementation details */
```

### 8.11.4. Notification Toasts

Slide-in notifications

```css
/* Implementation details */
```

### 8.11.5. Accordion Menus

Expand/collapse smoothly

```css
/* Implementation details */
```


## 8.12. Tips & Tricks

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

## 8.13. Common Mistakes

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

## 8.14. Troubleshooting

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

## 8.15. Advanced Topics

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

## 8.16. Bài Tập

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

**Chương tiếp theo:** Animations


## 8.10. Advanced Transition Techniques

### 8.10.1. Staggered Transitions
```css
.list-item {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.3s, transform 0.3s;
}

.list-item:nth-child(1) { transition-delay: 0.1s; }
.list-item:nth-child(2) { transition-delay: 0.2s; }
.list-item:nth-child(3) { transition-delay: 0.3s; }
.list-item:nth-child(4) { transition-delay: 0.4s; }

.list-item.visible {
    opacity: 1;
    transform: translateY(0);
}
```

### 8.10.2. Easing Function Visualizations
```css
.ease { transition-timing-function: ease; }
.ease-in { transition-timing-function: ease-in; }
.ease-out { transition-timing-function: ease-out; }
.ease-in-out { transition-timing-function: ease-in-out; }
.linear { transition-timing-function: linear; }

/* Custom bezier curves */
.bounce { transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55); }
.elastic { transition-timing-function: cubic-bezier(0.68, -0.6, 0.32, 1.6); }
```

### 8.10.3. Multi-Property Transitions
```css
.card {
    transition:
        transform 0.3s cubic-bezier(0.4, 0, 0.2, 1),
        box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1),
        background-color 0.2s ease,
        color 0.2s ease;
}

.card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    background-color: #f8f9fa;
    color: #333;
}
```

### 8.10.4. Page Transition Effects
```css
.page {
    opacity: 0;
    transform: translateX(-100%);
    transition: opacity 0.3s, transform 0.3s;
}

.page.enter {
    opacity: 1;
    transform: translateX(0);
}

.page.exit {
    opacity: 0;
    transform: translateX(100%);
}
```

### 8.10.5. Hover Underline Effects
```css
.link {
    position: relative;
    text-decoration: none;
}

.link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: currentColor;
    transform: scaleX(0);
    transform-origin: right;
    transition: transform 0.3s ease;
}

.link:hover::after {
    transform: scaleX(1);
    transform-origin: left;
}
```

### 8.10.6. Modal Transitions
```css
.modal-overlay {
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
}

.modal-overlay.active {
    opacity: 1;
    pointer-events: all;
}

.modal {
    transform: translateY(-50px);
    opacity: 0;
    transition: transform 0.3s, opacity 0.3s;
}

.modal-overlay.active .modal {
    transform: translateY(0);
    opacity: 1;
}
```

### 8.10.7. Accordion Transitions
```css
.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
}

.accordion-item.active .accordion-content {
    max-height: 500px; /* Approximate max height */
}
```

### 8.10.8. Color Scheme Transitions
```css
:root {
    --bg: white;
    --text: black;
    transition: --bg 0.3s, --text 0.3s;
}

body {
    background: var(--bg);
    color: var(--text);
    transition: background 0.3s, color 0.3s;
}

[data-theme="dark"] {
    --bg: #1a1a1a;
    --text: white;
}
```

### 8.10.9. Hover Grow Effect
```css
.grow {
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.grow:hover {
    transform: scale(1.05);
}
```

### 8.10.10. Slide Toggle
```css
.slide-toggle {
    height: 0;
    overflow: hidden;
    transition: height 0.3s ease;
}

.slide-toggle.open {
    height: auto; /* This won't transition */
}

/* Better approach */
.slide-toggle {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
}

.slide-toggle.open {
    max-height: 1000px;
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
