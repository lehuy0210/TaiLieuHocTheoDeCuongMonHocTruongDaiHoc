# CHƯƠNG 5: TYPOGRAPHY & FONTS

## 5.1. Web Fonts

### 5.1.1. @font-face

```css
@font-face {
    font-family: 'MyFont';
    src: url('myfont.woff2') format('woff2'),
         url('myfont.woff') format('woff');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}

.text {
    font-family: 'MyFont', sans-serif;
}
```

### 5.1.2. Google Fonts

```html
<!-- In HTML -->
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
```

```css
/* In CSS */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
}
```

### 5.1.3. font-display

```css
@font-face {
    font-family: 'MyFont';
    src: url('font.woff2');
    font-display: swap;      /* Recommended */
    font-display: block;     /* Wait for font */
    font-display: fallback;  /* Short block, swap */
    font-display: optional;  /* Use only if cached */
}
```

## 5.2. Font Properties

### 5.2.1. font-family

```css
.text {
    /* Web fonts */
    font-family: 'Roboto', sans-serif;

    /* System fonts */
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;

    /* Generic families */
    font-family: serif;
    font-family: sans-serif;
    font-family: monospace;
    font-family: cursive;
    font-family: fantasy;
}

/* System font stack */
body {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
}
```

### 5.2.2. font-size

```css
.text {
    /* Absolute */
    font-size: 16px;
    font-size: 12pt;

    /* Relative */
    font-size: 1.2em;    /* Relative to parent */
    font-size: 1.2rem;   /* Relative to root */

    /* Viewport units */
    font-size: 5vw;

    /* Keywords */
    font-size: small;
    font-size: medium;
    font-size: large;
    font-size: larger;
    font-size: smaller;
}

/* Responsive typography */
html {
    font-size: 16px;
}

h1 {
    font-size: 2.5rem;  /* 40px */
}

p {
    font-size: 1rem;    /* 16px */
}

small {
    font-size: 0.875rem; /* 14px */
}
```

### 5.2.3. font-weight

```css
.text {
    font-weight: normal;   /* 400 */
    font-weight: bold;     /* 700 */
    font-weight: lighter;
    font-weight: bolder;

    /* Numeric values */
    font-weight: 100;  /* Thin */
    font-weight: 200;  /* Extra Light */
    font-weight: 300;  /* Light */
    font-weight: 400;  /* Normal */
    font-weight: 500;  /* Medium */
    font-weight: 600;  /* Semi Bold */
    font-weight: 700;  /* Bold */
    font-weight: 800;  /* Extra Bold */
    font-weight: 900;  /* Black */
}
```

### 5.2.4. font-style

```css
.text {
    font-style: normal;
    font-style: italic;
    font-style: oblique;
    font-style: oblique 10deg;
}
```

### 5.2.5. font Shorthand

```css
.text {
    /* font: style weight size/line-height family */
    font: italic bold 16px/1.5 'Arial', sans-serif;
    font: 1rem/1.6 system-ui, sans-serif;
}
```

## 5.3. Text Properties

### 5.3.1. color

```css
.text {
    color: #333;
    color: rgb(51, 51, 51);
    color: rgba(0, 0, 0, 0.8);
    color: hsl(0, 0%, 20%);
    color: currentColor;  /* Inherit from parent */
}
```

### 5.3.2. text-align

```css
.text {
    text-align: left;
    text-align: right;
    text-align: center;
    text-align: justify;
    text-align: start;   /* Same as left in LTR */
    text-align: end;     /* Same as right in LTR */
}
```

### 5.3.3. text-decoration

```css
.text {
    text-decoration: underline;
    text-decoration: overline;
    text-decoration: line-through;
    text-decoration: none;

    /* Detailed */
    text-decoration-line: underline;
    text-decoration-color: red;
    text-decoration-style: solid;
    text-decoration-style: wavy;
    text-decoration-style: dashed;
    text-decoration-style: dotted;
    text-decoration-thickness: 2px;

    /* Shorthand */
    text-decoration: underline wavy red 2px;
}

/* Link styles */
a {
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```

