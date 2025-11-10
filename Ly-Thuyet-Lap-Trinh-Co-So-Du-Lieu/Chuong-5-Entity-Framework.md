# CHƯƠNG 5: ENTITY FRAMEWORK

## Mục tiêu học tập
Sau khi học xong chương này, sinh viên có khả năng:
- Hiểu khái niệm ORM và Entity Framework
- Sử dụng Database First approach
- Sử dụng Code First approach
- Thực hiện CRUD operations với EF
- Sử dụng LINQ với Entity Framework

---

## 5.1. TỔNG QUAN VỀ ENTITY FRAMEWORK

### Entity Framework là gì?

**Entity Framework (EF)** là một ORM (Object-Relational Mapping) framework của Microsoft, cho phép làm việc với database thông qua các object C#.

### ORM là gì?

**ORM** là kỹ thuật ánh xạ giữa object-oriented programming và relational database.

```
C# Classes (Entities)  ←→  Database Tables
Properties             ←→  Columns
Objects                ←→  Rows
Relationships          ←→  Foreign Keys
```

### Lợi ích của Entity Framework

1. **Giảm code ADO.NET**: Không cần viết SQL thủ công
2. **Strongly-typed**: Type-safe, IntelliSense hỗ trợ
3. **LINQ support**: Truy vấn bằng LINQ
4. **Change tracking**: Tự động theo dõi thay đổi
5. **Migration**: Quản lý phiên bản database
6. **Productivity**: Tăng năng suất lập trình

### Các cách tiếp cận (Approaches)

#### 1. Database First
```
Database → EF Designer → Entity Classes → Code
```
- Có sẵn database
- Tạo model từ database
- Phù hợp: Hệ thống có sẵn

#### 2. Model First
```
EF Designer → Entity Classes → Database Schema
```
- Thiết kế bằng designer
- Tạo database từ model
- Ít phổ biến

#### 3. Code First
```
Entity Classes → Database Schema
```
- Viết code trước
- Tạo database từ code
- Phổ biến nhất hiện nay
- Control tốt, migration

---

## 5.2. MÔ HÌNH DATABASE FIRST

### 5.2.1. Tạo mô hình từ database

**Bước 1: Cài đặt Entity Framework**
```bash
# NuGet Package Manager Console
Install-Package EntityFramework
```

**Bước 2: Add ADO.NET Entity Data Model**
1. Right-click project → Add → New Item
2. Chọn "ADO.NET Entity Data Model"
3. Đặt tên: `QLSVModel.edmx`
4. Chọn "EF Designer from database"
5. Chọn kết nối database
6. Chọn bảng cần map
7. Finish

**Kết quả:**
- File `.edmx` (Entity Data Model)
- Context class: `QLSVEntities`
- Entity classes: `SinhVien`, `MonHoc`, `KetQua`...

### 5.2.2. Truy vấn dữ liệu

**Lấy tất cả sinh viên:**
```csharp
using (QLSVEntities db = new QLSVEntities())
{
    var students = db.SinhViens.ToList();

    foreach (var student in students)
    {
        Console.WriteLine($"{student.MaSV} - {student.HoTen}");
    }
}
```

**Lọc dữ liệu:**
```csharp
using (QLSVEntities db = new QLSVEntities())
{
    // Lọc theo điều kiện
    var cnttStudents = db.SinhViens
        .Where(s => s.MaLop == "CNTT01")
        .ToList();

    // Tìm theo khóa chính
    var student = db.SinhViens.Find("SV001");

    // FirstOrDefault
    var firstStudent = db.SinhViens
        .FirstOrDefault(s => s.MaSV == "SV001");

    // Single
    var singleStudent = db.SinhViens
        .Single(s => s.MaSV == "SV001");
}
```

**Join bảng:**
```csharp
using (QLSVEntities db = new QLSVEntities())
{
    // Navigation property (tự động join)
    var students = db.SinhViens
        .Include("Lop")  // Eager loading
        .ToList();

    foreach (var student in students)
    {
        Console.WriteLine($"{student.HoTen} - {student.Lop.TenLop}");
    }

    // LINQ Join
    var query = from s in db.SinhViens
                join l in db.Lops on s.MaLop equals l.MaLop
                select new
                {
                    s.MaSV,
                    s.HoTen,
                    l.TenLop
                };
}
```

**Thêm dữ liệu:**
```csharp
using (QLSVEntities db = new QLSVEntities())
{
    // Tạo entity mới
    SinhVien sv = new SinhVien
    {
        MaSV = "SV001",
        HoTen = "Nguyễn Văn A",
        NgaySinh = new DateTime(2000, 1, 1),
        GioiTinh = "Nam",
        MaLop = "CNTT01"
    };

    // Thêm vào context
    db.SinhViens.Add(sv);

    // Lưu xuống database
    int rowsAffected = db.SaveChanges();

    Console.WriteLine($"Đã thêm {rowsAffected} sinh viên");
}
```

