# CHƯƠNG 9: HTML5 APIs

## 9.1. Geolocation API

### 9.1.1. Lấy vị trí hiện tại

```javascript
if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
        // Success callback
        (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            const accuracy = position.coords.accuracy;
            console.log(`Lat: ${lat}, Lon: ${lon}`);
        },
        // Error callback
        (error) => {
            console.error(`Error: ${error.message}`);
        },
        // Options
        {
            enableHighAccuracy: true,
            timeout: 5000,
            maximumAge: 0
        }
    );
} else {
    console.log("Geolocation not supported");
}
```

### 9.1.2. Watch Position

```javascript
const watchId = navigator.geolocation.watchPosition(
    (position) => {
        console.log(`New position: ${position.coords.latitude}, ${position.coords.longitude}`);
    },
    (error) => {
        console.error(error);
    }
);

// Stop watching
navigator.geolocation.clearWatch(watchId);
```

## 9.2. Drag and Drop API

### 9.2.1. Draggable Element

```html
<div id="drag1" draggable="true" ondragstart="drag(event)">
    Drag me
</div>

<div id="dropzone"
     ondrop="drop(event)"
     ondragover="allowDrop(event)">
    Drop here
</div>

<script>
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}
</script>
```

### 9.2.2. Drag Events

```javascript
element.addEventListener('dragstart', (e) => {
    // Bắt đầu kéo
    e.dataTransfer.effectAllowed = 'move';
});

element.addEventListener('drag', (e) => {
    // Đang kéo
});

element.addEventListener('dragend', (e) => {
    // Kết thúc kéo
});

dropzone.addEventListener('dragenter', (e) => {
    // Vào vùng drop
    e.preventDefault();
});

dropzone.addEventListener('dragover', (e) => {
    // Hover trên vùng drop
    e.preventDefault();
});

dropzone.addEventListener('dragleave', (e) => {
    // Rời khỏi vùng drop
});

dropzone.addEventListener('drop', (e) => {
    // Thả xuống
    e.preventDefault();
});
```

## 9.3. Web Storage API

### 9.3.1. localStorage

```javascript
// Lưu data
localStorage.setItem('username', 'john');
localStorage.setItem('age', '25');

// Lưu object
const user = { name: 'John', age: 25 };
localStorage.setItem('user', JSON.stringify(user));

// Đọc data
const username = localStorage.getItem('username');
const userObj = JSON.parse(localStorage.getItem('user'));

// Xóa item
localStorage.removeItem('username');

// Xóa tất cả
localStorage.clear();

// Check tồn tại
if (localStorage.getItem('username')) {
    console.log('Username exists');
}

// Lấy key theo index
const key = localStorage.key(0);

// Số lượng items
const count = localStorage.length;
```

### 9.3.2. sessionStorage

```javascript
// Tương tự localStorage nhưng chỉ tồn tại trong session
sessionStorage.setItem('temp', 'value');
const temp = sessionStorage.getItem('temp');
sessionStorage.removeItem('temp');
sessionStorage.clear();
```

### 9.3.3. Storage Events

```javascript
window.addEventListener('storage', (e) => {
    console.log('Key:', e.key);
    console.log('Old Value:', e.oldValue);
    console.log('New Value:', e.newValue);
    console.log('URL:', e.url);
});
```

## 9.4. Web Workers

### 9.4.1. Tạo Worker

**main.js:**
```javascript
if (window.Worker) {
    const worker = new Worker('worker.js');

    // Send message to worker
    worker.postMessage({ cmd: 'start', value: 100 });

    // Receive message from worker
    worker.onmessage = (e) => {
        console.log('Result:', e.data);
    };

    // Handle errors
    worker.onerror = (e) => {
        console.error('Error:', e.message);
    };

    // Terminate worker
    worker.terminate();
}
```

**worker.js:**
```javascript
// Listen for messages
onmessage = function(e) {
    const { cmd, value } = e.data;

    if (cmd === 'start') {
        const result = heavyComputation(value);
        postMessage(result);
    }
};

function heavyComputation(n) {
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += i;
    }
    return sum;
}
```

## 9.5. WebSocket API

### 9.5.1. Kết nối WebSocket

```javascript
const socket = new WebSocket('ws://localhost:8080');

// Connection opened
socket.addEventListener('open', (event) => {
    console.log('Connected');
    socket.send('Hello Server!');
});

// Listen for messages
socket.addEventListener('message', (event) => {
    console.log('Message from server:', event.data);
});

// Connection closed
socket.addEventListener('close', (event) => {
    console.log('Disconnected');
});

// Error handling
socket.addEventListener('error', (error) => {
    console.error('WebSocket error:', error);
});

// Send data
socket.send('Message to server');
socket.send(JSON.stringify({ type: 'chat', message: 'Hello' }));

// Close connection
socket.close();
```

### 9.5.2. Ready State

```javascript
switch (socket.readyState) {
    case WebSocket.CONNECTING:
        console.log('Connecting...');
        break;
    case WebSocket.OPEN:
        console.log('Open');
        break;
    case WebSocket.CLOSING:
        console.log('Closing...');
        break;
    case WebSocket.CLOSED:
        console.log('Closed');
        break;
}
```

## 9.6. History API

### 9.6.1. Manipulate Browser History

```javascript
// Push state
history.pushState({ page: 1 }, 'Page 1', '/page1');

// Replace state
history.replaceState({ page: 2 }, 'Page 2', '/page2');

// Go back
history.back();

// Go forward
history.forward();

// Go to specific page
history.go(-2); // 2 pages back
history.go(1);  // 1 page forward

// Get current state
console.log(history.state);

// Listen for popstate
window.addEventListener('popstate', (event) => {
    console.log('State:', event.state);
});
```

## 9.7. File API

### 9.7.1. Read Files

