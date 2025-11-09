# CHƯƠNG 2: ADO.NET

## Mục tiêu học tập
Sau khi học xong chương này, sinh viên có khả năng:
- Hiểu kiến trúc và các thành phần của ADO.NET
- Sử dụng Connected Model và Disconnected Model
- Thao tác dữ liệu với SqlConnection, SqlCommand, SqlDataReader
- Sử dụng DataSet, DataAdapter để làm việc với dữ liệu
- Binding dữ liệu với các control trên form

---

## 2.1. TỔNG QUAN ADO.NET

### ADO.NET là gì?

**ADO.NET** (ActiveX Data Objects .NET) là một tập hợp các lớp trong .NET Framework cho phép ứng dụng .NET tương tác với cơ sở dữ liệu.

### Đặc điểm của ADO.NET

1. **Hỗ trợ nhiều loại CSDL**: SQL Server, Oracle, MySQL, Access, v.v.
2. **Disconnected Architecture**: Làm việc với dữ liệu offline
3. **Dataset-based**: Sử dụng Dataset như bộ nhớ cache
4. **XML Integration**: Tích hợp với XML
5. **Performance**: Hiệu suất cao với data reader

### Kiến trúc ADO.NET

```
┌─────────────────────────────────────────────────────────┐
│               Ứng dụng .NET (C#, VB.NET)                │
├─────────────────────────────────────────────────────────┤
│                    ADO.NET                              │
│  ┌──────────────────────┐  ┌──────────────────────┐   │
│  │  Data Provider       │  │    DataSet           │   │
│  │  - Connection        │  │  - DataTable         │   │
│  │  - Command           │  │  - DataRelation      │   │
│  │  - DataReader        │  │  - Constraints       │   │
│  │  - DataAdapter       │  └──────────────────────┘   │
│  └──────────────────────┘                             │
├─────────────────────────────────────────────────────────┤
│                     Database                            │
│        (SQL Server, Oracle, MySQL...)                  │
└─────────────────────────────────────────────────────────┘
```

### Các thành phần chính của ADO.NET

**1. Data Provider** (Nhà cung cấp dữ liệu)
- **Connection**: Kết nối đến database
- **Command**: Thực thi câu lệnh SQL
- **DataReader**: Đọc dữ liệu forward-only, read-only
- **DataAdapter**: Cầu nối giữa DataSet và database

**2. DataSet** (Tập dữ liệu)
- Bộ nhớ cache dữ liệu offline
- Có thể chứa nhiều DataTable
- Hỗ trợ quan hệ giữa các bảng

### Các Data Provider phổ biến

| Provider | Namespace | Dùng cho |
|----------|-----------|----------|
| SQL Server | System.Data.SqlClient | SQL Server |
| OLE DB | System.Data.OleDb | Access, Excel |
| ODBC | System.Data.Odbc | MySQL, PostgreSQL |
| Oracle | System.Data.OracleClient | Oracle Database |

---

## 2.2. MÔ HÌNH KẾT NỐI VÀ PHI KẾT NỐI

### Connected Model (Mô hình kết nối)

**Đặc điểm:**
- Giữ kết nối liên tục với database
- Sử dụng **Connection**, **Command**, **DataReader**
- Đọc dữ liệu forward-only (chỉ đọc tiến)
- Hiệu suất cao cho việc đọc dữ liệu lớn
- Không thể cập nhật trực tiếp

**Khi nào sử dụng:**
- Đọc dữ liệu một chiều
- Dữ liệu lớn, không cần lưu cache
- Thao tác đơn giản: INSERT, UPDATE, DELETE

**Ví dụ:**
```csharp
using (SqlConnection conn = new SqlConnection(connectionString))
{
    conn.Open();
    SqlCommand cmd = new SqlCommand("SELECT * FROM SinhVien", conn);
    SqlDataReader reader = cmd.ExecuteReader();

    while (reader.Read())
    {
        Console.WriteLine(reader["HoTen"]);
    }

    reader.Close();
} // Connection tự động đóng khi ra khỏi using
```

### Disconnected Model (Mô hình phi kết nối)

**Đặc điểm:**
- Kết nối chỉ mở khi cần thiết
- Sử dụng **DataSet**, **DataAdapter**
- Dữ liệu được cache trong bộ nhớ
- Có thể cập nhật offline, đồng bộ sau
- Hỗ trợ quan hệ giữa các bảng

**Khi nào sử dụng:**
- Cần binding dữ liệu lên UI
- Làm việc offline với dữ liệu
- Cập nhật nhiều bảng cùng lúc
- Dữ liệu cần xử lý phức tạp

**Ví dụ:**
```csharp
SqlConnection conn = new SqlConnection(connectionString);
SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM SinhVien", conn);
DataSet ds = new DataSet();

// Kết nối tự động mở và đóng
adapter.Fill(ds, "SinhVien");

// Làm việc với dữ liệu offline
DataTable dt = ds.Tables["SinhVien"];
foreach (DataRow row in dt.Rows)
{
    Console.WriteLine(row["HoTen"]);
}
```

### So sánh 2 mô hình

| Tiêu chí | Connected | Disconnected |
|----------|-----------|--------------|
| Kết nối | Liên tục | Chỉ khi cần |
| Bộ nhớ | Ít | Nhiều hơn |
| Hiệu suất đọc | Cao | Trung bình |
| Cập nhật | Trực tiếp | Batch update |
| Binding UI | Khó | Dễ dàng |
| Offline work | Không | Có |

---

## 2.3. ĐỐI TƯỢNG SQLCONNECTION

### SqlConnection là gì?

**SqlConnection** đại diện cho kết nối đến SQL Server database.

### Connection String