**Cập nhật dữ liệu:**
```csharp
using (QLSVEntities db = new QLSVEntities())
{
    // Tìm entity
    var student = db.SinhViens.Find("SV001");

    if (student != null)
    {
        // Cập nhật thuộc tính
        student.HoTen = "Nguyễn Văn A - Updated";
        student.Email = "a@email.com";

        // Lưu thay đổi
        db.SaveChanges();
    }
}
```

**Xóa dữ liệu:**
```csharp
using (QLSVEntities db = new QLSVEntities())
{
    // Tìm entity
    var student = db.SinhViens.Find("SV001");

    if (student != null)
    {
        // Xóa khỏi context
        db.SinhViens.Remove(student);

        // Lưu thay đổi
        db.SaveChanges();
    }
}
```

### Loading Strategies

**1. Lazy Loading (Mặc định)**
```csharp
// Chỉ load sinh viên, chưa load lớp
var student = db.SinhViens.Find("SV001");

// Truy cập Lop → Query mới
Console.WriteLine(student.Lop.TenLop); // Lazy load
```

**2. Eager Loading**
```csharp
// Load sinh viên và lớp cùng lúc
var student = db.SinhViens
    .Include(s => s.Lop)
    .FirstOrDefault(s => s.MaSV == "SV001");

// Không có query mới
Console.WriteLine(student.Lop.TenLop);
```

**3. Explicit Loading**
```csharp
var student = db.SinhViens.Find("SV001");

// Load Lop một cách tường minh
db.Entry(student).Reference(s => s.Lop).Load();

// Load collection
db.Entry(student).Collection(s => s.KetQuas).Load();
```

---

## 5.3. MÔ HÌNH CODE FIRST

### 5.3.1. Giới thiệu Code First

**Code First** cho phép định nghĩa model bằng C# classes, EF sẽ tạo database tự động.

**Ưu điểm:**
- Full control code
- Migration hỗ trợ
- POCO classes (Plain Old CLR Objects)
- Không phụ thuộc designer

### 5.3.2. Tạo Entity Classes

**Entity class:**
```csharp
public class SinhVien
{
    // Primary key (convention: Id hoặc ClassNameId)
    public string MaSV { get; set; }

    [Required]
    [MaxLength(100)]
    public string HoTen { get; set; }

    [Required]
    public DateTime NgaySinh { get; set; }

    [MaxLength(3)]
    public string GioiTinh { get; set; }

    [EmailAddress]
    [MaxLength(100)]
    public string Email { get; set; }

    [MaxLength(20)]
    public string SoDienThoai { get; set; }

    [MaxLength(200)]
    public string DiaChi { get; set; }

    // Foreign key
    [Required]
    [MaxLength(10)]
    public string MaLop { get; set; }

    // Navigation property
    public virtual Lop Lop { get; set; }

    public virtual ICollection<KetQua> KetQuas { get; set; }
}
```

**Related entity:**
```csharp
public class Lop
{
    [Key]
    [MaxLength(10)]
    public string MaLop { get; set; }

    [Required]
    [MaxLength(100)]
    public string TenLop { get; set; }

    [MaxLength(10)]
    public string Khoa { get; set; }

    // Navigation property
    public virtual ICollection<SinhVien> SinhViens { get; set; }
}

public class MonHoc
{
    [Key]
    [MaxLength(10)]
    public string MaMonHoc { get; set; }

    [Required]
    [MaxLength(100)]
    public string TenMonHoc { get; set; }

    public int SoTinChi { get; set; }

    public virtual ICollection<KetQua> KetQuas { get; set; }
}

public class KetQua
{
    [Key, Column(Order = 0)]
    [MaxLength(10)]
    public string MaSV { get; set; }

    [Key, Column(Order = 1)]
    [MaxLength(10)]
    public string MaMonHoc { get; set; }

    [Range(0, 10)]
    public float DiemGiuaKy { get; set; }

    [Range(0, 10)]
    public float DiemCuoiKy { get; set; }

    [Range(0, 10)]
    public float DiemTongKet { get; set; }

    // Navigation properties
    public virtual SinhVien SinhVien { get; set; }
    public virtual MonHoc MonHoc { get; set; }
}
```

### 5.3.3. DbContext

