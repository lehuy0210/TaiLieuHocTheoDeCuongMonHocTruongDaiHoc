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

## 12.5. Use Cases Thực Tế

### 12.5.1. Use Case 1: API Data Orchestration

```javascript
// Fetch multiple APIs với error handling và fallback
async function getUserDashboard(userId) {
    try {
        const [userPromise, postsPromise, commentsPromise] = [
            fetch(`/api/users/${userId}`),
            fetch(`/api/posts?userId=${userId}`),
            fetch(`/api/comments?userId=${userId}`)
        ];

        // Parallel fetch
        const [userRes, postsRes, commentsRes] = await Promise.all([
            userPromise,
            postsPromise,
            commentsPromise
        ]);

        if (!userRes.ok) throw new Error('Failed to fetch user');

        const [user, posts, comments] = await Promise.all([
            userRes.json(),
            postsRes.ok ? postsRes.json() : [],
            commentsRes.ok ? commentsRes.json() : []
        ]);

        return {
            user,
            stats: {
                posts: posts.length,
                comments: comments.length,
                engagement: (posts.length + comments.length) / 2
            }
        };
    } catch (error) {
        console.error('Dashboard load failed:', error);
        return { user: null, stats: null, error };
    }
}
```

### 12.5.2. Use Case 2: Sequential File Processing

```javascript
// Xử lý các tác vụ theo thứ tự
async function processDataPipeline(files) {
    const results = [];

    for (const file of files) {
        try {
            console.log(`Processing ${file.name}...`);

            // Step 1: Read file
            const data = await readFile(file);

            // Step 2: Validate
            const validated = await validateData(data);

            // Step 3: Transform
            const transformed = await transformData(validated);

            // Step 4: Save
            const saved = await saveToDatabase(transformed);

            results.push({ file: file.name, success: true, id: saved.id });
            console.log(`Completed ${file.name}`);
        } catch (error) {
            results.push({ file: file.name, success: false, error: error.message });
        }
    }

    return results;
}
```

### 12.5.3. Use Case 3: Batch Processing with Rate Limiting

```javascript
// Xử lý batch requests với giới hạn đồng thời
async function batchFetchUsers(userIds, batchSize = 5) {
    const results = [];

    for (let i = 0; i < userIds.length; i += batchSize) {
        const batch = userIds.slice(i, i + batchSize);
        console.log(`Fetching batch ${i / batchSize + 1}`);

        try {
            const users = await Promise.all(
                batch.map(id => fetchUserDetail(id))
            );
            results.push(...users);

            // Rate limiting: wait before next batch
            if (i + batchSize < userIds.length) {
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
        } catch (error) {
            console.error(`Batch failed:`, error);
            // Continue với batch tiếp theo
        }
    }

    return results;
}
```

### 12.5.4. Use Case 4: Real-time Data Streaming

```javascript
// Xử lý streaming data với async generator
async function* fetchUserUpdates(userId) {
    let page = 1;
    let hasMore = true;

    while (hasMore) {
        try {
            const response = await fetch(`/api/updates?userId=${userId}&page=${page}`);
            const data = await response.json();

            if (data.updates.length === 0) {
                hasMore = false;
            } else {
                yield* data.updates;  // Yield each update
                page++;
            }
        } catch (error) {
            console.error(`Error fetching updates:`, error);
            hasMore = false;
        }
    }
}

// Usage
async function processUserUpdates(userId) {
    for await (const update of fetchUserUpdates(userId)) {
        console.log(`Processing update: ${update.id}`);
        await handleUpdate(update);
    }
}
```

### 12.5.5. Use Case 5: Timeout Handling

