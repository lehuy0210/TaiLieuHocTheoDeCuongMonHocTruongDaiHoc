# CHƯƠNG 4: LINQ (Language Integrated Query)

## Mục tiêu học tập
Sau khi học xong chương này, sinh viên có khả năng:
- Hiểu khái niệm và lợi ích của LINQ
- Sử dụng các mở rộng của C# hỗ trợ LINQ
- Viết câu truy vấn LINQ to Objects
- Sử dụng LINQ to XML

---

## 4.1. CÁC MỞ RỘNG CỦA C# HỖ TRỢ LINQ

### 4.1.1. Implicit Typed Local Variables (var)

**Var** cho phép compiler tự suy luận kiểu dữ liệu.

```csharp
// Khai báo tường minh
int number = 10;
string name = "John";
List<string> list = new List<string>();

// Sử dụng var (kiểu ngầm định)
var number = 10;              // int
var name = "John";            // string
var list = new List<string>(); // List<string>
var result = 5 * 10.5;        // double

// Lỗi: Phải gán giá trị ngay
// var x; // Error
```

**Khi nào dùng var:**
- Query LINQ (kết quả phức tạp)
- Anonymous types
- Kiểu dữ liệu rõ ràng từ ngữ cảnh

**Khi không nên dùng:**
- Kiểu dữ liệu không rõ ràng
- Giảm khả năng đọc code

### 4.1.2. Object and Collection Initializers

**Object Initializer:**
```csharp
// Cách cũ
SinhVien sv = new SinhVien();
sv.MaSV = "SV001";
sv.HoTen = "Nguyễn Văn A";
sv.NgaySinh = new DateTime(2000, 1, 1);

// Object Initializer (C# 3.0+)
SinhVien sv = new SinhVien
{
    MaSV = "SV001",
    HoTen = "Nguyễn Văn A",
    NgaySinh = new DateTime(2000, 1, 1)
};
```

**Collection Initializer:**
```csharp
// Cách cũ
List<string> list = new List<string>();
list.Add("Apple");
list.Add("Banana");
list.Add("Orange");

// Collection Initializer
List<string> list = new List<string>
{
    "Apple",
    "Banana",
    "Orange"
};

// Dictionary Initializer
Dictionary<string, int> dict = new Dictionary<string, int>
{
    { "Apple", 100 },
    { "Banana", 50 },
    { "Orange", 75 }
};

// C# 6.0+
Dictionary<string, int> dict = new Dictionary<string, int>
{
    ["Apple"] = 100,
    ["Banana"] = 50,
    ["Orange"] = 75
};
```

### 4.1.3. Lambda Expression

**Lambda Expression** là cú pháp ngắn gọn để viết anonymous method.

**Cú pháp:**
```
(parameters) => expression
(parameters) => { statements; }
```

**Ví dụ:**
```csharp
// Delegate truyền thống
delegate int Calculate(int x, int y);

Calculate add = delegate(int x, int y)
{
    return x + y;
};

// Lambda expression
Calculate add = (x, y) => x + y;

// Với LINQ
List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

// Lọc số chẵn
var evenNumbers = numbers.Where(n => n % 2 == 0);

// Lọc số lớn hơn 5
var greaterThan5 = numbers.Where(n => n > 5);

// Tính bình phương
var squares = numbers.Select(n => n * n);
```

**Lambda với nhiều parameters:**
```csharp
// 2 parameters
Func<int, int, int> add = (x, y) => x + y;

// 3 parameters
Func<int, int, int, int> sum3 = (x, y, z) => x + y + z;

// Không có parameter
Func<int> random = () => new Random().Next();

// 1 parameter (có thể bỏ dấu ngoặc)
Func<int, bool> isEven = x => x % 2 == 0;
```

**Lambda với nhiều statements:**
```csharp
Func<int, int, int> divide = (x, y) =>
{
    if (y == 0)
        throw new DivideByZeroException();

    return x / y;
};
```