### 5.3.4. text-transform

```css
.text {
    text-transform: uppercase;   /* ALL CAPS */
    text-transform: lowercase;   /* all lowercase */
    text-transform: capitalize;  /* First Letter */
    text-transform: none;
}
```

### 5.3.5. text-shadow

```css
.text {
    /* x-offset | y-offset | blur | color */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

/* Multiple shadows */
.text {
    text-shadow:
        2px 2px 0 white,
        4px 4px 0 #333;
}

/* Glow effect */
.glow {
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
}

/* 3D effect */
.three-d {
    text-shadow:
        1px 1px 0 #ccc,
        2px 2px 0 #c9c9c9,
        3px 3px 0 #bbb,
        4px 4px 0 #b9b9b9,
        5px 5px 0 #aaa,
        6px 6px 10px rgba(0, 0, 0, 0.5);
}
```

## 5.4. Line and Letter Spacing

### 5.4.1. line-height

```css
.text {
    line-height: 1.6;      /* Recommended for body text */
    line-height: 24px;
    line-height: 1.5em;
    line-height: 150%;
}

/* Good for readability */
body {
    font-size: 16px;
    line-height: 1.6;  /* 25.6px */
}

h1 {
    line-height: 1.2;  /* Tighter for headings */
}
```

### 5.4.2. letter-spacing

```css
.text {
    letter-spacing: 0.05em;
    letter-spacing: 2px;
    letter-spacing: -1px;  /* Tighter */
}

/* Headings */
h1 {
    letter-spacing: -0.02em;  /* Slightly tighter */
}

/* All caps */
.uppercase {
    text-transform: uppercase;
    letter-spacing: 0.1em;  /* More spacing */
}
```

### 5.4.3. word-spacing

```css
.text {
    word-spacing: 5px;
    word-spacing: 0.3em;
}
```

## 5.5. Text Overflow and Wrapping

### 5.5.1. white-space

```css
.text {
    white-space: normal;    /* Default */
    white-space: nowrap;    /* No wrapping */
    white-space: pre;       /* Preserve spaces & newlines */
    white-space: pre-wrap;  /* Preserve & wrap */
    white-space: pre-line;  /* Collapse spaces, preserve newlines */
}
```

### 5.5.2. text-overflow

```css
/* Ellipsis (must have nowrap and overflow) */
.truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Clip */
.text {
    text-overflow: clip;
}
```

### 5.5.3. word-break

```css
.text {
    word-break: normal;
    word-break: break-all;    /* Break anywhere */
    word-break: keep-all;     /* Don't break words */
}
```

### 5.5.4. word-wrap / overflow-wrap

```css
.text {
    overflow-wrap: normal;
    overflow-wrap: break-word;  /* Break long words */
    overflow-wrap: anywhere;
}
```

### 5.5.5. hyphens

```css
.text {
    hyphens: none;
    hyphens: manual;  /* Use &shy; in HTML */
    hyphens: auto;    /* Automatic hyphenation */
}
```

## 5.6. Advanced Typography

### 5.6.1. text-indent

```css
p {
    text-indent: 2em;  /* First line indent */
}

/* Hanging indent */
.hanging {
    padding-left: 2em;
    text-indent: -2em;
}
```

### 5.6.2. direction and writing-mode

```css
.rtl {
    direction: rtl;  /* Right to left */
}

.vertical {
    writing-mode: vertical-rl;  /* Vertical right to left */
    writing-mode: vertical-lr;  /* Vertical left to right */
}
```

### 5.6.3. Font Variants

```css
.text {
    font-variant: small-caps;
    font-variant-caps: small-caps;
    font-variant-numeric: tabular-nums;
    font-variant-ligatures: common-ligatures;
}
```

### 5.6.4. Variable Fonts

```css
@font-face {
    font-family: 'Variable';
    src: url('variable-font.woff2') format('woff2-variations');
    font-weight: 100 900;  /* Range */
}

.text {
    font-family: 'Variable';
    font-weight: 450;  /* Any value in range */
    font-variation-settings: 'wght' 450, 'wdth' 100;
}
```

