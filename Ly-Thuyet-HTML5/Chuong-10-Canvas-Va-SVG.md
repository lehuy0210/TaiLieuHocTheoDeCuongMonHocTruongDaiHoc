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

## 10.5. Use Cases Thực Tế

### 10.5.1. Data Visualization Dashboard (Canvas)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Sales Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        #dashboard { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
        .chart-container { border: 1px solid #ddd; padding: 15px; border-radius: 8px; }
        canvas { border: 1px solid #eee; }
    </style>
</head>
<body>
    <h1>Sales Dashboard</h1>
    <div id="dashboard">
        <div class="chart-container">
            <h3>Monthly Revenue</h3>
            <canvas id="barChart" width="400" height="300"></canvas>
        </div>
        <div class="chart-container">
            <h3>Sales Distribution</h3>
            <canvas id="pieChart" width="400" height="300"></canvas>
        </div>
    </div>

    <script>
    // Bar Chart
    function drawBarChart() {
        const canvas = document.getElementById('barChart');
        const ctx = canvas.getContext('2d');
        const data = [65, 80, 120, 95, 150, 110];
        const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'];
        const colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'];

        const barWidth = 50;
        const spacing = 15;
        const maxValue = Math.max(...data);
        const chartHeight = 250;

        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw bars
        data.forEach((value, index) => {
            const barHeight = (value / maxValue) * chartHeight;
            const x = index * (barWidth + spacing) + spacing;
            const y = canvas.height - barHeight - 30;

            // Draw bar
            ctx.fillStyle = colors[index];
            ctx.fillRect(x, y, barWidth, barHeight);

            // Draw value
            ctx.fillStyle = '#000';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(value, x + barWidth/2, y - 5);

            // Draw label
            ctx.fillText(labels[index], x + barWidth/2, canvas.height - 10);
        });

        // Draw title
        ctx.font = 'bold 14px Arial';
        ctx.fillText('Revenue ($1000)', canvas.width/2, 20);
    }

    // Pie Chart
    function drawPieChart() {
        const canvas = document.getElementById('pieChart');
        const ctx = canvas.getContext('2d');
        const data = [30, 20, 25, 15, 10];
        const labels = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'];
        const colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'];

        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = 100;

        let currentAngle = -Math.PI / 2;
        const total = data.reduce((a, b) => a + b, 0);

        data.forEach((value, index) => {
            const sliceAngle = (value / total) * 2 * Math.PI;

            // Draw slice
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
            ctx.closePath();
            ctx.fillStyle = colors[index];
            ctx.fill();

            // Draw label
            const labelAngle = currentAngle + sliceAngle / 2;
            const labelX = centerX + Math.cos(labelAngle) * (radius + 30);
            const labelY = centerY + Math.sin(labelAngle) * (radius + 30);

            ctx.fillStyle = '#000';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`${labels[index]}: ${value}%`, labelX, labelY);

            currentAngle += sliceAngle;
        });
    }

    // Initialize charts
    drawBarChart();
    drawPieChart();
    </script>
</body>
</html>
```

### 10.5.2. Interactive Game (Canvas)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Snake Game</title>
    <style>
        body { display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #000; }
        canvas { border: 2px solid #fff; }
        #gameInfo { color: #fff; text-align: center; margin-bottom: 20px; font-family: Arial; }
    </style>
</head>
<body>
    <div>
        <div id="gameInfo">
            <h2>Snake Game</h2>
            <p>Score: <span id="score">0</span></p>
            <p>Use Arrow Keys to Control</p>
        </div>
        <canvas id="gameCanvas" width="400" height="400"></canvas>
    </div>

    <script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const scoreElement = document.getElementById('score');

    const gridSize = 20;
    const tileCount = canvas.width / gridSize;

    let snake = [{x: 10, y: 10}];
    let food = {x: 15, y: 15};
    let dx = 0, dy = 0;
    let score = 0;

    document.addEventListener('keydown', changeDirection);

    function changeDirection(event) {
        const LEFT = 37, UP = 38, RIGHT = 39, DOWN = 40;

        const keyPressed = event.keyCode;
        const goingUp = dy === -1;
        const goingDown = dy === 1;
        const goingRight = dx === 1;
        const goingLeft = dx === -1;

        if (keyPressed === LEFT && !goingRight) { dx = -1; dy = 0; }
        if (keyPressed === UP && !goingDown) { dx = 0; dy = -1; }
        if (keyPressed === RIGHT && !goingLeft) { dx = 1; dy = 0; }
        if (keyPressed === DOWN && !goingUp) { dx = 0; dy = 1; }
    }

    function gameLoop() {
        update();
        draw();
        setTimeout(gameLoop, 100);
    }

    function update() {
        const head = {x: snake[0].x + dx, y: snake[0].y + dy};

        // Check wall collision
        if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
            resetGame();
            return;
        }

        // Check self collision
        for (let segment of snake) {
            if (head.x === segment.x && head.y === segment.y) {
                resetGame();
                return;
            }
        }

        snake.unshift(head);

        // Check food collision
        if (head.x === food.x && head.y === food.y) {
            score++;
            scoreElement.textContent = score;
            placeFood();
        } else {
            snake.pop();
        }
    }

    function draw() {
        // Clear canvas
        ctx.fillStyle = '#000';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw snake
        ctx.fillStyle = '#0f0';
        for (let segment of snake) {
            ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize - 2, gridSize - 2);
        }

        // Draw food
        ctx.fillStyle = '#f00';
        ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
    }

    function placeFood() {
        food = {
            x: Math.floor(Math.random() * tileCount),
            y: Math.floor(Math.random() * tileCount)
        };
    }

    function resetGame() {
        snake = [{x: 10, y: 10}];
        dx = 0;
        dy = 0;
        score = 0;
        scoreElement.textContent = score;
        placeFood();
    }

    gameLoop();
    </script>
</body>
</html>
```

### 10.5.3. Icon System với SVG

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>SVG Icon System</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 40px; }
        .icon-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 20px; }
        .icon-item { text-align: center; padding: 20px; border: 1px solid #eee; border-radius: 8px; }
        .icon { width: 48px; height: 48px; fill: #333; }
        .icon-item:hover .icon { fill: #007bff; }
        .icon-label { margin-top: 10px; font-size: 14px; }

        /* Icon variations */
        .icon-small { width: 24px; height: 24px; }
        .icon-large { width: 64px; height: 64px; }
        .icon-primary { fill: #007bff; }
        .icon-success { fill: #28a745; }
        .icon-danger { fill: #dc3545; }
    </style>
</head>
<body>
    <h1>SVG Icon System</h1>

    <!-- Define SVG symbols -->
    <svg style="display: none;">
        <!-- Home Icon -->
        <symbol id="icon-home" viewBox="0 0 24 24">
            <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/>
        </symbol>

        <!-- Search Icon -->
        <symbol id="icon-search" viewBox="0 0 24 24">
            <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
        </symbol>

        <!-- Settings Icon -->
        <symbol id="icon-settings" viewBox="0 0 24 24">
            <path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.07-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.74,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.07,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.47-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/>
        </symbol>

        <!-- User Icon -->
        <symbol id="icon-user" viewBox="0 0 24 24">
            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
        </symbol>

        <!-- Mail Icon -->
        <symbol id="icon-mail" viewBox="0 0 24 24">
            <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
        </symbol>

        <!-- Heart Icon -->
        <symbol id="icon-heart" viewBox="0 0 24 24">
            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </symbol>
    </svg>

    <div class="icon-grid">
        <div class="icon-item">
            <svg class="icon"><use href="#icon-home" /></svg>
            <div class="icon-label">Home</div>
        </div>

        <div class="icon-item">
            <svg class="icon icon-primary"><use href="#icon-search" /></svg>
            <div class="icon-label">Search (Primary)</div>
        </div>

        <div class="icon-item">
            <svg class="icon icon-success"><use href="#icon-settings" /></svg>
            <div class="icon-label">Settings (Success)</div>
        </div>

        <div class="icon-item">
            <svg class="icon"><use href="#icon-user" /></svg>
            <div class="icon-label">User</div>
        </div>

        <div class="icon-item">
            <svg class="icon"><use href="#icon-mail" /></svg>
            <div class="icon-label">Mail</div>
        </div>

        <div class="icon-item">
            <svg class="icon icon-danger"><use href="#icon-heart" /></svg>
            <div class="icon-label">Heart (Danger)</div>
        </div>
    </div>

    <h2 style="margin-top: 40px;">Icon Sizes</h2>
    <div style="display: flex; gap: 20px; align-items: center;">
        <div>
            <svg class="icon icon-small"><use href="#icon-home" /></svg>
            <div>Small (24px)</div>
        </div>
        <div>
            <svg class="icon"><use href="#icon-home" /></svg>
            <div>Medium (48px)</div>
        </div>
        <div>
            <svg class="icon icon-large"><use href="#icon-home" /></svg>
            <div>Large (64px)</div>
        </div>
    </div>
</body>
</html>
```

### 10.5.4. Animated Logo với SVG

```html
<!DOCTYPE html>
<html>
<head>
    <title>Animated SVG Logo</title>
    <style>
        body { display: flex; justify-content: center; align-items: center; height: 100vh; background: #f0f0f0; }
        .logo-container { text-align: center; }
        #logo { width: 300px; height: 300px; }

        /* Animations */
        .circle { animation: pulse 2s ease-in-out infinite; }
        @keyframes pulse {
            0%, 100% { r: 40; opacity: 1; }
            50% { r: 50; opacity: 0.7; }
        }

        .star { animation: rotate 4s linear infinite; }
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="logo-container">
        <svg id="logo" viewBox="0 0 200 200">
            <!-- Background circle -->
            <circle cx="100" cy="100" r="80" fill="#007bff" opacity="0.1"/>

            <!-- Animated circles -->
            <circle class="circle" cx="100" cy="100" r="40" fill="none" stroke="#007bff" stroke-width="3">
                <animate attributeName="r" values="40;50;40" dur="2s" repeatCount="indefinite"/>
                <animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite"/>
            </circle>

            <!-- Rotating star -->
            <g class="star" transform-origin="100 100">
                <path d="M100,50 L110,80 L140,90 L115,110 L120,140 L100,125 L80,140 L85,110 L60,90 L90,80 Z"
                      fill="#ffc107">
                    <animateTransform attributeName="transform" type="rotate"
                                      from="0 100 100" to="360 100 100"
                                      dur="4s" repeatCount="indefinite"/>
                </path>
            </g>

            <!-- Company name -->
            <text x="100" y="180" font-family="Arial, sans-serif" font-size="24"
                  font-weight="bold" fill="#333" text-anchor="middle">
                LOGO
                <animate attributeName="opacity" values="1;0.5;1" dur="3s" repeatCount="indefinite"/>
            </text>
        </svg>
        <p style="color: #666; margin-top: 20px;">Animated SVG Logo</p>
    </div>
</body>
</html>
```

### 10.5.5. Signature Pad (Canvas)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Signature Pad</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; max-width: 800px; margin: 0 auto; }
        h1 { color: #333; }
        #signatureCanvas { border: 2px solid #007bff; border-radius: 8px; cursor: crosshair; background: #fff; }
        .controls { margin-top: 20px; display: flex; gap: 10px; }
        button { padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 14px; }
        .btn-clear { background: #dc3545; color: white; }
        .btn-save { background: #28a745; color: white; }
        .btn-color { background: #007bff; color: white; }
        input[type="color"] { height: 40px; width: 60px; border: none; cursor: pointer; }
        .pen-width { display: flex; align-items: center; gap: 10px; }
    </style>
</head>
<body>
    <h1>Signature Pad</h1>
    <p>Sign below using your mouse or touch:</p>

    <canvas id="signatureCanvas" width="760" height="400"></canvas>

    <div class="controls">
        <button class="btn-clear" onclick="clearSignature()">Clear</button>
        <button class="btn-save" onclick="saveSignature()">Save as Image</button>
        <div class="pen-width">
            <label>Pen Width:</label>
            <input type="range" id="penWidth" min="1" max="10" value="2" oninput="updatePenWidth()">
            <span id="widthValue">2px</span>
        </div>
        <div>
            <label>Color:</label>
            <input type="color" id="penColor" value="#000000" onchange="updatePenColor()">
        </div>
    </div>

    <script>
    const canvas = document.getElementById('signatureCanvas');
    const ctx = canvas.getContext('2d');
    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;
    let penWidth = 2;
    let penColor = '#000000';

    // Set up canvas
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    // Mouse events
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing);

    // Touch events
    canvas.addEventListener('touchstart', (e) => {
        e.preventDefault();
        const touch = e.touches[0];
        const rect = canvas.getBoundingClientRect();
        lastX = touch.clientX - rect.left;
        lastY = touch.clientY - rect.top;
        isDrawing = true;
    });

    canvas.addEventListener('touchmove', (e) => {
        e.preventDefault();
        if (!isDrawing) return;
        const touch = e.touches[0];
        const rect = canvas.getBoundingClientRect();
        const x = touch.clientX - rect.left;
        const y = touch.clientY - rect.top;

        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.strokeStyle = penColor;
        ctx.lineWidth = penWidth;
        ctx.stroke();

        lastX = x;
        lastY = y;
    });

    canvas.addEventListener('touchend', () => {
        isDrawing = false;
    });

    function startDrawing(e) {
        isDrawing = true;
        lastX = e.offsetX;
        lastY = e.offsetY;
    }

    function draw(e) {
        if (!isDrawing) return;

        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.strokeStyle = penColor;
        ctx.lineWidth = penWidth;
        ctx.stroke();

        lastX = e.offsetX;
        lastY = e.offsetY;
    }

    function stopDrawing() {
        isDrawing = false;
    }

    function clearSignature() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function saveSignature() {
        const dataURL = canvas.toDataURL('image/png');
        const link = document.createElement('a');
        link.download = 'signature.png';
        link.href = dataURL;
        link.click();
    }

    function updatePenWidth() {
        penWidth = document.getElementById('penWidth').value;
        document.getElementById('widthValue').textContent = penWidth + 'px';
    }

    function updatePenColor() {
        penColor = document.getElementById('penColor').value;
    }
    </script>
</body>
</html>
```

## 10.6. Tips & Tricks

### Tip 1: Canvas Performance - Clear only dirty regions
```javascript
// Thay vì clear toàn bộ canvas
ctx.clearRect(0, 0, canvas.width, canvas.height);

// Clear chỉ vùng cần thiết
ctx.clearRect(dirtyX, dirtyY, dirtyWidth, dirtyHeight);
```

### Tip 2: Use requestAnimationFrame cho animations
```javascript
// Tốt hơn setTimeout/setInterval
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    // Draw code here
    requestAnimationFrame(animate);
}
animate();
```

### Tip 3: SVG - Optimize path data
```html
<!-- Before -->
<path d="M 10 10 L 20 20 L 30 10 Z"/>

<!-- After - more concise -->
<path d="M10 10L20 20L30 10Z"/>
```

### Tip 4: Canvas - Save/Restore context
```javascript
ctx.save(); // Save current state
ctx.translate(100, 100);
ctx.rotate(Math.PI / 4);
// ... drawing code
ctx.restore(); // Restore to saved state
```

### Tip 5: SVG - Use <defs> for reusable elements
```html
<svg>
    <defs>
        <linearGradient id="grad1">
            <stop offset="0%" stop-color="red"/>
            <stop offset="100%" stop-color="blue"/>
        </linearGradient>
    </defs>
    <rect fill="url(#grad1)" width="200" height="100"/>
</svg>
```

### Tip 6: Canvas - Batch operations
```javascript
// Hiệu quả hơn
ctx.beginPath();
for (let i = 0; i < 1000; i++) {
    ctx.rect(i * 10, i * 10, 10, 10);
}
ctx.fill();

// Kém hiệu quả
for (let i = 0; i < 1000; i++) {
    ctx.fillRect(i * 10, i * 10, 10, 10);
}
```

### Tip 7: SVG - Use CSS for styling
```html
<style>
.my-circle { fill: blue; }
.my-circle:hover { fill: red; }
</style>
<circle class="my-circle" cx="50" cy="50" r="40"/>
```

### Tip 8: Canvas - Offscreen rendering
```javascript
// Create offscreen canvas for complex shapes
const offscreen = document.createElement('canvas');
const offCtx = offscreen.getContext('2d');
// Draw complex shape once
// Then use drawImage() to copy it multiple times
ctx.drawImage(offscreen, x, y);
```

### Tip 9: SVG viewBox cho responsive
```html
<!-- Scales automatically -->
<svg viewBox="0 0 100 100" width="100%" height="100%">
    <circle cx="50" cy="50" r="40"/>
</svg>
```

### Tip 10: Canvas - Use multiple layers
```html
<!-- Separate static and dynamic content -->
<canvas id="background"></canvas>
<canvas id="foreground" style="position: absolute; top: 0;"></canvas>
```

## 10.7. Common Mistakes

### Mistake 1: Forgetting to begin new path
```javascript
// ✗ SAI: All shapes connected
ctx.moveTo(10, 10);
ctx.lineTo(50, 50);
ctx.moveTo(100, 100);
ctx.lineTo(150, 150);
ctx.stroke();

// ✓ ĐÚNG: Separate paths
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(50, 50);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(100, 100);
ctx.lineTo(150, 150);
ctx.stroke();
```

### Mistake 2: Not setting canvas size properly
```html
<!-- ✗ SAI: CSS size không khớp -->
<canvas width="300" height="200" style="width: 600px; height: 400px;"></canvas>

<!-- ✓ ĐÚNG: Match canvas and display size -->
<canvas id="canvas" width="600" height="400"></canvas>
```

### Mistake 3: SVG - Forgetting viewBox
```html
<!-- ✗ SAI: Not scalable -->
<svg width="200" height="200">
    <circle cx="100" cy="100" r="50"/>
</svg>

<!-- ✓ ĐÚNG: Scalable -->
<svg viewBox="0 0 200 200" width="200" height="200">
    <circle cx="100" cy="100" r="50"/>
</svg>
```

### Mistake 4: Canvas - Not clearing before redraw
```javascript
// ✗ SAI: Trails left behind
function animate() {
    // ctx.clearRect() missing!
    drawCircle();
    requestAnimationFrame(animate);
}

// ✓ ĐÚNG
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawCircle();
    requestAnimationFrame(animate);
}
```

### Mistake 5: SVG - Incorrect coordinate system
```html
<!-- ✗ SAI: Negative coordinates may be clipped -->
<svg width="100" height="100">
    <circle cx="-10" cy="-10" r="20"/>
</svg>

<!-- ✓ ĐÚNG: Adjust viewBox -->
<svg viewBox="-50 -50 100 100" width="100" height="100">
    <circle cx="-10" cy="-10" r="20"/>
</svg>
```

### Mistake 6: Canvas - Memory leaks with images
```javascript
// ✗ SAI: Loading image multiple times
function draw() {
    const img = new Image();
    img.src = 'image.jpg'; // Loaded every frame!
    img.onload = () => ctx.drawImage(img, 0, 0);
}

// ✓ ĐÚNG: Load once
const img = new Image();
img.src = 'image.jpg';
img.onload = () => draw();

function draw() {
    ctx.drawImage(img, 0, 0);
}
```

### Mistake 7: Not handling retina displays
```javascript
// ✗ SAI: Blurry on retina
canvas.width = 400;
canvas.height = 300;

// ✓ ĐÚNG: Account for device pixel ratio
const dpr = window.devicePixelRatio || 1;
canvas.width = 400 * dpr;
canvas.height = 300 * dpr;
canvas.style.width = '400px';
canvas.style.height = '300px';
ctx.scale(dpr, dpr);
```

### Mistake 8: SVG - Inefficient animations
```html
<!-- ✗ SAI: Animating transform attribute -->
<circle cx="50" cy="50" r="20">
    <animateTransform attributeName="transform" type="translate" from="0 0" to="100 0"/>
</circle>

<!-- ✓ ĐÚNG: Animate cx directly -->
<circle cy="50" r="20">
    <animate attributeName="cx" from="50" to="150" dur="2s"/>
</circle>
```

### Mistake 9: Canvas - Wrong composite operation
```javascript
// ✗ SAI: Unexpected blending
ctx.globalCompositeOperation = 'multiply';
// Draw something
// Forgot to reset!
ctx.fillRect(0, 0, 100, 100); // Unexpected result

// ✓ ĐÚNG: Reset after use
ctx.globalCompositeOperation = 'multiply';
// Draw something
ctx.globalCompositeOperation = 'source-over'; // Reset to default
```

### Mistake 10: Not optimizing SVG file size
```html
<!-- ✗ SAI: Unnecessary precision -->
<path d="M 10.123456789 10.987654321 L 20.456789012 30.123456789"/>

<!-- ✓ ĐÚNG: Round to reasonable precision -->
<path d="M 10.12 10.99 L 20.46 30.12"/>
```

## 10.8. Troubleshooting

### Issue 1: Canvas appears blurry
**Problem:** Canvas looks fuzzy/blurry

**Solutions:**
```javascript
// 1. Account for device pixel ratio
const dpr = window.devicePixelRatio || 1;
canvas.width = desiredWidth * dpr;
canvas.height = desiredHeight * dpr;
canvas.style.width = desiredWidth + 'px';
canvas.style.height = desiredHeight + 'px';
ctx.scale(dpr, dpr);

// 2. Disable image smoothing for pixel art
ctx.imageSmoothingEnabled = false;
```

### Issue 2: SVG not scaling properly
**Problem:** SVG doesn't resize correctly

**Solution:**
```html
<!-- Add viewBox and remove fixed width/height -->
<svg viewBox="0 0 200 200" width="100%" height="auto">
    <!-- content -->
</svg>
```

### Issue 3: Canvas animation lag
**Problem:** Animation stutters or drops frames

**Solutions:**
```javascript
// 1. Use requestAnimationFrame
function animate() {
    requestAnimationFrame(animate);
    render();
}

// 2. Implement delta time
let lastTime = 0;
function animate(currentTime) {
    const deltaTime = currentTime - lastTime;
    lastTime = currentTime;
    update(deltaTime);
    render();
    requestAnimationFrame(animate);
}

// 3. Batch operations
// Draw all similar shapes in one pass
```

### Issue 4: SVG not displaying in IE
**Problem:** SVG doesn't show in Internet Explorer

**Solution:**
```html
<!-- Add explicit dimensions -->
<svg width="200" height="200" viewBox="0 0 200 200">
    <!-- content -->
</svg>

<!-- Or use CSS -->
<style>
svg { width: 200px; height: 200px; }
</style>
```

### Issue 5: Canvas memory issues
**Problem:** Browser crashes with large canvas

**Solutions:**
```javascript
// 1. Limit canvas size
const MAX_SIZE = 4096;
if (width > MAX_SIZE) width = MAX_SIZE;
if (height > MAX_SIZE) height = MAX_SIZE;

// 2. Use multiple smaller canvases
// 3. Clear canvas when not in use
canvas.width = canvas.width; // Quick clear and reset
```

## 10.9. Advanced Topics

### 10.9.1. Canvas WebGL Context
```javascript
const gl = canvas.getContext('webgl');
// High-performance 3D graphics
```

### 10.9.2. SVG Filters
```html
<svg>
    <defs>
        <filter id="glow">
            <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <circle cx="100" cy="100" r="50" fill="yellow" filter="url(#glow)"/>
</svg>
```

### 10.9.3. Canvas Image Processing
```javascript
const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
const data = imageData.data;

// Grayscale filter
for (let i = 0; i < data.length; i += 4) {
    const avg = (data[i] + data[i+1] + data[i+2]) / 3;
    data[i] = data[i+1] = data[i+2] = avg;
}

ctx.putImageData(imageData, 0, 0);
```

### 10.9.4. SVG Path Morphing
```html
<svg>
    <path d="M10,10 L50,10 L50,50 L10,50 Z">
        <animate attributeName="d"
                 from="M10,10 L50,10 L50,50 L10,50 Z"
                 to="M30,10 L50,30 L30,50 L10,30 Z"
                 dur="2s" repeatCount="indefinite"/>
    </path>
</svg>
```

### 10.9.5. Canvas Custom Patterns
```javascript
const pattern = ctx.createPattern(image, 'repeat');
ctx.fillStyle = pattern;
ctx.fillRect(0, 0, canvas.width, canvas.height);
```

## 10.10. Bài Tập Thực Hành (Mở Rộng)

### Bài 1: Drawing App
**Yêu cầu:**
- Canvas drawing với pen, eraser
- Color picker và pen size slider
- Clear, undo, redo functions
- Save as image
- Touch support cho mobile

### Bài 2: Animated Clock
**Yêu cầu:**
- Analog clock với Canvas hoặc SVG
- Real-time updates mỗi giây
- Hour, minute, second hands
- Số và marks trên mặt đồng hồ
- Smooth animations

### Bài 3: Interactive Chart Library
**Yêu cầu:**
- Bar chart, line chart, pie chart
- Tooltips khi hover
- Animated transitions
- Responsive design
- Export chart as image

### Bài 4: SVG Icon Library
**Yêu cầu:**
- Tạo 20+ icons
- Icon system với <symbol> và <use>
- Multiple sizes và colors
- Hover effects
- Animated variants

### Bài 5: Particle System
**Yêu cầu:**
- Canvas particle animation
- Mouse interaction
- Performance optimization
- Configurable parameters
- Multiple particle types

### Bài 6: Photo Filter App
**Yêu cầu:**
- Load image to canvas
- Grayscale, sepia, blur filters
- Brightness/contrast controls
- Real-time preview
- Save edited image

### Bài 7: Simple Game
**Yêu cầu:**
- Snake, Pong, hoặc Breakout
- Canvas-based rendering
- Keyboard controls
- Score tracking
- Game over screen

### Bài 8: SVG Data Visualization
**Yêu cầu:**
- Interactive timeline
- Animated charts
- Hover tooltips
- Click events
- Responsive layout

### Bài 9: Logo Animation
**Yêu cầu:**
- Animated company logo
- SVG morphing effects
- Loop animation
- Multiple animation sequences
- Loading indicator variant

### Bài 10: Collaborative Whiteboard
**Yêu cầu:**
- Real-time drawing
- Multiple users (simulate locally)
- Shapes: line, rect, circle, freehand
- Text tool
- Export as PNG/SVG

### Bài 11: Music Visualizer
**Yêu cầu:**
- Canvas animation
- Audio input (Web Audio API)
- Frequency bars
- Waveform display
- Color themes

### Bài 12: Map Visualization
**Yêu cầu:**
- SVG map of Vietnam or world
- Clickable regions
- Tooltips with data
- Color-coded by data values
- Zoom and pan capabilities

## 10.11. Tổng Kết

Trong chương này chúng ta đã học:
- Canvas API cho raster graphics
- SVG cho vector graphics
- So sánh Canvas vs SVG
- Use cases và best practices cho mỗi công nghệ
- Tips & tricks để optimize performance
- Common mistakes và cách tránh
- Troubleshooting các vấn đề thường gặp
- Advanced topics cho đồ họa phức tạp

**Key takeaways:**
- Canvas tốt cho: Games, pixel manipulation, complex animations, large số objects
- SVG tốt cho: Icons, logos, charts, interactive graphics, scalable designs
- Chọn công nghệ phù hợp với yêu cầu dự án
- Performance luôn là ưu tiên khi làm việc với graphics

---

**Chương tiếp theo:** Chúng ta sẽ tìm hiểu về Storage và Offline capabilities trong HTML5.
