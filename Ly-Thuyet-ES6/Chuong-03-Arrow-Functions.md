# CHƯƠNG 3: ARROW FUNCTIONS

## 3.1. Giới thiệu Arrow Functions

Arrow functions là cú pháp ngắn gọn hơn cho function expressions.

### 3.1.1. Syntax

**ES5:**
```javascript
var add = function(a, b) {
    return a + b;
};
```

**ES6:**
```javascript
const add = (a, b) => {
    return a + b;
};

// Implicit return (1 expression)
const add = (a, b) => a + b;
```

## 3.2. Syntax Variations

### 3.2.1. No Parameters

```javascript
// ES5
var greet = function() {
    return 'Hello';
};

// ES6
const greet = () => 'Hello';
```

### 3.2.2. One Parameter

```javascript
// Có thể bỏ parentheses
const double = n => n * 2;

// Hoặc giữ parentheses (recommended)
const double = (n) => n * 2;
```

### 3.2.3. Multiple Parameters

```javascript
const add = (a, b) => a + b;

const fullName = (first, last) => `${first} ${last}`;
```

### 3.2.4. Multiple Statements

```javascript
const calculate = (a, b) => {
    const sum = a + b;
    const product = a * b;
    return { sum, product };
};
```

### 3.2.5. Returning Object Literals

```javascript
// Wrap in parentheses
const makeUser = (name, age) => ({ name, age });

// NOT this (interpreted as function body)
const makeUser = (name, age) => { name, age };  // ERROR
```

## 3.3. this Binding

### 3.3.1. Traditional Functions

```javascript
function Person() {
    this.age = 0;

    setInterval(function() {
        this.age++;  // 'this' refers to global/undefined
    }, 1000);
}

// Fix với .bind()
function Person() {
    this.age = 0;

    setInterval(function() {
        this.age++;
    }.bind(this), 1000);
}

// Fix với variable
function Person() {
    this.age = 0;
    var self = this;

    setInterval(function() {
        self.age++;
    }, 1000);
}
```

### 3.3.2. Arrow Functions

```javascript
// Arrow function inherits 'this'
function Person() {
    this.age = 0;

    setInterval(() => {
        this.age++;  // 'this' từ Person
    }, 1000);
}
```

### 3.3.3. Practical Example

```javascript
const team = {
    members: ['John', 'Jane'],
    teamName: 'Super Squad',

    // Traditional function
    printMembers() {
        this.members.forEach(function(member) {
            // 'this' is undefined here
            console.log(this.teamName + ': ' + member);  // ERROR
        });
    },

    // Arrow function
    printMembersArrow() {
        this.members.forEach(member => {
            // 'this' from team object
            console.log(`${this.teamName}: ${member}`);  // Works!
        });
    }
};
```

## 3.4. When NOT to Use Arrow Functions

### 3.4.1. Object Methods

```javascript
// BAD
const person = {
    name: 'John',
    greet: () => {
        console.log(`Hello, ${this.name}`);  // 'this' is undefined
    }
};

// GOOD
const person = {
    name: 'John',
    greet() {
        console.log(`Hello, ${this.name}`);
    }
};
```

### 3.4.2. Prototype Methods

```javascript
// BAD
Person.prototype.greet = () => {
    console.log(this.name);  // 'this' is undefined
};

// GOOD
Person.prototype.greet = function() {
    console.log(this.name);
};
```

### 3.4.3. Event Handlers (when need 'this')

```javascript
// BAD
button.addEventListener('click', () => {
    this.classList.toggle('active');  // 'this' is not the button
});

// GOOD
button.addEventListener('click', function() {
    this.classList.toggle('active');  // 'this' is the button
});
```

### 3.4.4. Constructors

```javascript
// Cannot use arrow function as constructor
const Person = (name) => {
    this.name = name;
};

const john = new Person('John');  // ERROR: not a constructor
```

## 3.5. Practical Examples

### 3.5.1. Array Methods

```javascript
const numbers = [1, 2, 3, 4, 5];

// map
const doubled = numbers.map(n => n * 2);

// filter
const evens = numbers.filter(n => n % 2 === 0);

// reduce
const sum = numbers.reduce((total, n) => total + n, 0);

// find
const firstEven = numbers.find(n => n % 2 === 0);

// sort
const sorted = numbers.sort((a, b) => b - a);
```

### 3.5.2. Promises

```javascript
fetch('/api/users')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
```

### 3.5.3. setTimeout/setInterval

```javascript
setTimeout(() => {
    console.log('Delayed message');
}, 1000);

const interval = setInterval(() => {
    console.log('Repeating message');
}, 1000);
```

