# CHƯƠNG 12: ASYNC/AWAIT

## 12.1. Giới thiệu Async/Await

Async/Await là syntax sugar built on top of Promises, làm async code trông giống synchronous code.

### 12.1.1. Evolution of Async

**Callbacks:**
```javascript
getData(function(a) {
    getMoreData(a, function(b) {
        getMoreData(b, function(c) {
            console.log(c);
        });
    });
});
```

**Promises:**
```javascript
getData()
    .then(a => getMoreData(a))
    .then(b => getMoreData(b))
    .then(c => console.log(c))
    .catch(error => console.error(error));
```

**Async/Await:**
```javascript
async function fetchData() {
    try {
        const a = await getData();
        const b = await getMoreData(a);
        const c = await getMoreData(b);
        console.log(c);
    } catch (error) {
        console.error(error);
    }
}
```

## 12.2. Async Functions

### 12.2.1. Basic Async Function

```javascript
// Always returns a Promise
async function greet() {
    return 'Hello';
}

greet().then(message => console.log(message));  // "Hello"

// Same as:
function greet() {
    return Promise.resolve('Hello');
}
```

### 12.2.2. Async Function Expressions

```javascript
// Function expression
const greet = async function() {
    return 'Hello';
};

// Arrow function
const greet = async () => {
    return 'Hello';
};

// Method
const obj = {
    async greet() {
        return 'Hello';
    }
};
```

## 12.3. Await Keyword

### 12.3.1. Basic Await

```javascript
async function fetchUser() {
    const response = await fetch('/api/user');
    const data = await response.json();
    return data;
}

// Can only use await inside async functions
function notAsync() {
    const data = await fetch('/api');  // SyntaxError!
}
```

### 12.3.2. Multiple Awaits

```javascript
async function fetchAll() {
    const user = await fetchUser();
    const posts = await fetchPosts();
    const comments = await fetchComments();

    return { user, posts, comments };
}
```

### 12.3.3. Await with Non-Promise

```javascript
async function example() {
    const result = await 42;  // Wraps in resolved Promise
    console.log(result);  // 42
}

// Equivalent to:
async function example() {
    const result = await Promise.resolve(42);
    console.log(result);
}
```

## 12.4. Error Handling

### 12.4.1. Try-Catch

```javascript
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error.message);
        throw error;  // Re-throw if needed
    }
}
```

### 12.4.2. Multiple Try-Catch

```javascript
async function processData() {
    let user;
    try {
        user = await fetchUser();
    } catch (error) {
        console.error('Failed to fetch user');
        user = getDefaultUser();
    }

    let posts;
    try {
        posts = await fetchPosts(user.id);
    } catch (error) {
        console.error('Failed to fetch posts');
        posts = [];
    }

    return { user, posts };
}
```

### 12.4.3. Finally

```javascript
async function fetchWithLoader() {
    showLoader();
    try {
        const data = await fetch('/api/data');
        return data.json();
    } catch (error) {
        console.error('Error:', error);
        return null;
    } finally {
        hideLoader();  // Always executes
    }
}
```

## 12.5. Parallel Execution

### 12.5.1. Promise.all with Async/Await

```javascript
// Sequential (slow)
async function fetchSequential() {
    const user = await fetchUser();      // Wait 1s
    const posts = await fetchPosts();    // Wait 1s
    const comments = await fetchComments(); // Wait 1s
    // Total: 3s
}

// Parallel (fast)
async function fetchParallel() {
    const [user, posts, comments] = await Promise.all([
        fetchUser(),
        fetchPosts(),
        fetchComments()
    ]);
    // Total: 1s (all run simultaneously)
    return { user, posts, comments };
}
```

### 12.5.2. Promise.allSettled

```javascript
async function fetchAllData() {
    const results = await Promise.allSettled([
        fetchUser(),
        fetchPosts(),
        fetchComments()
    ]);

    results.forEach((result, index) => {
        if (result.status === 'fulfilled') {
            console.log(`Result ${index}:`, result.value);
        } else {
            console.log(`Error ${index}:`, result.reason);
        }
    });
}
```

