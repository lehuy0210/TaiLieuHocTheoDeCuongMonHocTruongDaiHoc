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

## 6.6.4. Data Table với Sorting và Searching

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Interactive Data Table</title>
    <style>
        .table-container {
            max-width: 900px;
            margin: 20px auto;
            padding: 20px;
        }
        .search-box {
            margin-bottom: 20px;
        }
        .search-box input {
            padding: 10px;
            width: 300px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        th {
            background: #2c3e50;
            color: white;
            padding: 15px;
            text-align: left;
            cursor: pointer;
            user-select: none;
        }
        th:hover {
            background: #34495e;
        }
        td {
            padding: 12px 15px;
            border-bottom: 1px solid #ecf0f1;
        }
        tr:hover {
            background: #f5f5f5;
        }
        .sort-indicator {
            margin-left: 5px;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="table-container">
        <h1>Employee Database</h1>

        <div class="search-box">
            <input type="text" id="searchInput" placeholder="Search by name, position, or department...">
        </div>

        <table id="dataTable">
            <thead>
                <tr>
                    <th onclick="sortTable(0)">Name <span class="sort-indicator">▼</span></th>
                    <th onclick="sortTable(1)">Position <span class="sort-indicator">▼</span></th>
                    <th onclick="sortTable(2)">Department <span class="sort-indicator">▼</span></th>
                    <th onclick="sortTable(3)">Salary <span class="sort-indicator">▼</span></th>
                    <th onclick="sortTable(4)">Start Date <span class="sort-indicator">▼</span></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Nguyễn Văn A</td>
                    <td>Software Engineer</td>
                    <td>IT</td>
                    <td>50,000,000đ</td>
                    <td>2020-01-15</td>
                </tr>
                <tr>
                    <td>Trần Thị B</td>
                    <td>Project Manager</td>
                    <td>Management</td>
                    <td>45,000,000đ</td>
                    <td>2019-06-20</td>
                </tr>
                <tr>
                    <td>Phạm Minh C</td>
                    <td>Designer</td>
                    <td>Design</td>
                    <td>35,000,000đ</td>
                    <td>2021-03-10</td>
                </tr>
                <tr>
                    <td>Hoàng Tuấn D</td>
                    <td>Senior Developer</td>
                    <td>IT</td>
                    <td>60,000,000đ</td>
                    <td>2018-09-05</td>
                </tr>
                <tr>
                    <td>Lý Thanh E</td>
                    <td>HR Specialist</td>
                    <td>HR</td>
                    <td>30,000,000đ</td>
                    <td>2021-11-01</td>
                </tr>
            </tbody>
        </table>
    </div>

    <script>
        let currentSort = { column: -1, ascending: true };

        // Search functionality
        document.getElementById('searchInput').addEventListener('keyup', (e) => {
            const searchTerm = e.target.value.toLowerCase();
            const table = document.getElementById('dataTable');
            const rows = table.querySelectorAll('tbody tr');

            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });

        // Sort functionality
        function sortTable(columnIndex) {
            const table = document.getElementById('dataTable');
            const tbody = table.querySelector('tbody');
            const rows = Array.from(tbody.querySelectorAll('tr'));

            const isNumeric = (str) => !isNaN(str.replace(/[^0-9.-]/g, ''));
            const getValue = (row) => row.cells[columnIndex].textContent.trim();

            rows.sort((a, b) => {
                const aVal = getValue(a);
                const bVal = getValue(b);

                let comparison = 0;
                if (isNumeric(aVal) && isNumeric(bVal)) {
                    const aNum = parseFloat(aVal.replace(/[^0-9.-]/g, ''));
                    const bNum = parseFloat(bVal.replace(/[^0-9.-]/g, ''));
                    comparison = aNum - bNum;
                } else {
                    comparison = aVal.localeCompare(bVal, 'vi');
                }

                if (currentSort.column === columnIndex) {
                    currentSort.ascending = !currentSort.ascending;
                } else {
                    currentSort.column = columnIndex;
                    currentSort.ascending = true;
                }

                return currentSort.ascending ? comparison : -comparison;
            });

            tbody.innerHTML = '';
            rows.forEach(row => tbody.appendChild(row));

            updateSortIndicators(columnIndex);
        }

        function updateSortIndicators(columnIndex) {
            const headers = document.querySelectorAll('th');
            headers.forEach((header, index) => {
                if (index === columnIndex) {
                    const indicator = currentSort.ascending ? '▲' : '▼';
                    header.querySelector('.sort-indicator').textContent = indicator;
                } else {
                    header.querySelector('.sort-indicator').textContent = '▼';
                }
            });
        }
    </script>
</body>
</html>
```

### 6.6.5. Responsive Table cho Mobile

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Responsive Table</title>
    <style>
        * {
            box-sizing: border-box;
        }

        .table-container {
            max-width: 1000px;
            margin: 20px auto;
            padding: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #3498db;
            color: white;
        }

        tbody tr:nth-child(even) {
            background-color: #ecf0f1;
        }

        /* Mobile responsive */
        @media screen and (max-width: 768px) {
            table, thead, tbody, th, td, tr {
                display: block;
                width: 100%;
            }

            thead tr {
                position: absolute;
                top: -9999px;
                left: -9999px;
            }

            tr {
                margin-bottom: 15px;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 10px;
            }

            td {
                padding-left: 50%;
                position: relative;
                border: none;
                padding-bottom: 10px;
            }

            /* Label từ data attribute */
            td:before {
                content: attr(data-label);
                position: absolute;
                left: 10px;
                font-weight: bold;
                color: #3498db;
                width: 40%;
            }
        }
    </style>
</head>
<body>
    <div class="table-container">
        <h1>Sản phẩm bán chạy</h1>

        <table>
            <thead>
                <tr>
                    <th>Tên sản phẩm</th>
                    <th>Giá</th>
                    <th>Số lượng bán</th>
                    <th>Đánh giá</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td data-label="Tên sản phẩm">Laptop Dell XPS 13</td>
                    <td data-label="Giá">25,990,000đ</td>
                    <td data-label="Số lượng bán">152</td>
                    <td data-label="Đánh giá">4.8/5</td>
                </tr>
                <tr>
                    <td data-label="Tên sản phẩm">Chuột Logitech MX</td>
                    <td data-label="Giá">2,490,000đ</td>
                    <td data-label="Số lượng bán">485</td>
                    <td data-label="Đánh giá">4.6/5</td>
                </tr>
                <tr>
                    <td data-label="Tên sản phẩm">Bàn phím Mechanical</td>
                    <td data-label="Giá">3,990,000đ</td>
                    <td data-label="Số lượng bán">320</td>
                    <td data-label="Đánh giá">4.7/5</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```

## 6.7. Tips & Tricks

### Tip 1: Sử dụng colspan và rowspan hiệu quả
```html
<!-- ❌ Sai: Lạm dụng colspan/rowspan -->
<table>
    <tr>
        <td colspan="10">Header</td>
    </tr>
</table>

<!-- ✅ Đúng: Sử dụng khi cần thiết -->
<table>
    <tr>
        <th colspan="2">Contact Info</th>
        <th>Location</th>
    </tr>
</table>
```

### Tip 2: Table striping cho dễ đọc
```css
tbody tr:nth-child(odd) {
    background-color: #ffffff;
}

tbody tr:nth-child(even) {
    background-color: #f9f9f9;
}

tbody tr:hover {
    background-color: #e8e8e8;
}
```

### Tip 3: Percentage-based column widths
```html
<table style="width: 100%;">
    <colgroup>
        <col style="width: 20%;">
        <col style="width: 30%;">
        <col style="width: 25%;">
        <col style="width: 25%;">
    </colgroup>
</table>
```

### Tip 4: Scrollable table container
```css
.table-container {
    overflow-x: auto;
    max-width: 100%;
}

table {
    min-width: 600px;
}
```

### Tip 5: Fixed header với scrollable body
```html
<style>
    .table-wrapper {
        max-height: 400px;
        overflow-y: auto;
    }

    table {
        width: 100%;
    }

    thead {
        position: sticky;
        top: 0;
        background: #2c3e50;
        z-index: 10;
    }
</style>

<div class="table-wrapper">
    <table>
        <thead><!-- sticky headers --></thead>
        <tbody><!-- scrollable content --></tbody>
    </table>
</div>
```

### Tip 6: Pagination cho large datasets
```html
<div id="table-container"></div>
<div id="pagination"></div>

<script>
    const pageSize = 10;
    let currentPage = 1;

    function displayPage(data, page) {
        const start = (page - 1) * pageSize;
        const end = start + pageSize;
        const pageData = data.slice(start, end);

        // Render table
        renderTable(pageData);

        // Render pagination buttons
        const totalPages = Math.ceil(data.length / pageSize);
        renderPagination(totalPages, page);
    }
</script>
```

### Tip 7: Export table to CSV
```javascript
function exportTableToCSV(tableId, filename) {
    const csv = [];
    const table = document.getElementById(tableId);

    for (let row of table.rows) {
        const rowData = [];
        for (let cell of row.cells) {
            rowData.push('"' + cell.textContent + '"');
        }
        csv.push(rowData.join(','));
    }

    const csvContent = csv.join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
}

// Usage
exportTableToCSV('myTable', 'data.csv');
```

### Tip 8: Table filtering
```javascript
function filterTable(tableId, filterValue, columnIndex) {
    const table = document.getElementById(tableId);
    const rows = table.querySelectorAll('tbody tr');

    rows.forEach(row => {
        const cell = row.cells[columnIndex];
        if (cell.textContent.includes(filterValue)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}
```

### Tip 9: Merge cells dinamically
```javascript
function mergeCells(tableId, rowStart, rowEnd, colIndex) {
    const table = document.getElementById(tableId);
    const rows = table.querySelectorAll('tbody tr');

    // Set rowspan
    rows[rowStart].cells[colIndex].rowSpan = rowEnd - rowStart + 1;

    // Hide merged cells
    for (let i = rowStart + 1; i <= rowEnd; i++) {
        rows[i].cells[colIndex].style.display = 'none';
    }
}
```

### Tip 10: Keyboard navigation
```javascript
function enableTableKeyboardNav(tableId) {
    const table = document.getElementById(tableId);
    let selectedRow = 0;

    table.addEventListener('keydown', (e) => {
        const rows = table.querySelectorAll('tbody tr');

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            rows[selectedRow].style.background = '';
            selectedRow = Math.min(selectedRow + 1, rows.length - 1);
            rows[selectedRow].style.background = '#e8e8e8';
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            rows[selectedRow].style.background = '';
            selectedRow = Math.max(selectedRow - 1, 0);
            rows[selectedRow].style.background = '#e8e8e8';
        }
    });
}
```

## 6.8. Common Mistakes

### Lỗi 1: Không sử dụng thead, tbody, tfoot
```html
<!-- ❌ Sai -->
<table>
    <tr><th>Name</th></tr>
    <tr><td>John</td></tr>
</table>

<!-- ✅ Đúng -->
<table>
    <thead>
        <tr><th>Name</th></tr>
    </thead>
    <tbody>
        <tr><td>John</td></tr>
    </tbody>
</table>
```

### Lỗi 2: Quên set scope attribute
```html
<!-- ❌ Sai: Không accessible -->
<table>
    <tr>
        <th>Name</th>
        <th>Email</th>
    </tr>
</table>

<!-- ✅ Đúng -->
<table>
    <tr>
        <th scope="col">Name</th>
        <th scope="col">Email</th>
    </tr>
</table>
```

### Lỗi 3: Table layout quá phức tạp
```html
<!-- ❌ Sai: Quá nhiều colspan/rowspan -->
<table>
    <tr>
        <td colspan="5" rowspan="3">Complex</td>
    </tr>
</table>

<!-- ✅ Đúng: Đơn giản, rõ ràng -->
<table>
    <tr>
        <th>A</th>
        <th>B</th>
    </tr>
</table>
```

### Lỗi 4: Không có caption hoặc summary
```html
<!-- ❌ Sai: Không có mô tả -->
<table>
    <tr><th>Data</th></tr>
</table>

<!-- ✅ Đúng: Có caption -->
<table>
    <caption>Sales Data Q4 2024</caption>
    <tr><th>Data</th></tr>
</table>
```

### Lỗi 5: Dùng table cho layout (outdated)
```html
<!-- ❌ Sai: Dùng table cho layout -->
<table>
    <tr>
        <td width="200">Sidebar</td>
        <td>Main content</td>
    </tr>
</table>

<!-- ✅ Đúng: Dùng CSS Grid/Flexbox -->
<div style="display: grid; grid-template-columns: 200px 1fr;">
    <aside>Sidebar</aside>
    <main>Main content</main>
</div>
```

### Lỗi 6: Không responsive
```html
<!-- ❌ Sai: Fixed width -->
<table style="width: 1200px;"></table>

<!-- ✅ Đúng: Responsive -->
<div class="table-container" style="overflow-x: auto;">
    <table style="width: 100%; min-width: 600px;"></table>
</div>
```

### Lỗi 7: Không handle empty cells
```html
<!-- ❌ Sai: Empty cells gây confusion -->
<tr>
    <td>John</td>
    <td></td>
    <td>NYC</td>
</tr>

<!-- ✅ Đúng: Rõ ràng hoặc use N/A -->
<tr>
    <td>John</td>
    <td>-</td>
    <td>NYC</td>
</tr>
```

### Lỗi 8: Quên border-collapse
```css
/* ❌ Sai: Double borders */
table {
    border: 1px solid #ddd;
}
th, td {
    border: 1px solid #ddd;
}

/* ✅ Đúng: Collapse borders */
table {
    border-collapse: collapse;
    border: 1px solid #ddd;
}
th, td {
    border: 1px solid #ddd;
}
```

### Lỗi 9: Không use headers attribute cho complex tables
```html
<!-- ❌ Sai: Không rõ relationship -->
<table>
    <tr>
        <th>Product</th>
        <th>Q1</th>
        <th>Q2</th>
    </tr>
</table>

<!-- ✅ Đúng: Clear headers -->
<table>
    <tr>
        <th id="product">Product</th>
        <th id="q1">Q1</th>
        <th id="q2">Q2</th>
    </tr>
    <tr>
        <td headers="product">Laptop</td>
        <td headers="q1">100</td>
        <td headers="q2">150</td>
    </tr>
</table>
```

### Lỗi 10: Quên tối ưu hóa cho large tables
```html
<!-- ❌ Sai: Load 10,000 rows -->
<table>
    <tbody>
        <!-- 10,000 rows -->
    </tbody>
</table>

<!-- ✅ Đúng: Pagination/Virtual scroll -->
<table>
    <tbody id="tableBody">
        <!-- Max 50 rows visible -->
    </tbody>
</table>
<div id="pagination"></div>
```

## 6.9. Troubleshooting

### Issue 1: Table borders không hiển thị đúng
**Triệu chứng:** Borders bị đôi hoặc biến mất

**Giải pháp:**
```css
table {
    border-collapse: collapse; /* Tối ưu */
    /* hoặc */
    border-spacing: 0;
}

th, td {
    border: 1px solid #ddd;
}
```

### Issue 2: Table không responsive trên mobile
**Triệu chứng:** Table overflow, chiếm quá nhiều chỗ trên mobile

**Giải pháp:**
```html
<style>
    @media (max-width: 768px) {
        .table-container {
            overflow-x: auto;
        }

        table {
            min-width: 100%;
        }
    }
</style>

<div class="table-container">
    <table><!-- content --></table>
</div>
```

### Issue 3: Header không sticky khi scroll
**Triệu chứng:** Header cuộn khỏi view

**Giải pháp:**
```css
thead {
    position: sticky;
    top: 0;
    background: white;
    z-index: 10;
}
```

### Issue 4: Colspan/Rowspan gây confusion
**Triệu chứng:** Layout không align, cell bị miss

**Giải pháp:**
```html
<!-- Cẩn thận tính toán -->
<tr>
    <td colspan="2">A</td>
    <td>B</td>
    <!-- Row này cần 3 columns -->
</tr>
<tr>
    <td>C</td>
    <td>D</td>
    <td>E</td>
</tr>
```

### Issue 5: Table slow performance
**Triệu chứng:** Browser lag với large table

**Giải pháp:**
```javascript
// Use virtual scrolling
const virtualize = (container, items, itemHeight) => {
    const scrollTop = container.scrollTop;
    const visibleItems = Math.ceil(container.height / itemHeight);
    const startIndex = Math.floor(scrollTop / itemHeight);

    // Render only visible items
    renderRows(items.slice(startIndex, startIndex + visibleItems));
};
```

### Issue 6: Sorting không bekerja dengan currencies
**Triệu chứng:** $100 diangap < $20

**Giải pháp:**
```javascript
function sortNumeric(a, b) {
    const aNum = parseFloat(a.replace(/[^0-9.-]/g, ''));
    const bNum = parseFloat(b.replace(/[^0-9.-]/g, ''));
    return aNum - bNum;
}
```

### Issue 7: Colspan/Rowspan accessibility issues
**Triệu chứng:** Screen readers confuse

**Giải pháp:**
```html
<table>
    <tr>
        <th scope="col" id="name">Name</th>
        <th scope="colgroup" colspan="2" id="scores">Scores</th>
    </tr>
    <tr>
        <td headers="name">John</td>
        <td headers="scores">90</td>
        <td headers="scores">85</td>
    </tr>
</table>
```

### Issue 8: Table styling bị reset oleh browser defaults
**Triệu chứng:** Custom styles tidak apply

**Giải pháp:**
```css
table {
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
}

th, td {
    margin: 0;
    padding: 10px;
}
```

### Issue 9: Table export bị encode errors
**Triệu chứng:** Unicode characters bị corrupt

**Giải pháp:**
```javascript
function exportToCSV(table) {
    const csv = [];
    const rows = table.querySelectorAll('tr');

    rows.forEach(row => {
        const rowData = [];
        row.querySelectorAll('td, th').forEach(cell => {
            // Escape quotes dan newlines
            let text = cell.textContent.trim();
            text = text.replace(/"/g, '""');
            rowData.push(`"${text}"`);
        });
        csv.push(rowData.join(','));
    });

    // UTF-8 BOM
    const bom = '\uFEFF';
    const file = new Blob([bom + csv.join('\n')], {type: 'text/csv;charset=utf-8'});
    downloadFile(file, 'export.csv');
}
```

### Issue 10: Table alignment inconsistent
**Triệu chứng:** Text alignment không consistent

**Giải pháp:**
```css
/* Set default alignment */
th {
    text-align: left;
}

td {
    text-align: left;
}

/* Number columns */
td:nth-child(3),
td:nth-child(4) {
    text-align: right;
}
```

## 6.10. Advanced Topics

### Topic 1: Dynamic Table Generation từ JSON
```html
<!DOCTYPE html>
<html>
<body>
    <div id="table-container"></div>

    <script>
        const data = [
            { id: 1, name: 'John', email: 'john@example.com', salary: 50000 },
            { id: 2, name: 'Jane', email: 'jane@example.com', salary: 60000 },
            { id: 3, name: 'Bob', email: 'bob@example.com', salary: 55000 }
        ];

        function generateTableFromJSON(jsonData, containerId) {
            const container = document.getElementById(containerId);

            // Create table
            const table = document.createElement('table');
            table.style.cssText = 'border-collapse: collapse; width: 100%;';

            // Create header
            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');

            Object.keys(jsonData[0]).forEach(key => {
                const th = document.createElement('th');
                th.textContent = key.toUpperCase();
                th.style.cssText = 'border: 1px solid #ddd; padding: 10px; text-align: left; background: #f5f5f5;';
                headerRow.appendChild(th);
            });

            thead.appendChild(headerRow);
            table.appendChild(thead);

            // Create body
            const tbody = document.createElement('tbody');

            jsonData.forEach(item => {
                const row = document.createElement('tr');

                Object.values(item).forEach(value => {
                    const td = document.createElement('td');
                    td.textContent = value;
                    td.style.cssText = 'border: 1px solid #ddd; padding: 10px;';
                    row.appendChild(td);
                });

                tbody.appendChild(row);
            });

            table.appendChild(tbody);
            container.appendChild(table);
        }

        generateTableFromJSON(data, 'table-container');
    </script>
</body>
</html>
```

### Topic 2: Excel-like Table Editor
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .editable-table {
            border-collapse: collapse;
        }

        .editable-table td {
            border: 1px solid #ddd;
            padding: 5px;
            min-width: 100px;
        }

        .editable-table td.editing {
            padding: 0;
        }

        .editable-table input {
            width: 100%;
            border: none;
            padding: 5px;
        }
    </style>
</head>
<body>
    <table class="editable-table">
        <tr>
            <td>Cell 1</td>
            <td>Cell 2</td>
        </tr>
        <tr>
            <td>Cell 3</td>
            <td>Cell 4</td>
        </tr>
    </table>

    <script>
        const cells = document.querySelectorAll('.editable-table td');

        cells.forEach(cell => {
            cell.addEventListener('click', () => {
                const currentText = cell.textContent;
                cell.classList.add('editing');

                const input = document.createElement('input');
                input.value = currentText;
                input.focus();

                cell.innerHTML = '';
                cell.appendChild(input);

                const saveEdit = () => {
                    cell.textContent = input.value;
                    cell.classList.remove('editing');
                };

                input.addEventListener('blur', saveEdit);
                input.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') saveEdit();
                    if (e.key === 'Escape') {
                        cell.textContent = currentText;
                        cell.classList.remove('editing');
                    }
                });
            });
        });
    </script>
