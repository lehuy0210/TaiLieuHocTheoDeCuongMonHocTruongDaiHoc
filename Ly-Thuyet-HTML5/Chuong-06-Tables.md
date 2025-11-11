# CHƯƠNG 6: TABLES (BẢNG)

## 6.1. Table Basics

### 6.1.1. Cấu trúc cơ bản

```html
<table>
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
        <th>Header 3</th>
    </tr>
    <tr>
        <td>Data 1</td>
        <td>Data 2</td>
        <td>Data 3</td>
    </tr>
    <tr>
        <td>Data 4</td>
        <td>Data 5</td>
        <td>Data 6</td>
    </tr>
</table>
```

### 6.1.2. Table Elements

- `<table>`: Định nghĩa table
- `<tr>`: Table row (hàng)
- `<th>`: Table header cell (ô tiêu đề)
- `<td>`: Table data cell (ô dữ liệu)
- `<thead>`: Table header section
- `<tbody>`: Table body section
- `<tfoot>`: Table footer section
- `<caption>`: Table caption
- `<col>`: Column properties
- `<colgroup>`: Group of columns

## 6.2. Complete Table Structure

```html
<table>
    <caption>Sales Report Q4 2023</caption>

    <colgroup>
        <col style="background-color: #f0f0f0">
        <col span="2" style="background-color: #e0e0e0">
    </colgroup>

    <thead>
        <tr>
            <th>Month</th>
            <th>Revenue</th>
            <th>Profit</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>October</td>
            <td>$10,000</td>
            <td>$2,000</td>
        </tr>
        <tr>
            <td>November</td>
            <td>$12,000</td>
            <td>$2,400</td>
        </tr>
        <tr>
            <td>December</td>
            <td>$15,000</td>
            <td>$3,000</td>
        </tr>
    </tbody>

    <tfoot>
        <tr>
            <th>Total</th>
            <td>$37,000</td>
            <td>$7,400</td>
        </tr>
    </tfoot>
</table>
```

## 6.3. Table Attributes

### 6.3.1. colspan - Merge Columns

```html
<table border="1">
    <tr>
        <th>Name</th>
        <th colspan="2">Contact</th>
    </tr>
    <tr>
        <td>John Doe</td>
        <td>Email</td>
        <td>Phone</td>
    </tr>
    <tr>
        <td>Jane Smith</td>
        <td>jane@email.com</td>
        <td>123-456-7890</td>
    </tr>
</table>
```

### 6.3.2. rowspan - Merge Rows

```html
<table border="1">
    <tr>
        <th>Name</th>
        <th>Subject</th>
        <th>Grade</th>
    </tr>
    <tr>
        <td rowspan="2">John Doe</td>
        <td>Math</td>
        <td>A</td>
    </tr>
    <tr>
        <td>Science</td>
        <td>B</td>
    </tr>
    <tr>
        <td rowspan="2">Jane Smith</td>
        <td>Math</td>
        <td>B</td>
    </tr>
    <tr>
        <td>Science</td>
        <td>A</td>
    </tr>
</table>
```

### 6.3.3. Combining colspan và rowspan

```html
<table border="1">
    <tr>
        <th rowspan="2">Name</th>
        <th colspan="2">Details</th>
    </tr>
    <tr>
        <th>Age</th>
        <th>City</th>
    </tr>
    <tr>
        <td>John</td>
        <td>25</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>30</td>
        <td>London</td>
    </tr>
</table>
```

## 6.4. Table Headers

### 6.4.1. scope Attribute

```html
<table>
    <thead>
        <tr>
            <th scope="col">Product</th>
            <th scope="col">Price</th>
            <th scope="col">Quantity</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">Laptop</th>
            <td>$999</td>
            <td>5</td>
        </tr>
        <tr>
            <th scope="row">Mouse</th>
            <td>$25</td>
            <td>20</td>
        </tr>
    </tbody>
</table>
```

**Values của scope:**
- `col`: Header cho column
- `row`: Header cho row
- `colgroup`: Header cho group of columns
- `rowgroup`: Header cho group of rows

### 6.4.2. headers Attribute

```html
<table>
    <thead>
        <tr>
            <th id="name">Name</th>
            <th id="math">Math</th>
            <th id="sci">Science</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td headers="name">John</td>
            <td headers="math">95</td>
            <td headers="sci">88</td>
        </tr>
        <tr>
            <td headers="name">Jane</td>
            <td headers="math">92</td>
            <td headers="sci">95</td>
        </tr>
    </tbody>
</table>
```

## 6.5. Styling Tables

### 6.5.1. Basic Styling

