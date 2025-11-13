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


## 12.10. Practical Examples - Extended

### 12.10.1. CSS Houdini Paint API

Custom paint worklet

```javascript
// paint-worklet.js
registerPaint('circles', class {
    static get inputProperties() {
        return ['--circle-color'];
    }

    paint(ctx, size, props) {
        const color = props.get('--circle-color').toString();
        ctx.fillStyle = color;
        ctx.fillRect(0, 0, size.width, size.height);

        for(let i = 0; i < 10; i++) {
            ctx.beginPath();
            ctx.arc(
                Math.random() * size.width,
                Math.random() * size.height,
                30, 0, 2 * Math.PI
            );
            ctx.fill();
        }
    }
});
```

```css
.box {
    --circle-color: #3498db;
    background: paint(circles);
}
```

### 12.10.2. Container Queries

Element-based responsive design

```css
.card-container {
    container-type: inline-size;
    container-name: card;
}

@container card (min-width: 400px) {
    .card {
        display: grid;
        grid-template-columns: 1fr 2fr;
    }
}

@container card (min-width: 600px) {
    .card {
        grid-template-columns: 1fr 1fr 2fr;
    }
}
```


## 12.11. Real-World Use Cases

### 12.11.1. Design Systems

Scalable component libraries

```css
/* Implementation details */
```

### 12.11.2. Micro-interactions

Delightful user interactions

```css
/* Implementation details */
```

### 12.11.3. Performance Optimization

CSS containment strategies

```css
/* Implementation details */
```

### 12.11.4. Advanced Animations

Complex keyframe sequences

```css
/* Implementation details */
```

### 12.11.5. CSS Architecture

Maintainable large-scale CSS

```css
/* Implementation details */
```


## 12.12. Tips & Tricks

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

## 12.13. Common Mistakes

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

## 12.14. Troubleshooting

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

## 12.15. Advanced Topics

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

## 12.16. Bài Tập

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

**Chương tiếp theo:** End


## 12.20. Cutting-Edge CSS Features

### 12.20.1. CSS Layers (@layer)
```css
@layer reset, base, components, utilities;

@layer reset {
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
}

@layer base {
    body {
        font-family: system-ui;
        line-height: 1.5;
    }
}

@layer components {
    .button {
        padding: 10px 20px;
        background: blue;
        color: white;
    }
}

@layer utilities {
    .text-center {
        text-align: center;
    }
}
```

### 12.20.2. Scroll-Driven Animations
```css
@keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
}

.scroll-animate {
    animation: fade-in linear;
    animation-timeline: scroll();
    animation-range: entry 0% cover 50%;
}
```

### 12.20.3. View Transitions API
```css
::view-transition-old(root),
::view-transition-new(root) {
    animation-duration: 0.5s;
}

::view-transition-old(header) {
    animation: slide-out 0.3s ease-out;
}

::view-transition-new(header) {
    animation: slide-in 0.3s ease-in;
}

@keyframes slide-out {
    to { transform: translateX(-100%); }
}

@keyframes slide-in {
    from { transform: translateX(100%); }
}
```

### 12.20.4. Nesting (Future)
```css
.card {
    padding: 20px;

    & .title {
        font-size: 1.5rem;
        font-weight: bold;
    }

    & .content {
        margin-top: 10px;

        & p {
            margin-bottom: 10px;
        }
    }

    &:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
}
```

### 12.20.5. CSS Scoping
```css
@scope (.card) {
    .title {
        font-size: 1.5rem;
    }

    .content {
        padding: 10px;
    }
}

/* These styles only apply inside .card */
```

### 12.20.6. Color Functions (Future)
```css
.box {
    /* Relative colors */
    --base: #3498db;
    --lighter: color-mix(in srgb, var(--base) 80%, white);
    --darker: color-mix(in srgb, var(--base) 80%, black);

    /* Color contrast */
    color: color-contrast(var(--base) vs white, black);

    /* Color modification */
    background: hwb(from var(--base) h w calc(b * 0.8));
}
```

### 12.20.7. Anchor Positioning
```css
.tooltip {
    position: anchor;
    anchor-name: --my-anchor;
    position-anchor: --my-anchor;
    inset-area: top;
}
```

### 12.20.8. Container Style Queries
```css
.card-container {
    container-type: inline-size;
    container-name: card;
}

@container card style(--theme: dark) {
    .card {
        background: #333;
        color: white;
    }
}
```

### 12.20.9. :has() Pseudo-class Applications
```css
/* Parent selector based on children */
.form:has(:invalid) {
    border: 2px solid red;
}

.card:has(img) {
    display: grid;
    grid-template-columns: 200px 1fr;
}

/* Sibling combinations */
h2:has(+ p) {
    margin-bottom: 0.5rem;
}

/* State-based styling */
.menu:has(.submenu:hover) {
    background: #f0f0f0;
}
```

### 12.20.10. Trigonometric Functions
```css
.element {
    /* Use sin, cos, tan for circular layouts */
    --angle: 45deg;
    transform: rotate(var(--angle));
    left: calc(50% + 100px * cos(var(--angle)));
    top: calc(50% + 100px * sin(var(--angle)));
}

/* Circular navigation */
.nav-item:nth-child(1) {
    --angle: calc(360deg / 8 * 0);
    transform: rotate(var(--angle)) translateX(150px) rotate(calc(-1 * var(--angle)));
}
```

## 12.21. CSS Architecture Best Practices

### 12.21.1. BEM Methodology
```css
/* Block */
.button {}

/* Element */
.button__icon {}
.button__text {}

/* Modifier */
.button--primary {}
.button--large {}

/* Combined */
.button--primary .button__icon {}
```

### 12.21.2. ITCSS Structure
```
settings/
tools/
generic/
elements/
objects/
components/
utilities/
```

### 12.21.3. Component-Based CSS
```css
/* Component root */
.c-card {
    display: flex;
    flex-direction: column;
}

/* Component parts */
.c-card__header {}
.c-card__body {}
.c-card__footer {}

/* Component modifiers */
.c-card--featured {}
.c-card--horizontal {}
```

### 12.21.4. Utility-First CSS
```css
/* Spacing utilities */
.p-4 { padding: 1rem; }
.m-2 { margin: 0.5rem; }

/* Flexbox utilities */
.flex { display: flex; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }

/* Responsive utilities */
@media (min-width: 768px) {
    .md\:grid { display: grid; }
    .md\:col-2 { grid-template-columns: repeat(2, 1fr); }
}
```

### 12.21.5. CSS Custom Property Patterns
```css
/* Design tokens */
:root {
    /* Colors */
    --color-primary-50: #e3f2fd;
    --color-primary-500: #2196f3;
    --color-primary-900: #0d47a1;

    /* Spacing scale */
    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-4: 1rem;
    --space-8: 2rem;

    /* Typography */
    --font-size-sm: 0.875rem;
    --font-size-base: 1rem;
    --font-size-lg: 1.125rem;
}

/* Theme variations */
[data-theme="dark"] {
    --color-bg: var(--color-primary-900);
    --color-text: var(--color-primary-50);
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