### 3.5.4. Chaining

```javascript
const users = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 },
    { name: 'Bob', age: 35 }
];

const result = users
    .filter(user => user.age >= 30)
    .map(user => user.name)
    .join(', ');

console.log(result);  // "John, Bob"
```

## 3.6. Arguments Object

### 3.6.1. Traditional Functions

```javascript
function sum() {
    console.log(arguments);  // [1, 2, 3]
    return Array.from(arguments).reduce((a, b) => a + b);
}

sum(1, 2, 3);  // 6
```

### 3.6.2. Arrow Functions (no arguments)

```javascript
// Arrow functions don't have 'arguments'
const sum = () => {
    console.log(arguments);  // ReferenceError
};

// Use rest parameters instead
const sum = (...args) => {
    return args.reduce((a, b) => a + b);
};

sum(1, 2, 3);  // 6
```

## 3.7. Best Practices

### 3.7.1. Khi nào dùng Arrow Functions

**Use arrow functions for:**
- Callbacks
- Array methods
- Promises
- Short functions
- When you need lexical 'this'

**Use traditional functions for:**
- Object methods
- Prototype methods
- Constructors
- When you need 'arguments'
- When you need dynamic 'this'

### 3.7.2. Readability

```javascript
// Clear and concise
const double = n => n * 2;

// Too concise (less readable)
const complex = (a,b,c,d) => a+b>c?d:a;

// Better (more readable)
const complex = (a, b, c, d) => {
    return a + b > c ? d : a;
};
```

## 3.8. Advanced Practical Examples

### Example 1: Data Processing Pipeline

```javascript
// Complex data transformation with arrow functions
const users = [
    { id: 1, name: 'John Doe', age: 30, active: true, salary: 50000 },
    { id: 2, name: 'Jane Smith', age: 25, active: true, salary: 60000 },
    { id: 3, name: 'Bob Johnson', age: 35, active: false, salary: 55000 },
    { id: 4, name: 'Alice Brown', age: 28, active: true, salary: 65000 }
];

// Processing pipeline
const result = users
    .filter(user => user.active)
    .filter(user => user.age >= 28)
    .map(user => ({
        name: user.name,
        salary: user.salary,
        bonus: user.salary * 0.1
    }))
    .sort((a, b) => b.salary - a.salary)
    .map(user => `${user.name}: $${user.salary + user.bonus}`);

console.log(result);
// ["Alice Brown: $71500", "John Doe: $55000"]
```

### Example 2: Event Handling System

```javascript
// Event emitter using arrow functions
class EventEmitter {
    constructor() {
        this.events = {};
    }

    on(event, callback) {
        if (!this.events[event]) {
            this.events[event] = [];
        }
        this.events[event].push(callback);

        // Return unsubscribe function using arrow function
        return () => {
            this.events[event] = this.events[event].filter(cb => cb !== callback);
        };
    }

    emit(event, data) {
        if (!this.events[event]) return;

        // Using arrow functions for iteration
        this.events[event].forEach(callback => callback(data));
    }

    once(event, callback) {
        const onceCallback = (data) => {
            callback(data);
            this.off(event, onceCallback);
        };
        this.on(event, onceCallback);
    }

    off(event, callback) {
        if (!this.events[event]) return;
        this.events[event] = this.events[event].filter(cb => cb !== callback);
    }
}

// Usage
const emitter = new EventEmitter();

emitter.on('user:login', (user) => {
    console.log(`Welcome, ${user.name}!`);
});

emitter.on('user:login', (user) => {
    console.log(`Last login: ${user.lastLogin}`);
});

emitter.emit('user:login', { name: 'John', lastLogin: '2024-01-01' });
```

### Example 3: Async Operations with Arrow Functions

```javascript
// API service with arrow functions
class APIService {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    // Using arrow functions for async methods
    fetchUser = async (userId) => {
        try {
            const response = await fetch(`${this.baseURL}/users/${userId}`);
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching user:', error);
            throw error;
        }
    }

    fetchAllUsers = async () => {
        try {
            const response = await fetch(`${this.baseURL}/users`);
            const users = await response.json();

            // Process users with arrow functions
            return users
                .filter(user => user.active)
                .map(user => ({
                    id: user.id,
                    name: user.name,
                    email: user.email
                }));
        } catch (error) {
            console.error('Error fetching users:', error);
            throw error;
        }
    }

    // Parallel requests
    fetchUserWithPosts = async (userId) => {
        try {
            const [user, posts] = await Promise.all([
                this.fetchUser(userId),
                fetch(`${this.baseURL}/users/${userId}/posts`).then(r => r.json())
            ]);

            return {
                ...user,
                posts: posts.map(post => ({
                    id: post.id,
                    title: post.title
                }))
            };
        } catch (error) {
            console.error('Error:', error);
            throw error;
        }
    }
}

// Usage
const api = new APIService('https://jsonplaceholder.typicode.com');
api.fetchUser(1)
    .then(user => console.log('User:', user))
    .catch(err => console.error('Failed:', err));
```

