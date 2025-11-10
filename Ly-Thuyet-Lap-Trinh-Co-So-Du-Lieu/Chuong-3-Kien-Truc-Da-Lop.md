# CHƯƠNG 3: KIẾN TRÚC ĐA LỚP

## Mục tiêu học tập
Sau khi học xong chương này, sinh viên có khả năng:
- Hiểu khái niệm và lợi ích của kiến trúc đa lớp
- Phân biệt kiến trúc đa lớp (Multi-layer) và đa tầng (Multi-tier)
- Thiết kế và xây dựng ứng dụng theo mô hình 3 lớp
- Hiểu và áp dụng ASP.NET Core MVC

---

## 3.1. TỔNG QUAN KIẾN TRÚC ĐA LỚP

### Kiến trúc đa lớp là gì?

**Kiến trúc đa lớp (Multi-layer/Multi-tier Architecture)** là mô hình tổ chức mã nguồn thành các lớp logic riêng biệt, mỗi lớp có trách nhiệm cụ thể.

### Lợi ích của kiến trúc đa lớp

1. **Tách biệt mối quan tâm** (Separation of Concerns)
   - Mỗi lớp có trách nhiệm riêng
   - Dễ hiểu và bảo trì

2. **Tái sử dụng** (Reusability)
   - Logic nghiệp vụ có thể dùng lại
   - Giảm duplicate code

3. **Dễ bảo trì** (Maintainability)
   - Thay đổi một lớp không ảnh hưởng lớp khác
   - Dễ tìm và sửa lỗi

4. **Dễ kiểm thử** (Testability)
   - Có thể test riêng từng lớp
   - Unit testing dễ dàng

5. **Mở rộng** (Scalability)
   - Dễ thêm tính năng mới
   - Có thể scale theo chiều ngang

6. **Làm việc nhóm** (Team Collaboration)
   - Nhiều người có thể làm việc song song
   - Chia công việc rõ ràng

### Các mô hình kiến trúc phổ biến

#### 1. Kiến trúc 2 lớp (2-Tier)
```
┌───────────────┐      ┌───────────┐
│  Presentation │ ←──→ │  Database │
│   + Business  │      └───────────┘
└───────────────┘
```

**Ưu điểm:**
- Đơn giản, dễ triển khai
- Phù hợp ứng dụng nhỏ

**Nhược điểm:**
- Khó bảo trì khi lớn
- Logic nghiệp vụ lẫn với UI
- Khó tái sử dụng

#### 2. Kiến trúc 3 lớp (3-Tier)
```
┌───────────────┐
│  Presentation │ (UI Layer)
│    Layer      │
└───────┬───────┘
        ↓
┌───────────────┐
│   Business    │ (BLL - Business Logic Layer)
│     Layer     │
└───────┬───────┘
        ↓
┌───────────────┐
│  Data Access  │ (DAL - Data Access Layer)
│     Layer     │
└───────┬───────┘
        ↓
┌───────────────┐
│   Database    │
└───────────────┘
```

**Các lớp:**
- **Presentation Layer (UI)**: Giao diện người dùng
- **Business Logic Layer (BLL)**: Logic nghiệp vụ
- **Data Access Layer (DAL)**: Truy xuất dữ liệu

**Ưu điểm:**
- Tách biệt rõ ràng
- Dễ bảo trì và mở rộng
- Tái sử dụng tốt
- Phù hợp đa số ứng dụng

#### 3. Kiến trúc N-lớp (N-Tier)
```
┌───────────────┐
│  Presentation │
└───────┬───────┘
        ↓
┌───────────────┐
│   Business    │
│     Logic     │
└───────┬───────┘
        ↓
┌───────────────┐
│   Service     │
│     Layer     │
└───────┬───────┘
        ↓
┌───────────────┐
│  Data Access  │
└───────┬───────┘
        ↓
┌───────────────┐
│   Database    │
└───────────────┘
```

---

## 3.2. KIẾN TRÚC ĐA TẦNG

### Phân biệt Multi-layer và Multi-tier

| Đặc điểm | Multi-layer | Multi-tier |
|----------|-------------|------------|
| Khái niệm | Tổ chức logic code | Phân tách vật lý |
| Deployment | Cùng server | Khác server |
| Ví dụ | 3 project trong 1 solution | UI server, API server, DB server |
| Mục đích | Tổ chức code | Phân tải, bảo mật |

