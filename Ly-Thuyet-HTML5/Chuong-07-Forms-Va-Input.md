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