### Example 4: Functional Programming Utilities

```javascript
// Utility functions using arrow functions

// Curry function
const curry = (fn) => {
    return function curried(...args) {
        if (args.length >= fn.length) {
            return fn(...args);
        }
        return (...nextArgs) => curried(...args, ...nextArgs);
    };
};

// Usage
const add = (a, b, c) => a + b + c;
const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3)); // 6
console.log(curriedAdd(1, 2)(3)); // 6

// Compose function
const compose = (...fns) => (value) =>
    fns.reduceRight((acc, fn) => fn(acc), value);

// Pipe function
const pipe = (...fns) => (value) =>
    fns.reduce((acc, fn) => fn(acc), value);

// Usage
const double = x => x * 2;
const addOne = x => x + 1;
const square = x => x * x;

const composedFn = compose(square, addOne, double);
console.log(composedFn(3)); // ((3 * 2) + 1)^2 = 49

const pipedFn = pipe(double, addOne, square);
console.log(pipedFn(3)); // ((3 * 2) + 1)^2 = 49

// Debounce with arrow function
const debounce = (fn, delay) => {
    let timeoutId;
    return (...args) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn(...args), delay);
    };
};

// Throttle with arrow function
const throttle = (fn, limit) => {
    let inThrottle;
    return (...args) => {
        if (!inThrottle) {
            fn(...args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
};

// Memoize function
const memoize = (fn) => {
    const cache = new Map();
    return (...args) => {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn(...args);
        cache.set(key, result);
        return result;
    };
};

// Usage
const fibonacci = memoize((n) => {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
});

console.log(fibonacci(10)); // 55
```

### Example 5: React Component Pattern

```javascript
// Functional React components with arrow functions

// Simple component
const Welcome = ({ name }) => (
    <div>
        <h1>Welcome, {name}!</h1>
    </div>
);

// Component with hooks
const UserProfile = ({ userId }) => {
    const [user, setUser] = React.useState(null);
    const [loading, setLoading] = React.useState(true);

    React.useEffect(() => {
        // Arrow function in useEffect
        const fetchUser = async () => {
            try {
                const response = await fetch(`/api/users/${userId}`);
                const data = await response.json();
                setUser(data);
            } catch (error) {
                console.error('Error:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchUser();
    }, [userId]);

    // Early returns with arrow functions
    if (loading) return <div>Loading...</div>;
    if (!user) return <div>User not found</div>;

    return (
        <div>
            <h2>{user.name}</h2>
            <p>{user.email}</p>
            <button onClick={() => console.log('Profile clicked')}>
                View Profile
            </button>
        </div>
    );
};

// Higher-order component
const withLoading = (Component) => ({ loading, ...props }) => {
    if (loading) return <div>Loading...</div>;
    return <Component {...props} />;
};

// Usage
const EnhancedUserProfile = withLoading(UserProfile);
```

### Example 6: State Management Pattern

```javascript
// Redux-style reducer with arrow functions
const createReducer = (initialState, handlers) => {
    return (state = initialState, action) => {
        const handler = handlers[action.type];
        return handler ? handler(state, action) : state;
    };
};

// User reducer
const userReducer = createReducer(
    { users: [], loading: false, error: null },
    {
        FETCH_USERS_REQUEST: (state) => ({
            ...state,
            loading: true,
            error: null
        }),
        FETCH_USERS_SUCCESS: (state, action) => ({
            ...state,
            loading: false,
            users: action.payload
        }),
        FETCH_USERS_FAILURE: (state, action) => ({
            ...state,
            loading: false,
            error: action.payload
        }),
        ADD_USER: (state, action) => ({
            ...state,
            users: [...state.users, action.payload]
        }),
        REMOVE_USER: (state, action) => ({
            ...state,
            users: state.users.filter(user => user.id !== action.payload)
        })
    }
);

// Action creators
const fetchUsersRequest = () => ({ type: 'FETCH_USERS_REQUEST' });
const fetchUsersSuccess = (users) => ({ type: 'FETCH_USERS_SUCCESS', payload: users });
const fetchUsersFailure = (error) => ({ type: 'FETCH_USERS_FAILURE', payload: error });
const addUser = (user) => ({ type: 'ADD_USER', payload: user });
const removeUser = (userId) => ({ type: 'REMOVE_USER', payload: userId });

// Thunk action creator
const fetchUsers = () => async (dispatch) => {
    dispatch(fetchUsersRequest());
    try {
        const response = await fetch('/api/users');
        const users = await response.json();
        dispatch(fetchUsersSuccess(users));
    } catch (error) {
        dispatch(fetchUsersFailure(error.message));
    }
};
```

