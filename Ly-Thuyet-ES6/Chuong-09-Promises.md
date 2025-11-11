# CHƯƠNG 9: PROMISES

## 9.1. Giới thiệu Promises

Promise là object đại diện cho eventual completion (or failure) của một asynchronous operation.

### 9.1.1. Tại sao cần Promises?

**Callback Hell (ES5):**
```javascript
getData(function(a) {
    getMoreData(a, function(b) {
        getMoreData(b, function(c) {
            getMoreData(c, function(d) {
                getMoreData(d, function(e) {
                    // ...
                });
            });
        });
    });
});
```

**Promises (ES6):**
```javascript
getData()
    .then(a => getMoreData(a))
    .then(b => getMoreData(b))
    .then(c => getMoreData(c))
    .then(d => getMoreData(d))
    .catch(error => console.log(error));
```

## 9.2. Promise States

Promise có 3 states:

1. **Pending**: Initial state
2. **Fulfilled**: Operation completed successfully
3. **Rejected**: Operation failed

```javascript
const promise = new Promise((resolve, reject) => {
    // Pending state

    if (success) {
        resolve(value);  // Fulfilled
    } else {
        reject(error);   // Rejected
    }
});
```

## 9.3. Creating Promises

### 9.3.1. Basic Promise

```javascript
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Success!');
    }, 1000);
});

myPromise.then(result => {
    console.log(result);  // "Success!" after 1 second
});
```

### 9.3.2. Promise with Rejection

```javascript
const fetchData = new Promise((resolve, reject) => {
    const success = Math.random() > 0.5;

    setTimeout(() => {
        if (success) {
            resolve({ data: 'Some data' });
        } else {
            reject(new Error('Failed to fetch'));
        }
    }, 1000);
});

fetchData
    .then(result => console.log(result))
    .catch(error => console.error(error));
```

## 9.4. Promise Methods

### 9.4.1. .then()

```javascript
promise.then(
    value => {
        // Success callback
        console.log(value);
    },
    error => {
        // Error callback (optional)
        console.error(error);
    }
);

// Chaining
promise
    .then(value => {
        console.log(value);
        return newValue;
    })
    .then(newValue => {
        console.log(newValue);
    });
```

### 9.4.2. .catch()

```javascript
promise
    .then(value => console.log(value))
    .catch(error => console.error(error));

// Catch any error in the chain
promise
    .then(value => {
        throw new Error('Something went wrong');
    })
    .then(value => {
        // Won't execute
    })
    .catch(error => {
        console.error(error);  // Catches the error
    });
```

### 9.4.3. .finally()

```javascript
promise
    .then(result => console.log(result))
    .catch(error => console.error(error))
    .finally(() => {
        console.log('Cleanup'); // Always executes
    });

// Practical example
fetchData()
    .then(data => updateUI(data))
    .catch(error => showError(error))
    .finally(() => hideLoader());
```

## 9.5. Promise Chaining

```javascript
const promise = new Promise((resolve, reject) => {
    resolve(1);
});

promise
    .then(value => {
        console.log(value);  // 1
        return value * 2;
    })
    .then(value => {
        console.log(value);  // 2
        return value * 2;
    })
    .then(value => {
        console.log(value);  // 4
    });
```

### 9.5.1. Returning Promises

```javascript
function fetchUser() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve({ id: 1, name: 'John' });
        }, 1000);
    });
}

function fetchPosts(userId) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(['Post 1', 'Post 2']);
        }, 1000);
    });
}

fetchUser()
    .then(user => {
        console.log('User:', user);
        return fetchPosts(user.id);
    })
    .then(posts => {
        console.log('Posts:', posts);
    })
    .catch(error => console.error(error));
```

## 9.6. Static Methods

### 9.6.1. Promise.resolve()

```javascript
// Create immediately resolved promise
const promise = Promise.resolve('Success');

promise.then(value => console.log(value));  // "Success"

// Convert value to promise
const converted = Promise.resolve(42);
```

### 9.6.2. Promise.reject()

```javascript
const promise = Promise.reject(new Error('Failed'));

promise.catch(error => console.error(error));
```

### 9.6.3. Promise.all()

Chờ tất cả promises complete:

```javascript
const promise1 = Promise.resolve(1);
const promise2 = Promise.resolve(2);
const promise3 = Promise.resolve(3);

Promise.all([promise1, promise2, promise3])
    .then(values => {
        console.log(values);  // [1, 2, 3]
    })
    .catch(error => {
        // If ANY promise rejects
        console.error(error);
    });

// Practical example
Promise.all([
    fetch('/api/users'),
    fetch('/api/posts'),
    fetch('/api/comments')
])
    .then(responses => Promise.all(
        responses.map(r => r.json())
    ))
    .then(([users, posts, comments]) => {
        console.log({ users, posts, comments });
    });
```