### Ví dụ Multi-tier

**2-Tier Physical:**
```
┌──────────────────┐         ┌──────────────────┐
│   Client         │ ←────→  │  Database Server │
│   (UI + BLL)     │         └──────────────────┘
└──────────────────┘
```

**3-Tier Physical:**
```
┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│  Client/Web   │ ←──→ │  Application  │ ←──→ │    Database   │
│  (UI Layer)   │      │  Server (BLL) │      │    Server     │
└───────────────┘      └───────────────┘      └───────────────┘
```

---

## 3.3. THIẾT KẾ ỨNG DỤNG 3 LỚP

### Cấu trúc tổng quan

```
Solution: QuanLySinhVien
│
├── QuanLySinhVien.GUI          (Presentation Layer)
│   ├── Forms
│   ├── UserControls
│   └── Program.cs
│
├── QuanLySinhVien.BLL          (Business Logic Layer)
│   ├── SinhVienBLL.cs
│   ├── MonHocBLL.cs
│   └── KetQuaBLL.cs
│
├── QuanLySinhVien.DAL          (Data Access Layer)
│   ├── SinhVienDAL.cs
│   ├── MonHocDAL.cs
│   ├── KetQuaDAL.cs
│   └── DatabaseHelper.cs
│
└── QuanLySinhVien.DTO          (Data Transfer Object)
    ├── SinhVienDTO.cs
    ├── MonHocDTO.cs
    └── KetQuaDTO.cs
```

### 3.3.1. Lớp DTO (Data Transfer Object)

**DTO** là đối tượng truyền dữ liệu giữa các lớp, chỉ chứa properties, không có logic.

**Ví dụ: SinhVienDTO.cs**
```csharp
using System;

namespace QuanLySinhVien.DTO
{
    public class SinhVienDTO
    {
        public string MaSV { get; set; }
        public string HoTen { get; set; }
        public DateTime NgaySinh { get; set; }
        public string GioiTinh { get; set; }
        public string Email { get; set; }
        public string SoDienThoai { get; set; }
        public string DiaChi { get; set; }
        public string MaLop { get; set; }

        // Constructor mặc định
        public SinhVienDTO()
        {
        }

        // Constructor với tham số
        public SinhVienDTO(string maSV, string hoTen, DateTime ngaySinh)
        {
            MaSV = maSV;
            HoTen = hoTen;
            NgaySinh = ngaySinh;
        }

        // Tính tuổi
        public int TinhTuoi()
        {
            return DateTime.Now.Year - NgaySinh.Year;
        }

        // Override ToString
        public override string ToString()
        {
            return $"{MaSV} - {HoTen}";
        }
    }
}
```

**Ví dụ: MonHocDTO.cs**
```csharp
namespace QuanLySinhVien.DTO
{
    public class MonHocDTO
    {
        public string MaMonHoc { get; set; }
        public string TenMonHoc { get; set; }
        public int SoTinChi { get; set; }
        public int SoTietLyThuyet { get; set; }
        public int SoTietThucHanh { get; set; }

        public MonHocDTO()
        {
        }

        public MonHocDTO(string maMH, string tenMH, int soTC)
        {
            MaMonHoc = maMH;
            TenMonHoc = tenMH;
            SoTinChi = soTC;
        }
    }
}
```

**Ví dụ: KetQuaDTO.cs**
```csharp
namespace QuanLySinhVien.DTO
{
    public class KetQuaDTO
    {
        public string MaSV { get; set; }
        public string MaMonHoc { get; set; }
        public float DiemGiuaKy { get; set; }
        public float DiemCuoiKy { get; set; }
        public float DiemTongKet { get; set; }

        // Tính điểm tổng kết
        public void TinhDiemTongKet()
        {
            DiemTongKet = DiemGiuaKy * 0.4f + DiemCuoiKy * 0.6f;
        }

        // Xếp loại
        public string XepLoai()
        {
            if (DiemTongKet >= 9.0) return "Xuất sắc";
            if (DiemTongKet >= 8.0) return "Giỏi";
            if (DiemTongKet >= 6.5) return "Khá";
            if (DiemTongKet >= 5.0) return "Trung bình";
            return "Yếu";
        }
    }
}
```

### 3.3.2. Lớp DAL (Data Access Layer)

