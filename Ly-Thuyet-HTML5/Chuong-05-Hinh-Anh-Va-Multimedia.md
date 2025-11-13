# CHƯƠNG 5: HÌNH ẢNH VÀ MULTIMEDIA

## 5.1. Images (Hình ảnh)

### 5.1.1. Thẻ `<img>`

**Cú pháp cơ bản:**
```html
<img src="image.jpg" alt="Description">
```

**Attributes bắt buộc:**
- `src`: Đường dẫn đến file hình ảnh
- `alt`: Mô tả hình ảnh (cho accessibility và SEO)

### 5.1.2. Image Attributes

#### src - Source
```html
<!-- Relative path -->
<img src="images/logo.png" alt="Logo">
<img src="../images/photo.jpg" alt="Photo">

<!-- Absolute path -->
<img src="/assets/images/banner.jpg" alt="Banner">

<!-- External URL -->
<img src="https://example.com/image.jpg" alt="External image">

<!-- Data URL -->
<img src="data:image/png;base64,iVBORw0KGgo..." alt="Inline image">
```

#### alt - Alternative Text
```html
<!-- Descriptive alt text -->
<img src="cat.jpg" alt="A black cat sleeping on a couch">

<!-- Decorative images -->
<img src="decoration.png" alt="">

<!-- Functional images (logo as link) -->
<a href="/">
    <img src="logo.png" alt="Company Name - Home">
</a>

<!-- Complex images -->
<img src="chart.png"
     alt="Bar chart showing sales increase of 25% in Q4 2023">
```

#### width và height
```html
<!-- Pixels -->
<img src="photo.jpg" alt="Photo" width="300" height="200">

<!-- Giữ tỷ lệ aspect ratio với CSS -->
<img src="photo.jpg" alt="Photo" style="width: 100%; height: auto;">
```

**Lợi ích của việc set width/height:**
- Tránh layout shift khi page load
- Browser dự trữ không gian trước khi image load

#### loading - Lazy Loading
```html
<!-- Lazy load (HTML5.2+) -->
<img src="image.jpg" alt="Description" loading="lazy">

<!-- Eager load (default) -->
<img src="hero.jpg" alt="Hero image" loading="eager">
```

#### decoding
```html
<!-- Async decoding -->
<img src="large-image.jpg" alt="Large image" decoding="async">

<!-- Sync decoding -->
<img src="critical-image.jpg" alt="Critical" decoding="sync">

<!-- Auto (default) -->
<img src="image.jpg" alt="Image" decoding="auto">
```

#### srcset và sizes - Responsive Images
```html
<!-- Srcset với different resolutions -->
<img src="image-400.jpg"
     srcset="image-400.jpg 400w,
             image-800.jpg 800w,
             image-1200.jpg 1200w"
     sizes="(max-width: 600px) 400px,
            (max-width: 900px) 800px,
            1200px"
     alt="Responsive image">

<!-- Srcset với pixel density -->
<img src="image.jpg"
     srcset="image.jpg 1x,
             image-2x.jpg 2x,
             image-3x.jpg 3x"
     alt="High DPI image">
```

### 5.1.3. Picture Element

**Responsive images với `<picture>`:**
```html
<picture>
    <!-- WebP for modern browsers -->
    <source srcset="image.webp" type="image/webp">

    <!-- JPEG fallback -->
    <source srcset="image.jpg" type="image/jpeg">

    <!-- Default -->
    <img src="image.jpg" alt="Description">
</picture>
```

**Art direction:**
```html
<picture>
    <!-- Mobile: portrait -->
    <source media="(max-width: 600px)"
            srcset="image-mobile.jpg">

    <!-- Tablet: square -->
    <source media="(max-width: 1200px)"
            srcset="image-tablet.jpg">

    <!-- Desktop: landscape -->
    <img src="image-desktop.jpg" alt="Responsive image">
</picture>
```

**Multiple formats:**
```html
<picture>
    <source srcset="image.avif" type="image/avif">
    <source srcset="image.webp" type="image/webp">
    <source srcset="image.jpg" type="image/jpeg">
    <img src="image.jpg" alt="Modern image formats">
</picture>
```

### 5.1.4. Figure và Figcaption

```html
<figure>
    <img src="photo.jpg" alt="Beautiful landscape">
    <figcaption>Figure 1: A beautiful landscape in Vietnam</figcaption>
</figure>
```

**Multiple images:**
```html
<figure>
    <img src="img1.jpg" alt="Image 1">
    <img src="img2.jpg" alt="Image 2">
    <img src="img3.jpg" alt="Image 3">
    <figcaption>Gallery: Product photos</figcaption>
</figure>
```

**With code:**
```html
<figure>
    <pre><code>
function hello() {
    console.log("Hello World");
}
    </code></pre>
    <figcaption>Listing 1: Hello World function</figcaption>
</figure>
```

### 5.1.5. Image Maps

```html
<img src="workplace.jpg" alt="Workplace" usemap="#workmap">

<map name="workmap">
    <area shape="rect"
          coords="34,44,270,350"
          alt="Computer"
          href="computer.html">

    <area shape="circle"
          coords="337,300,44"
          alt="Cup"
          href="cup.html">

    <area shape="poly"
          coords="140,121,181,116,204,160,204,222,191,270,140,329,85,355,58,352,37,322,40,259,103,161,128,147"
          alt="Phone"
          href="phone.html">
</map>
```

### 5.1.6. Image Formats

| Format | Use Case | Supports Transparency | Supports Animation |
|--------|----------|----------------------|-------------------|
| JPEG/JPG | Photos, complex images | No | No |
| PNG | Logos, icons, graphics | Yes | No |
| GIF | Simple animations | Yes | Yes |
| WebP | Modern format, smaller size | Yes | Yes |
| SVG | Scalable vector graphics | Yes | Yes (CSS/JS) |
| AVIF | Next-gen format, best compression | Yes | Yes |

## 5.2. Audio

### 5.2.1. Thẻ `<audio>`

**Basic audio:**
```html
<audio src="audio.mp3" controls>
    Your browser does not support the audio element.
</audio>
```

### 5.2.2. Audio Attributes

```html
<audio src="music.mp3"
       controls
       autoplay
       loop
       muted
       preload="auto">
    Fallback text
</audio>
```

**Attributes:**
- `controls`: Hiển thị controls (play, pause, volume)
- `autoplay`: Tự động phát (cần `muted` để hoạt động trong hầu hết browsers)
- `loop`: Lặp lại
- `muted`: Tắt tiếng
- `preload`: "none" | "metadata" | "auto"

### 5.2.3. Multiple Audio Sources

```html
<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    <source src="audio.ogg" type="audio/ogg">
    <source src="audio.wav" type="audio/wav">
    Your browser does not support the audio element.
</audio>
```

