# CHƯƠNG 7: FORMS VÀ INPUT

## 7.1. Form Basics

### 7.1.1. Thẻ `<form>`

```html
<form action="/submit" method="POST">
    <!-- Form fields -->
</form>
```

**Attributes:**
- `action`: URL xử lý form
- `method`: GET hoặc POST
- `enctype`: Encoding type (multipart/form-data cho file upload)
- `autocomplete`: on | off
- `novalidate`: Tắt validation
- `target`: _self | _blank | _parent | _top

### 7.1.2. Form Methods

**GET:**
```html
<form action="/search" method="GET">
    <input type="text" name="q">
    <button type="submit">Search</button>
</form>
<!-- URL: /search?q=query -->
```

**POST:**
```html
<form action="/login" method="POST">
    <input type="text" name="username">
    <input type="password" name="password">
    <button type="submit">Login</button>
</form>
```

## 7.2. Input Types

### 7.2.1. Text Inputs

**text:**
```html
<label for="username">Username:</label>
<input type="text" id="username" name="username" placeholder="Enter username">
```

**password:**
```html
<label for="password">Password:</label>
<input type="password" id="password" name="password">
```

**email:**
```html
<label for="email">Email:</label>
<input type="email" id="email" name="email" required>
```

**url:**
```html
<label for="website">Website:</label>
<input type="url" id="website" name="website" placeholder="https://example.com">
```

**tel:**
```html
<label for="phone">Phone:</label>
<input type="tel" id="phone" name="phone" pattern="[0-9]{10}">
```

**search:**
```html
<label for="search">Search:</label>
<input type="search" id="search" name="search">
```

### 7.2.2. Number Inputs

**number:**
```html
<label for="quantity">Quantity:</label>
<input type="number" id="quantity" name="quantity"
       min="1" max="10" step="1" value="1">
```

**range:**
```html
<label for="volume">Volume:</label>
<input type="range" id="volume" name="volume"
       min="0" max="100" value="50">
<output id="volumeOutput">50</output>
```

### 7.2.3. Date và Time Inputs

**date:**
```html
<label for="birthday">Birthday:</label>
<input type="date" id="birthday" name="birthday"
       min="1900-01-01" max="2024-12-31">
```

**time:**
```html
<label for="meeting">Meeting time:</label>
<input type="time" id="meeting" name="meeting"
       min="09:00" max="18:00">
```

**datetime-local:**
```html
<label for="appointment">Appointment:</label>
<input type="datetime-local" id="appointment" name="appointment">
```

**month:**
```html
<label for="month">Month:</label>
<input type="month" id="month" name="month">
```

**week:**
```html
<label for="week">Week:</label>
<input type="week" id="week" name="week">
```

### 7.2.4. Color Picker

```html
<label for="color">Choose color:</label>
<input type="color" id="color" name="color" value="#ff0000">
```

### 7.2.5. File Upload

```html
<label for="file">Choose file:</label>
<input type="file" id="file" name="file" accept="image/*">

<!-- Multiple files -->
<input type="file" name="files" multiple>

<!-- Specific file types -->
<input type="file" name="document" accept=".pdf,.doc,.docx">
<input type="file" name="image" accept="image/png,image/jpeg">
```

### 7.2.6. Hidden Input

```html
<input type="hidden" name="userId" value="12345">
```

## 7.3. Selection Inputs

### 7.3.1. Checkbox

```html
<!-- Single checkbox -->
<input type="checkbox" id="agree" name="agree" value="yes">
<label for="agree">I agree to terms</label>

<!-- Multiple checkboxes -->
<fieldset>
    <legend>Select interests:</legend>
    <input type="checkbox" id="sports" name="interests" value="sports">
    <label for="sports">Sports</label>

    <input type="checkbox" id="music" name="interests" value="music">
    <label for="music">Music</label>

    <input type="checkbox" id="reading" name="interests" value="reading" checked>
    <label for="reading">Reading</label>
</fieldset>
```

### 7.3.2. Radio Buttons

```html
<fieldset>
    <legend>Select gender:</legend>
    <input type="radio" id="male" name="gender" value="male" checked>
    <label for="male">Male</label>

    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>

    <input type="radio" id="other" name="gender" value="other">
    <label for="other">Other</label>
</fieldset>
```

### 7.3.3. Select Dropdown

**Basic select:**
```html
<label for="country">Country:</label>
<select id="country" name="country">
    <option value="">--Select--</option>
    <option value="vn">Vietnam</option>
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
</select>
```

**With optgroup:**
```html
<label for="car">Choose car:</label>
<select id="car" name="car">
    <optgroup label="German Cars">
        <option value="mercedes">Mercedes</option>
        <option value="bmw">BMW</option>
    </optgroup>
    <optgroup label="Japanese Cars">
        <option value="toyota">Toyota</option>
        <option value="honda">Honda</option>
    </optgroup>
</select>
```

**Multiple select:**
```html
<label for="skills">Skills:</label>
<select id="skills" name="skills" multiple size="5">
    <option value="html">HTML</option>
    <option value="css">CSS</option>
    <option value="js">JavaScript</option>
    <option value="python">Python</option>
</select>
```

### 7.3.4. Datalist (Autocomplete)

```html
<label for="browser">Choose browser:</label>
<input list="browsers" id="browser" name="browser">
<datalist id="browsers">
    <option value="Chrome">
    <option value="Firefox">
    <option value="Safari">
    <option value="Edge">
</datalist>
```

## 7.4. Text Areas

```html
<label for="message">Message:</label>
<textarea id="message" name="message"
          rows="4" cols="50"
          maxlength="500"
          placeholder="Enter your message">
</textarea>
```

## 7.5. Buttons

