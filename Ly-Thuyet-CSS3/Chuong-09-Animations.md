# CHƯƠNG 9: CSS3 ANIMATIONS

## 9.1. Giới thiệu Animations

CSS Animations cho phép tạo complex animations bằng @keyframes.

### 9.1.1. Basic Animation

```css
/* Define keyframes */
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* Apply animation */
.box {
    animation: fadeIn 1s ease;
}
```

## 9.2. @keyframes

### 9.2.1. Percentage Keyframes

```css
@keyframes slide {
    0% {
        transform: translateX(0);
    }
    50% {
        transform: translateX(100px);
    }
    100% {
        transform: translateX(200px);
    }
}
```

### 9.2.2. Multiple Properties

```css
@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
        opacity: 1;
    }
    50% {
        transform: translateY(-20px);
        opacity: 0.7;
    }
}
```

### 9.2.3. From and To

```css
@keyframes grow {
    from {
        transform: scale(0);
    }
    to {
        transform: scale(1);
    }
}
```

## 9.3. Animation Properties

### 9.3.1. animation-name

```css
.box {
    animation-name: fadeIn;
    animation-name: slideLeft, fadeIn;  /* Multiple animations */
}
```

### 9.3.2. animation-duration

```css
.box {
    animation-duration: 2s;
    animation-duration: 500ms;
    animation-duration: 1s, 2s;  /* For multiple animations */
}
```

### 9.3.3. animation-timing-function

```css
.box {
    animation-timing-function: ease;
    animation-timing-function: linear;
    animation-timing-function: ease-in;
    animation-timing-function: ease-out;
    animation-timing-function: ease-in-out;
    animation-timing-function: cubic-bezier(0.42, 0, 0.58, 1);
    animation-timing-function: steps(4, end);
}
```

### 9.3.4. animation-delay

```css
.box {
    animation-delay: 0.5s;
    animation-delay: -0.5s;  /* Start halfway through */
}
```

### 9.3.5. animation-iteration-count

```css
.box {
    animation-iteration-count: 1;        /* Once */
    animation-iteration-count: 3;        /* 3 times */
    animation-iteration-count: infinite; /* Forever */
}
```

### 9.3.6. animation-direction

```css
.box {
    animation-direction: normal;            /* 0% → 100% */
    animation-direction: reverse;           /* 100% → 0% */
    animation-direction: alternate;         /* 0% → 100% → 0% ... */
    animation-direction: alternate-reverse; /* 100% → 0% → 100% ... */
}
```

### 9.3.7. animation-fill-mode

```css
.box {
    animation-fill-mode: none;      /* Default state before/after */
    animation-fill-mode: forwards;  /* Keep last keyframe */
    animation-fill-mode: backwards; /* Apply first keyframe during delay */
    animation-fill-mode: both;      /* Both forwards and backwards */
}
```

### 9.3.8. animation-play-state

```css
.box {
    animation-play-state: running;  /* Default */
    animation-play-state: paused;   /* Pause animation */
}

.box:hover {
    animation-play-state: paused;
}
```

### 9.3.9. Animation Shorthand

```css
.box {
    /* name | duration | timing-function | delay | iteration-count | direction | fill-mode | play-state */
    animation: fadeIn 1s ease 0s 1 normal forwards running;

    /* Common */
    animation: slideLeft 2s ease-in-out infinite;

    /* Multiple animations */
    animation:
        fadeIn 1s ease,
        slideUp 2s ease-out 0.5s;
}
```

## 9.4. Practical Examples

### 9.4.1. Fade In

```css
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.fade-in {
    animation: fadeIn 0.5s ease-in forwards;
}
```

### 9.4.2. Slide In

```css
@keyframes slideInLeft {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

.slide-in {
    animation: slideInLeft 0.5s ease-out forwards;
}
```

### 9.4.3. Bounce

```css
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-30px);
    }
    60% {
        transform: translateY(-15px);
    }
}

.bounce {
    animation: bounce 2s ease infinite;
}
```

### 9.4.4. Pulse

```css
@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
}

.pulse {
    animation: pulse 1s ease-in-out infinite;
}
```

### 9.4.5. Shake

```css
@keyframes shake {
    0%, 100% {
        transform: translateX(0);
    }
    10%, 30%, 50%, 70%, 90% {
        transform: translateX(-10px);
    }
    20%, 40%, 60%, 80% {
        transform: translateX(10px);
    }
}

.shake {
    animation: shake 0.5s ease;
}
```

