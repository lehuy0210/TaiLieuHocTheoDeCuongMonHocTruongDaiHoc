# TÀI LIỆU LÝ THUYẾT LẬP TRÌNH CƠ SỞ DỮ LIỆU

## Giới thiệu

Tài liệu lý thuyết đầy đủ cho môn **Lập trình cơ sở dữ liệu (ITEC3406)** theo đề cương của **Trường Đại học Mở TP.HCM**.

**Thông tin môn học:**
- Mã môn: ITEC3406
- Số tín chỉ: 3 (2 LT + 1 TH)
- Giảng viên: ThS. Nguyễn Thị Phương Trang
- Khoa: Công nghệ Thông tin

## Nội dung chi tiết

### Chương 1: Ngôn ngữ T-SQL
- Khai báo và sử dụng biến
- Cấu trúc điều khiển (IF, WHILE, CASE)
- View (Khung nhìn)
- Stored Procedure (Thủ tục lưu trữ)
- User-Defined Function (Hàm người dùng)
- Trigger (Bẫy sự kiện)
- Transaction (Giao tác)

📄 [Xem chi tiết Chương 1](./Chuong-1-Ngon-Ngu-T-SQL.md)

### Chương 2: ADO.NET
- Tổng quan ADO.NET
- Mô hình kết nối và phi kết nối
- SqlConnection, SqlCommand, SqlDataReader
- DataSet, DataAdapter, DataTable
- Data Binding (Simple & Complex)

📄 [Xem chi tiết Chương 2](./Chuong-2-ADO-NET.md)

### Chương 3: Kiến trúc đa lớp
- Tổng quan kiến trúc đa lớp
- Kiến trúc đa tầng (Multi-tier)
- Thiết kế ứng dụng 3 lớp
  - Lớp DTO (Data Transfer Object)
  - Lớp DAL (Data Access Layer)
  - Lớp BLL (Business Logic Layer)
  - Lớp GUI (Presentation Layer)
- ASP.NET Core MVC

📄 [Xem chi tiết Chương 3](./Chuong-3-Kien-Truc-Da-Lop.md)

### Chương 4: LINQ
- Các mở rộng của C# hỗ trợ LINQ
  - Var (Implicit typed variables)
  - Object & Collection Initializers
  - Lambda Expression
  - Anonymous Types
  - Extension Methods
- LINQ to Objects
  - Query Syntax & Method Syntax
  - Các toán tử: Where, Select, OrderBy, GroupBy, Join...
- LINQ to XML

📄 [Xem chi tiết Chương 4](./Chuong-4-LINQ.md)

### Chương 5: Entity Framework
- Tổng quan ORM và Entity Framework
- Database First Approach
  - Tạo model từ database
  - Truy vấn dữ liệu
  - CRUD operations
  - Loading strategies (Lazy, Eager, Explicit)
- Code First Approach
  - Entity Classes
  - DbContext
  - Migrations
  - Fluent API
- Repository Pattern

📄 [Xem chi tiết Chương 5](./Chuong-5-Entity-Framework.md)

### Chương 6: ASP.NET Core Web API
- Khái niệm Web API và RESTful API
- HTTP Methods & Status Codes
- JSON
- Tạo ASP.NET Core Web API
- CRUD API với Entity Framework
- DTO Pattern
- Pagination, Filtering, Sorting
- Deploy lên Azure

📄 [Xem chi tiết Chương 6](./Chuong-6-ASP-NET-Core-Web-API.md)

## Cấu trúc thư mục

```
Ly-Thuyet-Lap-Trinh-Co-So-Du-Lieu/
├── README.md (File này)
├── Chuong-1-Ngon-Ngu-T-SQL.md
├── Chuong-2-ADO-NET.md
├── Chuong-3-Kien-Truc-Da-Lop.md
├── Chuong-4-LINQ.md
├── Chuong-5-Entity-Framework.md
└── Chuong-6-ASP-NET-Core-Web-API.md
```