### 4.1.4. Anonymous Types

**Anonymous Type** là kiểu dữ liệu không có tên, được tạo tự động.

```csharp
// Tạo anonymous type
var person = new
{
    Name = "John",
    Age = 25,
    Email = "john@email.com"
};

Console.WriteLine(person.Name);  // John
Console.WriteLine(person.Age);   // 25

// Sử dụng với LINQ
var students = new List<SinhVien> { /* ... */ };

var query = students.Select(sv => new
{
    sv.MaSV,
    sv.HoTen,
    Tuoi = DateTime.Now.Year - sv.NgaySinh.Year
});

foreach (var item in query)
{
    Console.WriteLine($"{item.MaSV} - {item.HoTen} - {item.Tuoi} tuổi");
}
```

**Lưu ý:**
- Chỉ dùng trong phạm vi method
- Không thể return anonymous type từ method (phải dùng dynamic)
- Read-only properties

### 4.1.5. Extension Methods

**Extension Method** cho phép thêm method vào kiểu dữ liệu có sẵn mà không cần kế thừa.

```csharp
// Định nghĩa extension method
public static class StringExtensions
{
    // Extension method cho string
    public static bool IsEmail(this string value)
    {
        return value.Contains("@") && value.Contains(".");
    }

    public static string Reverse(this string value)
    {
        char[] chars = value.ToCharArray();
        Array.Reverse(chars);
        return new string(chars);
    }
}

// Sử dụng
string email = "test@email.com";
bool isValid = email.IsEmail(); // true

string text = "Hello";
string reversed = text.Reverse(); // "olleH"
```

**Extension method cho LINQ:**
```csharp
public static class IEnumerableExtensions
{
    // Lọc các phần tử unique
    public static IEnumerable<T> DistinctBy<T, TKey>(
        this IEnumerable<T> source,
        Func<T, TKey> keySelector)
    {
        HashSet<TKey> seenKeys = new HashSet<TKey>();

        foreach (T element in source)
        {
            if (seenKeys.Add(keySelector(element)))
            {
                yield return element;
            }
        }
    }
}

// Sử dụng
var uniqueStudents = students.DistinctBy(s => s.MaSV);
```

---

## 4.2. LINQ TO OBJECTS

### 4.2.1. Giới thiệu LINQ

**LINQ (Language Integrated Query)** là công nghệ truy vấn dữ liệu được tích hợp vào C#.

**Ưu điểm:**
- Cú pháp truy vấn thống nhất
- Strongly-typed, IntelliSense hỗ trợ
- Compile-time checking
- Dễ đọc, dễ viết

**Các loại LINQ:**
- LINQ to Objects (collection, array)
- LINQ to SQL (SQL Server)
- LINQ to XML
- LINQ to Entities (Entity Framework)

### 4.2.2. Cú pháp LINQ

**Query Syntax (SQL-like):**
```csharp
var query = from item in collection
            where condition
            orderby item.Property
            select item;
```

**Method Syntax (Fluent API):**
```csharp
var query = collection
            .Where(item => condition)
            .OrderBy(item => item.Property)
            .Select(item => item);
```

### 4.2.3. Các toán tử truy vấn cơ bản

#### 1. Filtering (Lọc)

**Where:**
```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

// Query syntax
var evenNumbers = from n in numbers
                  where n % 2 == 0
                  select n;

// Method syntax
var evenNumbers = numbers.Where(n => n % 2 == 0);

// Nhiều điều kiện
var filtered = numbers.Where(n => n > 3 && n < 8);

// Với index
var filtered = numbers.Where((n, index) => index % 2 == 0);
```

**OfType:**
```csharp
ArrayList list = new ArrayList { 1, "two", 3, "four", 5 };

// Lọc chỉ lấy int
var numbers = list.OfType<int>(); // { 1, 3, 5 }

// Lọc chỉ lấy string
var strings = list.OfType<string>(); // { "two", "four" }
```