</body>
</html>
```

### Topic 3: Table with Drag-and-Drop Rows
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        tr[draggable="true"] {
            cursor: move;
            opacity: 0.7;
        }

        tr.drag-over {
            border-top: 3px solid blue;
        }
    </style>
</head>
<body>
    <table id="draggable-table">
        <thead>
            <tr>
                <th>Item</th>
            </tr>
        </thead>
        <tbody>
            <tr draggable="true" data-id="1">
                <td>Item 1</td>
            </tr>
            <tr draggable="true" data-id="2">
                <td>Item 2</td>
            </tr>
            <tr draggable="true" data-id="3">
                <td>Item 3</td>
            </tr>
        </tbody>
    </table>

    <script>
        let draggedRow = null;

        const rows = document.querySelectorAll('tbody tr');

        rows.forEach(row => {
            row.addEventListener('dragstart', (e) => {
                draggedRow = row;
                e.dataTransfer.effectAllowed = 'move';
            });

            row.addEventListener('dragover', (e) => {
                e.preventDefault();
                e.dataTransfer.dropEffect = 'move';
                row.classList.add('drag-over');
            });

            row.addEventListener('dragleave', () => {
                row.classList.remove('drag-over');
            });

            row.addEventListener('drop', (e) => {
                e.preventDefault();
                row.classList.remove('drag-over');

                const tbody = row.parentElement;
                if (draggedRow !== row) {
                    // Swap rows
                    if (draggedRow.compareDocumentPosition(row) === Node.DOCUMENT_POSITION_FOLLOWING) {
                        draggedRow.parentNode.insertBefore(row, draggedRow);
                    } else {
                        draggedRow.parentNode.insertBefore(draggedRow, row.nextSibling);
                    }
                }
            });
        });
    </script>
</body>
</html>
```

