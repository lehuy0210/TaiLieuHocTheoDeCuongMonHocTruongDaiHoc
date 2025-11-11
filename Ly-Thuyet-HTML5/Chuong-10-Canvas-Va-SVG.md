# CHƯƠNG 10: CANVAS VÀ SVG

## 10.1. HTML5 Canvas

### 10.1.1. Canvas Element

```html
<canvas id="myCanvas" width="500" height="300">
    Your browser does not support canvas
</canvas>
```

### 10.1.2. Drawing Context

```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
```

### 10.1.3. Drawing Shapes

**Rectangles:**
```javascript
// Fill rectangle
ctx.fillStyle = 'red';
ctx.fillRect(10, 10, 100, 50);

// Stroke rectangle
ctx.strokeStyle = 'blue';
ctx.lineWidth = 2;
ctx.strokeRect(150, 10, 100, 50);

// Clear rectangle
ctx.clearRect(20, 20, 80, 30);
```

**Paths:**
```javascript
ctx.beginPath();
ctx.moveTo(50, 50);
ctx.lineTo(150, 50);
ctx.lineTo(100, 150);
ctx.closePath();
ctx.fillStyle = 'green';
ctx.fill();
ctx.stroke();
```

**Circles:**
```javascript
ctx.beginPath();
ctx.arc(250, 100, 50, 0, 2 * Math.PI);
ctx.fillStyle = 'purple';
ctx.fill();
```

**Bezier Curves:**
```javascript
ctx.beginPath();
ctx.moveTo(50, 200);
ctx.quadraticCurveTo(150, 100, 250, 200);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(50, 250);
ctx.bezierCurveTo(100, 200, 200, 300, 250, 250);
ctx.stroke();
```

### 10.1.4. Text

```javascript
ctx.font = '30px Arial';
ctx.fillStyle = 'black';
ctx.fillText('Hello Canvas', 10, 50);

ctx.strokeStyle = 'red';
ctx.strokeText('Outlined Text', 10, 100);

// Text alignment
ctx.textAlign = 'center'; // left, right, center, start, end
ctx.textBaseline = 'middle'; // top, hanging, middle, alphabetic, bottom

// Measure text
const metrics = ctx.measureText('Hello');
console.log('Width:', metrics.width);
```

### 10.1.5. Gradients

**Linear Gradient:**
```javascript
const gradient = ctx.createLinearGradient(0, 0, 200, 0);
gradient.addColorStop(0, 'red');
gradient.addColorStop(0.5, 'yellow');
gradient.addColorStop(1, 'blue');

ctx.fillStyle = gradient;
ctx.fillRect(10, 10, 200, 100);
```

**Radial Gradient:**
```javascript
const radialGrad = ctx.createRadialGradient(100, 100, 10, 100, 100, 80);
radialGrad.addColorStop(0, 'white');
radialGrad.addColorStop(1, 'blue');

ctx.fillStyle = radialGrad;
ctx.fillRect(0, 0, 200, 200);
```

### 10.1.6. Images

```javascript
const img = new Image();
img.src = 'image.jpg';

img.onload = () => {
    // Draw image
    ctx.drawImage(img, 0, 0);

    // Draw with size
    ctx.drawImage(img, 0, 0, 200, 100);

    // Slice and draw
    ctx.drawImage(img,
        50, 50, 100, 100,    // Source
        10, 10, 200, 200      // Destination
    );
};
```

### 10.1.7. Transformations

```javascript
// Translate
ctx.translate(50, 50);

// Rotate
ctx.rotate(Math.PI / 4); // 45 degrees

// Scale
ctx.scale(1.5, 1.5);

// Save and restore state
ctx.save();
ctx.translate(100, 100);
ctx.fillRect(0, 0, 50, 50);
ctx.restore(); // Restore to saved state
```

### 10.1.8. Compositing

```javascript
ctx.globalAlpha = 0.5; // Transparency

ctx.globalCompositeOperation = 'source-over';
// source-over, destination-over, source-atop, destination-atop,
// lighter, copy, xor, multiply, screen, overlay, etc.
```

### 10.1.9. Pixel Manipulation