### 12.5.3. Promise.race

```javascript
async function fetchWithTimeout(url, timeout = 5000) {
    const fetchPromise = fetch(url);
    const timeoutPromise = new Promise((_, reject) =>
        setTimeout(() => reject(new Error('Timeout')), timeout)
    );

    const response = await Promise.race([fetchPromise, timeoutPromise]);
    return response.json();
}
```

## 12.6. Practical Examples

### 12.6.1. API Calls

```javascript
async function getUser(id) {
    const response = await fetch(`/api/users/${id}`);

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
}

async function getUserWithPosts(id) {
    const user = await getUser(id);
    const posts = await fetch(`/api/users/${id}/posts`).then(r => r.json());

    return {
        ...user,
        posts
    };
}
```

### 12.6.2. Sequential Processing

```javascript
async function processUsers(userIds) {
    const results = [];

    for (const id of userIds) {
        const user = await getUser(id);
        const processed = await processUser(user);
        results.push(processed);
    }

    return results;
}
```

### 12.6.3. Parallel Processing

```javascript
async function processUsersParallel(userIds) {
    const promises = userIds.map(async (id) => {
        const user = await getUser(id);
        return processUser(user);
    });

    return Promise.all(promises);
}
```

### 12.6.4. Retry Logic

```javascript
async function fetchWithRetry(url, retries = 3) {
    for (let i = 0; i < retries; i++) {
        try {
            const response = await fetch(url);
            return await response.json();
        } catch (error) {
            if (i === retries - 1) throw error;
            console.log(`Retry ${i + 1}/${retries}`);
            await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
        }
    }
}
```

### 12.6.5. Conditional Fetching

```javascript
async function getUserData(id, includeDetails = false) {
    const user = await fetchUser(id);

    if (includeDetails) {
        const [posts, friends, settings] = await Promise.all([
            fetchPosts(id),
            fetchFriends(id),
            fetchSettings(id)
        ]);

        return { ...user, posts, friends, settings };
    }

    return user;
}
```

### 12.6.6. Caching

```javascript
const cache = new Map();

async function fetchWithCache(url) {
    if (cache.has(url)) {
        return cache.get(url);
    }

    const response = await fetch(url);
    const data = await response.json();

    cache.set(url, data);
    return data;
}
```

## 12.7. Advanced Patterns

### 12.7.1. Async Iteration

```javascript
async function* asyncGenerator() {
    yield await Promise.resolve(1);
    yield await Promise.resolve(2);
    yield await Promise.resolve(3);
}

async function iterate() {
    for await (const value of asyncGenerator()) {
        console.log(value);  // 1, 2, 3
    }
}
```

### 12.7.2. Queue Processing

```javascript
class AsyncQueue {
    constructor() {
        this.queue = [];
        this.processing = false;
    }

    async add(task) {
        this.queue.push(task);
        if (!this.processing) {
            await this.process();
        }
    }

    async process() {
        this.processing = true;

        while (this.queue.length > 0) {
            const task = this.queue.shift();
            try {
                await task();
            } catch (error) {
                console.error('Task failed:', error);
            }
        }

        this.processing = false;
    }
}
```

### 12.7.3. Throttle Async

```javascript
async function throttleAsync(fn, limit) {
    const queue = [];
    let activeCount = 0;

    return async function(...args) {
        while (activeCount >= limit) {
            await new Promise(resolve => queue.push(resolve));
        }

        activeCount++;
        try {
            return await fn(...args);
        } finally {
            activeCount--;
            const resolve = queue.shift();
            if (resolve) resolve();
        }
    };
}

// Usage
const limitedFetch = throttleAsync(fetch, 3);
```

### 12.7.4. Race with Default