**Cú pháp kết nối SQL Server:**
```csharp
// Kết nối với Windows Authentication
string connStr = "Data Source=ServerName;Initial Catalog=DatabaseName;Integrated Security=True;";

// Kết nối với SQL Server Authentication
string connStr = "Data Source=ServerName;Initial Catalog=DatabaseName;User ID=sa;Password=123456;";

// Kết nối local
string connStr = "Data Source=.;Initial Catalog=QLSV;Integrated Security=True;";
string connStr = "Data Source=(local);Initial Catalog=QLSV;Integrated Security=True;";
string connStr = "Server=localhost;Database=QLSV;Trusted_Connection=True;";
```

**Các thành phần quan trọng:**
- **Data Source / Server**: Tên server hoặc địa chỉ IP
- **Initial Catalog / Database**: Tên database
- **Integrated Security / Trusted_Connection**: Xác thực Windows
- **User ID / Password**: Tài khoản SQL Server
- **Connection Timeout**: Thời gian chờ kết nối (mặc định 15 giây)
- **Pooling**: Bật/tắt connection pooling (mặc định true)

### Sử dụng SqlConnection

**Ví dụ 1: Mở và đóng kết nối**
```csharp
using System.Data.SqlClient;

string connectionString = "Data Source=.;Initial Catalog=QLSV;Integrated Security=True;";
SqlConnection conn = new SqlConnection(connectionString);

try
{
    conn.Open();
    Console.WriteLine("Kết nối thành công!");
    Console.WriteLine($"Database: {conn.Database}");
    Console.WriteLine($"Server: {conn.DataSource}");
    Console.WriteLine($"State: {conn.State}");
}
catch (SqlException ex)
{
    Console.WriteLine($"Lỗi kết nối: {ex.Message}");
}
finally
{
    if (conn.State == System.Data.ConnectionState.Open)
    {
        conn.Close();
    }
}
```

**Ví dụ 2: Sử dụng using statement (khuyến nghị)**
```csharp
using (SqlConnection conn = new SqlConnection(connectionString))
{
    conn.Open();
    // Thực hiện các thao tác

} // Connection tự động đóng và dispose
```

**Ví dụ 3: Kiểm tra trạng thái kết nối**
```csharp
using (SqlConnection conn = new SqlConnection(connectionString))
{
    Console.WriteLine($"Trạng thái ban đầu: {conn.State}"); // Closed

    conn.Open();
    Console.WriteLine($"Sau khi mở: {conn.State}"); // Open

    // Kiểm tra trạng thái
    if (conn.State == System.Data.ConnectionState.Open)
    {
        Console.WriteLine("Kết nối đang mở");
    }
}
```

### Các phương thức quan trọng

| Phương thức | Mô tả |
|-------------|-------|
| Open() | Mở kết nối |
| Close() | Đóng kết nối |
| Dispose() | Giải phóng tài nguyên |
| BeginTransaction() | Bắt đầu transaction |
| ChangeDatabase() | Chuyển database |

### Các thuộc tính quan trọng

| Thuộc tính | Mô tả |
|-----------|-------|
| ConnectionString | Chuỗi kết nối |
| Database | Tên database hiện tại |
| DataSource | Tên server |
| State | Trạng thái kết nối |
| ServerVersion | Phiên bản SQL Server |

### Best Practices

1. **Luôn đóng kết nối**: Sử dụng `using` hoặc `try-finally`
2. **Connection Pooling**: Tận dụng connection pool của ADO.NET
3. **Lưu connection string an toàn**: Sử dụng `app.config` hoặc `appsettings.json`
4. **Xử lý exception**: Bắt và xử lý `SqlException`

**Ví dụ: Lưu connection string trong App.config**
```xml
<configuration>
  <connectionStrings>
    <add name="QLSV"
         connectionString="Data Source=.;Initial Catalog=QLSV;Integrated Security=True;"
         providerName="System.Data.SqlClient"/>
  </connectionStrings>
</configuration>
```

```csharp
using System.Configuration;

string connectionString = ConfigurationManager.ConnectionStrings["QLSV"].ConnectionString;
```

---

## 2.4. ĐỐI TƯỢNG SQLCOMMAND

### SqlCommand là gì?

**SqlCommand** đại diện cho một câu lệnh SQL hoặc stored procedure để thực thi trên SQL Server.

### Tạo SqlCommand

**Cách 1: Constructor**
```csharp
SqlCommand cmd = new SqlCommand();
cmd.Connection = conn;
cmd.CommandText = "SELECT * FROM SinhVien";
cmd.CommandType = CommandType.Text;
```

**Cách 2: Constructor với tham số**
```csharp
SqlCommand cmd = new SqlCommand("SELECT * FROM SinhVien", conn);
```

**Cách 3: Từ Connection**
```csharp
SqlCommand cmd = conn.CreateCommand();
cmd.CommandText = "SELECT * FROM SinhVien";
```

### Các thuộc tính quan trọng

| Thuộc tính | Mô tả | Giá trị |
|-----------|-------|---------|
| CommandText | Câu lệnh SQL hoặc tên stored procedure | string |
| CommandType | Loại command | Text, StoredProcedure, TableDirect |
| Connection | Kết nối sử dụng | SqlConnection |
| Parameters | Tham số của command | SqlParameterCollection |
| CommandTimeout | Thời gian chờ thực thi (giây) | int (mặc định 30) |

### Các phương thức thực thi

#### 1. ExecuteNonQuery()

Dùng cho: **INSERT, UPDATE, DELETE**

Trả về: Số dòng bị ảnh hưởng

```csharp
using (SqlConnection conn = new SqlConnection(connectionString))
{
    conn.Open();

    string sql = "INSERT INTO SinhVien (MaSV, HoTen, NgaySinh) VALUES (@MaSV, @HoTen, @NgaySinh)";
    SqlCommand cmd = new SqlCommand(sql, conn);

    cmd.Parameters.AddWithValue("@MaSV", "SV001");
    cmd.Parameters.AddWithValue("@HoTen", "Nguyễn Văn A");
    cmd.Parameters.AddWithValue("@NgaySinh", new DateTime(2000, 1, 1));

    int rowsAffected = cmd.ExecuteNonQuery();
    Console.WriteLine($"Đã thêm {rowsAffected} sinh viên");
}
```