**DbContext class:**
```csharp
using System.Data.Entity;

public class QLSVContext : DbContext
{
    // Constructor
    public QLSVContext() : base("name=QLSVConnection")
    {
    }

    // DbSet cho các entity
    public DbSet<SinhVien> SinhViens { get; set; }
    public DbSet<Lop> Lops { get; set; }
    public DbSet<MonHoc> MonHocs { get; set; }
    public DbSet<KetQua> KetQuas { get; set; }

    // Fluent API (tùy chọn)
    protected override void OnModelCreating(DbModelBuilder modelBuilder)
    {
        // Cấu hình bảng SinhVien
        modelBuilder.Entity<SinhVien>()
            .ToTable("SinhVien")
            .HasKey(s => s.MaSV);

        modelBuilder.Entity<SinhVien>()
            .Property(s => s.HoTen)
            .IsRequired()
            .HasMaxLength(100);

        // Cấu hình quan hệ 1-nhiều
        modelBuilder.Entity<Lop>()
            .HasMany(l => l.SinhViens)
            .WithRequired(s => s.Lop)
            .HasForeignKey(s => s.MaLop);

        // Cấu hình quan hệ nhiều-nhiều với composite key
        modelBuilder.Entity<KetQua>()
            .HasKey(kq => new { kq.MaSV, kq.MaMonHoc });

        modelBuilder.Entity<KetQua>()
            .HasRequired(kq => kq.SinhVien)
            .WithMany(s => s.KetQuas)
            .HasForeignKey(kq => kq.MaSV);

        modelBuilder.Entity<KetQua>()
            .HasRequired(kq => kq.MonHoc)
            .WithMany(m => m.KetQuas)
            .HasForeignKey(kq => kq.MaMonHoc);

        base.OnModelCreating(modelBuilder);
    }
}
```

**Connection string (App.config):**
```xml
<connectionStrings>
  <add name="QLSVConnection"
       connectionString="Data Source=.;Initial Catalog=QLSV_CodeFirst;Integrated Security=True;"
       providerName="System.Data.SqlClient"/>
</connectionStrings>
```

### 5.3.4. Migrations

**Enable Migrations:**
```bash
# Package Manager Console
Enable-Migrations
```

**Tạo Migration:**
```bash
Add-Migration InitialCreate
```

**Update Database:**
```bash
Update-Database
```

**Migration class:**
```csharp
public partial class InitialCreate : DbMigration
{
    public override void Up()
    {
        CreateTable(
            "dbo.SinhVien",
            c => new
            {
                MaSV = c.String(nullable: false, maxLength: 10),
                HoTen = c.String(nullable: false, maxLength: 100),
                NgaySinh = c.DateTime(nullable: false),
                GioiTinh = c.String(maxLength: 3),
                Email = c.String(maxLength: 100),
                MaLop = c.String(nullable: false, maxLength: 10),
            })
            .PrimaryKey(t => t.MaSV)
            .ForeignKey("dbo.Lop", t => t.MaLop, cascadeDelete: true)
            .Index(t => t.MaLop);
    }

    public override void Down()
    {
        DropForeignKey("dbo.SinhVien", "MaLop", "dbo.Lop");
        DropIndex("dbo.SinhVien", new[] { "MaLop" });
        DropTable("dbo.SinhVien");
    }
}
```

**Seed Data:**
```csharp
internal sealed class Configuration : DbMigrationsConfiguration<QLSVContext>
{
    public Configuration()
    {
        AutomaticMigrationsEnabled = false;
    }

    protected override void Seed(QLSVContext context)
    {
        // Seed Lop
        context.Lops.AddOrUpdate(
            l => l.MaLop,
            new Lop { MaLop = "CNTT01", TenLop = "Công nghệ thông tin 01", Khoa = "CNTT" },
            new Lop { MaLop = "CNTT02", TenLop = "Công nghệ thông tin 02", Khoa = "CNTT" }
        );

        // Seed SinhVien
        context.SinhViens.AddOrUpdate(
            s => s.MaSV,
            new SinhVien
            {
                MaSV = "SV001",
                HoTen = "Nguyễn Văn A",
                NgaySinh = new DateTime(2000, 1, 1),
                GioiTinh = "Nam",
                MaLop = "CNTT01"
            },
            new SinhVien
            {
                MaSV = "SV002",
                HoTen = "Trần Thị B",
                NgaySinh = new DateTime(2000, 5, 15),
                GioiTinh = "Nữ",
                MaLop = "CNTT01"
            }
        );

        context.SaveChanges();
    }
}
```

### 5.3.5. Sử dụng Code First