```html
<style>
table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #4CAF50;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #ddd;
}
</style>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John Doe</td>
            <td>john@example.com</td>
            <td>123-456-7890</td>
        </tr>
        <tr>
            <td>Jane Smith</td>
            <td>jane@example.com</td>
            <td>098-765-4321</td>
        </tr>
    </tbody>
</table>
```

### 6.5.2. Striped Tables

```css
tr:nth-child(odd) {
    background-color: #f9f9f9;
}

tr:nth-child(even) {
    background-color: #ffffff;
}
```

### 6.5.3. Bordered Tables

```css
/* Border all cells */
table {
    border-collapse: collapse;
}

th, td {
    border: 1px solid black;
}

/* Border only outside */
table {
    border: 2px solid black;
}

/* Rounded corners */
table {
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 10px;
    overflow: hidden;
}
```

### 6.5.4. Responsive Tables

**Scrollable table:**
```html
<div class="table-container">
    <table>
        <!-- Table content -->
    </table>
</div>

<style>
.table-container {
    overflow-x: auto;
}

table {
    min-width: 600px;
}
</style>
```

**Stack on mobile:**
```html
<style>
@media screen and (max-width: 600px) {
    table, thead, tbody, th, td, tr {
        display: block;
    }

    thead tr {
        position: absolute;
        top: -9999px;
        left: -9999px;
    }

    tr {
        border: 1px solid #ccc;
        margin-bottom: 10px;
    }

    td {
        border: none;
        position: relative;
        padding-left: 50%;
    }

    td:before {
        position: absolute;
        left: 6px;
        content: attr(data-label);
        font-weight: bold;
    }
}
</style>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td data-label="Name">John Doe</td>
            <td data-label="Email">john@example.com</td>
            <td data-label="Phone">123-456-7890</td>
        </tr>
    </tbody>
</table>
```

## 6.6. Practical Examples

### 6.6.1. Pricing Table

```html
<table class="pricing-table">
    <caption>Pricing Plans</caption>
    <thead>
        <tr>
            <th>Feature</th>
            <th>Basic</th>
            <th>Pro</th>
            <th>Enterprise</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Price</td>
            <td>$9/month</td>
            <td>$29/month</td>
            <td>$99/month</td>
        </tr>
        <tr>
            <td>Storage</td>
            <td>10 GB</td>
            <td>100 GB</td>
            <td>Unlimited</td>
        </tr>
        <tr>
            <td>Users</td>
            <td>1</td>
            <td>10</td>
            <td>Unlimited</td>
        </tr>
        <tr>
            <td>Support</td>
            <td>Email</td>
            <td>Priority</td>
            <td>24/7 Dedicated</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td></td>
            <td><button>Choose Basic</button></td>
            <td><button>Choose Pro</button></td>
            <td><button>Choose Enterprise</button></td>
        </tr>
    </tfoot>
</table>
```

### 6.6.2. Schedule Table

```html
<table class="schedule">
    <caption>Class Schedule</caption>
    <thead>
        <tr>
            <th>Time</th>
            <th>Monday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">8:00 - 9:00</th>
            <td>Math</td>
            <td>English</td>
            <td>Math</td>
            <td>English</td>
            <td>Math</td>
        </tr>
        <tr>
            <th scope="row">9:00 - 10:00</th>
            <td>Science</td>
            <td>History</td>
            <td>Science</td>
            <td>History</td>
            <td>Science</td>
        </tr>
        <tr>
            <th scope="row">10:00 - 11:00</th>
            <td colspan="5" class="break">Break</td>
        </tr>
    </tbody>
</table>
```

### 6.6.3. Financial Report

```html
<table class="financial-report">
    <caption>Quarterly Financial Report</caption>
    <colgroup>
        <col>
        <col span="3" class="quarterly">
        <col class="total">
    </colgroup>
    <thead>
        <tr>
            <th rowspan="2">Item</th>
            <th colspan="3">Quarter</th>
            <th rowspan="2">Total</th>
        </tr>
        <tr>
            <th>Q1</th>
            <th>Q2</th>
            <th>Q3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">Revenue</th>
            <td>$100,000</td>
            <td>$120,000</td>
            <td>$150,000</td>
            <td>$370,000</td>
        </tr>
        <tr>
            <th scope="row">Expenses</th>
            <td>$70,000</td>
            <td>$80,000</td>
            <td>$90,000</td>
            <td>$240,000</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th scope="row">Profit</th>
            <td>$30,000</td>
            <td>$40,000</td>
            <td>$60,000</td>
            <td>$130,000</td>
        </tr>
    </tfoot>
</table>
```

## 6.7. Accessibility

### 6.7.1. Caption

```html
<table>
    <caption>Student Grades - Fall 2023</caption>
    <!-- Table content -->
</table>
```

### 6.7.2. Scope và Headers

