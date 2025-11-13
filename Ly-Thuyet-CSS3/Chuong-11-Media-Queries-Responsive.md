# CHƯƠNG 11: MEDIA QUERIES & RESPONSIVE DESIGN

## 11.1. Media Queries Basics

### 11.1.1. Basic Syntax

```css
@media media-type and (condition) {
    /* CSS rules */
}

/* Example */
@media screen and (max-width: 768px) {
    .container {
        width: 100%;
    }
}
```

### 11.1.2. Media Types

```css
@media screen { }    /* Screens */
@media print { }     /* Print */
@media speech { }    /* Screen readers */
@media all { }       /* All devices (default) */
```

## 11.2. Common Breakpoints

```css
/* Mobile First Approach */
/* Mobile (default) */
.container {
    width: 100%;
    padding: 10px;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        width: 750px;
        margin: 0 auto;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        width: 1000px;
    }
}

/* Large Desktop */
@media (min-width: 1440px) {
    .container {
        width: 1200px;
    }
}
```

```css
/* Desktop First Approach */
/* Desktop (default) */
.container {
    width: 1200px;
}

/* Tablet */
@media (max-width: 1024px) {
    .container {
        width: 750px;
    }
}

/* Mobile */
@media (max-width: 768px) {
    .container {
        width: 100%;
    }
}
```

## 11.3. Width and Height Queries

```css
/* Width */
@media (min-width: 600px) { }
@media (max-width: 1200px) { }
@media (width: 600px) { }  /* Exact width */

/* Range */
@media (min-width: 600px) and (max-width: 1200px) { }

/* Modern range syntax */
@media (600px <= width <= 1200px) { }

/* Height */
@media (min-height: 600px) { }
@media (max-height: 800px) { }
```

## 11.4. Orientation

```css
/* Portrait */
@media (orientation: portrait) {
    .sidebar {
        display: none;
    }
}

/* Landscape */
@media (orientation: landscape) {
    .content {
        display: flex;
    }
}
```

## 11.5. Device Pixel Ratio

```css
/* Retina displays */
@media (-webkit-min-device-pixel-ratio: 2),
       (min-resolution: 192dpi) {
    .logo {
        background-image: url('logo@2x.png');
    }
}

/* 3x displays */
@media (-webkit-min-device-pixel-ratio: 3),
       (min-resolution: 288dpi) {
    .logo {
        background-image: url('logo@3x.png');
    }
}
```

## 11.6. Aspect Ratio

```css
/* Widescreen */
@media (min-aspect-ratio: 16/9) {
    .video {
        width: 100%;
    }
}

/* Square-ish */
@media (aspect-ratio: 1/1) {
    .square-content {
        display: block;
    }
}
```

## 11.7. Logical Operators

```css
/* AND */
@media (min-width: 768px) and (max-width: 1024px) {
    /* Tablet only */
}

/* OR (comma) */
@media (max-width: 768px), (orientation: portrait) {
    /* Mobile OR portrait */
}

/* NOT */
@media not screen {
    /* Not screen devices */
}

@media not (min-width: 768px) {
    /* Less than 768px */
}

/* ONLY (legacy) */
@media only screen and (max-width: 768px) {
    /* Hide from old browsers */
}
```

## 11.8. Modern Media Features

### 11.8.1. prefers-color-scheme

```css
/* Light mode (default) */
:root {
    --bg-color: white;
    --text-color: black;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
    :root {
        --bg-color: #1a1a1a;
        --text-color: white;
    }
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
}
```

### 11.8.2. prefers-reduced-motion

```css
/* Default animations */
.box {
    transition: transform 0.3s ease;
}

/* Respect user preference */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

### 11.8.3. prefers-contrast

```css
@media (prefers-contrast: high) {
    .button {
        border: 2px solid black;
        font-weight: bold;
    }
}

@media (prefers-contrast: low) {
    .button {
        border: 1px solid #ccc;
    }
}
```

### 11.8.4. hover

```css
/* Touch devices (no hover) */
@media (hover: none) {
    .button {
        /* Always show active state */
        background-color: #3498db;
    }
}

/* Devices with hover */
@media (hover: hover) {
    .button:hover {
        background-color: #2980b9;
    }
}
```

### 11.8.5. pointer

```css
/* Fine pointer (mouse) */
@media (pointer: fine) {
    .clickable {
        cursor: pointer;
    }
}

/* Coarse pointer (touch) */
@media (pointer: coarse) {
    .button {
        min-height: 44px;  /* Larger touch targets */
        min-width: 44px;
    }
}
```

## 11.9. Responsive Typography

```css
/* Base font size */
html {
    font-size: 16px;
}

