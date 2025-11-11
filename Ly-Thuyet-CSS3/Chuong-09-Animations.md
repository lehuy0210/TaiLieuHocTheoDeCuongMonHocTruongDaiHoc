# CHƯƠNG 9: CSS3 ANIMATIONS

## 9.1. Giới thiệu Animations

CSS Animations cho phép tạo complex animations bằng @keyframes.

### 9.1.1. Basic Animation

```css
/* Define keyframes */
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* Apply animation */
.box {
    animation: fadeIn 1s ease;
}
```

## 9.2. @keyframes

### 9.2.1. Percentage Keyframes

```css
@keyframes slide {
    0% {
        transform: translateX(0);
    }
    50% {
        transform: translateX(100px);
    }
    100% {
        transform: translateX(200px);
    }
}
```

### 9.2.2. Multiple Properties

```css
@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
        opacity: 1;
    }
    50% {
        transform: translateY(-20px);
        opacity: 0.7;
    }
}
```

### 9.2.3. From and To

```css
@keyframes grow {
    from {
        transform: scale(0);
    }
    to {
        transform: scale(1);
    }
}
```

## 9.3. Animation Properties

### 9.3.1. animation-name

```css
.box {
    animation-name: fadeIn;
    animation-name: slideLeft, fadeIn;  /* Multiple animations */
}
```

### 9.3.2. animation-duration

```css
.box {
    animation-duration: 2s;
    animation-duration: 500ms;
    animation-duration: 1s, 2s;  /* For multiple animations */
}
```

### 9.3.3. animation-timing-function

```css
.box {
    animation-timing-function: ease;
    animation-timing-function: linear;
    animation-timing-function: ease-in;
    animation-timing-function: ease-out;
    animation-timing-function: ease-in-out;
    animation-timing-function: cubic-bezier(0.42, 0, 0.58, 1);
    animation-timing-function: steps(4, end);
}
```

### 9.3.4. animation-delay

```css
.box {
    animation-delay: 0.5s;
    animation-delay: -0.5s;  /* Start halfway through */
}
```

### 9.3.5. animation-iteration-count

```css
.box {
    animation-iteration-count: 1;        /* Once */
    animation-iteration-count: 3;        /* 3 times */
    animation-iteration-count: infinite; /* Forever */
}
```

### 9.3.6. animation-direction

```css
.box {
    animation-direction: normal;            /* 0% → 100% */
    animation-direction: reverse;           /* 100% → 0% */
    animation-direction: alternate;         /* 0% → 100% → 0% ... */
    animation-direction: alternate-reverse; /* 100% → 0% → 100% ... */
}
```

### 9.3.7. animation-fill-mode

```css
.box {
    animation-fill-mode: none;      /* Default state before/after */
    animation-fill-mode: forwards;  /* Keep last keyframe */
    animation-fill-mode: backwards; /* Apply first keyframe during delay */
    animation-fill-mode: both;      /* Both forwards and backwards */
}
```

### 9.3.8. animation-play-state

```css
.box {
    animation-play-state: running;  /* Default */
    animation-play-state: paused;   /* Pause animation */
}

.box:hover {
    animation-play-state: paused;
}
```

### 9.3.9. Animation Shorthand

```css
.box {
    /* name | duration | timing-function | delay | iteration-count | direction | fill-mode | play-state */
    animation: fadeIn 1s ease 0s 1 normal forwards running;

    /* Common */
    animation: slideLeft 2s ease-in-out infinite;

    /* Multiple animations */
    animation:
        fadeIn 1s ease,
        slideUp 2s ease-out 0.5s;
}
```

## 9.4. Practical Examples

### 9.4.1. Fade In

```css
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.fade-in {
    animation: fadeIn 0.5s ease-in forwards;
}
```

### 9.4.2. Slide In

```css
@keyframes slideInLeft {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

.slide-in {
    animation: slideInLeft 0.5s ease-out forwards;
}
```

### 9.4.3. Bounce