**Ví dụ UPDATE:**
```csharp
string sql = "UPDATE SinhVien SET HoTen = @HoTen WHERE MaSV = @MaSV";
SqlCommand cmd = new SqlCommand(sql, conn);

cmd.Parameters.AddWithValue("@MaSV", "SV001");
cmd.Parameters.AddWithValue("@HoTen", "Nguyễn Văn B");

int count = cmd.ExecuteNonQuery();
if (count > 0)
    Console.WriteLine("Cập nhật thành công");
else
    Console.WriteLine("Không tìm thấy sinh viên");
```

**Ví dụ DELETE:**
```csharp
string sql = "DELETE FROM SinhVien WHERE MaSV = @MaSV";
SqlCommand cmd = new SqlCommand(sql, conn);

cmd.Parameters.AddWithValue("@MaSV", "SV001");

int count = cmd.ExecuteNonQuery();
Console.WriteLine($"Đã xóa {count} sinh viên");
```

#### 2. ExecuteScalar()

Dùng cho: Truy vấn trả về **một giá trị duy nhất**

Trả về: Giá trị ở cột đầu tiên, dòng đầu tiên (kiểu object)

```csharp
// Đếm số sinh viên
string sql = "SELECT COUNT(*) FROM SinhVien";
SqlCommand cmd = new SqlCommand(sql, conn);

int count = (int)cmd.ExecuteScalar();
Console.WriteLine($"Tổng số sinh viên: {count}");
```

**Ví dụ 2: Lấy giá trị MAX**
```csharp
string sql = "SELECT MAX(DiemTB) FROM SinhVien";
SqlCommand cmd = new SqlCommand(sql, conn);

object result = cmd.ExecuteScalar();
if (result != DBNull.Value)
{
    float maxDiem = Convert.ToSingle(result);
    Console.WriteLine($"Điểm cao nhất: {maxDiem}");
}
```

**Ví dụ 3: Kiểm tra tồn tại**
```csharp
string sql = "SELECT COUNT(*) FROM SinhVien WHERE Email = @Email";
SqlCommand cmd = new SqlCommand(sql, conn);
cmd.Parameters.AddWithValue("@Email", "test@email.com");

int count = (int)cmd.ExecuteScalar();
bool exists = count > 0;

Console.WriteLine(exists ? "Email đã tồn tại" : "Email chưa tồn tại");
```

#### 3. ExecuteReader()

Dùng cho: Truy vấn **SELECT** trả về nhiều dòng

Trả về: SqlDataReader

```csharp
string sql = "SELECT MaSV, HoTen, NgaySinh FROM SinhVien";
SqlCommand cmd = new SqlCommand(sql, conn);

SqlDataReader reader = cmd.ExecuteReader();

while (reader.Read())
{
    string maSV = reader["MaSV"].ToString();
    string hoTen = reader["HoTen"].ToString();
    DateTime ngaySinh = Convert.ToDateTime(reader["NgaySinh"]);

    Console.WriteLine($"{maSV} - {hoTen} - {ngaySinh:dd/MM/yyyy}");
}

reader.Close();
```

### Sử dụng Parameters (Tham số)

**Tại sao phải dùng Parameters?**
1. Ngăn chặn SQL Injection
2. Tăng hiệu suất (query plan được cache)
3. Xử lý kiểu dữ liệu tự động

**Cách thêm Parameters:**

**Cách 1: AddWithValue (đơn giản, phổ biến)**
```csharp
cmd.Parameters.AddWithValue("@MaSV", "SV001");
cmd.Parameters.AddWithValue("@HoTen", "Nguyễn Văn A");
cmd.Parameters.AddWithValue("@Tuoi", 20);
```

**Cách 2: Add (chỉ định kiểu dữ liệu)**
```csharp
cmd.Parameters.Add("@MaSV", SqlDbType.NVarChar, 10).Value = "SV001";
cmd.Parameters.Add("@Tuoi", SqlDbType.Int).Value = 20;
cmd.Parameters.Add("@DiemTB", SqlDbType.Float).Value = 8.5;
```

**Cách 3: SqlParameter object**
```csharp
SqlParameter param = new SqlParameter();
param.ParameterName = "@MaSV";
param.SqlDbType = SqlDbType.NVarChar;
param.Size = 10;
param.Value = "SV001";
cmd.Parameters.Add(param);
```

**Ví dụ: Tìm kiếm với nhiều điều kiện**
```csharp
string sql = @"SELECT * FROM SinhVien
               WHERE (@HoTen IS NULL OR HoTen LIKE '%' + @HoTen + '%')
               AND (@Khoa IS NULL OR Khoa = @Khoa)
               AND (@DiemMin IS NULL OR DiemTB >= @DiemMin)";

SqlCommand cmd = new SqlCommand(sql, conn);

// Null nếu không tìm kiếm
cmd.Parameters.AddWithValue("@HoTen", string.IsNullOrEmpty(hoTen) ? (object)DBNull.Value : hoTen);
cmd.Parameters.AddWithValue("@Khoa", string.IsNullOrEmpty(khoa) ? (object)DBNull.Value : khoa);
cmd.Parameters.AddWithValue("@DiemMin", diemMin.HasValue ? (object)diemMin.Value : DBNull.Value);
```

### Gọi Stored Procedure

**Ví dụ 1: Stored Procedure không tham số**
```sql
-- SQL: Tạo procedure
CREATE PROCEDURE sp_LayDanhSachSinhVien
AS
BEGIN
    SELECT * FROM SinhVien ORDER BY HoTen;
END
GO
```

