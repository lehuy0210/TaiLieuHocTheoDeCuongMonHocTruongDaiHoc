# CHƯƠNG 6: ASP.NET CORE WEB API

## Mục tiêu học tập
Sau khi học xong chương này, sinh viên có khả năng:
- Hiểu khái niệm Web API và RESTful API
- Tạo ASP.NET Core Web API project
- Xây dựng CRUD API với Entity Framework
- Sử dụng LINQ và EF trong API
- Deploy Web API lên Azure

---

## 6.1. CÁC KHÁI NIỆM LIÊN QUAN

### 6.1.1. Web API là gì?

**Web API (Application Programming Interface)** là giao diện lập trình ứng dụng cho phép các hệ thống giao tiếp với nhau qua HTTP.

**Đặc điểm:**
- Giao tiếp qua HTTP/HTTPS
- Trả về dữ liệu (JSON, XML)
- Không có UI, chỉ có endpoints
- Có thể được gọi từ bất kỳ client nào

**Ứng dụng:**
- Mobile apps (iOS, Android)
- Single Page Applications (React, Angular, Vue)
- Microservices
- Integration giữa các hệ thống

### 6.1.2. RESTful API

**REST (Representational State Transfer)** là một kiến trúc thiết kế API.

**Nguyên tắc REST:**

1. **Client-Server**: Tách biệt client và server
2. **Stateless**: Mỗi request độc lập, không lưu state
3. **Cacheable**: Response có thể cache
4. **Uniform Interface**: Giao diện thống nhất
5. **Layered System**: Hệ thống phân lớp

**HTTP Methods:**

| Method | Mục đích | SQL tương đương |
|--------|----------|-----------------|
| GET | Lấy dữ liệu | SELECT |
| POST | Tạo mới | INSERT |
| PUT | Cập nhật toàn bộ | UPDATE |
| PATCH | Cập nhật một phần | UPDATE |
| DELETE | Xóa | DELETE |

**HTTP Status Codes:**

| Code | Ý nghĩa | Khi nào dùng |
|------|---------|--------------|
| 200 OK | Thành công | GET, PUT thành công |
| 201 Created | Tạo thành công | POST thành công |
| 204 No Content | Thành công, không trả data | DELETE thành công |
| 400 Bad Request | Request không hợp lệ | Validation lỗi |
| 401 Unauthorized | Chưa xác thực | Chưa login |
| 403 Forbidden | Không có quyền | Không đủ permission |
| 404 Not Found | Không tìm thấy | Resource không tồn tại |
| 500 Internal Server Error | Lỗi server | Exception |

**RESTful URL Design:**

```
GET    /api/students           - Lấy tất cả sinh viên
GET    /api/students/{id}      - Lấy sinh viên theo ID
POST   /api/students           - Tạo sinh viên mới
PUT    /api/students/{id}      - Cập nhật sinh viên
DELETE /api/students/{id}      - Xóa sinh viên

GET    /api/students/{id}/grades - Lấy điểm của sinh viên
```

### 6.1.3. JSON

**JSON (JavaScript Object Notation)** là định dạng dữ liệu phổ biến cho Web API.

**Ví dụ:**
```json
{
  "maSV": "SV001",
  "hoTen": "Nguyễn Văn A",
  "ngaySinh": "2000-01-01",
  "gioiTinh": "Nam",
  "email": "a@email.com",
  "lop": {
    "maLop": "CNTT01",
    "tenLop": "Công nghệ thông tin 01"
  },
  "ketQuas": [
    {
      "maMonHoc": "MH001",
      "tenMonHoc": "Lập trình C#",
      "diem": 8.5
    },
    {
      "maMonHoc": "MH002",
      "tenMonHoc": "Cơ sở dữ liệu",
      "diem": 9.0
    }
  ]
}
```

---

## 6.2. TẠO WEB API

### 6.2.1. Tạo ASP.NET Core Web API Project

**Bước 1: Tạo project**
```bash
# CLI
dotnet new webapi -n QuanLySinhVien.API

# Hoặc Visual Studio:
# File → New → Project → ASP.NET Core Web API
```

**Cấu trúc project:**
```
QuanLySinhVien.API
├── Controllers/
│   └── WeatherForecastController.cs
├── Models/
├── Properties/
│   └── launchSettings.json
├── appsettings.json
├── appsettings.Development.json
├── Program.cs
└── WeatherForecast.cs
```

