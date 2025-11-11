# CHƯƠNG 4: BOX MODEL & SIZING

## 4.1. Box Model

### 4.1.1. Traditional Box Model

```css
.box {
    width: 300px;
    padding: 20px;
    border: 5px solid black;
    margin: 10px;
}
/* Total width = 300 + 20*2 + 5*2 + 10*2 = 370px */
```

### 4.1.2. box-sizing: border-box

```css
/* Modern approach */
*, *::before, *::after {
    box-sizing: border-box;
}

.box {
    box-sizing: border-box;
    width: 300px;  /* Total width including padding and border */
    padding: 20px;
    border: 5px solid black;
}
/* Total width = 300px exactly */
```

## 4.2. Width và Height

### 4.2.1. Fixed Sizing

```css
.box {
    width: 300px;
    height: 200px;
}
```

### 4.2.2. min/max Width/Height

```css
.container {
    width: 100%;
    max-width: 1200px;  /* Never wider than 1200px */
    min-width: 320px;   /* Never narrower than 320px */
    margin: 0 auto;     /* Center */
}

.sidebar {
    min-height: 300px;  /* Minimum height */
    max-height: 600px;  /* Maximum height */
}
```

### 4.2.3. Percentage Sizing

```css
.container {
    width: 80%;
}

.half {
    width: 50%;
}
```

### 4.2.4. Viewport Units

```css
.hero {
    width: 100vw;   /* 100% viewport width */
    height: 100vh;  /* 100% viewport height */
}

.sidebar {
    width: 25vw;
    min-height: 50vh;
}

/* Font sizes with viewport units */
h1 {
    font-size: 5vw;  /* Responsive */
}
```

### 4.2.5. calc()

```css
.content {
    width: calc(100% - 300px);  /* Full width minus sidebar */
    padding: calc(1rem + 5px);
}

.grid {
    width: calc(100% / 3 - 20px);
}

/* Mix units */
.box {
    width: calc(100vw - 2rem);
    height: calc(50vh + 100px);
}
```

## 4.3. Padding

```css
/* All sides */
.box {
    padding: 20px;
}

/* Vertical | Horizontal */
.box {
    padding: 10px 20px;
}

/* Top | Horizontal | Bottom */
.box {
    padding: 10px 20px 15px;
}

/* Top | Right | Bottom | Left */
.box {
    padding: 10px 20px 15px 25px;
}

/* Individual sides */
.box {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 15px;
    padding-left: 25px;
}

/* Logical properties */
.box {
    padding-block: 20px;    /* Top and bottom */
    padding-inline: 10px;   /* Left and right */
}
```

## 4.4. Margin

```css
/* Same syntax as padding */
.box {
    margin: 20px;
    margin: 10px 20px;
    margin: 10px 20px 15px 25px;
}

/* Auto centering */
.centered {
    width: 600px;
    margin: 0 auto;  /* Horizontal center */
}

/* Negative margins */
.overlap {
    margin-top: -20px;
}

/* Margin collapse */
.box1 {
    margin-bottom: 20px;
}
.box2 {
    margin-top: 30px;
}
/* Gap between boxes is 30px (not 50px) */
```

## 4.5. Border

### 4.5.1. Basic Border

```css
.box {
    border: 2px solid black;

    /* Individual sides */
    border-top: 1px solid red;
    border-right: 2px dashed blue;
    border-bottom: 3px dotted green;
    border-left: 4px double yellow;
}

/* Border style */
.box {
    border-style: solid;
    border-style: dashed;
    border-style: dotted;
    border-style: double;
    border-style: groove;
    border-style: ridge;
    border-style: inset;
    border-style: outset;
}
```

### 4.5.2. border-radius

```css
/* All corners */
.box {
    border-radius: 10px;
}

/* Individual corners */
.box {
    border-radius: 10px 20px 30px 40px;
    /* top-left | top-right | bottom-right | bottom-left */
}

/* Specific corners */
.box {
    border-top-left-radius: 10px;
    border-top-right-radius: 20px;
    border-bottom-right-radius: 30px;
    border-bottom-left-radius: 40px;
}

/* Circle */
.circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

/* Pill shape */
.pill {
    border-radius: 9999px;
}

/* Elliptical corners */
.box {
    border-radius: 50px / 25px;  /* horizontal / vertical */
}
```

### 4.5.3. border-image

```css
.box {
    border: 10px solid;
    border-image: url('border.png') 30 round;
}

.gradient-border {
    border: 5px solid;
    border-image: linear-gradient(45deg, red, blue) 1;
}
```

## 4.6. Outline

```css
.box {
    outline: 2px solid blue;
    outline-offset: 5px;  /* Space between border and outline */
}

/* Focus outline */
button:focus {
    outline: 3px solid blue;
    outline-offset: 2px;
}

/* Remove outline (provide alternative!) */
button {
    outline: none;  /* Bad without alternative focus style */
}

button:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.5);  /* Alternative */
}
```

## 4.7. Box Shadow

```css
.box {
    /* x-offset | y-offset | blur | spread | color */
    box-shadow: 2px 2px 10px 0px rgba(0, 0, 0, 0.3);
}

/* Multiple shadows */
.box {
    box-shadow:
        0 2px 4px rgba(0, 0, 0, 0.1),
        0 4px 8px rgba(0, 0, 0, 0.1),
        0 8px 16px rgba(0, 0, 0, 0.1);
}

/* Inset shadow */
.inset {
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Elevation effect */
.card {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s;
}

.card:hover {
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

/* No shadow */
.flat {
    box-shadow: none;
}
```

## 4.8. Overflow

```css
.box {
    overflow: visible;  /* Default */
    overflow: hidden;   /* Clip content */
    overflow: scroll;   /* Always show scrollbars */
    overflow: auto;     /* Show scrollbars if needed */
}

/* Individual axes */
.box {
    overflow-x: hidden;
    overflow-y: auto;
}

/* Text ellipsis */
.truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Line clamp */
.clamp {
    display: -webkit-box;
    -webkit-line-clamp: 3;  /* Number of lines */
    -webkit-box-orient: vertical;
    overflow: hidden;
}
```

## 4.9. Aspect Ratio

```css
.video-container {
    aspect-ratio: 16 / 9;
}

.square {
    aspect-ratio: 1 / 1;
}

/* Old technique (padding hack) */
.aspect-box {
    position: relative;
    padding-bottom: 56.25%;  /* 16:9 = 9/16 = 0.5625 */
}

.aspect-box > * {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
```

## 4.10. Object Fit

```css
img, video {
    width: 100%;
    height: 300px;

    object-fit: cover;     /* Fill, may crop */
    object-fit: contain;   /* Fit inside, may have gaps */
    object-fit: fill;      /* Stretch to fill */
    object-fit: none;      /* Original size */
    object-fit: scale-down; /* none or contain, whichever is smaller */
}

/* Object position */
img {
    object-fit: cover;
    object-position: top;      /* Crop from top */
    object-position: 50% 50%;  /* Center (default) */
}
```

## 4.11. Practical Examples

### 4.11.1. Card Component

```css
.card {
    box-sizing: border-box;
    width: 100%;
    max-width: 400px;
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin: 20px;
}
```

### 4.11.2. Responsive Container

```css
.container {
    box-sizing: border-box;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```

### 4.11.3. Avatar with Border

```css
.avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 3px solid white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    object-fit: cover;
}
```

---

**Kết luận:** Box model và sizing là nền tảng của CSS layout. Hiểu rõ box-sizing, padding, margin, và các đơn vị đo lường là essential.

**Chương tiếp theo:** Typography & Fonts
