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

## 3.6. Modern Color Functions

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

---

**Kết luận:** CSS3 cung cấp nhiều cách để làm việc với colors và backgrounds, từ gradients đến multiple backgrounds và background-clip.

**Chương tiếp theo:** Box Model & Sizing