### 6.2.2. Program.cs (ASP.NET Core 6+)

```csharp
var builder = WebApplication.CreateBuilder(args);

// Add services to the container
builder.Services.AddControllers();

// Swagger/OpenAPI
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// CORS
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", builder =>
    {
        builder.AllowAnyOrigin()
               .AllowAnyMethod()
               .AllowAnyHeader();
    });
});

// Add DbContext
builder.Services.AddDbContext<QLSVContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();

// Configure the HTTP request pipeline
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseCors("AllowAll");

app.UseAuthorization();

app.MapControllers();

app.Run();
```

### 6.2.3. Tạo Model

**SinhVien.cs:**
```csharp
public class SinhVien
{
    public string MaSV { get; set; }
    public string HoTen { get; set; }
    public DateTime NgaySinh { get; set; }
    public string GioiTinh { get; set; }
    public string Email { get; set; }
    public string SoDienThoai { get; set; }
    public string MaLop { get; set; }

    // Navigation properties
    public Lop Lop { get; set; }
    public ICollection<KetQua> KetQuas { get; set; }
}
```

### 6.2.4. Tạo DbContext

**QLSVContext.cs:**
```csharp
using Microsoft.EntityFrameworkCore;

public class QLSVContext : DbContext
{
    public QLSVContext(DbContextOptions<QLSVContext> options)
        : base(options)
    {
    }

    public DbSet<SinhVien> SinhViens { get; set; }
    public DbSet<Lop> Lops { get; set; }
    public DbSet<MonHoc> MonHocs { get; set; }
    public DbSet<KetQua> KetQuas { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<SinhVien>()
            .HasKey(s => s.MaSV);

        modelBuilder.Entity<SinhVien>()
            .HasOne(s => s.Lop)
            .WithMany(l => l.SinhViens)
            .HasForeignKey(s => s.MaLop);

        modelBuilder.Entity<KetQua>()
            .HasKey(kq => new { kq.MaSV, kq.MaMonHoc });

        base.OnModelCreating(modelBuilder);
    }
}
```

**appsettings.json:**
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=.;Database=QLSV;Trusted_Connection=True;MultipleActiveResultSets=true;TrustServerCertificate=True"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

### 6.2.5. Tạo API Controller

**SinhViensController.cs:**
```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace QuanLySinhVien.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SinhViensController : ControllerBase
    {
        private readonly QLSVContext _context;

        public SinhViensController(QLSVContext context)
        {
            _context = context;
        }

        // GET: api/SinhViens
        [HttpGet]
        public async Task<ActionResult<IEnumerable<SinhVien>>> GetSinhViens()
        {
            return await _context.SinhViens
                .Include(s => s.Lop)
                .ToListAsync();
        }

        // GET: api/SinhViens/SV001
        [HttpGet("{id}")]
        public async Task<ActionResult<SinhVien>> GetSinhVien(string id)
        {
            var sinhVien = await _context.SinhViens
                .Include(s => s.Lop)
                .Include(s => s.KetQuas)
                .ThenInclude(kq => kq.MonHoc)
                .FirstOrDefaultAsync(s => s.MaSV == id);

            if (sinhVien == null)
            {
                return NotFound(new { message = "Không tìm thấy sinh viên" });
            }

            return sinhVien;
        }

        // POST: api/SinhViens
        [HttpPost]
        public async Task<ActionResult<SinhVien>> PostSinhVien(SinhVien sinhVien)
        {
            // Validate
            if (string.IsNullOrEmpty(sinhVien.MaSV))
            {
                return BadRequest(new { message = "Mã sinh viên không được rỗng" });
            }

            // Kiểm tra trùng
            if (await _context.SinhViens.AnyAsync(s => s.MaSV == sinhVien.MaSV))
            {
                return Conflict(new { message = "Mã sinh viên đã tồn tại" });
            }

            _context.SinhViens.Add(sinhVien);
            await _context.SaveChangesAsync();

            return CreatedAtAction(nameof(GetSinhVien), new { id = sinhVien.MaSV }, sinhVien);
        }

        // PUT: api/SinhViens/SV001
        [HttpPut("{id}")]
        public async Task<IActionResult> PutSinhVien(string id, SinhVien sinhVien)
        {
            if (id != sinhVien.MaSV)
            {
                return BadRequest(new { message = "Mã sinh viên không khớp" });
            }

            _context.Entry(sinhVien).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!SinhVienExists(id))
                {
                    return NotFound(new { message = "Không tìm thấy sinh viên" });
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // DELETE: api/SinhViens/SV001
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteSinhVien(string id)
        {
            var sinhVien = await _context.SinhViens.FindAsync(id);

            if (sinhVien == null)
            {
                return NotFound(new { message = "Không tìm thấy sinh viên" });
            }

            _context.SinhViens.Remove(sinhVien);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        // GET: api/SinhViens/search?keyword=nguyen
        [HttpGet("search")]
        public async Task<ActionResult<IEnumerable<SinhVien>>> SearchSinhViens([FromQuery] string keyword)
        {
            if (string.IsNullOrEmpty(keyword))
            {
                return await GetSinhViens();
            }

            var sinhViens = await _context.SinhViens
                .Include(s => s.Lop)
                .Where(s => s.MaSV.Contains(keyword) || s.HoTen.Contains(keyword))
                .ToListAsync();

            return sinhViens;
        }

        // GET: api/SinhViens/SV001/ketqua
        [HttpGet("{id}/ketqua")]
        public async Task<ActionResult<IEnumerable<KetQua>>> GetKetQuaSinhVien(string id)
        {
            var sinhVien = await _context.SinhViens.FindAsync(id);

            if (sinhVien == null)
            {
                return NotFound(new { message = "Không tìm thấy sinh viên" });
            }

            var ketQuas = await _context.KetQuas
                .Include(kq => kq.MonHoc)
                .Where(kq => kq.MaSV == id)
                .ToListAsync();

            return ketQuas;
        }

        private bool SinhVienExists(string id)
        {
            return _context.SinhViens.Any(e => e.MaSV == id);
        }
    }
}
```

