# CHƯƠNG 5: DESTRUCTURING

## 5.1. Giới thiệu Destructuring

Destructuring cho phép extract values từ arrays hoặc properties từ objects vào distinct variables.

### 5.1.1. Why Destructuring?

**ES5:**
```javascript
var user = { name: 'John', age: 30 };
var name = user.name;
var age = user.age;

var numbers = [1, 2, 3];
var first = numbers[0];
var second = numbers[1];
```

**ES6:**
```javascript
const user = { name: 'John', age: 30 };
const { name, age } = user;

const numbers = [1, 2, 3];
const [first, second] = numbers;
```

## 5.2. Object Destructuring

### 5.2.1. Basic Syntax

```javascript
const user = {
    name: 'John',
    age: 30,
    city: 'NYC'
};

// Extract properties
const { name, age, city } = user;

console.log(name);  // "John"
console.log(age);   // 30
console.log(city);  // "NYC"
```

### 5.2.2. Variable Renaming

```javascript
const user = { name: 'John', age: 30 };

// Rename variables
const { name: userName, age: userAge } = user;

console.log(userName);  // "John"
console.log(userAge);   // 30
// console.log(name);   // ReferenceError
```

### 5.2.3. Default Values

```javascript
const user = { name: 'John' };

// Provide defaults for missing properties
const { name, age = 25, city = 'Unknown' } = user;

console.log(name);  // "John"
console.log(age);   // 25 (default)
console.log(city);  // "Unknown" (default)
```

### 5.2.4. Combining Rename and Default

```javascript
const user = { name: 'John' };

const { name: userName, age: userAge = 30 } = user;

console.log(userName);  // "John"
console.log(userAge);   // 30 (default)
```

### 5.2.5. Nested Objects

```javascript
const user = {
    name: 'John',
    address: {
        city: 'NYC',
        country: 'USA'
    }
};

// Nested destructuring
const {
    name,
    address: { city, country }
} = user;

console.log(name);     // "John"
console.log(city);     // "NYC"
console.log(country);  // "USA"
// console.log(address); // ReferenceError (address not extracted)
```

### 5.2.6. Deep Nesting

```javascript
const data = {
    user: {
        profile: {
            name: 'John',
            age: 30
        }
    }
};

const {
    user: {
        profile: { name, age }
    }
} = data;

console.log(name, age);  // "John" 30
```

## 5.3. Array Destructuring

### 5.3.1. Basic Syntax

```javascript
const numbers = [1, 2, 3, 4, 5];

// Extract elements
const [first, second, third] = numbers;

console.log(first);   // 1
console.log(second);  // 2
console.log(third);   // 3
```

### 5.3.2. Skipping Elements

```javascript
const numbers = [1, 2, 3, 4, 5];

// Skip elements with commas
const [first, , third, , fifth] = numbers;

console.log(first);  // 1
console.log(third);  // 3
console.log(fifth);  // 5
```

### 5.3.3. Default Values

```javascript
const numbers = [1];

const [first, second = 2, third = 3] = numbers;

console.log(first);   // 1
console.log(second);  // 2 (default)
console.log(third);   // 3 (default)
```

### 5.3.4. Rest Elements

```javascript
const numbers = [1, 2, 3, 4, 5];

// Collect remaining elements
const [first, second, ...rest] = numbers;

console.log(first);   // 1
console.log(second);  // 2
console.log(rest);    // [3, 4, 5]
```

### 5.3.5. Swapping Variables

```javascript
let a = 1;
let b = 2;

// Swap without temp variable
[a, b] = [b, a];

console.log(a);  // 2
console.log(b);  // 1
```

### 5.3.6. Nested Arrays

```javascript
const nested = [1, [2, 3], 4];

const [first, [second, third], fourth] = nested;

console.log(first);   // 1
console.log(second);  // 2
console.log(third);   // 3
console.log(fourth);  // 4
```

## 5.4. Function Parameters

### 5.4.1. Object Parameters

