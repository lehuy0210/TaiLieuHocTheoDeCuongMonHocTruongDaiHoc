# CHƯƠNG 3: COLORS & BACKGROUNDS

## 3.1. CSS3 Colors

### 3.1.1. RGB và RGBA

```css
/* RGB */
.box {
    color: rgb(255, 0, 0);  /* Red */
    background: rgb(0, 255, 0);  /* Green */
}

/* RGBA (with alpha/transparency) */
.overlay {
    background: rgba(0, 0, 0, 0.5);  /* 50% transparent black */
}

.button {
    background: rgba(52, 152, 219, 0.8);
}
```

### 3.1.2. HSL và HSLA

```css
/* HSL (Hue, Saturation, Lightness) */
.primary {
    color: hsl(200, 70%, 50%);
}

/* HSLA (with alpha) */
.secondary {
    background: hsla(120, 60%, 50%, 0.3);
}

/* Easier to manipulate */
:root {
    --hue: 200;
}

.light { background: hsl(var(--hue), 70%, 70%); }
.dark { background: hsl(var(--hue), 70%, 30%); }
```

### 3.1.3. HEX Colors

```css
/* 6-digit hex */
.box {
    color: #3498db;
}

/* 3-digit shorthand */
.box {
    color: #3db;  /* Same as #33ddbb */
}

/* 8-digit hex (with alpha) */
.box {
    background: #3498db80;  /* 50% transparent */
}
```

### 3.1.4. Named Colors

```css
.box {
    color: red;
    background: skyblue;
    border-color: coral;
}
```

### 3.1.5. currentColor

```css
.icon {
    color: blue;
    border: 2px solid currentColor;  /* Uses text color */
}

svg {
    fill: currentColor;  /* Inherits parent color */
}
```

## 3.2. Gradients

### 3.2.1. Linear Gradient

```css
/* Top to bottom */
.gradient {
    background: linear-gradient(red, blue);
}

/* Direction */
.gradient {
    background: linear-gradient(to right, red, blue);
    background: linear-gradient(to bottom right, red, blue);
    background: linear-gradient(45deg, red, blue);
}

/* Multiple colors */
.gradient {
    background: linear-gradient(red, yellow, green);
}

/* Color stops */
.gradient {
    background: linear-gradient(
        red 0%,
        yellow 50%,
        green 100%
    );
}

/* Sharp transition */
.gradient {
    background: linear-gradient(
        red 0%, red 50%,
        blue 50%, blue 100%
    );
}
```

### 3.2.2. Radial Gradient

```css
/* Center to edges */
.radial {
    background: radial-gradient(red, blue);
}

/* Shape and size */
.radial {
    background: radial-gradient(circle, red, blue);
    background: radial-gradient(ellipse, red, blue);
}

/* Position */
.radial {
    background: radial-gradient(circle at top left, red, blue);
    background: radial-gradient(circle at 20% 50%, red, blue);
}

/* Size */
.radial {
    background: radial-gradient(
        circle closest-side,
        red, blue
    );
}
```

### 3.2.3. Conic Gradient

```css
.conic {
    background: conic-gradient(red, yellow, green, blue, red);
}

/* Pie chart */
.pie {
    background: conic-gradient(
        red 0deg 90deg,
        blue 90deg 180deg,
        green 180deg 270deg,
        yellow 270deg 360deg
    );
}
```

### 3.2.4. Repeating Gradients

```css
/* Repeating linear */
.stripes {
    background: repeating-linear-gradient(
        45deg,
        #fff 0px,
        #fff 10px,
        #000 10px,
        #000 20px
    );
}

/* Repeating radial */
.circles {
    background: repeating-radial-gradient(
        circle,
        red 0px,
        red 10px,
        blue 10px,
        blue 20px
    );
}
```

## 3.3. Backgrounds

### 3.3.1. background-size

```css
.box {
    background-image: url('image.jpg');

    /* Keyword values */
    background-size: cover;      /* Fill entire box */
    background-size: contain;    /* Fit inside box */

    /* Specific sizes */
    background-size: 100px 50px; /* Width height */
    background-size: 50%;        /* Percentage */
    background-size: auto 100%; /* Auto width, full height */
}
```