#### 2. Projection (Chiếu)

**Select:**
```csharp
List<SinhVien> students = GetStudents();

// Lấy chỉ tên
var names = students.Select(s => s.HoTen);

// Tạo anonymous type
var query = students.Select(s => new
{
    s.MaSV,
    s.HoTen,
    Tuoi = DateTime.Now.Year - s.NgaySinh.Year
});

// Select với index
var indexed = students.Select((s, index) => new
{
    Index = index + 1,
    s.HoTen
});
```

**SelectMany (Flatten):**
```csharp
// Lớp có danh sách sinh viên
class Lop
{
    public string TenLop { get; set; }
    public List<SinhVien> DanhSach { get; set; }
}

List<Lop> classes = GetClasses();

// Lấy tất cả sinh viên từ tất cả lớp
var allStudents = classes.SelectMany(c => c.DanhSach);

// Với projection
var query = classes.SelectMany(
    c => c.DanhSach,
    (c, s) => new { c.TenLop, s.HoTen }
);
```

#### 3. Sorting (Sắp xếp)

**OrderBy, OrderByDescending:**
```csharp
List<SinhVien> students = GetStudents();

// Sắp xếp tăng dần theo tên
var sorted = students.OrderBy(s => s.HoTen);

// Sắp xếp giảm dần theo điểm
var sorted = students.OrderByDescending(s => s.DiemTB);

// Sắp xếp nhiều tiêu chí
var sorted = students
    .OrderBy(s => s.Khoa)
    .ThenByDescending(s => s.DiemTB)
    .ThenBy(s => s.HoTen);
```

#### 4. Grouping (Nhóm)

**GroupBy:**
```csharp
List<SinhVien> students = GetStudents();

// Nhóm theo khoa
var grouped = students.GroupBy(s => s.Khoa);

foreach (var group in grouped)
{
    Console.WriteLine($"Khoa: {group.Key}");

    foreach (var student in group)
    {
        Console.WriteLine($"  - {student.HoTen}");
    }
}

// Với projection
var query = students
    .GroupBy(s => s.Khoa)
    .Select(g => new
    {
        Khoa = g.Key,
        SoLuong = g.Count(),
        DiemTB = g.Average(s => s.DiemTB)
    });
```

#### 5. Joining (Nối)

**Join (Inner Join):**
```csharp
List<SinhVien> students = GetStudents();
List<Lop> classes = GetClasses();

// Join students với classes
var query = students.Join(
    classes,
    s => s.MaLop,      // Key từ students
    c => c.MaLop,      // Key từ classes
    (s, c) => new      // Result
    {
        s.MaSV,
        s.HoTen,
        c.TenLop,
        c.Khoa
    }
);

// Query syntax
var query = from s in students
            join c in classes on s.MaLop equals c.MaLop
            select new { s.MaSV, s.HoTen, c.TenLop };
```

**GroupJoin (Left Join):**
```csharp
// Left join: Lấy tất cả classes, kể cả không có sinh viên
var query = classes.GroupJoin(
    students,
    c => c.MaLop,
    s => s.MaLop,
    (c, studentGroup) => new
    {
        c.TenLop,
        SoSinhVien = studentGroup.Count(),
        DanhSach = studentGroup
    }
);

// Query syntax
var query = from c in classes
            join s in students on c.MaLop equals s.MaLop into studentGroup
            select new
            {
                c.TenLop,
                DanhSach = studentGroup
            };
```

#### 6. Aggregation (Tổng hợp)

