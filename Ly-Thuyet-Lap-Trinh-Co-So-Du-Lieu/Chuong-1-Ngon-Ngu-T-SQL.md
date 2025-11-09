# CHƯƠNG 1: NGÔN NGỮ T-SQL

## Mục tiêu học tập
Sau khi học xong chương này, sinh viên có khả năng:
- Hiểu và sử dụng được các cấu trúc điều khiển trong T-SQL
- Viết được View, Function, Stored Procedure, Trigger
- Hiểu và áp dụng được khái niệm giao tác (Transaction)

---

## 1.1. GIỚI THIỆU T-SQL

### T-SQL là gì?
**T-SQL (Transact-SQL)** là phần mở rộng của SQL được Microsoft phát triển cho SQL Server. T-SQL bổ sung thêm:
- Các cấu trúc điều khiển (IF...ELSE, WHILE, CASE)
- Khai báo biến
- Xử lý lỗi
- Stored Procedures, Functions, Triggers

### Đặc điểm của T-SQL
- Ngôn ngữ lập trình thủ tục (procedural language)
- Tích hợp chặt chẽ với SQL Server
- Hỗ trợ xử lý logic nghiệp vụ phức tạp
- Tối ưu hiệu suất thực thi trên server

---

## 1.2. KHAI BÁO VÀ SỬ DỤNG BIẾN

### Khai báo biến
Cú pháp:
```sql
DECLARE @TenBien KieuDuLieu;
```

Ví dụ:
```sql
DECLARE @HoTen NVARCHAR(100);
DECLARE @Tuoi INT;
DECLARE @NgaySinh DATE;
DECLARE @Luong DECIMAL(18,2);
```

### Gán giá trị cho biến

**Cách 1: Sử dụng SET**
```sql
DECLARE @TenSV NVARCHAR(50);
SET @TenSV = N'Nguyễn Văn A';
```

**Cách 2: Sử dụng SELECT**
```sql
DECLARE @SoLuong INT;
SELECT @SoLuong = COUNT(*) FROM SinhVien;
```

**Cách 3: Gán khi khai báo (SQL Server 2008 trở lên)**
```sql
DECLARE @Pi FLOAT = 3.14159;
DECLARE @TenTruong NVARCHAR(100) = N'ĐH Mở TP.HCM';
```

### Ví dụ thực tế
```sql
-- Tính tổng lương của nhân viên theo phòng ban
DECLARE @MaPhongBan INT = 10;
DECLARE @TongLuong DECIMAL(18,2);

SELECT @TongLuong = SUM(Luong)
FROM NhanVien
WHERE MaPhongBan = @MaPhongBan;

PRINT N'Tổng lương phòng ban ' + CAST(@MaPhongBan AS NVARCHAR) + N': ' + CAST(@TongLuong AS NVARCHAR);
```

---

## 1.3. CẤU TRÚC ĐIỀU KHIỂN

### 1.3.1. IF...ELSE

**Cú pháp:**
```sql
IF <điều_kiện>
BEGIN
    -- Khối lệnh thực hiện khi điều kiện đúng
END
ELSE
BEGIN
    -- Khối lệnh thực hiện khi điều kiện sai
END
```

**Ví dụ 1: Kiểm tra điểm sinh viên**
```sql
DECLARE @Diem FLOAT = 8.5;
DECLARE @XepLoai NVARCHAR(20);

IF @Diem >= 9.0
    SET @XepLoai = N'Xuất sắc';
ELSE IF @Diem >= 8.0
    SET @XepLoai = N'Giỏi';
ELSE IF @Diem >= 6.5
    SET @XepLoai = N'Khá';
ELSE IF @Diem >= 5.0
    SET @XepLoai = N'Trung bình';
ELSE
    SET @XepLoai = N'Yếu';

PRINT N'Xếp loại: ' + @XepLoai;
```

**Ví dụ 2: Kiểm tra sự tồn tại**
```sql
DECLARE @MaSV NVARCHAR(10) = 'SV001';

IF EXISTS (SELECT 1 FROM SinhVien WHERE MaSV = @MaSV)
BEGIN
    PRINT N'Sinh viên tồn tại trong hệ thống';
    -- Thực hiện các thao tác khác
END
ELSE
BEGIN
    PRINT N'Sinh viên không tồn tại';
    -- Thêm sinh viên mới
END
```

### 1.3.2. WHILE

**Cú pháp:**
```sql
WHILE <điều_kiện>
BEGIN
    -- Khối lệnh lặp
    -- BREAK: Thoát khỏi vòng lặp
    -- CONTINUE: Bỏ qua lần lặp hiện tại
END
```

**Ví dụ 1: In số từ 1 đến 10**
```sql
DECLARE @i INT = 1;

WHILE @i <= 10
BEGIN
    PRINT N'Số: ' + CAST(@i AS NVARCHAR);
    SET @i = @i + 1;
END
```

**Ví dụ 2: Tính tổng các số từ 1 đến N**
```sql
DECLARE @N INT = 100;
DECLARE @i INT = 1;
DECLARE @Tong INT = 0;

WHILE @i <= @N
BEGIN
    SET @Tong = @Tong + @i;
    SET @i = @i + 1;
END

PRINT N'Tổng từ 1 đến ' + CAST(@N AS NVARCHAR) + N' = ' + CAST(@Tong AS NVARCHAR);
```