### 9.6.4. Promise.race()

Trả về promise đầu tiên complete:

```javascript
const promise1 = new Promise(resolve =>
    setTimeout(() => resolve('First'), 1000)
);

const promise2 = new Promise(resolve =>
    setTimeout(() => resolve('Second'), 500)
);

Promise.race([promise1, promise2])
    .then(value => {
        console.log(value);  // "Second" (faster)
    });

// Timeout implementation
function timeout(ms) {
    return new Promise((_, reject) =>
        setTimeout(() => reject(new Error('Timeout')), ms)
    );
}

Promise.race([
    fetch('/api/data'),
    timeout(3000)
])
    .then(response => response.json())
    .catch(error => console.error(error));
```

### 9.6.5. Promise.allSettled()

Chờ tất cả promises settle (resolved or rejected):

```javascript
const promises = [
    Promise.resolve('Success'),
    Promise.reject('Error'),
    Promise.resolve('Another success')
];

Promise.allSettled(promises)
    .then(results => {
        results.forEach(result => {
            if (result.status === 'fulfilled') {
                console.log('Value:', result.value);
            } else {
                console.log('Reason:', result.reason);
            }
        });
    });
```

### 9.6.6. Promise.any()

Trả về promise fulfilled đầu tiên:

```javascript
const promises = [
    Promise.reject('Error 1'),
    Promise.resolve('Success'),
    Promise.reject('Error 2')
];

Promise.any(promises)
    .then(value => {
        console.log(value);  // "Success"
    })
    .catch(error => {
        console.error('All rejected');
    });
```

## 9.7. Error Handling

### 9.7.1. Try-Catch in Promises

```javascript
const promise = new Promise((resolve, reject) => {
    try {
        // Code that might throw
        const result = riskyOperation();
        resolve(result);
    } catch (error) {
        reject(error);
    }
});
```

### 9.7.2. Catching Errors

```javascript
promise
    .then(value => {
        // Process value
        if (!value) {
            throw new Error('No value');
        }
        return value;
    })
    .catch(error => {
        console.error('Error:', error.message);
        // Can recover from error
        return defaultValue;
    })
    .then(value => {
        // Continues with recovered value
    });
```

## 9.8. Practical Examples

### 9.8.1. Fetch API

```javascript
fetch('/api/users')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Users:', data);
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });
```

### 9.8.2. Sequential Requests

```javascript
function fetchUserPosts(userId) {
    return fetch(`/api/users/${userId}`)
        .then(response => response.json())
        .then(user => {
            console.log('User:', user);
            return fetch(`/api/users/${userId}/posts`);
        })
        .then(response => response.json())
        .then(posts => {
            console.log('Posts:', posts);
            return posts;
        });
}
```

### 9.8.3. Parallel Requests

```javascript
function fetchAllData() {
    return Promise.all([
        fetch('/api/users').then(r => r.json()),
        fetch('/api/posts').then(r => r.json()),
        fetch('/api/comments').then(r => r.json())
    ]);
}

fetchAllData()
    .then(([users, posts, comments]) => {
        console.log({ users, posts, comments });
    });
```

### 9.8.4. Retry Logic

```javascript
function fetchWithRetry(url, retries = 3) {
    return fetch(url)
        .catch(error => {
            if (retries > 0) {
                console.log(`Retrying... (${retries} left)`);
                return fetchWithRetry(url, retries - 1);
            }
            throw error;
        });
}
```

## 9.9. Use Cases Thực Tế

### Use Case 1: API Call with Loading State

```javascript
// Real-world API integration
class DataService {
    constructor() {
        this.isLoading = false;
        this.error = null;
        this.data = null;
    }

    fetchData(url) {
        this.isLoading = true;
        this.error = null;

        return fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                this.data = data;
                return data;
            })
            .catch(error => {
                this.error = error.message;
                throw error;
            })
            .finally(() => {
                this.isLoading = false;
            });
    }
}

// Usage
const service = new DataService();
service.fetchData('/api/users')
    .then(users => console.log('Users:', users))
    .catch(error => console.error('Error:', error));
```

### Use Case 2: Async Form Submission