### 7.5.1. Button Types

**submit:**
```html
<button type="submit">Submit Form</button>
<input type="submit" value="Submit">
```

**reset:**
```html
<button type="reset">Reset Form</button>
<input type="reset" value="Reset">
```

**button:**
```html
<button type="button" onclick="doSomething()">Click Me</button>
<input type="button" value="Click" onclick="doSomething()">
```

### 7.5.2. Image Button

```html
<input type="image" src="submit.png" alt="Submit" width="50" height="50">
```

## 7.6. Form Attributes

### 7.6.1. Input Attributes

**required:**
```html
<input type="text" name="username" required>
```

**readonly:**
```html
<input type="text" name="username" value="johndoe" readonly>
```

**disabled:**
```html
<input type="text" name="username" disabled>
```

**placeholder:**
```html
<input type="email" placeholder="user@example.com">
```

**autofocus:**
```html
<input type="text" name="search" autofocus>
```

**autocomplete:**
```html
<input type="email" name="email" autocomplete="email">
<input type="text" name="cc" autocomplete="cc-number">
```

**pattern (regex):**
```html
<input type="text" name="phone" pattern="[0-9]{10}"
       title="10 digit phone number">
```

**min, max, step:**
```html
<input type="number" min="1" max="100" step="5">
<input type="date" min="2024-01-01" max="2024-12-31">
```

**maxlength, minlength:**
```html
<input type="text" name="username" minlength="3" maxlength="20">
<textarea maxlength="500"></textarea>
```

**size:**
```html
<input type="text" size="30">
```

**multiple:**
```html
<input type="file" multiple>
<input type="email" multiple>
```

**accept:**
```html
<input type="file" accept="image/*">
<input type="file" accept=".pdf,.doc">
```

## 7.7. Label và Fieldset

### 7.7.1. Label

**Explicit label:**
```html
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

**Implicit label:**
```html
<label>
    Email:
    <input type="email" name="email">
</label>
```

### 7.7.2. Fieldset và Legend

```html
<form>
    <fieldset>
        <legend>Personal Information</legend>
        <label for="fname">First name:</label>
        <input type="text" id="fname" name="fname"><br>
        <label for="lname">Last name:</label>
        <input type="text" id="lname" name="lname">
    </fieldset>

    <fieldset>
        <legend>Contact Information</legend>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br>
        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone">
    </fieldset>
</form>
```

## 7.8. HTML5 Validation

### 7.8.1. Built-in Validation

```html
<form>
    <!-- Required -->
    <input type="text" name="username" required>

    <!-- Email validation -->
    <input type="email" name="email" required>

    <!-- URL validation -->
    <input type="url" name="website">

    <!-- Number range -->
    <input type="number" min="1" max="10" required>

    <!-- Pattern -->
    <input type="text" pattern="[A-Za-z]{3,}" title="At least 3 letters">

    <!-- Length -->
    <input type="text" minlength="5" maxlength="20">

    <button type="submit">Submit</button>
</form>
```

### 7.8.2. Custom Validation Messages

```javascript
const input = document.querySelector('input[type="email"]');

input.addEventListener('invalid', (e) => {
    if (input.validity.valueMissing) {
        input.setCustomValidity('Email is required');
    } else if (input.validity.typeMismatch) {
        input.setCustomValidity('Please enter a valid email');
    }
});

input.addEventListener('input', () => {
    input.setCustomValidity('');
});
```

### 7.8.3. Constraint Validation API

```javascript
const form = document.querySelector('form');
const input = document.querySelector('input');

// Check validity
if (input.checkValidity()) {
    console.log('Valid');
} else {
    console.log('Invalid');
}

// Validity state
console.log(input.validity.valid);
console.log(input.validity.valueMissing);
console.log(input.validity.typeMismatch);
console.log(input.validity.patternMismatch);
console.log(input.validity.tooLong);
console.log(input.validity.tooShort);
console.log(input.validity.rangeUnderflow);
console.log(input.validity.rangeOverflow);
console.log(input.validity.stepMismatch);

// Validation message
console.log(input.validationMessage);

// Custom validity
input.setCustomValidity('Custom error message');
```

### 7.8.4. Disable Validation

```html
<form novalidate>
    <!-- Validation disabled -->
</form>

<button type="submit" formnovalidate>Submit without validation</button>
```

## 7.9. Form Styling

### 7.9.1. Basic Form Styles

```css
/* Form container */
form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
}

/* Labels */
label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

/* Input fields */
input[type="text"],
input[type="email"],
input[type="password"],
textarea,
select {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

/* Focus state */
input:focus,
textarea:focus,
select:focus {
    outline: none;
    border-color: #4CAF50;
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
}

/* Buttons */
button[type="submit"],
input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

button[type="submit"]:hover {
    background-color: #45a049;
}

/* Validation states */
input:invalid {
    border-color: #f44336;
}

input:valid {
    border-color: #4CAF50;
}
```

### 7.9.2. Form Layouts

**Vertical layout:**
```css
.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
}

.form-group input {
    width: 100%;
}
```

**Horizontal layout:**
```css
.form-horizontal .form-group {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
}

.form-horizontal label {
    width: 150px;
    margin-right: 10px;
    text-align: right;
}

.form-horizontal input {
    flex: 1;
}
```

## 7.10. Practical Examples

### 7.10.1. Contact Form

```html
<form action="/contact" method="POST">
    <h2>Contact Us</h2>

    <div class="form-group">
        <label for="name">Name*</label>
        <input type="text" id="name" name="name" required>
    </div>

    <div class="form-group">
        <label for="email">Email*</label>
        <input type="email" id="email" name="email" required>
    </div>

    <div class="form-group">
        <label for="subject">Subject</label>
        <input type="text" id="subject" name="subject">
    </div>

    <div class="form-group">
        <label for="message">Message*</label>
        <textarea id="message" name="message" rows="5" required></textarea>
    </div>

    <button type="submit">Send Message</button>