**Ví dụ 3: Sử dụng BREAK và CONTINUE**
```sql
DECLARE @Count INT = 0;

WHILE @Count < 20
BEGIN
    SET @Count = @Count + 1;

    -- Bỏ qua số chẵn
    IF @Count % 2 = 0
        CONTINUE;

    -- Dừng khi gặp số 15
    IF @Count = 15
        BREAK;

    PRINT @Count;
END
```

### 1.3.3. CASE

**Cú pháp 1: Simple CASE**
```sql
CASE <biểu_thức>
    WHEN <giá_trị_1> THEN <kết_quả_1>
    WHEN <giá_trị_2> THEN <kết_quả_2>
    ...
    ELSE <kết_quả_mặc_định>
END
```

**Cú pháp 2: Searched CASE**
```sql
CASE
    WHEN <điều_kiện_1> THEN <kết_quả_1>
    WHEN <điều_kiện_2> THEN <kết_quả_2>
    ...
    ELSE <kết_quả_mặc_định>
END
```

**Ví dụ 1: Simple CASE**
```sql
SELECT
    MaNV,
    HoTen,
    GioiTinh,
    CASE GioiTinh
        WHEN 'M' THEN N'Nam'
        WHEN 'F' THEN N'Nữ'
        ELSE N'Khác'
    END AS GioiTinhText
FROM NhanVien;
```

**Ví dụ 2: Searched CASE**
```sql
SELECT
    MaSV,
    HoTen,
    DiemTB,
    CASE
        WHEN DiemTB >= 9.0 THEN N'Xuất sắc'
        WHEN DiemTB >= 8.0 THEN N'Giỏi'
        WHEN DiemTB >= 6.5 THEN N'Khá'
        WHEN DiemTB >= 5.0 THEN N'Trung bình'
        ELSE N'Yếu'
    END AS XepLoai
FROM SinhVien;
```

**Ví dụ 3: CASE trong UPDATE**
```sql
-- Tăng lương theo thâm niên
UPDATE NhanVien
SET Luong = CASE
    WHEN DATEDIFF(YEAR, NgayVaoLam, GETDATE()) >= 10 THEN Luong * 1.2
    WHEN DATEDIFF(YEAR, NgayVaoLam, GETDATE()) >= 5 THEN Luong * 1.15
    WHEN DATEDIFF(YEAR, NgayVaoLam, GETDATE()) >= 2 THEN Luong * 1.1
    ELSE Luong * 1.05
END;
```

---

## 1.4. VIEW (Khung nhìn)

### View là gì?
**View** là một bảng ảo được tạo ra từ kết quả của câu truy vấn SELECT. View không lưu trữ dữ liệu mà chỉ lưu trữ câu lệnh truy vấn.

### Lợi ích của View
1. **Bảo mật**: Giới hạn quyền truy cập dữ liệu
2. **Đơn giản hóa**: Ẩn đi độ phức tạp của truy vấn
3. **Tái sử dụng**: Dùng lại câu truy vấn phức tạp
4. **Tính nhất quán**: Đảm bảo logic truy vấn thống nhất

### Tạo View

**Cú pháp:**
```sql
CREATE VIEW <tên_view>
AS
    <câu_lệnh_SELECT>
GO
```

**Ví dụ 1: View đơn giản**
```sql
-- View hiển thị thông tin sinh viên và lớp
CREATE VIEW vw_ThongTinSinhVien
AS
SELECT
    sv.MaSV,
    sv.HoTen,
    sv.NgaySinh,
    sv.GioiTinh,
    l.TenLop,
    l.Khoa
FROM SinhVien sv
INNER JOIN Lop l ON sv.MaLop = l.MaLop;
GO
```

**Ví dụ 2: View với tính toán**
```sql
-- View tính điểm trung bình và xếp loại
CREATE VIEW vw_DiemTrungBinhSinhVien
AS
SELECT
    sv.MaSV,
    sv.HoTen,
    AVG(kq.Diem) AS DiemTB,
    CASE
        WHEN AVG(kq.Diem) >= 9.0 THEN N'Xuất sắc'
        WHEN AVG(kq.Diem) >= 8.0 THEN N'Giỏi'
        WHEN AVG(kq.Diem) >= 6.5 THEN N'Khá'
        WHEN AVG(kq.Diem) >= 5.0 THEN N'Trung bình'
        ELSE N'Yếu'
    END AS XepLoai
FROM SinhVien sv
INNER JOIN KetQua kq ON sv.MaSV = kq.MaSV
GROUP BY sv.MaSV, sv.HoTen;
GO
```

### Sử dụng View
```sql
-- Truy vấn như bảng thông thường
SELECT * FROM vw_ThongTinSinhVien;

SELECT * FROM vw_ThongTinSinhVien
WHERE Khoa = N'Công nghệ thông tin';
```

### Sửa đổi View
```sql
ALTER VIEW vw_ThongTinSinhVien
AS
SELECT
    sv.MaSV,
    sv.HoTen,
    sv.NgaySinh,
    sv.GioiTinh,
    sv.Email, -- Thêm cột mới
    l.TenLop,
    l.Khoa
FROM SinhVien sv
INNER JOIN Lop l ON sv.MaLop = l.MaLop;
GO
```