### 5.2.4. Audio Formats

| Format | MIME Type | Browser Support |
|--------|-----------|-----------------|
| MP3 | audio/mpeg | Excellent |
| WAV | audio/wav | Good |
| OGG | audio/ogg | Good (Firefox, Chrome) |
| AAC | audio/aac | Good |
| WebM | audio/webm | Good (Chrome, Firefox) |

### 5.2.5. Advanced Audio Features

```html
<audio id="myAudio" controls>
    <source src="music.mp3" type="audio/mpeg">
</audio>

<script>
const audio = document.getElementById('myAudio');

// Play
audio.play();

// Pause
audio.pause();

// Volume (0.0 to 1.0)
audio.volume = 0.5;

// Current time (seconds)
audio.currentTime = 30;

// Events
audio.addEventListener('play', () => {
    console.log('Audio playing');
});

audio.addEventListener('ended', () => {
    console.log('Audio ended');
});
</script>
```

## 5.3. Video

### 5.3.1. Thẻ `<video>`

**Basic video:**
```html
<video src="video.mp4" controls width="640" height="360">
    Your browser does not support the video tag.
</video>
```

### 5.3.2. Video Attributes

```html
<video src="movie.mp4"
       controls
       autoplay
       muted
       loop
       poster="thumbnail.jpg"
       width="800"
       height="450"
       preload="metadata">
    Fallback content
</video>
```

**Attributes:**
- `controls`: Hiển thị player controls
- `autoplay`: Tự động phát (cần `muted`)
- `loop`: Phát lặp lại
- `muted`: Tắt tiếng
- `poster`: Hình thumbnail hiển thị trước khi play
- `width`, `height`: Kích thước video
- `preload`: "none" | "metadata" | "auto"

### 5.3.3. Multiple Video Sources

```html
<video controls width="640" height="360" poster="poster.jpg">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    <source src="video.ogv" type="video/ogg">
    Your browser does not support the video tag.
</video>
```

### 5.3.4. Video with Subtitles/Captions

```html
<video controls>
    <source src="movie.mp4" type="video/mp4">

    <!-- Subtitles -->
    <track kind="subtitles"
           src="subtitles-en.vtt"
           srclang="en"
           label="English">

    <track kind="subtitles"
           src="subtitles-vi.vtt"
           srclang="vi"
           label="Tiếng Việt"
           default>

    <!-- Captions -->
    <track kind="captions"
           src="captions.vtt"
           srclang="en"
           label="English Captions">

    <!-- Descriptions -->
    <track kind="descriptions"
           src="descriptions.vtt"
           srclang="en">
</video>
```

**WebVTT file example (subtitles-vi.vtt):**
```
WEBVTT

00:00:00.000 --> 00:00:05.000
Đây là phụ đề đầu tiên

00:00:05.000 --> 00:00:10.000
Đây là phụ đề thứ hai
```

### 5.3.5. Video Formats

| Format | MIME Type | Browser Support |
|--------|-----------|-----------------|
| MP4 | video/mp4 | Excellent |
| WebM | video/webm | Good (Chrome, Firefox) |
| OGG | video/ogg | Good (Firefox, Chrome) |

**Recommended codec:**
- **MP4**: H.264 video + AAC audio
- **WebM**: VP8/VP9 video + Vorbis/Opus audio

### 5.3.6. Responsive Video

**CSS approach:**
```html
<div class="video-container">
    <video controls>
        <source src="video.mp4" type="video/mp4">
    </video>
</div>

<style>
.video-container {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    height: 0;
    overflow: hidden;
}

.video-container video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
```

### 5.3.7. Advanced Video Features

```html
<video id="myVideo" controls>
    <source src="movie.mp4" type="video/mp4">
</video>

<script>
const video = document.getElementById('myVideo');

// Play
video.play();

// Pause
video.pause();

// Fullscreen
video.requestFullscreen();

// Picture-in-Picture
video.requestPictureInPicture();

// Playback speed
video.playbackRate = 1.5; // 1.5x speed

// Volume
video.volume = 0.8;

// Events
video.addEventListener('play', () => {
    console.log('Video playing');
});

video.addEventListener('timeupdate', () => {
    console.log('Current time:', video.currentTime);
});

video.addEventListener('ended', () => {
    console.log('Video ended');
});
</script>
```

## 5.4. Embedding External Media

### 5.4.1. YouTube Videos

**Iframe embed:**
```html
<iframe width="560"
        height="315"
        src="https://www.youtube.com/embed/VIDEO_ID"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>
```

**Responsive YouTube embed:**
```html
<div class="youtube-container">
    <iframe src="https://www.youtube.com/embed/VIDEO_ID"
            title="YouTube video"
            frameborder="0"
            allowfullscreen>
    </iframe>
</div>

<style>
.youtube-container {
    position: relative;
    padding-bottom: 56.25%;
    height: 0;
    overflow: hidden;
}

.youtube-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
```

### 5.4.2. Vimeo Videos

```html
<iframe src="https://player.vimeo.com/video/VIDEO_ID"
        width="640"
        height="360"
        frameborder="0"
        allow="autoplay; fullscreen; picture-in-picture"
        allowfullscreen>
</iframe>
```

### 5.4.3. Google Maps

```html
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12..."
        width="600"
        height="450"
        style="border:0;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade">
</iframe>
```

## 5.5. SVG - Scalable Vector Graphics

### 5.5.1. Inline SVG

```html
<svg width="100" height="100">
    <circle cx="50" cy="50" r="40"
            stroke="black"
            stroke-width="3"
            fill="red" />
</svg>
```

### 5.5.2. SVG Shapes

**Rectangle:**
```html
<svg width="200" height="100">
    <rect width="200" height="100"
          fill="blue"
          stroke="black"
          stroke-width="2" />
</svg>
```

**Circle:**
```html
<svg width="100" height="100">
    <circle cx="50" cy="50" r="40" fill="green" />
</svg>
```

**Line:**
```html
<svg width="200" height="100">
    <line x1="0" y1="0" x2="200" y2="100"
          stroke="red"
          stroke-width="2" />
</svg>
```

**Polygon:**
```html
<svg width="200" height="200">
    <polygon points="100,10 40,180 190,60 10,60 160,180"
             fill="yellow"
             stroke="black"
             stroke-width="2" />
</svg>
```

**Path:**
```html
<svg width="200" height="200">
    <path d="M 10 10 L 90 90 L 10 90 Z"
          fill="purple"
          stroke="black"
          stroke-width="2" />
</svg>
```

### 5.5.3. SVG Text

```html
<svg width="200" height="100">
    <text x="10" y="50"
          font-family="Arial"
          font-size="24"
          fill="blue">
        Hello SVG
    </text>
</svg>
```