</form>
```

### 7.10.2. Registration Form

```html
<form action="/register" method="POST">
    <fieldset>
        <legend>Account Information</legend>

        <label for="username">Username*</label>
        <input type="text" id="username" name="username"
               minlength="3" maxlength="20" required>

        <label for="email">Email*</label>
        <input type="email" id="email" name="email" required>

        <label for="password">Password*</label>
        <input type="password" id="password" name="password"
               minlength="8" required>

        <label for="confirm">Confirm Password*</label>
        <input type="password" id="confirm" name="confirm" required>
    </fieldset>

    <fieldset>
        <legend>Personal Information</legend>

        <label for="fname">First Name*</label>
        <input type="text" id="fname" name="fname" required>

        <label for="lname">Last Name*</label>
        <input type="text" id="lname" name="lname" required>

        <label for="dob">Date of Birth</label>
        <input type="date" id="dob" name="dob">

        <label for="gender">Gender</label>
        <select id="gender" name="gender">
            <option value="">--Select--</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
        </select>
    </fieldset>

    <div>
        <input type="checkbox" id="terms" name="terms" required>
        <label for="terms">I agree to the Terms and Conditions*</label>
    </div>

    <button type="submit">Register</button>
</form>
```

### 7.10.3. Search Form

```html
<form action="/search" method="GET" role="search">
    <label for="search" class="sr-only">Search</label>
    <input type="search"
           id="search"
           name="q"
           placeholder="Search..."
           required>
    <button type="submit">Search</button>
</form>
```

## 7.10.4. Survey Form

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Survey Form</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }

        .form-container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        .form-section {
            margin-bottom: 30px;
        }

        .form-section h3 {
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
            color: #333;
        }

        label {
            display: block;
            margin: 10px 0 5px 0;
            font-weight: bold;
            color: #555;
        }

        input[type="text"],
        input[type="email"],
        input[type="number"],
        select,
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }

        input[type="radio"],
        input[type="checkbox"] {
            margin-right: 8px;
        }

        .radio-group,
        .checkbox-group {
            margin-bottom: 15px;
        }

        .radio-item,
        .checkbox-item {
            margin-bottom: 10px;
        }

        input[type="range"] {
            width: 100%;
            cursor: pointer;
        }

        .range-value {
            display: inline-block;
            margin-left: 10px;
            font-weight: bold;
            color: #007bff;
        }

        .form-buttons {
            display: flex;
            gap: 10px;
            margin-top: 30px;
        }

        button {
            flex: 1;
            padding: 12px;
            font-size: 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button[type="submit"] {
            background: #007bff;
            color: white;
        }

        button[type="submit"]:hover {
            background: #0056b3;
        }

        button[type="reset"] {
            background: #6c757d;
            color: white;
        }

        button[type="reset"]:hover {
            background: #545b62;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Customer Satisfaction Survey</h1>

        <form id="surveyForm" method="POST" action="/submit-survey">
            <div class="form-section">
                <label for="name">Full Name *</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email *</label>
                <input type="email" id="email" name="email" required>
            </div>

            <div class="form-section">
                <h3>Service Quality</h3>

                <label>Overall Service Rating *</label>
                <div class="radio-group">
                    <div class="radio-item">
                        <input type="radio" id="excellent" name="rating" value="excellent" required>
                        <label for="excellent">Excellent</label>
                    </div>
                    <div class="radio-item">
                        <input type="radio" id="good" name="rating" value="good">
                        <label for="good">Good</label>
                    </div>
                    <div class="radio-item">
                        <input type="radio" id="average" name="rating" value="average">
                        <label for="average">Average</label>
                    </div>
                    <div class="radio-item">
                        <input type="radio" id="poor" name="rating" value="poor">
                        <label for="poor">Poor</label>
                    </div>
                </div>

                <label>What aspects did you like? *</label>
                <div class="checkbox-group">
                    <div class="checkbox-item">
                        <input type="checkbox" id="quality" name="aspects" value="quality">
                        <label for="quality">Product Quality</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="price" name="aspects" value="price">
                        <label for="price">Price</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="customer_service" name="aspects" value="customer_service">
                        <label for="customer_service">Customer Service</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="delivery" name="aspects" value="delivery">
                        <label for="delivery">Fast Delivery</label>
                    </div>
                </div>
            </div>

            <div class="form-section">
                <label for="satisfaction">Satisfaction Level (1-10): <span class="range-value">5</span></label>
                <input type="range" id="satisfaction" name="satisfaction" min="1" max="10" value="5"
                       oninput="updateRangeValue(this.value)">
            </div>

            <div class="form-section">
                <label for="comments">Additional Comments</label>
                <textarea id="comments" name="comments" rows="5" placeholder="Please share any additional feedback..."></textarea>
            </div>

            <div class="form-buttons">
                <button type="submit">Submit Survey</button>
                <button type="reset">Clear Form</button>
            </div>
        </form>
    </div>

    <script>
        function updateRangeValue(value) {
            document.querySelector('.range-value').textContent = value;
        }

        document.getElementById('surveyForm').addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Survey submitted successfully!');
        });
    </script>
</body>
</html>
```