### Xóa View
```sql
DROP VIEW vw_ThongTinSinhVien;
GO
```

---

## 1.5. STORED PROCEDURE (Thủ tục lưu trữ)

### Stored Procedure là gì?
**Stored Procedure** là một tập hợp các câu lệnh T-SQL được biên dịch trước và lưu trữ trên server. Stored Procedure có thể nhận tham số đầu vào và trả về kết quả.

### Lợi ích của Stored Procedure
1. **Hiệu suất cao**: Được biên dịch và tối ưu hóa sẵn
2. **Bảo mật**: Phân quyền thực thi, không cần quyền trực tiếp trên bảng
3. **Giảm network traffic**: Chỉ gửi tên procedure và tham số
4. **Dễ bảo trì**: Thay đổi logic không ảnh hưởng ứng dụng
5. **Tái sử dụng**: Gọi từ nhiều ứng dụng khác nhau

### Tạo Stored Procedure

**Cú pháp:**
```sql
CREATE PROCEDURE <tên_procedure>
    @<tham_số_1> <kiểu_dữ_liệu>,
    @<tham_số_2> <kiểu_dữ_liệu> = <giá_trị_mặc_định>,
    @<tham_số_output> <kiểu_dữ_liệu> OUTPUT
AS
BEGIN
    -- Các câu lệnh T-SQL
END
GO
```

**Ví dụ 1: Procedure đơn giản không tham số**
```sql
CREATE PROCEDURE sp_LayDanhSachSinhVien
AS
BEGIN
    SELECT MaSV, HoTen, NgaySinh, GioiTinh
    FROM SinhVien
    ORDER BY HoTen;
END
GO

-- Gọi procedure
EXEC sp_LayDanhSachSinhVien;
```

**Ví dụ 2: Procedure với tham số đầu vào**
```sql
CREATE PROCEDURE sp_TimSinhVienTheoLop
    @MaLop NVARCHAR(10)
AS
BEGIN
    SELECT MaSV, HoTen, NgaySinh, GioiTinh
    FROM SinhVien
    WHERE MaLop = @MaLop
    ORDER BY HoTen;
END
GO

-- Gọi procedure
EXEC sp_TimSinhVienTheoLop @MaLop = 'CNTT01';
EXEC sp_TimSinhVienTheoLop 'CNTT01'; -- Có thể bỏ tên tham số
```

**Ví dụ 3: Procedure với tham số mặc định**
```sql
CREATE PROCEDURE sp_LayDanhSachSinhVien_PhanTrang
    @PageNumber INT = 1,
    @PageSize INT = 10
AS
BEGIN
    SELECT MaSV, HoTen, NgaySinh, GioiTinh
    FROM SinhVien
    ORDER BY MaSV
    OFFSET (@PageNumber - 1) * @PageSize ROWS
    FETCH NEXT @PageSize ROWS ONLY;
END
GO

-- Gọi với giá trị mặc định
EXEC sp_LayDanhSachSinhVien_PhanTrang; -- Trang 1, 10 dòng
EXEC sp_LayDanhSachSinhVien_PhanTrang @PageNumber = 2; -- Trang 2, 10 dòng
EXEC sp_LayDanhSachSinhVien_PhanTrang @PageNumber = 1, @PageSize = 20; -- Trang 1, 20 dòng
```

**Ví dụ 4: Procedure với tham số OUTPUT**
```sql
CREATE PROCEDURE sp_ThemSinhVien
    @MaSV NVARCHAR(10),
    @HoTen NVARCHAR(100),
    @NgaySinh DATE,
    @GioiTinh NVARCHAR(3),
    @MaLop NVARCHAR(10),
    @KetQua NVARCHAR(200) OUTPUT
AS
BEGIN
    -- Kiểm tra mã sinh viên đã tồn tại chưa
    IF EXISTS (SELECT 1 FROM SinhVien WHERE MaSV = @MaSV)
    BEGIN
        SET @KetQua = N'Lỗi: Mã sinh viên đã tồn tại';
        RETURN -1;
    END

    -- Kiểm tra mã lớp có tồn tại không
    IF NOT EXISTS (SELECT 1 FROM Lop WHERE MaLop = @MaLop)
    BEGIN
        SET @KetQua = N'Lỗi: Mã lớp không tồn tại';
        RETURN -2;
    END

    -- Thêm sinh viên
    INSERT INTO SinhVien (MaSV, HoTen, NgaySinh, GioiTinh, MaLop)
    VALUES (@MaSV, @HoTen, @NgaySinh, @GioiTinh, @MaLop);

    SET @KetQua = N'Thêm sinh viên thành công';
    RETURN 0;
END
GO

-- Gọi procedure với OUTPUT
DECLARE @ThongBao NVARCHAR(200);
DECLARE @MaLoi INT;

EXEC @MaLoi = sp_ThemSinhVien
    @MaSV = 'SV001',
    @HoTen = N'Nguyễn Văn A',
    @NgaySinh = '2000-01-01',
    @GioiTinh = N'Nam',
    @MaLop = 'CNTT01',
    @KetQua = @ThongBao OUTPUT;

PRINT @ThongBao;
PRINT N'Mã lỗi: ' + CAST(@MaLoi AS NVARCHAR);
```