**DAL** chịu trách nhiệm truy xuất dữ liệu từ database.

**DatabaseHelper.cs** - Lớp hỗ trợ kết nối
```csharp
using System;
using System.Data;
using System.Data.SqlClient;

namespace QuanLySinhVien.DAL
{
    public class DatabaseHelper
    {
        private static string connectionString =
            "Data Source=.;Initial Catalog=QLSV;Integrated Security=True;";

        // Thực thi câu lệnh SELECT trả về DataTable
        public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
        {
            DataTable dt = new DataTable();

            using (SqlConnection conn = new SqlConnection(connectionString))
            {
                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    if (parameters != null)
                    {
                        cmd.Parameters.AddRange(parameters);
                    }

                    using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
                    {
                        adapter.Fill(dt);
                    }
                }
            }

            return dt;
        }

        // Thực thi câu lệnh INSERT, UPDATE, DELETE
        public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
        {
            int rowsAffected = 0;

            using (SqlConnection conn = new SqlConnection(connectionString))
            {
                conn.Open();

                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    if (parameters != null)
                    {
                        cmd.Parameters.AddRange(parameters);
                    }

                    rowsAffected = cmd.ExecuteNonQuery();
                }
            }

            return rowsAffected;
        }

        // Thực thi câu lệnh trả về giá trị đơn
        public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
        {
            object result = null;

            using (SqlConnection conn = new SqlConnection(connectionString))
            {
                conn.Open();

                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    if (parameters != null)
                    {
                        cmd.Parameters.AddRange(parameters);
                    }

                    result = cmd.ExecuteScalar();
                }
            }

            return result;
        }
    }
}
```