```csharp
// C#: Gọi procedure
SqlCommand cmd = new SqlCommand("sp_LayDanhSachSinhVien", conn);
cmd.CommandType = CommandType.StoredProcedure;

SqlDataReader reader = cmd.ExecuteReader();
// Xử lý dữ liệu...
```

**Ví dụ 2: Stored Procedure với tham số đầu vào**
```sql
-- SQL
CREATE PROCEDURE sp_TimSinhVien
    @MaSV NVARCHAR(10)
AS
BEGIN
    SELECT * FROM SinhVien WHERE MaSV = @MaSV;
END
GO
```

```csharp
// C#
SqlCommand cmd = new SqlCommand("sp_TimSinhVien", conn);
cmd.CommandType = CommandType.StoredProcedure;
cmd.Parameters.AddWithValue("@MaSV", "SV001");

SqlDataReader reader = cmd.ExecuteReader();
if (reader.Read())
{
    Console.WriteLine(reader["HoTen"]);
}
```

**Ví dụ 3: Stored Procedure với OUTPUT parameter**
```sql
-- SQL
CREATE PROCEDURE sp_ThemSinhVien
    @MaSV NVARCHAR(10),
    @HoTen NVARCHAR(100),
    @NgaySinh DATE,
    @ThongBao NVARCHAR(200) OUTPUT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM SinhVien WHERE MaSV = @MaSV)
    BEGIN
        SET @ThongBao = N'Mã sinh viên đã tồn tại';
        RETURN -1;
    END

    INSERT INTO SinhVien (MaSV, HoTen, NgaySinh)
    VALUES (@MaSV, @HoTen, @NgaySinh);

    SET @ThongBao = N'Thêm thành công';
    RETURN 0;
END
GO
```

```csharp
// C#
SqlCommand cmd = new SqlCommand("sp_ThemSinhVien", conn);
cmd.CommandType = CommandType.StoredProcedure;

cmd.Parameters.AddWithValue("@MaSV", "SV001");
cmd.Parameters.AddWithValue("@HoTen", "Nguyễn Văn A");
cmd.Parameters.AddWithValue("@NgaySinh", new DateTime(2000, 1, 1));

// OUTPUT parameter
SqlParameter outputParam = new SqlParameter("@ThongBao", SqlDbType.NVarChar, 200);
outputParam.Direction = ParameterDirection.Output;
cmd.Parameters.Add(outputParam);

// Return value
SqlParameter returnParam = new SqlParameter("@ReturnValue", SqlDbType.Int);
returnParam.Direction = ParameterDirection.ReturnValue;
cmd.Parameters.Add(returnParam);

cmd.ExecuteNonQuery();

string message = outputParam.Value.ToString();
int returnValue = (int)returnParam.Value;

Console.WriteLine($"Thông báo: {message}");
Console.WriteLine($"Mã lỗi: {returnValue}");
```

---

## 2.5. ĐỐI TƯỢNG SQLDATAREADER

### SqlDataReader là gì?

**SqlDataReader** là đối tượng dùng để đọc dữ liệu từ SQL Server theo kiểu **forward-only** (chỉ đọc tiến) và **read-only** (chỉ đọc).

### Đặc điểm

1. **Forward-only**: Chỉ đọc từ đầu đến cuối, không quay lại
2. **Read-only**: Không thể cập nhật dữ liệu
3. **Connected**: Giữ kết nối trong khi đọc
4. **Fast**: Hiệu suất cao, tiết kiệm bộ nhớ
5. **One row at a time**: Đọc từng dòng một

### Sử dụng SqlDataReader

**Ví dụ cơ bản:**
```csharp
using (SqlConnection conn = new SqlConnection(connectionString))
{
    conn.Open();

    SqlCommand cmd = new SqlCommand("SELECT MaSV, HoTen, DiemTB FROM SinhVien", conn);
    SqlDataReader reader = cmd.ExecuteReader();

    while (reader.Read())
    {
        // Cách 1: Truy cập bằng tên cột (string)
        string maSV = reader["MaSV"].ToString();
        string hoTen = reader["HoTen"].ToString();

        // Cách 2: Truy cập bằng index (int)
        string maSV2 = reader[0].ToString();

        // Cách 3: Sử dụng phương thức Get (an toàn kiểu)
        string maSV3 = reader.GetString(0);
        string hoTen3 = reader.GetString(1);
        float diemTB = reader.GetFloat(2);

        Console.WriteLine($"{maSV} - {hoTen} - {diemTB}");
    }

    reader.Close();
}
```

### Các phương thức Get() theo kiểu dữ liệu

| Phương thức | Kiểu trả về | SQL Type |
|-------------|-------------|----------|
| GetString() | string | NVARCHAR, VARCHAR |
| GetInt32() | int | INT |
| GetInt64() | long | BIGINT |
| GetBoolean() | bool | BIT |
| GetDateTime() | DateTime | DATE, DATETIME |
| GetDecimal() | decimal | DECIMAL, MONEY |
| GetDouble() | double | FLOAT |
| GetFloat() | float | REAL |
| GetGuid() | Guid | UNIQUEIDENTIFIER |

**Ví dụ sử dụng Get():**
```csharp
while (reader.Read())
{
    int id = reader.GetInt32(0);                    // INT
    string hoTen = reader.GetString(1);             // NVARCHAR
    DateTime ngaySinh = reader.GetDateTime(2);      // DATE
    bool gioiTinh = reader.GetBoolean(3);           // BIT
    decimal luong = reader.GetDecimal(4);           // DECIMAL
    Guid guid = reader.GetGuid(5);                  // UNIQUEIDENTIFIER

    Console.WriteLine($"{id} - {hoTen} - {ngaySinh:dd/MM/yyyy}");
}
```

### Xử lý giá trị NULL

**Cách 1: Kiểm tra IsDBNull()**
```csharp
while (reader.Read())
{
    string maSV = reader.GetString(0);

    string email;
    if (reader.IsDBNull(1)) // Kiểm tra cột Email có NULL không
    {
        email = "Chưa có email";
    }
    else
    {
        email = reader.GetString(1);
    }

    Console.WriteLine($"{maSV} - {email}");
}
```