**Ví dụ 5: Procedure với xử lý lỗi**
```sql
CREATE PROCEDURE sp_CapNhatLuongNhanVien
    @MaNV INT,
    @LuongMoi DECIMAL(18,2)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        -- Kiểm tra nhân viên tồn tại
        IF NOT EXISTS (SELECT 1 FROM NhanVien WHERE MaNV = @MaNV)
        BEGIN
            RAISERROR(N'Nhân viên không tồn tại', 16, 1);
            RETURN;
        END

        -- Kiểm tra lương hợp lệ
        IF @LuongMoi <= 0
        BEGIN
            RAISERROR(N'Lương phải lớn hơn 0', 16, 1);
            RETURN;
        END

        -- Cập nhật lương
        UPDATE NhanVien
        SET Luong = @LuongMoi,
            NgayCapNhat = GETDATE()
        WHERE MaNV = @MaNV;

        COMMIT TRANSACTION;
        PRINT N'Cập nhật lương thành công';
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        PRINT N'Lỗi: ' + ERROR_MESSAGE();
    END CATCH
END
GO
```

### Sửa đổi Stored Procedure
```sql
ALTER PROCEDURE sp_LayDanhSachSinhVien
AS
BEGIN
    SELECT MaSV, HoTen, NgaySinh, GioiTinh, Email -- Thêm cột Email
    FROM SinhVien
    ORDER BY HoTen;
END
GO
```

### Xóa Stored Procedure
```sql
DROP PROCEDURE sp_LayDanhSachSinhVien;
GO
```

---

## 1.6. USER-DEFINED FUNCTION (Hàm do người dùng định nghĩa)

### Function là gì?
**Function** là một khối mã được thiết kế để thực hiện một tác vụ cụ thể và trả về một giá trị. Có 3 loại function trong SQL Server:
1. **Scalar Function**: Trả về một giá trị đơn
2. **Inline Table-Valued Function**: Trả về một bảng (kết quả của một câu SELECT)
3. **Multi-Statement Table-Valued Function**: Trả về một bảng (được xây dựng từ nhiều câu lệnh)

### 1.6.1. Scalar Function

**Cú pháp:**
```sql
CREATE FUNCTION <tên_function>
(
    @<tham_số_1> <kiểu_dữ_liệu>,
    @<tham_số_2> <kiểu_dữ_liệu>
)
RETURNS <kiểu_dữ_liệu_trả_về>
AS
BEGIN
    DECLARE @KetQua <kiểu_dữ_liệu_trả_về>;

    -- Logic xử lý

    RETURN @KetQua;
END
GO
```

**Ví dụ 1: Tính tuổi từ ngày sinh**
```sql
CREATE FUNCTION fn_TinhTuoi
(
    @NgaySinh DATE
)
RETURNS INT
AS
BEGIN
    DECLARE @Tuoi INT;
    SET @Tuoi = DATEDIFF(YEAR, @NgaySinh, GETDATE());
    RETURN @Tuoi;
END
GO

-- Sử dụng function
SELECT
    MaSV,
    HoTen,
    NgaySinh,
    dbo.fn_TinhTuoi(NgaySinh) AS Tuoi
FROM SinhVien;
```

**Ví dụ 2: Xếp loại học lực**
```sql
CREATE FUNCTION fn_XepLoaiHocLuc
(
    @DiemTB FLOAT
)
RETURNS NVARCHAR(20)
AS
BEGIN
    DECLARE @XepLoai NVARCHAR(20);

    IF @DiemTB >= 9.0
        SET @XepLoai = N'Xuất sắc';
    ELSE IF @DiemTB >= 8.0
        SET @XepLoai = N'Giỏi';
    ELSE IF @DiemTB >= 6.5
        SET @XepLoai = N'Khá';
    ELSE IF @DiemTB >= 5.0
        SET @XepLoai = N'Trung bình';
    ELSE
        SET @XepLoai = N'Yếu';

    RETURN @XepLoai;
END
GO

-- Sử dụng function
SELECT
    MaSV,
    HoTen,
    DiemTB,
    dbo.fn_XepLoaiHocLuc(DiemTB) AS XepLoai
FROM SinhVien;
```

**Ví dụ 3: Tính tổng tiền hóa đơn**
```sql
CREATE FUNCTION fn_TinhTongTienHoaDon
(
    @MaHD INT
)
RETURNS DECIMAL(18,2)
AS
BEGIN
    DECLARE @TongTien DECIMAL(18,2);

    SELECT @TongTien = SUM(SoLuong * DonGia)
    FROM ChiTietHoaDon
    WHERE MaHD = @MaHD;

    RETURN ISNULL(@TongTien, 0);
END
GO

-- Sử dụng function
SELECT
    MaHD,
    NgayLap,
    dbo.fn_TinhTongTienHoaDon(MaHD) AS TongTien
FROM HoaDon;
```

### 1.6.2. Inline Table-Valued Function

**Cú pháp:**
```sql
CREATE FUNCTION <tên_function>
(
    @<tham_số> <kiểu_dữ_liệu>
)
RETURNS TABLE
AS
RETURN
(
    <câu_lệnh_SELECT>
)
GO
```