```javascript
// Form validation and API submission
class FormHandler {
    constructor(formElement) {
        this.form = formElement;
        this.submitButton = formElement.querySelector('button[type="submit"]');
        this.setupListeners();
    }

    setupListeners() {
        this.form.addEventListener('submit', e => {
            e.preventDefault();
            this.submit();
        });
    }

    validate(data) {
        const errors = [];
        if (!data.email) errors.push('Email is required');
        if (!data.password) errors.push('Password is required');
        if (data.password?.length < 6) errors.push('Password too short');
        return { valid: errors.length === 0, errors };
    }

    submit() {
        const formData = new FormData(this.form);
        const data = Object.fromEntries(formData);

        const validation = this.validate(data);
        if (!validation.valid) {
            alert(validation.errors.join('\n'));
            return;
        }

        this.submitButton.disabled = true;
        this.submitButton.textContent = 'Submitting...';

        fetch('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
            .then(response => {
                if (!response.ok) throw new Error('Login failed');
                return response.json();
            })
            .then(result => {
                localStorage.setItem('token', result.token);
                window.location.href = '/dashboard';
            })
            .catch(error => {
                alert('Error: ' + error.message);
            })
            .finally(() => {
                this.submitButton.disabled = false;
                this.submitButton.textContent = 'Login';
            });
    }
}
```

### Use Case 3: Timeout with Promise.race()

```javascript
// API call with timeout mechanism
function fetchWithTimeout(url, timeout = 5000) {
    const timeoutPromise = new Promise((_, reject) =>
        setTimeout(() => reject(new Error('Request timeout')), timeout)
    );

    return Promise.race([
        fetch(url).then(r => r.json()),
        timeoutPromise
    ]);
}

// Usage
fetchWithTimeout('/api/slow-endpoint', 3000)
    .then(data => console.log('Success:', data))
    .catch(error => {
        if (error.message === 'Request timeout') {
            console.error('API took too long');
        } else {
            console.error('Error:', error);
        }
    });
```

### Use Case 4: Multiple Data Sources with Fallback

```javascript
// Try multiple sources until one succeeds
class DataFetcher {
    constructor(sources) {
        this.sources = sources; // Array of API endpoints
    }

    fetchWithFallback() {
        if (this.sources.length === 0) {
            return Promise.reject(new Error('No data sources available'));
        }

        const [firstSource, ...restSources] = this.sources;

        return fetch(firstSource)
            .then(response => {
                if (!response.ok) throw new Error('Source failed');
                return response.json();
            })
            .catch(error => {
                console.warn(`Failed to fetch from ${firstSource}:`, error);

                if (restSources.length === 0) {
                    return Promise.reject(
                        new Error('All data sources failed')
                    );
                }

                const fetcher = new DataFetcher(restSources);
                return fetcher.fetchWithFallback();
            });
    }
}

// Usage
const fetcher = new DataFetcher([
    'https://api1.example.com/data',
    'https://api2.example.com/data',
    'https://api3.example.com/data'
]);

fetcher.fetchWithFallback()
    .then(data => console.log('Data from available source:', data))
    .catch(error => console.error('All sources unavailable:', error));
```

### Use Case 5: Batch Processing with Concurrency Control

```javascript
// Process multiple items with controlled concurrency
class BatchProcessor {
    constructor(concurrency = 3) {
        this.concurrency = concurrency;
        this.queue = [];
        this.running = 0;
    }

    async process(items, processor) {
        this.queue = [...items];
        const results = [];

        const worker = () => {
            if (this.queue.length === 0) {
                if (this.running === 0) {
                    return Promise.resolve();
                }
                return new Promise(resolve => {
                    setTimeout(() => worker().then(resolve), 100);
                });
            }

            const item = this.queue.shift();
            this.running++;

            return Promise.resolve()
                .then(() => processor(item))
                .then(result => {
                    results.push(result);
                    this.running--;
                    return worker();
                });
        };

        const workers = Array(this.concurrency)
            .fill(null)
            .map(() => worker());

        await Promise.all(workers);
        return results;
    }
}

// Usage
const processor = new BatchProcessor(3); // 3 concurrent requests
const items = Array.from({ length: 10 }, (_, i) => i + 1);

processor.process(items, async (id) => {
    const response = await fetch(`/api/process/${id}`);
    return response.json();
})
    .then(results => console.log('All processed:', results))
    .catch(error => console.error('Processing failed:', error));
```

## 9.10. Tips & Tricks

### Tip 1: Promise Chaining Best Practices

```javascript
// Always return promises in .then()
const good = promise
    .then(data => {
        return fetch(`/api/${data.id}`);  // Returns promise
    })
    .then(response => response.json());

// Bad: Nested promises
const bad = promise
    .then(data => {
        fetch(`/api/${data.id}`)  // Doesn't return
            .then(response => response.json());
    });
```

### Tip 2: Error Recovery with .catch()

```javascript
// Recover from specific errors
fetch('/api/data')
    .then(r => r.json())
    .catch(error => {
        if (error instanceof SyntaxError) {
            console.log('Invalid JSON');
            return { fallback: true };
        }
        throw error;  // Re-throw if unexpected
    })
    .then(data => {
        console.log('Data:', data);
    });
```

### Tip 3: Finally for Cleanup

```javascript
// Use finally for cleanup operations
let isLoading = true;

fetch('/api/data')
    .then(r => r.json())
    .catch(e => console.error(e))
    .finally(() => {
        isLoading = false;  // Cleanup happens regardless
        updateUI();
    });
```

