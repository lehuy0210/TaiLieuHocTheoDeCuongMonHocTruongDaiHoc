# CHƯƠNG 11: STORAGE VÀ OFFLINE

## 11.1. Web Storage API

### 11.1.1. localStorage

**Lưu trữ vĩnh viễn:**
```javascript
// Set item
localStorage.setItem('username', 'john_doe');
localStorage.setItem('theme', 'dark');

// Get item
const username = localStorage.getItem('username');

// Remove item
localStorage.removeItem('username');

// Clear all
localStorage.clear();

// Check existence
if (localStorage.getItem('username')) {
    console.log('Username exists');
}

// Get all keys
for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    console.log(key, localStorage.getItem(key));
}
```

**Lưu objects:**
```javascript
const user = {
    name: 'John Doe',
    email: 'john@example.com',
    age: 30
};

// Save object
localStorage.setItem('user', JSON.stringify(user));

// Get object
const savedUser = JSON.parse(localStorage.getItem('user'));
console.log(savedUser.name);
```

**Storage size:**
```javascript
// Thường ~5-10MB tùy browser
function getStorageSize() {
    let total = 0;
    for (let key in localStorage) {
        if (localStorage.hasOwnProperty(key)) {
            total += localStorage[key].length + key.length;
        }
    }
    return total;
}
```

### 11.1.2. sessionStorage

**Lưu trữ trong session:**
```javascript
// Chỉ tồn tại cho đến khi tab/window đóng
sessionStorage.setItem('temp_data', 'value');
const tempData = sessionStorage.getItem('temp_data');
sessionStorage.removeItem('temp_data');
sessionStorage.clear();
```

### 11.1.3. Storage Events

```javascript
// Lắng nghe changes từ tab/window khác
window.addEventListener('storage', (e) => {
    console.log('Key:', e.key);
    console.log('Old Value:', e.oldValue);
    console.log('New Value:', e.newValue);
    console.log('URL:', e.url);
    console.log('Storage Area:', e.storageArea);
});
```

## 11.2. IndexedDB

### 11.2.1. Open Database

```javascript
let db;

const request = indexedDB.open('MyDatabase', 1);

request.onerror = (event) => {
    console.error('Database error:', event.target.error);
};

request.onsuccess = (event) => {
    db = event.target.result;
    console.log('Database opened successfully');
};

request.onupgradeneeded = (event) => {
    db = event.target.result;

    // Create object store
    const objectStore = db.createObjectStore('users', {
        keyPath: 'id',
        autoIncrement: true
    });

    // Create indexes
    objectStore.createIndex('email', 'email', { unique: true });
    objectStore.createIndex('name', 'name', { unique: false });
};
```

### 11.2.2. Add Data

```javascript
function addUser(user) {
    const transaction = db.transaction(['users'], 'readwrite');
    const objectStore = transaction.objectStore('users');

    const request = objectStore.add(user);

    request.onsuccess = () => {
        console.log('User added');
    };

    request.onerror = () => {
        console.error('Error adding user');
    };
}

addUser({ name: 'John Doe', email: 'john@example.com', age: 30 });
```

### 11.2.3. Get Data

```javascript
function getUser(id) {
    const transaction = db.transaction(['users'], 'readonly');
    const objectStore = transaction.objectStore('users');
    const request = objectStore.get(id);

    request.onsuccess = (event) => {
        const user = event.target.result;
        console.log('User:', user);
    };
}

// Get by index
function getUserByEmail(email) {
    const transaction = db.transaction(['users'], 'readonly');
    const objectStore = transaction.objectStore('users');
    const index = objectStore.index('email');
    const request = index.get(email);

    request.onsuccess = (event) => {
        console.log('User:', event.target.result);
    };
}
```

### 11.2.4. Update Data

```javascript
function updateUser(id, updates) {
    const transaction = db.transaction(['users'], 'readwrite');
    const objectStore = transaction.objectStore('users');

    const request = objectStore.get(id);

    request.onsuccess = (event) => {
        const user = event.target.result;
        Object.assign(user, updates);

        const updateRequest = objectStore.put(user);
        updateRequest.onsuccess = () => {
            console.log('User updated');
        };
    };
}
```

### 11.2.5. Delete Data

```javascript
function deleteUser(id) {
    const transaction = db.transaction(['users'], 'readwrite');
    const objectStore = transaction.objectStore('users');
    const request = objectStore.delete(id);

    request.onsuccess = () => {
        console.log('User deleted');
    };
}

// Clear all
function clearUsers() {
    const transaction = db.transaction(['users'], 'readwrite');
    const objectStore = transaction.objectStore('users');
    const request = objectStore.clear();

    request.onsuccess = () => {
        console.log('All users deleted');
    };
}
```

### 11.2.6. Query Data

```javascript
function getAllUsers() {
    const transaction = db.transaction(['users'], 'readonly');
    const objectStore = transaction.objectStore('users');
    const request = objectStore.getAll();

    request.onsuccess = (event) => {
        console.log('All users:', event.target.result);
    };
}

// Using cursor
function iterateUsers() {
    const transaction = db.transaction(['users'], 'readonly');
    const objectStore = transaction.objectStore('users');
    const request = objectStore.openCursor();

    request.onsuccess = (event) => {
        const cursor = event.target.result;
        if (cursor) {
            console.log('User:', cursor.value);
            cursor.continue();
        }
    };
}
```

## 11.3. Cookies

### 11.3.1. Set Cookie

```javascript
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

setCookie('username', 'john', 30);
```

### 11.3.2. Get Cookie

```javascript
function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

const username = getCookie('username');
```

### 11.3.3. Delete Cookie

```javascript
function deleteCookie(name) {
    document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}
```

## 11.4. Service Workers

### 11.4.1. Register Service Worker

```javascript
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
        .then(registration => {
            console.log('Service Worker registered:', registration);
        })
        .catch(error => {
            console.error('Service Worker registration failed:', error);
        });
}
```