**Cách 2: Sử dụng toán tử ??**
```csharp
while (reader.Read())
{
    string maSV = reader["MaSV"].ToString();
    string email = reader["Email"] == DBNull.Value ? "Chưa có" : reader["Email"].ToString();

    // Hoặc
    string email2 = reader["Email"]?.ToString() ?? "Chưa có";

    Console.WriteLine($"{maSV} - {email}");
}
```

### Đọc nhiều result set

Một Command có thể trả về nhiều result set:

```csharp
string sql = @"
    SELECT * FROM SinhVien;
    SELECT * FROM MonHoc;
    SELECT * FROM KetQua;
";

SqlCommand cmd = new SqlCommand(sql, conn);
SqlDataReader reader = cmd.ExecuteReader();

// Result set 1: SinhVien
Console.WriteLine("=== Danh sách sinh viên ===");
while (reader.Read())
{
    Console.WriteLine(reader["HoTen"]);
}

// Chuyển sang result set tiếp theo
reader.NextResult();

// Result set 2: MonHoc
Console.WriteLine("\n=== Danh sách môn học ===");
while (reader.Read())
{
    Console.WriteLine(reader["TenMonHoc"]);
}

// Chuyển sang result set tiếp theo
reader.NextResult();

// Result set 3: KetQua
Console.WriteLine("\n=== Kết quả học tập ===");
while (reader.Read())
{
    Console.WriteLine($"{reader["MaSV"]} - {reader["Diem"]}");
}

reader.Close();
```

### Các thuộc tính và phương thức quan trọng

| Thành viên | Loại | Mô tả |
|-----------|------|-------|
| Read() | Method | Di chuyển đến dòng tiếp theo |
| NextResult() | Method | Chuyển sang result set tiếp theo |
| Close() | Method | Đóng DataReader |
| HasRows | Property | Kiểm tra có dữ liệu không |
| FieldCount | Property | Số cột trong result set |
| IsClosed | Property | Kiểm tra đã đóng chưa |
| GetName() | Method | Lấy tên cột theo index |
| GetOrdinal() | Method | Lấy index của cột theo tên |

**Ví dụ sử dụng:**
```csharp
SqlDataReader reader = cmd.ExecuteReader();

// Kiểm tra có dữ liệu không
if (reader.HasRows)
{
    Console.WriteLine($"Số cột: {reader.FieldCount}");

    // In tên các cột
    for (int i = 0; i < reader.FieldCount; i++)
    {
        Console.Write($"{reader.GetName(i)}\t");
    }
    Console.WriteLine();

    // In dữ liệu
    while (reader.Read())
    {
        for (int i = 0; i < reader.FieldCount; i++)
        {
            Console.Write($"{reader[i]}\t");
        }
        Console.WriteLine();
    }
}
else
{
    Console.WriteLine("Không có dữ liệu");
}

reader.Close();
```

### Ví dụ thực tế: Load dữ liệu vào List<T>

```csharp
public class SinhVien
{
    public string MaSV { get; set; }
    public string HoTen { get; set; }
    public DateTime NgaySinh { get; set; }
    public string GioiTinh { get; set; }
    public string Email { get; set; }
}

public List<SinhVien> LayDanhSachSinhVien()
{
    List<SinhVien> list = new List<SinhVien>();

    using (SqlConnection conn = new SqlConnection(connectionString))
    {
        conn.Open();
        SqlCommand cmd = new SqlCommand("SELECT * FROM SinhVien", conn);
        SqlDataReader reader = cmd.ExecuteReader();

        while (reader.Read())
        {
            SinhVien sv = new SinhVien
            {
                MaSV = reader["MaSV"].ToString(),
                HoTen = reader["HoTen"].ToString(),
                NgaySinh = reader.GetDateTime(reader.GetOrdinal("NgaySinh")),
                GioiTinh = reader["GioiTinh"].ToString(),
                Email = reader["Email"] == DBNull.Value ? null : reader["Email"].ToString()
            };

            list.Add(sv);
        }

        reader.Close();
    }

    return list;
}
```

---

## 2.6. DATASET VÀ DATA ADAPTER

### 2.6.1. DataSet

**DataSet là gì?**

**DataSet** là một bộ nhớ cache (cache memory) chứa dữ liệu trong bộ nhớ. DataSet có thể chứa nhiều DataTable và quan hệ giữa chúng.

**Đặc điểm:**
- Disconnected: Làm việc offline, không cần kết nối liên tục
- In-memory: Dữ liệu lưu trong RAM
- Nhiều bảng: Chứa nhiều DataTable
- Quan hệ: Hỗ trợ DataRelation giữa các bảng
- XML-based: Có thể export/import XML

**Cấu trúc DataSet:**
```
DataSet
├── Tables (DataTableCollection)
│   ├── DataTable1
│   │   ├── Columns (DataColumnCollection)
│   │   ├── Rows (DataRowCollection)
│   │   └── Constraints (ConstraintCollection)
│   ├── DataTable2
│   └── ...
└── Relations (DataRelationCollection)
```

**Ví dụ tạo DataSet thủ công:**
```csharp
// Tạo DataSet
DataSet ds = new DataSet("QuanLySinhVien");

// Tạo DataTable
DataTable dtSinhVien = new DataTable("SinhVien");

// Thêm cột
dtSinhVien.Columns.Add("MaSV", typeof(string));
dtSinhVien.Columns.Add("HoTen", typeof(string));
dtSinhVien.Columns.Add("NgaySinh", typeof(DateTime));
dtSinhVien.Columns.Add("DiemTB", typeof(double));

// Thiết lập Primary Key
dtSinhVien.PrimaryKey = new DataColumn[] { dtSinhVien.Columns["MaSV"] };

// Thêm dòng
DataRow row1 = dtSinhVien.NewRow();
row1["MaSV"] = "SV001";
row1["HoTen"] = "Nguyễn Văn A";
row1["NgaySinh"] = new DateTime(2000, 1, 1);
row1["DiemTB"] = 8.5;
dtSinhVien.Rows.Add(row1);

// Hoặc thêm trực tiếp
dtSinhVien.Rows.Add("SV002", "Trần Thị B", new DateTime(2000, 5, 15), 9.0);

// Thêm DataTable vào DataSet
ds.Tables.Add(dtSinhVien);
```

