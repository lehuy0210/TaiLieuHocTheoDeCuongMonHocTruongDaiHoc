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

## 5.9. Bài tập thực hành

### Bài 1: Images
Tạo trang với:
- Các loại images: JPEG, PNG, SVG
- Responsive images với srcset
- Picture element với multiple formats
- Figure với figcaption

### Bài 2: Audio Player
Tạo:
- Custom audio player
- Multiple audio sources
- Playlist functionality

### Bài 3: Video Gallery
Tạo:
- Video gallery với thumbnails
- Video với subtitles
- Responsive video player
- Embedded YouTube videos

### Bài 4: SVG và Canvas
Tạo:
- Logo bằng SVG
- Chart bằng Canvas
- Animation với Canvas

---

**Kết luận:** Trong chương này, chúng ta đã học về images, audio, video, SVG, Canvas và các best practices cho multimedia trong HTML5. Chương tiếp theo sẽ tìm hiểu về Tables.