### 11.4.2. Service Worker File (sw.js)

```javascript
const CACHE_NAME = 'my-cache-v1';
const urlsToCache = [
    '/',
    '/styles/main.css',
    '/scripts/main.js',
    '/images/logo.png'
];

// Install event
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Cache opened');
                return cache.addAll(urlsToCache);
            })
    );
});

// Fetch event
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Cache hit - return response
                if (response) {
                    return response;
                }

                // Clone request
                const fetchRequest = event.request.clone();

                return fetch(fetchRequest).then(response => {
                    // Check valid response
                    if (!response || response.status !== 200 || response.type !== 'basic') {
                        return response;
                    }

                    // Clone response
                    const responseToCache = response.clone();

                    caches.open(CACHE_NAME)
                        .then(cache => {
                            cache.put(event.request, responseToCache);
                        });

                    return response;
                });
            })
    );
});

// Activate event
self.addEventListener('activate', (event) => {
    const cacheWhitelist = [CACHE_NAME];

    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (!cacheWhitelist.includes(cacheName)) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
```

### 11.4.3. Update Service Worker

```javascript
// Check for updates
navigator.serviceWorker.register('/sw.js').then(reg => {
    reg.addEventListener('updatefound', () => {
        const newWorker = reg.installing;

        newWorker.addEventListener('statechange', () => {
            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                // New service worker available
                console.log('New content available, please refresh');
            }
        });
    });
});

// Skip waiting
self.addEventListener('install', event => {
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    event.waitUntil(clients.claim());
});
```

## 11.5. Cache API

### 11.5.1. Basic Caching

```javascript
// Open cache
caches.open('my-cache').then(cache => {
    // Add to cache
    cache.add('/page.html');
    cache.addAll(['/page1.html', '/page2.html']);

    // Put in cache
    cache.put(request, response);

    // Match
    cache.match('/page.html').then(response => {
        if (response) {
            return response;
        }
    });

    // Delete
    cache.delete('/page.html');

    // Get all keys
    cache.keys().then(requests => {
        requests.forEach(request => {
            console.log(request.url);
        });
    });
});

// Get all caches
caches.keys().then(cacheNames => {
    console.log('Caches:', cacheNames);
});

// Delete cache
caches.delete('old-cache');
```

## 11.6. Application Cache (Deprecated)

**Note:** Application Cache (AppCache) đã deprecated, nên dùng Service Workers

## 11.7. Offline Detection

```javascript
// Check online status
if (navigator.onLine) {
    console.log('Online');
} else {
    console.log('Offline');
}

// Listen for online/offline events
window.addEventListener('online', () => {
    console.log('Connection restored');
    // Sync data
});

window.addEventListener('offline', () => {
    console.log('Connection lost');
    // Save data locally
});
```

## 11.8. Background Sync

```javascript
// Register sync
if ('serviceWorker' in navigator && 'SyncManager' in window) {
    navigator.serviceWorker.ready.then(registration => {
        return registration.sync.register('sync-data');
    });
}

// In service worker (sw.js)
self.addEventListener('sync', event => {
    if (event.tag === 'sync-data') {
        event.waitUntil(
            syncData() // Your sync function
        );
    }
});

function syncData() {
    return fetch('/api/sync', {
        method: 'POST',
        body: JSON.stringify(dataToSync)
    });
}
```

## 11.9. Use Cases Thực Tế