### 9.4.6. Rotate

```css
@keyframes rotate {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

.rotate {
    animation: rotate 2s linear infinite;
}
```

### 9.4.7. Loading Spinner

```css
@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

.spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #f3f3f3;
    border-top: 5px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}
```

### 9.4.8. Typing Effect

```css
@keyframes typing {
    from {
        width: 0;
    }
    to {
        width: 100%;
    }
}

@keyframes blink {
    50% {
        border-color: transparent;
    }
}

.typewriter {
    overflow: hidden;
    border-right: 2px solid #333;
    white-space: nowrap;
    animation:
        typing 3.5s steps(40, end),
        blink 0.75s step-end infinite;
}
```

### 9.4.9. Gradient Animation

```css
@keyframes gradientShift {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.gradient-bg {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}
```

### 9.4.10. Float

```css
@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-20px);
    }
}

.float {
    animation: float 3s ease-in-out infinite;
}
```

## 9.5. Complex Animations

### 9.5.1. Multi-Step Animation

```css
@keyframes complexMove {
    0% {
        transform: translate(0, 0) scale(1) rotate(0deg);
        opacity: 1;
    }
    25% {
        transform: translate(100px, 0) scale(1.2) rotate(90deg);
        opacity: 0.8;
    }
    50% {
        transform: translate(100px, 100px) scale(1) rotate(180deg);
        opacity: 0.6;
    }
    75% {
        transform: translate(0, 100px) scale(0.8) rotate(270deg);
        opacity: 0.8;
    }
    100% {
        transform: translate(0, 0) scale(1) rotate(360deg);
        opacity: 1;
    }
}
```

### 9.5.2. Staggered Animations

```css
.item:nth-child(1) { animation-delay: 0s; }
.item:nth-child(2) { animation-delay: 0.1s; }
.item:nth-child(3) { animation-delay: 0.2s; }
.item:nth-child(4) { animation-delay: 0.3s; }
.item:nth-child(5) { animation-delay: 0.4s; }
```

### 9.5.3. Combining Multiple Animations

```css
.box {
    animation:
        fadeIn 1s ease,
        slideUp 1s ease,
        rotate 2s linear infinite;
}
```

## 9.6. Performance Tips

```css
/* Good: Use transform and opacity */
@keyframes goodAnimation {
    to {
        transform: translateX(100px);
        opacity: 0.5;
    }
}

/* Avoid: Animating width/height/top/left */
@keyframes avoidAnimation {
    to {
        width: 200px;  /* Causes reflow */
        left: 100px;   /* Causes reflow */
    }
}

/* Use will-change for better performance */
.animated {
    will-change: transform, opacity;
    animation: complexMove 2s ease;
}
```

## 9.7. JavaScript Control

```javascript
// Play/Pause
element.style.animationPlayState = 'paused';
element.style.animationPlayState = 'running';

// Listen to events
element.addEventListener('animationstart', () => {
    console.log('Animation started');
});

element.addEventListener('animationend', () => {
    console.log('Animation ended');
});

element.addEventListener('animationiteration', () => {
    console.log('Animation iteration');
});
```

---

**Kết luận:** CSS Animations powerful hơn transitions, cho phép multi-step animations. Combine với @keyframes để tạo complex effects.

**Chương tiếp theo:** Transforms


## 9.10. Practical Examples - Extended

### 9.10.1. Skeleton Loader

Loading placeholder animation

```css
.skeleton {
    background: linear-gradient(
        90deg,
        #f0f0f0 25%,
        #e0e0e0 50%,
        #f0f0f0 75%
    );
    background-size: 200% 100%;
    animation: loading 1.5s ease-in-out infinite;
}

@keyframes loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
```

### 9.10.2. Heartbeat Animation

Pulsing effect

```css
@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    10%, 30% { transform: scale(0.9); }
    20%, 40% { transform: scale(1.1); }
}

.heart {
    animation: heartbeat 1.3s ease-in-out infinite;
}
```


## 9.11. Real-World Use Cases

### 9.11.1. Loading Spinners

Custom loaders for apps

```css
/* Implementation details */
```

### 9.11.2. Attention Grabbers

Call-to-action animations

```css
/* Implementation details */
```

### 9.11.3. Page Transitions

Route change animations

```css
/* Implementation details */
```

### 9.11.4. Success/Error Indicators

Feedback animations

```css
/* Implementation details */
```

### 9.11.5. Background Animations

Ambient motion effects

```css
/* Implementation details */
```


## 9.12. Tips & Tricks

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