```javascript
// Get image data
const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
const data = imageData.data; // [r, g, b, a, r, g, b, a, ...]

// Modify pixels (grayscale)
for (let i = 0; i < data.length; i += 4) {
    const avg = (data[i] + data[i + 1] + data[i + 2]) / 3;
    data[i] = avg;       // R
    data[i + 1] = avg;   // G
    data[i + 2] = avg;   // B
}

// Put image data back
ctx.putImageData(imageData, 0, 0);

// Create new image data
const newImageData = ctx.createImageData(100, 100);
```

### 10.1.10. Canvas Examples

**Draw Clock:**
```javascript
function drawClock() {
    const now = new Date();
    const hours = now.getHours() % 12;
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Clock face
    ctx.beginPath();
    ctx.arc(250, 250, 200, 0, 2 * Math.PI);
    ctx.fillStyle = 'white';
    ctx.fill();
    ctx.stroke();

    // Hour hand
    ctx.save();
    ctx.translate(250, 250);
    ctx.rotate((hours * 30 + minutes / 2) * Math.PI / 180);
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, -100);
    ctx.lineWidth = 6;
    ctx.stroke();
    ctx.restore();

    // Minute hand
    ctx.save();
    ctx.translate(250, 250);
    ctx.rotate((minutes * 6) * Math.PI / 180);
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, -150);
    ctx.lineWidth = 4;
    ctx.stroke();
    ctx.restore();

    // Second hand
    ctx.save();
    ctx.translate(250, 250);
    ctx.rotate((seconds * 6) * Math.PI / 180);
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, -170);
    ctx.strokeStyle = 'red';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.restore();

    requestAnimationFrame(drawClock);
}

drawClock();
```

**Drawing App:**
```javascript
let isDrawing = false;
let lastX = 0;
let lastY = 0;

canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mousemove', (e) => {
    if (!isDrawing) return;

    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();

    [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseout', () => isDrawing = false);
```

## 10.2. SVG - Scalable Vector Graphics

### 10.2.1. SVG Basics

```html
<svg width="200" height="200">
    <circle cx="100" cy="100" r="80" fill="blue" />
</svg>
```

### 10.2.2. SVG Shapes

**Rectangle:**
```html
<svg width="300" height="200">
    <rect x="10" y="10" width="200" height="100"
          fill="blue" stroke="black" stroke-width="2" />
</svg>
```

**Circle:**
```html
<svg width="200" height="200">
    <circle cx="100" cy="100" r="50"
            fill="red" stroke="black" stroke-width="2" />
</svg>
```

**Ellipse:**
```html
<svg width="300" height="200">
    <ellipse cx="150" cy="100" rx="100" ry="50"
             fill="green" />
</svg>
```

**Line:**
```html
<svg width="200" height="200">
    <line x1="10" y1="10" x2="190" y2="190"
          stroke="black" stroke-width="2" />
</svg>
```

**Polyline:**
```html
<svg width="300" height="200">
    <polyline points="10,10 50,50 50,100 100,50"
              fill="none" stroke="blue" stroke-width="2" />
</svg>
```

**Polygon:**
```html
<svg width="200" height="200">
    <polygon points="100,10 40,180 190,60 10,60 160,180"
             fill="yellow" stroke="black" stroke-width="2" />
</svg>
```

**Path:**
```html
<svg width="200" height="200">
    <path d="M 10 10 L 90 90 L 10 90 Z"
          fill="purple" stroke="black" stroke-width="2" />
</svg>
```

### 10.2.3. SVG Text

```html
<svg width="300" height="100">
    <text x="10" y="50" font-family="Arial" font-size="24" fill="blue">
        Hello SVG
    </text>

    <!-- Text on path -->
    <defs>
        <path id="textPath" d="M 10,50 Q 100,10 190,50" />
    </defs>
    <text>
        <textPath href="#textPath">
            Text along a curve
        </textPath>
    </text>
</svg>
```

### 10.2.4. SVG Gradients

**Linear Gradient:**
```html
<svg width="200" height="100">
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
            <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="100" fill="url(#grad1)" />
</svg>
```

**Radial Gradient:**
```html
<svg width="200" height="200">
    <defs>
        <radialGradient id="grad2">
            <stop offset="0%" style="stop-color:white" />
            <stop offset="100%" style="stop-color:blue" />
        </radialGradient>
    </defs>
    <circle cx="100" cy="100" r="80" fill="url(#grad2)" />
</svg>
```

### 10.2.5. SVG Filters