### Use Case 1: Complete Offline Note App

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Offline Note App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        .header {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .status {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            margin-right: 10px;
        }
        .status.online {
            background: #4CAF50;
            color: white;
        }
        .status.offline {
            background: #f44336;
            color: white;
        }
        .input-group {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        input[type="text"] {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }
        button {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover {
            background: #5568d3;
        }
        .notes-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }
        .note {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            position: relative;
            transition: transform 0.2s;
        }
        .note:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .note-title {
            font-weight: bold;
            margin-bottom: 10px;
            word-break: break-word;
        }
        .note-content {
            color: #666;
            font-size: 13px;
            word-break: break-word;
            white-space: pre-wrap;
        }
        .note-date {
            font-size: 11px;
            color: #aaa;
            margin-top: 10px;
        }
        .note-delete {
            position: absolute;
            top: 10px;
            right: 10px;
            background: #f44336;
            border: none;
            color: white;
            width: 25px;
            height: 25px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 16px;
        }
        .empty {
            text-align: center;
            color: white;
            padding: 40px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <span class="status online" id="status">Online</span>
                <span id="syncStatus"></span>
            </div>
            <h1>Offline Note App</h1>
            <div class="input-group">
                <input type="text" id="noteTitle" placeholder="Tiêu đề ghi chú...">
                <button onclick="addNote()">Thêm ghi chú</button>
                <button onclick="clearAll()" style="background: #f44336;">Xóa tất cả</button>
            </div>
        </div>

        <div id="notesList" class="notes-container">
            <div class="empty">Chưa có ghi chú nào. Thêm ghi chú mới!</div>
        </div>
    </div>

    <script>
        class OfflineNoteApp {
            constructor() {
                this.notes = this.loadNotes();
                this.setupServiceWorker();
                this.setupOfflineDetection();
                this.render();
            }

            loadNotes() {
                const saved = localStorage.getItem('notes');
                return saved ? JSON.parse(saved) : [];
            }

            saveNotes() {
                localStorage.setItem('notes', JSON.stringify(this.notes));
            }

            addNote(title) {
                if (!title.trim()) return alert('Vui lòng nhập tiêu đề!');

                const note = {
                    id: Date.now(),
                    title: title,
                    content: '',
                    date: new Date().toLocaleString('vi-VN')
                };

                this.notes.unshift(note);
                this.saveNotes();
                this.render();
                this.syncToServer();
            }

            deleteNote(id) {
                this.notes = this.notes.filter(note => note.id !== id);
                this.saveNotes();
                this.render();
            }

            clearAll() {
                if (confirm('Xóa tất cả ghi chú?')) {
                    this.notes = [];
                    this.saveNotes();
                    this.render();
                }
            }

            render() {
                const container = document.getElementById('notesList');
                if (this.notes.length === 0) {
                    container.innerHTML = '<div class="empty">Chưa có ghi chú nào. Thêm ghi chú mới!</div>';
                    return;
                }

                container.innerHTML = this.notes.map(note => `
                    <div class="note" onclick="editNote(${note.id})">
                        <button class="note-delete" onclick="deleteNote(${note.id}); event.stopPropagation();">×</button>
                        <div class="note-title">${this.escapeHtml(note.title)}</div>
                        <div class="note-content">${this.escapeHtml(note.content)}</div>
                        <div class="note-date">${note.date}</div>
                    </div>
                `).join('');
            }

            escapeHtml(text) {
                const div = document.createElement('div');
                div.textContent = text;
                return div.innerHTML;
            }

            setupOfflineDetection() {
                window.addEventListener('online', () => {
                    document.getElementById('status').textContent = 'Online';
                    document.getElementById('status').className = 'status online';
                    this.syncToServer();
                });

                window.addEventListener('offline', () => {
                    document.getElementById('status').textContent = 'Offline';
                    document.getElementById('status').className = 'status offline';
                });

                // Set initial status
                if (!navigator.onLine) {
                    document.getElementById('status').textContent = 'Offline';
                    document.getElementById('status').className = 'status offline';
                }
            }

            setupServiceWorker() {
                if ('serviceWorker' in navigator) {
                    navigator.serviceWorker.register('/sw.js').catch(() => {});
                }
            }

            syncToServer() {
                if (!navigator.onLine) return;

                const syncData = localStorage.getItem('sync_pending');
                if (syncData) {
                    fetch('/api/sync-notes', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: syncData
                    })
                    .then(r => r.json())
                    .then(data => {
                        localStorage.removeItem('sync_pending');
                        document.getElementById('syncStatus').textContent = 'Đã đồng bộ!';
                        setTimeout(() => {
                            document.getElementById('syncStatus').textContent = '';
                        }, 3000);
                    })
                    .catch(() => {});
                }
            }
        }

        let app;
        window.addEventListener('DOMContentLoaded', () => {
            app = new OfflineNoteApp();
        });

        function addNote() {
            const title = document.getElementById('noteTitle').value;
            app.addNote(title);
            document.getElementById('noteTitle').value = '';
        }

        function deleteNote(id) {
            event.preventDefault();
            event.stopPropagation();
            if (confirm('Xóa ghi chú này?')) {
                app.deleteNote(id);
            }
        }

        function clearAll() {
            app.clearAll();
        }

        function editNote(id) {
            const note = app.notes.find(n => n.id === id);
            if (note) {
                const content = prompt('Nội dung ghi chú:', note.content);
                if (content !== null) {
                    note.content = content;
                    app.saveNotes();
                    app.render();
                }
            }
        }
    </script>
</body>
</html>
```

### Use Case 2: Shopping Cart Persistent with IndexedDB

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Shopping Cart with IndexedDB</title>
    <style>
        body {
            font-family: Arial;
            background: #f5f5f5;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .product {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .product-name {
            font-weight: bold;
            margin-bottom: 10px;
        }
        .product-price {
            color: #f44336;
            font-size: 18px;
            margin-bottom: 10px;
        }
        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        .cart-section {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .cart-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #ddd;
        }
        .cart-total {
            font-weight: bold;
            font-size: 18px;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 2px solid #f44336;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shop</h1>

        <div class="products" id="products"></div>

        <div class="cart-section">
            <h2>Giỏ hàng</h2>
            <div id="cartItems"></div>
            <div class="cart-total">
                Tổng: <span id="cartTotal">0đ</span>
                <button onclick="checkout()" style="width: auto; margin-left: 20px;">Thanh toán</button>
            </div>
        </div>
    </div>

    <script>
        let db;

        const PRODUCTS = [
            { id: 1, name: 'Laptop', price: 15000000 },
            { id: 2, name: 'Mouse', price: 300000 },
            { id: 3, name: 'Keyboard', price: 800000 },
            { id: 4, name: 'Monitor', price: 3000000 }
        ];

        class ShoppingCart {
            constructor() {
                this.initDB();
            }

            initDB() {
                const request = indexedDB.open('ShopDB', 1);

                request.onerror = () => console.error('DB error');

                request.onsuccess = (e) => {
                    db = e.target.result;
                    this.renderCart();
                };

                request.onupgradeneeded = (e) => {
                    db = e.target.result;
                    if (!db.objectStoreNames.contains('cart')) {
                        const store = db.createObjectStore('cart', { keyPath: 'id' });
                        store.createIndex('product_id', 'product_id', { unique: false });
                    }
                };
            }

            addToCart(productId, quantity = 1) {
                const transaction = db.transaction(['cart'], 'readwrite');
                const store = transaction.objectStore('cart');

                const request = store.get(productId);

                request.onsuccess = () => {
                    const item = request.result || { id: productId, product_id: productId, quantity: 0 };
                    item.quantity += quantity;

                    if (item.quantity <= 0) {
                        store.delete(productId);
                    } else {
                        store.put(item);
                    }

                    this.renderCart();
                };
            }

            renderCart() {
                const transaction = db.transaction(['cart'], 'readonly');
                const store = transaction.objectStore('cart');
                const request = store.getAll();

                request.onsuccess = () => {
                    const items = request.result;
                    let html = '';
                    let total = 0;

                    items.forEach(item => {
                        const product = PRODUCTS.find(p => p.id === item.product_id);
                        const subtotal = product.price * item.quantity;
                        total += subtotal;

                        html += `
                            <div class="cart-item">
                                <span>${product.name} x${item.quantity}</span>
                                <span>${(subtotal).toLocaleString()}đ</span>
                                <button onclick="cart.addToCart(${product.id}, -1)" style="width: 50px;">-</button>
                            </div>
                        `;
                    });

                    document.getElementById('cartItems').innerHTML = html || '<p>Giỏ hàng trống</p>';
                    document.getElementById('cartTotal').textContent = total.toLocaleString() + 'đ';
                };
            }

            checkout() {
                const transaction = db.transaction(['cart'], 'readwrite');
                const store = transaction.objectStore('cart');
                store.clear();
                alert('Thanh toán thành công!');
                this.renderCart();
            }
        }

        const cart = new ShoppingCart();

        window.addEventListener('DOMContentLoaded', () => {
            document.getElementById('products').innerHTML = PRODUCTS.map(p => `
                <div class="product">
                    <div class="product-name">${p.name}</div>
                    <div class="product-price">${p.price.toLocaleString()}đ</div>
                    <button onclick="cart.addToCart(${p.id})">Thêm vào giỏ</button>
                </div>
            `).join('');
        });
    </script>
</body>
</html>
```

### Use Case 3: Form Auto-Save with localStorage

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Auto-Save Form</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 50px auto; }
        .form-group { margin: 20px 0; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: Arial;
        }
        textarea { resize: vertical; min-height: 100px; }
        button {
            background: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-right: 10px;
        }
        .status {
            margin-top: 10px;
            padding: 10px;
            border-radius: 4px;
            display: none;
        }
        .status.saved {
            background: #c8e6c9;
            color: #2e7d32;
            display: block;
        }
    </style>
</head>
<body>
    <h1>Biểu mẫu Auto-Save</h1>

    <form id="myForm">
        <div class="form-group">
            <label for="name">Họ tên:</label>
            <input type="text" id="name" name="name" required>
        </div>

        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>

        <div class="form-group">
            <label for="message">Tin nhắn:</label>
            <textarea id="message" name="message"></textarea>
        </div>

        <div class="form-group">
            <label for="category">Danh mục:</label>
            <select id="category" name="category">
                <option value="">-- Chọn --</option>
                <option value="tech">Công nghệ</option>
                <option value="business">Kinh doanh</option>
                <option value="other">Khác</option>
            </select>
        </div>

        <div>
            <button type="submit">Gửi</button>
            <button type="button" onclick="clearForm()">Xóa</button>
        </div>

        <div id="status" class="status">Đã lưu dự thảo!</div>
    </form>

    <script>
        const form = document.getElementById('myForm');
        const inputs = form.querySelectorAll('input, textarea, select');
        const statusDiv = document.getElementById('status');

        // Load saved data
        window.addEventListener('DOMContentLoaded', () => {
            inputs.forEach(input => {
                const saved = localStorage.getItem(`form_${input.name}`);
                if (saved) {
                    input.value = saved;
                }

                // Auto-save on input
                input.addEventListener('input', () => {
                    localStorage.setItem(`form_${input.name}`, input.value);
                    showStatus('Đã lưu dự thảo!');
                });

                input.addEventListener('change', () => {
                    localStorage.setItem(`form_${input.name}`, input.value);
                });
            });
        });

        function showStatus(message) {
            statusDiv.textContent = message;
            statusDiv.classList.add('saved');
            setTimeout(() => {
                statusDiv.classList.remove('saved');
            }, 2000);
        }

        function clearForm() {
            if (confirm('Xóa tất cả dữ liệu đã lưu?')) {
                form.reset();
                inputs.forEach(input => {
                    localStorage.removeItem(`form_${input.name}`);
                });
                showStatus('Đã xóa dữ liệu!');
            }
        }

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            // Submit to server
            alert('Form submitted!');

            // Clear saved data
            inputs.forEach(input => {
                localStorage.removeItem(`form_${input.name}`);
            });
            form.reset();
            showStatus('Gửi thành công! Dự thảo đã xóa.');
        });
    </script>