## 5.7. Practical Examples

### 5.7.1. Responsive Typography

```css
html {
    font-size: 16px;
}

@media (min-width: 768px) {
    html {
        font-size: 18px;
    }
}

/* Fluid typography */
html {
    font-size: calc(16px + (24 - 16) * ((100vw - 320px) / (1920 - 320)));
}

/* Clamp (modern) */
html {
    font-size: clamp(16px, 2vw, 24px);
}
```

### 5.7.2. Readable Text

```css
.article {
    max-width: 65ch;  /* Optimal line length */
    font-size: 18px;
    line-height: 1.6;
    color: #333;
}

.article h1 {
    font-size: 2.5em;
    line-height: 1.2;
    margin-bottom: 0.5em;
}

.article p {
    margin-bottom: 1.5em;
}
```

### 5.7.3. Multiline Truncation

```css
.truncate-lines {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}
```

---

**Kết luận:** Typography là key để tạo readable và beautiful text. Font loading, spacing, và responsive typography là important considerations.

**Chương tiếp theo:** Flexbox


## 5.10. Practical Examples - Extended

### 5.10.1. Font Loading Strategy

Load fonts efficiently

```css
@font-face {
    font-family: 'CustomFont';
    src: url('font.woff2') format('woff2');
    font-display: swap;
    font-weight: 400;
}

/* Preload critical fonts */
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>

/* Font loading API */
document.fonts.load('1em CustomFont').then(() => {
    document.body.classList.add('fonts-loaded');
});
```

### 5.10.2. Responsive Typography System

Fluid typography with clamp

```css
:root {
    --font-size-sm: clamp(0.875rem, 0.8rem + 0.375vw, 1rem);
    --font-size-base: clamp(1rem, 0.9rem + 0.5vw, 1.25rem);
    --font-size-lg: clamp(1.25rem, 1.1rem + 0.75vw, 1.75rem);
    --font-size-xl: clamp(1.75rem, 1.5rem + 1.25vw, 2.5rem);
    --font-size-xxl: clamp(2.5rem, 2rem + 2.5vw, 4rem);
}

body {
    font-size: var(--font-size-base);
}

h1 { font-size: var(--font-size-xxl); }
h2 { font-size: var(--font-size-xl); }
h3 { font-size: var(--font-size-lg); }
```

### 5.10.3. Drop Caps Effect

Magazine-style drop caps

```css
.article p:first-of-type::first-letter {
    font-size: 3.5em;
    font-weight: bold;
    line-height: 0.9;
    float: left;
    margin: 0.1em 0.1em 0 0;
    color: #3498db;
}
```

### 5.10.4. Text Stroke and Fill

Outlined text effect

```css
.outlined-text {
    font-size: 4rem;
    font-weight: bold;
    color: transparent;
    -webkit-text-stroke: 2px #3498db;
    text-stroke: 2px #3498db;
}
```

### 5.10.5. Variable Font Animations

Animate font variations

```css
@font-face {
    font-family: 'VariableFont';
    src: url('variable.woff2') format('woff2-variations');
    font-weight: 100 900;
}

.animated-text {
    font-family: 'VariableFont';
    animation: weight 3s ease-in-out infinite;
}

@keyframes weight {
    0%, 100% { font-variation-settings: 'wght' 400; }
    50% { font-variation-settings: 'wght' 900; }
}
```


## 5.11. Real-World Use Cases

### 5.11.1. Blog Article Layout

Optimized reading experience for long-form content

```css
/* Implementation details */
```

### 5.11.2. Pricing Tables

Clear hierarchy with typography

```css
/* Implementation details */
```

### 5.11.3. Hero Headlines

Attention-grabbing large text

```css
/* Implementation details */
```

### 5.11.4. Form Labels and Inputs

Accessible form typography

```css
/* Implementation details */
```

### 5.11.5. Code Documentation

Monospace font usage

```css
/* Implementation details */
```