### 6.2.6. DTO Pattern

**Tạo DTO để kiểm soát dữ liệu trả về:**

**DTOs/SinhVienDTO.cs:**
```csharp
public class SinhVienDTO
{
    public string MaSV { get; set; }
    public string HoTen { get; set; }
    public DateTime NgaySinh { get; set; }
    public string GioiTinh { get; set; }
    public string Email { get; set; }
    public string TenLop { get; set; }
    public int Tuoi => DateTime.Now.Year - NgaySinh.Year;
}

public class CreateSinhVienDTO
{
    [Required]
    [StringLength(10)]
    public string MaSV { get; set; }

    [Required]
    [StringLength(100)]
    public string HoTen { get; set; }

    [Required]
    public DateTime NgaySinh { get; set; }

    [Required]
    public string GioiTinh { get; set; }

    [EmailAddress]
    public string Email { get; set; }

    [Required]
    public string MaLop { get; set; }
}
```

**Controller với DTO:**
```csharp
[HttpGet]
public async Task<ActionResult<IEnumerable<SinhVienDTO>>> GetSinhViens()
{
    var sinhViens = await _context.SinhViens
        .Include(s => s.Lop)
        .Select(s => new SinhVienDTO
        {
            MaSV = s.MaSV,
            HoTen = s.HoTen,
            NgaySinh = s.NgaySinh,
            GioiTinh = s.GioiTinh,
            Email = s.Email,
            TenLop = s.Lop.TenLop
        })
        .ToListAsync();

    return sinhViens;
}

[HttpPost]
public async Task<ActionResult<SinhVienDTO>> PostSinhVien(CreateSinhVienDTO dto)
{
    if (!ModelState.IsValid)
    {
        return BadRequest(ModelState);
    }

    var sinhVien = new SinhVien
    {
        MaSV = dto.MaSV,
        HoTen = dto.HoTen,
        NgaySinh = dto.NgaySinh,
        GioiTinh = dto.GioiTinh,
        Email = dto.Email,
        MaLop = dto.MaLop
    };

    _context.SinhViens.Add(sinhVien);
    await _context.SaveChangesAsync();

    var result = new SinhVienDTO
    {
        MaSV = sinhVien.MaSV,
        HoTen = sinhVien.HoTen,
        NgaySinh = sinhVien.NgaySinh,
        GioiTinh = sinhVien.GioiTinh,
        Email = sinhVien.Email
    };

    return CreatedAtAction(nameof(GetSinhVien), new { id = sinhVien.MaSV }, result);
}
```

---

## 6.3. TEST API

### 6.3.1. Swagger UI

Truy cập: `https://localhost:5001/swagger`