**Blur:**
```html
<svg width="200" height="200">
    <defs>
        <filter id="blur">
            <feGaussianBlur in="SourceGraphic" stdDeviation="5" />
        </filter>
    </defs>
    <circle cx="100" cy="100" r="50" fill="blue" filter="url(#blur)" />
</svg>
```

**Drop Shadow:**
```html
<defs>
    <filter id="shadow">
        <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.5"/>
    </filter>
</defs>
<rect width="100" height="100" fill="red" filter="url(#shadow)" />
```

### 10.2.6. SVG Animations

**Animate:**
```html
<svg width="200" height="200">
    <circle cx="50" cy="100" r="20" fill="blue">
        <animate attributeName="cx"
                 from="50" to="150"
                 dur="2s"
                 repeatCount="indefinite" />
    </circle>
</svg>
```

**AnimateTransform:**
```html
<rect width="50" height="50" fill="red">
    <animateTransform attributeName="transform"
                      type="rotate"
                      from="0 25 25" to="360 25 25"
                      dur="3s"
                      repeatCount="indefinite" />
</rect>
```

### 10.2.7. SVG with JavaScript

```html
<svg id="mySVG" width="200" height="200">
    <circle id="myCircle" cx="100" cy="100" r="50" fill="blue" />
</svg>

<script>
const circle = document.getElementById('myCircle');

// Change attributes
circle.setAttribute('fill', 'red');
circle.setAttribute('r', '70');

// Add event listeners
circle.addEventListener('click', () => {
    circle.style.fill = circle.style.fill === 'red' ? 'blue' : 'red';
});

// Create SVG element
const svg = document.getElementById('mySVG');
const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
rect.setAttribute('x', '10');
rect.setAttribute('y', '10');
rect.setAttribute('width', '50');
rect.setAttribute('height', '50');
rect.setAttribute('fill', 'green');
svg.appendChild(rect);
</script>
```

## 10.3. Canvas vs SVG

| Feature | Canvas | SVG |
|---------|--------|-----|
| Type | Raster (pixel-based) | Vector |
| Scalability | Loses quality when scaled | Scales without quality loss |
| Performance | Better for many objects | Better for few complex objects |
| Interaction | Manual pixel detection | Built-in events on elements |
| File Size | Smaller for complex images | Larger for complex images |
| Text | Harder to handle | Easy to handle, selectable |
| DOM | Not part of DOM | Part of DOM |
| Best For | Games, pixel manipulation, charts | Icons, logos, illustrations |

## 10.4. Practical Examples

### 10.4.1. Chart với Canvas

```javascript
function drawBarChart(data) {
    const barWidth = 50;
    const barGap = 10;
    const maxValue = Math.max(...data);

    data.forEach((value, index) => {
        const barHeight = (value / maxValue) * 200;
        const x = index * (barWidth + barGap);
        const y = 250 - barHeight;

        ctx.fillStyle = 'blue';
        ctx.fillRect(x, y, barWidth, barHeight);

        ctx.fillStyle = 'black';
        ctx.fillText(value, x + 15, y - 5);
    });
}

drawBarChart([50, 80, 120, 90, 150]);
```

### 10.4.2. Icon System với SVG

```html
<!-- Define symbols -->
<svg style="display: none;">
    <symbol id="icon-home" viewBox="0 0 24 24">
        <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/>
    </symbol>
    <symbol id="icon-search" viewBox="0 0 24 24">
        <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
    </symbol>
</svg>

<!-- Use icons -->
<svg width="24" height="24"><use href="#icon-home" /></svg>
<svg width="24" height="24"><use href="#icon-search" /></svg>
```

## 10.5. Bài tập thực hành

### Bài 1: Drawing App
Tạo ứng dụng vẽ với Canvas (pen, eraser, colors)

### Bài 2: Animated Clock
Tạo đồng hồ analog với Canvas hoặc SVG

### Bài 3: Interactive Chart
Tạo chart với tooltips và animations

### Bài 4: SVG Icon Library
Tạo thư viện icon SVG có thể tái sử dụng

---

**Kết luận:** Canvas phù hợp cho pixel manipulation và games, SVG tốt cho graphics có thể scale và interactive elements. Hiểu rõ điểm mạnh của từng công nghệ giúp chọn đúng tool cho project.