## 5.12. Tips & Tricks

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

## 5.13. Common Mistakes

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

## 5.14. Troubleshooting

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

## 5.15. Advanced Topics

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

## 5.16. Bài Tập

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

**Chương tiếp theo:** Flexbox


## 5.20. Advanced Typography Techniques

### 5.20.1. OpenType Features
```css
.text {
    font-feature-settings: "liga" 1, "kern" 1;
    font-variant-ligatures: common-ligatures;
    font-variant-numeric: tabular-nums;
}

/* Enable all OpenType features */
.fancy-text {
    font-feature-settings:
        "swsh" 1,  /* Swashes */
        "calt" 1,  /* Contextual alternates */
        "dlig" 1,  /* Discretionary ligatures */
        "ss01" 1;  /* Stylistic set 1 */
}
```

### 5.20.2. Text Rendering Optimization
```css
body {
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
```

### 5.20.3. Multi-Column Text Layouts
```css
.article-columns {
    column-count: 3;
    column-gap: 40px;
    column-rule: 1px solid #ddd;
}

/* Column breaks */
.section-break {
    break-after: column;
}

.avoid-break {
    break-inside: avoid;
}
```

### 5.20.4. Hyphenation and Justification
```css
.justified-text {
    text-align: justify;
    hyphens: auto;
    hyphenate-limit-chars: 6 3 2;
    hyphenate-limit-lines: 2;
}
```

### 5.20.5. Advanced Text Effects
```css
.neon-text {
    color: #fff;
    text-shadow:
        0 0 7px #fff,
        0 0 10px #fff,
        0 0 21px #fff,
        0 0 42px #0fa,
        0 0 82px #0fa,
        0 0 92px #0fa,
        0 0 102px #0fa,
        0 0 151px #0fa;
}

.embossed-text {
    color: #333;
    background: #ddd;
    text-shadow: -1px -1px 0 rgba(255,255,255,.7), 1px 1px 0 rgba(0,0,0,.3);
}

.engraved-text {
    color: #ccc;
    text-shadow: 0px 1px 1px rgba(255,255,255,.3), 0px -1px 1px rgba(0,0,0,.7);
}
```

### 5.20.6. Font Loading Strategies
```javascript
// Use Font Loading API
if ('fonts' in document) {
    Promise.all([
        document.fonts.load('1em "Open Sans"'),
        document.fonts.load('700 1em "Open Sans"'),
        document.fonts.load('italic 1em "Open Sans"')
    ]).then(() => {
        document.documentElement.classList.add('fonts-loaded');
    });
}
```

```css
/* FOUT prevention */
.wf-loading {
    opacity: 0;
}

.wf-active,
.wf-inactive,
.fonts-loaded {
    opacity: 1;
    transition: opacity 0.3s;
}
```

### 5.20.7. Responsive Font Sizing with CSS Locks
```css
/* Font size scales between 16px and 24px */
html {
    font-size: 16px;
}

@media screen and (min-width: 320px) {
    html {
        font-size: calc(16px + 8 * ((100vw - 320px) / 680));
    }
}

@media screen and (min-width: 1000px) {
    html {
        font-size: 24px;
    }
}
```

### 5.20.8. Vertical Rhythm System
```css
:root {
    --base-font-size: 16px;
    --base-line-height: 1.5;
    --rhythm-unit: calc(var(--base-font-size) * var(--base-line-height));
}

p {
    margin-bottom: var(--rhythm-unit);
}

h1 {
    font-size: calc(var(--base-font-size) * 2.5);
    line-height: calc(var(--rhythm-unit) * 2);
    margin-bottom: var(--rhythm-unit);
}
```

### 5.20.9. Text Balancing (Future)
```css
.balanced-headline {
    text-wrap: balance; /* Future CSS */
    max-width: 50ch;
}
```