```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

// Count
int count = numbers.Count();                    // 5
int evenCount = numbers.Count(n => n % 2 == 0); // 2

// Sum
int sum = numbers.Sum();                        // 15
decimal totalSalary = employees.Sum(e => e.Salary);

// Average
double avg = numbers.Average();                 // 3.0
double avgScore = students.Average(s => s.DiemTB);

// Min, Max
int min = numbers.Min();                        // 1
int max = numbers.Max();                        // 5
var youngest = students.Min(s => s.NgaySinh);

// Aggregate (custom)
int product = numbers.Aggregate((a, b) => a * b); // 1*2*3*4*5 = 120
```

#### 7. Quantifiers (Định lượng)

```csharp
List<int> numbers = new List<int> { 2, 4, 6, 8, 10 };

// Any: Có phần tử nào thỏa điều kiện không?
bool hasEven = numbers.Any(n => n % 2 == 0);      // true
bool hasNegative = numbers.Any(n => n < 0);       // false

// All: Tất cả phần tử đều thỏa điều kiện?
bool allEven = numbers.All(n => n % 2 == 0);      // true
bool allPositive = numbers.All(n => n > 0);       // true

// Contains: Có chứa phần tử cụ thể không?
bool has5 = numbers.Contains(5);                   // false
bool has6 = numbers.Contains(6);                   // true
```

#### 8. Element Operators

```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

// First, FirstOrDefault
int first = numbers.First();                     // 1
int firstEven = numbers.First(n => n % 2 == 0);  // 2
int firstOrDefault = numbers.FirstOrDefault(n => n > 10); // 0 (default)

// Last, LastOrDefault
int last = numbers.Last();                       // 5
int lastEven = numbers.Last(n => n % 2 == 0);    // 4

// Single, SingleOrDefault (chỉ 1 phần tử duy nhất)
int single = numbers.Single(n => n == 3);        // 3
// int error = numbers.Single(n => n % 2 == 0);  // Exception: nhiều hơn 1

// ElementAt, ElementAtOrDefault
int third = numbers.ElementAt(2);                // 3 (index 2)
int outOfRange = numbers.ElementAtOrDefault(10); // 0
```

#### 9. Set Operators

```csharp
List<int> list1 = new List<int> { 1, 2, 3, 4, 5 };
List<int> list2 = new List<int> { 4, 5, 6, 7, 8 };

// Distinct: Loại bỏ trùng lặp
var distinct = list1.Concat(list2).Distinct();
// { 1, 2, 3, 4, 5, 6, 7, 8 }

// Union: Hợp (không trùng)
var union = list1.Union(list2);
// { 1, 2, 3, 4, 5, 6, 7, 8 }

// Intersect: Giao
var intersect = list1.Intersect(list2);
// { 4, 5 }

// Except: Hiệu (list1 - list2)
var except = list1.Except(list2);
// { 1, 2, 3 }
```

#### 10. Partitioning

```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

// Take: Lấy n phần tử đầu
var first5 = numbers.Take(5); // { 1, 2, 3, 4, 5 }

// Skip: Bỏ qua n phần tử đầu
var skip5 = numbers.Skip(5);  // { 6, 7, 8, 9, 10 }

// TakeWhile: Lấy cho đến khi điều kiện sai
var takeWhile = numbers.TakeWhile(n => n < 5); // { 1, 2, 3, 4 }

// SkipWhile: Bỏ qua cho đến khi điều kiện sai
var skipWhile = numbers.SkipWhile(n => n < 5); // { 5, 6, 7, 8, 9, 10 }

// Phân trang
int pageNumber = 2;
int pageSize = 5;
var page = numbers.Skip((pageNumber - 1) * pageSize).Take(pageSize);
```

### Ví dụ tổng hợp LINQ