### Topic 4: Infinite Scroll Table
```javascript
function initInfiniteScrollTable(containerId, dataFetcher, pageSize = 20) {
    const container = document.getElementById(containerId);
    let page = 0;
    let isLoading = false;

    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && !isLoading) {
            isLoading = true;

            dataFetcher(page, pageSize).then(newRows => {
                newRows.forEach(row => {
                    const tr = document.createElement('tr');
                    Object.values(row).forEach(cell => {
                        const td = document.createElement('td');
                        td.textContent = cell;
                        tr.appendChild(td);
                    });
                    container.querySelector('tbody').appendChild(tr);
                });

                page++;
                isLoading = false;
            });
        }
    });

    const sentinel = document.createElement('div');
    container.parentElement.appendChild(sentinel);
    observer.observe(sentinel);
}
```

### Topic 5: Table with Group Totals
```html
<!DOCTYPE html>
<html>
<body>
    <table id="grouped-table">
        <thead>
            <tr>
                <th>Department</th>
                <th>Employee</th>
                <th>Salary</th>
            </tr>
        </thead>
        <tbody>
            <tr class="group-header">
                <td colspan="3">IT</td>
            </tr>
            <tr>
                <td></td>
                <td>John</td>
                <td>50,000</td>
            </tr>
            <tr>
                <td></td>
                <td>Jane</td>
                <td>55,000</td>
            </tr>
            <tr class="group-total">
                <td></td>
                <td>Subtotal</td>
                <td>105,000</td>
            </tr>
        </tbody>
    </table>

    <script>
        function calculateGroupTotals(tableId, salaryColumnIndex = 2) {
            const table = document.getElementById(tableId);
            const groupTotals = table.querySelectorAll('.group-total');

            groupTotals.forEach(totalRow => {
                let sum = 0;
                let row = totalRow.previousElementSibling;

                while (row && !row.classList.contains('group-total')) {
                    if (!row.classList.contains('group-header')) {
                        const salary = parseFloat(
                            row.cells[salaryColumnIndex].textContent.replace(/[^0-9.-]/g, '')
                        );
                        sum += salary;
                    }
                    row = row.previousElementSibling;
                }

                totalRow.cells[salaryColumnIndex].textContent = sum.toLocaleString();
            });
        }

        calculateGroupTotals('grouped-table');
    </script>
</body>
</html>
```

