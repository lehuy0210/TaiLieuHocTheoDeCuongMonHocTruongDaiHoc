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