Swagger tự động tạo UI để test API.

### 6.3.2. Postman

**GET Request:**
```
GET https://localhost:5001/api/sinhviens
```

**POST Request:**
```
POST https://localhost:5001/api/sinhviens
Content-Type: application/json

{
  "maSV": "SV001",
  "hoTen": "Nguyễn Văn A",
  "ngaySinh": "2000-01-01",
  "gioiTinh": "Nam",
  "email": "a@email.com",
  "maLop": "CNTT01"
}
```

**PUT Request:**
```
PUT https://localhost:5001/api/sinhviens/SV001
Content-Type: application/json

{
  "maSV": "SV001",
  "hoTen": "Nguyễn Văn A - Updated",
  "ngaySinh": "2000-01-01",
  "gioiTinh": "Nam",
  "email": "a.updated@email.com",
  "maLop": "CNTT01"
}
```

**DELETE Request:**
```
DELETE https://localhost:5001/api/sinhviens/SV001
```

### 6.3.3. Test bằng code (C#)

```csharp
using System.Net.Http;
using System.Net.Http.Json;

public class ApiClient
{
    private readonly HttpClient _httpClient;

    public ApiClient()
    {
        _httpClient = new HttpClient
        {
            BaseAddress = new Uri("https://localhost:5001/")
        };
    }

    // GET
    public async Task<List<SinhVien>> GetAllSinhViens()
    {
        return await _httpClient.GetFromJsonAsync<List<SinhVien>>("api/sinhviens");
    }

    // GET by ID
    public async Task<SinhVien> GetSinhVien(string id)
    {
        return await _httpClient.GetFromJsonAsync<SinhVien>($"api/sinhviens/{id}");
    }

    // POST
    public async Task<SinhVien> CreateSinhVien(SinhVien sv)
    {
        var response = await _httpClient.PostAsJsonAsync("api/sinhviens", sv);
        response.EnsureSuccessStatusCode();
        return await response.Content.ReadFromJsonAsync<SinhVien>();
    }

    // PUT
    public async Task UpdateSinhVien(string id, SinhVien sv)
    {
        var response = await _httpClient.PutAsJsonAsync($"api/sinhviens/{id}", sv);
        response.EnsureSuccessStatusCode();
    }

    // DELETE
    public async Task DeleteSinhVien(string id)
    {
        var response = await _httpClient.DeleteAsync($"api/sinhviens/{id}");
        response.EnsureSuccessStatusCode();
    }
}
```

---

## 6.4. PAGINATION, FILTERING, SORTING

### Pagination

**Query Parameters:**
```csharp
[HttpGet]
public async Task<ActionResult<PaginatedResult<SinhVienDTO>>> GetSinhViens(
    [FromQuery] int pageNumber = 1,
    [FromQuery] int pageSize = 10)
{
    var totalCount = await _context.SinhViens.CountAsync();

    var sinhViens = await _context.SinhViens
        .Include(s => s.Lop)
        .Skip((pageNumber - 1) * pageSize)
        .Take(pageSize)
        .Select(s => new SinhVienDTO
        {
            MaSV = s.MaSV,
            HoTen = s.HoTen,
            TenLop = s.Lop.TenLop
        })
        .ToListAsync();

    var result = new PaginatedResult<SinhVienDTO>
    {
        Data = sinhViens,
        PageNumber = pageNumber,
        PageSize = pageSize,
        TotalCount = totalCount,
        TotalPages = (int)Math.Ceiling(totalCount / (double)pageSize)
    };

    return result;
}

public class PaginatedResult<T>
{
    public List<T> Data { get; set; }
    public int PageNumber { get; set; }
    public int PageSize { get; set; }
    public int TotalCount { get; set; }
    public int TotalPages { get; set; }
    public bool HasPrevious => PageNumber > 1;
    public bool HasNext => PageNumber < TotalPages;
}
```

**Usage:**
```
GET /api/sinhviens?pageNumber=2&pageSize=20
```

### Filtering & Sorting