### 5.20.10. Font Subsetting
```css
/* Only load Latin characters */
@font-face {
    font-family: 'Custom Font';
    src: url('font-latin.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153;
}

/* Cyrillic subset */
@font-face {
    font-family: 'Custom Font';
    src: url('font-cyrillic.woff2') format('woff2');
    unicode-range: U+0400-045F, U+0490-0491, U+04B0-04B1;
}
```

## 5.30. Complete Typography System Implementation

### 5.30.1. Professional Type Scale
```css
:root {
    /* Base */
    --font-size-base: 1rem; /* 16px */

    /* Type scale (1.25 - Major Third) */
    --font-size-xs: calc(var(--font-size-base) * 0.64);   /* 10.24px */
    --font-size-sm: calc(var(--font-size-base) * 0.8);    /* 12.8px */
    --font-size-md: var(--font-size-base);                /* 16px */
    --font-size-lg: calc(var(--font-size-base) * 1.25);   /* 20px */
    --font-size-xl: calc(var(--font-size-base) * 1.563);  /* 25px */
    --font-size-2xl: calc(var(--font-size-base) * 1.953); /* 31.25px */
    --font-size-3xl: calc(var(--font-size-base) * 2.441); /* 39.06px */
    --font-size-4xl: calc(var(--font-size-base) * 3.052); /* 48.83px */

    /* Line heights */
    --line-height-tight: 1.2;
    --line-height-normal: 1.5;
    --line-height-relaxed: 1.75;

    /* Letter spacing */
    --letter-spacing-tight: -0.05em;
    --letter-spacing-normal: 0;
    --letter-spacing-wide: 0.05em;
}

/* Apply type scale */
.text-xs { font-size: var(--font-size-xs); }
.text-sm { font-size: var(--font-size-sm); }
.text-md { font-size: var(--font-size-md); }
.text-lg { font-size: var(--font-size-lg); }
.text-xl { font-size: var(--font-size-xl); }
.text-2xl { font-size: var(--font-size-2xl); }
.text-3xl { font-size: var(--font-size-3xl); }
.text-4xl { font-size: var(--font-size-4xl); }
```

### 5.30.2. Complete Font Stack System
```css
/* Serif fonts */
.font-serif {
    font-family: Georgia, Cambria, "Times New Roman", Times, serif;
}

/* Sans-serif fonts */
.font-sans {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* Monospace fonts */
.font-mono {
    font-family: Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

/* Display fonts (for headings) */
.font-display {
    font-family: "Inter Display", -apple-system, BlinkMacSystemFont, sans-serif;
    font-feature-settings: "ss01", "ss02", "cv05", "cv10";
}

/* System UI fonts (native look) */
.font-system {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
```

### 5.30.3. Reading Experience Optimization
```css
.article-content {
    /* Optimal line length */
    max-width: 65ch;
    margin: 0 auto;

    /* Comfortable reading */
    font-size: 18px;
    line-height: 1.6;
    color: #333;

    /* Improved readability */
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    /* Better word breaks */
    hyphens: auto;
    word-break: break-word;
    overflow-wrap: break-word;
}

.article-content h1,
.article-content h2,
.article-content h3 {
    font-weight: 700;
    line-height: 1.2;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}

.article-content p {
    margin-bottom: 1.25em;
}

.article-content p:first-child::first-letter {
    font-size: 3.5em;
    float: left;
    line-height: 0.85;
    margin: 0.1em 0.1em 0 0;
    font-weight: bold;
}
```

### 5.30.4. Responsive Typography Matrix
```css
/* Mobile */
@media (max-width: 640px) {
    :root {
        --font-size-base: 16px;
        --font-size-4xl: 32px;
    }

    body {
        font-size: var(--font-size-base);
    }

    h1 { font-size: var(--font-size-4xl); }
    h2 { font-size: var(--font-size-3xl); }
    h3 { font-size: var(--font-size-2xl); }
}

/* Tablet */
@media (min-width: 641px) and (max-width: 1024px) {
    :root {
        --font-size-base: 17px;
        --font-size-4xl: 40px;
    }
}

/* Desktop */
@media (min-width: 1025px) {
    :root {
        --font-size-base: 18px;
        --font-size-4xl: 48px;
    }
}

/* Large screens */
@media (min-width: 1440px) {
    :root {
        --font-size-base: 20px;
        --font-size-4xl: 56px;
    }
}
```