**Duyệt dữ liệu trong DataSet:**
```csharp
foreach (DataTable table in ds.Tables)
{
    Console.WriteLine($"Bảng: {table.TableName}");

    foreach (DataRow row in table.Rows)
    {
        foreach (DataColumn col in table.Columns)
        {
            Console.Write($"{row[col]}\t");
        }
        Console.WriteLine();
    }
}
```

### 2.6.2. DataAdapter

**DataAdapter là gì?**

**DataAdapter** là cầu nối giữa DataSet và Database. Nó có nhiệm vụ:
- Fill: Đổ dữ liệu từ database vào DataSet
- Update: Cập nhật thay đổi từ DataSet xuống database

**Các thành phần của DataAdapter:**
- **SelectCommand**: Truy vấn SELECT
- **InsertCommand**: Thêm dữ liệu
- **UpdateCommand**: Cập nhật dữ liệu
- **DeleteCommand**: Xóa dữ liệu

**Ví dụ cơ bản:**
```csharp
using (SqlConnection conn = new SqlConnection(connectionString))
{
    // Tạo DataAdapter với SelectCommand
    SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM SinhVien", conn);

    // Tạo DataSet
    DataSet ds = new DataSet();

    // Fill: Đổ dữ liệu vào DataSet
    adapter.Fill(ds, "SinhVien");

    // Làm việc với dữ liệu
    DataTable dt = ds.Tables["SinhVien"];
    foreach (DataRow row in dt.Rows)
    {
        Console.WriteLine(row["HoTen"]);
    }
}
```

**Ví dụ với các Command riêng biệt:**
```csharp
SqlConnection conn = new SqlConnection(connectionString);

// SelectCommand
string selectSQL = "SELECT * FROM SinhVien";
SqlDataAdapter adapter = new SqlDataAdapter(selectSQL, conn);

// InsertCommand
string insertSQL = "INSERT INTO SinhVien (MaSV, HoTen, NgaySinh) VALUES (@MaSV, @HoTen, @NgaySinh)";
adapter.InsertCommand = new SqlCommand(insertSQL, conn);
adapter.InsertCommand.Parameters.Add("@MaSV", SqlDbType.NVarChar, 10, "MaSV");
adapter.InsertCommand.Parameters.Add("@HoTen", SqlDbType.NVarChar, 100, "HoTen");
adapter.InsertCommand.Parameters.Add("@NgaySinh", SqlDbType.Date, 0, "NgaySinh");

// UpdateCommand
string updateSQL = "UPDATE SinhVien SET HoTen = @HoTen, NgaySinh = @NgaySinh WHERE MaSV = @MaSV";
adapter.UpdateCommand = new SqlCommand(updateSQL, conn);
adapter.UpdateCommand.Parameters.Add("@MaSV", SqlDbType.NVarChar, 10, "MaSV");
adapter.UpdateCommand.Parameters.Add("@HoTen", SqlDbType.NVarChar, 100, "HoTen");
adapter.UpdateCommand.Parameters.Add("@NgaySinh", SqlDbType.Date, 0, "NgaySinh");

// DeleteCommand
string deleteSQL = "DELETE FROM SinhVien WHERE MaSV = @MaSV";
adapter.DeleteCommand = new SqlCommand(deleteSQL, conn);
adapter.DeleteCommand.Parameters.Add("@MaSV", SqlDbType.NVarChar, 10, "MaSV");

// Fill DataSet
DataSet ds = new DataSet();
adapter.Fill(ds, "SinhVien");
```

### 2.6.3. DataTable

**DataTable là gì?**

**DataTable** đại diện cho một bảng dữ liệu trong bộ nhớ.

**Các thành phần:**
- **Columns**: Danh sách các cột (DataColumnCollection)
- **Rows**: Danh sách các dòng (DataRowCollection)
- **Constraints**: Các ràng buộc
- **PrimaryKey**: Khóa chính

**Ví dụ thao tác với DataTable:**
```csharp
DataTable dt = ds.Tables["SinhVien"];

// Thêm dòng
DataRow newRow = dt.NewRow();
newRow["MaSV"] = "SV003";
newRow["HoTen"] = "Lê Văn C";
newRow["NgaySinh"] = new DateTime(2001, 3, 10);
dt.Rows.Add(newRow);

// Sửa dòng
DataRow[] rows = dt.Select("MaSV = 'SV001'");
if (rows.Length > 0)
{
    rows[0]["HoTen"] = "Nguyễn Văn A - Updated";
}

// Xóa dòng
DataRow rowToDelete = dt.Rows.Find("SV002"); // Tìm theo primary key
if (rowToDelete != null)
{
    rowToDelete.Delete();
}

// Lọc dữ liệu
DataRow[] filteredRows = dt.Select("DiemTB >= 8.0");
foreach (DataRow row in filteredRows)
{
    Console.WriteLine(row["HoTen"]);
}

// Sắp xếp
DataRow[] sortedRows = dt.Select("", "DiemTB DESC");
```

### 2.6.4. Cập nhật thay đổi trở lại cơ sở dữ liệu