```javascript
// Thực hiện operation với timeout
async function fetchWithTimeout(url, timeout = 5000) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);

    try {
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        if (error.name === 'AbortError') {
            throw new Error(`Request timeout after ${timeout}ms`);
        }
        throw error;
    } finally {
        clearTimeout(timeoutId);
    }
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

## 12.10. Tips & Tricks

### Tip 1: Promise.allSettled for Partial Failures

```javascript
// Nếu một request fail, allSettled vẫn chờ tất cả
async function fetchAllData(urls) {
    const results = await Promise.allSettled(
        urls.map(url => fetch(url).then(r => r.json()))
    );

    const successful = results
        .filter(r => r.status === 'fulfilled')
        .map(r => r.value);

    const failed = results
        .filter(r => r.status === 'rejected')
        .map(r => r.reason);

    return { successful, failed };
}
```

### Tip 2: AbortController for Cancellation

```javascript
// Cancel async operations
const controller = new AbortController();

async function fetchData(url) {
    try {
        return await fetch(url, { signal: controller.signal });
    } catch (error) {
        if (error.name === 'AbortError') {
            console.log('Request was cancelled');
        }
        throw error;
    }
}

// Cancel request
setTimeout(() => controller.abort(), 5000);
```

### Tip 3: Using Async IIFE

```javascript
// Async Immediately Invoked Function Expression
(async () => {
    try {
        const data = await fetchData();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
})();
```

### Tip 4: Promise.any for First Success

```javascript
// Race - trả về first fulfilled (ES2021)
async function fetchFromFastestServer(urls) {
    try {
        const response = await Promise.any(
            urls.map(url => fetch(url))
        );
        return response;
    } catch (error) {
        console.log('All requests failed:', error);
    }
}
```

### Tip 5: Async Recursive Functions

```javascript
// Recursively fetch paginated data
async function fetchAllPages(url, page = 1, acc = []) {
    const response = await fetch(`${url}?page=${page}`);
    const data = await response.json();
    const result = [...acc, ...data.items];

    if (data.hasMore) {
        return fetchAllPages(url, page + 1, result);
    }

    return result;
}
```

### Tip 6: Conditional Async Operations

```javascript
// Skip unnecessary async operations
async function getUser(id, includeDetails = false) {
    const user = await fetchUser(id);

    if (includeDetails) {
        const details = await fetchUserDetails(id);
        return { ...user, ...details };
    }

    return user;
}
```

### Tip 7: Transform Callbacks to Async

```javascript
// Promisify callbacks
function promisify(fn) {
    return (...args) => new Promise((resolve, reject) => {
        fn(...args, (err, result) => {
            if (err) reject(err);
            else resolve(result);
        });
    });
}

// Usage with async/await
const readFile = promisify(require('fs').readFile);
async function readConfig() {
    const data = await readFile('config.json', 'utf-8');
    return JSON.parse(data);
}
```

### Tip 8: Parallel Execution with Concurrency Control

```javascript
// Execute multiple promises với maximum concurrency
async function parallelLimit(promises, limit) {
    const results = [];
    const executing = [];

    for (const promise of promises) {
        const p = Promise.resolve(promise).then(r => {
            executing.splice(executing.indexOf(p), 1);
            return r;
        });
        results.push(p);
        executing.push(p);

        if (executing.length >= limit) {
            await Promise.race(executing);
        }
    }

    return Promise.all(results);
}
```

### Tip 9: Error Aggregation

```javascript
// Collect multiple errors thay vì fail immediately
async function validateAndProcess(items) {
    const errors = [];
    const results = [];

    for (const item of items) {
        try {
            const result = await processItem(item);
            results.push(result);
        } catch (error) {
            errors.push({ item, error });
        }
    }

    if (errors.length > 0) {
        throw new Error(`${errors.length} items failed: ${JSON.stringify(errors)}`);
    }

    return results;
}
```

### Tip 10: Cleanup with Finally

```javascript
// Ensure cleanup happens
async function withConnection(fn) {
    const conn = await createConnection();
    try {
        return await fn(conn);
    } finally {
        await conn.close();  // Always executed
    }
}

// Usage
const result = await withConnection(async (conn) => {
    return await conn.query('SELECT * FROM users');
});
```

## 12.11. Common Mistakes

### Mistake 1: Forgetting Async Keyword

```javascript
// BAD: SyntaxError
function getData() {
    const data = await fetch('/api');
}

// GOOD: Mark function as async
async function getData() {
    const data = await fetch('/api');
}
```

### Mistake 2: Awaiting in Loop (Performance)

```javascript
// BAD: Sequential (slow)
async function processItems(items) {
    for (const item of items) {
        await processItem(item);  // Waits each one
    }
}

// GOOD: Parallel (fast)
async function processItems(items) {
    await Promise.all(items.map(processItem));
}
```

### Mistake 3: Not Handling Errors

```javascript
// BAD: Unhandled rejection
async function fetchData() {
    const data = await fetch('/api');  // Error silently fails
    return data.json();
}

// GOOD: Always handle
async function fetchData() {
    try {
        const data = await fetch('/api');
        return data.json();
    } catch (error) {
        console.error('Fetch failed:', error);
        throw error;  // Re-throw or return fallback
    }
}
```

### Mistake 4: Ignoring HTTP Errors

```javascript
// BAD: 404/500 don't throw
const data = await fetch('/api/data');
const result = await data.json();  // No error thrown!

// GOOD: Check status
const response = await fetch('/api/data');
if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
}
const result = await response.json();
```

### Mistake 5: Unnecessary Await

```javascript
// BAD: Double awaiting
async function getUser(id) {
    return await fetch(`/api/users/${id}`);
}

