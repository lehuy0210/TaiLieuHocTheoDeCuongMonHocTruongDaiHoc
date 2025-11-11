# CHƯƠNG 10: CSS3 TRANSFORMS

## 10.1. 2D Transforms

### 10.1.1. translate()

```css
.box {
    /* Move element */
    transform: translate(50px, 100px);  /* x, y */
    transform: translateX(50px);        /* x only */
    transform: translateY(100px);       /* y only */

    /* Percentage (relative to element size) */
    transform: translate(50%, 50%);

    /* Center positioning trick */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

### 10.1.2. scale()

```css
.box {
    /* Scale both axes */
    transform: scale(1.5);          /* 150% */
    transform: scale(2, 0.5);       /* x: 200%, y: 50% */

    /* Individual axes */
    transform: scaleX(1.5);
    transform: scaleY(0.8);

    /* Flip */
    transform: scaleX(-1);  /* Horizontal flip */
    transform: scaleY(-1);  /* Vertical flip */
}
```

### 10.1.3. rotate()

```css
.box {
    transform: rotate(45deg);      /* Clockwise */
    transform: rotate(-45deg);     /* Counter-clockwise */
    transform: rotate(0.5turn);    /* Half turn */
    transform: rotate(180deg);     /* 180 degrees */
}
```

### 10.1.4. skew()

```css
.box {
    transform: skew(20deg, 10deg);  /* x, y */
    transform: skewX(20deg);
    transform: skewY(10deg);
}
```

### 10.1.5. Multiple Transforms

```css
.box {
    /* Order matters! */
    transform: translate(50px, 50px) rotate(45deg) scale(1.5);

    /* Different order = different result */
    transform: rotate(45deg) translate(50px, 50px) scale(1.5);
}
```

## 10.2. 3D Transforms

### 10.2.1. perspective

```css
.container {
    perspective: 1000px;  /* Set 3D perspective */
}

.box {
    transform: rotateY(45deg);
}

/* Or on element itself */
.box {
    transform: perspective(1000px) rotateY(45deg);
}
```

### 10.2.2. rotateX(), rotateY(), rotateZ()

```css
.box {
    transform: rotateX(45deg);   /* Around X axis */
    transform: rotateY(45deg);   /* Around Y axis */
    transform: rotateZ(45deg);   /* Around Z axis (same as rotate()) */

    /* 3D rotation */
    transform: rotate3d(1, 1, 1, 45deg);  /* x, y, z, angle */
}
```

### 10.2.3. translateZ() và translate3d()

```css
.box {
    transform: translateZ(100px);  /* Move toward viewer */

    /* 3D translate */
    transform: translate3d(50px, 100px, 200px);  /* x, y, z */
}
```

### 10.2.4. scaleZ() và scale3d()

```css
.box {
    transform: scaleZ(2);
    transform: scale3d(1.5, 1.5, 2);  /* x, y, z */
}
```

## 10.3. Transform Properties

### 10.3.1. transform-origin

```css
.box {
    /* Default: center */
    transform-origin: center center;

    /* Keywords */
    transform-origin: top left;
    transform-origin: bottom right;
    transform-origin: center;

    /* Percentages */
    transform-origin: 50% 50%;

    /* Pixels */
    transform-origin: 10px 20px;

    /* 3D */
    transform-origin: 50% 50% 100px;
}

/* Example: Rotate from corner */
.box {
    transform-origin: top left;
    transform: rotate(45deg);
}
```

### 10.3.2. transform-style

```css
.parent {
    transform-style: flat;          /* Default */
    transform-style: preserve-3d;   /* Children in 3D space */
}
```

### 10.3.3. perspective-origin

```css
.container {
    perspective: 1000px;
    perspective-origin: 50% 50%;    /* Default: center */
    perspective-origin: left top;
    perspective-origin: 100px 200px;
}
```

### 10.3.4. backface-visibility

```css
.box {
    backface-visibility: visible;   /* Default */
    backface-visibility: hidden;    /* Hide when rotated */
}