```csharp
// Tìm top 5 sinh viên có điểm cao nhất của khoa CNTT
var top5 = students
    .Where(s => s.Khoa == "CNTT")
    .OrderByDescending(s => s.DiemTB)
    .Take(5)
    .Select(s => new
    {
        s.MaSV,
        s.HoTen,
        s.DiemTB
    });

// Thống kê điểm trung bình theo khoa
var thongKe = students
    .GroupBy(s => s.Khoa)
    .Select(g => new
    {
        Khoa = g.Key,
        SoLuong = g.Count(),
        DiemTrungBinh = g.Average(s => s.DiemTB),
        DiemCaoNhat = g.Max(s => s.DiemTB),
        DiemThapNhat = g.Min(s => s.DiemTB)
    })
    .OrderByDescending(x => x.DiemTrungBinh);

// Tìm sinh viên có điểm cao nhất mỗi lớp
var topByClass = students
    .GroupBy(s => s.MaLop)
    .Select(g => g.OrderByDescending(s => s.DiemTB).First());
```

---

## 4.3. LINQ TO XML

### Tạo XML Document

```csharp
using System.Xml.Linq;

// Tạo XML document
XDocument doc = new XDocument(
    new XDeclaration("1.0", "utf-8", "yes"),
    new XElement("SinhViens",
        new XElement("SinhVien",
            new XElement("MaSV", "SV001"),
            new XElement("HoTen", "Nguyễn Văn A"),
            new XElement("NgaySinh", "2000-01-01"),
            new XElement("DiemTB", 8.5)
        ),
        new XElement("SinhVien",
            new XElement("MaSV", "SV002"),
            new XElement("HoTen", "Trần Thị B"),
            new XElement("NgaySinh", "2000-05-15"),
            new XElement("DiemTB", 9.0)
        )
    )
);

// Lưu file
doc.Save("sinhvien.xml");
```

### Đọc XML

```csharp
// Load XML
XDocument doc = XDocument.Load("sinhvien.xml");

// Query với LINQ
var query = from sv in doc.Descendants("SinhVien")
            where (double)sv.Element("DiemTB") >= 8.0
            select new
            {
                MaSV = sv.Element("MaSV").Value,
                HoTen = sv.Element("HoTen").Value,
                DiemTB = (double)sv.Element("DiemTB")
            };

foreach (var item in query)
{
    Console.WriteLine($"{item.MaSV} - {item.HoTen} - {item.DiemTB}");
}
```

### Sửa đổi XML

```csharp
XDocument doc = XDocument.Load("sinhvien.xml");

// Thêm sinh viên mới
doc.Root.Add(
    new XElement("SinhVien",
        new XElement("MaSV", "SV003"),
        new XElement("HoTen", "Lê Văn C"),
        new XElement("NgaySinh", "2001-03-10"),
        new XElement("DiemTB", 7.5)
    )
);

// Cập nhật điểm
var sv001 = doc.Descendants("SinhVien")
    .FirstOrDefault(sv => sv.Element("MaSV").Value == "SV001");

if (sv001 != null)
{
    sv001.Element("DiemTB").Value = "9.5";
}

// Xóa sinh viên
var sv002 = doc.Descendants("SinhVien")
    .FirstOrDefault(sv => sv.Element("MaSV").Value == "SV002");

sv002?.Remove();

// Lưu
doc.Save("sinhvien.xml");
```

---

## TÓM TẮT CHƯƠNG 4

### Các khái niệm chính

1. **LINQ**: Truy vấn dữ liệu thống nhất
2. **Lambda Expression**: Cú pháp ngắn gọn cho anonymous method
3. **Anonymous Types**: Kiểu dữ liệu không tên
4. **Extension Methods**: Mở rộng kiểu dữ liệu có sẵn

### Các toán tử LINQ quan trọng

| Loại | Toán tử |
|------|---------|
| Filtering | Where, OfType |
| Projection | Select, SelectMany |
| Sorting | OrderBy, ThenBy |
| Grouping | GroupBy |
| Joining | Join, GroupJoin |
| Aggregation | Count, Sum, Average, Min, Max |
| Set | Distinct, Union, Intersect, Except |
| Partitioning | Take, Skip, TakeWhile, SkipWhile |

---

**Kết thúc Chương 4**