/* Tablet */
@media (min-width: 768px) {
    html {
        font-size: 18px;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    html {
        font-size: 20px;
    }
}

/* Fluid typography */
html {
    font-size: calc(16px + (24 - 16) * ((100vw - 320px) / (1920 - 320)));
}

/* Modern clamp */
html {
    font-size: clamp(16px, 2vw, 24px);
}
```

## 11.10. Responsive Images

```css
/* Basic responsive image */
img {
    max-width: 100%;
    height: auto;
}

/* Background images */
.hero {
    background-image: url('hero-mobile.jpg');
}

@media (min-width: 768px) {
    .hero {
        background-image: url('hero-tablet.jpg');
    }
}

@media (min-width: 1024px) {
    .hero {
        background-image: url('hero-desktop.jpg');
    }
}

/* Art direction with picture element */
```

```html
<picture>
    <source media="(min-width: 1024px)" srcset="large.jpg">
    <source media="(min-width: 768px)" srcset="medium.jpg">
    <img src="small.jpg" alt="Description">
</picture>
```

## 11.11. Container Queries

```css
/* Container */
.card-container {
    container-type: inline-size;
    container-name: card;
}

/* Query container */
@container card (min-width: 400px) {
    .card-title {
        font-size: 2rem;
    }
}

@container (min-width: 600px) {
    .card-layout {
        display: grid;
        grid-template-columns: 1fr 2fr;
    }
}
```

## 11.12. Practical Examples

### 11.12.1. Responsive Grid

```css
.grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
}

@media (min-width: 768px) {
    .grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1024px) {
    .grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

@media (min-width: 1440px) {
    .grid {
        grid-template-columns: repeat(4, 1fr);
    }
}
```

### 11.12.2. Responsive Navigation

```css
/* Mobile: Hamburger menu */
.nav-toggle {
    display: block;
}

.nav-menu {
    display: none;
    flex-direction: column;
}

.nav-menu.active {
    display: flex;
}

/* Desktop: Horizontal menu */
@media (min-width: 768px) {
    .nav-toggle {
        display: none;
    }

    .nav-menu {
        display: flex;
        flex-direction: row;
    }
}
```

### 11.12.3. Responsive Sidebar

```css
/* Mobile: Stack */
.layout {
    display: flex;
    flex-direction: column;
}

.sidebar {
    width: 100%;
}

/* Desktop: Side-by-side */
@media (min-width: 1024px) {
    .layout {
        flex-direction: row;
    }

    .sidebar {
        width: 300px;
        flex-shrink: 0;
    }

    .content {
        flex: 1;
    }
}
```

## 11.13. Common Breakpoints Reference

```css
/* Extra small (phones, 0px and up) */
@media (min-width: 0px) { }

/* Small (landscape phones, 576px and up) */
@media (min-width: 576px) { }

/* Medium (tablets, 768px and up) */
@media (min-width: 768px) { }

/* Large (desktops, 992px and up) */
@media (min-width: 992px) { }

/* Extra large (large desktops, 1200px and up) */
@media (min-width: 1200px) { }

/* Extra extra large (larger desktops, 1400px and up) */
@media (min-width: 1400px) { }
```

## 11.14. Print Styles

```css
@media print {
    /* Hide non-essential elements */
    nav, aside, footer {
        display: none;
    }

    /* Ensure readability */
    body {
        font-size: 12pt;
        color: black;
        background: white;
    }

    /* Page breaks */
    h1, h2, h3 {
        page-break-after: avoid;
    }

    /* Show link URLs */
    a::after {
        content: " (" attr(href) ")";
    }
}
```

---

**Kết luận:** Media queries là foundation của responsive design. Combine với flexible layouts (Flexbox, Grid) để tạo responsive websites. Always test trên real devices.

**Chương tiếp theo:** Advanced CSS3 Topics


## 11.10. Practical Examples - Extended

### 11.10.1. Responsive Grid System

Custom grid breakpoints

```css
.grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
}

@media (min-width: 576px) {
    .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 768px) {
    .grid { grid-template-columns: repeat(3, 1fr); }
}

@media (min-width: 992px) {
    .grid { grid-template-columns: repeat(4, 1fr); }
}

@media (min-width: 1200px) {
    .grid { grid-template-columns: repeat(6, 1fr); }
}
```

### 11.10.2. Dark Mode Implementation

System preference detection

```css
:root {
    --bg: white;
    --text: #333;
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg: #1a1a1a;
        --text: #f0f0f0;
    }
}