### 3.3.2. background-position

```css
.box {
    /* Keywords */
    background-position: center;
    background-position: top right;
    background-position: bottom left;

    /* Percentages */
    background-position: 50% 50%;

    /* Pixels */
    background-position: 10px 20px;

    /* Mixed */
    background-position: left 10px top 20px;
}
```

### 3.3.3. background-repeat

```css
.box {
    background-repeat: no-repeat;
    background-repeat: repeat;
    background-repeat: repeat-x;
    background-repeat: repeat-y;
    background-repeat: space;
    background-repeat: round;
}
```

### 3.3.4. background-attachment

```css
.parallax {
    background-image: url('bg.jpg');
    background-attachment: fixed;    /* Parallax effect */
    background-attachment: scroll;   /* Scrolls with content */
    background-attachment: local;    /* Scrolls with element */
}
```

### 3.3.5. background-origin

```css
.box {
    background-origin: border-box;   /* Include border */
    background-origin: padding-box;  /* Default */
    background-origin: content-box;  /* Content only */
}
```

### 3.3.6. background-clip

```css
.box {
    background-clip: border-box;   /* Default */
    background-clip: padding-box;
    background-clip: content-box;
}

/* Text clip */
.title {
    background: linear-gradient(45deg, red, blue);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
}
```

### 3.3.7. Multiple Backgrounds

```css
.box {
    background-image:
        url('top.png'),
        url('middle.png'),
        url('bottom.png');

    background-position:
        top center,
        center center,
        bottom center;

    background-repeat: no-repeat;
}

/* With gradients */
.box {
    background:
        linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)),
        url('image.jpg');
    background-size: cover;
}
```

## 3.4. Practical Examples

### 3.4.1. Hero Section

```css
.hero {
    background: linear-gradient(
        rgba(0, 0, 0, 0.5),
        rgba(0, 0, 0, 0.5)
    ), url('hero.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    height: 100vh;
}
```

### 3.4.2. Gradient Button

```css
.button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px 30px;
    border: none;
    border-radius: 5px;
}

.button:hover {
    background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
}
```

### 3.4.3. Card with Gradient Border

```css
.card {
    background: white;
    border-radius: 10px;
    padding: 2px;
    background: linear-gradient(45deg, red, blue);
}

.card-content {
    background: white;
    border-radius: 8px;
    padding: 20px;
}
```

### 3.4.4. Gradient Text

```css
.gradient-text {
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(45deg, #f3ec78, #af4261);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}
```

### 3.4.5. Pattern Background

```css
.pattern {
    background-color: #ffffff;
    background-image: repeating-linear-gradient(
        45deg,
        transparent,
        transparent 10px,
        rgba(0,0,0,.05) 10px,
        rgba(0,0,0,.05) 20px
    );
}
```

### 3.4.6. Modern Card with Glassmorphism

```html
<div class="glass-card">
    <h2>Glassmorphism Card</h2>
    <p>Beautiful frosted glass effect with backdrop blur</p>
</div>
```

```css
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 40px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    color: white;
}

.glass-card h2 {
    margin-bottom: 15px;
    font-size: 2rem;
}
```

### 3.4.7. Animated Gradient Background

```css
.animated-gradient {
    background: linear-gradient(
        -45deg,
        #ee7752,
        #e73c7e,
        #23a6d5,
        #23d5ab
    );
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

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

/* Usage */
.hero-section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}
```

## 3.5. Real-World Use Cases

### 3.5.1. E-commerce Product Cards

```css
.product-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.product-card:hover {
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
    transform: translateY(-5px);
}

.product-image {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    aspect-ratio: 1 / 1;
    display: flex;
    align-items: center;
    justify-content: center;
}

.product-badge {
    position: absolute;
    top: 10px;
    right: 10px;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: bold;
}
```

### 3.5.2. Dashboard Status Indicators