```html
<input type="file" id="fileInput" accept="image/*" multiple>
<img id="preview">

<script>
const input = document.getElementById('fileInput');
const preview = document.getElementById('preview');

input.addEventListener('change', (e) => {
    const file = e.target.files[0];

    if (file) {
        // FileReader
        const reader = new FileReader();

        reader.onload = (e) => {
            preview.src = e.target.result;
        };

        reader.readAsDataURL(file);
        // or reader.readAsText(file);
        // or reader.readAsArrayBuffer(file);
    }
});
</script>
```

### 9.7.2. File Properties

```javascript
const file = input.files[0];

console.log('Name:', file.name);
console.log('Size:', file.size);
console.log('Type:', file.type);
console.log('Last Modified:', new Date(file.lastModified));
```

### 9.7.3. Drag and Drop Files

```html
<div id="dropzone">Drop files here</div>

<script>
const dropzone = document.getElementById('dropzone');

dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
});

dropzone.addEventListener('drop', (e) => {
    e.preventDefault();

    const files = e.dataTransfer.files;

    for (let file of files) {
        console.log('File:', file.name);
    }
});
</script>
```

## 9.8. Notification API

### 9.8.1. Show Notifications

```javascript
// Request permission
if ('Notification' in window) {
    Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
            // Show notification
            const notification = new Notification('Title', {
                body: 'Notification body text',
                icon: '/icon.png',
                badge: '/badge.png',
                tag: 'unique-tag',
                requireInteraction: false,
                silent: false
            });

            // Click event
            notification.onclick = () => {
                console.log('Notification clicked');
                window.focus();
                notification.close();
            };

            // Close after 5 seconds
            setTimeout(() => notification.close(), 5000);
        }
    });
}

// Check permission status
console.log(Notification.permission); // "default", "granted", "denied"
```

## 9.9. Page Visibility API

```javascript
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        console.log('Page is hidden');
        // Pause video, stop animations
    } else {
        console.log('Page is visible');
        // Resume video, animations
    }
});

// Check visibility
if (document.hidden) {
    console.log('Page is currently hidden');
}
```

## 9.10. Fullscreen API

```javascript
const element = document.getElementById('myElement');

// Enter fullscreen
function enterFullscreen() {
    if (element.requestFullscreen) {
        element.requestFullscreen();
    } else if (element.webkitRequestFullscreen) {
        element.webkitRequestFullscreen();
    } else if (element.msRequestFullscreen) {
        element.msRequestFullscreen();
    }
}

// Exit fullscreen
function exitFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
        document.msExitFullscreen();
    }
}

// Check fullscreen
if (document.fullscreenElement) {
    console.log('In fullscreen mode');
}

// Fullscreen change event
document.addEventListener('fullscreenchange', () => {
    if (document.fullscreenElement) {
        console.log('Entered fullscreen');
    } else {
        console.log('Exited fullscreen');
    }
});
```

## 9.11. Vibration API

```javascript
if ('vibrate' in navigator) {
    // Vibrate for 200ms
    navigator.vibrate(200);

    // Pattern: vibrate, pause, vibrate
    navigator.vibrate([100, 50, 100]);

    // Stop vibration
    navigator.vibrate(0);
}
```

## 9.12. Battery Status API

```javascript
if ('getBattery' in navigator) {
    navigator.getBattery().then(battery => {
        console.log('Battery level:', battery.level * 100 + '%');
        console.log('Charging:', battery.charging);
        console.log('Charging time:', battery.chargingTime);
        console.log('Discharging time:', battery.dischargingTime);

        // Events
        battery.addEventListener('levelchange', () => {
            console.log('Battery level changed:', battery.level);
        });

        battery.addEventListener('chargingchange', () => {
            console.log('Charging status:', battery.charging);
        });
    });
}
```

## 9.13. Clipboard API

```javascript
// Copy text
async function copyText(text) {
    try {
        await navigator.clipboard.writeText(text);
        console.log('Text copied');
    } catch (err) {
        console.error('Failed to copy:', err);
    }
}

// Paste text
async function pasteText() {
    try {
        const text = await navigator.clipboard.readText();
        console.log('Pasted:', text);
        return text;
    } catch (err) {
        console.error('Failed to paste:', err);
    }
}

// Copy with fallback
function copyTextFallback(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
}
```

## 9.14. Intersection Observer API

```javascript
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            console.log('Element is visible');
            entry.target.classList.add('visible');
        } else {
            console.log('Element is not visible');
            entry.target.classList.remove('visible');
        }
    });
}, {
    root: null, // viewport
    rootMargin: '0px',
    threshold: 0.5 // 50% visible
});

// Observe elements
const elements = document.querySelectorAll('.animate-on-scroll');
elements.forEach(el => observer.observe(el));

// Unobserve
observer.unobserve(element);

// Disconnect
observer.disconnect();
```

## 9.15. Resize Observer API

```javascript
const resizeObserver = new ResizeObserver(entries => {
    entries.forEach(entry => {
        console.log('Element size changed');
        console.log('Width:', entry.contentRect.width);
        console.log('Height:', entry.contentRect.height);
    });
});

// Observe element
resizeObserver.observe(document.getElementById('myElement'));

// Unobserve
resizeObserver.unobserve(element);

// Disconnect
resizeObserver.disconnect();
```

## 9.16. Practical Examples

### 9.16.1. Auto-save Form với localStorage

```javascript
const form = document.getElementById('myForm');
const inputs = form.querySelectorAll('input, textarea');

// Load saved data
inputs.forEach(input => {
    const saved = localStorage.getItem(input.name);
    if (saved) {
        input.value = saved;
    }
});

// Save on input
inputs.forEach(input => {
    input.addEventListener('input', (e) => {
        localStorage.setItem(e.target.name, e.target.value);
    });
});

// Clear on submit
form.addEventListener('submit', () => {
    inputs.forEach(input => {
        localStorage.removeItem(input.name);
    });
});
```