```css
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-30px);
    }
    60% {
        transform: translateY(-15px);
    }
}

.bounce {
    animation: bounce 2s ease infinite;
}
```

### 9.4.4. Pulse

```css
@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
}

.pulse {
    animation: pulse 1s ease-in-out infinite;
}
```

### 9.4.5. Shake

```css
@keyframes shake {
    0%, 100% {
        transform: translateX(0);
    }
    10%, 30%, 50%, 70%, 90% {
        transform: translateX(-10px);
    }
    20%, 40%, 60%, 80% {
        transform: translateX(10px);
    }
}

.shake {
    animation: shake 0.5s ease;
}
```

### 9.4.6. Rotate

```css
@keyframes rotate {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

.rotate {
    animation: rotate 2s linear infinite;
}
```

### 9.4.7. Loading Spinner

```css
@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

.spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #f3f3f3;
    border-top: 5px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}
```

### 9.4.8. Typing Effect

```css
@keyframes typing {
    from {
        width: 0;
    }
    to {
        width: 100%;
    }
}

@keyframes blink {
    50% {
        border-color: transparent;
    }
}

.typewriter {
    overflow: hidden;
    border-right: 2px solid #333;
    white-space: nowrap;
    animation:
        typing 3.5s steps(40, end),
        blink 0.75s step-end infinite;
}
```

### 9.4.9. Gradient Animation

```css
@keyframes gradientShift {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.gradient-bg {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}
```

### 9.4.10. Float

```css
@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-20px);
    }
}

.float {
    animation: float 3s ease-in-out infinite;
}
```

## 9.5. Complex Animations

### 9.5.1. Multi-Step Animation

```css
@keyframes complexMove {
    0% {
        transform: translate(0, 0) scale(1) rotate(0deg);
        opacity: 1;
    }
    25% {
        transform: translate(100px, 0) scale(1.2) rotate(90deg);
        opacity: 0.8;
    }
    50% {
        transform: translate(100px, 100px) scale(1) rotate(180deg);
        opacity: 0.6;
    }
    75% {
        transform: translate(0, 100px) scale(0.8) rotate(270deg);
        opacity: 0.8;
    }
    100% {
        transform: translate(0, 0) scale(1) rotate(360deg);
        opacity: 1;
    }
}
```

### 9.5.2. Staggered Animations

```css
.item:nth-child(1) { animation-delay: 0s; }
.item:nth-child(2) { animation-delay: 0.1s; }
.item:nth-child(3) { animation-delay: 0.2s; }
.item:nth-child(4) { animation-delay: 0.3s; }
.item:nth-child(5) { animation-delay: 0.4s; }
```

### 9.5.3. Combining Multiple Animations

```css
.box {
    animation:
        fadeIn 1s ease,
        slideUp 1s ease,
        rotate 2s linear infinite;
}
```

## 9.6. Performance Tips

```css
/* Good: Use transform and opacity */
@keyframes goodAnimation {
    to {
        transform: translateX(100px);
        opacity: 0.5;
    }
}

/* Avoid: Animating width/height/top/left */
@keyframes avoidAnimation {
    to {
        width: 200px;  /* Causes reflow */
        left: 100px;   /* Causes reflow */
    }
}

/* Use will-change for better performance */
.animated {
    will-change: transform, opacity;
    animation: complexMove 2s ease;
}
```

## 9.7. JavaScript Control

```javascript
// Play/Pause
element.style.animationPlayState = 'paused';
element.style.animationPlayState = 'running';

// Listen to events
element.addEventListener('animationstart', () => {
    console.log('Animation started');
});

element.addEventListener('animationend', () => {
    console.log('Animation ended');
});

element.addEventListener('animationiteration', () => {
    console.log('Animation iteration');
});
```

---

**Kết luận:** CSS Animations powerful hơn transitions, cho phép multi-step animations. Combine với @keyframes để tạo complex effects.

**Chương tiếp theo:** Transforms