</body>
</html>
```

### Use Case 4: Real-time Sync Across Tabs

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Multi-Tab Sync</title>
    <style>
        body {
            font-family: Arial;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
        }
        .todo-item {
            background: #f5f5f5;
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        input { padding: 10px; width: 80%; border: 1px solid #ddd; }
        button { padding: 10px 15px; background: #4CAF50; color: white; border: none; }
        .info { background: #e3f2fd; padding: 10px; margin-bottom: 20px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="info">
        <p>Thay đổi dữ liệu ở tab này, các tab khác sẽ tự cập nhật!</p>
        <p>Tâb hiện tại: <strong id="tabInfo"></strong></p>
    </div>

    <input type="text" id="newTodo" placeholder="Thêm công việc mới...">
    <button onclick="addTodo()">Thêm</button>

    <div id="todoList"></div>

    <script>
        const TAB_ID = Date.now();
        let todos = [];

        // Initialize
        window.addEventListener('DOMContentLoaded', () => {
            document.getElementById('tabInfo').textContent = `Tab #${TAB_ID}`;
            loadTodos();
        });

        function loadTodos() {
            const saved = localStorage.getItem('todos');
            todos = saved ? JSON.parse(saved) : [];
            render();
        }

        function saveTodos() {
            localStorage.setItem('todos', JSON.stringify(todos));
        }

        function addTodo() {
            const input = document.getElementById('newTodo');
            if (!input.value.trim()) return;

            todos.push({
                id: Date.now(),
                text: input.value,
                done: false,
                createdBy: TAB_ID
            });

            saveTodos();
            input.value = '';
            render();
            broadcastChange('add');
        }

        function deleteTodo(id) {
            todos = todos.filter(t => t.id !== id);
            saveTodos();
            render();
            broadcastChange('delete');
        }

        function toggleTodo(id) {
            const todo = todos.find(t => t.id === id);
            if (todo) todo.done = !todo.done;
            saveTodos();
            render();
            broadcastChange('toggle');
        }

        function render() {
            const list = document.getElementById('todoList');
            list.innerHTML = todos.map(todo => `
                <div class="todo-item" style="${todo.done ? 'opacity: 0.5;' : ''}">
                    <span onclick="toggleTodo(${todo.id})" style="cursor: pointer; flex: 1;">
                        ${todo.done ? '✓ ' : ''}${todo.text}
                    </span>
                    <button onclick="deleteTodo(${todo.id})">Xóa</button>
                </div>
            `).join('');
        }

        // Listen for changes from other tabs
        window.addEventListener('storage', (e) => {
            if (e.key === 'todos') {
                console.log('Received update from Tab #' + e.newValue);
                loadTodos();
            }
        });

        function broadcastChange(action) {
            // Trigger storage event in other tabs
            // This is done automatically by setting localStorage
        }
    </script>