**SinhVienDAL.cs**
```csharp
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using QuanLySinhVien.DTO;

namespace QuanLySinhVien.DAL
{
    public class SinhVienDAL
    {
        // Lấy tất cả sinh viên
        public List<SinhVienDTO> LayDanhSachSinhVien()
        {
            List<SinhVienDTO> list = new List<SinhVienDTO>();
            string query = "SELECT * FROM SinhVien ORDER BY HoTen";

            DataTable dt = DatabaseHelper.ExecuteQuery(query);

            foreach (DataRow row in dt.Rows)
            {
                SinhVienDTO sv = new SinhVienDTO
                {
                    MaSV = row["MaSV"].ToString(),
                    HoTen = row["HoTen"].ToString(),
                    NgaySinh = Convert.ToDateTime(row["NgaySinh"]),
                    GioiTinh = row["GioiTinh"].ToString(),
                    Email = row["Email"] == DBNull.Value ? null : row["Email"].ToString(),
                    SoDienThoai = row["SoDienThoai"] == DBNull.Value ? null : row["SoDienThoai"].ToString(),
                    DiaChi = row["DiaChi"] == DBNull.Value ? null : row["DiaChi"].ToString(),
                    MaLop = row["MaLop"].ToString()
                };

                list.Add(sv);
            }

            return list;
        }

        // Tìm sinh viên theo mã
        public SinhVienDTO TimSinhVienTheoMa(string maSV)
        {
            string query = "SELECT * FROM SinhVien WHERE MaSV = @MaSV";
            SqlParameter[] parameters = {
                new SqlParameter("@MaSV", maSV)
            };

            DataTable dt = DatabaseHelper.ExecuteQuery(query, parameters);

            if (dt.Rows.Count > 0)
            {
                DataRow row = dt.Rows[0];
                return new SinhVienDTO
                {
                    MaSV = row["MaSV"].ToString(),
                    HoTen = row["HoTen"].ToString(),
                    NgaySinh = Convert.ToDateTime(row["NgaySinh"]),
                    GioiTinh = row["GioiTinh"].ToString(),
                    Email = row["Email"] == DBNull.Value ? null : row["Email"].ToString(),
                    SoDienThoai = row["SoDienThoai"] == DBNull.Value ? null : row["SoDienThoai"].ToString(),
                    DiaChi = row["DiaChi"] == DBNull.Value ? null : row["DiaChi"].ToString(),
                    MaLop = row["MaLop"].ToString()
                };
            }

            return null;
        }

        // Thêm sinh viên
        public bool ThemSinhVien(SinhVienDTO sv)
        {
            string query = @"INSERT INTO SinhVien (MaSV, HoTen, NgaySinh, GioiTinh, Email, SoDienThoai, DiaChi, MaLop)
                           VALUES (@MaSV, @HoTen, @NgaySinh, @GioiTinh, @Email, @SoDienThoai, @DiaChi, @MaLop)";

            SqlParameter[] parameters = {
                new SqlParameter("@MaSV", sv.MaSV),
                new SqlParameter("@HoTen", sv.HoTen),
                new SqlParameter("@NgaySinh", sv.NgaySinh),
                new SqlParameter("@GioiTinh", sv.GioiTinh),
                new SqlParameter("@Email", (object)sv.Email ?? DBNull.Value),
                new SqlParameter("@SoDienThoai", (object)sv.SoDienThoai ?? DBNull.Value),
                new SqlParameter("@DiaChi", (object)sv.DiaChi ?? DBNull.Value),
                new SqlParameter("@MaLop", sv.MaLop)
            };

            return DatabaseHelper.ExecuteNonQuery(query, parameters) > 0;
        }

        // Cập nhật sinh viên
        public bool CapNhatSinhVien(SinhVienDTO sv)
        {
            string query = @"UPDATE SinhVien
                           SET HoTen = @HoTen, NgaySinh = @NgaySinh, GioiTinh = @GioiTinh,
                               Email = @Email, SoDienThoai = @SoDienThoai, DiaChi = @DiaChi, MaLop = @MaLop
                           WHERE MaSV = @MaSV";

            SqlParameter[] parameters = {
                new SqlParameter("@MaSV", sv.MaSV),
                new SqlParameter("@HoTen", sv.HoTen),
                new SqlParameter("@NgaySinh", sv.NgaySinh),
                new SqlParameter("@GioiTinh", sv.GioiTinh),
                new SqlParameter("@Email", (object)sv.Email ?? DBNull.Value),
                new SqlParameter("@SoDienThoai", (object)sv.SoDienThoai ?? DBNull.Value),
                new SqlParameter("@DiaChi", (object)sv.DiaChi ?? DBNull.Value),
                new SqlParameter("@MaLop", sv.MaLop)
            };

            return DatabaseHelper.ExecuteNonQuery(query, parameters) > 0;
        }

        // Xóa sinh viên
        public bool XoaSinhVien(string maSV)
        {
            string query = "DELETE FROM SinhVien WHERE MaSV = @MaSV";
            SqlParameter[] parameters = {
                new SqlParameter("@MaSV", maSV)
            };

            return DatabaseHelper.ExecuteNonQuery(query, parameters) > 0;
        }

        // Tìm kiếm sinh viên
        public List<SinhVienDTO> TimKiemSinhVien(string keyword)
        {
            List<SinhVienDTO> list = new List<SinhVienDTO>();
            string query = @"SELECT * FROM SinhVien
                           WHERE MaSV LIKE @Keyword OR HoTen LIKE @Keyword
                           ORDER BY HoTen";

            SqlParameter[] parameters = {
                new SqlParameter("@Keyword", "%" + keyword + "%")
            };

            DataTable dt = DatabaseHelper.ExecuteQuery(query, parameters);

            foreach (DataRow row in dt.Rows)
            {
                SinhVienDTO sv = new SinhVienDTO
                {
                    MaSV = row["MaSV"].ToString(),
                    HoTen = row["HoTen"].ToString(),
                    NgaySinh = Convert.ToDateTime(row["NgaySinh"]),
                    GioiTinh = row["GioiTinh"].ToString(),
                    Email = row["Email"] == DBNull.Value ? null : row["Email"].ToString(),
                    MaLop = row["MaLop"].ToString()
                };

                list.Add(sv);
            }

            return list;
        }

        // Kiểm tra tồn tại
        public bool KiemTraTonTai(string maSV)
        {
            string query = "SELECT COUNT(*) FROM SinhVien WHERE MaSV = @MaSV";
            SqlParameter[] parameters = {
                new SqlParameter("@MaSV", maSV)
            };

            int count = Convert.ToInt32(DatabaseHelper.ExecuteScalar(query, parameters));
            return count > 0;
        }
    }
}
```

### 3.3.3. Lớp BLL (Business Logic Layer)

**BLL** chứa logic nghiệp vụ, validate dữ liệu, gọi DAL.