### 9.16.2. Lazy Loading Images

```javascript
const images = document.querySelectorAll('img[data-src]');

const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
            imageObserver.unobserve(img);
        }
    });
});

images.forEach(img => imageObserver.observe(img));
```

### 9.16.3. Real-time Notification System

```javascript
async function setupNotifications() {
    if ('Notification' in window) {
        const permission = await Notification.requestPermission();

        if (permission === 'granted') {
            // WebSocket connection
            const socket = new WebSocket('ws://localhost:8080/notifications');

            socket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                new Notification(data.title, {
                    body: data.message,
                    icon: '/icon.png'
                });
            };
        }
    }
}
```

## 9.17. Use Cases Thực Tế

### Use Case 1: Weather App với Geolocation API
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Weather App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; display: flex; justify-content: center; align-items: center; }
        .container { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); max-width: 500px; width: 100%; }
        h1 { color: #333; margin-bottom: 30px; text-align: center; }
        .location { background: #f5f5f5; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .location h2 { font-size: 1.3em; color: #667eea; margin-bottom: 10px; }
        .weather-info { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
        .info-item { background: #f9f9f9; padding: 15px; border-radius: 10px; border-left: 4px solid #667eea; }
        .info-item h3 { font-size: 0.9em; color: #999; margin-bottom: 5px; }
        .info-item p { font-size: 1.5em; color: #333; font-weight: bold; }
        button { background: #667eea; color: white; border: none; padding: 12px 30px; border-radius: 8px; font-size: 1em; cursor: pointer; width: 100%; }
        button:hover { background: #764ba2; }
        .error { color: #e74c3c; padding: 15px; background: #ffe6e6; border-radius: 8px; display: none; }
        .loading { display: none; text-align: center; color: #667eea; }
        .forecast { margin-top: 30px; }
        .forecast h3 { margin-bottom: 15px; color: #333; }
        .forecast-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 10px; }
        .forecast-card { background: #f5f5f5; padding: 15px; border-radius: 8px; text-align: center; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Weather App</h1>

        <div class="loading" id="loading">
            <p>Đang lấy vị trí...</p>
        </div>

        <div class="error" id="error"></div>

        <div class="location" id="location" style="display: none;">
            <h2 id="city"></h2>
            <p id="coordinates"></p>

            <div class="weather-info">
                <div class="info-item">
                    <h3>Nhiệt độ</h3>
                    <p id="temp"></p>
                </div>
                <div class="info-item">
                    <h3>Độ ẩm</h3>
                    <p id="humidity"></p>
                </div>
                <div class="info-item">
                    <h3>Tốc độ gió</h3>
                    <p id="windSpeed"></p>
                </div>
                <div class="info-item">
                    <h3>Mô tả</h3>
                    <p id="description"></p>
                </div>
            </div>

            <button style="margin-top: 20px;" onclick="getLocation()">Cập nhật vị trí</button>
        </div>
    </div>

    <script>
        const loading = document.getElementById('loading');
        const error = document.getElementById('error');
        const location = document.getElementById('location');

        // Mock weather data (trong thực tế sẽ gọi API)
        function mockWeatherData(lat, lon) {
            return {
                city: 'Hà Nội',
                temp: '28°C',
                humidity: '75%',
                windSpeed: '10 km/h',
                description: 'Nắng nhẹ'
            };
        }

        function getLocation() {
            loading.style.display = 'block';
            error.style.display = 'none';
            location.style.display = 'none';

            if ('geolocation' in navigator) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        const lat = position.coords.latitude;
                        const lon = position.coords.longitude;
                        const accuracy = position.coords.accuracy;

                        const weather = mockWeatherData(lat, lon);

                        document.getElementById('city').textContent = weather.city;
                        document.getElementById('coordinates').textContent = `Vĩ độ: ${lat.toFixed(4)}, Kinh độ: ${lon.toFixed(4)}`;
                        document.getElementById('temp').textContent = weather.temp;
                        document.getElementById('humidity').textContent = weather.humidity;
                        document.getElementById('windSpeed').textContent = weather.windSpeed;
                        document.getElementById('description').textContent = weather.description;

                        loading.style.display = 'none';
                        location.style.display = 'block';

                        // Save to localStorage
                        localStorage.setItem('lastLocation', JSON.stringify({
                            lat, lon, timestamp: new Date().toISOString()
                        }));
                    },
                    (err) => {
                        error.style.display = 'block';
                        error.textContent = 'Lỗi: ' + err.message;
                        loading.style.display = 'none';
                    },
                    {
                        enableHighAccuracy: true,
                        timeout: 5000,
                        maximumAge: 0
                    }
                );
            } else {
                error.style.display = 'block';
                error.textContent = 'Browser không hỗ trợ Geolocation';
                loading.style.display = 'none';
            }
        }

        // Get location on page load
        window.addEventListener('load', getLocation);
    </script>
</body>
</html>
```

### Use Case 2: Notes App với LocalStorage
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Notes App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #f5f5f5; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { text-align: center; color: #333; margin-bottom: 30px; }
        .input-area { display: grid; grid-template-columns: 1fr 100px; gap: 10px; margin-bottom: 30px; }
        input[type="text"] { padding: 12px; border: 2px solid #ddd; border-radius: 8px; font-size: 1em; }
        button { background: #667eea; color: white; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; }
        button:hover { background: #764ba2; }
        .notes { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
        .note { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: relative; }
        .note h3 { margin-bottom: 10px; color: #333; word-wrap: break-word; }
        .note p { color: #666; font-size: 0.9em; margin-bottom: 10px; word-wrap: break-word; }
        .note-time { font-size: 0.8em; color: #999; margin-bottom: 15px; }
        .delete-btn { background: #e74c3c; padding: 5px 10px; font-size: 0.8em; width: auto; }
        .empty { text-align: center; color: #999; padding: 40px; grid-column: 1 / -1; }
        .clear-all { margin-top: 20px; background: #c0392b; width: 100%; }
    </style>
</head>
<body>
    <div class="container">
        <h1>My Notes</h1>

        <div class="input-area">
            <input type="text" id="noteInput" placeholder="Nhập ghi chú mới..." onkeypress="handleKeyPress(event)">
            <button onclick="addNote()">Thêm</button>
        </div>

        <div class="notes" id="notesList"></div>
        <button class="clear-all" onclick="clearAll()">Xóa tất cả ghi chú</button>
    </div>

    <script>
        const STORAGE_KEY = 'notes_app';

        function loadNotes() {
            const notes = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
            displayNotes(notes);
        }

        function displayNotes(notes) {
            const notesList = document.getElementById('notesList');
            notesList.innerHTML = '';

            if (notes.length === 0) {
                notesList.innerHTML = '<div class="empty">Chưa có ghi chú nào. Hãy thêm ghi chú mới!</div>';
                return;
            }

            notes.forEach((note, index) => {
                const noteEl = document.createElement('div');
                noteEl.className = 'note';
                noteEl.innerHTML = `
                    <h3>${note.title}</h3>
                    <p>${note.content}</p>
                    <div class="note-time">${new Date(note.timestamp).toLocaleString('vi-VN')}</div>
                    <button class="delete-btn" onclick="deleteNote(${index})">Xóa</button>
                `;
                notesList.appendChild(noteEl);
            });
        }

        function addNote() {
            const input = document.getElementById('noteInput');
            const text = input.value.trim();

            if (!text) {
                alert('Vui lòng nhập ghi chú');
                return;
            }

            const notes = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

            // Extract title (first 50 chars) and content
            const title = text.substring(0, 50);
            const content = text;

            notes.unshift({
                title,
                content,
                timestamp: new Date().toISOString()
            });

            localStorage.setItem(STORAGE_KEY, JSON.stringify(notes));
            input.value = '';
            loadNotes();
        }

        function deleteNote(index) {
            if (confirm('Bạn chắc chắn muốn xóa?')) {
                const notes = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
                notes.splice(index, 1);
                localStorage.setItem(STORAGE_KEY, JSON.stringify(notes));
                loadNotes();
            }
        }

        function clearAll() {
            if (confirm('Xóa tất cả ghi chú? Hành động này không thể hoàn tác.')) {
                localStorage.removeItem(STORAGE_KEY);
                loadNotes();
            }
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                addNote();
            }
        }

        // Load notes on page load
        window.addEventListener('load', loadNotes);
    </script>
</body>
</html>
```

### Use Case 3: Drag and Drop File Uploader
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>File Uploader</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #f5f5f5; padding: 40px 20px; }
        .container { max-width: 600px; margin: 0 auto; }
        h1 { text-align: center; color: #333; margin-bottom: 30px; }
        .dropzone { border: 3px dashed #667eea; border-radius: 10px; padding: 40px; text-align: center; background: #f9f9f9; cursor: pointer; transition: all 0.3s; }
        .dropzone.dragover { background: #667eea; color: white; border-color: #764ba2; }
        .dropzone p { font-size: 1.1em; color: #666; margin-bottom: 10px; }
        .dropzone input { display: none; }
        .file-list { margin-top: 30px; }
        .file-list h2 { margin-bottom: 15px; color: #333; }
        .file-item { background: white; padding: 15px; border-radius: 8px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .file-info { flex: 1; }
        .file-name { color: #333; font-weight: bold; }
        .file-size { font-size: 0.9em; color: #999; }
        .file-progress { width: 100%; background: #eee; border-radius: 4px; height: 4px; margin-top: 8px; overflow: hidden; }
        .progress-bar { height: 100%; background: #667eea; transition: width 0.3s; }
        .delete-btn { background: #e74c3c; color: white; border: none; padding: 5px 15px; border-radius: 4px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Drag and Drop File Uploader</h1>

        <div class="dropzone" id="dropzone" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
            <p>Kéo thả file vào đây</p>
            <p>hoặc</p>
            <button onclick="document.getElementById('fileInput').click()">Chọn file</button>
            <input type="file" id="fileInput" multiple onchange="handleFileSelect(event)">
        </div>

        <div class="file-list">
            <h2>Đã tải lên</h2>
            <div id="uploadedFiles"></div>
        </div>
    </div>

    <script>
        const dropzone = document.getElementById('dropzone');
        let uploadedFiles = [];

        function handleDragOver(e) {
            e.preventDefault();
            dropzone.classList.add('dragover');
        }

        function handleDragLeave(e) {
            e.preventDefault();
            dropzone.classList.remove('dragover');
        }

        function handleDrop(e) {
            e.preventDefault();
            dropzone.classList.remove('dragover');

            const files = e.dataTransfer.files;
            processFiles(files);
        }

        function handleFileSelect(e) {
            const files = e.target.files;
            processFiles(files);
        }

        function processFiles(files) {
            for (let file of files) {
                // Validate file
                if (file.size > 10 * 1024 * 1024) { // 10MB limit
                    alert(`File ${file.name} quá lớn (tối đa 10MB)`);
                    continue;
                }

                const fileObj = {
                    id: Date.now() + Math.random(),
                    name: file.name,
                    size: file.size,
                    type: file.type,
                    progress: 0
                };

                uploadedFiles.push(fileObj);

                // Simulate upload
                simulateUpload(fileObj);
            }

            displayFiles();
        }

        function simulateUpload(file) {
            const interval = setInterval(() => {
                file.progress += Math.random() * 30;
                if (file.progress >= 100) {
                    file.progress = 100;
                    clearInterval(interval);
                }
                displayFiles();
            }, 500);
        }

        function displayFiles() {
            const uploadedFilesDiv = document.getElementById('uploadedFiles');
            uploadedFilesDiv.innerHTML = '';

            if (uploadedFiles.length === 0) {
                uploadedFilesDiv.innerHTML = '<p style="color: #999;">Chưa có file nào</p>';
                return;
            }

            uploadedFiles.forEach(file => {
                const fileEl = document.createElement('div');
                fileEl.className = 'file-item';
                fileEl.innerHTML = `
                    <div class="file-info">
                        <div class="file-name">${file.name}</div>
                        <div class="file-size">${(file.size / 1024 / 1024).toFixed(2)} MB</div>
                        <div class="file-progress">
                            <div class="progress-bar" style="width: ${file.progress}%"></div>
                        </div>
                    </div>
                    <button class="delete-btn" onclick="deleteFile('${file.id}')">Xóa</button>
                `;
                uploadedFilesDiv.appendChild(fileEl);
            });
        }

        function deleteFile(id) {
            uploadedFiles = uploadedFiles.filter(f => f.id !== id);
            displayFiles();
        }
    </script>
</body>
</html>
```

### Use Case 4: Real-time Chat with WebSocket (Mock)
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Chat Application</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #f5f5f5; height: 100vh; display: flex; }
        .chat-container { width: 100%; max-width: 600px; margin: auto; background: white; height: 100vh; display: flex; flex-direction: column; box-shadow: 0 0 20px rgba(0,0,0,0.1); }
        .chat-header { background: #667eea; color: white; padding: 20px; text-align: center; }
        .chat-messages { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 10px; }
        .message { padding: 12px 16px; border-radius: 8px; max-width: 80%; word-wrap: break-word; }
        .message.sent { background: #667eea; color: white; align-self: flex-end; }
        .message.received { background: #f5f5f5; color: #333; align-self: flex-start; }
        .message-time { font-size: 0.8em; opacity: 0.7; margin-top: 4px; }
        .chat-input-area { display: flex; gap: 10px; padding: 20px; border-top: 1px solid #ddd; }
        input { flex: 1; padding: 12px; border: 2px solid #ddd; border-radius: 8px; font-size: 1em; }
        button { background: #667eea; color: white; border: none; padding: 12px 30px; border-radius: 8px; cursor: pointer; font-weight: bold; }
        button:hover { background: #764ba2; }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h1>Chat</h1>
            <p>Trực tuyến</p>
        </div>

        <div class="chat-messages" id="messages"></div>

        <div class="chat-input-area">
            <input type="text" id="messageInput" placeholder="Nhập tin nhắn..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Gửi</button>
        </div>
    </div>

    <script>
        const STORAGE_KEY = 'chat_messages';
        let messages = [];

        function loadMessages() {
            const saved = localStorage.getItem(STORAGE_KEY);
            messages = saved ? JSON.parse(saved) : [];
            displayMessages();
        }

        function displayMessages() {
            const messagesDiv = document.getElementById('messages');
            messagesDiv.innerHTML = '';

            messages.forEach(msg => {
                const msgEl = document.createElement('div');
                msgEl.className = `message ${msg.sent ? 'sent' : 'received'}`;
                msgEl.innerHTML = `
                    <div>${msg.text}</div>
                    <div class="message-time">${new Date(msg.timestamp).toLocaleTimeString('vi-VN')}</div>
                `;
                messagesDiv.appendChild(msgEl);
            });

            // Scroll to bottom
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const text = input.value.trim();

            if (!text) return;

            messages.push({
                text,
                sent: true,
                timestamp: new Date().toISOString()
            });

            localStorage.setItem(STORAGE_KEY, JSON.stringify(messages));
            input.value = '';
            displayMessages();

            // Simulate reply
            setTimeout(() => {
                messages.push({
                    text: 'Đã nhận: ' + text,
                    sent: false,
                    timestamp: new Date().toISOString()
                });
                localStorage.setItem(STORAGE_KEY, JSON.stringify(messages));
                displayMessages();
            }, 1000);
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }

        window.addEventListener('load', loadMessages);
    </script>
</body>
</html>
```

### Use Case 5: Task Manager with IndexedDB-like localStorage
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Task Manager</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { text-align: center; color: white; margin-bottom: 30px; }
        .add-task { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .add-task form { display: flex; gap: 10px; }
        input[type="text"] { flex: 1; padding: 12px; border: 2px solid #ddd; border-radius: 8px; }
        button { background: #667eea; color: white; border: none; padding: 12px 30px; border-radius: 8px; cursor: pointer; }
        .tasks { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .task { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .task h3 { margin-bottom: 10px; color: #333; }
        .task p { color: #666; margin-bottom: 15px; }
        .task-status { display: flex; gap: 10px; }
        .status-btn { padding: 8px 15px; border: none; border-radius: 5px; cursor: pointer; font-size: 0.9em; }
        .mark-done { background: #27ae60; color: white; }
        .delete-btn { background: #e74c3c; color: white; }
        .task.completed h3 { text-decoration: line-through; color: #999; }
        .stats { background: white; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 20px; }
        .stats p { color: #666; margin: 5px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Task Manager</h1>

        <div class="stats">
            <p>Tổng: <strong id="total">0</strong> | Hoàn thành: <strong id="completed">0</strong> | Còn lại: <strong id="remaining">0</strong></p>
        </div>

        <div class="add-task">
            <form onsubmit="handleAddTask(event)">
                <input type="text" id="taskInput" placeholder="Thêm nhiệm vụ mới..." required>
                <button type="submit">Thêm</button>
            </form>
        </div>

        <div class="tasks" id="tasksList"></div>
    </div>

    <script>
        const STORAGE_KEY = 'tasks_app';
        let tasks = [];

        function loadTasks() {
            const saved = localStorage.getItem(STORAGE_KEY);
            tasks = saved ? JSON.parse(saved) : [];
            displayTasks();
            updateStats();
        }

        function displayTasks() {
            const tasksList = document.getElementById('tasksList');
            tasksList.innerHTML = '';

            tasks.forEach((task, index) => {
                const taskEl = document.createElement('div');
                taskEl.className = `task ${task.completed ? 'completed' : ''}`;
                taskEl.innerHTML = `
                    <h3>${task.title}</h3>
                    <p>Tạo: ${new Date(task.created).toLocaleDateString('vi-VN')}</p>
                    <div class="task-status">
                        <button class="status-btn mark-done" onclick="toggleTask(${index})">
                            ${task.completed ? 'Hoàn tác' : 'Hoàn thành'}
                        </button>
                        <button class="status-btn delete-btn" onclick="deleteTask(${index})">Xóa</button>
                    </div>
                `;
                tasksList.appendChild(taskEl);
            });
        }

        function handleAddTask(e) {
            e.preventDefault();
            const input = document.getElementById('taskInput');
            const title = input.value.trim();

            if (!title) return;

            tasks.push({
                title,
                completed: false,
                created: new Date().toISOString()
            });

            localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
            input.value = '';
            displayTasks();
            updateStats();
        }

        function toggleTask(index) {
            tasks[index].completed = !tasks[index].completed;
            localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
            displayTasks();
            updateStats();
        }

        function deleteTask(index) {
            tasks.splice(index, 1);
            localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
            displayTasks();
            updateStats();
        }

        function updateStats() {
            const total = tasks.length;
            const completed = tasks.filter(t => t.completed).length;
            const remaining = total - completed;

            document.getElementById('total').textContent = total;
            document.getElementById('completed').textContent = completed;
            document.getElementById('remaining').textContent = remaining;
        }

        window.addEventListener('load', loadTasks);
    </script>
</body>
</html>
```

## 9.18. Tips & Tricks

### Tip 1: Intersection Observer cho Lazy Loading
```javascript
const images = document.querySelectorAll('img[data-src]');
const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
            observer.unobserve(img);
        }
    });
}, {
    rootMargin: '50px'
});

images.forEach(img => observer.observe(img));
```

### Tip 2: LocalStorage with Expiration
```javascript
function setItemWithExpiry(key, value, ttl) {
    const item = {
        value: value,
        expiry: Date.now() + (ttl * 1000)
    };
    localStorage.setItem(key, JSON.stringify(item));
}

function getItemWithExpiry(key) {
    const itemStr = localStorage.getItem(key);
    if (!itemStr) return null;

    const item = JSON.parse(itemStr);
    if (Date.now() > item.expiry) {
        localStorage.removeItem(key);
        return null;
    }

    return item.value;
}
```

### Tip 3: Drag and Drop File Validation
```javascript
function validateFile(file) {
    const MAX_SIZE = 5 * 1024 * 1024; // 5MB
    const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'application/pdf'];

    if (file.size > MAX_SIZE) {
        return { valid: false, error: 'File quá lớn' };
    }

    if (!ALLOWED_TYPES.includes(file.type)) {
        return { valid: false, error: 'Loại file không được hỗ trợ' };
    }

    return { valid: true };
}
```

### Tip 4: Copy to Clipboard with Fallback
```javascript
async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        console.log('Đã copy');
    } catch (err) {
        // Fallback for older browsers
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
    }
}
```

### Tip 5: Check Online/Offline Status
```javascript
if (navigator.onLine) {
    console.log('Online');
} else {
    console.log('Offline');
}

window.addEventListener('online', () => {
    console.log('Back online');
    // Sync data
});

window.addEventListener('offline', () => {
    console.log('Lost connection');
    // Save state to localStorage
});
```

### Tip 6: Vibration API Pattern
```javascript
// Short vibration
navigator.vibrate(200);

// Pattern: vibrate 100ms, pause 50ms, vibrate 100ms
navigator.vibrate([100, 50, 100]);

// Stop vibration
navigator.vibrate(0);
```

### Tip 7: Request Idle Callback for Non-Critical Tasks
```javascript
if ('requestIdleCallback' in window) {
    requestIdleCallback(() => {
        // Do non-critical work
        console.log('Running in idle time');
    });
} else {
    setTimeout(() => {
        console.log('Fallback: running after timeout');
    }, 1);
}
```

### Tip 8: Batch Storage Operations
```javascript
function batchSave(updates) {
    const current = JSON.parse(localStorage.getItem('app_state') || '{}');
    const updated = { ...current, ...updates };
    localStorage.setItem('app_state', JSON.stringify(updated));
}

// Usage
batchSave({
    user: 'john',
    theme: 'dark'
});
```

### Tip 9: Worker for Heavy Computation
```javascript
// main.js
const worker = new Worker('calculator.js');

// Send message to worker
worker.postMessage({ numbers: [1, 2, 3, 4, 5] });

// Receive result
worker.onmessage = (e) => {
    console.log('Sum:', e.data);
};

// worker.js
onmessage = (e) => {
    const sum = e.data.numbers.reduce((a, b) => a + b, 0);
    postMessage(sum);
};
```

### Tip 10: Detect Feature Support
```javascript
function supportedApis() {
    return {
        geolocation: 'geolocation' in navigator,
        webWorker: typeof(Worker) !== 'undefined',
        localStorage: typeof(Storage) !== 'undefined',
        webSocket: 'WebSocket' in window,
        notification: 'Notification' in window
    };
}

console.log(supportedApis());
```

## 9.19. Common Mistakes

### Mistake 1: Blocking Geolocation
```javascript
// ❌ SAI: No timeout
navigator.geolocation.getCurrentPosition(success, error);

// ✅ ĐÚNG: Set timeout
navigator.geolocation.getCurrentPosition(success, error, {
    timeout: 5000
});
```

### Mistake 2: Not Handling localStorage Quota
```javascript
// ❌ SAI: No error handling
localStorage.setItem('key', largeData);

// ✅ ĐÚNG: Handle QuotaExceededError
try {
    localStorage.setItem('key', largeData);
} catch (e) {
    if (e.name === 'QuotaExceededError') {
        console.error('localStorage full');
    }
}
```

### Mistake 3: WebSocket Without Reconnection
```javascript
// ❌ SAI: No reconnection logic
const socket = new WebSocket('ws://example.com');

// ✅ ĐÚNG: Auto-reconnect
class ReconnectingWebSocket {
    constructor(url) {
        this.url = url;
        this.socket = null;
        this.connect();
    }

    connect() {
        this.socket = new WebSocket(this.url);
        this.socket.onclose = () => {
            setTimeout(() => this.connect(), 3000);
        };
    }
}
```

### Mistake 4: Not Checking Feature Availability
```javascript
// ❌ SAI: No check
navigator.geolocation.getCurrentPosition(...);

// ✅ ĐÚNG: Check first
if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(...);
}
```

### Mistake 5: Memory Leaks with Observers
```javascript
// ❌ SAI: Observer never disconnected
const observer = new IntersectionObserver(callback);
observer.observe(element);

// ✅ ĐÚNG: Disconnect when done
observer.unobserve(element);
// or
observer.disconnect();
```

### Mistake 6: Infinite Drag Events
```javascript
// ❌ SAI: dragover fires every millisecond
dropzone.ondragover = () => {
    // Heavy processing
};

// ✅ ĐÚNG: Use preventDefault
dropzone.ondragover = (e) => {
    e.preventDefault();
    // Light processing
};
```

### Mistake 7: Storing Sensitive Data in localStorage
```javascript
// ❌ SAI: Storing passwords
localStorage.setItem('password', userPassword);

// ✅ ĐÚNG: Only store non-sensitive data
localStorage.setItem('theme', 'dark');
localStorage.setItem('language', 'vi');
```

### Mistake 8: Not Serializing Complex Objects
```javascript
// ❌ SAI: Object not serialized
const obj = { name: 'John', date: new Date() };
localStorage.setItem('user', obj);

// ✅ ĐÚNG: Serialize to JSON
localStorage.setItem('user', JSON.stringify(obj));
```

### Mistake 9: File API Without Size Check
```javascript
// ❌ SAI: No size validation
input.onchange = (e) => {
    const file = e.target.files[0];
    processFile(file);
};

// ✅ ĐÚNG: Check size first
input.onchange = (e) => {
    const file = e.target.files[0];
    if (file.size > 10 * 1024 * 1024) {
        alert('File too large');
        return;
    }
    processFile(file);
};
```

### Mistake 10: Not Handling Worker Errors
```javascript
// ❌ SAI: No error handling
const worker = new Worker('worker.js');

// ✅ ĐÚNG: Handle errors
worker.onerror = (error) => {
    console.error('Worker error:', error.message);
};
```

## 9.20. Troubleshooting Issues

### Issue 1: Geolocation Permission Denied
**Triệu chứng:** Luôn báo lỗi permission denied

**Nguyên nhân:**
- User từ chối quyền truy cập
- HTTPS không được sử dụng

**Giải pháp:**
```javascript
navigator.geolocation.getCurrentPosition(
    success,
    (error) => {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                console.log('User denied geolocation');
                break;
            case error.POSITION_UNAVAILABLE:
                console.log('Location unavailable');
                break;
            case error.TIMEOUT:
                console.log('Request timeout');
                break;
        }
    }
);
```

### Issue 2: LocalStorage Data Loss
**Triệu chứng:** Data biến mất sau khi reload

**Nguyên nhân:**
- Private browsing mode
- Storage quota exceeded
- Browser cleared data

**Giải pháp:**
```javascript
function safeSetItem(key, value) {
    try {
        localStorage.setItem(key, value);
        return true;
    } catch (e) {
        if (e.name === 'QuotaExceededError') {
            // Clear old data
            localStorage.clear();
            localStorage.setItem(key, value);
        }
        return false;
    }
}
```

### Issue 3: WebSocket Connection Hangs
**Triệu chứng:** WebSocket không kết nối

**Nguyên nhân:**
- Server không chạy
- Firewall chặn
- SSL issues

**Giải pháp:**
```javascript
const socket = new WebSocket('wss://example.com');

socket.addEventListener('open', () => {
    console.log('Connected');
});

socket.addEventListener('error', (event) => {
    console.error('WebSocket error:', event);
});

socket.addEventListener('close', () => {
    console.log('Disconnected');
});
```

### Issue 4: Drag and Drop Not Working
**Triệu chứng:** Drop event không trigger

**Nguyên nhân:**
- preventDefault() không được gọi
- Event listener không đúng

**Giải pháp:**
```javascript
const dropzone = document.getElementById('dropzone');

dropzone.addEventListener('dragover', (e) => {
    e.preventDefault(); // IMPORTANT
});

dropzone.addEventListener('dragleave', (e) => {
    e.preventDefault();
});

dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    const files = e.dataTransfer.files;
});
```

### Issue 5: Worker Script Not Found
**Triệu chứng:** Worker throws error

**Nguyên nhân:**
- Sai đường dẫn script
- CORS issues
- Script not deployed

**Giải pháp:**
```javascript
try {
    const worker = new Worker('/js/worker.js');
} catch (e) {
    console.error('Failed to create worker:', e);
    // Fallback to main thread
}
```

### Issue 6: Clipboard Permission Denied
**Triệu chứng:** Clipboard API không hoạt động

**Nguyên nhân:**
- User từ chối quyền
- Không phải HTTPS
- Browser không hỗ trợ

**Giải pháp:**
```javascript
async function copyText(text) {
    try {
        await navigator.clipboard.writeText(text);
    } catch (err) {
        if (err.name !== 'NotAllowedError') {
            console.error(err);
        }
        // Use fallback method
        fallbackCopy(text);
    }
}
```

### Issue 7: Notification Permission Issues
**Triệu chứng:** Notification không hiển thị

**Giải pháp:**
```javascript
if (Notification.permission === 'granted') {
    new Notification('Title', { body: 'Message' });
} else if (Notification.permission !== 'denied') {
    Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
            new Notification('Title');
        }
    });
}
```

### Issue 8: File Upload Cancelled
**Triệu chứng:** File input reset unexpectedly

**Giải pháp:**
```javascript
let selectedFile = null;

input.addEventListener('change', (e) => {
    selectedFile = e.target.files[0];
    if (selectedFile) {
        uploadFile(selectedFile);
    }
});
```

### Issue 9: SessionStorage vs LocalStorage Confusion
**Triệu chứng:** Data không persist

**Giải pháp:**
```javascript
// sessionStorage: cleared when tab closes
sessionStorage.setItem('tempData', data);

// localStorage: persists until manually cleared
localStorage.setItem('persistentData', data);
```

### Issue 10: History API State Issues
**Triệu chứng:** State data lost on navigation

**Giải pháp:**
```javascript
// Save complex state
const state = { page: 1, filter: 'active' };
window.history.pushState(state, '', '/page1');

// Listen for state changes
window.addEventListener('popstate', (e) => {
    console.log('State:', e.state);
});
```

## 9.21. Advanced Topics

### Topic 1: Service Worker for Offline Support
```javascript
// Service Worker Registration
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').then(reg => {
        console.log('Service Worker registered');
    });
}

// sw.js
const CACHE_NAME = 'v1';
const URLS_TO_CACHE = ['/', '/index.html', '/style.css'];

self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(URLS_TO_CACHE);
        })
    );
});

self.addEventListener('fetch', (e) => {
    e.respondWith(
        caches.match(e.request).then(response => {
            return response || fetch(e.request);
        })
    );
});
```

### Topic 2: IndexedDB for Complex Data
```javascript
function openDatabase() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open('myDB', 1);

        request.onerror = () => reject(request.error);
        request.onsuccess = () => resolve(request.result);

        request.onupgradeneeded = (e) => {
            const db = e.target.result;
            if (!db.objectStoreNames.contains('users')) {
                db.createObjectStore('users', { keyPath: 'id' });
            }
        };
    });
}

// Save data
async function saveUser(user) {
    const db = await openDatabase();
    const tx = db.transaction('users', 'readwrite');
    tx.objectStore('users').add(user);
}
```

### Topic 3: WebRTC for Video Streaming
```javascript
async function startVideoCall() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: true
        });

        const videoElement = document.getElementById('video');
        videoElement.srcObject = stream;
    } catch (err) {
        console.error('Failed to get media:', err);
    }
}
```

### Topic 4: Intersection Observer Patterns
```javascript
// Infinite scroll pattern
const observer = new IntersectionObserver(
    entries => {
        if (entries[0].isIntersecting) {
            loadMoreItems();
        }
    },
    { threshold: 0.1 }
);