```javascript
// Without destructuring
function displayUser(user) {
    console.log(user.name);
    console.log(user.age);
}

// With destructuring
function displayUser({ name, age }) {
    console.log(name);
    console.log(age);
}

displayUser({ name: 'John', age: 30 });
```

### 5.4.2. Default Parameter Values

```javascript
function createUser({ name, age = 25, city = 'NYC' }) {
    return { name, age, city };
}

createUser({ name: 'John' });
// { name: 'John', age: 25, city: 'NYC' }
```

### 5.4.3. Default Parameter Object

```javascript
function createUser({ name, age } = {}) {
    return { name: name || 'Guest', age: age || 0 };
}

createUser();  // { name: 'Guest', age: 0 }
createUser({ name: 'John', age: 30 });  // { name: 'John', age: 30 }
```

### 5.4.4. Array Parameters

```javascript
function sum([a, b, c]) {
    return a + b + c;
}

sum([1, 2, 3]);  // 6
```

### 5.4.5. Mixed Destructuring

```javascript
function displayData({ user: { name, age }, items: [first, second] }) {
    console.log(`${name}, ${age}`);
    console.log(`First item: ${first}, Second item: ${second}`);
}

displayData({
    user: { name: 'John', age: 30 },
    items: ['Apple', 'Banana', 'Orange']
});
```

## 5.5. Practical Examples

### 5.5.1. API Response Handling

```javascript
// Fetch user data
fetch('/api/user')
    .then(response => response.json())
    .then(({ id, name, email, profile: { avatar } }) => {
        console.log(`${name} (${email})`);
        console.log(`Avatar: ${avatar}`);
    });
```

### 5.5.2. React Props

```javascript
// React component with destructured props
function UserCard({ name, age, avatar, isOnline = false }) {
    return `
        <div class="card">
            <img src="${avatar}" alt="${name}" />
            <h3>${name}</h3>
            <p>Age: ${age}</p>
            <span>${isOnline ? 'Online' : 'Offline'}</span>
        </div>
    `;
}
```

### 5.5.3. Config Objects

```javascript
function initApp({
    apiUrl = 'https://api.example.com',
    timeout = 5000,
    retries = 3,
    debug = false
} = {}) {
    console.log('API URL:', apiUrl);
    console.log('Timeout:', timeout);
    console.log('Retries:', retries);
    console.log('Debug:', debug);
}

initApp({ apiUrl: 'https://custom.com', debug: true });
```

### 5.5.4. Returning Multiple Values

```javascript
function getMinMax(numbers) {
    return {
        min: Math.min(...numbers),
        max: Math.max(...numbers),
        length: numbers.length
    };
}

const { min, max, length } = getMinMax([1, 2, 3, 4, 5]);
console.log(`Min: ${min}, Max: ${max}, Count: ${length}`);
```

### 5.5.5. For-of Loop

```javascript
const users = [
    { id: 1, name: 'John', age: 30 },
    { id: 2, name: 'Jane', age: 25 }
];

for (const { id, name, age } of users) {
    console.log(`${id}: ${name} (${age})`);
}
```

### 5.5.6. Array Methods

```javascript
const users = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 },
    { name: 'Bob', age: 35 }
];

// map
const names = users.map(({ name }) => name);

// filter
const adults = users.filter(({ age }) => age >= 30);

// forEach
users.forEach(({ name, age }) => {
    console.log(`${name}: ${age}`);
});
```

## 5.6. Advanced Patterns

### 5.6.1. Computed Property Names

```javascript
const key = 'name';
const { [key]: value } = { name: 'John', age: 30 };

console.log(value);  // "John"
```

### 5.6.2. Rest in Objects

```javascript
const user = {
    id: 1,
    name: 'John',
    age: 30,
    city: 'NYC',
    country: 'USA'
};

const { id, ...userData } = user;

console.log(id);         // 1
console.log(userData);   // { name: 'John', age: 30, city: 'NYC', country: 'USA' }
```