```css
.status-card {
    padding: 20px;
    border-radius: 10px;
    border-left: 4px solid;
}

.status-success {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1) 0%, rgba(46, 204, 113, 0.05) 100%);
    border-left-color: #2ecc71;
}

.status-warning {
    background: linear-gradient(135deg, rgba(241, 196, 15, 0.1) 0%, rgba(241, 196, 15, 0.05) 100%);
    border-left-color: #f1c40f;
}

.status-error {
    background: linear-gradient(135deg, rgba(231, 76, 60, 0.1) 0%, rgba(231, 76, 60, 0.05) 100%);
    border-left-color: #e74c3c;
}

.status-info {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1) 0%, rgba(52, 152, 219, 0.05) 100%);
    border-left-color: #3498db;
}
```

### 3.5.3. Social Media Profile Headers

```css
.profile-header {
    position: relative;
    height: 300px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    overflow: hidden;
}

.profile-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('pattern.svg');
    background-size: 100px;
    opacity: 0.1;
}

.profile-avatar {
    position: absolute;
    bottom: -50px;
    left: 30px;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 5px solid white;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}
```

### 3.5.4. Blog Post Featured Images

```css
.featured-image {
    position: relative;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border-radius: 12px;
}

.featured-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.featured-image::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0) 0%,
        rgba(0, 0, 0, 0.7) 100%
    );
}

.featured-content {
    position: absolute;
    bottom: 20px;
    left: 20px;
    right: 20px;
    color: white;
    z-index: 1;
}
```

### 3.5.5. Mobile App Onboarding Screens

```css
.onboarding-screen {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
}

.onboarding-1 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.onboarding-2 {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.onboarding-3 {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.onboarding-illustration {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    margin-bottom: 40px;
}
```

## 3.6. Tips & Tricks

### Tip 1: Use HSL for Color Variations
```css
:root {
    --primary-hue: 200;
}

.button-light {
    background: hsl(var(--primary-hue), 70%, 70%);
}

.button-normal {
    background: hsl(var(--primary-hue), 70%, 50%);
}

.button-dark {
    background: hsl(var(--primary-hue), 70%, 30%);
}
```

### Tip 2: Layer Multiple Gradients for Complex Patterns
```css
.complex-bg {
    background:
        linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.1) 30%),
        linear-gradient(-45deg, transparent 30%, rgba(255, 255, 255, 0.1) 30%),
        linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    background-size: 20px 20px, 20px 20px, 100% 100%;
}
```

### Tip 3: Use currentColor for Icon Colors
```css
.icon-button {
    color: #3498db;
}

.icon-button svg {
    fill: currentColor;
    width: 20px;
    height: 20px;
}

.icon-button:hover {
    color: #2980b9;
}
```

### Tip 4: Create Gradient Borders with Pseudo-elements
```css
.gradient-border {
    position: relative;
    background: white;
    padding: 2px;
    border-radius: 10px;
}

.gradient-border::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 10px;
    padding: 2px;
    background: linear-gradient(45deg, #f093fb, #f5576c);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
}
```

### Tip 5: Use RGB with CSS Variables
```css
:root {
    --primary-rgb: 52, 152, 219;
}

.button {
    background: rgb(var(--primary-rgb));
}

.button-transparent {
    background: rgba(var(--primary-rgb), 0.5);
}

.button-overlay {
    box-shadow: 0 4px 10px rgba(var(--primary-rgb), 0.3);
}
```

### Tip 6: Create Smooth Color Transitions
```css
.smooth-transition {
    background: linear-gradient(to right, red, yellow, green);
    transition: filter 0.3s ease;
}

.smooth-transition:hover {
    filter: brightness(1.2) saturate(1.3);
}
```

### Tip 7: Use background-blend-mode for Photo Effects
```css
.photo-effect {
    background-image: url('photo.jpg'), linear-gradient(45deg, #f093fb, #f5576c);
    background-size: cover;
    background-blend-mode: multiply;
}
```

### Tip 8: Create Gradient Text with Fallback
```css
.gradient-text {
    color: #667eea; /* Fallback */
    background: linear-gradient(45deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

@supports not (background-clip: text) {
    .gradient-text {
        color: #667eea;
    }
}
```