### Example 7: Custom Array Methods

```javascript
// Extending Array prototype with arrow function concepts

const arrayUtils = {
    // Custom map
    customMap: (arr, fn) => {
        const result = [];
        for (let i = 0; i < arr.length; i++) {
            result.push(fn(arr[i], i, arr));
        }
        return result;
    },

    // Custom filter
    customFilter: (arr, fn) => {
        const result = [];
        for (let i = 0; i < arr.length; i++) {
            if (fn(arr[i], i, arr)) {
                result.push(arr[i]);
            }
        }
        return result;
    },

    // Custom reduce
    customReduce: (arr, fn, initial) => {
        let acc = initial;
        for (let i = 0; i < arr.length; i++) {
            acc = fn(acc, arr[i], i, arr);
        }
        return acc;
    },

    // Chunk array
    chunk: (arr, size) => {
        return Array.from({ length: Math.ceil(arr.length / size) }, (_, i) =>
            arr.slice(i * size, i * size + size)
        );
    },

    // Flatten array
    flatten: (arr) => arr.reduce((acc, val) =>
        Array.isArray(val) ? acc.concat(arrayUtils.flatten(val)) : acc.concat(val),
        []
    ),

    // Unique values
    unique: (arr) => [...new Set(arr)],

    // Group by
    groupBy: (arr, key) => arr.reduce((acc, item) => {
        const group = typeof key === 'function' ? key(item) : item[key];
        acc[group] = acc[group] || [];
        acc[group].push(item);
        return acc;
    }, {}),

    // Partition
    partition: (arr, predicate) => arr.reduce(
        ([pass, fail], item) =>
            predicate(item) ? [[...pass, item], fail] : [pass, [...fail, item]],
        [[], []]
    )
};

// Usage
const numbers = [1, 2, 3, 4, 5, 6];

console.log(arrayUtils.customMap(numbers, n => n * 2));
// [2, 4, 6, 8, 10, 12]

console.log(arrayUtils.chunk(numbers, 2));
// [[1, 2], [3, 4], [5, 6]]

const users = [
    { name: 'John', role: 'admin' },
    { name: 'Jane', role: 'user' },
    { name: 'Bob', role: 'admin' }
];

console.log(arrayUtils.groupBy(users, 'role'));
// { admin: [...], user: [...] }

const [evens, odds] = arrayUtils.partition(numbers, n => n % 2 === 0);
console.log(evens); // [2, 4, 6]
console.log(odds);  // [1, 3, 5]
```

## 3.9. Real-World Use Cases

### Use Case 1: Form Validation

```javascript
// Form validator using arrow functions
const createValidator = (rules) => (formData) => {
    const errors = {};

    Object.keys(rules).forEach(field => {
        const fieldRules = rules[field];
        const value = formData[field];

        fieldRules.forEach(rule => {
            const error = rule(value, formData);
            if (error) {
                errors[field] = errors[field] || [];
                errors[field].push(error);
            }
        });
    });

    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
};

// Validation rules
const required = (value) => !value ? 'This field is required' : null;
const email = (value) => !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) ? 'Invalid email' : null;
const minLength = (min) => (value) => value.length < min ? `Minimum ${min} characters` : null;
const matchField = (otherField) => (value, formData) =>
    value !== formData[otherField] ? 'Fields do not match' : null;

// Create validator
const validator = createValidator({
    username: [required, minLength(3)],
    email: [required, email],
    password: [required, minLength(8)],
    confirmPassword: [required, matchField('password')]
});

// Usage
const formData = {
    username: 'jo',
    email: 'invalid',
    password: '12345678',
    confirmPassword: '12345679'
};

const result = validator(formData);
console.log(result);
```

### Use Case 2: API Request Manager