### 7.10.5. Advanced Form with Validation

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Advanced Form with Validation</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .form-container {
            max-width: 500px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: #333;
        }

        input[type="text"],
        input[type="email"],
        input[type="password"],
        input[type="number"],
        select,
        textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
            transition: all 0.3s;
        }

        input:focus,
        select:focus,
        textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        input:valid {
            border-color: #28a745;
        }

        input:invalid:not(:placeholder-shown) {
            border-color: #dc3545;
        }

        .error-message {
            color: #dc3545;
            font-size: 12px;
            margin-top: 5px;
            display: none;
        }

        input:invalid:not(:placeholder-shown) ~ .error-message {
            display: block;
        }

        .password-strength {
            margin-top: 10px;
            height: 4px;
            background: #ddd;
            border-radius: 2px;
            overflow: hidden;
        }

        .password-strength-bar {
            height: 100%;
            width: 0;
            transition: width 0.3s, background-color 0.3s;
        }

        .password-strength-bar.weak {
            width: 33%;
            background: #dc3545;
        }

        .password-strength-bar.medium {
            width: 66%;
            background: #ffc107;
        }

        .password-strength-bar.strong {
            width: 100%;
            background: #28a745;
        }

        .form-buttons {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 30px;
        }

        button {
            padding: 12px;
            font-size: 16px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.3s;
        }

        button[type="submit"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            grid-column: 1 / -1;
        }

        button[type="submit"]:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        button[type="submit"]:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        button[type="reset"] {
            background: #6c757d;
            color: white;
        }

        button[type="reset"]:hover {
            background: #545b62;
        }

        .success-message {
            display: none;
            background: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 20px;
        }

        .success-message.show {
            display: block;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <div class="success-message" id="successMessage">
            Form submitted successfully! Thank you for registering.
        </div>

        <h1>Register Account</h1>

        <form id="registerForm" novalidate>
            <div class="form-group">
                <label for="username">Username *</label>
                <input type="text"
                       id="username"
                       name="username"
                       placeholder="Choose a username"
                       minlength="3"
                       maxlength="20"
                       pattern="^[a-zA-Z0-9_]+$"
                       title="Username must contain only letters, numbers, and underscores"
                       required>
                <span class="error-message">Username must be 3-20 characters, letters/numbers/underscore only</span>
            </div>

            <div class="form-group">
                <label for="email">Email *</label>
                <input type="email"
                       id="email"
                       name="email"
                       placeholder="your.email@example.com"
                       required>
                <span class="error-message">Please enter a valid email address</span>
            </div>

            <div class="form-group">
                <label for="password">Password *</label>
                <input type="password"
                       id="password"
                       name="password"
                       placeholder="At least 8 characters"
                       minlength="8"
                       pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$"
                       title="Password must contain uppercase, lowercase, number, and special character"
                       required>
                <div class="password-strength">
                    <div class="password-strength-bar" id="strengthBar"></div>
                </div>
                <span class="error-message">Password must have 8+ chars with uppercase, lowercase, number, and special char</span>
            </div>

            <div class="form-group">
                <label for="confirmPassword">Confirm Password *</label>
                <input type="password"
                       id="confirmPassword"
                       name="confirmPassword"
                       placeholder="Re-enter your password"
                       required>
                <span class="error-message">Passwords do not match</span>
            </div>

            <div class="form-group">
                <label for="age">Age</label>
                <input type="number"
                       id="age"
                       name="age"
                       min="13"
                       max="120"
                       placeholder="Enter your age">
            </div>

            <div class="form-group">
                <label for="country">Country *</label>
                <select id="country" name="country" required>
                    <option value="">Select a country</option>
                    <option value="vn">Vietnam</option>
                    <option value="th">Thailand</option>
                    <option value="id">Indonesia</option>
                    <option value="us">United States</option>
                    <option value="uk">United Kingdom</option>
                </select>
            </div>

            <div class="form-group">
                <label>
                    <input type="checkbox" id="terms" name="terms" required>
                    I agree to Terms and Conditions *
                </label>
            </div>

            <div class="form-buttons">
                <button type="reset">Clear</button>
                <button type="submit" id="submitBtn">Register</button>
            </div>
        </form>
    </div>

    <script>
        const form = document.getElementById('registerForm');
        const passwordInput = document.getElementById('password');
        const confirmPasswordInput = document.getElementById('confirmPassword');
        const strengthBar = document.getElementById('strengthBar');
        const successMessage = document.getElementById('successMessage');
        const submitBtn = document.getElementById('submitBtn');

        // Password strength checker
        passwordInput.addEventListener('input', (e) => {
            const password = e.target.value;
            let strength = 0;

            if (password.length >= 8) strength++;
            if (/[a-z]/.test(password)) strength++;
            if (/[A-Z]/.test(password)) strength++;
            if (/\d/.test(password)) strength++;
            if (/[@$!%*?&]/.test(password)) strength++;

            strengthBar.className = 'password-strength-bar';
            if (strength <= 2) {
                strengthBar.classList.add('weak');
            } else if (strength <= 4) {
                strengthBar.classList.add('medium');
            } else {
                strengthBar.classList.add('strong');
            }
        });

        // Confirm password validation
        confirmPasswordInput.addEventListener('input', () => {
            if (confirmPasswordInput.value !== passwordInput.value) {
                confirmPasswordInput.setCustomValidity('Passwords do not match');
            } else {
                confirmPasswordInput.setCustomValidity('');
            }
        });

        // Form submission
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            // Check HTML5 validation
            if (!form.checkValidity()) {
                console.log('Form validation failed');
                return;
            }

            // Custom validation
            if (passwordInput.value !== confirmPasswordInput.value) {
                alert('Passwords do not match!');
                return;
            }

            // Show success message
            successMessage.classList.add('show');
            form.style.display = 'none';

            // Reset after 3 seconds
            setTimeout(() => {
                form.reset();
                form.style.display = 'block';
                successMessage.classList.remove('show');
            }, 3000);
        });

        // Disable submit button if form is invalid
        form.addEventListener('input', () => {
            submitBtn.disabled = !form.checkValidity();
        });
    </script>