### 5.5.4. SVG as Image

```html
<img src="image.svg" alt="SVG image">
```

### 5.5.5. SVG as Background

```css
.element {
    background-image: url('pattern.svg');
}
```

## 5.6. Canvas

### 5.6.1. Canvas Element

```html
<canvas id="myCanvas" width="400" height="200">
    Your browser does not support the canvas element.
</canvas>
```

### 5.6.2. Drawing on Canvas

**Rectangle:**
```html
<canvas id="canvas1" width="200" height="100"></canvas>

<script>
const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');

// Fill rectangle
ctx.fillStyle = 'blue';
ctx.fillRect(10, 10, 150, 80);

// Stroke rectangle
ctx.strokeStyle = 'red';
ctx.lineWidth = 3;
ctx.strokeRect(30, 30, 100, 40);
</script>
```

**Circle:**
```javascript
ctx.beginPath();
ctx.arc(100, 75, 50, 0, 2 * Math.PI);
ctx.fillStyle = 'green';
ctx.fill();
ctx.strokeStyle = 'black';
ctx.lineWidth = 2;
ctx.stroke();
```

**Line:**
```javascript
ctx.beginPath();
ctx.moveTo(0, 0);
ctx.lineTo(200, 100);
ctx.strokeStyle = 'red';
ctx.lineWidth = 2;
ctx.stroke();
```

**Text:**
```javascript
ctx.font = '30px Arial';
ctx.fillStyle = 'blue';
ctx.fillText('Hello Canvas', 10, 50);

// Stroke text
ctx.strokeStyle = 'red';
ctx.strokeText('Outline Text', 10, 100);
```

## 5.7. Optimization Best Practices

### 5.7.1. Image Optimization

1. **Compress images:**
   - Use tools: TinyPNG, ImageOptim, Squoosh
   - Target: < 200KB for most images

2. **Choose right format:**
   - Photos: JPEG, WebP
   - Graphics/Logos: PNG, SVG, WebP
   - Animations: GIF, WebP, video

3. **Responsive images:**
```html
<picture>
    <source srcset="image-large.webp" media="(min-width: 1200px)">
    <source srcset="image-medium.webp" media="(min-width: 768px)">
    <source srcset="image-small.webp">
    <img src="image.jpg" alt="Optimized image">
</picture>
```

4. **Lazy loading:**
```html
<img src="image.jpg" alt="Description" loading="lazy">
```

### 5.7.2. Video Optimization

1. **Compress videos**
2. **Use appropriate format**
3. **Preload metadata only:**
```html
<video preload="metadata" poster="poster.jpg">
```

4. **Lazy load videos:**
```html
<video loading="lazy">
```

## 5.8. Accessibility

### 5.8.1. Images

```html
<!-- Meaningful images -->
<img src="cat.jpg" alt="Orange tabby cat sleeping">

<!-- Decorative images -->
<img src="border.png" alt="" role="presentation">

<!-- Complex images -->
<img src="chart.jpg"
     alt="Sales chart"
     aria-describedby="chart-description">
<div id="chart-description">
    Detailed description of the sales chart...
</div>
```

### 5.8.2. Audio/Video

```html
<video controls>
    <source src="video.mp4" type="video/mp4">
    <track kind="captions" src="captions.vtt" srclang="en" default>
    <track kind="subtitles" src="subtitles.vtt" srclang="vi">
</video>
```

## 5.9. Use Cases Thực Tế

### Use Case 1: Photo Gallery cho E-commerce
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Product Gallery</title>
    <style>
        .product-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .product-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        .product-image {
            width: 100%;
            aspect-ratio: 1/1;
            object-fit: cover;
        }
        .product-info {
            padding: 15px;
        }
    </style>
</head>
<body>
    <div class="product-gallery">
        <article class="product-card">
            <picture>
                <source srcset="product1.webp" type="image/webp">
                <source srcset="product1.jpg" type="image/jpeg">
                <img src="product1.jpg"
                     alt="Laptop Dell XPS 13"
                     class="product-image"
                     loading="lazy">
            </picture>
            <div class="product-info">
                <h3>Laptop Dell XPS 13</h3>
                <p class="price">25,990,000đ</p>
            </div>
        </article>

        <article class="product-card">
            <picture>
                <source srcset="product2.webp" type="image/webp">
                <img src="product2.jpg"
                     alt="iPhone 15 Pro"
                     class="product-image"
                     loading="lazy">
            </picture>
            <div class="product-info">
                <h3>iPhone 15 Pro</h3>
                <p class="price">29,990,000đ</p>
            </div>
        </article>
    </div>
</body>
</html>
```

### Use Case 2: Video Course Platform
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Online Course Player</title>
    <style>
        .course-player {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .video-wrapper {
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            background: #000;
            border-radius: 8px;
            overflow: hidden;
        }
        .video-wrapper video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        .video-controls {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
        .lesson-list {
            margin-top: 30px;
        }
        .lesson-item {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-bottom: 10px;
            cursor: pointer;
        }
        .lesson-item:hover {
            background: #f5f5f5;
        }
        .lesson-thumbnail {
            width: 120px;
            height: 67px;
            object-fit: cover;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="course-player">
        <div class="video-wrapper">
            <video id="courseVideo" controls poster="lesson1-poster.jpg">
                <source src="lesson1.mp4" type="video/mp4">
                <source src="lesson1.webm" type="video/webm">
                <track kind="subtitles"
                       src="lesson1-vi.vtt"
                       srclang="vi"
                       label="Tiếng Việt"
                       default>
                <track kind="subtitles"
                       src="lesson1-en.vtt"
                       srclang="en"
                       label="English">
            </video>
        </div>

        <div class="video-controls">
            <button onclick="changeSpeed(0.5)">0.5x</button>
            <button onclick="changeSpeed(1.0)">1x</button>
            <button onclick="changeSpeed(1.5)">1.5x</button>
            <button onclick="changeSpeed(2.0)">2x</button>
            <button onclick="togglePIP()">Picture-in-Picture</button>
        </div>

        <div class="lesson-list">
            <h2>Danh sách bài học</h2>
            <div class="lesson-item" onclick="loadLesson('lesson1.mp4', 'lesson1-poster.jpg')">
                <img src="lesson1-thumb.jpg" alt="Lesson 1" class="lesson-thumbnail">
                <div>
                    <h3>Bài 1: Giới thiệu HTML5</h3>
                    <p>Thời lượng: 15:30</p>
                </div>
            </div>
            <div class="lesson-item" onclick="loadLesson('lesson2.mp4', 'lesson2-poster.jpg')">
                <img src="lesson2-thumb.jpg" alt="Lesson 2" class="lesson-thumbnail">
                <div>
                    <h3>Bài 2: Cấu trúc HTML cơ bản</h3>
                    <p>Thời lượng: 20:15</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        const video = document.getElementById('courseVideo');

        function changeSpeed(rate) {
            video.playbackRate = rate;
        }

        function togglePIP() {
            if (document.pictureInPictureElement) {
                document.exitPictureInPicture();
            } else {
                video.requestPictureInPicture();
            }
        }

        function loadLesson(videoSrc, posterSrc) {
            video.src = videoSrc;
            video.poster = posterSrc;
            video.load();
            video.play();
        }

        // Save progress
        video.addEventListener('timeupdate', () => {
            localStorage.setItem('videoProgress', video.currentTime);
        });

        // Resume from saved progress
        window.addEventListener('load', () => {
            const savedTime = localStorage.getItem('videoProgress');
            if (savedTime) {
                video.currentTime = parseFloat(savedTime);
            }
        });
    </script>
</body>
</html>
```