### Tip 9: Use conic-gradient for Progress Rings
```css
.progress-ring {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: conic-gradient(
        #3498db 0deg 270deg,
        #ecf0f1 270deg 360deg
    );
}
```

### Tip 10: Optimize Gradient Performance
```css
/* Bad: Many color stops can be slow */
.bad-gradient {
    background: linear-gradient(
        to right,
        red 0%, orange 10%, yellow 20%, /* ... many more */
    );
}

/* Good: Use fewer stops */
.good-gradient {
    background: linear-gradient(to right, red, orange, yellow);
    will-change: transform; /* Only when animating */
}
```

## 3.7. Common Mistakes

### Mistake 1: Forgetting Alpha Channel Units
```css
/* Wrong */
.box {
    background: rgba(255, 0, 0, 50); /* Alpha should be 0-1, not 0-100 */
}

/* Correct */
.box {
    background: rgba(255, 0, 0, 0.5);
}
```

### Mistake 2: Not Using Vendor Prefixes for background-clip: text
```css
/* Incomplete */
.text {
    background-clip: text;
    color: transparent;
}

/* Complete */
.text {
    background: linear-gradient(45deg, red, blue);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent; /* Fallback */
}
```

### Mistake 3: Wrong Gradient Syntax Order
```css
/* Wrong */
.box {
    background: linear-gradient(red, blue, to right); /* Direction should be first */
}

/* Correct */
.box {
    background: linear-gradient(to right, red, blue);
}
```

### Mistake 4: Not Providing Fallback Colors
```css
/* Risky */
.box {
    background: linear-gradient(to right, red, blue);
}

/* Safe */
.box {
    background: red; /* Fallback for old browsers */
    background: linear-gradient(to right, red, blue);
}
```

### Mistake 5: Overusing background: all
```css
/* Bad: Overwrites everything */
.box {
    background-image: url('image.jpg');
    background-size: cover;
    background: blue; /* This removes the image! */
}

/* Good: Use specific properties */
.box {
    background-image: url('image.jpg');
    background-size: cover;
    background-color: blue; /* Only sets color */
}
```

### Mistake 6: Wrong background-size for Patterns
```css
/* Wrong: Pattern too large */
.pattern {
    background-image: repeating-linear-gradient(45deg, transparent, transparent 10px, black 10px, black 20px);
    background-size: cover; /* Makes pattern huge */
}

/* Correct: Let pattern use its natural size */
.pattern {
    background-image: repeating-linear-gradient(45deg, transparent, transparent 10px, black 10px, black 20px);
}
```

### Mistake 7: Forgetting background-attachment for Parallax
```css
/* Incomplete parallax */
.hero {
    background-image: url('bg.jpg');
    background-size: cover;
}

/* Complete parallax */
.hero {
    background-image: url('bg.jpg');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}
```

### Mistake 8: Using Too Many background-position Keywords
```css
/* Wrong syntax */
.box {
    background-position: top right bottom; /* Too many keywords */
}

/* Correct */
.box {
    background-position: top right;
}
```

### Mistake 9: Not Considering Color Contrast
```css
/* Bad accessibility */
.button {
    background: #ffeb3b; /* Yellow */
    color: white; /* Poor contrast */
}

/* Good accessibility */
.button {
    background: #ffeb3b;
    color: #333; /* Better contrast */
}
```

### Mistake 10: Forgetting to Set Background for Transparency
```css
/* Transparent background with no fallback */
.overlay {
    background: rgba(0, 0, 0, 0.5);
    /* What if rgba isn't supported? */
}

/* With fallback */
.overlay {
    background: rgb(0, 0, 0); /* Fallback */
    background: rgba(0, 0, 0, 0.5);
}
```

## 3.8. Troubleshooting

### Problem 1: Gradient Not Showing

**Symptoms:** Background appears solid color or transparent