/* Card flip example */
.card-front,
.card-back {
    backface-visibility: hidden;
}
```

## 10.4. Practical Examples

### 10.4.1. Hover Grow

```css
.button {
    transition: transform 0.3s ease;
}

.button:hover {
    transform: scale(1.1);
}
```

### 10.4.2. Card Flip

```css
.card-container {
    perspective: 1000px;
}

.card {
    width: 300px;
    height: 400px;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.6s;
}

.card:hover {
    transform: rotateY(180deg);
}

.card-front,
.card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
}

.card-back {
    transform: rotateY(180deg);
}
```

### 10.4.3. 3D Cube

```css
.cube-container {
    perspective: 1000px;
}

.cube {
    width: 200px;
    height: 200px;
    position: relative;
    transform-style: preserve-3d;
    animation: rotateCube 10s infinite linear;
}

@keyframes rotateCube {
    from { transform: rotateX(0deg) rotateY(0deg); }
    to { transform: rotateX(360deg) rotateY(360deg); }
}

.cube-face {
    position: absolute;
    width: 200px;
    height: 200px;
    border: 2px solid #333;
}

.cube-face.front  { transform: rotateY(0deg) translateZ(100px); }
.cube-face.back   { transform: rotateY(180deg) translateZ(100px); }
.cube-face.right  { transform: rotateY(90deg) translateZ(100px); }
.cube-face.left   { transform: rotateY(-90deg) translateZ(100px); }
.cube-face.top    { transform: rotateX(90deg) translateZ(100px); }
.cube-face.bottom { transform: rotateX(-90deg) translateZ(100px); }
```

### 10.4.4. Parallax Effect

```css
.parallax-layer {
    transform: translateZ(-500px) scale(1.5);
}

.parallax-container {
    perspective: 1000px;
    overflow-x: hidden;
    overflow-y: auto;
}
```

### 10.4.5. Skewed Section

```css
.section {
    position: relative;
    background: #3498db;
    padding: 100px 0;
}

.section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: inherit;
    transform: skewY(-3deg);
    transform-origin: top left;
}
```

### 10.4.6. Image Zoom on Hover

```css
.image-container {
    overflow: hidden;
}

.image-container img {
    transition: transform 0.5s ease;
}

.image-container:hover img {
    transform: scale(1.2);
}
```

### 10.4.7. Rotating Badge

```css
.badge {
    position: absolute;
    top: 20px;
    right: -40px;
    background: red;
    color: white;
    padding: 5px 40px;
    transform: rotate(45deg);
}
```

## 10.5. Animation with Transforms

```css
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
}

@keyframes flip {
    0% { transform: rotateY(0deg); }
    100% { transform: rotateY(360deg); }
}

.spinning {
    animation: spin 2s linear infinite;
}
```

## 10.6. Performance Tips

```css
/* Good: Use transform for movement */
.box {
    transform: translate(100px, 100px);
}

/* Avoid: Position properties (cause reflow) */
.box {
    top: 100px;
    left: 100px;
}

/* Use will-change for complex transforms */
.box {
    will-change: transform;
}

/* Use transform: translate3d for hardware acceleration */
.box {
    transform: translate3d(100px, 100px, 0);
}
```

## 10.7. Matrix Transform

```css
/* Advanced: matrix transformation */
.box {
    transform: matrix(a, b, c, d, tx, ty);
    transform: matrix3d(...); /* 16 values */
}

/* Equivalent transformations */
transform: translate(50px, 100px);
/* Same as */
transform: matrix(1, 0, 0, 1, 50, 100);
```

---

**Kết luận:** Transforms cho phép manipulate elements trong 2D và 3D space. Essential cho animations và interactive effects. Transform and opacity là hai properties performant nhất để animate.

**Chương tiếp theo:** Media Queries & Responsive Design