</body>
</html>
```

### Use Case 5: Progressive Sync with Service Worker

```javascript
// sw.js - Service Worker with Background Sync
const CACHE_NAME = 'v1';
const DB_NAME = 'app-db';

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll([
                '/',
                '/styles.css',
                '/app.js'
            ]);
        })
    );
    self.skipWaiting();
});

self.addEventListener('fetch', event => {
    // For API calls, use network first, fallback to cache
    if (event.request.url.includes('/api/')) {
        event.respondWith(
            fetch(event.request)
                .then(response => {
                    // Cache successful responses
                    if (response.status === 200) {
                        const responseClone = response.clone();
                        caches.open(CACHE_NAME).then(cache => {
                            cache.put(event.request, responseClone);
                        });
                    }
                    return response;
                })
                .catch(() => {
                    // Fallback to cache or offline page
                    return caches.match(event.request)
                        .then(response => response || new Response('Offline'));
                })
        );
    } else {
        // For other resources, use cache first
        event.respondWith(
            caches.match(event.request)
                .then(response => response || fetch(event.request))
        );
    }
});

// Background Sync
self.addEventListener('sync', event => {
    if (event.tag === 'sync-data') {
        event.waitUntil(syncPendingData());
    }
});

async function syncPendingData() {
    const db = await openDB();
    const pending = await getAllPendingItems(db);

    for (const item of pending) {
        try {
            const response = await fetch(item.url, {
                method: item.method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(item.data)
            });

            if (response.ok) {
                await deletePendingItem(db, item.id);
            }
        } catch (error) {
            console.error('Sync failed:', error);
            throw error; // Retry later
        }
    }
}

function openDB() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open(DB_NAME, 1);
        request.onsuccess = () => resolve(request.result);
        request.onerror = () => reject(request.error);
    });
}

// Main app code
class OfflineApp {
    async submitForm(data) {
        try {
            const response = await fetch('/api/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                return await response.json();
            }
        } catch (error) {
            // Save to pending and schedule sync
            await this.savePending('/api/submit', 'POST', data);
            await this.registerSync();
        }
    }

    async savePending(url, method, data) {
        const db = await openDB();
        const transaction = db.transaction(['pending'], 'readwrite');
        const store = transaction.objectStore('pending');

        return new Promise((resolve, reject) => {
            const request = store.add({
                url, method, data,
                timestamp: Date.now()
            });
            request.onsuccess = () => resolve();
            request.onerror = () => reject(request.error);
        });
    }

    async registerSync() {
        if ('serviceWorker' in navigator && 'SyncManager' in window) {
            const registration = await navigator.serviceWorker.ready;
            await registration.sync.register('sync-data');
        }
    }
}
```

## 11.10. Practical Examples

### 11.10.1. Offline-First App

```javascript
// Save data for offline use
function saveOfflineData(data) {
    localStorage.setItem('offline-data', JSON.stringify(data));
}

// Load data
function loadData() {
    if (navigator.onLine) {
        // Fetch from server
        return fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                saveOfflineData(data);
                return data;
            });
    } else {
        // Load from offline storage
        const offlineData = localStorage.getItem('offline-data');
        return Promise.resolve(JSON.parse(offlineData));
    }
}
```

### 11.9.2. Form Data Persistence

```javascript
const form = document.getElementById('myForm');
const inputs = form.querySelectorAll('input, textarea');

// Auto-save on input
inputs.forEach(input => {
    const savedValue = localStorage.getItem(`form-${input.name}`);
    if (savedValue) {
        input.value = savedValue;
    }

    input.addEventListener('input', (e) => {
        localStorage.setItem(`form-${e.target.name}`, e.target.value);
    });
});

// Clear on successful submit
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Submit form
    submitForm().then(() => {
        inputs.forEach(input => {
            localStorage.removeItem(`form-${input.name}`);
        });
    });
});
```

### 11.9.3. Shopping Cart với localStorage

```javascript
class ShoppingCart {
    constructor() {
        this.items = this.load();
    }

    load() {
        const cart = localStorage.getItem('shopping-cart');
        return cart ? JSON.parse(cart) : [];
    }

    save() {
        localStorage.setItem('shopping-cart', JSON.stringify(this.items));
    }

    add(item) {
        this.items.push(item);
        this.save();
    }

    remove(itemId) {
        this.items = this.items.filter(item => item.id !== itemId);
        this.save();
    }

    clear() {
        this.items = [];
        localStorage.removeItem('shopping-cart');
    }

    getTotal() {
        return this.items.reduce((total, item) => total + item.price, 0);
    }
}