</body>
</html>
```

## 7.11. Tips & Tricks

### Tip 1: Auto-save form data to localStorage
```javascript
const form = document.getElementById('myForm');
const inputs = form.querySelectorAll('input, textarea, select');

// Load saved data
inputs.forEach(input => {
    const saved = localStorage.getItem(input.name);
    if (saved) input.value = saved;
});

// Save on change
inputs.forEach(input => {
    input.addEventListener('change', () => {
        localStorage.setItem(input.name, input.value);
    });
});

// Clear on submit
form.addEventListener('submit', () => {
    inputs.forEach(input => localStorage.removeItem(input.name));
});
```

### Tip 2: Dynamic form fields
```html
<form id="dynamicForm">
    <div id="fieldsContainer"></div>
    <button type="button" onclick="addField()">Add Field</button>
</form>

<script>
    let fieldCount = 0;

    function addField() {
        const container = document.getElementById('fieldsContainer');
        const fieldId = `field-${fieldCount++}`;

        const div = document.createElement('div');
        div.innerHTML = `
            <label for="${fieldId}">Field ${fieldCount}:</label>
            <input type="text" id="${fieldId}" name="${fieldId}">
            <button type="button" onclick="removeField('${fieldId}')">Remove</button>
        `;

        container.appendChild(div);
    }

    function removeField(fieldId) {
        document.getElementById(fieldId).parentElement.remove();
    }
</script>
```

### Tip 3: Form validation with custom messages
```javascript
const email = document.getElementById('email');

email.addEventListener('invalid', (e) => {
    if (email.validity.valueMissing) {
        email.setCustomValidity('Email is required');
    } else if (email.validity.typeMismatch) {
        email.setCustomValidity('Please enter a valid email');
    }
});

email.addEventListener('input', () => {
    email.setCustomValidity('');
});
```

### Tip 4: Conditional field display
```html
<select id="userType" name="userType">
    <option>Individual</option>
    <option>Business</option>
</select>

<div id="businessFields" style="display: none;">
    <input type="text" placeholder="Company name">
</div>

<script>
    document.getElementById('userType').addEventListener('change', (e) => {
        const businessFields = document.getElementById('businessFields');
        businessFields.style.display = e.target.value === 'Business' ? 'block' : 'none';
    });
</script>
```

### Tip 5: File upload preview
```html
<input type="file" id="imageInput" accept="image/*">
<img id="preview" style="max-width: 200px; margin-top: 10px;">

<script>
    document.getElementById('imageInput').addEventListener('change', (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();

        reader.onload = (event) => {
            document.getElementById('preview').src = event.target.result;
        };

        reader.readAsDataURL(file);
    });
</script>
```

### Tip 6: Real-time character counter
```html
<textarea id="message" maxlength="200" placeholder="Enter message..."></textarea>
<span id="charCount">0/200</span>

<script>
    const textarea = document.getElementById('message');
    const charCount = document.getElementById('charCount');

    textarea.addEventListener('input', () => {
        charCount.textContent = `${textarea.value.length}/200`;
    });
</script>
```

### Tip 7: Form reset with confirmation
```javascript
const form = document.getElementById('myForm');
const resetBtn = form.querySelector('button[type="reset"]');

resetBtn.addEventListener('click', (e) => {
    if (form.elements.length > 0 &&
        !confirm('Are you sure you want to reset the form?')) {
        e.preventDefault();
    }
});
```

### Tip 8: Auto-focus next field
```html
<input type="tel" maxlength="3" placeholder="Area code">
<input type="tel" maxlength="3" placeholder="Exchange">
<input type="tel" maxlength="4" placeholder="Number">

<script>
    const inputs = document.querySelectorAll('input[type="tel"]');

    inputs.forEach((input, index) => {
        input.addEventListener('input', () => {
            if (input.value.length === input.maxLength && index < inputs.length - 1) {
                inputs[index + 1].focus();
            }
        });
    });
</script>
```

### Tip 9: Dependent select dropdowns
```html
<select id="country" onchange="updateStates()">
    <option>USA</option>
    <option>Canada</option>
</select>
<select id="state"></select>

<script>
    const statesByCountry = {
        USA: ['California', 'Texas', 'New York'],
        Canada: ['Ontario', 'Quebec', 'British Columbia']
    };

    function updateStates() {
        const country = document.getElementById('country').value;
        const stateSelect = document.getElementById('state');

        stateSelect.innerHTML = '';
        statesByCountry[country].forEach(state => {
            stateSelect.appendChild(new Option(state, state));
        });
    }
</script>
```

### Tip 10: Form progress indicator
```html
<div class="progress-bar">
    <div class="progress-fill" id="progressFill"></div>
</div>
<p>Progress: <span id="progressPercent">0</span>%</p>

<form id="myForm">
    <input type="text" name="field1" required>
    <input type="text" name="field2" required>
    <input type="text" name="field3" required>
</form>

<script>
    const form = document.getElementById('myForm');
    const progressFill = document.getElementById('progressFill');
    const progressPercent = document.getElementById('progressPercent');

    form.addEventListener('input', () => {
        const fields = form.querySelectorAll('input[required]');
        const filled = Array.from(fields).filter(f => f.value).length;
        const progress = (filled / fields.length) * 100;

        progressFill.style.width = progress + '%';
        progressPercent.textContent = Math.round(progress);
    });
</script>
```

## 7.12. Common Mistakes

### Lỗi 1: Không có label cho form fields
```html
<!-- ❌ Sai -->
<input type="text" name="email" placeholder="Email">