### Use Case 3: Interactive Image Map cho Building Directory
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Building Directory</title>
    <style>
        .directory-container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        .floor-map {
            position: relative;
            display: inline-block;
        }
        area {
            cursor: pointer;
        }
        .room-info {
            margin-top: 20px;
            padding: 20px;
            background: #f5f5f5;
            border-radius: 8px;
            display: none;
        }
        .room-info.active {
            display: block;
        }
    </style>
</head>
<body>
    <div class="directory-container">
        <h1>Sơ đồ tầng 2 - Văn phòng</h1>

        <div class="floor-map">
            <img src="floor2-plan.jpg"
                 alt="Sơ đồ tầng 2"
                 usemap="#floormap"
                 width="800">

            <map name="floormap">
                <area shape="rect"
                      coords="50,50,250,150"
                      alt="Phòng họp A"
                      href="#"
                      onclick="showRoom('meetingA'); return false;">

                <area shape="rect"
                      coords="270,50,470,150"
                      alt="Phòng họp B"
                      href="#"
                      onclick="showRoom('meetingB'); return false;">

                <area shape="poly"
                      coords="50,170,150,170,150,270,50,270"
                      alt="Văn phòng IT"
                      href="#"
                      onclick="showRoom('itOffice'); return false;">
            </map>
        </div>

        <div id="meetingA" class="room-info">
            <h2>Phòng họp A</h2>
            <p>Sức chứa: 20 người</p>
            <p>Thiết bị: Projector, TV 65", Whiteboard</p>
            <button>Đặt phòng</button>
        </div>

        <div id="meetingB" class="room-info">
            <h2>Phòng họp B</h2>
            <p>Sức chứa: 10 người</p>
            <p>Thiết bị: TV 55", Video conference</p>
            <button>Đặt phòng</button>
        </div>

        <div id="itOffice" class="room-info">
            <h2>Văn phòng IT</h2>
            <p>Số nhân viên: 15</p>
            <p>Liên hệ: ext 123</p>
        </div>
    </div>

    <script>
        function showRoom(roomId) {
            // Hide all rooms
            document.querySelectorAll('.room-info').forEach(room => {
                room.classList.remove('active');
            });

            // Show selected room
            document.getElementById(roomId).classList.add('active');
        }
    </script>
</body>
</html>
```

### Use Case 4: Audio Podcast Player
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Podcast Player</title>
    <style>
        .podcast-player {
            max-width: 600px;
            margin: 50px auto;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px;
            border-radius: 15px;
            color: white;
        }
        .album-art {
            width: 100%;
            aspect-ratio: 1/1;
            object-fit: cover;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .episode-info {
            text-align: center;
            margin: 20px 0;
        }
        audio {
            width: 100%;
            margin: 20px 0;
        }
        .playlist {
            margin-top: 30px;
        }
        .playlist-item {
            background: rgba(255,255,255,0.1);
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .playlist-item:hover {
            background: rgba(255,255,255,0.2);
        }
        .playlist-item.playing {
            background: rgba(255,255,255,0.3);
        }
    </style>
</head>
<body>
    <div class="podcast-player">
        <img id="albumArt"
             src="podcast-cover.jpg"
             alt="Podcast Cover"
             class="album-art">

        <div class="episode-info">
            <h2 id="episodeTitle">Episode 1: Getting Started</h2>
            <p id="episodeDescription">Introduction to web development</p>
        </div>

        <audio id="audioPlayer" controls>
            <source src="episode1.mp3" type="audio/mpeg">
            <source src="episode1.ogg" type="audio/ogg">
            Your browser does not support the audio element.
        </audio>

        <div class="playlist">
            <h3>Playlist</h3>
            <div class="playlist-item playing"
                 onclick="playEpisode('episode1.mp3', 'Episode 1', 'Introduction to web development', 'podcast-cover.jpg')">
                <strong>Episode 1:</strong> Getting Started (15:30)
            </div>
            <div class="playlist-item"
                 onclick="playEpisode('episode2.mp3', 'Episode 2', 'HTML Fundamentals', 'podcast-cover.jpg')">
                <strong>Episode 2:</strong> HTML Fundamentals (20:15)
            </div>
            <div class="playlist-item"
                 onclick="playEpisode('episode3.mp3', 'Episode 3', 'CSS Styling', 'podcast-cover.jpg')">
                <strong>Episode 3:</strong> CSS Styling (18:45)
            </div>
        </div>
    </div>

    <script>
        const audio = document.getElementById('audioPlayer');
        const albumArt = document.getElementById('albumArt');
        const episodeTitle = document.getElementById('episodeTitle');
        const episodeDescription = document.getElementById('episodeDescription');

        function playEpisode(src, title, description, cover) {
            audio.src = src;
            episodeTitle.textContent = title;
            episodeDescription.textContent = description;
            albumArt.src = cover;
            audio.play();

            // Update playlist UI
            document.querySelectorAll('.playlist-item').forEach(item => {
                item.classList.remove('playing');
            });
            event.currentTarget.classList.add('playing');
        }

        // Auto-play next episode
        audio.addEventListener('ended', () => {
            const currentItem = document.querySelector('.playlist-item.playing');
            const nextItem = currentItem.nextElementSibling;
            if (nextItem) {
                nextItem.click();
            }
        });
    </script>
</body>
</html>
```