// GOOD: Return promise directly
async function getUser(id) {
    return fetch(`/api/users/${id}`);
}
```

### Mistake 6: Race Condition

```javascript
// BAD: Race condition
let user = null;

async function loadUser(id) {
    user = await fetchUser(id);  // Could be overwritten
}

// GOOD: Use Promises properly
async function getUser(id) {
    return fetchUser(id);
}
```

### Mistake 7: Not Using Promise.all

```javascript
// BAD: Sequential
const user = await fetchUser();
const posts = await fetchPosts();
const comments = await fetchComments();
// Takes 3x time

// GOOD: Parallel
const [user, posts, comments] = await Promise.all([
    fetchUser(),
    fetchPosts(),
    fetchComments()
]);
// Takes time of slowest request
```

### Mistake 8: Losing Error Context

```javascript
// BAD: Error message lost
try {
    await riskyOperation();
} catch (error) {
    console.error('Operation failed');  // No error details
}

// GOOD: Preserve context
try {
    await riskyOperation();
} catch (error) {
    console.error('Operation failed:', error.message);
    throw new Error(`Failed to process: ${error.message}`);
}
```

### Mistake 9: Async in Callbacks

```javascript
// BAD: Async callback not handled
[1, 2, 3].forEach(async (id) => {
    const user = await fetchUser(id);  // Not awaited
});

// GOOD: Use Promise.all
await Promise.all([1, 2, 3].map(id => fetchUser(id)));
```

### Mistake 10: Forgetting Return Type

```javascript
// BAD: Unclear what is returned
async function getData() {
    fetch('/api');  // Missing return
}

// GOOD: Clear return
async function getData() {
    const response = await fetch('/api');
    return response.json();
}
```

## 12.12. Troubleshooting Issues

### Issue 1: Unhandled Promise Rejection

**Problem:**
```javascript
async function load() {
    const data = await fetch('/api');
    return data.json();
}

load();  // No .catch(), unhandled rejection
```

**Solution:**
```javascript
load().catch(error => {
    console.error('Failed to load:', error);
    // Handle error
});