**Solutions:**
```css
/* Check 1: Verify syntax */
.box {
    /* Wrong */
    background: linear-gradient(red blue);

    /* Correct */
    background: linear-gradient(red, blue);
}

/* Check 2: Ensure element has size */
.box {
    min-height: 200px; /* Gradients need dimensions */
}

/* Check 3: Check color format */
.box {
    /* Wrong */
    background: linear-gradient(#red, #blue);

    /* Correct */
    background: linear-gradient(#ff0000, #0000ff);
}
```

### Problem 2: Background Image Not Loading

**Solutions:**
```css
/* Check 1: Verify path */
.box {
    background-image: url('../images/bg.jpg'); /* Relative path */
    background-image: url('/images/bg.jpg'); /* Absolute from root */
    background-image: url('https://example.com/bg.jpg'); /* Full URL */
}

/* Check 2: Check quotes */
.box {
    background-image: url('image.jpg'); /* With quotes */
    background-image: url(image.jpg); /* Without quotes (also valid) */
}

/* Check 3: Ensure element has dimensions */
.box {
    min-height: 300px;
    background-size: cover;
}
```

### Problem 3: Parallax Effect Not Working

**Solutions:**
```css
/* Ensure all required properties */
.parallax {
    background-image: url('bg.jpg');
    background-attachment: fixed; /* Critical for parallax */
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    min-height: 100vh; /* Needs height */
}

/* iOS Safari fix */
@supports (-webkit-touch-callout: none) {
    .parallax {
        background-attachment: scroll;
    }
}
```

### Problem 4: Multiple Backgrounds Not Layering Correctly

**Solutions:**
```css
/* Remember: First listed is on top */
.box {
    background-image:
        url('top-layer.png'),      /* Top */
        url('middle-layer.png'),   /* Middle */
        url('bottom-layer.png');   /* Bottom */

    background-size:
        contain,
        cover,
        cover;

    background-position:
        center top,
        center,
        center;

    background-repeat:
        no-repeat,
        no-repeat,
        no-repeat;
}
```

### Problem 5: Gradient Text Not Working

**Solutions:**
```css
/* Complete implementation */
.gradient-text {
    background: linear-gradient(45deg, red, blue);
    -webkit-background-clip: text; /* Webkit prefix required */
    -webkit-text-fill-color: transparent; /* Webkit prefix required */
    background-clip: text;
    color: transparent; /* Fallback */
    display: inline-block; /* Sometimes needed */
}
```

### Problem 6: Background Not Covering Full Element

**Solutions:**
```css
/* Issue: background-size default is auto */
.hero {
    background-image: url('bg.jpg');
    background-size: auto; /* Image shows at natural size */
}

/* Solution 1: Use cover */
.hero {
    background-size: cover; /* Covers entire element */
}

/* Solution 2: Use 100% */
.hero {
    background-size: 100% 100%; /* Stretches to fit (may distort) */
}
```

### Problem 7: Gradient Banding (Visible Steps)

**Solutions:**
```css
/* Issue: Too few color stops */
.gradient {
    background: linear-gradient(#000, #fff);
}

/* Solution: Add intermediate stops */
.gradient {
    background: linear-gradient(
        #000 0%,
        #333 25%,
        #666 50%,
        #999 75%,
        #fff 100%
    );
}

/* Or use noise texture overlay */
.gradient {
    background: linear-gradient(#000, #fff);
}

.gradient::after {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url('data:image/svg+xml,...'); /* Noise pattern */
    opacity: 0.05;
}
```

### Problem 8: Background-clip: text Not Supported

**Solutions:**
```css
/* Feature detection and fallback */
.gradient-text {
    color: #667eea; /* Fallback color */
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
    .gradient-text {
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        color: transparent;
    }
}
```

### Problem 9: RGBA Colors Not Working

**Solutions:**
```css
/* Old browser fallback */
.box {
    background: rgb(52, 152, 219); /* Fallback */
    background: rgba(52, 152, 219, 0.5);
}

/* Or use opacity (affects whole element) */
.box {
    background: rgb(52, 152, 219);
    opacity: 0.5;
}
```

### Problem 10: Background Repeating Unexpectedly

