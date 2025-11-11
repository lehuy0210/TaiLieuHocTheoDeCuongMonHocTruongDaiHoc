# CHƯƠNG 5: TYPOGRAPHY & FONTS

## 5.1. Web Fonts

### 5.1.1. @font-face

```css
@font-face {
    font-family: 'MyFont';
    src: url('myfont.woff2') format('woff2'),
         url('myfont.woff') format('woff');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}

.text {
    font-family: 'MyFont', sans-serif;
}
```

### 5.1.2. Google Fonts

```html
<!-- In HTML -->
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
```

```css
/* In CSS */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
}
```

### 5.1.3. font-display

```css
@font-face {
    font-family: 'MyFont';
    src: url('font.woff2');
    font-display: swap;      /* Recommended */
    font-display: block;     /* Wait for font */
    font-display: fallback;  /* Short block, swap */
    font-display: optional;  /* Use only if cached */
}
```

## 5.2. Font Properties

### 5.2.1. font-family

```css
.text {
    /* Web fonts */
    font-family: 'Roboto', sans-serif;

    /* System fonts */
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;

    /* Generic families */
    font-family: serif;
    font-family: sans-serif;
    font-family: monospace;
    font-family: cursive;
    font-family: fantasy;
}

/* System font stack */
body {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
}
```

### 5.2.2. font-size

```css
.text {
    /* Absolute */
    font-size: 16px;
    font-size: 12pt;

    /* Relative */
    font-size: 1.2em;    /* Relative to parent */
    font-size: 1.2rem;   /* Relative to root */

    /* Viewport units */
    font-size: 5vw;

    /* Keywords */
    font-size: small;
    font-size: medium;
    font-size: large;
    font-size: larger;
    font-size: smaller;
}

/* Responsive typography */
html {
    font-size: 16px;
}

h1 {
    font-size: 2.5rem;  /* 40px */
}

p {
    font-size: 1rem;    /* 16px */
}

small {
    font-size: 0.875rem; /* 14px */
}
```

### 5.2.3. font-weight

```css
.text {
    font-weight: normal;   /* 400 */
    font-weight: bold;     /* 700 */
    font-weight: lighter;
    font-weight: bolder;

    /* Numeric values */
    font-weight: 100;  /* Thin */
    font-weight: 200;  /* Extra Light */
    font-weight: 300;  /* Light */
    font-weight: 400;  /* Normal */
    font-weight: 500;  /* Medium */
    font-weight: 600;  /* Semi Bold */
    font-weight: 700;  /* Bold */
    font-weight: 800;  /* Extra Bold */
    font-weight: 900;  /* Black */
}
```

### 5.2.4. font-style

```css
.text {
    font-style: normal;
    font-style: italic;
    font-style: oblique;
    font-style: oblique 10deg;
}
```

### 5.2.5. font Shorthand

```css
.text {
    /* font: style weight size/line-height family */
    font: italic bold 16px/1.5 'Arial', sans-serif;
    font: 1rem/1.6 system-ui, sans-serif;
}
```

## 5.3. Text Properties

### 5.3.1. color

```css
.text {
    color: #333;
    color: rgb(51, 51, 51);
    color: rgba(0, 0, 0, 0.8);
    color: hsl(0, 0%, 20%);
    color: currentColor;  /* Inherit from parent */
}
```

### 5.3.2. text-align

```css
.text {
    text-align: left;
    text-align: right;
    text-align: center;
    text-align: justify;
    text-align: start;   /* Same as left in LTR */
    text-align: end;     /* Same as right in LTR */
}
```

### 5.3.3. text-decoration

```css
.text {
    text-decoration: underline;
    text-decoration: overline;
    text-decoration: line-through;
    text-decoration: none;

    /* Detailed */
    text-decoration-line: underline;
    text-decoration-color: red;
    text-decoration-style: solid;
    text-decoration-style: wavy;
    text-decoration-style: dashed;
    text-decoration-style: dotted;
    text-decoration-thickness: 2px;

    /* Shorthand */
    text-decoration: underline wavy red 2px;
}

/* Link styles */
a {
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```

### 5.3.4. text-transform

```css
.text {
    text-transform: uppercase;   /* ALL CAPS */
    text-transform: lowercase;   /* all lowercase */
    text-transform: capitalize;  /* First Letter */
    text-transform: none;
}
```

### 5.3.5. text-shadow