**SinhVienBLL.cs**
```csharp
using System;
using System.Collections.Generic;
using QuanLySinhVien.DAL;
using QuanLySinhVien.DTO;

namespace QuanLySinhVien.BLL
{
    public class SinhVienBLL
    {
        private SinhVienDAL dal = new SinhVienDAL();

        // Lấy danh sách sinh viên
        public List<SinhVienDTO> LayDanhSachSinhVien()
        {
            return dal.LayDanhSachSinhVien();
        }

        // Tìm sinh viên theo mã
        public SinhVienDTO TimSinhVienTheoMa(string maSV)
        {
            if (string.IsNullOrWhiteSpace(maSV))
            {
                throw new ArgumentException("Mã sinh viên không được rỗng");
            }

            return dal.TimSinhVienTheoMa(maSV);
        }

        // Thêm sinh viên
        public bool ThemSinhVien(SinhVienDTO sv)
        {
            // Validate
            if (string.IsNullOrWhiteSpace(sv.MaSV))
                throw new ArgumentException("Mã sinh viên không được rỗng");

            if (string.IsNullOrWhiteSpace(sv.HoTen))
                throw new ArgumentException("Họ tên không được rỗng");

            if (sv.NgaySinh > DateTime.Now)
                throw new ArgumentException("Ngày sinh không hợp lệ");

            if (sv.NgaySinh.Year < 1900)
                throw new ArgumentException("Năm sinh phải lớn hơn 1900");

            // Validate email
            if (!string.IsNullOrEmpty(sv.Email))
            {
                if (!sv.Email.Contains("@"))
                    throw new ArgumentException("Email không hợp lệ");
            }

            // Kiểm tra trùng mã
            if (dal.KiemTraTonTai(sv.MaSV))
            {
                throw new InvalidOperationException("Mã sinh viên đã tồn tại");
            }

            // Thêm vào database
            return dal.ThemSinhVien(sv);
        }

        // Cập nhật sinh viên
        public bool CapNhatSinhVien(SinhVienDTO sv)
        {
            // Validate
            if (string.IsNullOrWhiteSpace(sv.MaSV))
                throw new ArgumentException("Mã sinh viên không được rỗng");

            if (string.IsNullOrWhiteSpace(sv.HoTen))
                throw new ArgumentException("Họ tên không được rỗng");

            if (sv.NgaySinh > DateTime.Now)
                throw new ArgumentException("Ngày sinh không hợp lệ");

            // Validate email
            if (!string.IsNullOrEmpty(sv.Email))
            {
                if (!sv.Email.Contains("@"))
                    throw new ArgumentException("Email không hợp lệ");
            }

            // Kiểm tra tồn tại
            if (!dal.KiemTraTonTai(sv.MaSV))
            {
                throw new InvalidOperationException("Sinh viên không tồn tại");
            }

            // Cập nhật
            return dal.CapNhatSinhVien(sv);
        }

        // Xóa sinh viên
        public bool XoaSinhVien(string maSV)
        {
            if (string.IsNullOrWhiteSpace(maSV))
                throw new ArgumentException("Mã sinh viên không được rỗng");

            // Kiểm tra tồn tại
            if (!dal.KiemTraTonTai(maSV))
            {
                throw new InvalidOperationException("Sinh viên không tồn tại");
            }

            // TODO: Kiểm tra ràng buộc (sinh viên có điểm thì không xóa)

            return dal.XoaSinhVien(maSV);
        }

        // Tìm kiếm
        public List<SinhVienDTO> TimKiemSinhVien(string keyword)
        {
            if (string.IsNullOrWhiteSpace(keyword))
            {
                return LayDanhSachSinhVien();
            }

            return dal.TimKiemSinhVien(keyword.Trim());
        }

        // Validate email
        private bool ValidateEmail(string email)
        {
            if (string.IsNullOrWhiteSpace(email))
                return true; // Email không bắt buộc

            // Regex hoặc check đơn giản
            return email.Contains("@") && email.Contains(".");
        }
    }
}
```

### 3.3.4. Lớp GUI (Presentation Layer)