// Or use async IIFE
(async () => {
    try {
        const data = await load();
    } catch (error) {
        console.error('Failed to load:', error);
    }
})();
```

### Issue 2: Memory Leak with Event Listeners

**Problem:**
```javascript
async function watchData() {
    const data = await fetchData();
    document.addEventListener('click', () => {
        // References data, never cleaned up
    });
}
```

**Solution:**
```javascript
async function watchData() {
    const data = await fetchData();
    const handler = () => console.log(data);
    document.addEventListener('click', handler);

    // Cleanup
    return () => document.removeEventListener('click', handler);
}
```

### Issue 3: Slow Waterfall of Requests

**Problem:**
```javascript
async function load() {
    const user = await fetchUser();
    const posts = await fetchPosts(user.id);
    const comments = await fetchComments(posts[0].id);
    // Sequential, very slow!
}
```

**Solution:**
```javascript
async function load() {
    const user = await fetchUser();
    // Fetch in parallel if possible
    const [posts, friends] = await Promise.all([
        fetchPosts(user.id),
        fetchFriends(user.id)
    ]);
    return { user, posts, friends };
}
```

### Issue 4: Lost this Context

**Problem:**
```javascript
class DataLoader {
    url = '/api/data';

    async load() {
        const data = await fetch(this.url);
        return data.json();
    }
}

const loader = new DataLoader();
const fn = loader.load;
fn();  // this is undefined
```

**Solution:**
```javascript
// Bind explicitly
const fn = loader.load.bind(loader);

// Or use arrow function
const load = async () => {
    const data = await fetch(this.url);
    return data.json();
};

// Or use static method
static async load(url) {
    const data = await fetch(url);
    return data.json();
}
```

### Issue 5: Too Many Concurrent Requests

**Problem:**
```javascript
async function processAll(items) {
    // Starts 1000 requests at once - crashes!
    return Promise.all(items.map(processItem));
}
```

**Solution:**
```javascript
async function processAll(items, concurrency = 5) {
    const results = [];
    for (let i = 0; i < items.length; i += concurrency) {
        const batch = items.slice(i, i + concurrency);
        const batchResults = await Promise.all(
            batch.map(processItem)
        );
        results.push(...batchResults);
    }
    return results;
}
```

### Issue 6: Timeout Handling

**Problem:**
```javascript
// Request hangs indefinitely
const data = await fetch('/api/data');
```

**Solution:**
```javascript
async function fetchWithTimeout(url, timeout = 5000) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);

    try {
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);
        return response.json();
    } catch (error) {
        if (error.name === 'AbortError') {
            throw new Error('Request timeout');
        }
        throw error;
    }
}
```

### Issue 7: Circular Dependencies

**Problem:**
```javascript
// Task A waits for B, B waits for A
async function taskA() {
    const result = await taskB();  // Deadlock
}

async function taskB() {
    const result = await taskA();
}
```

**Solution:**
```javascript
// Break circular dependency
async function taskA() {
    const result = await taskBWithTimeout();
}

// Or use Promise.race
const result = await Promise.race([
    taskA(),
    new Promise((_, reject) =>
        setTimeout(() => reject(new Error('Deadlock')), 1000)
    )
]);
```

### Issue 8: Stale Data

**Problem:**
```javascript
let cachedUser = null;

async function getUser(id) {
    if (cachedUser) return cachedUser;
    cachedUser = await fetchUser(id);  // Forever stale
}
```

**Solution:**
```javascript
const cache = new Map();
const TTL = 60000;  // 1 minute

async function getUser(id) {
    const cached = cache.get(id);
    if (cached && Date.now() - cached.time < TTL) {
        return cached.data;
    }

    const data = await fetchUser(id);
    cache.set(id, { data, time: Date.now() });
    return data;
}
```

### Issue 9: Partial Failures Ignored

**Problem:**
```javascript
// If one fails, all are lost
const [a, b, c] = await Promise.all([
    fetch1(), fetch2(), fetch3()
]);
```

**Solution:**
```javascript
const results = await Promise.allSettled([
    fetch1(), fetch2(), fetch3()
]);