<!-- ✅ Đúng -->
<label for="email">Email:</label>
<input type="email" id="email" name="email" placeholder="your@email.com">
```

### Lỗi 2: Quên name attribute
```html
<!-- ❌ Sai -->
<input type="text" id="username">

<!-- ✅ Đúng -->
<input type="text" id="username" name="username">
```

### Lỗi 3: Không set form action
```html
<!-- ❌ Sai: Form không biết gửi đến đâu -->
<form>
    <input type="text">
    <button type="submit">Submit</button>
</form>

<!-- ✅ Đúng -->
<form action="/submit" method="POST">
    <input type="text" name="data">
    <button type="submit">Submit</button>
</form>
```

### Lỗi 4: Weak password validation
```html
<!-- ❌ Sai: Chỉ check độ dài -->
<input type="password" minlength="5">

<!-- ✅ Đúng: Check strength -->
<input type="password"
       minlength="8"
       pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])"
       title="Must contain uppercase, lowercase, number, special char">
```

### Lỗi 5: File input không validate type
```html
<!-- ❌ Sai: Accept any file -->
<input type="file">

<!-- ✅ Đúng: Restrict file types -->
<input type="file" accept=".pdf,.doc,.docx" required>
```

### Lỗi 6: Không handle form submission properly
```javascript
// ❌ Sai: No error handling
form.addEventListener('submit', () => {
    fetch('/api/submit', { method: 'POST' });
});

// ✅ Đúng: Proper error handling
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    try {
        const response = await fetch('/api/submit', {
            method: 'POST',
            body: new FormData(form)
        });

        if (!response.ok) throw new Error('Submit failed');
        console.log('Success');
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to submit form');
    }
});
```

### Lỗi 7: Không validate email format
```html
<!-- ❌ Sai -->
<input type="text" name="email" placeholder="Email">

<!-- ✅ Đúng -->
<input type="email" name="email" required>
```

### Lỗi 8: Mismatch between label và input IDs
```html
<!-- ❌ Sai: IDs không match -->
<label for="username">Username:</label>
<input type="text" id="user_name" name="username">

<!-- ✅ Đúng: IDs match -->
<label for="username">Username:</label>
<input type="text" id="username" name="username">
```

### Lỗi 9: Required radio buttons not grouped properly
```html
<!-- ❌ Sai: Validate individually -->
<input type="radio" name="gender" value="m" required>
<input type="radio" name="gender" value="f" required>

<!-- ✅ Đúng: Group with fieldset -->
<fieldset required>
    <legend>Gender:</legend>
    <input type="radio" name="gender" value="m">
    <input type="radio" name="gender" value="f">
</fieldset>
```

### Lỗi 10: Không sanitize user input
```javascript
// ❌ Sai: XSS vulnerability
element.innerHTML = userInput;

// ✅ Đúng: Sanitize input
element.textContent = userInput;

// Hoặc escape HTML
function escapeHTML(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}
```

## 7.13. Troubleshooting

### Issue 1: Form validation message không hiển thị
**Triệu chứng:** HTML5 validation silent mode

**Giải pháp:**
```javascript
const form = document.getElementById('myForm');

form.addEventListener('submit', (e) => {
    if (!form.checkValidity()) {
        e.preventDefault();
        // Show custom message
        form.querySelectorAll(':invalid').forEach(field => {
            console.log(field.validationMessage);
        });
    }
});
```

### Issue 2: Autocomplete không hoạt động
**Triệu chứng:** Browser không suggest password/email

**Giải pháp:**
```html
<!-- Use proper autocomplete attributes -->
<input type="email" name="email" autocomplete="email" required>
<input type="password" name="password" autocomplete="current-password" required>
<input type="tel" name="phone" autocomplete="tel">
```

### Issue 3: File upload không work
**Triệu chứng:** Form action không upload file

**Giải pháp:**
```html
<!-- MUST use enctype for file upload -->
<form action="/upload" method="POST" enctype="multipart/form-data">
    <input type="file" name="file" required>
    <button type="submit">Upload</button>
</form>
```

### Issue 4: Select dropdown value không submit
**Triệu chứng:** Selected value missing from submitted data

**Giải pháp:**
```html
<!-- Must have value attribute -->
<select name="country">
    <option value="">Select</option>
    <option value="vn">Vietnam</option>
    <option value="us">USA</option>
</select>
```

### Issue 5: Placeholder disappears on type
**Triệu chứng:** User confuse

**Giải pháp:**
```html
<!-- Use label + placeholder combination -->
<label for="email">Email:</label>
<input type="email" id="email" name="email"
       placeholder="example@email.com"
       title="Enter your email address">
```

### Issue 6: Form data lost on page refresh
**Triệu chứng:** User frustration, incomplete form

**Giải pháp:**
```javascript
// Save to localStorage
const form = document.getElementById('myForm');
const inputs = form.querySelectorAll('input, textarea, select');

inputs.forEach(input => {
    input.addEventListener('input', () => {
        localStorage.setItem(`form_${input.name}`, input.value);
    });

    // Restore on load
    const saved = localStorage.getItem(`form_${input.name}`);
    if (saved) input.value = saved;
});
```

### Issue 7: Datepicker not consistent across browsers
**Triệu chứng:** Different UI/UX on different browsers

**Giải pháp:**
```html
<!-- Use polyfill or custom date picker -->
<input type="date" name="birthdate" required>

<!-- Or use date format validation -->
<input type="text"
       name="date"
       placeholder="YYYY-MM-DD"
       pattern="\d{4}-\d{2}-\d{2}"
       required>