**Sử dụng DataAdapter.Update():**
```csharp
SqlConnection conn = new SqlConnection(connectionString);
SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM SinhVien", conn);

// Sử dụng CommandBuilder để tự động tạo InsertCommand, UpdateCommand, DeleteCommand
SqlCommandBuilder builder = new SqlCommandBuilder(adapter);

DataSet ds = new DataSet();
adapter.Fill(ds, "SinhVien");

DataTable dt = ds.Tables["SinhVien"];

// Thêm
DataRow newRow = dt.NewRow();
newRow["MaSV"] = "SV004";
newRow["HoTen"] = "Phạm Thị D";
newRow["NgaySinh"] = new DateTime(2000, 12, 25);
dt.Rows.Add(newRow);

// Sửa
dt.Rows[0]["HoTen"] = "Nguyễn Văn A - Modified";

// Xóa
dt.Rows[1].Delete();

// Cập nhật xuống database
int affectedRows = adapter.Update(ds, "SinhVien");
Console.WriteLine($"Đã cập nhật {affectedRows} dòng");
```

### 2.6.5. Lọc và sắp xếp trong DataSet

**Sử dụng DataTable.Select():**
```csharp
DataTable dt = ds.Tables["SinhVien"];

// Lọc đơn giản
DataRow[] rows1 = dt.Select("DiemTB >= 8.0");

// Lọc với nhiều điều kiện
DataRow[] rows2 = dt.Select("DiemTB >= 8.0 AND GioiTinh = 'Nam'");

// Lọc với LIKE
DataRow[] rows3 = dt.Select("HoTen LIKE 'Nguyễn%'");

// Lọc với IN
DataRow[] rows4 = dt.Select("MaLop IN ('CNTT01', 'CNTT02', 'CNTT03')");

// Lọc và sắp xếp
DataRow[] rows5 = dt.Select("DiemTB >= 7.0", "DiemTB DESC, HoTen ASC");

// In kết quả
foreach (DataRow row in rows5)
{
    Console.WriteLine($"{row["HoTen"]} - {row["DiemTB"]}");
}
```

**Sử dụng DataView:**
```csharp
DataTable dt = ds.Tables["SinhVien"];

// Tạo DataView
DataView dv = new DataView(dt);

// Thiết lập filter
dv.RowFilter = "DiemTB >= 8.0 AND GioiTinh = 'Nam'";

// Thiết lập sort
dv.Sort = "DiemTB DESC, HoTen ASC";

// Bind vào control
dataGridView1.DataSource = dv;

// Hoặc duyệt qua DataView
foreach (DataRowView rowView in dv)
{
    DataRow row = rowView.Row;
    Console.WriteLine(row["HoTen"]);
}
```

### 2.6.6. CommandBuilder

**SqlCommandBuilder** tự động tạo InsertCommand, UpdateCommand, DeleteCommand dựa trên SelectCommand.

**Ví dụ:**
```csharp
SqlConnection conn = new SqlConnection(connectionString);

// SelectCommand
SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM SinhVien", conn);

// CommandBuilder tự động tạo các command
SqlCommandBuilder builder = new SqlCommandBuilder(adapter);

// Có thể lấy command được tạo ra
string insertSQL = builder.GetInsertCommand().CommandText;
string updateSQL = builder.GetUpdateCommand().CommandText;
string deleteSQL = builder.GetDeleteCommand().CommandText;

Console.WriteLine($"Insert: {insertSQL}");
Console.WriteLine($"Update: {updateSQL}");
Console.WriteLine($"Delete: {deleteSQL}");

// Sử dụng như bình thường
DataSet ds = new DataSet();
adapter.Fill(ds, "SinhVien");

// Thay đổi dữ liệu...

// Update
adapter.Update(ds, "SinhVien");
```

**Lưu ý về CommandBuilder:**
- Chỉ hoạt động với bảng có Primary Key
- Không hiệu quả cho cập nhật nhiều dữ liệu
- Phù hợp cho prototype và ứng dụng đơn giản

---

## 2.7. DATA BINDING

### Data Binding là gì?

**Data Binding** là kỹ thuật liên kết dữ liệu với các control trên giao diện (UI). Khi dữ liệu thay đổi, UI tự động cập nhật và ngược lại.

### 2.7.1. Simple Data Binding (Liên kết đơn giản)

**Simple Binding** là liên kết một control với một giá trị duy nhất.

**Ví dụ: Bind TextBox với DataRow**
```csharp
// Lấy dữ liệu
DataTable dt = ds.Tables["SinhVien"];
DataRow row = dt.Rows[0];

// Bind các TextBox
txtMaSV.DataBindings.Add("Text", row, "MaSV");
txtHoTen.DataBindings.Add("Text", row, "HoTen");
dtpNgaySinh.DataBindings.Add("Value", row, "NgaySinh");
```

**Ví dụ: Bind với BindingSource**
```csharp
// Tạo BindingSource
BindingSource bindingSource = new BindingSource();
bindingSource.DataSource = ds.Tables["SinhVien"];

// Bind controls
txtMaSV.DataBindings.Add("Text", bindingSource, "MaSV");
txtHoTen.DataBindings.Add("Text", bindingSource, "HoTen");
txtEmail.DataBindings.Add("Text", bindingSource, "Email");
dtpNgaySinh.DataBindings.Add("Value", bindingSource, "NgaySinh");

// Navigation buttons
btnFirst.Click += (s, e) => bindingSource.MoveFirst();
btnPrevious.Click += (s, e) => bindingSource.MovePrevious();
btnNext.Click += (s, e) => bindingSource.MoveNext();
btnLast.Click += (s, e) => bindingSource.MoveLast();

// Hiển thị vị trí
lblPosition.DataBindings.Add("Text", bindingSource, "Position");
```

### 2.7.2. Complex Data Binding (Liên kết phức tạp)

**Complex Binding** là liên kết control với toàn bộ nguồn dữ liệu (nhiều dòng).

**Các control hỗ trợ Complex Binding:**
- ListBox
- ComboBox
- DataGridView
- CheckedListBox