### Tip 4: Promise.all vs Promise.allSettled

```javascript
// Use all() when you need all to succeed
Promise.all([fetch(...), fetch(...)])
    .then(responses => console.log('All good'))
    .catch(() => console.log('One failed'));

// Use allSettled() when you need all results
Promise.allSettled([fetch(...), fetch(...)])
    .then(results => {
        const successful = results
            .filter(r => r.status === 'fulfilled')
            .map(r => r.value);
        const failed = results
            .filter(r => r.status === 'rejected')
            .map(r => r.reason);
    });
```

### Tip 5: Promise.any() for Fastest Success

```javascript
// Race multiple sources, return first success
Promise.any([
    fetch('https://api1.com/data'),
    fetch('https://api2.com/data'),
    fetch('https://api3.com/data')
])
    .then(response => console.log('Got response from one source'))
    .catch(() => console.log('All sources failed'));
```

### Tip 6: Delay Promises

```javascript
// Create a delay helper
const delay = (ms) => new Promise(resolve =>
    setTimeout(resolve, ms)
);

// Usage
Promise.resolve('start')
    .then(val => delay(1000).then(() => val))
    .then(val => console.log(val));

// Or with async/await
async function withDelay() {
    console.log('start');
    await delay(1000);
    console.log('after 1 second');
}
```

### Tip 7: Promise Composition

```javascript
// Compose multiple async operations
const compose = (...fns) => (value) =>
    fns.reduce((promise, fn) =>
        promise.then(fn),
        Promise.resolve(value)
    );

const fetchUser = id => fetch(`/api/users/${id}`).then(r => r.json());
const fetchUserPosts = user => fetch(`/api/users/${user.id}/posts`).then(r => r.json());
const filterPublicPosts = posts => posts.filter(p => !p.private);

const getUserPublicPosts = compose(
    fetchUser,
    fetchUserPosts,
    filterPublicPosts
);

getUserPublicPosts(123)
    .then(posts => console.log('Public posts:', posts));
```

### Tip 8: Promise Timeout Helper

```javascript
// Add timeout to any promise
const withTimeout = (promise, ms) =>
    Promise.race([
        promise,
        new Promise((_, reject) =>
            setTimeout(() => reject(new Error('Timeout')), ms)
        )
    ]);

// Usage
withTimeout(fetch('/api/data'), 5000)
    .catch(e => e.message === 'Timeout'
        ? console.log('Too slow')
        : console.error(e)
    );
```

### Tip 9: Promise.all with Map

```javascript
// Common pattern: fetch multiple items
const ids = [1, 2, 3, 4, 5];

Promise.all(
    ids.map(id => fetch(`/api/users/${id}`).then(r => r.json()))
)
    .then(users => console.log('All users:', users));

// With error handling per item
Promise.allSettled(
    ids.map(id =>
        fetch(`/api/users/${id}`)
            .then(r => r.json())
            .catch(e => ({ error: e, id }))
    )
)
    .then(results => {
        const successful = results
            .filter(r => r.status === 'fulfilled' && !r.value.error)
            .map(r => r.value);
        console.log('Valid users:', successful);
    });
```

### Tip 10: Promise Chaining with Array Methods

```javascript
// Process array items sequentially
const items = [1, 2, 3, 4, 5];

items.reduce((promise, item) =>
    promise.then(() => {
        console.log(`Processing ${item}`);
        return new Promise(resolve =>
            setTimeout(resolve, 1000)
        );
    }),
    Promise.resolve()
)
    .then(() => console.log('All processed'));
```

## 9.11. Common Mistakes

### Mistake 1: Swallowing Errors

```javascript
// BAD: Error silently ignored
promise
    .then(result => {
        // Error here disappears!
        doSomething(result.unknownProp.value);
    })
    .then(result => {
        // Never executes if error occurred
    });

// GOOD: Always catch
promise
    .then(result => {
        return doSomething(result.unknownProp?.value);
    })
    .catch(error => {
        console.error('Error:', error);
    });
```

### Mistake 2: Nested Promises (Pyramid of Doom)

```javascript
// BAD: Deeply nested
promise
    .then(result => {
        return new Promise(resolve => {
            doSomething(result, () => {
                doAnotherThing(result, () => {
                    doMore(result, () => {
                        resolve(result);
                    });
                });
            });
        });
    });

// GOOD: Flat chain
promise
    .then(result => doSomething(result))
    .then(result => doAnotherThing(result))
    .then(result => doMore(result));
```

### Mistake 3: Not Returning from .then()