**Ví dụ 1: Lấy danh sách sinh viên theo lớp**
```sql
CREATE FUNCTION fn_LaySinhVienTheoLop
(
    @MaLop NVARCHAR(10)
)
RETURNS TABLE
AS
RETURN
(
    SELECT MaSV, HoTen, NgaySinh, GioiTinh, Email
    FROM SinhVien
    WHERE MaLop = @MaLop
)
GO

-- Sử dụng function
SELECT * FROM dbo.fn_LaySinhVienTheoLop('CNTT01');

-- Kết hợp với WHERE
SELECT * FROM dbo.fn_LaySinhVienTheoLop('CNTT01')
WHERE GioiTinh = N'Nam';
```

**Ví dụ 2: Lấy sản phẩm theo khoảng giá**
```sql
CREATE FUNCTION fn_LaySanPhamTheoGia
(
    @GiaMin DECIMAL(18,2),
    @GiaMax DECIMAL(18,2)
)
RETURNS TABLE
AS
RETURN
(
    SELECT MaSP, TenSP, DonGia, SoLuongTon
    FROM SanPham
    WHERE DonGia BETWEEN @GiaMin AND @GiaMax
)
GO

-- Sử dụng function
SELECT * FROM dbo.fn_LaySanPhamTheoGia(100000, 500000);
```

### 1.6.3. Multi-Statement Table-Valued Function

**Cú pháp:**
```sql
CREATE FUNCTION <tên_function>
(
    @<tham_số> <kiểu_dữ_liệu>
)
RETURNS @<tên_biến_bảng> TABLE
(
    <cột_1> <kiểu_dữ_liệu>,
    <cột_2> <kiểu_dữ_liệu>
)
AS
BEGIN
    -- Các câu lệnh xử lý

    RETURN;
END
GO
```

**Ví dụ: Thống kê điểm của sinh viên**
```sql
CREATE FUNCTION fn_ThongKeDiemSinhVien
(
    @MaSV NVARCHAR(10)
)
RETURNS @KetQua TABLE
(
    TenMonHoc NVARCHAR(100),
    Diem FLOAT,
    XepLoai NVARCHAR(20),
    KetQua NVARCHAR(20)
)
AS
BEGIN
    INSERT INTO @KetQua
    SELECT
        mh.TenMonHoc,
        kq.Diem,
        CASE
            WHEN kq.Diem >= 9.0 THEN N'Xuất sắc'
            WHEN kq.Diem >= 8.0 THEN N'Giỏi'
            WHEN kq.Diem >= 6.5 THEN N'Khá'
            WHEN kq.Diem >= 5.0 THEN N'Trung bình'
            ELSE N'Yếu'
        END,
        CASE
            WHEN kq.Diem >= 5.0 THEN N'Đạt'
            ELSE N'Không đạt'
        END
    FROM KetQua kq
    INNER JOIN MonHoc mh ON kq.MaMonHoc = mh.MaMonHoc
    WHERE kq.MaSV = @MaSV;

    RETURN;
END
GO

-- Sử dụng function
SELECT * FROM dbo.fn_ThongKeDiemSinhVien('SV001');
```

### So sánh Function và Stored Procedure

| Đặc điểm | Function | Stored Procedure |
|----------|----------|------------------|
| Mục đích | Tính toán và trả về giá trị | Thực hiện logic nghiệp vụ |
| Trả về | Bắt buộc trả về giá trị | Không bắt buộc trả về |
| Gọi trong SELECT | Được | Không được |
| Thay đổi dữ liệu | Không được (DML) | Được |
| Transaction | Không quản lý | Quản lý được |
| OUTPUT parameter | Không | Có |

---

## 1.7. TRIGGER (Bẫy sự kiện)

### Trigger là gì?
**Trigger** là một stored procedure đặc biệt tự động thực thi khi có sự kiện INSERT, UPDATE hoặc DELETE xảy ra trên bảng.

### Phân loại Trigger

**1. DML Trigger** (Data Manipulation Language)
- AFTER Trigger (FOR Trigger): Thực thi sau khi thao tác hoàn thành
- INSTEAD OF Trigger: Thực thi thay vì thao tác gốc

**2. DDL Trigger** (Data Definition Language)
- Thực thi khi có thay đổi cấu trúc database (CREATE, ALTER, DROP)

### Bảng đặc biệt trong Trigger
- **inserted**: Chứa các dòng mới được INSERT hoặc UPDATE
- **deleted**: Chứa các dòng cũ bị DELETE hoặc UPDATE

### AFTER Trigger

**Cú pháp:**
```sql
CREATE TRIGGER <tên_trigger>
ON <tên_bảng>
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    -- Logic xử lý
END
GO
```

**Ví dụ 1: Trigger ghi log khi thêm sinh viên**
```sql
-- Tạo bảng log
CREATE TABLE LogSinhVien
(
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    MaSV NVARCHAR(10),
    HanhDong NVARCHAR(50),
    NgayThucHien DATETIME,
    NguoiThucHien NVARCHAR(100)
);
GO

-- Tạo trigger
CREATE TRIGGER trg_LogThemSinhVien
ON SinhVien
AFTER INSERT
AS
BEGIN
    INSERT INTO LogSinhVien (MaSV, HanhDong, NgayThucHien, NguoiThucHien)
    SELECT
        MaSV,
        N'Thêm sinh viên',
        GETDATE(),
        SUSER_SNAME()
    FROM inserted;
END
GO
```