### Use Case 5: Canvas-based Image Editor
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Simple Image Editor</title>
    <style>
        .editor-container {
            max-width: 900px;
            margin: 20px auto;
            padding: 20px;
        }
        canvas {
            border: 2px solid #333;
            max-width: 100%;
            cursor: crosshair;
        }
        .tools {
            display: flex;
            gap: 10px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        .tool-btn {
            padding: 10px 20px;
            border: none;
            background: #667eea;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }
        .tool-btn:hover {
            background: #5568d3;
        }
        input[type="color"] {
            width: 50px;
            height: 40px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="editor-container">
        <h1>Simple Image Editor</h1>

        <div class="tools">
            <input type="file" id="imageUpload" accept="image/*">
            <button class="tool-btn" onclick="applyFilter('grayscale')">Grayscale</button>
            <button class="tool-btn" onclick="applyFilter('sepia')">Sepia</button>
            <button class="tool-btn" onclick="applyFilter('invert')">Invert</button>
            <button class="tool-btn" onclick="applyFilter('blur')">Blur</button>
            <button class="tool-btn" onclick="resetImage()">Reset</button>
            <input type="color" id="colorPicker" value="#ff0000">
            <button class="tool-btn" onclick="enableDrawing()">Draw</button>
            <button class="tool-btn" onclick="addText()">Add Text</button>
            <button class="tool-btn" onclick="downloadImage()">Download</button>
        </div>

        <canvas id="canvas" width="800" height="600"></canvas>
    </div>

    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        let originalImage = null;
        let isDrawing = false;

        // Upload image
        document.getElementById('imageUpload').addEventListener('change', (e) => {
            const file = e.target.files[0];
            const reader = new FileReader();

            reader.onload = (event) => {
                const img = new Image();
                img.onload = () => {
                    canvas.width = img.width;
                    canvas.height = img.height;
                    ctx.drawImage(img, 0, 0);
                    originalImage = ctx.getImageData(0, 0, canvas.width, canvas.height);
                };
                img.src = event.target.result;
            };

            reader.readAsDataURL(file);
        });

        // Apply filters
        function applyFilter(filterType) {
            if (!originalImage) return;

            ctx.putImageData(originalImage, 0, 0);
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const data = imageData.data;

            for (let i = 0; i < data.length; i += 4) {
                const r = data[i];
                const g = data[i + 1];
                const b = data[i + 2];

                switch(filterType) {
                    case 'grayscale':
                        const gray = 0.299 * r + 0.587 * g + 0.114 * b;
                        data[i] = data[i + 1] = data[i + 2] = gray;
                        break;
                    case 'sepia':
                        data[i] = Math.min(255, r * 0.393 + g * 0.769 + b * 0.189);
                        data[i + 1] = Math.min(255, r * 0.349 + g * 0.686 + b * 0.168);
                        data[i + 2] = Math.min(255, r * 0.272 + g * 0.534 + b * 0.131);
                        break;
                    case 'invert':
                        data[i] = 255 - r;
                        data[i + 1] = 255 - g;
                        data[i + 2] = 255 - b;
                        break;
                    case 'blur':
                        // Simple blur effect
                        if (i % 8 === 0) {
                            data[i] = (data[i] + data[i + 4]) / 2;
                            data[i + 1] = (data[i + 1] + data[i + 5]) / 2;
                            data[i + 2] = (data[i + 2] + data[i + 6]) / 2;
                        }
                        break;
                }
            }

            ctx.putImageData(imageData, 0, 0);
        }

        // Reset image
        function resetImage() {
            if (originalImage) {
                ctx.putImageData(originalImage, 0, 0);
            }
        }

        // Drawing functionality
        function enableDrawing() {
            canvas.addEventListener('mousedown', startDrawing);
            canvas.addEventListener('mousemove', draw);
            canvas.addEventListener('mouseup', stopDrawing);
        }

        function startDrawing(e) {
            isDrawing = true;
            const rect = canvas.getBoundingClientRect();
            ctx.beginPath();
            ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
        }

        function draw(e) {
            if (!isDrawing) return;
            const rect = canvas.getBoundingClientRect();
            ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
            ctx.strokeStyle = document.getElementById('colorPicker').value;
            ctx.lineWidth = 3;
            ctx.stroke();
        }

        function stopDrawing() {
            isDrawing = false;
        }

        // Add text
        function addText() {
            const text = prompt('Enter text:');
            if (text) {
                ctx.font = '30px Arial';
                ctx.fillStyle = document.getElementById('colorPicker').value;
                ctx.fillText(text, 50, 50);
            }
        }

        // Download image
        function downloadImage() {
            const link = document.createElement('a');
            link.download = 'edited-image.png';
            link.href = canvas.toDataURL();
            link.click();
        }
    </script>
</body>
</html>
```

## 5.10. Tips & Tricks

### Tip 1: Image Loading Strategy
```html
<!-- Critical images: eager load -->
<img src="hero.jpg" alt="Hero" loading="eager" fetchpriority="high">

<!-- Below fold images: lazy load -->
<img src="gallery1.jpg" alt="Gallery" loading="lazy">

<!-- Use sizes for better performance -->
<img src="responsive.jpg"
     srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
     sizes="(max-width: 600px) 400px, (max-width: 900px) 800px, 1200px"
     alt="Responsive">
```

### Tip 2: Modern Image Formats với Fallbacks
```html
<picture>
    <!-- Modern browsers: AVIF -->
    <source srcset="image.avif" type="image/avif">

    <!-- Most browsers: WebP -->
    <source srcset="image.webp" type="image/webp">

    <!-- Fallback: JPEG -->
    <img src="image.jpg" alt="Image with modern formats">
</picture>
```

### Tip 3: Preload Important Media
```html
<head>
    <!-- Preload hero image -->
    <link rel="preload" as="image" href="hero.jpg">

    <!-- Preload video poster -->
    <link rel="preload" as="image" href="video-poster.jpg">
</head>
```

### Tip 4: Video Optimization
```html
<!-- Optimize for web viewing -->
<video controls preload="metadata" poster="poster.jpg">
    <source src="video.mp4" type="video/mp4">
</video>

<!-- Add playsinline for iOS -->
<video controls playsinline>
    <source src="mobile-video.mp4" type="video/mp4">
</video>
```

### Tip 5: Audio Sprite Technique
```javascript
// Load one audio file with multiple sounds
const audioSprite = new Audio('sounds-sprite.mp3');

function playSound(start, duration) {
    audioSprite.currentTime = start;
    audioSprite.play();

    setTimeout(() => {
        audioSprite.pause();
    }, duration * 1000);
}

// Play different sounds from same file
playSound(0, 2);    // Sound 1: 0-2s
playSound(2, 1.5);  // Sound 2: 2-3.5s
```

### Tip 6: Responsive SVG Icons
```html
<svg viewBox="0 0 24 24" class="icon">
    <path d="M12 2L2 7l10 5 10-5-10-5z"/>
</svg>

<style>
.icon {
    width: 24px;  /* SVG scales perfectly */
    height: 24px;
    fill: currentColor;  /* Inherits text color */
}
</style>
```

### Tip 7: Canvas High DPI Support
```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const dpr = window.devicePixelRatio || 1;

// Set actual size for high DPI displays
canvas.width = 800 * dpr;
canvas.height = 600 * dpr;

// Scale back down with CSS
canvas.style.width = '800px';
canvas.style.height = '600px';

// Scale context to match
ctx.scale(dpr, dpr);
```

### Tip 8: Video Thumbnail Generation
```javascript
const video = document.getElementById('myVideo');
const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');

video.addEventListener('loadeddata', () => {
    // Seek to 5 seconds
    video.currentTime = 5;
});

video.addEventListener('seeked', () => {
    // Capture frame
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);

    // Get thumbnail as data URL
    const thumbnail = canvas.toDataURL('image/jpeg');
    console.log(thumbnail);
});
```

### Tip 9: Lazy Load Videos
```html
<!-- Lazy load video -->
<video controls preload="none" poster="poster.jpg">
    <source data-src="video.mp4" type="video/mp4">
</video>

<script>
// Load video when in viewport
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const video = entry.target;
            const source = video.querySelector('source');
            source.src = source.dataset.src;
            video.load();
            observer.unobserve(video);
        }
    });
});