## 9.13. Common Mistakes

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

## 9.14. Troubleshooting

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

## 9.15. Advanced Topics

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

## 9.16. Bài Tập

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

**Chương tiếp theo:** Transforms


## 9.20. Complex Animation Examples

### 9.20.1. Loading Dots Animation
```css
.loading-dots {
    display: flex;
    gap: 8px;
}

.dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #3498db;
    animation: bounce 1.4s infinite ease-in-out both;
}

.dot:nth-child(1) { animation-delay: -0.32s; }
.dot:nth-child(2) { animation-delay: -0.16s; }

@keyframes bounce {
    0%, 80%, 100% {
        transform: scale(0);
    }
    40% {
        transform: scale(1);
    }
}
```

### 9.20.2. Ripple Effect
```css
.ripple {
    position: relative;
    overflow: hidden;
}

.ripple::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.5);
    transform: translate(-50%, -50%);
    animation: ripple-animation 0.6s ease-out;
}

@keyframes ripple-animation {
    to {
        width: 200%;
        height: 200%;
        opacity: 0;
    }
}
```

### 9.20.3. Text Reveal Animation
```css
.text-reveal {
    display: inline-block;
    overflow: hidden;
}

.text-reveal span {
    display: inline-block;
    transform: translateY(100%);
    animation: reveal 0.6s cubic-bezier(0.77, 0, 0.175, 1) forwards;
}

@keyframes reveal {
    to {
        transform: translateY(0);
    }
}
```

### 9.20.4. Flip Card Animation
```css
.flip-card {
    perspective: 1000px;
}

.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 0.6s;
}

.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
}

.flip-card-back {
    transform: rotateY(180deg);
}
```

### 9.20.5. Particle Animation
```css
.particles {
    position: relative;
}

.particle {
    position: absolute;
    width: 4px;
    height: 4px;
    background: white;
    border-radius: 50%;
    animation: float 3s ease-in-out infinite;
}

.particle:nth-child(1) {
    left: 10%;
    animation-delay: 0s;
    animation-duration: 2s;
}

.particle:nth-child(2) {
    left: 30%;
    animation-delay: 0.5s;
    animation-duration: 2.5s;
}

@keyframes float {
    0%, 100% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }
    50% {
        transform: translateY(-100px) rotate(180deg);
        opacity: 0.5;
    }
}
```

### 9.20.6. Progress Bar with Animation
```css
.progress-bar {
    position: relative;
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #3498db, #2ecc71);
    animation: progress 2s ease-out forwards;
}

@keyframes progress {
    from {
        width: 0;
    }
    to {
        width: 100%;
    }
}

.progress-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.3),
        transparent
    );
    animation: shimmer 1s infinite;
}

@keyframes shimmer {
    to {
        transform: translateX(100%);
    }
}
```

### 9.20.7. Clock Loader
```css
.clock-loader {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 3px solid #e0e0e0;
    position: relative;
}

.clock-loader::before,
.clock-loader::after {
    content: '';
    position: absolute;
    background: #3498db;
    transform-origin: bottom center;
}

/* Hour hand */
.clock-loader::before {
    width: 3px;
    height: 15px;
    top: 10px;
    left: 50%;
    margin-left: -1.5px;
    animation: rotate-hour 3s linear infinite;
}

/* Minute hand */
.clock-loader::after {
    width: 2px;
    height: 20px;
    top: 5px;
    left: 50%;
    margin-left: -1px;
    animation: rotate-minute 1s linear infinite;
}

@keyframes rotate-hour {
    to { transform: rotate(360deg); }
}

@keyframes rotate-minute {
    to { transform: rotate(360deg); }
}
```

### 9.20.8. Glitch Effect
```css
.glitch {
    position: relative;
    animation: glitch-anim 2s infinite;
}

@keyframes glitch-anim {
    0%, 100% {
        clip-path: inset(0);
    }
    10% {
        clip-path: inset(10% 0 85% 0);
    }
    20% {
        clip-path: inset(80% 0 0 0);
    }
    30% {
        clip-path: inset(10% 0 0 0);
    }
}

.glitch::before,
.glitch::after {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.glitch::before {
    left: 2px;
    text-shadow: -2px 0 #ff00c1;
    animation: glitch-anim-2 3s infinite linear alternate-reverse;
}

.glitch::after {
    left: -2px;
    text-shadow: 2px 0 #00fff9;
    animation: glitch-anim-3 2.5s infinite linear alternate-reverse;
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