const fulfilled = results
    .filter(r => r.status === 'fulfilled')
    .map(r => r.value);

const errors = results
    .filter(r => r.status === 'rejected')
    .map((r, i) => ({ index: i, error: r.reason }));

console.log('Success:', fulfilled, 'Errors:', errors);
```

### Issue 10: Complex Async Logic

**Problem:**
```javascript
// Hard to follow logic
const data1 = await fetch1();
const data2 = data1 ? await fetch2(data1.id) : null;
const data3 = data2 ? await fetch3(data2.id) : null;
// Very nested and hard to maintain
```

**Solution:**
```javascript
async function loadRelatedData() {
    const data1 = await fetch1();
    if (!data1) return null;

    const data2 = await fetch2(data1.id);
    if (!data2) return { data1 };

    const data3 = await fetch3(data2.id);

    return { data1, data2, data3 };
}
```

## 12.13. Advanced Topics

### 12.13.1. Async Generators

```javascript
// Generate values asynchronously
async function* fetchPages(baseUrl) {
    let page = 1;
    while (true) {
        const response = await fetch(`${baseUrl}?page=${page}`);
        const data = await response.json();

        if (data.items.length === 0) break;

        yield* data.items;
        page++;
    }
}

// Usage
async function processAllPages() {
    for await (const item of fetchPages('/api/items')) {
        console.log('Processing:', item);
    }
}
```

### 12.13.2. Async Middleware Pattern

```javascript
// Compose async middlewares
function createMiddleware() {
    const middlewares = [];

    return {
        use(fn) {
            middlewares.push(fn);
            return this;
        },

        async execute(request) {
            let index = -1;

            const dispatch = async (i) => {
                if (i <= index) throw new Error('next() called multiple times');
                index = i;

                if (i < middlewares.length) {
                    return middlewares[i](request, () => dispatch(i + 1));
                }
            };

            return dispatch(0);
        }
    };
}

// Usage
const app = createMiddleware();
app.use(async (req, next) => {
    console.log('Before');
    await next();
    console.log('After');
});
```

### 12.13.3. Async Resource Management

```javascript
// Ensure resources are cleaned up
class Resource {
    async open() {
        // Open resource
    }

    async close() {
        // Close resource
    }
}

// Using pattern
async function withResource(fn) {
    const resource = new Resource();
    try {
        await resource.open();
        return await fn(resource);
    } finally {
        await resource.close();  // Always called
    }
}

// Usage
const result = await withResource(async (resource) => {
    // Use resource
    return await resource.read();
});
```

### 12.13.4. Async Error Boundary

```javascript
// Catch errors from async operations
class AsyncBoundary {
    constructor(errorHandler) {
        this.errorHandler = errorHandler;
    }

    async execute(fn) {
        try {
            return await fn();
        } catch (error) {
            this.errorHandler(error);
            throw error;
        }
    }

    async executeWithFallback(fn, fallback) {
        try {
            return await fn();
        } catch (error) {
            this.errorHandler(error);
            return fallback();
        }
    }
}

// Usage
const boundary = new AsyncBoundary((error) => {
    console.error('Boundary error:', error);
});

const result = await boundary.executeWithFallback(
    () => fetch('/api'),
    () => ({ data: [] })
);
```

### 12.13.5. Async State Machine

```javascript
// State machine with async transitions
class StateMachine {
    constructor(initialState) {
        this.state = initialState;
        this.handlers = {};
    }

    on(state, handler) {
        this.handlers[state] = handler;
        return this;
    }

    async transition(event) {
        const handler = this.handlers[this.state];
        if (!handler) throw new Error(`No handler for ${this.state}`);

        const nextState = await handler(event);
        if (nextState) this.state = nextState;
        return nextState;
    }
}

// Usage
const machine = new StateMachine('idle');
machine
    .on('idle', async (event) => {
        if (event === 'start') {
            await delay(1000);
            return 'running';
        }
    })
    .on('running', async (event) => {
        if (event === 'stop') {
            return 'stopped';
        }
    });