document.querySelectorAll('video').forEach(video => {
    observer.observe(video);
});
</script>
```

### Tip 10: Image Placeholder Strategy
```html
<!-- LQIP: Low Quality Image Placeholder -->
<img src="tiny-blurred.jpg"
     data-src="full-quality.jpg"
     alt="Image"
     class="lqip">

<style>
.lqip {
    filter: blur(20px);
    transition: filter 0.3s;
}
.lqip.loaded {
    filter: blur(0);
}
</style>

<script>
document.querySelectorAll('.lqip').forEach(img => {
    const fullImg = new Image();
    fullImg.src = img.dataset.src;
    fullImg.onload = () => {
        img.src = fullImg.src;
        img.classList.add('loaded');
    };
});
</script>
```

## 5.11. Common Mistakes (Lỗi Thường Gặp)

### Lỗi 1: Không set width và height cho images
```html
<!-- ❌ Sai: Gây layout shift -->
<img src="large-image.jpg" alt="Image">

<!-- ✅ Đúng: Set dimensions -->
<img src="large-image.jpg" alt="Image" width="800" height="600">

<!-- ✅ Hoặc dùng aspect-ratio -->
<img src="large-image.jpg" alt="Image" style="aspect-ratio: 16/9; width: 100%;">
```

### Lỗi 2: Alt text kém chất lượng
```html
<!-- ❌ Sai -->
<img src="img1.jpg" alt="image">
<img src="product.jpg" alt="click here">

<!-- ✅ Đúng -->
<img src="laptop.jpg" alt="Dell XPS 13 laptop with 13-inch screen">
<img src="product.jpg" alt="Wireless Bluetooth headphones in black">
```

### Lỗi 3: Không optimize images
```html
<!-- ❌ Sai: 5MB image -->
<img src="huge-photo.jpg" alt="Photo">

<!-- ✅ Đúng: Compressed và responsive -->
<picture>
    <source srcset="photo-small.webp" media="(max-width: 600px)">
    <source srcset="photo-medium.webp" media="(max-width: 1200px)">
    <img src="photo-large.webp" alt="Photo">
</picture>
```

### Lỗi 4: Autoplay video với sound
```html
<!-- ❌ Sai: Browsers block this -->
<video autoplay>
    <source src="video.mp4">
</video>

<!-- ✅ Đúng: Muted autoplay -->
<video autoplay muted playsinline>
    <source src="video.mp4">
</video>
```

### Lỗi 5: Không có fallback cho media
```html
<!-- ❌ Sai -->
<video>
    <source src="video.mp4">
</video>

<!-- ✅ Đúng -->
<video controls>
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    <p>Your browser doesn't support video.
       <a href="video.mp4">Download the video</a>
    </p>
</video>
```

### Lỗi 6: Canvas không clear trước draw
```javascript
// ❌ Sai: Images stack up
function draw() {
    ctx.drawImage(img, x, y);
}

// ✅ Đúng: Clear before drawing
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, x, y);
}
```

### Lỗi 7: Không handle media errors
```html
<video id="myVideo" controls>
    <source src="video.mp4">
</video>

<script>
// ❌ Sai: No error handling

// ✅ Đúng: Handle errors
const video = document.getElementById('myVideo');
video.addEventListener('error', (e) => {
    console.error('Video error:', e);
    alert('Unable to load video. Please try again.');
});
</script>
```

### Lỗi 8: SVG không có viewBox
```html
<!-- ❌ Sai: Won't scale properly -->
<svg width="100" height="100">
    <circle cx="50" cy="50" r="40"/>
</svg>

<!-- ✅ Đúng: Use viewBox -->
<svg viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="40"/>
</svg>
```

### Lỗi 9: Memory leak với Canvas
```javascript
// ❌ Sai: Creates new canvas every frame
function animate() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    // ... draw
    requestAnimationFrame(animate);
}

// ✅ Đúng: Reuse canvas
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    // ... draw
    requestAnimationFrame(animate);
}
animate();
```

### Lỗi 10: Không preload poster image cho video
```html
<!-- ❌ Sai: Poster loads after video -->
<video controls poster="poster.jpg">
    <source src="video.mp4">
</video>

<!-- ✅ Đúng: Preload poster -->
<head>
    <link rel="preload" as="image" href="poster.jpg">
</head>
<video controls poster="poster.jpg">
    <source src="video.mp4">
</video>
```

## 5.12. Troubleshooting

### Issue 1: Images không hiển thị
**Triệu chứng:** Broken image icon

**Nguyên nhân:**
- Path sai
- CORS issues
- File không tồn tại

**Giải pháp:**
```javascript
// Check if image loads
const img = new Image();
img.onerror = () => {
    console.error('Image failed to load');
    // Show fallback
    img.src = 'fallback.jpg';
};
img.src = 'main-image.jpg';
```

### Issue 2: Video không autoplay
**Triệu chứng:** Video không tự động play

**Nguyên nhân:**
- Browser autoplay policy
- Không muted
- Không có user interaction

**Giải pháp:**
```html
<!-- Must be muted for autoplay -->
<video autoplay muted playsinline>
    <source src="video.mp4">
</video>

<script>
// Or request play after user interaction
button.addEventListener('click', () => {
    video.play().catch(e => {
        console.error('Autoplay prevented:', e);
    });
});
</script>
```

### Issue 3: Canvas blurry on high DPI displays
**Triệu chứng:** Canvas content looks blurry

**Nguyên nhân:**
- Không scale cho device pixel ratio

**Giải pháp:**
```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const dpr = window.devicePixelRatio || 1;

// Set actual size
canvas.width = 800 * dpr;
canvas.height = 600 * dpr;

// Scale CSS size
canvas.style.width = '800px';
canvas.style.height = '600px';