**CRUD operations:**
```csharp
// CREATE
using (var db = new QLSVContext())
{
    var sinhVien = new SinhVien
    {
        MaSV = "SV003",
        HoTen = "Lê Văn C",
        NgaySinh = new DateTime(2001, 3, 10),
        GioiTinh = "Nam",
        MaLop = "CNTT01"
    };

    db.SinhViens.Add(sinhVien);
    db.SaveChanges();
}

// READ
using (var db = new QLSVContext())
{
    var students = db.SinhViens
        .Include(s => s.Lop)
        .ToList();

    foreach (var s in students)
    {
        Console.WriteLine($"{s.HoTen} - {s.Lop.TenLop}");
    }
}

// UPDATE
using (var db = new QLSVContext())
{
    var student = db.SinhViens.Find("SV003");

    if (student != null)
    {
        student.Email = "c@email.com";
        db.SaveChanges();
    }
}

// DELETE
using (var db = new QLSVContext())
{
    var student = db.SinhViens.Find("SV003");

    if (student != null)
    {
        db.SinhViens.Remove(student);
        db.SaveChanges();
    }
}
```

**Complex queries:**
```csharp
using (var db = new QLSVContext())
{
    // Thống kê sinh viên theo lớp
    var thongKe = db.SinhViens
        .GroupBy(s => s.MaLop)
        .Select(g => new
        {
            MaLop = g.Key,
            SoLuong = g.Count(),
            TenLop = g.FirstOrDefault().Lop.TenLop
        })
        .ToList();

    // Tìm sinh viên có điểm cao nhất
    var topStudent = db.KetQuas
        .OrderByDescending(kq => kq.DiemTongKet)
        .Select(kq => new
        {
            kq.SinhVien.HoTen,
            kq.MonHoc.TenMonHoc,
            kq.DiemTongKet
        })
        .FirstOrDefault();

    // Join nhiều bảng
    var query = from s in db.SinhViens
                join l in db.Lops on s.MaLop equals l.MaLop
                join kq in db.KetQuas on s.MaSV equals kq.MaSV
                join mh in db.MonHocs on kq.MaMonHoc equals mh.MaMonHoc
                where kq.DiemTongKet >= 8.0
                select new
                {
                    s.HoTen,
                    l.TenLop,
                    mh.TenMonHoc,
                    kq.DiemTongKet
                };
}
```

---

## 5.4. REPOSITORY PATTERN

### Generic Repository

**Interface:**
```csharp
public interface IRepository<T> where T : class
{
    IEnumerable<T> GetAll();
    T GetById(object id);
    void Insert(T entity);
    void Update(T entity);
    void Delete(object id);
    void Delete(T entity);
    void Save();
}
```

**Implementation:**
```csharp
public class Repository<T> : IRepository<T> where T : class
{
    private QLSVContext context;
    private DbSet<T> dbSet;

    public Repository(QLSVContext context)
    {
        this.context = context;
        this.dbSet = context.Set<T>();
    }

    public IEnumerable<T> GetAll()
    {
        return dbSet.ToList();
    }

    public T GetById(object id)
    {
        return dbSet.Find(id);
    }

    public void Insert(T entity)
    {
        dbSet.Add(entity);
    }

    public void Update(T entity)
    {
        dbSet.Attach(entity);
        context.Entry(entity).State = EntityState.Modified;
    }

    public void Delete(object id)
    {
        T entity = dbSet.Find(id);
        Delete(entity);
    }

    public void Delete(T entity)
    {
        if (context.Entry(entity).State == EntityState.Detached)
        {
            dbSet.Attach(entity);
        }

        dbSet.Remove(entity);
    }

    public void Save()
    {
        context.SaveChanges();
    }
}
```

**Sử dụng:**
```csharp
public class SinhVienBLL
{
    private IRepository<SinhVien> repository;

    public SinhVienBLL()
    {
        var context = new QLSVContext();
        repository = new Repository<SinhVien>(context);
    }

    public List<SinhVien> LayDanhSach()
    {
        return repository.GetAll().ToList();
    }

    public SinhVien TimTheoMa(string maSV)
    {
        return repository.GetById(maSV);
    }

    public void Them(SinhVien sv)
    {
        repository.Insert(sv);
        repository.Save();
    }

    public void CapNhat(SinhVien sv)
    {
        repository.Update(sv);
        repository.Save();
    }

    public void Xoa(string maSV)
    {
        repository.Delete(maSV);
        repository.Save();
    }
}
```

---

## TÓM TẮT CHƯƠNG 5

### So sánh Database First vs Code First

| Tiêu chí | Database First | Code First |
|----------|----------------|------------|
| Xuất phát | Database có sẵn | Code trước |
| Control | Database-centric | Code-centric |
| Migration | Khó | Dễ dàng |
| Collaboration | Khó merge .edmx | Dễ merge code |
| Phù hợp | Legacy system | New project |

### Các khái niệm quan trọng

1. **DbContext**: Đại diện cho session với database
2. **DbSet**: Đại diện cho bảng
3. **Entity**: Class map với bảng
4. **Migration**: Quản lý phiên bản database
5. **Navigation Property**: Quan hệ giữa các entity
6. **Lazy/Eager Loading**: Chiến lược load dữ liệu

---

**Kết thúc Chương 5**