**Ví dụ: Bind DataGridView**
```csharp
SqlConnection conn = new SqlConnection(connectionString);
SqlDataAdapter adapter = new SqlDataAdapter("SELECT * FROM SinhVien", conn);
DataSet ds = new DataSet();
adapter.Fill(ds, "SinhVien");

// Cách 1: Bind trực tiếp
dataGridView1.DataSource = ds.Tables["SinhVien"];

// Cách 2: Bind qua BindingSource (khuyến nghị)
BindingSource bindingSource = new BindingSource();
bindingSource.DataSource = ds.Tables["SinhVien"];
dataGridView1.DataSource = bindingSource;

// Tùy chỉnh columns
dataGridView1.Columns["MaSV"].HeaderText = "Mã SV";
dataGridView1.Columns["MaSV"].Width = 100;
dataGridView1.Columns["HoTen"].HeaderText = "Họ tên";
dataGridView1.Columns["HoTen"].Width = 200;

// Ẩn cột
if (dataGridView1.Columns.Contains("MatKhau"))
{
    dataGridView1.Columns["MatKhau"].Visible = false;
}
```

**Ví dụ: Bind ComboBox**
```csharp
// Lấy danh sách lớp
SqlDataAdapter adapter = new SqlDataAdapter("SELECT MaLop, TenLop FROM Lop", conn);
DataTable dtLop = new DataTable();
adapter.Fill(dtLop);

// Bind ComboBox
cboLop.DataSource = dtLop;
cboLop.DisplayMember = "TenLop";  // Hiển thị
cboLop.ValueMember = "MaLop";      // Giá trị

// Lấy giá trị đã chọn
string maLop = cboLop.SelectedValue.ToString();
string tenLop = cboLop.Text;
```

**Ví dụ: Bind ListBox**
```csharp
// Lấy danh sách môn học
SqlCommand cmd = new SqlCommand("SELECT MaMonHoc, TenMonHoc FROM MonHoc", conn);
SqlDataAdapter adapter = new SqlDataAdapter(cmd);
DataTable dt = new DataTable();
adapter.Fill(dt);

// Bind ListBox
listBox1.DataSource = dt;
listBox1.DisplayMember = "TenMonHoc";
listBox1.ValueMember = "MaMonHoc";

// Lấy giá trị đã chọn
if (listBox1.SelectedValue != null)
{
    string maMonHoc = listBox1.SelectedValue.ToString();
}
```

**Ví dụ: Master-Detail với 2 DataGridView**
```csharp
// Load dữ liệu
SqlConnection conn = new SqlConnection(connectionString);
DataSet ds = new DataSet();

// Lấy sinh viên
SqlDataAdapter adapterSV = new SqlDataAdapter("SELECT * FROM SinhVien", conn);
adapterSV.Fill(ds, "SinhVien");

// Lấy kết quả
SqlDataAdapter adapterKQ = new SqlDataAdapter("SELECT * FROM KetQua", conn);
adapterKQ.Fill(ds, "KetQua");

// Tạo quan hệ
DataRelation relation = new DataRelation("SinhVien_KetQua",
    ds.Tables["SinhVien"].Columns["MaSV"],
    ds.Tables["KetQua"].Columns["MaSV"]);
ds.Relations.Add(relation);

// Bind master (DataGridView 1)
BindingSource bsSinhVien = new BindingSource();
bsSinhVien.DataSource = ds;
bsSinhVien.DataMember = "SinhVien";
dgvSinhVien.DataSource = bsSinhVien;

// Bind detail (DataGridView 2)
BindingSource bsKetQua = new BindingSource();
bsKetQua.DataSource = bsSinhVien;
bsKetQua.DataMember = "SinhVien_KetQua"; // Tên relation
dgvKetQua.DataSource = bsKetQua;
```

---

## TÓM TẮT CHƯƠNG 2

### Các thành phần chính

| Thành phần | Mô tả | Khi nào dùng |
|-----------|-------|--------------|
| SqlConnection | Kết nối database | Luôn cần |
| SqlCommand | Thực thi câu lệnh | Luôn cần |
| SqlDataReader | Đọc dữ liệu forward-only | Đọc nhanh, không cache |
| DataSet | Cache dữ liệu offline | Binding, offline work |
| DataAdapter | Cầu nối DataSet-Database | Làm việc với DataSet |
| DataTable | Bảng trong bộ nhớ | Thao tác dữ liệu |
| BindingSource | Quản lý binding | Bind với UI |

### Best Practices

1. **Luôn đóng kết nối**: Dùng `using` statement
2. **Sử dụng Parameters**: Tránh SQL Injection
3. **Xử lý exception**: Bắt `SqlException`
4. **Connection pooling**: Tận dụng connection pool
5. **Chọn mô hình phù hợp**:
   - Connected: Đọc nhanh, không cache
   - Disconnected: Binding UI, offline
6. **Dispose objects**: DataReader, Command, Connection

---

## BÀI TẬP THỰC HÀNH

### Bài 1: CRUD cơ bản
Viết các phương thức:
1. Thêm sinh viên (ExecuteNonQuery)
2. Cập nhật thông tin sinh viên
3. Xóa sinh viên
4. Lấy danh sách sinh viên (DataReader)
5. Tìm sinh viên theo mã

### Bài 2: Sử dụng DataSet
1. Load dữ liệu vào DataSet
2. Thêm/Sửa/Xóa trong DataSet
3. Cập nhật xuống database
4. Lọc và sắp xếp dữ liệu

### Bài 3: Data Binding
1. Tạo form quản lý sinh viên
2. Bind dữ liệu vào DataGridView
3. Bind TextBox với BindingSource
4. Thực hiện navigation (First, Previous, Next, Last)
5. Thêm/Sửa/Xóa qua UI

### Bài 4: Master-Detail
1. Hiển thị danh sách lớp (master)
2. Hiển thị sinh viên của lớp được chọn (detail)
3. Sử dụng DataRelation

---

**Kết thúc Chương 2**
