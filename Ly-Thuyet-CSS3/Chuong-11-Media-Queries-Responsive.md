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