```javascript
// BAD: Breaking the chain
fetch('/api/user')
    .then(r => r.json())
    .then(user => {
        console.log(user);
        // Forgot to return!
    })
    .then(result => {
        console.log(result);  // undefined
    });

// GOOD: Always return
fetch('/api/user')
    .then(r => r.json())
    .then(user => {
        console.log(user);
        return user;  // Return value
    })
    .then(result => {
        console.log(result);  // User object
    });
```

### Mistake 4: Handling Same Error Multiple Times

```javascript
// BAD: Error handled twice
promise
    .then(result => doSomething(result))
    .catch(error => {
        console.error('Error:', error);
        return defaultValue;  // Continues chain
    })
    .catch(error => {
        // This catch never triggers for the first error!
    });

// GOOD: Single catch point
promise
    .then(result => doSomething(result))
    .catch(error => {
        console.error('Error:', error);
        return defaultValue;
    });
```

### Mistake 5: Using Promise in Loop Incorrectly

```javascript
// BAD: Parallel when should be sequential
const ids = [1, 2, 3];
const results = [];

ids.forEach(id => {
    fetch(`/api/${id}`)
        .then(r => r.json())
        .then(data => results.push(data));
});

// Results order is unpredictable

// GOOD: Sequential with .reduce()
ids.reduce((promise, id) =>
    promise.then(() =>
        fetch(`/api/${id}`)
            .then(r => r.json())
            .then(data => results.push(data))
    ),
    Promise.resolve()
);
```

### Mistake 6: Missing Error Handling

```javascript
// BAD: No error handling
fetch('/api/data').then(r => r.json());

// GOOD: Handle errors
fetch('/api/data')
    .then(r => {
        if (!r.ok) throw new Error('Response failed');
        return r.json();
    })
    .catch(e => console.error('Error:', e));
```

### Mistake 7: Not Handling .catch() Return

```javascript
// BAD: Unclear state after error
promise
    .catch(e => {
        console.error(e);
        // What do we return?
    })
    .then(result => {
        // Could be undefined or error object
    });

// GOOD: Explicit error handling
promise
    .catch(e => {
        console.error(e);
        return null;  // Or throw again
    })
    .then(result => {
        if (result === null) {
            console.log('Operation failed');
        }
    });
```

### Mistake 8: Promise Constructor Anti-pattern

```javascript
// BAD: Promisifying without need
const bad = () => new Promise(resolve => {
    const result = calculateSomething();
    resolve(result);
});

// GOOD: Return promise directly
const good = () => Promise.resolve(calculateSomething());

// BAD: Unnecessary constructor
new Promise((resolve, reject) => {
    otherPromise
        .then(resolve)
        .catch(reject);
});

// GOOD: Return directly
function good() {
    return otherPromise;
}
```

### Mistake 9: Mixing Callbacks and Promises

```javascript
// BAD: Confusing mix
function getData(callback) {
    return fetch('/api/data')
        .then(r => r.json())
        .then(data => {
            callback(data);  // Also calls callback
            return data;     // And returns promise
        });
}

// GOOD: One pattern only
function getData() {
    return fetch('/api/data').then(r => r.json());
}

// Usage
getData().then(data => console.log(data));
```

### Mistake 10: Promise.all() and Single Failure

```javascript
// BAD: Don't know which failed
Promise.all([
    fetch('/api/1'),
    fetch('/api/2'),
    fetch('/api/3')
])
    .catch(error => {
        // Which endpoint failed?
        console.error('Unknown:', error);
    });

// GOOD: Wrap with metadata
Promise.all([
    fetch('/api/1').catch(e => ({ error: true, endpoint: 1, reason: e })),
    fetch('/api/2').catch(e => ({ error: true, endpoint: 2, reason: e })),
    fetch('/api/3').catch(e => ({ error: true, endpoint: 3, reason: e }))
])
    .then(results => {
        const errors = results.filter(r => r.error);
        if (errors.length > 0) {
            console.error('Failed endpoints:', errors);
        }
    });
```

## 9.12. Troubleshooting Issues

### Issue 1: Promise Stays Pending

**Problem:**
```javascript
const promise = new Promise((resolve, reject) => {
    // Forgot to call resolve or reject!
});

promise.then(r => console.log('Done'));  // Never executes
```

**Solution:**
```javascript
const promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve('Done'), 1000);
});

promise.then(r => console.log(r));
```

### Issue 2: Unhandled Promise Rejection

**Problem:**
```javascript
Promise.reject(new Error('Something failed'));
// UnhandledPromiseRejectionWarning
```

**Solution:**
```javascript
Promise.reject(new Error('Something failed'))
    .catch(error => console.error('Handled:', error));

// Or add global handler
window.addEventListener('unhandledrejection', event => {
    console.error('Unhandled rejection:', event.reason);
});
```

### Issue 3: Promise Chain Breaks Silently