## 6.11. Bài tập thực hành

### Bài 1 (Dễ): Basic Employee Table
Tạo bảng nhân viên với:
- 5 nhân viên
- Cột: Name, Position, Email, Phone
- Proper styling với header
- Zebra striping

### Bài 2 (Dễ): Pricing Comparison Table
Tạo bảng so sánh giá với:
- 3 pricing plans
- 5 features
- Highlighted recommended plan
- Call-to-action buttons

### Bài 3 (Dễ): Schedule Table
Tạo bảng lịch học với:
- 5 ngày trong tuần
- 6 time slots
- Tên môn học
- Phòng học
- Giảng viên

### Bài 4 (Dễ): Product Inventory
Tạo bảng kho hàng với:
- 10 sản phẩm
- SKU, tên, số lượng, giá
- Total value column
- Color coding for low stock

### Bài 5 (Trung bình): Financial Report Table
Tạo bảng báo cáo tài chính với:
- 4 quarters
- Revenue, Expenses, Profit rows
- Multi-level headers
- Colored rows
- Footer với totals

### Bài 6 (Trung bình): Sortable Data Table
Tạo bảng có:
- Ít nhất 50 dòng dữ liệu
- Sortable columns (click header)
- Search/filter functionality
- Pagination (10 rows per page)

### Bài 7 (Trung bình): Responsive Comparison Table
Tạo bảng responsive với:
- Desktop: traditional table format
- Mobile: card-like layout
- Data attributes cho labels
- Touch-friendly interactions

### Bài 8 (Trung bình): Students Grades Table
Tạo bảng điểm với:
- Student info
- 4 subjects
- Average score
- Grade letter
- Ranking

### Bài 9 (Khó): Interactive Data Dashboard
Tạo dashboard với:
- Multiple tables
- Real-time data updates
- Charts/visualizations
- Export to CSV
- Responsive design

### Bài 10 (Khó): Editable Table
Tạo bảng có thể edit với:
- Click-to-edit cells
- Input validation
- Save/Cancel buttons
- Add/Remove rows
- Undo functionality

### Bài 11 (Khó): Advanced Financial Dashboard
Tạo dashboard tài chính với:
- Hierarchical data
- Group totals
- Currency formatting
- Year-over-year comparison
- Export options

### Bài 12 (Khó): Real-time Table with WebSocket
Tạo bảng real-time với:
- WebSocket connection
- Live data updates
- Change highlighting
- Historical trend indicators
- Performance metrics

---

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