```javascript
async function fetchWithDefault(url, defaultValue, timeout = 5000) {
    try {
        const timeoutPromise = new Promise((_, reject) =>
            setTimeout(() => reject(new Error('Timeout')), timeout)
        );

        const response = await Promise.race([
            fetch(url),
            timeoutPromise
        ]);

        return await response.json();
    } catch (error) {
        console.error('Using default value');
        return defaultValue;
    }
}
```

## 12.8. Top-Level Await (ES2022)

### 12.8.1. Module-Level Await

```javascript
// In ES modules (.mjs or type="module")
const data = await fetch('/api/config').then(r => r.json());

export default data;

// Conditional import
const module = await import(
    condition ? './module-a.js' : './module-b.js'
);
```

### 12.8.2. Dynamic Config Loading

```javascript
// config.js
const env = await fetch('/api/env').then(r => r.json());

export const config = {
    apiUrl: env.API_URL,
    debug: env.DEBUG
};

// main.js
import { config } from './config.js';
console.log(config);  // Already loaded
```

## 12.9. Best Practices

### 12.9.1. Always Handle Errors

```javascript
// Good
async function fetchData() {
    try {
        return await fetch('/api/data');
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Or with .catch()
async function fetchData() {
    return fetch('/api/data').catch(error => {
        console.error('Error:', error);
        throw error;
    });
}
```

### 12.9.2. Avoid Unnecessary Await

```javascript
// Bad: Unnecessary await
async function getUser(id) {
    return await fetch(`/api/users/${id}`);
}

// Good: Return Promise directly
async function getUser(id) {
    return fetch(`/api/users/${id}`);
}

// Only await if you need to process the result
async function getUser(id) {
    const response = await fetch(`/api/users/${id}`);
    return response.json();  // Need to await here
}
```

### 12.9.3. Parallel When Possible

```javascript
// Bad: Sequential (slow)
const user = await fetchUser();
const posts = await fetchPosts();

// Good: Parallel (fast)
const [user, posts] = await Promise.all([
    fetchUser(),
    fetchPosts()
]);
```

## 12.10. Common Mistakes

### 12.10.1. Forgot Async Keyword

```javascript
// Wrong
function getData() {
    const data = await fetch('/api');  // SyntaxError
}

// Correct
async function getData() {
    const data = await fetch('/api');
}
```

### 12.10.2. Await in Loop

```javascript
// Bad: Sequential processing
async function processUsers(ids) {
    const users = [];
    for (const id of ids) {
        users.push(await fetchUser(id));  // Slow!
    }
    return users;
}

// Good: Parallel processing
async function processUsers(ids) {
    return Promise.all(ids.map(id => fetchUser(id)));
}
```

### 12.10.3. Not Handling Promise Rejection

```javascript
// Bad: Unhandled rejection
async function getData() {
    const data = await fetch('/api/data');
    return data.json();
}
getData();  // If fails, unhandled rejection

// Good: Handle errors
async function getData() {
    try {
        const data = await fetch('/api/data');
        return data.json();
    } catch (error) {
        console.error(error);
    }
}
```

## 12.11. Exercises

### Exercise 1: Convert Promise Chain

```javascript
// Convert this Promise chain to async/await
function getUserData(id) {
    return fetch(`/api/users/${id}`)
        .then(response => response.json())
        .then(user => {
            return fetch(`/api/posts?userId=${user.id}`)
                .then(response => response.json())
                .then(posts => ({ user, posts }));
        });
}
```

### Exercise 2: Parallel Requests

```javascript
// Fetch multiple users in parallel using async/await
async function getUsers(ids) {
    // Your code: fetch all users at once
}
```

### Exercise 3: Retry Logic

```javascript
// Implement retry logic for failed requests
async function fetchWithRetry(url, maxRetries = 3) {
    // Your code: retry on failure
}
```

---

**Kết luận:** Async/Await làm async code dễ đọc và maintain hơn. Luôn handle errors, sử dụng parallel execution khi có thể, và tránh await không cần thiết.

**Chương tiếp theo:** Map, Set, WeakMap, WeakSet