**Problem:**
```javascript
fetch('/api/users')
    .then(r => r.json())
    .then(users => {
        const user = users.find(u => u.id === 1);
        console.log(user.name);  // Error if not found
    })
    .then(() => console.log('Done'));  // May not execute
```

**Solution:**
```javascript
fetch('/api/users')
    .then(r => r.json())
    .then(users => {
        const user = users.find(u => u.id === 1);
        if (!user) throw new Error('User not found');
        return user.name;
    })
    .then(name => console.log('User:', name))
    .catch(error => console.error('Error:', error));
```

### Issue 4: Race Condition with Data

**Problem:**
```javascript
let latestData = null;

function fetchData() {
    return fetch('/api/data').then(r => r.json());
}

function updateUI() {
    fetchData().then(data => {
        latestData = data;  // Which request completed last?
    });
}

updateUI();
updateUI();  // Called twice
updateUI();  // Race condition!
```

**Solution:**
```javascript
class DataManager {
    constructor() {
        this.requestId = 0;
        this.latestData = null;
    }

    fetchData() {
        const id = ++this.requestId;

        return fetch('/api/data')
            .then(r => r.json())
            .then(data => {
                if (id === this.requestId) {
                    this.latestData = data;
                    return data;
                }
                throw new Error('Superseded');
            });
    }
}
```

### Issue 5: Memory Leaks with Promises

**Problem:**
```javascript
function attachListeners() {
    element.addEventListener('click', () => {
        fetch('/api/data')
            .then(r => r.json())
            .then(data => {
                // Captured 'element' in closure
                element.textContent = data.value;
            });
    });
}

// If element is removed, promise still holds reference
```

**Solution:**
```javascript
class Component {
    constructor(element) {
        this.element = element;
        this.setupListeners();
    }

    setupListeners() {
        this.handleClick = () => this.onClick();
        this.element.addEventListener('click', this.handleClick);
    }

    onClick() {
        if (!this.element.parentElement) {
            return;  // Element already removed
        }

        fetch('/api/data')
            .then(r => r.json())
            .then(data => {
                if (this.element?.parentElement) {
                    this.element.textContent = data.value;
                }
            });
    }

    destroy() {
        this.element.removeEventListener('click', this.handleClick);
        this.element = null;
    }
}
```

### Issue 6: Timeout Implementation Wrong

**Problem:**
```javascript
// BAD: Still executes after timeout
const timeoutPromise = new Promise((_, reject) =>
    setTimeout(() => reject(new Error('Timeout')), 1000)
);

Promise.race([
    fetch('/api/slow'),
    timeoutPromise
])
    .then(r => r.json())  // Still sends request
    .then(data => console.log(data));
```

**Solution:**
```javascript
const withAbort = async (promise, ms) => {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), ms);

    try {
        return await promise;
    } finally {
        clearTimeout(timeout);
    }
};

// Usage with fetch
fetch('/api/data', { signal: controller.signal })
    .then(r => r.json())
    .catch(e => e.name === 'AbortError'
        ? console.log('Cancelled')
        : console.error(e)
    );
```

### Issue 7: Testing Promise Code

**Problem:**
```javascript
// Test doesn't wait for promise
it('fetches data', () => {
    const promise = fetch('/api/data').then(r => r.json());
    // Test ends before promise resolves
});
```

**Solution:**
```javascript
// Return promise from test
it('fetches data', () => {
    return fetch('/api/data')
        .then(r => r.json())
        .then(data => {
            expect(data).toBeDefined();
        });
});

// Or with async/await
it('fetches data', async () => {
    const data = await fetch('/api/data').then(r => r.json());
    expect(data).toBeDefined();
});
```

### Issue 8: Promise.all() vs forEach

**Problem:**
```javascript
// BAD: Requests sequential instead of parallel
const results = [];
const ids = [1, 2, 3];

ids.forEach(id => {
    fetch(`/api/${id}`)
        .then(r => r.json())
        .then(data => results.push(data));
});

// Doesn't wait for completion
```

**Solution:**
```javascript
// GOOD: Parallel requests
const ids = [1, 2, 3];

Promise.all(
    ids.map(id =>
        fetch(`/api/${id}`).then(r => r.json())
    )
)
    .then(results => console.log(results));
```

### Issue 9: Error Type Checking

**Problem:**
```javascript
fetch('/api/data')
    .catch(error => {
        // Don't know what type of error
        console.error('Failed:', error);
    });
```

**Solution:**
```javascript
fetch('/api/data')
    .catch(error => {
        if (error instanceof TypeError) {
            console.error('Network error:', error);
        } else if (error instanceof SyntaxError) {
            console.error('Invalid JSON:', error);
        } else if (error instanceof Error) {
            console.error('HTTP error:', error);
        }
    });
```

### Issue 10: Promise Context (this)