**frmQuanLySinhVien.cs**
```csharp
using System;
using System.Windows.Forms;
using QuanLySinhVien.BLL;
using QuanLySinhVien.DTO;

namespace QuanLySinhVien.GUI
{
    public partial class frmQuanLySinhVien : Form
    {
        private SinhVienBLL bll = new SinhVienBLL();

        public frmQuanLySinhVien()
        {
            InitializeComponent();
        }

        private void frmQuanLySinhVien_Load(object sender, EventArgs e)
        {
            LoadDanhSach();
        }

        private void LoadDanhSach()
        {
            try
            {
                var list = bll.LayDanhSachSinhVien();
                dgvSinhVien.DataSource = list;

                // Tùy chỉnh columns
                if (dgvSinhVien.Columns.Count > 0)
                {
                    dgvSinhVien.Columns["MaSV"].HeaderText = "Mã SV";
                    dgvSinhVien.Columns["HoTen"].HeaderText = "Họ tên";
                    dgvSinhVien.Columns["NgaySinh"].HeaderText = "Ngày sinh";
                    dgvSinhVien.Columns["GioiTinh"].HeaderText = "Giới tính";
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi: " + ex.Message, "Lỗi",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnThem_Click(object sender, EventArgs e)
        {
            try
            {
                // Tạo DTO từ UI
                SinhVienDTO sv = new SinhVienDTO
                {
                    MaSV = txtMaSV.Text.Trim(),
                    HoTen = txtHoTen.Text.Trim(),
                    NgaySinh = dtpNgaySinh.Value,
                    GioiTinh = rdoNam.Checked ? "Nam" : "Nữ",
                    Email = txtEmail.Text.Trim(),
                    SoDienThoai = txtSDT.Text.Trim(),
                    DiaChi = txtDiaChi.Text.Trim(),
                    MaLop = cboLop.SelectedValue.ToString()
                };

                // Gọi BLL
                bool result = bll.ThemSinhVien(sv);

                if (result)
                {
                    MessageBox.Show("Thêm sinh viên thành công!", "Thông báo",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);

                    LoadDanhSach();
                    ClearInputs();
                }
                else
                {
                    MessageBox.Show("Thêm sinh viên thất bại!", "Lỗi",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (ArgumentException ex)
            {
                MessageBox.Show(ex.Message, "Lỗi nhập liệu",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi: " + ex.Message, "Lỗi",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnSua_Click(object sender, EventArgs e)
        {
            try
            {
                SinhVienDTO sv = new SinhVienDTO
                {
                    MaSV = txtMaSV.Text.Trim(),
                    HoTen = txtHoTen.Text.Trim(),
                    NgaySinh = dtpNgaySinh.Value,
                    GioiTinh = rdoNam.Checked ? "Nam" : "Nữ",
                    Email = txtEmail.Text.Trim(),
                    SoDienThoai = txtSDT.Text.Trim(),
                    DiaChi = txtDiaChi.Text.Trim(),
                    MaLop = cboLop.SelectedValue.ToString()
                };

                bool result = bll.CapNhatSinhVien(sv);

                if (result)
                {
                    MessageBox.Show("Cập nhật thành công!", "Thông báo",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);

                    LoadDanhSach();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi: " + ex.Message, "Lỗi",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnXoa_Click(object sender, EventArgs e)
        {
            try
            {
                string maSV = txtMaSV.Text.Trim();

                DialogResult confirm = MessageBox.Show(
                    "Bạn có chắc muốn xóa sinh viên này?",
                    "Xác nhận",
                    MessageBoxButtons.YesNo,
                    MessageBoxIcon.Question);

                if (confirm == DialogResult.Yes)
                {
                    bool result = bll.XoaSinhVien(maSV);

                    if (result)
                    {
                        MessageBox.Show("Xóa thành công!", "Thông báo",
                            MessageBoxButtons.OK, MessageBoxIcon.Information);

                        LoadDanhSach();
                        ClearInputs();
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi: " + ex.Message, "Lỗi",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnTimKiem_Click(object sender, EventArgs e)
        {
            try
            {
                string keyword = txtTimKiem.Text.Trim();
                var list = bll.TimKiemSinhVien(keyword);
                dgvSinhVien.DataSource = list;

                lblKetQua.Text = $"Tìm thấy {list.Count} kết quả";
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi: " + ex.Message, "Lỗi",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void dgvSinhVien_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow row = dgvSinhVien.Rows[e.RowIndex];

                txtMaSV.Text = row.Cells["MaSV"].Value.ToString();
                txtHoTen.Text = row.Cells["HoTen"].Value.ToString();
                dtpNgaySinh.Value = Convert.ToDateTime(row.Cells["NgaySinh"].Value);

                string gioiTinh = row.Cells["GioiTinh"].Value.ToString();
                if (gioiTinh == "Nam")
                    rdoNam.Checked = true;
                else
                    rdoNu.Checked = true;

                txtEmail.Text = row.Cells["Email"].Value?.ToString() ?? "";
                txtSDT.Text = row.Cells["SoDienThoai"].Value?.ToString() ?? "";
                txtDiaChi.Text = row.Cells["DiaChi"].Value?.ToString() ?? "";
            }
        }

        private void ClearInputs()
        {
            txtMaSV.Clear();
            txtHoTen.Clear();
            txtEmail.Clear();
            txtSDT.Clear();
            txtDiaChi.Clear();
            dtpNgaySinh.Value = DateTime.Now;
            rdoNam.Checked = true;
            txtMaSV.Focus();
        }
    }
}
```