## Công nghệ sử dụng

- **Database**: Microsoft SQL Server
- **Language**: C#, T-SQL
- **Framework**: .NET Framework, ASP.NET Core
- **ORM**: ADO.NET, Entity Framework Core
- **Query**: LINQ
- **API**: RESTful Web API
- **Tools**: Visual Studio, SQL Server Management Studio
- **Cloud**: Microsoft Azure

## Cách sử dụng tài liệu

1. **Đọc tuần tự**: Bắt đầu từ Chương 1 đến Chương 6
2. **Thực hành song song**: Mỗi chương đều có ví dụ code chi tiết
3. **Làm bài tập**: Cuối mỗi chương có bài tập thực hành
4. **Xây dựng project**: Áp dụng kiến thức vào project thực tế

## Lộ trình học

### Tuần 1: T-SQL (Chương 1)
- Học các cấu trúc điều khiển
- Viết View, Stored Procedure, Function
- Thực hành Trigger và Transaction

### Tuần 2: ADO.NET (Chương 2)
- Kết nối database bằng ADO.NET
- Thực hiện CRUD với Connected Model
- Sử dụng DataSet và Data Binding

### Tuần 3: Kiến trúc 3 lớp (Chương 3)
- Thiết kế ứng dụng theo mô hình 3 lớp
- Tạo DTO, DAL, BLL, GUI
- Tìm hiểu ASP.NET Core MVC

### Tuần 4: LINQ (Chương 4)
- Học Lambda Expression
- Thực hành LINQ to Objects
- LINQ to XML

### Tuần 5: Entity Framework (Chương 5)
- Database First approach
- Code First approach
- Migrations và Repository Pattern

### Tuần 6-7: ASP.NET Core Web API (Chương 6)
- Tạo RESTful API
- CRUD API với EF Core
- Pagination, Filtering, Sorting
- Deploy lên Azure

## Tài liệu tham khảo

### Sách
1. Beginning Database Programming Using ASP.NET Core 3 - Bipin Joshi (2019)
2. C# 6.0 and the .NET 4.6 Framework - Andrew Troelsen, Philip Japikse (2015)
3. Beginning Microsoft SQL Server 2012 Programming - Robert Vieira (2012)
4. Murach's C# 2015 - Anne Boehm, Joel Murach (2016)

### Online Resources
- [Microsoft Docs - C#](https://docs.microsoft.com/en-us/dotnet/csharp/)
- [Microsoft Docs - LINQ](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)
- [Microsoft Docs - EF Core](https://docs.microsoft.com/en-us/ef/core/)
- [Microsoft Docs - ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/)

## Đánh giá môn học

- **Quá trình (40%)**: Bài tập thực hành
- **Giữa kỳ (10%)**: Trắc nghiệm LMS
- **Cuối kỳ (50%)**: Đồ án môn học / Vấn đáp

## Yêu cầu môn học trước

- **Cơ sở dữ liệu (ITEC2502)**: Kiến thức SQL cơ bản
- **Lập trình giao diện (ITEC2401)**: C# và Windows Forms

## Phần mềm cần thiết

- Microsoft Visual Studio 2017+ (hoặc Visual Studio Code)
- Microsoft SQL Server 2014+ (hoặc SQL Server Express)
- SQL Server Management Studio (SSMS)
- .NET Framework 4.6+ / .NET Core 3.0+

## Lưu ý

- Tài liệu này được soạn dựa trên đề cương chính thức
- Sinh viên nên kết hợp với bài giảng của giảng viên
- Thực hành là then chốt để nắm vững kiến thức
- Làm đầy đủ các bài tập được giao

## Liên hệ

Nếu có thắc mắc về tài liệu, vui lòng liên hệ:
- Email: trang.ntp@ou.edu.vn
- Phòng làm việc: 604

---

**Trường Đại học Mở Thành phố Hồ Chí Minh**
**Khoa Công nghệ Thông tin**

*Chúc các bạn học tốt!* 📚💻