const cart = new ShoppingCart();
```

## 11.10. Storage Comparison

| Feature | Cookies | localStorage | sessionStorage | IndexedDB |
|---------|---------|--------------|----------------|-----------|
| Capacity | ~4KB | ~5-10MB | ~5-10MB | ~50MB+ |
| Expiration | Set expiration | Never | Session | Never |
| Sent to server | Yes | No | No | No |
| Accessibility | All windows | All windows | Same tab | All windows |
| API | Simple | Simple | Simple | Complex |
| Data type | String | String | String | Any |
| Use case | Session data | Preferences | Temporary | Large data |

## 11.11. Tips & Tricks

### Tip 1: Wrap localStorage với try-catch cho Cross-Origin Issues
```javascript
function safeSetItem(key, value) {
    try {
        localStorage.setItem(key, value);
        return true;
    } catch (e) {
        if (e.name === 'QuotaExceededError') {
            console.error('Storage quota exceeded');
        }
        return false;
    }
}
```

### Tip 2: Auto-Expire localStorage Items
```javascript
function setWithExpiry(key, value, expiryTime) {
    const item = {
        value: value,
        expiry: Date.now() + expiryTime
    };
    localStorage.setItem(key, JSON.stringify(item));
}

function getWithExpiry(key) {
    const item = localStorage.getItem(key);
    if (!item) return null;

    const data = JSON.parse(item);
    if (Date.now() > data.expiry) {
        localStorage.removeItem(key);
        return null;
    }
    return data.value;
}
```

### Tip 3: Monitor Storage Space
```javascript
async function getStorageQuota() {
    if (navigator.storage && navigator.storage.estimate) {
        const estimate = await navigator.storage.estimate();
        const percentUsed = (estimate.usage / estimate.quota) * 100;
        console.log(`Storage: ${percentUsed.toFixed(2)}% used`);
        return {
            used: estimate.usage,
            quota: estimate.quota,
            available: estimate.quota - estimate.usage
        };
    }
}
```

### Tip 4: Efficient Batch IndexedDB Operations
```javascript
async function batchInsert(storeName, items) {
    return new Promise((resolve, reject) => {
        const transaction = db.transaction([storeName], 'readwrite');
        const store = transaction.objectStore(storeName);

        items.forEach(item => {
            store.add(item);
        });

        transaction.oncomplete = () => resolve();
        transaction.onerror = () => reject(transaction.error);
    });
}
```

### Tip 5: Storage Observer Pattern
```javascript
class StorageManager {
    constructor() {
        this.listeners = {};
    }

    subscribe(key, callback) {
        if (!this.listeners[key]) {
            this.listeners[key] = [];
        }
        this.listeners[key].push(callback);
    }

    set(key, value) {
        const oldValue = localStorage.getItem(key);
        localStorage.setItem(key, JSON.stringify(value));

        if (this.listeners[key]) {
            this.listeners[key].forEach(cb => {
                cb(value, oldValue);
            });
        }
    }

    get(key) {
        const value = localStorage.getItem(key);
        return value ? JSON.parse(value) : null;
    }
}
```

### Tip 6: Service Worker Caching Strategies
```javascript
// Network First Strategy
self.addEventListener('fetch', event => {
    event.respondWith(
        fetch(event.request)
            .then(response => {
                caches.open('dynamic').then(cache => {
                    cache.put(event.request, response.clone());
                });
                return response;
            })
            .catch(() => caches.match(event.request))
    );
});

