#!/usr/bin/env python3
"""
Script to generate additional content for HTML5 chapters
"""

import os

BASE_DIR = "/home/user/TaiLieuHocTheoDeCuongMonHocTruongDaiHoc/Ly-Thuyet-HTML5"

# Content templates for each chapter
CHAPTERS_CONTENT = {
    "Chuong-05-Hinh-Anh-Va-Multimedia.md": {
        "insert_before": "## 5.9. Bài tập thực hành",
        "content": """
## 5.9. Practical Complete Examples

### 5.9.1. Image Gallery with Lightbox

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Photo Gallery</title>
    <style>
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1rem;
            padding: 2rem;
        }

        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 8px;
            cursor: pointer;
        }

        .gallery-item img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            transition: transform 0.3s;
        }

        .gallery-item:hover img {
            transform: scale(1.1);
        }

        .lightbox {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            z-index: 9999;
            justify-content: center;
            align-items: center;
        }

        .lightbox.active {
            display: flex;
        }

        .lightbox img {
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
        }

        .lightbox-close {
            position: absolute;
            top: 20px;
            right: 40px;
            font-size: 3rem;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="gallery">
        <div class="gallery-item" onclick="openLightbox('image1.jpg')">
            <img src="image1.jpg" alt="Image 1" loading="lazy">
        </div>
        <div class="gallery-item" onclick="openLightbox('image2.jpg')">
            <img src="image2.jpg" alt="Image 2" loading="lazy">
        </div>
        <div class="gallery-item" onclick="openLightbox('image3.jpg')">
            <img src="image3.jpg" alt="Image 3" loading="lazy">
        </div>
    </div>

    <div class="lightbox" id="lightbox" onclick="closeLightbox()">
        <span class="lightbox-close">&times;</span>
        <img src="" alt="" id="lightbox-img">
    </div>

    <script>
        function openLightbox(src) {
            document.getElementById('lightbox').classList.add('active');
            document.getElementById('lightbox-img').src = src;
        }

        function closeLightbox() {
            document.getElementById('lightbox').classList.remove('active');
        }
    </script>
</body>
</html>
```

### 5.9.2. Responsive Video Player

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Video Player</title>
    <style>
        .video-container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .video-wrapper {
            position: relative;
            padding-bottom: 56.25%; /* 16:9 aspect ratio */
            height: 0;
            overflow: hidden;
            background: #000;
            border-radius: 8px;
        }

        .video-wrapper video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .custom-controls {
            margin-top: 1rem;
            display: flex;
            gap: 1rem;
            align-items: center;
        }

        .custom-controls button {
            padding: 0.5rem 1rem;
            border: none;
            background: #007bff;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        .progress-bar {
            flex: 1;
            height: 5px;
            background: #dee2e6;
            border-radius: 5px;
            cursor: pointer;
            position: relative;
        }

        .progress {
            height: 100%;
            background: #007bff;
            border-radius: 5px;
            width: 0%;
        }
    </style>
</head>
<body>
    <div class="video-container">
        <div class="video-wrapper">
            <video id="myVideo">
                <source src="video.mp4" type="video/mp4">
                <source src="video.webm" type="video/webm">
                <track kind="subtitles" src="subtitles-vi.vtt" srclang="vi" label="Tiếng Việt">
                <track kind="subtitles" src="subtitles-en.vtt" srclang="en" label="English">
                Your browser doesn't support video.
            </video>
        </div>

        <div class="custom-controls">
            <button id="playPause">Play</button>
            <button id="stop">Stop</button>
            <div class="progress-bar" id="progressBar">
                <div class="progress" id="progress"></div>
            </div>
            <span id="time">0:00 / 0:00</span>
            <button id="fullscreen">Fullscreen</button>
        </div>
    </div>

    <script>
        const video = document.getElementById('myVideo');
        const playPause = document.getElementById('playPause');
        const stop = document.getElementById('stop');
        const progress = document.getElementById('progress');
        const progressBar = document.getElementById('progressBar');
        const time = document.getElementById('time');
        const fullscreen = document.getElementById('fullscreen');

        playPause.addEventListener('click', () => {
            if (video.paused) {
                video.play();
                playPause.textContent = 'Pause';
            } else {
                video.pause();
                playPause.textContent = 'Play';
            }
        });

        stop.addEventListener('click', () => {
            video.pause();
            video.currentTime = 0;
            playPause.textContent = 'Play';
        });

        video.addEventListener('timeupdate', () => {
            const percent = (video.currentTime / video.duration) * 100;
            progress.style.width = percent + '%';

            const currentMin = Math.floor(video.currentTime / 60);
            const currentSec = Math.floor(video.currentTime % 60);
            const durationMin = Math.floor(video.duration / 60);
            const durationSec = Math.floor(video.duration % 60);

            time.textContent = `${currentMin}:${currentSec.toString().padStart(2, '0')} / ${durationMin}:${durationSec.toString().padStart(2, '0')}`;
        });

        progressBar.addEventListener('click', (e) => {
            const rect = progressBar.getBoundingClientRect();
            const pos = (e.clientX - rect.left) / rect.width;
            video.currentTime = pos * video.duration;
        });

        fullscreen.addEventListener('click', () => {
            if (video.requestFullscreen) {
                video.requestFullscreen();
            }
        });
    </script>
</body>
</html>
```

## 5.10. Tips & Tricks

### Image Optimization Tips

**1. Choose Right Format**
- JPEG: Photos, complex images
- PNG: Graphics with transparency
- WebP: Modern format, 25-35% smaller
- SVG: Icons, logos, simple graphics

**2. Compress Images**
```bash
# Using ImageMagick
convert input.jpg -quality 85 output.jpg

# Using WebP
cwebp -q 80 input.jpg -o output.webp
```

**3. Responsive Images**
```html
<picture>
    <source media="(min-width: 1200px)" srcset="large.webp" type="image/webp">
    <source media="(min-width: 768px)" srcset="medium.webp" type="image/webp">
    <img src="small.jpg" alt="Description" loading="lazy">
</picture>
```

**4. Lazy Loading**
```html
<img src="image.jpg" alt="Description" loading="lazy">
```

**5. Use CDN for Images**
```html
<img src="https://cdn.example.com/images/photo.jpg" alt="Photo">
```

### Video/Audio Tips

**6. Multiple Formats**
```html
<video controls>
    <source src="video.webm" type="video/webm">
    <source src="video.mp4" type="video/mp4">
</video>
```

**7. Preload Strategy**
```html
<!-- Don't preload on mobile -->
<video controls preload="none">
    <source src="video.mp4" type="video/mp4">
</video>
```

**8. Poster Image**
```html
<video controls poster="thumbnail.jpg">
    <source src="video.mp4" type="video/mp4">
</video>
```

**9. Subtitles/Captions**
```html
<video controls>
    <source src="video.mp4" type="video/mp4">
    <track kind="captions" src="captions.vtt" srclang="en" label="English" default>
    <track kind="subtitles" src="subtitles.vtt" srclang="vi" label="Tiếng Việt">
</video>
```

**10. Autoplay Best Practices**
```html
<!-- Muted autoplay is allowed -->
<video autoplay muted loop playsinline>
    <source src="video.mp4" type="video/mp4">
</video>
```

## 5.11. Common Mistakes

### Mistake 1: Not Providing Alt Text
```html
<!-- SAI -->
<img src="logo.jpg">

<!-- ĐÚNG -->
<img src="logo.jpg" alt="Company Logo">
```
**Tại sao:** Alt text cần thiết cho accessibility và SEO.

### Mistake 2: Using Wrong Image Format
```html
<!-- SAI - Using PNG for photos -->
<img src="photo.png" alt="Photo">

<!-- ĐÚNG - Use JPEG/WebP for photos -->
<img src="photo.jpg" alt="Photo">
```
**Tại sao:** PNG files lớn hơn nhiều cho photos.

### Mistake 3: Not Optimizing Images
```html
<!-- SAI - 5MB image -->
<img src="huge-image.jpg" alt="Photo">

<!-- ĐÚNG - Optimized image -->
<img src="optimized-image.jpg" alt="Photo" width="800" height="600">
```
**Tại sao:** Ảnh không tối ưu làm chậm page load.

### Mistake 4: Forgetting Video Fallback
```html
<!-- SAI -->
<video controls>
    <source src="video.mp4" type="video/mp4">
</video>

<!-- ĐÚNG -->
<video controls>
    <source src="video.mp4" type="video/mp4">
    <p>Your browser doesn't support video. <a href="video.mp4">Download video</a></p>
</video>
```
**Tại sao:** Cần fallback cho browsers không support.

### Mistake 5: Using Inline Base64 Images
```html
<!-- SAI - Large base64 in HTML -->
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhE..." alt="Image">

<!-- ĐÚNG - External file -->
<img src="image.png" alt="Image">
```
**Tại sao:** Base64 tăng HTML size và không cacheable.

### Mistake 6: Not Using Responsive Images
```html
<!-- SAI - Same image for all sizes -->
<img src="large.jpg" alt="Photo">

<!-- ĐÚNG - Responsive images -->
<img src="small.jpg"
     srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
     sizes="(max-width: 400px) 400px, (max-width: 800px) 800px, 1200px"
     alt="Photo">
```
**Tại sao:** Mobile users tải ảnh quá lớn.

### Mistake 7: Autoplay Video with Sound
```html
<!-- SAI - Autoplay with sound -->
<video autoplay controls>
    <source src="video.mp4" type="video/mp4">
</video>

<!-- ĐÚNG - Muted autoplay -->
<video autoplay muted controls>
    <source src="video.mp4" type="video/mp4">
</video>
```
**Tại sao:** Browsers block autoplay with sound.

### Mistake 8: Missing Width/Height
```html
<!-- SAI - No dimensions -->
<img src="image.jpg" alt="Image">

<!-- ĐÚNG - Include dimensions -->
<img src="image.jpg" alt="Image" width="800" height="600">
```
**Tại sao:** Prevents layout shift khi image load.

### Mistake 9: Using `<img>` for Decorative Images
```html
<!-- SAI -->
<img src="decoration.png" alt="decoration">

<!-- ĐÚNG -->
<div style="background-image: url('decoration.png')" role="presentation"></div>
<!-- Or -->
<img src="decoration.png" alt="" role="presentation">
```
**Tại sao:** Decorative images nên có empty alt.

### Mistake 10: Not Testing Video on Mobile
```html
<!-- SAI - No mobile consideration -->
<video controls>
    <source src="4k-video.mp4" type="video/mp4">
</video>

<!-- ĐÚNG - Mobile-optimized -->
<video controls preload="metadata">
    <source src="mobile-video.mp4" type="video/mp4" media="(max-width: 768px)">
    <source src="desktop-video.mp4" type="video/mp4">
</video>
```
**Tại sao:** 4K video quá nặng cho mobile.

## 5.12. Troubleshooting

### Issue 1: Images Not Loading
**Problem:** Images không hiển thị

**Solutions:**
- Check file path
- Verify file permissions
- Check image format support
- Look for CORS issues

### Issue 2: Video Not Playing on iOS
**Problem:** Video không play trên iPhone/iPad

**Solution:**
```html
<video controls playsinline>
    <source src="video.mp4" type="video/mp4">
</video>
```
**Giải thích:** iOS requires `playsinline` attribute.

### Issue 3: Images Load Slowly
**Problem:** Images tải chậm

**Solutions:**
- Compress images
- Use WebP format
- Implement lazy loading
- Use CDN
- Enable browser caching

### Issue 4: Video Controls Not Working
**Problem:** Custom video controls không hoạt động

**Solution:**
```javascript
// Remove default controls first
video.removeAttribute('controls');

// Then add custom controls
```

### Issue 5: Aspect Ratio Issues
**Problem:** Images bị stretch/squash

**Solution:**
```css
img {
    width: 100%;
    height: auto;
    object-fit: cover; /* or contain */
}
```

### Issue 6: Canvas Drawing Blurry
**Problem:** Canvas graphics bị blur trên high-DPI screens

**Solution:**
```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const dpr = window.devicePixelRatio || 1;

canvas.width = 800 * dpr;
canvas.height = 600 * dpr;
canvas.style.width = '800px';
canvas.style.height = '600px';

ctx.scale(dpr, dpr);
```

## 5.13. Advanced Topics

### 5.13.1. Progressive Image Loading

```html
<style>
    .progressive-image {
        position: relative;
        overflow: hidden;
    }

    .progressive-image img {
        width: 100%;
        transition: opacity 0.3s;
    }

    .progressive-image img.blurred {
        filter: blur(20px);
        transform: scale(1.1);
    }

    .progressive-image img.loaded {
        filter: none;
        transform: none;
    }
</style>

<div class="progressive-image">
    <img src="tiny-placeholder.jpg"
         data-large="full-size.jpg"
         alt="Image"
         class="blurred">
</div>

<script>
document.querySelectorAll('.progressive-image img').forEach(img => {
    const largeImage = new Image();
    largeImage.src = img.dataset.large;

    largeImage.onload = () => {
        img.src = largeImage.src;
        img.classList.remove('blurred');
        img.classList.add('loaded');
    };
});
</script>
```

### 5.13.2. Image Comparison Slider

```html
<div class="image-compare">
    <img src="before.jpg" alt="Before">
    <img src="after.jpg" alt="After" class="overlay">
    <div class="slider"></div>
</div>

<style>
.image-compare {
    position: relative;
    overflow: hidden;
}

.image-compare img {
    width: 100%;
    display: block;
}

.image-compare .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 50%;
    clip-path: inset(0 50% 0 0);
}

.slider {
    position: absolute;
    top: 0;
    left: 50%;
    width: 4px;
    height: 100%;
    background: white;
    cursor: ew-resize;
}
</style>

<script>
const compare = document.querySelector('.image-compare');
const slider = compare.querySelector('.slider');
const overlay = compare.querySelector('.overlay');

let isDragging = false;

slider.addEventListener('mousedown', () => isDragging = true);
document.addEventListener('mouseup', () => isDragging = false);

document.addEventListener('mousemove', (e) => {
    if (!isDragging) return;

    const rect = compare.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const percent = (x / rect.width) * 100;

    slider.style.left = percent + '%';
    overlay.style.width = percent + '%';
    overlay.style.clipPath = `inset(0 ${100 - percent}% 0 0)`;
});
</script>
```

## 5.14. Bài tập thực hành mở rộng

### Bài 1: Responsive Image Gallery (Dễ)
**Yêu cầu:**
- Grid layout responsive
- 12 images với proper alt text
- Lazy loading
- Hover effects
- Mobile-friendly

### Bài 2: Lightbox Gallery (Dễ)
**Yêu cầu:**
- Click to open lightbox
- Navigation (prev/next)
- Close button
- Keyboard navigation (arrows, ESC)
- Touch swipe support

### Bài 3: Custom Video Player (Trung bình)
**Yêu cầu:**
- Play/pause button
- Progress bar
- Volume control
- Fullscreen toggle
- Subtitles support
- Responsive design

### Bài 4: Audio Playlist (Trung bình)
**Yêu cầu:**
- Multiple tracks
- Track list UI
- Play/pause per track
- Progress indicators
- Auto-play next track

### Bài 5: SVG Animation (Trung bình)
**Yêu cầu:**
- Animated logo SVG
- CSS animations
- Interactive hover effects
- Fallback PNG
- Accessible

### Bài 6: Canvas Drawing App (Khó)
**Yêu cầu:**
- Drawing tools (pen, eraser)
- Color picker
- Line width control
- Clear canvas
- Save as image
- Touch support

### Bài 7: Image Lazy Loading (Trung bình)
**Yêu cầu:**
- Intersection Observer
- Placeholder images
- Loading indicators
- Error handling
- Performance optimized

### Bài 8: Picture Element (Dễ)
**Yêu cầu:**
- Multiple sources
- Art direction
- WebP with fallback
- Responsive breakpoints
- Proper alt text

### Bài 9: Video Background (Trung bình)
**Yêu cầu:**
- Fullscreen video background
- Muted autoplay
- Mobile fallback image
- Performance optimized
- Accessible controls

### Bài 10: Image Comparison Slider (Khó)
**Yêu cầu:**
- Before/after images
- Draggable slider
- Touch support
- Responsive
- Smooth animations

### Bài 11: Media Gallery with Filters (Khó)
**Yêu cầu:**
- Mixed media (images, videos)
- Filter by category
- Search functionality
- Sorting options
- Pagination
- Full accessibility

### Bài 12: Progressive Web App Gallery (Rất khó)
**Yêu cầu:**
- Offline support
- Service Worker caching
- Progressive image loading
- Upload functionality
- IndexedDB storage
- Share API integration
- Performance optimized

---

"""
    },

    # Add more chapters here with similar structure
}

def main():
    print("This script template is ready for content generation.")
    print("Content will be added to chapters programmatically.")

if __name__ == "__main__":
    main()