**Solutions:**
```css
/* Issue: Default is repeat */
.box {
    background-image: url('pattern.png');
    /* Background repeats by default */
}

/* Solution: Set no-repeat */
.box {
    background-image: url('pattern.png');
    background-repeat: no-repeat;
    background-size: cover; /* Often needed with no-repeat */
}
```

## 3.9. Advanced Topics

### Advanced 1: Color Interpolation in Gradients

```css
/* Standard RGB interpolation */
.gradient-rgb {
    background: linear-gradient(to right, red, blue);
}

/* Longer route through color wheel */
.gradient-hsl {
    background: linear-gradient(
        to right,
        hsl(0, 100%, 50%),    /* Red */
        hsl(240, 100%, 50%)   /* Blue */
    );
}

/* Future: Specify interpolation color space */
.gradient-lab {
    background: linear-gradient(in lab to right, red, blue);
}
```

### Advanced 2: CSS Paint API (Houdini)

```css
/* Register custom paint worklet */
.box {
    background: paint(myCustomPattern);
}
```

```javascript
// In worklet file
registerPaint('myCustomPattern', class {
    paint(ctx, size, properties) {
        ctx.fillStyle = '#3498db';
        ctx.fillRect(0, 0, size.width, size.height);
        // Custom drawing code
    }
});
```

### Advanced 3: Complex Multi-layer Patterns

```css
.complex-pattern {
    background:
        /* Layer 1: Dots */
        radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px),
        /* Layer 2: Lines */
        linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
        /* Layer 3: Base gradient */
        linear-gradient(135deg, #667eea 0%, #764ba2 100%);

    background-size:
        20px 20px,  /* Dots */
        20px 20px,  /* Vertical lines */
        20px 20px,  /* Horizontal lines */
        100% 100%;  /* Base */

    background-position:
        0 0,
        0 0,
        0 0,
        center;
}
```

### Advanced 4: Gradient Mesh (Future)

```css
/* Future CSS feature */
.mesh {
    background: mesh-gradient(
        from (0%, 0%) to (100%, 100%),
        #ff0000 at 0% 0%,
        #00ff00 at 100% 0%,
        #0000ff at 0% 100%,
        #ffff00 at 100% 100%
    );
}
```

### Advanced 5: Dynamic Color Manipulation

```css
:root {
    --base-color: 200;
    --saturation: 70%;
    --lightness: 50%;
}

.button {
    background: hsl(var(--base-color), var(--saturation), var(--lightness));
}

.button:hover {
    background: hsl(var(--base-color), var(--saturation), calc(var(--lightness) * 0.8));
}

.button:active {
    background: hsl(var(--base-color), var(--saturation), calc(var(--lightness) * 0.6));
}
```

### Advanced 6: Perceptually Uniform Color Spaces

```css
/* Standard gradient (not perceptually uniform) */
.gradient-srgb {
    background: linear-gradient(to right, red, yellow);
}

/* Future: Lab color space (perceptually uniform) */
.gradient-lab {
    background: linear-gradient(in lab to right, lab(50% 80 60), lab(90% -20 70));
}

/* Future: LCH color space */
.gradient-lch {
    background: linear-gradient(in lch to right, lch(50% 60 60), lch(90% 40 120));
}
```

### Advanced 7: Background Masking Techniques

```css
.masked-background {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-mask-image: linear-gradient(to bottom, black 0%, transparent 100%);
    mask-image: linear-gradient(to bottom, black 0%, transparent 100%);
}

/* Complex mask with multiple layers */
.complex-mask {
    background: linear-gradient(45deg, red, blue);
    -webkit-mask-image:
        radial-gradient(circle at 30% 30%, black 0%, transparent 50%),
        radial-gradient(circle at 70% 70%, black 0%, transparent 50%);
    -webkit-mask-composite: source-over;
}
```

### Advanced 8: Performance Optimization for Backgrounds