// Scale drawing operations
ctx.scale(dpr, dpr);
```

### Issue 4: Audio không play trên mobile
**Triệu chứng:** Audio silent on iOS/Android

**Nguyên nhân:**
- Mobile browsers require user gesture

**Giải pháp:**
```javascript
// Unlock audio on first touch
document.addEventListener('touchstart', function unlockAudio() {
    const audio = document.getElementById('myAudio');
    audio.play();
    audio.pause();
    audio.currentTime = 0;
    document.removeEventListener('touchstart', unlockAudio);
}, false);
```

### Issue 5: Video không fullscreen trên iOS
**Triệu chứng:** Video plays in fullscreen by default

**Nguyên nhân:**
- iOS default behavior

**Giải pháp:**
```html
<!-- Use playsinline attribute -->
<video controls playsinline webkit-playsinline>
    <source src="video.mp4">
</video>
```

### Issue 6: SVG không scale trong IE
**Triệu chứng:** SVG có fixed size

**Giải pháp:**
```html
<svg viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet">
    <!-- content -->
</svg>

<style>
svg {
    width: 100%;
    height: auto;
}
</style>
```

### Issue 7: Large images block page load
**Triệu chứng:** Page loads slowly

**Giải pháp:**
```html
<!-- Lazy load images -->
<img src="placeholder.jpg"
     data-src="large-image.jpg"
     loading="lazy"
     alt="Image">

<!-- Decode async -->
<img src="large.jpg" decoding="async" alt="Large image">
```

### Issue 8: Canvas export quality poor
**Triệu chứng:** Downloaded image looks pixelated

**Giải pháp:**
```javascript
// Export at high quality
const dataURL = canvas.toDataURL('image/jpeg', 1.0);

// Or export as PNG
const pngURL = canvas.toDataURL('image/png');

// Download with proper filename
const link = document.createElement('a');
link.download = 'canvas-export.png';
link.href = pngURL;
link.click();
```

### Issue 9: Video subtitles không hiển thị
**Triệu chứng:** Captions not showing

**Nguyên nhân:**
- VTT file format sai
- CORS issues

**Giải pháp:**
```html
<!-- Ensure correct VTT format -->
<video controls>
    <source src="video.mp4">
    <track kind="subtitles"
           src="subtitles.vtt"
           srclang="vi"
           label="Tiếng Việt"
           default>
</video>

<!-- VTT file must start with: -->
<!-- WEBVTT

00:00:00.000 --> 00:00:05.000
Subtitle text
-->
```

### Issue 10: Memory leak with large media files
**Triệu chứng:** Browser becomes slow/crashes

**Giải pháp:**
```javascript
// Clean up media resources
function cleanupMedia() {
    const video = document.getElementById('myVideo');

    // Pause and reset
    video.pause();
    video.src = '';
    video.load();

    // Remove event listeners
    video.removeEventListener('timeupdate', handler);
}

// Call when done
window.addEventListener('beforeunload', cleanupMedia);
```

## 5.13. Advanced Topics

### Topic 1: Progressive Image Loading (Blur-up)
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .progressive {
            position: relative;
            overflow: hidden;
        }
        .progressive img {
            width: 100%;
            display: block;
        }
        .progressive .placeholder {
            filter: blur(20px);
            transform: scale(1.1);
        }
        .progressive .full-img {
            position: absolute;
            top: 0;
            left: 0;
            opacity: 0;
            transition: opacity 0.5s;
        }
        .progressive .full-img.loaded {
            opacity: 1;
        }
    </style>
</head>
<body>
    <div class="progressive" data-fullsrc="full-image.jpg">
        <img src="tiny-placeholder.jpg" class="placeholder" alt="Image">
        <img class="full-img" alt="Image">
    </div>

    <script>
        document.querySelectorAll('.progressive').forEach(container => {
            const placeholder = container.querySelector('.placeholder');
            const fullImg = container.querySelector('.full-img');
            const fullSrc = container.dataset.fullsrc;

            const img = new Image();
            img.onload = () => {
                fullImg.src = fullSrc;
                fullImg.classList.add('loaded');
            };
            img.src = fullSrc;
        });
    </script>
</body>
</html>
```

### Topic 2: WebRTC Video Streaming
```html
<!DOCTYPE html>
<html>
<head>
    <title>WebRTC Camera</title>
</head>
<body>
    <video id="webcam" autoplay playsinline></video>
    <button onclick="startCamera()">Start Camera</button>
    <button onclick="stopCamera()">Stop Camera</button>
    <button onclick="takeSnapshot()">Take Photo</button>
    <canvas id="snapshot"></canvas>

    <script>
        let stream = null;
        const video = document.getElementById('webcam');
        const canvas = document.getElementById('snapshot');

        async function startCamera() {
            try {
                stream = await navigator.mediaDevices.getUserMedia({
                    video: { width: 1280, height: 720 },
                    audio: false
                });
                video.srcObject = stream;
            } catch (err) {
                console.error('Error accessing camera:', err);
            }
        }

        function stopCamera() {
            if (stream) {
                stream.getTracks().forEach(track => track.stop());
                video.srcObject = null;
            }
        }

        function takeSnapshot() {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0);

            // Download snapshot
            const dataURL = canvas.toDataURL('image/jpeg');
            const link = document.createElement('a');
            link.download = 'snapshot.jpg';
            link.href = dataURL;
            link.click();
        }
    </script>
</body>
</html>
```

### Topic 3: Canvas Animation với requestAnimationFrame
```html
<!DOCTYPE html>
<html>
<body>
    <canvas id="animCanvas" width="800" height="600"></canvas>

    <script>
        const canvas = document.getElementById('animCanvas');
        const ctx = canvas.getContext('2d');

        class Particle {
            constructor(x, y) {
                this.x = x;
                this.y = y;
                this.vx = (Math.random() - 0.5) * 5;
                this.vy = (Math.random() - 0.5) * 5;
                this.radius = Math.random() * 3 + 2;
                this.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                // Bounce off edges
                if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.fill();
            }
        }

        const particles = [];
        for (let i = 0; i < 100; i++) {
            particles.push(new Particle(
                Math.random() * canvas.width,
                Math.random() * canvas.height
            ));
        }

        function animate() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            particles.forEach(particle => {
                particle.update();
                particle.draw();
            });

            requestAnimationFrame(animate);
        }

        animate();
    </script>
</body>
</html>
```