```

### Issue 8: Form too long, hard to navigate
**Triệu chứng:** Scroll fatigue

**Giải pháp:**
```html
<!-- Split into steps -->
<form id="multiStepForm">
    <div class="step" id="step1">
        <!-- Step 1 fields -->
    </div>
    <div class="step" id="step2" style="display: none;">
        <!-- Step 2 fields -->
    </div>
</form>
```

### Issue 9: Form field size inconsistent
**Triệu chứng:** Bad alignment

**Giải pháp:**
```css
input[type="text"],
input[type="email"],
input[type="password"],
select,
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    box-sizing: border-box; /* Important! */
}
```

### Issue 10: Submit button doubles on fast click
**Triệu chứng:** Double submission

**Giải pháp:**
```javascript
const form = document.getElementById('myForm');
const submitBtn = form.querySelector('button[type="submit"]');
let isSubmitting = false;

form.addEventListener('submit', async (e) => {
    if (isSubmitting) {
        e.preventDefault();
        return;
    }

    isSubmitting = true;
    submitBtn.disabled = true;

    try {
        await fetch('/api/submit', { method: 'POST' });
    } finally {
        isSubmitting = false;
        submitBtn.disabled = false;
    }
});
```

## 7.14. Advanced Topics

### Topic 1: Multi-step Form Wizard
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .step { display: none; }
        .step.active { display: block; }
        .step-indicator {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        .step-dot {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #ddd;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .step-dot.active {
            background: #007bff;
            color: white;
        }
    </style>
</head>
<body>
    <div class="step-indicator">
        <div class="step-dot active">1</div>
        <div class="step-dot">2</div>
        <div class="step-dot">3</div>
    </div>

    <form id="wizardForm">
        <div class="step active" id="step1">
            <h2>Step 1: Personal Info</h2>
            <input type="text" name="name" required>
            <input type="email" name="email" required>
        </div>

        <div class="step" id="step2">
            <h2>Step 2: Address</h2>
            <input type="text" name="address" required>
            <input type="text" name="city" required>
        </div>

        <div class="step" id="step3">
            <h2>Step 3: Confirmation</h2>
            <p>Please review your information and click Submit</p>
        </div>

        <div style="margin-top: 20px;">
            <button type="button" id="prevBtn" onclick="previousStep()">Previous</button>
            <button type="button" id="nextBtn" onclick="nextStep()">Next</button>
            <button type="submit" id="submitBtn" style="display: none;">Submit</button>
        </div>
    </form>

    <script>
        let currentStep = 1;

        function showStep(step) {
            document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
            document.getElementById(`step${step}`).classList.add('active');

            document.getElementById('prevBtn').style.display = step === 1 ? 'none' : 'block';
            document.getElementById('nextBtn').style.display = step === 3 ? 'none' : 'block';
            document.getElementById('submitBtn').style.display = step === 3 ? 'block' : 'none';

            updateStepIndicators();
        }

        function nextStep() {
            if (currentStep < 3) {
                currentStep++;
                showStep(currentStep);
            }
        }

        function previousStep() {
            if (currentStep > 1) {
                currentStep--;
                showStep(currentStep);
            }
        }

        function updateStepIndicators() {
            document.querySelectorAll('.step-dot').forEach((dot, index) => {
                if (index + 1 <= currentStep) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        }

        showStep(1);
    </script>
</body>
</html>
```

### Topic 2: Real-time Form Validation
```javascript
class FormValidator {
    constructor(formId) {
        this.form = document.getElementById(formId);
        this.rules = {};
        this.init();
    }

    init() {
        this.form.querySelectorAll('input, textarea, select').forEach(field => {
            field.addEventListener('blur', () => this.validateField(field));
            field.addEventListener('input', () => this.validateField(field));
        });
    }

    addRule(fieldName, rules) {
        this.rules[fieldName] = rules;
    }

    validateField(field) {
        const rules = this.rules[field.name];
        if (!rules) return true;

        const value = field.value.trim();
        let isValid = true;

        if (rules.required && !value) {
            this.showError(field, 'This field is required');
            isValid = false;
        }

        if (rules.pattern && !rules.pattern.test(value)) {
            this.showError(field, 'Invalid format');
            isValid = false;
        }

        if (rules.minLength && value.length < rules.minLength) {
            this.showError(field, `Minimum ${rules.minLength} characters`);
            isValid = false;
        }

        if (rules.custom && !rules.custom(value)) {
            this.showError(field, rules.customMessage);
            isValid = false;
        }

        if (isValid) {
            this.clearError(field);
        }

        return isValid;
    }

    showError(field, message) {
        field.classList.add('is-invalid');
        let errorDiv = field.parentElement.querySelector('.error-message');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            field.parentElement.appendChild(errorDiv);
        }
        errorDiv.textContent = message;
    }

    clearError(field) {
        field.classList.remove('is-invalid');
        const errorDiv = field.parentElement.querySelector('.error-message');
        if (errorDiv) errorDiv.remove();
    }

    validate() {
        let isValid = true;
        this.form.querySelectorAll('input, textarea, select').forEach(field => {
            if (!this.validateField(field)) {
                isValid = false;
            }
        });
        return isValid;
    }
}

// Usage
const validator = new FormValidator('myForm');
validator.addRule('email', {
    required: true,
    pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/
});
validator.addRule('password', {
    required: true,
    minLength: 8,
    custom: (value) => /[A-Z]/.test(value) && /[0-9]/.test(value),
    customMessage: 'Password must contain uppercase and number'
});
```

### Topic 3: Form data conversion to different formats
```javascript
function formToJSON(form) {
    const formData = new FormData(form);
    return Object.fromEntries(formData);
}

function formToQueryString(form) {
    const formData = new FormData(form);
    return new URLSearchParams(formData).toString();
}

function formToFormData(form) {
    return new FormData(form);
}

// Usage
const form = document.getElementById('myForm');
console.log(formToJSON(form));
console.log(formToQueryString(form));
```