### 5.6.3. Combining Arrays and Objects

```javascript
const data = {
    user: 'John',
    scores: [85, 90, 95]
};

const { user, scores: [test1, test2, test3] } = data;

console.log(user);   // "John"
console.log(test1);  // 85
console.log(test2);  // 90
console.log(test3);  // 95
```

### 5.6.4. Function Chaining

```javascript
const process = ({ value }) => ({ value: value * 2 });
const format = ({ value }) => ({ result: `Value: ${value}` });

const { result } = format(process({ value: 10 }));
console.log(result);  // "Value: 20"
```

## 5.7. Common Patterns

### 5.7.1. Object Property Extraction

```javascript
// Extract specific properties
const { name, age } = user;

// Extract and rename
const { name: userName, age: userAge } = user;

// Extract with defaults
const { name, age = 25 } = user;
```

### 5.7.2. Array Element Extraction

```javascript
// Get first and last
const [first, ...middle] = array;
const last = middle.pop();

// Or using length
const [first] = array;
const last = array[array.length - 1];
```

### 5.7.3. Partial Extraction

```javascript
// Only get what you need
const { name } = user;  // Ignore other properties

const [first] = array;  // Ignore other elements
```

## 5.8. Best Practices

### 5.8.1. Readability

```javascript
// Good: Clear destructuring
const { name, age } = user;

// Bad: Too much nesting
const { user: { profile: { address: { city } } } } = data;

// Better: Break it down
const { user } = data;
const { profile } = user;
const { address } = profile;
const { city } = address;
```

### 5.8.2. Default Values

```javascript
// Always provide defaults for optional properties
function createUser({ name, age = 0, city = 'Unknown' } = {}) {
    return { name, age, city };
}
```

### 5.8.3. Error Handling

```javascript
// Safe destructuring
try {
    const { data: { user: { name } } } = response;
} catch (error) {
    console.error('Invalid response structure');
}

// Or use optional chaining (ES2020)
const name = response?.data?.user?.name;
```

## 5.9. Common Mistakes

### 5.9.1. Destructuring null/undefined

```javascript
// Error: Cannot destructure undefined
const { name } = undefined;  // TypeError

// Fix: Provide default
const { name } = undefined || {};  // OK
const { name } = user ?? {};       // OK (nullish coalescing)
```

### 5.9.2. Variable Already Declared

```javascript
let name = 'Jane';

// Error: name already declared
let { name } = { name: 'John' };  // SyntaxError

// Fix: Use different name
let { name: userName } = { name: 'John' };
```

### 5.9.3. Assigning to Existing Variables

```javascript
let name, age;

// Wrong: This is a block, not destructuring
{ name, age } = user;  // SyntaxError

// Correct: Wrap in parentheses
({ name, age } = user);  // OK
```

## 5.10. Exercises

### Exercise 1: Basic Destructuring

```javascript
// Extract name and age from user object
const user = { name: 'John', age: 30, city: 'NYC' };
// Your code here
```

### Exercise 2: Array Swap

```javascript
// Swap x and y using destructuring
let x = 10;
let y = 20;
// Your code here
// Result: x = 20, y = 10
```

### Exercise 3: Function Parameters

```javascript
// Create a function that takes an object and logs name and age
// Provide default age of 25
function greetUser(/* your parameters */) {
    // Your code here
}

greetUser({ name: 'John' });  // "Hello, John! Age: 25"
greetUser({ name: 'Jane', age: 30 });  // "Hello, Jane! Age: 30"
```

### Exercise 4: Nested Destructuring

```javascript
// Extract city from nested object
const data = {
    user: {
        name: 'John',
        address: {
            city: 'NYC',
            country: 'USA'
        }
    }
};
// Extract city using destructuring
```

---

**Kết luận:** Destructuring làm code ngắn gọn và dễ đọc hơn khi extract values từ objects và arrays. Đặc biệt hữu ích cho function parameters và API responses.

**Chương tiếp theo:** Spread & Rest Operators