---

## 3.4. ASP.NET CORE MVC

### Giới thiệu ASP.NET Core MVC

**MVC (Model-View-Controller)** là một design pattern để xây dựng ứng dụng web.

```
          ┌─────────────┐
          │   Browser   │
          └──────┬──────┘
                 │ Request
                 ↓
          ┌─────────────┐
          │ Controller  │ ← Xử lý request
          └──────┬──────┘
                 │
      ┌──────────┼──────────┐
      ↓          ↓           ↓
┌──────────┐ ┌────────┐ ┌────────┐
│  Model   │ │  View  │ │  Data  │
│ (Logic)  │ │  (UI)  │ │  (DB)  │
└──────────┘ └────────┘ └────────┘
```

**Các thành phần:**
- **Model**: Dữ liệu và logic nghiệp vụ
- **View**: Giao diện hiển thị
- **Controller**: Điều khiển luồng xử lý

### Cấu trúc project ASP.NET Core MVC

```
QuanLySinhVien.Web
├── Controllers         (Controller)
│   ├── HomeController.cs
│   └── SinhVienController.cs
│
├── Models             (Model)
│   ├── SinhVienViewModel.cs
│   └── ErrorViewModel.cs
│
├── Views              (View)
│   ├── Home
│   │   └── Index.cshtml
│   ├── SinhVien
│   │   ├── Index.cshtml
│   │   ├── Create.cshtml
│   │   ├── Edit.cshtml
│   │   └── Delete.cshtml
│   └── Shared
│       └── _Layout.cshtml
│
├── wwwroot            (Static files)
│   ├── css
│   ├── js
│   └── images
│
├── appsettings.json   (Configuration)
└── Program.cs         (Entry point)
```

### Ví dụ Controller

**SinhVienController.cs**
```csharp
using Microsoft.AspNetCore.Mvc;
using QuanLySinhVien.BLL;
using QuanLySinhVien.DTO;

namespace QuanLySinhVien.Web.Controllers
{
    public class SinhVienController : Controller
    {
        private readonly SinhVienBLL _bll;

        public SinhVienController()
        {
            _bll = new SinhVienBLL();
        }

        // GET: SinhVien
        public IActionResult Index()
        {
            var list = _bll.LayDanhSachSinhVien();
            return View(list);
        }

        // GET: SinhVien/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: SinhVien/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create(SinhVienDTO sinhVien)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    _bll.ThemSinhVien(sinhVien);
                    TempData["SuccessMessage"] = "Thêm sinh viên thành công!";
                    return RedirectToAction(nameof(Index));
                }
                catch (Exception ex)
                {
                    ModelState.AddModelError("", ex.Message);
                }
            }

            return View(sinhVien);
        }

        // GET: SinhVien/Edit/5
        public IActionResult Edit(string id)
        {
            var sinhVien = _bll.TimSinhVienTheoMa(id);

            if (sinhVien == null)
            {
                return NotFound();
            }

            return View(sinhVien);
        }

        // POST: SinhVien/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(string id, SinhVienDTO sinhVien)
        {
            if (id != sinhVien.MaSV)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _bll.CapNhatSinhVien(sinhVien);
                    TempData["SuccessMessage"] = "Cập nhật thành công!";
                    return RedirectToAction(nameof(Index));
                }
                catch (Exception ex)
                {
                    ModelState.AddModelError("", ex.Message);
                }
            }

            return View(sinhVien);
        }

        // GET: SinhVien/Delete/5
        public IActionResult Delete(string id)
        {
            var sinhVien = _bll.TimSinhVienTheoMa(id);

            if (sinhVien == null)
            {
                return NotFound();
            }

            return View(sinhVien);
        }

        // POST: SinhVien/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public IActionResult DeleteConfirmed(string id)
        {
            try
            {
                _bll.XoaSinhVien(id);
                TempData["SuccessMessage"] = "Xóa thành công!";
            }
            catch (Exception ex)
            {
                TempData["ErrorMessage"] = ex.Message;
            }

            return RedirectToAction(nameof(Index));
        }
    }
}
```