### Topic 4: Form with Dynamic Sections
```html
<form id="dynamicForm">
    <div id="sectionsContainer"></div>
    <button type="button" onclick="addSection()">Add Section</button>
</form>

<script>
    let sectionCount = 0;

    function addSection() {
        const container = document.getElementById('sectionsContainer');
        const sectionId = `section-${sectionCount++}`;

        const section = document.createElement('fieldset');
        section.id = sectionId;
        section.innerHTML = `
            <legend>Section ${sectionCount}</legend>
            <input type="text" name="title" placeholder="Title" required>
            <textarea name="content" placeholder="Content" required></textarea>
            <button type="button" onclick="removeSection('${sectionId}')">Remove Section</button>
        `;

        container.appendChild(section);
    }

    function removeSection(sectionId) {
        document.getElementById(sectionId).remove();
    }
</script>
```

### Topic 5: Form with File Upload Progress
```html
<form id="uploadForm" enctype="multipart/form-data">
    <input type="file" id="fileInput" name="file" required>
    <button type="submit">Upload</button>
</form>

<div id="progressContainer" style="display: none;">
    <progress id="progressBar" max="100" value="0"></progress>
    <span id="progressText">0%</span>
</div>

<script>
    document.getElementById('uploadForm').addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(this);
        const progressContainer = document.getElementById('progressContainer');
        const progressBar = document.getElementById('progressBar');
        const progressText = document.getElementById('progressText');

        progressContainer.style.display = 'block';

        const xhr = new XMLHttpRequest();

        xhr.upload.addEventListener('progress', (e) => {
            if (e.lengthComputable) {
                const percentComplete = (e.loaded / e.total) * 100;
                progressBar.value = percentComplete;
                progressText.textContent = Math.round(percentComplete) + '%';
            }
        });

        xhr.addEventListener('load', () => {
            if (xhr.status === 200) {
                alert('File uploaded successfully');
            }
        });

        xhr.addEventListener('error', () => {
            alert('Upload failed');
        });

        xhr.open('POST', '/upload');
        xhr.send(formData);
    });
</script>
```

## 7.15. Bài tập thực hành

### Bài 1 (Dễ): Simple Login Form
Tạo form login với:
- Username field
- Password field
- Remember me checkbox
- Submit button
- Basic validation

### Bài 2 (Dễ): Newsletter Signup
Tạo form với:
- Email input
- Name input
- Subscribe checkbox
- Submit button
- Success message

### Bài 3 (Dễ): Contact Form
Tạo form contact với:
- Name, Email, Phone
- Subject
- Message textarea
- Submit button

### Bài 4 (Dễ): Feedback Form
Tạo form với:
- Rating radio buttons
- Feedback textarea
- Email input
- Submit button

### Bài 5 (Trung bình): Registration Form
Tạo form registration với:
- Username (3-20 chars)
- Email
- Password (strong password)
- Confirm password
- Terms checkbox
- Real-time validation
- Error messages

### Bài 6 (Trung bình): Job Application Form
Tạo form với:
- Personal information
- Job position select
- Experience level
- Skills checkboxes
- Resume upload
- Validation

### Bài 7 (Trung bình): Event Registration
Tạo form với:
- Participant info
- Event selection
- Ticket quantity
- Payment method
- Terms agreement
- Responsive design

### Bài 8 (Trung bình): Product Order Form
Tạo form với:
- Product selection
- Quantity
- Shipping address
- Payment method
- Order summary
- Validation

### Bài 9 (Khó): Multi-step Registration Wizard
Tạo wizard với:
- Step 1: Personal info
- Step 2: Address
- Step 3: Payment
- Step 4: Review
- Progress indicator
- Data persistence

### Bài 10 (Khó): Advanced Survey Form
Tạo form với:
- Dynamic questions
- Conditional fields
- File uploads
- Real-time validation
- Auto-save
- Progress indicator

### Bài 11 (Khó): Real-time Data Form
Tạo form với:
- Live validation
- Auto-suggestions
- Dependent dropdowns
- Dynamic form sections
- Data persistence
- Error recovery

### Bài 12 (Khó): Form Builder
Tạo app cho phép:
- Create custom forms
- Add/remove fields
- Set validation rules
- Preview form
- Export form
- Share form link

---

## 7.11. Accessibility

### 7.11.1. Labels

```html
<!-- Always use labels -->
<label for="email">Email:</label>
<input type="email" id="email" name="email">
```

### 7.11.2. ARIA Attributes

```html
<label for="email">Email</label>
<input type="email"
       id="email"
       name="email"
       aria-required="true"
       aria-invalid="false"
       aria-describedby="email-help">
<span id="email-help">We'll never share your email</span>
```

### 7.11.3. Error Messages

```html
<label for="email">Email</label>
<input type="email"
       id="email"
       aria-describedby="email-error"
       aria-invalid="true">
<span id="email-error" role="alert">Please enter a valid email</span>
```

## 7.12. Bài tập thực hành

### Bài 1: Basic Form
- Contact form with validation
- All input types
- Proper labels

### Bài 2: Registration Form
- Multi-step form
- Password strength indicator
- Confirmation

### Bài 3: Survey Form
- Radio buttons
- Checkboxes
- Range sliders
- Text areas

### Bài 4: File Upload Form
- Multiple file upload
- File type validation
- Preview before upload

---

**Kết luận:** Forms là phần quan trọng của web development. HTML5 cung cấp nhiều input types và validation features mạnh mẽ. Chương tiếp theo sẽ tìm hiểu về HTML5 Semantic Elements.