const sentinel = document.getElementById('sentinel');
observer.observe(sentinel);
```

### Topic 5: Web Audio API Playback
```javascript
async function playWithEffects(audioFile) {
    const context = new (window.AudioContext || window.webkitAudioContext)();
    const response = await fetch(audioFile);
    const buffer = await response.arrayBuffer();
    const decoded = await context.decodeAudioData(buffer);

    const source = context.createBufferSource();
    source.buffer = decoded;

    const filter = context.createBiquadFilter();
    source.connect(filter);
    filter.connect(context.destination);

    source.start(0);
}
```

## 9.22. Bài tập thực hành

### Bài 1 (Dễ): Simple Location Display
Tạo app hiển thị vị trí hiện tại (latitude, longitude, accuracy)

### Bài 2 (Dễ): LocalStorage Todo List
Tạo todo list đơn giản lưu data bằng localStorage

### Bài 3 (Dễ): File Size Validator
Tạo form upload file với validation kích thước và loại file

### Bài 4 (Dễ): Online/Offline Indicator
Tạo indicator hiển thị trạng thái online/offline của browser

### Bài 5 (Trung bình): Weather App
Tạo weather app sử dụng Geolocation API (mock data)

### Bài 6 (Trung bình): Image Gallery with Lazy Loading
Tạo gallery ảnh sử dụng Intersection Observer để lazy load

### Bài 7 (Trung bình): Notes App with Rich Features
Tạo notes app với:
- Thêm/xóa/sửa ghi chú
- LocalStorage persistence
- Search functionality
- Categories

### Bài 8 (Trung bình): Drag and Drop Task Manager
Tạo task manager với:
- Drag and drop tasks
- Multiple columns (To Do, In Progress, Done)
- LocalStorage sync
- Task details

### Bài 9 (Trung bình): File Upload with Progress
Tạo file uploader với:
- Drag & drop
- Progress bar
- Multiple files
- File preview

### Bài 10 (Khó): Chat Application
Tạo chat app mock với:
- Real-time message display
- User list
- Typing indicators
- Message history (localStorage)

### Bài 11 (Khó): Service Worker & Offline Support
Tạo website với:
- Service Worker registration
- Offline caching
- Background sync mock
- Update notifications

### Bài 12 (Khó): Advanced Analytics Dashboard
Tạo dashboard với:
- IndexedDB data storage
- Real-time data visualization
- Export/import functionality
- Data persistence
- Performance monitoring

---

**Kết luận:** HTML5 APIs cung cấp nhiều tính năng mạnh mẽ cho web applications. Hiểu và sử dụng đúng các APIs này giúp tạo ra những ứng dụng web hiện đại, nhanh, và user-friendly với khả năng hoạt động offline.