**Problem:**
```javascript
class User {
    name = 'John';

    fetchData() {
        fetch('/api/data')
            .then(r => r.json())
            .then(data => {
                console.log(this.name);  // undefined!
            });
    }
}

new User().fetchData();
```

**Solution:**
```javascript
class User {
    name = 'John';

    fetchData() {
        fetch('/api/data')
            .then(r => r.json())
            .then(data => {
                console.log(this.name);  // 'John'
            });
    }
}

// Or use arrow function in constructor
class User {
    constructor() {
        this.name = 'John';
    }

    fetchData = () => {
        fetch('/api/data')
            .then(r => r.json())
            .then(data => {
                console.log(this.name);  // 'John'
            });
    };
}
```

## 9.13. Advanced Topics

### 9.13.1. Custom Promise Implementation

```javascript
// Simplified promise implementation
class MyPromise {
    constructor(fn) {
        this.state = 'pending';
        this.value = undefined;
        this.reason = undefined;
        this.handlers = [];

        try {
            fn(
                (value) => this.resolve(value),
                (reason) => this.reject(reason)
            );
        } catch (error) {
            this.reject(error);
        }
    }

    resolve(value) {
        if (this.state !== 'pending') return;
        this.state = 'fulfilled';
        this.value = value;
        this.handlers.forEach(h => h());
    }

    reject(reason) {
        if (this.state !== 'pending') return;
        this.state = 'rejected';
        this.reason = reason;
        this.handlers.forEach(h => h());
    }

    then(onFulfilled, onRejected) {
        return new MyPromise((resolve, reject) => {
            const handler = () => {
                try {
                    if (this.state === 'fulfilled') {
                        const value = onFulfilled(this.value);
                        resolve(value);
                    } else if (this.state === 'rejected') {
                        const reason = onRejected(this.reason);
                        resolve(reason);
                    }
                } catch (error) {
                    reject(error);
                }
            };

            if (this.state === 'pending') {
                this.handlers.push(handler);
            } else {
                handler();
            }
        });
    }
}
```

### 9.13.2. Promise Pool with Concurrency

```javascript
// Advanced: Process items with controlled concurrency
class PromisePool {
    constructor(concurrency) {
        this.concurrency = concurrency;
        this.executing = [];
        this.queue = [];
    }

    add(fn) {
        return new Promise((resolve, reject) => {
            this.queue.push({ fn, resolve, reject });
            this.process();
        });
    }

    async process() {
        while (this.executing.length < this.concurrency && this.queue.length > 0) {
            const { fn, resolve, reject } = this.queue.shift();

            const promise = Promise.resolve()
                .then(() => fn())
                .then(resolve, reject)
                .finally(() => {
                    this.executing.splice(
                        this.executing.indexOf(promise),
                        1
                    );
                    this.process();
                });

            this.executing.push(promise);
        }
    }
}

// Usage
const pool = new PromisePool(3);
const items = Array.from({ length: 10 }, (_, i) => i + 1);

Promise.all(
    items.map(item =>
        pool.add(() => fetch(`/api/${item}`).then(r => r.json()))
    )
)
    .then(results => console.log('All results:', results));
```

### 9.13.3. Promise Middleware Pattern

```javascript
// Create middleware chain for promises
class PromiseChain {
    constructor() {
        this.middlewares = [];
    }

    use(middleware) {
        this.middlewares.push(middleware);
        return this;
    }

    async execute(initial) {
        let value = initial;

        for (const middleware of this.middlewares) {
            value = await middleware(value);
        }

        return value;
    }
}

// Usage
const chain = new PromiseChain();

chain
    .use(async (data) => {
        console.log('Step 1:', data);
        return data + 1;
    })
    .use(async (data) => {
        console.log('Step 2:', data);
        return data * 2;
    })
    .use(async (data) => {
        console.log('Step 3:', data);
        return data - 5;
    });

chain.execute(10)
    .then(result => console.log('Final:', result));
```

### 9.13.4. Promise Retry with Exponential Backoff

```javascript
// Advanced retry logic with exponential backoff
async function retryWithBackoff(fn, options = {}) {
    const {
        maxRetries = 3,
        initialDelay = 1000,
        maxDelay = 10000,
        backoffMultiplier = 2,
        shouldRetry = () => true
    } = options;

    let lastError;
    let delay = initialDelay;

    for (let attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            return await fn();
        } catch (error) {
            lastError = error;

            if (attempt === maxRetries || !shouldRetry(error)) {
                throw error;
            }

            await new Promise(resolve => setTimeout(resolve, delay));
            delay = Math.min(delay * backoffMultiplier, maxDelay);
        }
    }

    throw lastError;
}

// Usage
retryWithBackoff(
    () => fetch('/api/flaky-endpoint'),
    {
        maxRetries: 5,
        initialDelay: 1000,
        shouldRetry: (error) => {
            // Only retry on network errors, not 4xx
            return error instanceof TypeError ||
                   error.status >= 500;
        }
    }
)
    .then(r => r.json())
    .catch(e => console.error('Failed after retries:', e));
```