**Ví dụ 2: Trigger cập nhật tồn kho khi bán hàng**
```sql
CREATE TRIGGER trg_CapNhatTonKho
ON ChiTietHoaDon
AFTER INSERT
AS
BEGIN
    UPDATE sp
    SET sp.SoLuongTon = sp.SoLuongTon - i.SoLuong
    FROM SanPham sp
    INNER JOIN inserted i ON sp.MaSP = i.MaSP;

    -- Kiểm tra tồn kho âm
    IF EXISTS (SELECT 1 FROM SanPham WHERE SoLuongTon < 0)
    BEGIN
        RAISERROR(N'Lỗi: Không đủ hàng trong kho', 16, 1);
        ROLLBACK TRANSACTION;
    END
END
GO
```

**Ví dụ 3: Trigger ngăn xóa dữ liệu quan trọng**
```sql
CREATE TRIGGER trg_Ngăn_Xoa_SinhVien
ON SinhVien
AFTER DELETE
AS
BEGIN
    -- Kiểm tra nếu sinh viên có điểm
    IF EXISTS (
        SELECT 1
        FROM deleted d
        INNER JOIN KetQua kq ON d.MaSV = kq.MaSV
    )
    BEGIN
        RAISERROR(N'Không thể xóa sinh viên đã có điểm', 16, 1);
        ROLLBACK TRANSACTION;
    END
END
GO
```

**Ví dụ 4: Trigger kiểm tra ràng buộc nghiệp vụ**
```sql
CREATE TRIGGER trg_KiemTraLuong
ON NhanVien
AFTER INSERT, UPDATE
AS
BEGIN
    DECLARE @LuongMin DECIMAL(18,2) = 4000000; -- Lương tối thiểu

    IF EXISTS (SELECT 1 FROM inserted WHERE Luong < @LuongMin)
    BEGIN
        RAISERROR(N'Lương phải lớn hơn hoặc bằng 4.000.000 VNĐ', 16, 1);
        ROLLBACK TRANSACTION;
    END

    -- Kiểm tra lương trưởng phòng phải cao hơn nhân viên
    IF EXISTS (
        SELECT 1
        FROM inserted i
        INNER JOIN NhanVien nv ON i.MaPhongBan = nv.MaPhongBan
        WHERE i.ChucVu = N'Trưởng phòng'
            AND nv.ChucVu = N'Nhân viên'
            AND i.Luong <= nv.Luong
    )
    BEGIN
        RAISERROR(N'Lương trưởng phòng phải cao hơn nhân viên', 16, 1);
        ROLLBACK TRANSACTION;
    END
END
GO
```

### INSTEAD OF Trigger

**Ví dụ: Trigger cho View**
```sql
-- Tạo view
CREATE VIEW vw_SinhVien_Lop
AS
SELECT
    sv.MaSV,
    sv.HoTen,
    sv.NgaySinh,
    l.TenLop,
    l.Khoa
FROM SinhVien sv
INNER JOIN Lop l ON sv.MaLop = l.MaLop;
GO

-- Tạo INSTEAD OF trigger để INSERT vào view
CREATE TRIGGER trg_InsertView_SinhVien_Lop
ON vw_SinhVien_Lop
INSTEAD OF INSERT
AS
BEGIN
    INSERT INTO SinhVien (MaSV, HoTen, NgaySinh, MaLop)
    SELECT
        i.MaSV,
        i.HoTen,
        i.NgaySinh,
        l.MaLop
    FROM inserted i
    INNER JOIN Lop l ON i.TenLop = l.TenLop;
END
GO
```

### Quản lý Trigger

**Vô hiệu hóa Trigger:**
```sql
DISABLE TRIGGER trg_LogThemSinhVien ON SinhVien;
```

**Kích hoạt lại Trigger:**
```sql
ENABLE TRIGGER trg_LogThemSinhVien ON SinhVien;
```

**Xóa Trigger:**
```sql
DROP TRIGGER trg_LogThemSinhVien;
```

**Xem danh sách Trigger:**
```sql
SELECT * FROM sys.triggers;

-- Xem trigger của bảng cụ thể
SELECT * FROM sys.triggers
WHERE parent_id = OBJECT_ID('SinhVien');
```

---

## 1.8. GIAO TÁC (Transaction)

### Transaction là gì?
**Transaction** là một đơn vị công việc logic bao gồm một hoặc nhiều câu lệnh SQL. Transaction đảm bảo tính toàn vẹn dữ liệu theo nguyên tắc **ACID**.

### Nguyên tắc ACID

1. **Atomicity (Tính nguyên tử)**:
   - Tất cả thao tác trong transaction đều thành công hoặc tất cả đều thất bại
   - Không tồn tại trạng thái trung gian

2. **Consistency (Tính nhất quán)**:
   - Dữ liệu phải ở trạng thái hợp lệ trước và sau transaction
   - Không vi phạm ràng buộc toàn vẹn