```javascript
// Request manager with retry logic
class RequestManager {
    constructor(baseURL, maxRetries = 3) {
        this.baseURL = baseURL;
        this.maxRetries = maxRetries;
    }

    // Request with retry using arrow functions
    request = async (endpoint, options = {}) => {
        let attempt = 0;

        const makeRequest = async () => {
            try {
                const response = await fetch(`${this.baseURL}${endpoint}`, options);

                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}`);
                }

                return await response.json();
            } catch (error) {
                attempt++;

                if (attempt >= this.maxRetries) {
                    throw new Error(`Failed after ${this.maxRetries} attempts: ${error.message}`);
                }

                // Exponential backoff
                const delay = Math.pow(2, attempt) * 1000;
                await new Promise(resolve => setTimeout(resolve, delay));

                return makeRequest();
            }
        };

        return makeRequest();
    }

    // Convenience methods
    get = (endpoint) => this.request(endpoint);
    post = (endpoint, data) => this.request(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    put = (endpoint, data) => this.request(endpoint, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    delete = (endpoint) => this.request(endpoint, { method: 'DELETE' });
}

// Usage
const api = new RequestManager('https://api.example.com');

api.get('/users')
    .then(users => console.log('Users:', users))
    .catch(error => console.error('Error:', error));
```

### Use Case 3: Observable Pattern

```javascript
// Observable implementation using arrow functions
class Observable {
    constructor(subscribe) {
        this.subscribe = subscribe;
    }

    // Static creators
    static of = (...values) => new Observable(observer => {
        values.forEach(value => observer.next(value));
        observer.complete();
    });

    static from = (array) => new Observable(observer => {
        array.forEach(value => observer.next(value));
        observer.complete();
    });

    static interval = (period) => new Observable(observer => {
        let count = 0;
        const id = setInterval(() => observer.next(count++), period);
        return () => clearInterval(id);
    });

    // Operators
    map = (fn) => new Observable(observer => {
        return this.subscribe({
            next: (value) => observer.next(fn(value)),
            error: (err) => observer.error(err),
            complete: () => observer.complete()
        });
    });

    filter = (predicate) => new Observable(observer => {
        return this.subscribe({
            next: (value) => predicate(value) && observer.next(value),
            error: (err) => observer.error(err),
            complete: () => observer.complete()
        });
    });

    take = (count) => new Observable(observer => {
        let taken = 0;
        const subscription = this.subscribe({
            next: (value) => {
                if (taken < count) {
                    observer.next(value);
                    taken++;
                    if (taken === count) {
                        observer.complete();
                        subscription && subscription();
                    }
                }
            },
            error: (err) => observer.error(err),
            complete: () => observer.complete()
        });
        return subscription;
    });
}

// Usage
const numbers$ = Observable.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

numbers$
    .filter(x => x % 2 === 0)
    .map(x => x * 2)
    .subscribe({
        next: value => console.log(value),
        complete: () => console.log('Complete')
    });
// Output: 4, 8, 12, 16, 20, Complete
```

### Use Case 4: Middleware Pattern

```javascript
// Express-style middleware using arrow functions
class App {
    constructor() {
        this.middlewares = [];
    }

    use = (middleware) => {
        this.middlewares.push(middleware);
        return this;
    }

    execute = async (context) => {
        let index = 0;

        const next = async () => {
            if (index >= this.middlewares.length) return;

            const middleware = this.middlewares[index++];
            await middleware(context, next);
        };

        await next();
    }
}

// Middleware functions
const logger = async (ctx, next) => {
    console.log(`[${new Date().toISOString()}] ${ctx.method} ${ctx.url}`);
    await next();
};

const auth = async (ctx, next) => {
    if (!ctx.headers.authorization) {
        ctx.status = 401;
        ctx.body = { error: 'Unauthorized' };
        return;
    }
    await next();
};

const timer = async (ctx, next) => {
    const start = Date.now();
    await next();
    const duration = Date.now() - start;
    console.log(`Request took ${duration}ms`);
};

// Usage
const app = new App();

app.use(logger)
   .use(auth)
   .use(timer)
   .use(async (ctx) => {
       ctx.body = { message: 'Hello World' };
   });

// Execute
app.execute({
    method: 'GET',
    url: '/api/users',
    headers: { authorization: 'Bearer token' }
});
```

### Use Case 5: State Machine

```javascript
// Finite state machine using arrow functions
const createStateMachine = (initialState, transitions) => {
    let currentState = initialState;
    const listeners = [];

    return {
        getState: () => currentState,

        transition: (action) => {
            const transition = transitions[currentState]?.[action];

            if (!transition) {
                console.warn(`Invalid transition: ${action} from ${currentState}`);
                return currentState;
            }

            const nextState = transition.target;
            const beforeChange = transition.before;
            const afterChange = transition.after;

            // Before hook
            if (beforeChange) {
                beforeChange(currentState, nextState);
            }

            // Change state
            const previousState = currentState;
            currentState = nextState;

            // Notify listeners
            listeners.forEach(listener => listener(previousState, currentState));

            // After hook
            if (afterChange) {
                afterChange(previousState, currentState);
            }

            return currentState;
        },

        on: (listener) => {
            listeners.push(listener);
            return () => {
                const index = listeners.indexOf(listener);
                if (index > -1) listeners.splice(index, 1);
            };
        }
    };
};

// Traffic light state machine
const trafficLight = createStateMachine('red', {
    red: {
        next: {
            target: 'green',
            before: () => console.log('Red -> Green'),
            after: () => console.log('Now green')
        }
    },
    green: {
        next: {
            target: 'yellow',
            before: () => console.log('Green -> Yellow')
        }
    },
    yellow: {
        next: {
            target: 'red',
            before: () => console.log('Yellow -> Red')
        }
    }
});

// Listen to state changes
trafficLight.on((prev, next) => {
    console.log(`State changed: ${prev} -> ${next}`);
});

// Transitions
trafficLight.transition('next'); // red -> green
trafficLight.transition('next'); // green -> yellow
trafficLight.transition('next'); // yellow -> red
```

## 3.10. Tips & Tricks

### Tip 1: Implicit Return for Objects

```javascript
// Wrap object literals in parentheses
const makeUser = (name, age) => ({ name, age });

// Multi-line object
const makeUser = (name, age) => ({
    name,
    age,
    createdAt: new Date()
});
```

### Tip 2: Use Parentheses for Clarity

```javascript
// Less clear
const fn = x => y => z => x + y + z;

// More clear
const fn = (x) => (y) => (z) => x + y + z;
```

### Tip 3: Arrow Functions in Ternary

```javascript
// Concise conditional logic
const getDiscount = (price) =>
    price > 100 ? price * 0.2 : price * 0.1;

// With multiple conditions
const getShippingCost = (total) =>
    total > 100 ? 0 :
    total > 50 ? 5 :
    10;
```

### Tip 4: Destructuring in Parameters

```javascript
// Extract only what you need
const greet = ({ name, age }) =>
    `Hello, ${name}! You are ${age} years old.`;

// With default values
const greet = ({ name = 'Guest', age = 0 } = {}) =>
    `Hello, ${name}! You are ${age} years old.`;

// Array destructuring
const sum = ([a, b]) => a + b;
console.log(sum([5, 3])); // 8
```

### Tip 5: Immediately Invoked Arrow Functions

```javascript
// IIAFE - Immediately Invoked Arrow Function Expression
const result = ((x, y) => x + y)(5, 3);
console.log(result); // 8

// Async IIAFE
(async () => {
    const data = await fetchData();
    console.log(data);
})();
```

### Tip 6: Method Chaining

```javascript
const calculator = {
    value: 0,
    add: function(n) {
        this.value += n;
        return this;
    },
    subtract: function(n) {
        this.value -= n;
        return this;
    },
    multiply: function(n) {
        this.value *= n;
        return this;
    },
    getValue: function() {
        return this.value;
    }
};

const result = calculator
    .add(10)
    .multiply(2)
    .subtract(5)
    .getValue();
console.log(result); // 15
```

### Tip 7: Avoiding 'this' Issues in Callbacks

```javascript
class Timer {
    constructor() {
        this.seconds = 0;
    }

    start() {
        // Arrow function preserves 'this'
        setInterval(() => {
            this.seconds++;
            console.log(this.seconds);
        }, 1000);
    }
}

const timer = new Timer();
timer.start();
```

### Tip 8: Partial Application

```javascript
// Partial application using arrow functions
const add = (a) => (b) => a + b;

const add5 = add(5);
console.log(add5(3)); // 8
console.log(add5(10)); // 15

// More complex example
const multiply = (a) => (b) => (c) => a * b * c;

const double = multiply(2);
const doubleAndTriple = double(3);
console.log(doubleAndTriple(4)); // 24
```

### Tip 9: Arrow Functions with Default Parameters

```javascript
const greet = (name = 'Guest', greeting = 'Hello') =>
    `${greeting}, ${name}!`;

console.log(greet()); // "Hello, Guest!"
console.log(greet('John')); // "Hello, John!"
console.log(greet('Jane', 'Hi')); // "Hi, Jane!"
```

### Tip 10: Combining with Array Methods

```javascript
// Clean and readable data transformations
const products = [
    { name: 'Laptop', price: 1000, category: 'electronics' },
    { name: 'Phone', price: 500, category: 'electronics' },
    { name: 'Shirt', price: 30, category: 'clothing' }
];

const expensive = products
    .filter(p => p.price > 100)
    .map(p => ({ ...p, tax: p.price * 0.1 }))
    .map(p => ({ ...p, total: p.price + p.tax }));

console.log(expensive);
```

## 3.11. Common Mistakes

### Mistake 1: Using Arrow Functions as Methods

```javascript
// WRONG
const obj = {
    name: 'John',
    greet: () => {
        console.log(`Hello, ${this.name}`); // 'this' is undefined
    }
};

// CORRECT
const obj = {
    name: 'John',
    greet() {
        console.log(`Hello, ${this.name}`);
    }
};
```

### Mistake 2: Forgetting Parentheses for Object Returns

```javascript
// WRONG - returns undefined
const makeUser = (name) => { name };

// CORRECT
const makeUser = (name) => ({ name });
```

### Mistake 3: Using Arrow Functions as Constructors

```javascript
// WRONG
const Person = (name) => {
    this.name = name;
};

// new Person('John'); // TypeError

// CORRECT
function Person(name) {
    this.name = name;
}

// Or use class
class Person {
    constructor(name) {
        this.name = name;
    }
}
```

### Mistake 4: Expecting 'arguments' Object

```javascript
// WRONG
const sum = () => {
    return Array.from(arguments).reduce((a, b) => a + b);
};

// CORRECT - use rest parameters
const sum = (...args) => {
    return args.reduce((a, b) => a + b);
};
```

### Mistake 5: Breaking Method Chaining

```javascript
// WRONG - arrow function doesn't return 'this'
const calculator = {
    value: 0,
    add: (n) => {
        this.value += n;
        return this; // 'this' is not calculator
    }
};

// CORRECT
const calculator = {
    value: 0,
    add(n) {
        this.value += n;
        return this;
    }
};
```

### Mistake 6: Overusing Arrow Functions

```javascript
// WRONG - too terse, hard to read
const f = x => y => z => w => x + y + z + w;

// BETTER - more readable
const createAdder = (x) => {
    return (y) => {
        return (z) => {
            return (w) => {
                return x + y + z + w;
            };
        };
    };
};

// OR use traditional function for clarity
function createAdder(x) {
    return function(y) {
        return function(z) {
            return function(w) {
                return x + y + z + w;
            };
        };
    };
}
```

### Mistake 7: Event Handler Context

```javascript
// WRONG - loses button context
button.addEventListener('click', () => {
    this.classList.toggle('active'); // 'this' is not the button
});

// CORRECT - when you need the element
button.addEventListener('click', function() {
    this.classList.toggle('active');
});

// OR use event parameter
button.addEventListener('click', (e) => {
    e.currentTarget.classList.toggle('active');
});
```

### Mistake 8: Forgetting Return Statement

```javascript
// WRONG - no return
const double = (n) => {
    n * 2; // Missing return!
};

// CORRECT - implicit return
const double = (n) => n * 2;

// OR explicit return
const double = (n) => {
    return n * 2;
};
```

## 3.12. Troubleshooting

### Issue 1: 'this' is undefined

**Problem:**
```javascript
const obj = {
    name: 'John',
    greet: () => {
        console.log(this.name); // undefined
    }
};
```

**Solution:**
Use regular function for methods:
```javascript
const obj = {
    name: 'John',
    greet() {
        console.log(this.name); // 'John'
    }
};
```

### Issue 2: Cannot use as constructor

**Problem:**
```javascript
const Person = (name) => {
    this.name = name;
};
new Person('John'); // TypeError
```

**Solution:**
Use function declaration or class:
```javascript
function Person(name) {
    this.name = name;
}
// OR
class Person {
    constructor(name) {
        this.name = name;
    }
}
```

### Issue 3: Unexpected return value

**Problem:**
```javascript
const makeUser = (name) => { name, age: 30 }; // undefined
```

**Solution:**
Wrap object literal in parentheses:
```javascript
const makeUser = (name) => ({ name, age: 30 });
```

### Issue 4: Arguments not defined

**Problem:**
```javascript
const sum = () => {
    return Array.from(arguments).reduce((a, b) => a + b);
};
// ReferenceError: arguments is not defined
```

**Solution:**
Use rest parameters:
```javascript
const sum = (...args) => {
    return args.reduce((a, b) => a + b);
};
```

### Issue 5: Binding Issues in Loops

**Problem:**
```javascript
for (var i = 0; i < 5; i++) {
    setTimeout(() => console.log(i), 100); // Always logs 5
}
```

**Solution:**
Use let instead of var:
```javascript
for (let i = 0; i < 5; i++) {
    setTimeout(() => console.log(i), 100); // Logs 0, 1, 2, 3, 4
}
```

## 3.13. Advanced Topics

### Advanced Topic 1: Arrow Functions and Hoisting

```javascript
// Function declarations are hoisted
greet(); // Works
function greet() {
    console.log('Hello');
}

// Arrow functions are NOT hoisted
// sayHello(); // ReferenceError
const sayHello = () => {
    console.log('Hello');
};
```

### Advanced Topic 2: Performance Considerations

```javascript
// Arrow functions are slightly faster in V8
// But the difference is negligible in most cases

// Traditional function - creates new function object
const obj = {
    method: function() {
        return 42;
    }
};

// Arrow function - also creates new function object
const obj2 = {
    method: () => 42
};

// For performance-critical code, measure!
```

### Advanced Topic 3: Lexical 'super'

```javascript
// Arrow functions don't have their own 'super'
class Parent {
    constructor() {
        this.name = 'Parent';
    }
}

class Child extends Parent {
    constructor() {
        super();

        // Regular method - can use super
        this.regularMethod = function() {
            // Cannot use super here
        };

        // Arrow function - lexical super
        this.arrowMethod = () => {
            // Can use super from constructor scope
        };
    }
}
```

### Advanced Topic 4: Memory Implications

```javascript
// Each arrow function creates a new function instance

class Component {
    constructor() {
        // This creates a new arrow function for each instance
        this.handleClick = () => {
            console.log('Clicked');
        };
    }
}

// Better for memory (shared across instances)
class Component {
    handleClick() {
        console.log('Clicked');
    }
}

// If you need binding, bind in constructor
class Component {
    constructor() {
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        console.log('Clicked');
    }
}
```

### Advanced Topic 5: Arrow Functions in Closures

```javascript
// Complex closure example
const createMultiplier = (factor) => {
    let count = 0;

    return {
        multiply: (n) => {
            count++;
            return n * factor;
        },
        getCount: () => count,
        reset: () => {
            count = 0;
        }
    };
};

const times5 = createMultiplier(5);
console.log(times5.multiply(3)); // 15
console.log(times5.multiply(4)); // 20
console.log(times5.getCount()); // 2
```

## 3.14. Exercises (Extended)

### Exercise 1: Convert to Arrow Functions
```javascript
// Convert these to arrow functions
function square(x) {
    return x * x;
}

function isEven(num) {
    return num % 2 === 0;
}

function greet(name) {
    return 'Hello, ' + name;
}
```

### Exercise 2: Fix 'this' Issue
```javascript
// Fix this code using arrow function
const counter = {
    count: 0,
    increment() {
        setInterval(function() {
            this.count++;
            console.log(this.count);
        }, 1000);
    }
};
```

### Exercise 3: Array Transformations
```javascript
// Use arrow functions to:
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// 1. Double all numbers
// 2. Filter even numbers only
// 3. Sum all numbers
// 4. Find first number > 5
// 5. Check if all numbers are positive
```

### Exercise 4: Create Utility Functions
```javascript
// Implement these using arrow functions:
// 1. pipe - compose functions left to right
// 2. compose - compose functions right to left
// 3. curry - curry a function
// 4. partial - partial application
```

### Exercise 5: Event Handling
```javascript
// Create a simple event emitter with:
// - on(event, handler)
// - off(event, handler)
// - emit(event, data)
// - once(event, handler)
// Use arrow functions where appropriate
```

### Exercise 6: Async Operations
```javascript
// Create an API wrapper with:
// - get(url)
// - post(url, data)
// - Error handling
// - Retry logic
// Use arrow functions and async/await
```

### Exercise 7: Higher-Order Functions
```javascript
// Create a function that:
// - Takes an array of functions
// - Returns a function that applies all of them in sequence
// Use arrow functions
```

### Exercise 8: Memoization
```javascript
// Implement a memoize function using arrow functions
// Test it with fibonacci
```

### Exercise 9: Debounce and Throttle
```javascript
// Implement debounce and throttle using arrow functions
```

### Exercise 10: Functional Array Methods
```javascript
// Implement custom versions of:
// - map
// - filter
// - reduce
// Using arrow functions
```

### Exercise 11: State Machine
```javascript
// Create a simple state machine using arrow functions
// Example: Traffic light (red -> green -> yellow -> red)
```

### Exercise 12: Advanced Challenge
```javascript
// Create a reactive data store with:
// - state management
// - computed values
// - subscriptions
// - middleware support
// Use arrow functions throughout
```

---

**Kết luận:** Arrow functions làm code ngắn gọn và giải quyết vấn đề 'this' binding. Tuy nhiên, cần biết khi nào nên dùng và khi nào không nên dùng.
