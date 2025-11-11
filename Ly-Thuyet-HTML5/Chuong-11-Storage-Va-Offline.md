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

## 11.9. Practical Examples

### 11.9.1. Offline-First App

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

## 11.11. Bài tập thực hành

### Bài 1: Notes App
Tạo app ghi chú lưu bằng localStorage

### Bài 2: Offline Todo List
Tạo todo app hoạt động offline với Service Worker

### Bài 3: Shopping Cart
Tạo shopping cart persist data với localStorage

### Bài 4: PWA
Tạo Progressive Web App đơn giản với Service Worker và caching

---

**Kết luận:** Web storage technologies cho phép tạo offline-capable applications. Chọn đúng storage method dựa trên use case: cookies cho server communication, localStorage cho persistent data, sessionStorage cho temporary data, và IndexedDB cho large datasets.
