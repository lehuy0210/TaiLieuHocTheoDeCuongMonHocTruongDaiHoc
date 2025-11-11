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

## 9.17. Bài tập thực hành

### Bài 1: Location Tracker
Tạo app hiển thị vị trí hiện tại trên map

### Bài 2: Drag and Drop File Upload
Tạo file uploader với drag & drop và preview

### Bài 3: Notes App với localStorage
Tạo app ghi chú lưu offline

### Bài 4: Real-time Chat với WebSocket
Tạo chat app đơn giản

---

**Kết luận:** HTML5 APIs cung cấp nhiều tính năng mạnh mẽ cho web applications. Hiểu và sử dụng đúng các APIs này giúp tạo ra những ứng dụng web hiện đại và user-friendly.