### 5.30.5. Advanced Text Effects Library
```css
/* Gradient text */
.text-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* 3D text effect */
.text-3d {
    text-shadow:
        1px 1px 0 #ccc,
        2px 2px 0 #c9c9c9,
        3px 3px 0 #bbb,
        4px 4px 0 #b9b9b9,
        5px 5px 0 #aaa,
        6px 6px 1px rgba(0,0,0,.1),
        0 0 5px rgba(0,0,0,.1),
        1px 3px 3px rgba(0,0,0,.3),
        3px 5px 5px rgba(0,0,0,.2),
        5px 10px 10px rgba(0,0,0,.25),
        10px 20px 20px rgba(0,0,0,.2);
}

/* Neon text glow */
.text-neon {
    color: #fff;
    text-shadow:
        0 0 7px #fff,
        0 0 10px #fff,
        0 0 21px #fff,
        0 0 42px #0fa,
        0 0 82px #0fa,
        0 0 92px #0fa,
        0 0 102px #0fa,
        0 0 151px #0fa;
    animation: neon-flicker 1.5s infinite alternate;
}

@keyframes neon-flicker {
    0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
        text-shadow:
            0 0 7px #fff,
            0 0 10px #fff,
            0 0 21px #fff,
            0 0 42px #0fa,
            0 0 82px #0fa,
            0 0 92px #0fa,
            0 0 102px #0fa,
            0 0 151px #0fa;
    }
    20%, 24%, 55% {
        text-shadow: none;
    }
}

/* Outline text */
.text-outline {
    color: transparent;
    -webkit-text-stroke: 2px #000;
    text-stroke: 2px #000;
}

/* Shadow text */
.text-shadow-soft {
    text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
}

.text-shadow-hard {
    text-shadow: 4px 4px 0 rgba(0,0,0,0.2);
}

/* Retro text */
.text-retro {
    font-weight: 900;
    text-transform: uppercase;
    background: linear-gradient(180deg, #ffd700 0%, #ff6347 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow:
        3px 3px 0 #ff6347,
        6px 6px 0 #ffa500,
        9px 9px 0 #ffd700;
}
```

### 5.30.6. Typography Utility Classes
```css
/* Weight */
.font-thin { font-weight: 100; }
.font-light { font-weight: 300; }
.font-normal { font-weight: 400; }
.font-medium { font-weight: 500; }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: 700; }
.font-extrabold { font-weight: 800; }
.font-black { font-weight: 900; }

/* Style */
.italic { font-style: italic; }
.not-italic { font-style: normal; }

/* Alignment */
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-justify { text-align: justify; }

/* Transform */
.uppercase { text-transform: uppercase; }
.lowercase { text-transform: lowercase; }
.capitalize { text-transform: capitalize; }
.normal-case { text-transform: none; }

/* Decoration */
.underline { text-decoration: underline; }
.line-through { text-decoration: line-through; }
.no-underline { text-decoration: none; }

/* Overflow */
.truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Whitespace */
.whitespace-normal { white-space: normal; }
.whitespace-nowrap { white-space: nowrap; }
.whitespace-pre { white-space: pre; }
.whitespace-pre-line { white-space: pre-line; }
.whitespace-pre-wrap { white-space: pre-wrap; }

/* Break */
.break-normal { word-break: normal; overflow-wrap: normal; }
.break-words { overflow-wrap: break-word; }
.break-all { word-break: break-all; }
```

---

**Kết luận hoàn chỉnh:** Typography là foundation của web design. Một type system tốt không chỉ làm cho content dễ đọc mà còn tạo ra visual hierarchy mạnh mẽ, enhance user experience, và strengthen brand identity. Nắm vững các principles về font loading, responsive typography, và advanced text effects sẽ giúp bạn tạo ra những website professional và accessible.

**Chương tiếp theo:** Flexbox