```html
<table>
    <thead>
        <tr>
            <th scope="col" id="name">Name</th>
            <th scope="col" id="grade">Grade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td headers="name">John</td>
            <td headers="grade">A</td>
        </tr>
    </tbody>
</table>
```

### 6.7.3. Summary (HTML5 không còn dùng)

```html
<!-- HTML4 - Deprecated -->
<table summary="This table shows student grades">

<!-- HTML5 - Dùng caption hoặc figure -->
<figure>
    <figcaption>
        This table shows student grades for Fall 2023
    </figcaption>
    <table>
        <!-- Content -->
    </table>
</figure>
```

### 6.7.4. ARIA Attributes

```html
<table role="table" aria-label="Student Information">
    <thead role="rowgroup">
        <tr role="row">
            <th role="columnheader">Name</th>
            <th role="columnheader">Age</th>
        </tr>
    </thead>
    <tbody role="rowgroup">
        <tr role="row">
            <td role="cell">John</td>
            <td role="cell">25</td>
        </tr>
    </tbody>
</table>
```

## 6.8. Complex Tables

### 6.8.1. Multi-level Headers

```html
<table>
    <thead>
        <tr>
            <th rowspan="2">Student</th>
            <th colspan="2">Semester 1</th>
            <th colspan="2">Semester 2</th>
        </tr>
        <tr>
            <th>Math</th>
            <th>Science</th>
            <th>Math</th>
            <th>Science</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>85</td>
            <td>90</td>
            <td>88</td>
            <td>92</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>92</td>
            <td>88</td>
            <td>95</td>
            <td>90</td>
        </tr>
    </tbody>
</table>
```

### 6.8.2. Nested Tables (Không khuyến khích)

```html
<!-- Tránh nested tables, dùng colspan/rowspan thay thế -->
<table>
    <tr>
        <td>
            <table>
                <tr>
                    <td>Nested</td>
                </tr>
            </table>
        </td>
    </tr>
</table>
```

## 6.9. Sortable Tables

### 6.9.1. HTML Structure

```html
<table id="sortable">
    <thead>
        <tr>
            <th onclick="sortTable(0)">Name ▲▼</th>
            <th onclick="sortTable(1)">Age ▲▼</th>
            <th onclick="sortTable(2)">City ▲▼</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>25</td>
            <td>New York</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>30</td>
            <td>London</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>22</td>
            <td>Paris</td>
        </tr>
    </tbody>
</table>
```

### 6.9.2. JavaScript Sort Function

```javascript
function sortTable(columnIndex) {
    const table = document.getElementById('sortable');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    const sortedRows = rows.sort((a, b) => {
        const aValue = a.cells[columnIndex].textContent;
        const bValue = b.cells[columnIndex].textContent;

        // Numeric sort if both are numbers
        if (!isNaN(aValue) && !isNaN(bValue)) {
            return aValue - bValue;
        }

        // String sort
        return aValue.localeCompare(bValue);
    });

    // Clear tbody
    tbody.innerHTML = '';

    // Append sorted rows
    sortedRows.forEach(row => tbody.appendChild(row));
}
```

## 6.10. Data Tables Best Practices

### 6.10.1. Structure

1. **Luôn dùng `<thead>`, `<tbody>`, `<tfoot>`**
2. **Dùng `<th>` cho headers với scope**
3. **Dùng `<caption>` để mô tả table**
4. **Avoid nested tables**

### 6.10.2. Styling

1. **Consistent spacing và alignment**
2. **Zebra striping cho dễ đọc**
3. **Highlight on hover**
4. **Responsive design**

### 6.10.3. Performance

```html
<!-- Limit rows per page -->
<!-- Use pagination -->
<!-- Virtual scrolling cho large datasets -->
```

### 6.10.4. Accessibility

1. **Caption và summary**
2. **scope và headers attributes**
3. **ARIA labels khi cần**
4. **Keyboard navigation**

## 6.11. Bài tập thực hành

### Bài 1: Basic Table
Tạo bảng với:
- 5 rows, 4 columns
- Header row
- Proper structure với thead, tbody
- Basic styling

### Bài 2: Complex Table
Tạo bảng với:
- Multi-level headers
- colspan và rowspan
- tfoot cho totals
- Responsive design

### Bài 3: Pricing Table
Tạo pricing comparison table với:
- 3 pricing tiers
- Feature comparison
- Highlighted recommended plan
- Call-to-action buttons

### Bài 4: Sortable Data Table
Tạo:
- Table với student data
- Sortable columns
- Searchable
- Pagination

---

**Kết luận:** Trong chương này, chúng ta đã học về tables trong HTML5, bao gồm cấu trúc, styling, responsive design, accessibility và best practices. Chương tiếp theo sẽ tìm hiểu về Forms và Input.