```css
/* Use will-change sparingly */
.animated-bg {
    will-change: background-position; /* Only during animation */
    background: url('large-image.jpg');
    background-size: cover;
}

.animated-bg.animating {
    animation: bgMove 20s linear infinite;
}

@keyframes bgMove {
    0% { background-position: 0% 0%; }
    100% { background-position: 100% 100%; }
}

/* Remove will-change when done */
.animated-bg:not(.animating) {
    will-change: auto;
}
```

### Advanced 9: Responsive Background Images

```css
/* Use image-set for resolution-aware backgrounds */
.box {
    background-image: image-set(
        url('bg-1x.jpg') 1x,
        url('bg-2x.jpg') 2x,
        url('bg-3x.jpg') 3x
    );
}

/* Combine with media queries */
@media (max-width: 768px) {
    .box {
        background-image: image-set(
            url('bg-mobile-1x.jpg') 1x,
            url('bg-mobile-2x.jpg') 2x
        );
    }
}
```

### Advanced 10: Color Contrast Functions

```css
/* Future: Automatic contrast */
.button {
    background: var(--button-bg);
    color: color-contrast(var(--button-bg) vs white, black);
}

/* Workaround: Use filter for hover states */
.button {
    background: #3498db;
    color: white;
}

.button:hover {
    filter: brightness(0.9) saturate(1.1);
}
```

## 3.5. CSS Variables for Colors

```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2ecc71;
    --dark-color: #2c3e50;
    --light-color: #ecf0f1;

    --primary-rgb: 52, 152, 219;
}

.button {
    background-color: var(--primary-color);
    color: white;
}

.overlay {
    background-color: rgba(var(--primary-rgb), 0.8);
}
```

## 3.10. Modern Color Functions

```css
/* color-mix (future) */
.box {
    color: color-mix(in srgb, blue 50%, red);
}

/* hwb (Hue, Whiteness, Blackness) */
.box {
    color: hwb(120 20% 30%);
}
```

## 3.11. Bài Tập

### Bài Tập 1: Gradient Button Collection
Tạo một collection gồm 5 buttons với các gradient styles khác nhau:
- Button 1: Linear gradient từ trái sang phải
- Button 2: Radial gradient từ center
- Button 3: Gradient với hover effect (đổi direction)
- Button 4: Multi-color gradient (ít nhất 4 màu)
- Button 5: Animated gradient background

```html
<!-- HTML structure -->
<div class="button-collection">
    <button class="btn btn-1">Linear</button>
    <button class="btn btn-2">Radial</button>
    <button class="btn btn-3">Hover</button>
    <button class="btn btn-4">Multi</button>
    <button class="btn btn-5">Animated</button>
</div>
```

**Yêu cầu:**
- Mỗi button có padding 15px 30px
- Border radius 8px
- Smooth transition 0.3s
- Text màu trắng, font-weight bold

### Bài Tập 2: Hero Section với Parallax Background
Tạo một hero section với:
- Background image với parallax effect
- Gradient overlay (top: transparent, bottom: dark)
- Centered content
- Full viewport height

**Yêu cầu:**
- Sử dụng background-attachment: fixed
- Overlay gradient từ transparent đến rgba(0,0,0,0.7)
- Content có backdrop-filter blur
- Responsive cho mobile (tắt parallax)

### Bài Tập 3: Color Palette Generator
Tạo một color palette hiển thị các variations của một màu primary sử dụng HSL:
- Base color
- 3 lighter variations
- 3 darker variations
- Hiển thị color code khi hover

**Yêu cầu:**
- Sử dụng CSS variables
- Grid layout 7 columns
- Smooth color transition
- Tooltip hiển thị HSL value

### Bài Tập 4: Glassmorphism Card
Tạo một card với glassmorphism effect:
- Semi-transparent background
- Backdrop blur
- Subtle border
- Floating shadow

**Yêu cầu:**
- background: rgba(255, 255, 255, 0.1)
- backdrop-filter: blur(10px)
- border: 1px solid rgba(255, 255, 255, 0.2)
- Animated hover effect

### Bài Tập 5: Gradient Text Heading
Tạo một heading với gradient text effect:
- Animated gradient background
- Text có gradient fill
- Smooth animation
- Fallback color cho browsers không support