3. **Isolation (Tính độc lập)**:
   - Các transaction đồng thời không ảnh hưởng lẫn nhau
   - Kết quả giống như chạy tuần tự

4. **Durability (Tính bền vững)**:
   - Sau khi commit, thay đổi được lưu vĩnh viễn
   - Không mất dữ liệu khi có sự cố

### Các lệnh quản lý Transaction

**1. BEGIN TRANSACTION**: Bắt đầu transaction
**2. COMMIT TRANSACTION**: Xác nhận và lưu thay đổi
**3. ROLLBACK TRANSACTION**: Hủy bỏ toàn bộ thay đổi
**4. SAVE TRANSACTION**: Tạo điểm lưu trong transaction

### Cú pháp cơ bản

```sql
BEGIN TRANSACTION;

    -- Các câu lệnh SQL

    IF <điều_kiện_lỗi>
        ROLLBACK TRANSACTION;
    ELSE
        COMMIT TRANSACTION;
```

### Ví dụ 1: Chuyển tiền giữa 2 tài khoản

```sql
BEGIN TRANSACTION;

BEGIN TRY
    DECLARE @SoTienChuyen DECIMAL(18,2) = 1000000;
    DECLARE @TaiKhoanGui NVARCHAR(20) = 'TK001';
    DECLARE @TaiKhoanNhan NVARCHAR(20) = 'TK002';

    -- Kiểm tra số dư tài khoản gửi
    DECLARE @SoDu DECIMAL(18,2);
    SELECT @SoDu = SoDu FROM TaiKhoan WHERE SoTaiKhoan = @TaiKhoanGui;

    IF @SoDu < @SoTienChuyen
    BEGIN
        RAISERROR(N'Số dư không đủ để thực hiện giao dịch', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END

    -- Trừ tiền tài khoản gửi
    UPDATE TaiKhoan
    SET SoDu = SoDu - @SoTienChuyen
    WHERE SoTaiKhoan = @TaiKhoanGui;

    -- Cộng tiền tài khoản nhận
    UPDATE TaiKhoan
    SET SoDu = SoDu + @SoTienChuyen
    WHERE SoTaiKhoan = @TaiKhoanNhan;

    -- Ghi log giao dịch
    INSERT INTO LichSuGiaoDich (TaiKhoanGui, TaiKhoanNhan, SoTien, NgayGiaoDich)
    VALUES (@TaiKhoanGui, @TaiKhoanNhan, @SoTienChuyen, GETDATE());

    COMMIT TRANSACTION;
    PRINT N'Chuyển tiền thành công';
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;

    PRINT N'Lỗi: ' + ERROR_MESSAGE();
END CATCH
```

### Ví dụ 2: Đặt hàng và cập nhật tồn kho

```sql
CREATE PROCEDURE sp_DatHang
    @MaKH INT,
    @DanhSachSanPham NVARCHAR(MAX) -- JSON: [{"MaSP": 1, "SoLuong": 5}, ...]
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRANSACTION;

    BEGIN TRY
        -- Tạo hóa đơn
        DECLARE @MaHD INT;
        INSERT INTO HoaDon (MaKH, NgayLap, TongTien)
        VALUES (@MaKH, GETDATE(), 0);

        SET @MaHD = SCOPE_IDENTITY();

        -- Parse JSON và thêm chi tiết hóa đơn
        DECLARE @TongTien DECIMAL(18,2) = 0;

        -- Duyệt qua từng sản phẩm
        DECLARE @MaSP INT, @SoLuong INT, @DonGia DECIMAL(18,2), @ThanhTien DECIMAL(18,2);

        -- (Giả sử đã parse JSON thành bảng tạm #TempSanPham)

        DECLARE cur CURSOR FOR
        SELECT MaSP, SoLuong FROM #TempSanPham;

        OPEN cur;
        FETCH NEXT FROM cur INTO @MaSP, @SoLuong;

        WHILE @@FETCH_STATUS = 0
        BEGIN
            -- Kiểm tra tồn kho
            DECLARE @TonKho INT;
            SELECT @TonKho = SoLuongTon, @DonGia = DonGia
            FROM SanPham
            WHERE MaSP = @MaSP;

            IF @TonKho < @SoLuong
            BEGIN
                RAISERROR(N'Sản phẩm không đủ hàng trong kho', 16, 1);
                CLOSE cur;
                DEALLOCATE cur;
                ROLLBACK TRANSACTION;
                RETURN;
            END

            -- Thêm chi tiết hóa đơn
            SET @ThanhTien = @SoLuong * @DonGia;
            INSERT INTO ChiTietHoaDon (MaHD, MaSP, SoLuong, DonGia, ThanhTien)
            VALUES (@MaHD, @MaSP, @SoLuong, @DonGia, @ThanhTien);

            -- Cập nhật tồn kho
            UPDATE SanPham
            SET SoLuongTon = SoLuongTon - @SoLuong
            WHERE MaSP = @MaSP;

            SET @TongTien = @TongTien + @ThanhTien;

            FETCH NEXT FROM cur INTO @MaSP, @SoLuong;
        END

        CLOSE cur;
        DEALLOCATE cur;

        -- Cập nhật tổng tiền hóa đơn
        UPDATE HoaDon
        SET TongTien = @TongTien
        WHERE MaHD = @MaHD;

        COMMIT TRANSACTION;
        PRINT N'Đặt hàng thành công. Mã hóa đơn: ' + CAST(@MaHD AS NVARCHAR);
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
        DECLARE @ErrorState INT = ERROR_STATE();

        RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
    END CATCH
END
GO
```