body {
    background: var(--bg);
    color: var(--text);
    transition: background 0.3s, color 0.3s;
}
```


## 11.11. Real-World Use Cases

### 11.11.1. Mobile-First Design

Progressive enhancement

```css
/* Implementation details */
```

### 11.11.2. Print Stylesheets

Optimized print layouts

```css
/* Implementation details */
```

### 11.11.3. Touch Device Optimization

Larger hit areas for touch

```css
/* Implementation details */
```

### 11.11.4. High-DPI Displays

Retina image serving

```css
/* Implementation details */
```

### 11.11.5. Accessibility Features

Reduced motion support

```css
/* Implementation details */
```


## 11.12. Tips & Tricks

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

## 11.13. Common Mistakes

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

## 11.14. Troubleshooting

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

## 11.15. Advanced Topics

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

## 11.16. Bài Tập

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

**Chương tiếp theo:** Advanced Topics


## 11.20. Advanced Responsive Techniques

### 11.20.1. Container Queries
```css
.card-container {
    container-type: inline-size;
    container-name: card;
}

@container card (min-width: 400px) {
    .card {
        display: grid;
        grid-template-columns: 200px 1fr;
    }
}

@container card (min-width: 600px) {
    .card {
        grid-template-columns: 250px 1fr 200px;
    }
}
```

### 11.20.2. Fluid Typography System
```css
:root {
    --fluid-min-width: 320;
    --fluid-max-width: 1140;
    --fluid-min-size: 16;
    --fluid-max-size: 24;
}

html {
    font-size: calc(
        (var(--fluid-min-size) * 1px) +
        (var(--fluid-max-size) - var(--fluid-min-size)) *
        ((100vw - (var(--fluid-min-width) * 1px)) /
        (var(--fluid-max-width) - var(--fluid-min-width)))
    );
}

@media (max-width: 320px) {
    html {
        font-size: calc(var(--fluid-min-size) * 1px);
    }
}

@media (min-width: 1140px) {
    html {
        font-size: calc(var(--fluid-max-size) * 1px);
    }
}
```

### 11.20.3. Responsive Images with Art Direction
```html
<picture>
    <source media="(min-width: 1200px)" srcset="image-large.jpg">
    <source media="(min-width: 768px)" srcset="image-medium.jpg">
    <source media="(min-width: 320px)" srcset="image-small.jpg">
    <img src="image-fallback.jpg" alt="Description">
</picture>
```

```css
.responsive-image {
    width: 100%;
    height: auto;
    object-fit: cover;
}
```

### 11.20.4. Responsive Navigation Patterns
```css
/* Mobile hamburger menu */
.nav {
    display: none;
    flex-direction: column;
}

.nav-toggle {
    display: block;
}

.nav.active {
    display: flex;
}

/* Desktop horizontal menu */
@media (min-width: 768px) {
    .nav {
        display: flex;
        flex-direction: row;
    }

    .nav-toggle {
        display: none;
    }
}
```

### 11.20.5. Responsive Grid System
```css
.grid {
    display: grid;
    gap: 20px;
    grid-template-columns: repeat(12, 1fr);
}

.col-1 { grid-column: span 1; }
.col-2 { grid-column: span 2; }
.col-3 { grid-column: span 3; }
/* ... up to col-12 */

@media (max-width: 768px) {
    .col-sm-12 { grid-column: span 12; }
    .col-sm-6 { grid-column: span 6; }
}

@media (min-width: 769px) and (max-width: 1024px) {
    .col-md-6 { grid-column: span 6; }
    .col-md-4 { grid-column: span 4; }
}
```

### 11.20.6. Responsive Typography Scale
```css
:root {
    --scale: 1.2;
}

@media (min-width: 768px) {
    :root { --scale: 1.25; }
}

@media (min-width: 1024px) {
    :root { --scale: 1.333; }
}

h1 {
    font-size: calc(1rem * var(--scale) * var(--scale) * var(--scale));
}

h2 {
    font-size: calc(1rem * var(--scale) * var(--scale));
}

h3 {
    font-size: calc(1rem * var(--scale));
}
```

### 11.20.7. Print Stylesheet Optimization
```css
@media print {
    * {
        background: transparent !important;
        color: black !important;
        box-shadow: none !important;
        text-shadow: none !important;
    }

    @page {
        margin: 2cm;
    }

    h2, h3, p {
        orphans: 3;
        widows: 3;
    }

    h2, h3 {
        page-break-after: avoid;
    }

    a[href]::after {
        content: " (" attr(href) ")";
    }

    nav, video, audio, object, embed {
        display: none;
    }
}
```

### 11.20.8. Responsive Spacing System
```css
:root {
    --spacing-xs: clamp(0.5rem, 1vw, 0.75rem);
    --spacing-sm: clamp(0.75rem, 2vw, 1rem);
    --spacing-md: clamp(1rem, 3vw, 1.5rem);
    --spacing-lg: clamp(1.5rem, 4vw, 2rem);
    --spacing-xl: clamp(2rem, 6vw, 3rem);
}

.section {
    padding: var(--spacing-lg) var(--spacing-md);
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