### 9.13.5. Promise Debounce and Throttle

```javascript
// Debounce promises - only execute latest request
function debouncePromise(fn, delay) {
    let timeoutId;
    let lastPromise;

    return (...args) => {
        clearTimeout(timeoutId);

        return new Promise((resolve, reject) => {
            timeoutId = setTimeout(() => {
                lastPromise = Promise.resolve()
                    .then(() => fn(...args))
                    .then(resolve, reject);
            }, delay);
        });
    };
}

// Usage
const debouncedSearch = debouncePromise(
    (query) => fetch(`/api/search?q=${query}`).then(r => r.json()),
    300
);

input.addEventListener('input', (e) => {
    debouncedSearch(e.target.value)
        .then(results => console.log('Search results:', results));
});

// Throttle promises - limit request frequency
function throttlePromise(fn, delay) {
    let lastCall = 0;
    let timeout;

    return (...args) => {
        return new Promise((resolve, reject) => {
            const now = Date.now();

            const execute = () => {
                lastCall = Date.now();
                Promise.resolve()
                    .then(() => fn(...args))
                    .then(resolve, reject);
            };

            if (now - lastCall >= delay) {
                execute();
            } else {
                clearTimeout(timeout);
                timeout = setTimeout(execute, delay - (now - lastCall));
            }
        });
    };
}
```

## 9.14. Best Practices

### 9.14.1. Always Handle Errors

```javascript
// DO: Handle errors
promise
    .then(result => console.log(result))
    .catch(error => console.error(error));

// DON'T: Ignore errors
promise.then(result => console.log(result));
```

### 9.14.2. Return Promises

```javascript
// DO: Return promises
promise.then(value => {
    return doSomething(value);
});

// DON'T: Don't return
promise.then(value => {
    doSomething(value);
});
```

### 9.14.3. Avoid Nesting

```javascript
// DO: Flat chain
promise1
    .then(value1 => promise2)
    .then(value2 => promise3)
    .then(value3 => console.log(value3));

// DON'T: Nested
promise1.then(value1 => {
    promise2.then(value2 => {
        promise3.then(value3 => console.log(value3));
    });
});
```

## 9.15. Exercises

### Exercise 1 (Dễ): Basic Promise

```javascript
// Tạo một promise resolve sau 2 giây với message "Done"
// In kết quả ra console
```

### Exercise 2 (Dễ): Promise Chain

```javascript
// Tạo 3 promises: thêm 1, nhân 2, trừ 5
// Chain chúng lại với nhau
// Bắt đầu với giá trị 10
```

### Exercise 3 (Dễ): Promise.all

```javascript
// Tạo 3 promises resolve sau 1, 2, 3 giây
// Dùng Promise.all để chờ tất cả
// In kết quả
```

### Exercise 4 (Dễ): Error Handling

```javascript
// Tạo promise reject với error
// Catch error và xử lý nó
```

### Exercise 5 (Trung bình): Fetch Data

```javascript
// Viết hàm fetchUser(id) sử dụng fetch API
// Trả về user data
// Handle errors appropriately
```

### Exercise 6 (Trung bình): Sequential Requests

```javascript
// Fetch user, sau đó fetch posts của user đó
// Chain requests
// Return combined data
```

### Exercise 7 (Trung bình): Parallel Requests

```javascript
// Fetch users, posts, comments cùng lúc
// Dùng Promise.all
// Return kết quả
```

### Exercise 8 (Trung bình): Retry Logic

```javascript
// Viết hàm fetchWithRetry(url, maxRetries)
// Retry khi fail
// Bỏ qua nếu vượt quá maxRetries
```

### Exercise 9 (Khó): Promise Pool

```javascript
// Implement class PromisePool(concurrency)
// Xử lý multiple operations với limited concurrency
// Ví dụ: 10 requests nhưng chỉ 3 parallel
```

### Exercise 10 (Khó): Custom Promise

```javascript
// Implement simplified Promise class
// Support resolve(), reject(), then()
// Handle promise chaining
```

### Exercise 11 (Khó): Timeout with Race

```javascript
// Tạo fetchWithTimeout(url, ms)
// Reject nếu vượt quá time limit
// Dùng Promise.race
```

### Exercise 12 (Khó): Error Recovery

```javascript
// Fetch từ multiple sources
// Return kết quả từ source đầu tiên thành công
// Implement fallback logic
```

---

**Kết luận:** Promises là foundation của async JavaScript. Hiểu rõ promise states, chaining, error handling, và best practices. Chương tiếp theo sẽ học về Async/Await - syntax sugar cho Promises.