### Ví dụ 3: Sử dụng SAVE TRANSACTION

```sql
BEGIN TRANSACTION;

BEGIN TRY
    -- Bước 1: Thêm khách hàng
    INSERT INTO KhachHang (HoTen, Email, SDT)
    VALUES (N'Nguyễn Văn A', 'a@email.com', '0123456789');

    SAVE TRANSACTION SavePoint1;

    -- Bước 2: Thêm địa chỉ
    INSERT INTO DiaChi (MaKH, DiaChi, QuanHuyen, ThanhPho)
    VALUES (SCOPE_IDENTITY(), N'123 Đường ABC', N'Quận 1', N'TP.HCM');

    SAVE TRANSACTION SavePoint2;

    -- Bước 3: Thêm đơn hàng (giả sử có lỗi)
    BEGIN TRY
        INSERT INTO DonHang (MaKH, NgayDat, TongTien)
        VALUES (SCOPE_IDENTITY(), GETDATE(), -1000); -- Giá trị không hợp lệ
    END TRY
    BEGIN CATCH
        PRINT N'Lỗi khi thêm đơn hàng, rollback về SavePoint2';
        ROLLBACK TRANSACTION SavePoint2;
        -- Tiếp tục với dữ liệu khách hàng và địa chỉ
    END CATCH

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;

    PRINT N'Lỗi: ' + ERROR_MESSAGE();
END CATCH
```

### Mức độ cô lập (Isolation Level)

SQL Server hỗ trợ 4 mức độ cô lập:

**1. READ UNCOMMITTED**: Mức thấp nhất, có thể đọc dữ liệu chưa commit (Dirty Read)
**2. READ COMMITTED**: Mặc định, chỉ đọc dữ liệu đã commit
**3. REPEATABLE READ**: Đảm bảo đọc lại cùng dữ liệu trong transaction
**4. SERIALIZABLE**: Mức cao nhất, transaction chạy tuần tự

```sql
-- Thiết lập isolation level
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

BEGIN TRANSACTION;
    -- Các câu lệnh
COMMIT TRANSACTION;
```

### Best Practices cho Transaction

1. **Giữ transaction ngắn gọn**: Tránh transaction chạy quá lâu
2. **Xử lý lỗi đầy đủ**: Luôn dùng TRY...CATCH
3. **Kiểm tra @@TRANCOUNT**: Đảm bảo rollback đúng
4. **Tránh tương tác người dùng**: Không chờ input trong transaction
5. **Sử dụng NOCOUNT**: Tắt thông báo số dòng để tăng hiệu suất

---

## TÓM TẮT CHƯƠNG 1

### Những điểm cần nhớ:

1. **T-SQL** là ngôn ngữ lập trình thủ tục mở rộng của SQL
2. **View**: Bảng ảo để đơn giản hóa truy vấn và bảo mật
3. **Stored Procedure**: Tối ưu hiệu suất, dễ bảo trì, tái sử dụng cao
4. **Function**:
   - Scalar: Trả về 1 giá trị
   - Table-Valued: Trả về bảng
5. **Trigger**: Tự động thực thi khi có sự kiện INSERT/UPDATE/DELETE
6. **Transaction**: Đảm bảo tính toàn vẹn dữ liệu theo ACID

### Khi nào dùng gì?

| Tình huống | Sử dụng |
|------------|---------|
| Đơn giản hóa truy vấn phức tạp | View |
| Logic nghiệp vụ, thay đổi dữ liệu | Stored Procedure |
| Tính toán trong SELECT | Scalar Function |
| Trả về tập dữ liệu tùy chỉnh | Table-Valued Function |
| Tự động xử lý khi thay đổi dữ liệu | Trigger |
| Đảm bảo tính toàn vẹn nhiều thao tác | Transaction |

---

## BÀI TẬP THỰC HÀNH

### Bài 1: Quản lý sinh viên
1. Tạo View hiển thị sinh viên kèm điểm trung bình và xếp loại
2. Viết Stored Procedure thêm/sửa/xóa sinh viên
3. Viết Function tính điểm trung bình của sinh viên
4. Tạo Trigger ghi log khi thay đổi thông tin sinh viên

### Bài 2: Quản lý bán hàng
1. Tạo Stored Procedure đặt hàng (sử dụng Transaction)
2. Viết Trigger tự động cập nhật tồn kho khi bán hàng
3. Viết Function tính tổng tiền hóa đơn
4. Tạo View thống kê doanh thu theo tháng

### Bài 3: Quản lý ngân hàng
1. Viết Stored Procedure chuyển tiền giữa 2 tài khoản
2. Tạo Trigger kiểm tra số dư không âm
3. Viết Function tính lãi suất
4. Sử dụng Transaction để đảm bảo tính toàn vẹn

---

**Kết thúc Chương 1**