// Stale While Revalidate
const cacheFirst = (event) => {
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
    );
};
```

### Tip 7: Detect Storage Availability
```javascript
function isStorageAvailable(type) {
    try {
        const storage = window[type];
        const x = '__test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return true;
    } catch(e) {
        return false;
    }
}
```

### Tip 8: Clear Sensitive Data on Logout
```javascript
function secureLogout() {
    localStorage.removeItem('auth_token');
    sessionStorage.clear();
    indexedDB.deleteDatabase('sensitive-data');

    // Clear all cookies
    document.cookie.split(";").forEach(cookie => {
        const eqPos = cookie.indexOf("=");
        const name = eqPos > -1 ? cookie.substr(0, eqPos).trim() : cookie.trim();
        document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 GMT`;
    });
}
```

### Tip 9: Smart Storage Fallback
```javascript
class SmartStorage {
    constructor() {
        this.inMemory = {};
        this.canUseStorage = this.checkAvailability();
    }

    checkAvailability() {
        try {
            const test = '__test__';
            localStorage.setItem(test, test);
            localStorage.removeItem(test);
            return true;
        } catch(e) {
            return false;
        }
    }

    setItem(key, value) {
        if (this.canUseStorage) {
            localStorage.setItem(key, value);
        } else {
            this.inMemory[key] = value;
        }
    }

    getItem(key) {
        if (this.canUseStorage) {
            return localStorage.getItem(key);
        }
        return this.inMemory[key] || null;
    }
}
```

### Tip 10: Broadcast Channel for Real-time Sync
```javascript
const channel = new BroadcastChannel('app_channel');

// Send message to all tabs
channel.postMessage({ type: 'data_updated', data: newData });

// Listen for messages
channel.addEventListener('message', (event) => {
    if (event.data.type === 'data_updated') {
        updateUI(event.data.data);
    }
});
```

## 11.12. Common Mistakes

### Mistake 1: Storing Large Objects Without Serialization
```javascript
// Lỗi
const user = { name: 'John', age: 30 };
localStorage.setItem('user', user); // Saves "[object Object]"

// Đúng
localStorage.setItem('user', JSON.stringify(user));
const loadedUser = JSON.parse(localStorage.getItem('user'));
```

### Mistake 2: Not Checking Storage Availability
```javascript
// Lỗi
localStorage.setItem('data', 'value');

// Đúng
try {
    localStorage.setItem('data', 'value');
} catch(e) {
    if (e.name === 'QuotaExceededError') {
        console.error('Storage is full');
    }
}
```

### Mistake 3: Not Clearing Old Cache Versions
```javascript
// Lỗi
const CACHE_NAME = 'v1'; // Always same

// Đúng
const CACHE_NAME = 'v2'; // Update version

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(name => {
                    if (name !== CACHE_NAME) {
                        return caches.delete(name);
                    }
                })
            );
        })
    );
});
```

### Mistake 4: Storing Sensitive Data in localStorage
```javascript
// Lỗi
localStorage.setItem('auth_token', 'secret_token');

// Đúng - Use sessionStorage or secure httpOnly cookies
sessionStorage.setItem('auth_token', 'secret_token');
// Or use httpOnly cookie on server
```

### Mistake 5: Not Handling JSON.parse Errors
```javascript
// Lỗi
const data = JSON.parse(localStorage.getItem('data'));

// Đúng
try {
    const data = JSON.parse(localStorage.getItem('data') || '{}');
} catch(e) {
    console.error('Invalid JSON:', e);
    const data = {};
}
```

### Mistake 6: Not Removing Event Listeners
```javascript
// Lỗi - Listeners accumulate
window.addEventListener('storage', handler);

// Đúng - Remove when done
window.removeEventListener('storage', handler);
```

### Mistake 7: Assuming IndexedDB Works Like SQL
```javascript
// Lỗi
const results = db.query('SELECT * FROM users WHERE age > 30');

// Đúng - Use indexes and cursors
const transaction = db.transaction(['users'], 'readonly');
const index = transaction.objectStore('users').index('age');
const range = IDBKeyRange.lowerBound(30);
const request = index.getAll(range);
```

### Mistake 8: Not Testing Offline Scenario
```javascript
// Lỗi
fetch('/api/data').then(r => r.json());

// Đúng
fetch('/api/data')
    .then(r => r.json())
    .catch(() => JSON.parse(localStorage.getItem('cached_data')));
```

### Mistake 9: Service Worker Registration Without Error Handling
```javascript
// Lỗi
navigator.serviceWorker.register('/sw.js');

// Đúng
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
        .catch(error => console.error('SW registration failed:', error));
}
```

### Mistake 10: Not Validating Cached Responses
```javascript
// Lỗi - Serves stale content
if (cached) return cached;

// Đúng - Check if still valid
if (cached && !isStale(cached)) {
    return cached;
}
```

## 11.13. Troubleshooting

### Issue 1: Service Worker not updating
**Triệu chứng:** Changes don't reflect despite updating sw.js

**Giải pháp:**
```javascript
// Force update
navigator.serviceWorker.ready.then(reg => {
    reg.update();
});

// Or add version query
navigator.serviceWorker.register('/sw.js?v=' + Date.now());
```

### Issue 2: IndexedDB quota exceeded
**Triệu chứng:** "QuotaExceededError"

**Giải pháp:**
```javascript
// Request persistent storage
if (navigator.storage && navigator.storage.persist) {
    navigator.storage.persist().then(persistent => {
        console.log('Persistent storage:', persistent);
    });
}
```

### Issue 3: Cross-tab communication not working
**Triệu chứng:** Storage event not firing

**Giải pháp:**
```javascript
// Use Broadcast Channel API
const channel = new BroadcastChannel('app');
channel.postMessage(data);
channel.addEventListener('message', e => {
    console.log('Received:', e.data);
});
```

### Issue 4: Cookies blocked in third-party
**Triệu chứng:** Cookies not working in iframes

**Giải pháp:**
```javascript
// Set correct attributes
document.cookie = "name=value; SameSite=None; Secure";
// Requires HTTPS

// Or use postMessage
window.parent.postMessage(data, '*');
```

### Issue 5: localStorage fails in private mode
**Triệu chứng:** Data disappears after closing

**Giải pháp:**
```javascript
// Fall back to in-memory storage
const storage = new SmartStorage();
// (Automatically uses in-memory if localStorage unavailable)
```

### Issue 6: IndexedDB transaction errors
**Triệu chứng:** "Transaction cannot be started"

**Giải pháp:**
```javascript
// Create new transaction for each operation
async function updateData(data) {
    return new Promise((resolve, reject) => {
        const tx = db.transaction(['store'], 'readwrite');
        const store = tx.objectStore('store');
        const req = store.put(data);

        tx.oncomplete = () => resolve();
        tx.onerror = () => reject(tx.error);
    });
}
```

### Issue 7: Cache poisoning
**Triệu chứng:** Stale content served from cache

**Giải pháp:**
```javascript
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            if (response && isStale(response)) {
                return fetch(event.request)
                    .then(r => {
                        caches.open(CACHE_NAME).then(c => {
                            c.put(event.request, r);
                        });
                        return r;
                    });
            }
            return response;
        })
    );
});
```

### Issue 8: Memory leak with open databases
**Triệu chứng:** Browser memory increases

**Giải pháp:**
```javascript
function closeDatabase() {
    if (db) {
        db.close();
        db = null;
    }
}

window.addEventListener('beforeunload', closeDatabase);
```

### Issue 9: Quota exceeded handling
**Triệu chứng:** Can't save more data

**Giải pháp:**
```javascript
function handleQuotaExceeded() {
    // Clear old data
    const cutoff = Date.now() - (7 * 24 * 60 * 60 * 1000);
    const transaction = db.transaction(['data'], 'readwrite');
    const store = transaction.objectStore('data');
    const index = store.index('timestamp');

    index.getAll(IDBKeyRange.upperBound(cutoff)).onsuccess = (e) => {
        e.result.forEach(item => {
            store.delete(item.id);
        });
    };
}
```

### Issue 10: Service Worker scope issues
**Triệu chứng:** Service Worker scope too narrow

**Giải pháp:**
```javascript
// Explicitly set scope
navigator.serviceWorker.register('/js/sw.js', {
    scope: '/' // Register for entire site
});
```

## 11.14. Advanced Topics

### Topic 1: Encrypted Storage with Web Crypto API
```javascript
async function encryptData(data, password) {
    const encoder = new TextEncoder();
    const salt = crypto.getRandomValues(new Uint8Array(16));

    const keyMaterial = await crypto.subtle.importKey(
        'raw',
        encoder.encode(password),
        { name: 'PBKDF2' },
        false,
        ['deriveKey']
    );

    const key = await crypto.subtle.deriveKey(
        {
            name: 'PBKDF2',
            salt: salt,
            iterations: 100000,
            hash: 'SHA-256'
        },
        keyMaterial,
        { name: 'AES-GCM', length: 256 },
        false,
        ['encrypt']
    );

    const iv = crypto.getRandomValues(new Uint8Array(12));
    const encrypted = await crypto.subtle.encrypt(
        { name: 'AES-GCM', iv: iv },
        key,
        encoder.encode(JSON.stringify(data))
    );

    // Combine salt + iv + encrypted
    const combined = new Uint8Array(
        salt.length + iv.length + encrypted.byteLength
    );
    combined.set(salt);
    combined.set(iv, salt.length);
    combined.set(new Uint8Array(encrypted), salt.length + iv.length);

    return btoa(String.fromCharCode.apply(null, combined));
}
```

### Topic 2: Multi-tab Sync with Conflict Resolution
```javascript
class DistributedSync {
    constructor() {
        this.version = 0;
        this.channel = new BroadcastChannel('sync');
        this.pendingChanges = [];
    }

    updateData(key, value) {
        this.version++;
        const change = {
            key, value,
            version: this.version,
            timestamp: Date.now(),
            tabId: this.tabId
        };

        localStorage.setItem(key, JSON.stringify(value));
        this.channel.postMessage(change);
    }

    async resolveConflict(local, remote) {
        // Last write wins
        if (remote.timestamp > local.timestamp) {
            return remote;
        }
        // Tiebreaker: lexicographically
        if (remote.timestamp === local.timestamp) {
            return remote.tabId > local.tabId ? remote : local;
        }
        return local;
    }
}
```

### Topic 3: Partial Sync for Large Datasets
```javascript
class PartialSyncManager {
    async syncLargeDataset(items, chunkSize = 100) {
        const chunks = [];
        for (let i = 0; i < items.length; i += chunkSize) {
            chunks.push(items.slice(i, i + chunkSize));
        }

        for (let i = 0; i < chunks.length; i++) {
            try {
                await this.syncChunk(chunks[i]);
                localStorage.setItem('sync_progress', i + 1);
            } catch (e) {
                localStorage.setItem('last_sync_error', e.message);
                break;
            }
        }
    }

    async syncChunk(chunk) {
        const response = await fetch('/api/batch-sync', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ items: chunk })
        });
        return response.json();
    }
}
```

### Topic 4: Offline Transaction Queue
```javascript
class OfflineQueue {
    constructor() {
        this.queue = [];
        this.syncing = false;
    }

    async queueTransaction(operation) {
        this.queue.push({
            operation,
            timestamp: Date.now()
        });
        localStorage.setItem('pending_queue', JSON.stringify(this.queue));

        if (navigator.onLine) {
            await this.sync();
        }
    }

    async sync() {
        if (this.syncing) return;
        this.syncing = true;

        while (this.queue.length > 0) {
            const item = this.queue[0];
            try {
                await this.executeRemote(item.operation);
                this.queue.shift();
                localStorage.setItem('pending_queue', JSON.stringify(this.queue));
            } catch (e) {
                break; // Retry later
            }
        }

        this.syncing = false;
    }

    async executeRemote(operation) {
        return fetch('/api/execute', {
            method: 'POST',
            body: JSON.stringify(operation)
        }).then(r => r.json());
    }
}
```

### Topic 5: CRDT-based Multi-Device Sync
```javascript
class CRDTCounter {
    constructor(id) {
        this.id = id;
        this.counts = {};
    }

    increment() {
        this.counts[this.id] = (this.counts[this.id] || 0) + 1;
    }

    value() {
        return Object.values(this.counts).reduce((a, b) => a + b, 0);
    }

    merge(other) {
        for (const id in other.counts) {
            this.counts[id] = Math.max(
                this.counts[id] || 0,
                other.counts[id]
            );
        }
    }
}
```

## 11.15. Bài tập thực hành

### Bài 1 (Dễ): Simple Notes App
Yêu cầu: Tạo app ghi chú với localStorage, CRUD operations

### Bài 2 (Dễ): Theme Persistence
Yêu cầu: Chọn theme light/dark, lưu preference

### Bài 3 (Dễ): Form Auto-save
Yêu cầu: Auto-save form data, khôi phục khi reload

### Bài 4 (Dễ): Counter with sessionStorage
Yêu cầu: Counter reset khi đóng tab

### Bài 5 (Trung bình): Todo App with IndexedDB
Yêu cầu: Complete todo app, categories, search

### Bài 6 (Trung bình): Shopping Cart
Yêu cầu: Persist cart, multi-session, export/import

### Bài 7 (Trung bình): Offline Browser Game
Yêu cầu: Snake game, offline playable, high scores

### Bài 8 (Trung bình): Service Worker Setup
Yêu cầu: Static caching, offline fallback, cache busting

### Bài 9 (Trung bình): Multi-tab Sync
Yêu cầu: Broadcast channel, real-time sync, conflict handling

### Bài 10 (Khó): Complete PWA
Yêu cầu: Full offline PWA, Service Worker, IndexedDB, Push notifications

### Bài 11 (Khó): Data Sync Engine
Yêu cầu: Sync mechanism, conflict resolution, rollback

### Bài 12 (Khó): Encrypted Storage
Yêu cầu: Web Crypto API, key derivation, secure deletion

---

**Kết luận:** Web storage technologies cho phép tạo offline-capable applications. Chọn đúng storage method dựa trên use case: cookies cho server communication, localStorage cho persistent data, sessionStorage cho temporary data, và IndexedDB cho large datasets.