```

## 12.14. Exercises

### Exercise 1 (Dễ): Convert Promise Chain

```javascript
// Chuyển đổi Promise chain thành async/await
function getUserData(id) {
    return fetch(`/api/users/${id}`)
        .then(response => response.json())
        .then(user => {
            return fetch(`/api/posts?userId=${user.id}`)
                .then(response => response.json())
                .then(posts => ({ user, posts }));
        });
}

// Giải pháp: Sử dụng async/await
```

### Exercise 2 (Dễ): Basic Async Function

```javascript
// Tạo hàm async fetch user
async function getUser(id) {
    // Fetch từ /api/users/{id}
    // Return user data
}

// Usage:
// const user = await getUser(1);
```

### Exercise 3 (Dễ): Error Handling

```javascript
// Thêm error handling cho async function
async function fetchData(url) {
    // Fetch từ url
    // Nếu không response.ok, throw error
    // Catch và log error
}
```

### Exercise 4 (Dễ): Parallel Requests

```javascript
// Fetch multiple users in parallel
async function getMultipleUsers(ids) {
    // Sử dụng Promise.all
    // Return array of users
}
```

### Exercise 5 (Trung bình): Sequential Processing

```javascript
// Xử lý items theo thứ tự
async function processItems(items) {
    const results = [];

    for (const item of items) {
        // Process each item
        // Add result to results array
    }

    return results;
}
```

### Exercise 6 (Trung bình): Retry Logic

```javascript
// Implement retry với exponential backoff
async function fetchWithRetry(url, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
        try {
            // Fetch URL
            // Return response
        } catch (error) {
            // Last retry?
            // Wait before retry: 1s, 2s, 4s...
        }
    }
}
```

### Exercise 7 (Trung bình): Timeout Handling

```javascript
// Fetch với timeout
async function fetchWithTimeout(url, timeout = 5000) {
    // Sử dụng AbortController
    // Throw error if timeout
}
```

### Exercise 8 (Trung bình): Batch Processing

```javascript
// Process items in batches
async function batchProcess(items, batchSize = 5) {
    const results = [];

    // Process items in batches parallel
    // Each batch runs at the same time
}
```

### Exercise 9 (Trung bình): Cache with TTL

```javascript
// Tạo async fetch function với cache
async function cachedFetch(url, ttl = 60000) {
    // Cache results
    // Check TTL before returning cached
    // Fetch new data if expired
}
```

### Exercise 10 (Khó): Async Queue

```javascript
// Tạo async queue processor
class AsyncQueue {
    // Constructor

    async add(task) {
        // Add task to queue
        // Process if not processing
    }

    async process() {
        // Process all tasks sequentially
        // Handle errors
    }
}
```

### Exercise 11 (Khó): Async State Machine

```javascript
// Tạo state machine with async transitions
class DataLoader {
    constructor() {
        this.state = 'idle';  // idle, loading, loaded, error
    }

    async load(url) {
        // Transition: idle -> loading -> loaded/error
        // Handle each state transition
    }
}
```

### Exercise 12 (Khó): Promise Pool

```javascript
// Tạo promise pool với max concurrency
class PromisePool {
    constructor(concurrency) {
        // Store concurrency limit
    }

    async run(tasks) {
        // Execute tasks with max concurrency
        // Return all results in order
    }
}

// Usage:
// const pool = new PromisePool(3);
// const results = await pool.run([task1, task2, task3, ...]);
```

---

**Kết luận:** Async/Await làm async code dễ đọc và maintain hơn. Nắm vững error handling, parallel execution, và cơ chế cleanup để viết robust async code. Hiểu rõ Promise.all, Promise.race, và Promise.allSettled để optimize performance.

**Chương tiếp theo:** Map, Set, WeakMap, WeakSet