**Yêu cầu:**
- Sử dụng background-clip: text
- Animation 5s infinite
- Fallback color #667eea
- Add text-shadow cho depth

### Bài Tập 6: Background Pattern Library
Tạo 4 different background patterns sử dụng CSS gradients:
- Diagonal stripes
- Polka dots
- Checkerboard
- Diagonal grid

**Yêu cầu:**
- Mỗi pattern trong một div 200x200px
- Sử dụng repeating gradients
- Pattern seamless (không có gaps)
- Hover effect: scale pattern

### Bài Tập 7: Status Badge System
Tạo một hệ thống status badges cho dashboard:
- Success (green)
- Warning (yellow)
- Error (red)
- Info (blue)
- Pending (gray)

**Yêu cầu:**
- Gradient background cho mỗi status
- Icon với currentColor
- Subtle pulse animation cho pending
- Border-left accent color

### Bài Tập 8: Image Overlay Gallery
Tạo một gallery với 6 images, mỗi image có gradient overlay khi hover:
- Overlay từ transparent đến dark
- Title và description xuất hiện
- Smooth fade-in effect
- Zoom image khi hover

**Yêu cầu:**
- Grid layout 3 columns
- Overlay: linear-gradient(to bottom, transparent, rgba(0,0,0,0.8))
- Transform: scale(1.1) cho image
- Transition 0.4s ease

### Bài Tập 9: Theme Switcher
Tạo một component có 3 theme options:
- Light theme
- Dark theme
- Auto (follows system preference)

**Yêu cầu:**
- Sử dụng CSS variables
- Smooth transition giữa themes
- Save preference trong localStorage (JavaScript)
- Use prefers-color-scheme media query

```css
:root {
    --bg: white;
    --text: #333;
    --primary: #3498db;
}

[data-theme="dark"] {
    --bg: #1a1a1a;
    --text: #f0f0f1;
    --primary: #5dade2;
}
```

### Bài Tập 10: Animated Background Waves
Tạo animated wave background sử dụng gradients:
- 3 waves với different speeds
- Smooth animation
- Gradient colors
- Full viewport coverage

**Yêu cầu:**
- Sử dụng multiple background layers
- CSS animations với keyframes
- Wave effect bằng radial-gradient
- Animation duration: 10s, 15s, 20s

### Bài Tập 11: Product Card với Gradient Border
Tạo một product card với animated gradient border:
- Gradient border xoay 360 độ
- Card content có background trắng
- Hover effect: faster rotation
- Shadow tăng lên khi hover

**Yêu cầu:**
- Sử dụng pseudo-element cho border
- Animation: rotate 4s linear infinite
- Hover: animation-duration 2s
- Border gradient: linear-gradient(45deg, #f093fb, #f5576c, #4facfe)

### Bài Tập 12: Color Contrast Checker
Tạo một tool kiểm tra color contrast:
- 2 input boxes cho foreground và background colors
- Hiển thị contrast ratio
- Pass/Fail indicator theo WCAG standards
- Preview text với colors đã chọn

**Yêu cầu:**
- Real-time preview
- Show contrast ratio number
- WCAG AA/AAA indicators
- Sử dụng CSS variables cho colors

```html
<div class="contrast-checker">
    <div class="color-inputs">
        <input type="color" id="fg-color" value="#333333">
        <input type="color" id="bg-color" value="#ffffff">
    </div>
    <div class="preview" style="background: var(--bg); color: var(--fg);">
        <h2>Sample Heading</h2>
        <p>Sample paragraph text to check readability</p>
    </div>
    <div class="results">
        <span class="ratio">Contrast Ratio: <strong>12.63:1</strong></span>
        <span class="wcag-aa pass">WCAG AA: Pass</span>
        <span class="wcag-aaa pass">WCAG AAA: Pass</span>
    </div>
</div>
```

---

**Kết luận:** CSS3 cung cấp nhiều cách để làm việc với colors và backgrounds, từ gradients đến multiple backgrounds và background-clip. Mastery của colors và backgrounds là foundation cho modern web design.

**Chương tiếp theo:** Box Model & Sizing