```css
.text {
    /* x-offset | y-offset | blur | color */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

/* Multiple shadows */
.text {
    text-shadow:
        2px 2px 0 white,
        4px 4px 0 #333;
}

/* Glow effect */
.glow {
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
}

/* 3D effect */
.three-d {
    text-shadow:
        1px 1px 0 #ccc,
        2px 2px 0 #c9c9c9,
        3px 3px 0 #bbb,
        4px 4px 0 #b9b9b9,
        5px 5px 0 #aaa,
        6px 6px 10px rgba(0, 0, 0, 0.5);
}
```

## 5.4. Line and Letter Spacing

### 5.4.1. line-height

```css
.text {
    line-height: 1.6;      /* Recommended for body text */
    line-height: 24px;
    line-height: 1.5em;
    line-height: 150%;
}

/* Good for readability */
body {
    font-size: 16px;
    line-height: 1.6;  /* 25.6px */
}

h1 {
    line-height: 1.2;  /* Tighter for headings */
}
```

### 5.4.2. letter-spacing

```css
.text {
    letter-spacing: 0.05em;
    letter-spacing: 2px;
    letter-spacing: -1px;  /* Tighter */
}

/* Headings */
h1 {
    letter-spacing: -0.02em;  /* Slightly tighter */
}

/* All caps */
.uppercase {
    text-transform: uppercase;
    letter-spacing: 0.1em;  /* More spacing */
}
```

### 5.4.3. word-spacing

```css
.text {
    word-spacing: 5px;
    word-spacing: 0.3em;
}
```

## 5.5. Text Overflow and Wrapping

### 5.5.1. white-space

```css
.text {
    white-space: normal;    /* Default */
    white-space: nowrap;    /* No wrapping */
    white-space: pre;       /* Preserve spaces & newlines */
    white-space: pre-wrap;  /* Preserve & wrap */
    white-space: pre-line;  /* Collapse spaces, preserve newlines */
}
```

### 5.5.2. text-overflow

```css
/* Ellipsis (must have nowrap and overflow) */
.truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Clip */
.text {
    text-overflow: clip;
}
```

### 5.5.3. word-break

```css
.text {
    word-break: normal;
    word-break: break-all;    /* Break anywhere */
    word-break: keep-all;     /* Don't break words */
}
```

### 5.5.4. word-wrap / overflow-wrap

```css
.text {
    overflow-wrap: normal;
    overflow-wrap: break-word;  /* Break long words */
    overflow-wrap: anywhere;
}
```

### 5.5.5. hyphens

```css
.text {
    hyphens: none;
    hyphens: manual;  /* Use &shy; in HTML */
    hyphens: auto;    /* Automatic hyphenation */
}
```

## 5.6. Advanced Typography

### 5.6.1. text-indent

```css
p {
    text-indent: 2em;  /* First line indent */
}

/* Hanging indent */
.hanging {
    padding-left: 2em;
    text-indent: -2em;
}
```

### 5.6.2. direction and writing-mode

```css
.rtl {
    direction: rtl;  /* Right to left */
}

.vertical {
    writing-mode: vertical-rl;  /* Vertical right to left */
    writing-mode: vertical-lr;  /* Vertical left to right */
}
```

### 5.6.3. Font Variants

```css
.text {
    font-variant: small-caps;
    font-variant-caps: small-caps;
    font-variant-numeric: tabular-nums;
    font-variant-ligatures: common-ligatures;
}
```

### 5.6.4. Variable Fonts

```css
@font-face {
    font-family: 'Variable';
    src: url('variable-font.woff2') format('woff2-variations');
    font-weight: 100 900;  /* Range */
}

.text {
    font-family: 'Variable';
    font-weight: 450;  /* Any value in range */
    font-variation-settings: 'wght' 450, 'wdth' 100;
}
```

## 5.7. Practical Examples

### 5.7.1. Responsive Typography

```css
html {
    font-size: 16px;
}

@media (min-width: 768px) {
    html {
        font-size: 18px;
    }
}

/* Fluid typography */
html {
    font-size: calc(16px + (24 - 16) * ((100vw - 320px) / (1920 - 320)));
}

/* Clamp (modern) */
html {
    font-size: clamp(16px, 2vw, 24px);
}
```

### 5.7.2. Readable Text

```css
.article {
    max-width: 65ch;  /* Optimal line length */
    font-size: 18px;
    line-height: 1.6;
    color: #333;
}

.article h1 {
    font-size: 2.5em;
    line-height: 1.2;
    margin-bottom: 0.5em;
}

.article p {
    margin-bottom: 1.5em;
}
```

### 5.7.3. Multiline Truncation

```css
.truncate-lines {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}
```

---

**Kết luận:** Typography là key để tạo readable và beautiful text. Font loading, spacing, và responsive typography là important considerations.

**Chương tiếp theo:** Flexbox
