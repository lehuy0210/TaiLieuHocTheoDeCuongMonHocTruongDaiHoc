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

## 9.9. Best Practices

### 9.9.1. Always Handle Errors

```javascript
// BAD
fetch('/api/data')
    .then(response => response.json());

// GOOD
fetch('/api/data')
    .then(response => response.json())
    .catch(error => console.error(error));
```

### 9.9.2. Return Promises

```javascript
// BAD
promise.then(value => {
    doSomething(value);  // Doesn't return
});

// GOOD
promise.then(value => {
    return doSomething(value);
});
```

### 9.9.3. Avoid Nesting

```javascript
// BAD (pyramid of doom)
promise1.then(value1 => {
    promise2.then(value2 => {
        promise3.then(value3 => {
            // ...
        });
    });
});

// GOOD (flat chain)
promise1
    .then(value1 => promise2)
    .then(value2 => promise3)
    .then(value3 => {
        // ...
    });
```

---

**Kết luận:** Promises giúp xử lý async code dễ đọc và maintain hơn. Chương tiếp theo sẽ học về Async/Await - syntax sugar cho Promises.