```csharp
[HttpGet]
public async Task<ActionResult<IEnumerable<SinhVienDTO>>> GetSinhViens(
    [FromQuery] string? maLop,
    [FromQuery] string? gioiTinh,
    [FromQuery] string? keyword,
    [FromQuery] string? sortBy,
    [FromQuery] bool descending = false)
{
    var query = _context.SinhViens.AsQueryable();

    // Filtering
    if (!string.IsNullOrEmpty(maLop))
    {
        query = query.Where(s => s.MaLop == maLop);
    }

    if (!string.IsNullOrEmpty(gioiTinh))
    {
        query = query.Where(s => s.GioiTinh == gioiTinh);
    }

    if (!string.IsNullOrEmpty(keyword))
    {
        query = query.Where(s => s.MaSV.Contains(keyword) || s.HoTen.Contains(keyword));
    }

    // Sorting
    query = sortBy?.ToLower() switch
    {
        "hoten" => descending ? query.OrderByDescending(s => s.HoTen) : query.OrderBy(s => s.HoTen),
        "ngaysinh" => descending ? query.OrderByDescending(s => s.NgaySinh) : query.OrderBy(s => s.NgaySinh),
        _ => query.OrderBy(s => s.MaSV)
    };

    var result = await query
        .Include(s => s.Lop)
        .Select(s => new SinhVienDTO
        {
            MaSV = s.MaSV,
            HoTen = s.HoTen,
            TenLop = s.Lop.TenLop
        })
        .ToListAsync();

    return result;
}
```

**Usage:**
```
GET /api/sinhviens?maLop=CNTT01&gioiTinh=Nam&sortBy=hoten&descending=true
```

---

## 6.5. DEPLOY LÊN AZURE

### 6.5.1. Chuẩn bị

1. Tạo Azure Account (trial miễn phí)
2. Cài Azure CLI hoặc dùng Azure Portal

### 6.5.2. Tạo Azure SQL Database

**Azure Portal:**
1. Tạo SQL Database
2. Chọn tier: Basic/Standard
3. Lấy connection string

**Connection string:**
```
Server=tcp:yourserver.database.windows.net,1433;Initial Catalog=QLSV;Persist Security Info=False;User ID=admin;Password=yourpassword;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
```

### 6.5.3. Deploy Web API

**Visual Studio:**
1. Right-click project → Publish
2. Chọn Azure → Azure App Service (Windows/Linux)
3. Tạo App Service mới
4. Configure settings
5. Publish

**Azure CLI:**
```bash
# Login
az login

# Tạo Resource Group
az group create --name MyResourceGroup --location eastus

# Tạo App Service Plan
az appservice plan create --name MyPlan --resource-group MyResourceGroup --sku B1

# Tạo Web App
az webapp create --name MyWebAPI --resource-group MyResourceGroup --plan MyPlan

# Deploy
az webapp deployment source config-zip --resource-group MyResourceGroup --name MyWebAPI --src ./publish.zip
```

### 6.5.4. Cấu hình Connection String

**Azure Portal:**
1. Vào App Service
2. Configuration → Connection strings
3. Thêm connection string
4. Save

---

## TÓM TẮT CHƯƠNG 6

### RESTful API Best Practices

1. **Sử dụng HTTP methods đúng**: GET, POST, PUT, DELETE
2. **Trả về status code chính xác**: 200, 201, 400, 404, 500
3. **Sử dụng JSON**: Định dạng chuẩn
4. **Versioning**: `/api/v1/students`
5. **Pagination**: Cho endpoint trả về nhiều dữ liệu
6. **Filtering & Sorting**: Query parameters
7. **Error handling**: Trả về message rõ ràng
8. **Security**: Authentication, Authorization
9. **Documentation**: Swagger/OpenAPI
10. **CORS**: Cho phép cross-origin requests

### Các công nghệ sử dụng

- **ASP.NET Core**: Framework
- **Entity Framework Core**: ORM
- **LINQ**: Truy vấn dữ liệu
- **Swagger**: API documentation
- **Azure**: Cloud hosting

---

**Kết thúc Chương 6**

---

# KẾT THÚC TÀI LIỆU LÝ THUYẾT

Đây là tài liệu lý thuyết đầy đủ cho môn **Lập trình cơ sở dữ liệu** theo đề cương của Trường Đại học Mở TP.HCM.

**6 chương đã được soạn:**
1. Ngôn ngữ T-SQL
2. ADO.NET
3. Kiến trúc đa lớp
4. LINQ
5. Entity Framework
6. ASP.NET Core Web API

**Lưu ý khi học:**
- Thực hành song song với lý thuyết
- Làm các bài tập cuối mỗi chương
- Tham khảo tài liệu gốc từ giảng viên
- Xây dựng project thực tế để củng cố kiến thức

**Chúc bạn học tốt!**