### Ví dụ View (Razor)

**Index.cshtml**
```cshtml
@model List<QuanLySinhVien.DTO.SinhVienDTO>

@{
    ViewData["Title"] = "Danh sách sinh viên";
}

<h2>@ViewData["Title"]</h2>

<p>
    <a asp-action="Create" class="btn btn-primary">Thêm sinh viên</a>
</p>

@if (TempData["SuccessMessage"] != null)
{
    <div class="alert alert-success">@TempData["SuccessMessage"]</div>
}

<table class="table table-striped">
    <thead>
        <tr>
            <th>Mã SV</th>
            <th>Họ tên</th>
            <th>Ngày sinh</th>
            <th>Giới tính</th>
            <th>Email</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        @foreach (var item in Model)
        {
            <tr>
                <td>@item.MaSV</td>
                <td>@item.HoTen</td>
                <td>@item.NgaySinh.ToString("dd/MM/yyyy")</td>
                <td>@item.GioiTinh</td>
                <td>@item.Email</td>
                <td>
                    <a asp-action="Edit" asp-route-id="@item.MaSV" class="btn btn-sm btn-warning">Sửa</a>
                    <a asp-action="Delete" asp-route-id="@item.MaSV" class="btn btn-sm btn-danger">Xóa</a>
                </td>
            </tr>
        }
    </tbody>
</table>
```

**Create.cshtml**
```cshtml
@model QuanLySinhVien.DTO.SinhVienDTO

@{
    ViewData["Title"] = "Thêm sinh viên";
}

<h2>@ViewData["Title"]</h2>

<form asp-action="Create" method="post">
    <div asp-validation-summary="ModelOnly" class="text-danger"></div>

    <div class="form-group">
        <label asp-for="MaSV"></label>
        <input asp-for="MaSV" class="form-control" />
        <span asp-validation-for="MaSV" class="text-danger"></span>
    </div>

    <div class="form-group">
        <label asp-for="HoTen"></label>
        <input asp-for="HoTen" class="form-control" />
        <span asp-validation-for="HoTen" class="text-danger"></span>
    </div>

    <div class="form-group">
        <label asp-for="NgaySinh"></label>
        <input asp-for="NgaySinh" class="form-control" type="date" />
        <span asp-validation-for="NgaySinh" class="text-danger"></span>
    </div>

    <div class="form-group">
        <label asp-for="GioiTinh"></label>
        <select asp-for="GioiTinh" class="form-control">
            <option value="Nam">Nam</option>
            <option value="Nữ">Nữ</option>
        </select>
    </div>

    <div class="form-group">
        <label asp-for="Email"></label>
        <input asp-for="Email" class="form-control" type="email" />
        <span asp-validation-for="Email" class="text-danger"></span>
    </div>

    <div class="form-group">
        <button type="submit" class="btn btn-primary">Lưu</button>
        <a asp-action="Index" class="btn btn-secondary">Quay lại</a>
    </div>
</form>

@section Scripts {
    @{await Html.RenderPartialAsync("_ValidationScriptsPartial");}
}
```

---

## TÓM TẮT CHƯƠNG 3

### Lợi ích kiến trúc 3 lớp
1. Tách biệt rõ ràng trách nhiệm
2. Dễ bảo trì và mở rộng
3. Tái sử dụng code
4. Dễ test
5. Làm việc nhóm hiệu quả

### Nguyên tắc
- DTO: Chỉ chứa dữ liệu, không có logic
- DAL: Chỉ truy xuất dữ liệu
- BLL: Chứa logic nghiệp vụ và validate
- GUI: Chỉ hiển thị và thu thập input

### Luồng dữ liệu
```
User → GUI → BLL → DAL → Database
          ↓     ↓     ↓
        Validate  Query  Data
```

---

**Kết thúc Chương 3**