### Topic 4: Web Audio API Integration
```html
<!DOCTYPE html>
<html>
<body>
    <button onclick="createOscillator()">Play Tone</button>
    <button onclick="playWithEffects()">Play with Effects</button>

    <audio id="audioElement" controls>
        <source src="music.mp3" type="audio/mpeg">
    </audio>

    <div>
        <label>Volume: <input type="range" id="volume" min="0" max="100" value="50"></label>
        <label>Bass: <input type="range" id="bass" min="-40" max="40" value="0"></label>
        <label>Treble: <input type="range" id="treble" min="-40" max="40" value="0"></label>
    </div>

    <canvas id="visualizer" width="800" height="200"></canvas>

    <script>
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const audioElement = document.getElementById('audioElement');
        const canvas = document.getElementById('visualizer');
        const canvasCtx = canvas.getContext('2d');

        // Create audio source and filters
        const source = audioContext.createMediaElementSource(audioElement);
        const analyser = audioContext.createAnalyser();
        const bassFilter = audioContext.createBiquadFilter();
        const trebleFilter = audioContext.createBiquadFilter();
        const gainNode = audioContext.createGain();

        bassFilter.type = 'lowshelf';
        bassFilter.frequency.value = 200;
        trebleFilter.type = 'highshelf';
        trebleFilter.frequency.value = 3000;

        // Connect audio graph
        source.connect(bassFilter);
        bassFilter.connect(trebleFilter);
        trebleFilter.connect(gainNode);
        gainNode.connect(analyser);
        analyser.connect(audioContext.destination);

        // Controls
        document.getElementById('volume').addEventListener('input', (e) => {
            gainNode.gain.value = e.target.value / 50;
        });

        document.getElementById('bass').addEventListener('input', (e) => {
            bassFilter.gain.value = e.target.value;
        });

        document.getElementById('treble').addEventListener('input', (e) => {
            trebleFilter.gain.value = e.target.value;
        });

        // Visualizer
        analyser.fftSize = 256;
        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        function drawVisualizer() {
            requestAnimationFrame(drawVisualizer);

            analyser.getByteFrequencyData(dataArray);

            canvasCtx.fillStyle = 'rgb(0, 0, 0)';
            canvasCtx.fillRect(0, 0, canvas.width, canvas.height);

            const barWidth = (canvas.width / bufferLength) * 2.5;
            let x = 0;

            for (let i = 0; i < bufferLength; i++) {
                const barHeight = dataArray[i] / 2;

                const r = barHeight + 25;
                const g = 250 * (i / bufferLength);
                const b = 50;

                canvasCtx.fillStyle = `rgb(${r},${g},${b})`;
                canvasCtx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);

                x += barWidth + 1;
            }
        }

        drawVisualizer();

        // Generate tone
        function createOscillator() {
            const oscillator = audioContext.createOscillator();
            const gain = audioContext.createGain();

            oscillator.type = 'sine';
            oscillator.frequency.value = 440; // A4 note

            gain.gain.setValueAtTime(0.3, audioContext.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 1);

            oscillator.connect(gain);
            gain.connect(audioContext.destination);

            oscillator.start();
            oscillator.stop(audioContext.currentTime + 1);
        }
    </script>
</body>
</html>
```

### Topic 5: Image Comparison Slider
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .comparison-container {
            position: relative;
            width: 800px;
            height: 600px;
            overflow: hidden;
        }
        .comparison-container img {
            position: absolute;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .img-after {
            clip-path: polygon(0 0, 50% 0, 50% 100%, 0 100%);
        }
        .slider {
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 4px;
            background: white;
            cursor: ew-resize;
            z-index: 10;
        }
        .slider-button {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 40px;
            height: 40px;
            background: white;
            border-radius: 50%;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <div class="comparison-container" id="comparison">
        <img src="before.jpg" alt="Before" class="img-before">
        <img src="after.jpg" alt="After" class="img-after">
        <div class="slider" id="slider">
            <div class="slider-button"></div>
        </div>
    </div>

    <script>
        const container = document.getElementById('comparison');
        const slider = document.getElementById('slider');
        const imgAfter = container.querySelector('.img-after');
        let isActive = false;

        slider.addEventListener('mousedown', () => {
            isActive = true;
        });

        document.addEventListener('mouseup', () => {
            isActive = false;
        });

        document.addEventListener('mousemove', (e) => {
            if (!isActive) return;

            const rect = container.getBoundingClientRect();
            let x = e.clientX - rect.left;

            // Constrain to container
            x = Math.max(0, Math.min(x, rect.width));

            const percent = (x / rect.width) * 100;

            slider.style.left = percent + '%';
            imgAfter.style.clipPath = `polygon(0 0, ${percent}% 0, ${percent}% 100%, 0 100%)`;
        });
    </script>
</body>
</html>
```

## 5.14. Bài tập thực hành

### Bài 1 (Dễ): Responsive Image Gallery
Tạo gallery với:
- 12 images trong grid layout
- Lazy loading
- Lightbox khi click
- Responsive breakpoints

### Bài 2 (Dễ): Simple Audio Player
Tạo player với:
- Play/Pause button
- Progress bar
- Volume control
- Current time display

### Bài 3 (Dễ): Video với Custom Controls
Tạo video player với controls:
- Play/Pause
- Progress bar
- Volume slider
- Fullscreen button

### Bài 4 (Dễ): SVG Icon Library
Tạo:
- 10 SVG icons
- Scalable và color-customizable
- Sprite sheet

### Bài 5 (Trung bình): Product Image Viewer
Tạo viewer với:
- Main image display
- Thumbnail gallery
- Zoom on hover
- Image format fallbacks

### Bài 6 (Trung bình): Podcast Player
Tạo player với:
- Episode list
- Auto-play next episode
- Playback speed control
- Save progress

### Bài 7 (Trung bình): Canvas Drawing App
Tạo app với:
- Drawing tools (pen, eraser, shapes)
- Color picker
- Undo/Redo
- Save as image

### Bài 8 (Trung bình): Video Course Platform
Tạo platform với:
- Video player với subtitles
- Lesson playlist
- Progress tracking
- Picture-in-Picture support

### Bài 9 (Trung bình): Interactive Floor Plan
Tạo floor plan với:
- Image map areas
- Room information popups
- Booking functionality
- Responsive design

### Bài 10 (Khó): Advanced Image Editor
Tạo editor với:
- Filters (grayscale, sepia, blur, etc.)
- Crop và rotate
- Text overlay
- Download functionality

### Bài 11 (Khó): WebRTC Video Chat
Tạo video chat với:
- Camera và microphone access
- Local và remote video
- Snapshot capture
- Stream recording

### Bài 12 (Khó): Audio Visualizer
Tạo visualizer với:
- Web Audio API integration
- Real-time frequency visualization
- EQ controls (bass, treble)
- Multiple visualization modes

---

**Kết luận:** Trong chương này, chúng ta đã học chi tiết về images, audio, video, SVG, Canvas với 5 use cases thực tế, 10 tips & tricks, 10 common mistakes, 10 troubleshooting issues, 5 advanced topics và 12 bài tập từ dễ đến khó. Chương tiếp theo sẽ tìm hiểu về Tables.
