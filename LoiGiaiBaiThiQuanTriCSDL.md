# LỜI GIẢI ĐỀ THI THỰC HÀNH QUẢN TRỊ HỆ CƠ SỞ DỮ LIỆU

**Môn**: Quản trị Hệ Cơ sở Dữ liệu
**Học kỳ**: 1 - Năm học 2023-2024
**Thời gian làm bài**: 90 phút

---

## CÂU 1: TẠO ALIAS SERVER

### Yêu cầu:
Tạo một Alias Server tên **HoTenSVLamBai** (họ tên không dấu sinh viên làm bài này) ánh xạ đến server thật là bản Named Instance có tên instance là **MISASME2021** trên máy tính làm bài. Test Alias Server bằng cách đăng nhập thành công vào Alias Server bằng sa, sau đó chụp màn hình có thấy danh sách các CSDL trong Alias Server.

### Cách thực hiện:

**Bước 1: Tạo Alias Server**
1. Mở **SQL Server Configuration Manager**
2. Chọn **SQL Native Client Configuration** (hoặc phiên bản tương ứng)
3. Click chuột phải vào **Aliases** → Chọn **New Alias**
4. Nhập thông tin:
   - **Alias Name**: `HoTenSVLamBai` (ví dụ: NguyenVanAnh)
   - **Port No**: Để trống (sử dụng dynamic port)
   - **Protocol**: TCP/IP
   - **Server**: `TenMaySV\MISASME2021` (ví dụ: 638\MISASME2021)
5. Click **OK** để lưu

**Bước 2: Test Alias Server**
1. Mở **SQL Server Management Studio (SSMS)**
2. Trong cửa sổ Connect to Server:
   - **Server type**: Database Engine
   - **Server name**: `HoTenSVLamBai` (tên alias vừa tạo)
   - **Authentication**: SQL Server Authentication
   - **Login**: `sa`
   - **Password**: nhập password của sa
3. Click **Connect**
4. Sau khi đăng nhập thành công, Object Explorer sẽ hiển thị:
   - Tên server là tên alias
   - Danh sách các database: master, model, msdb, tempdb, và các database khác

### Kết quả mong đợi:
- Đăng nhập thành công vào Alias Server
- Object Explorer hiển thị tên server là tên alias đã tạo
- Có thể thấy danh sách các CSDL: System Databases và User Databases

---

## CÂU 2: TẠO SYNONYM

### Yêu cầu:
Tạo một đối tượng ảo là synonym có đường dẫn và tên là `[Northwind].[dbo].[TaiLieu]` trỏ tới đối tượng thật là bảng dữ liệu có đường dẫn và tên là `[AdventureWorks].[Production].[Document]`. Chỉ chụp 2 hình: hình thiết kế synonym và hình test synonym.

### Cách thực hiện:

**Bước 1: Tạo Synonym bằng T-SQL**
```sql
USE [Northwind]
GO

CREATE SYNONYM [dbo].[TaiLieu]
FOR [AdventureWorks].[Production].[Document]
GO
```

**Bước 2: Kiểm tra Properties của Synonym**
1. Trong SSMS, mở rộng database **Northwind**
2. Mở rộng **Synonyms**
3. Click chuột phải vào **dbo.TaiLieu** → chọn **Properties**
4. Trong cửa sổ Properties, xác nhận:
   - **Synonym name**: dbo.TaiLieu
   - **Synonym base object**: [AdventureWorks].[Production].[Document]

**Bước 3: Test Synonym**

**Test 1 - Sử dụng bảng thật:**
```sql
-- Query từ bảng thật
SELECT TOP (1000) *
FROM [AdventureWorks].[Production].[Document]
```

**Test 2 - Sử dụng synonym:**
```sql
-- Query từ synonym
SELECT TOP (1000) *
FROM [Northwind].[dbo].[TaiLieu]
```

### Kết quả mong đợi:
- Cả hai câu query đều trả về kết quả giống hệt nhau
- Properties của synonym hiển thị đúng tên synonym và base object
- Có thể sử dụng synonym như một bảng thông thường

---

## CÂU 3: SỬ DỤNG CÔNG CỤ SQLCMD

### Câu 3a: Đăng nhập vào Named Instance bằng Windows Authentication

### Yêu cầu:
Viết lệnh đăng nhập vào SQL Server có tên Instance là **MISASME2021**, dùng windows login trên máy tính làm bài.

### Cách thực hiện:

**Bước 1: Mở Command Prompt (CMD)**
- Nhấn Windows + R, gõ `cmd`, Enter

**Bước 2: Chạy lệnh SQLCMD**
```cmd
sqlcmd -S TenMaySV\MISASME2021 -E
```

Trong đó:
- `-S`: chỉ định server name (TenMaySV\MISASME2021)
- `-E`: sử dụng Windows Authentication (Trusted Connection)

**Kết quả:**
- Dấu nhắc lệnh thay đổi thành `1>`
- Có thể bắt đầu nhập câu lệnh T-SQL

---

### Câu 3b: Đăng nhập vào Default Instance và query dữ liệu

### Yêu cầu:
Viết lệnh đăng nhập vào SQL Server Default Instance bằng login sa và xem dữ liệu của bảng `[Northwind].[dbo].[Customers]`, chỉ select 5 hàng, 4 cột: [CustomerID], [CompanyName], [ContactName], [ContactTitle].

### Cách thực hiện:

**Bước 1: Đăng nhập vào Default Instance**
```cmd
sqlcmd -S TenMaySV -U sa -P MatKhauSa
```

Hoặc nếu server là localhost:
```cmd
sqlcmd -S . -U sa -P MatKhauSa
```

Trong đó:
- `-S`: chỉ định server name (. hoặc localhost hoặc tên máy)
- `-U`: username (sa)
- `-P`: password của sa

**Bước 2: Query dữ liệu**
```sql
1> USE Northwind
2> GO
1> SELECT TOP 5 [CustomerID], [CompanyName], [ContactName], [ContactTitle]
2> FROM [dbo].[Customers]
3> GO
```

### Kết quả mong đợi:
- Hiển thị 5 dòng dữ liệu với 4 cột được chỉ định
- Dữ liệu được format dạng text trong console

**Ví dụ kết quả:**
```
CustomerID  CompanyName              ContactName      ContactTitle
----------- ------------------------ ---------------- ------------------
ALFKI       Alfreds Futterkiste      Maria Anders     Sales Representative
ANATR       Ana Trujillo             Ana Trujillo     Owner
ANTON       Antonio Moreno           Antonio Moreno   Owner
...
```

---

## CÂU 4: SAO LƯU CSDL FULL

### Yêu cầu:
1. Tạo CSDL **QLSinhVien** với recovery model là FULL
2. Tạo table **SinhVien** với 3 cột: MaSV (PK, int, Identity), HoSV (nvarchar(50)), TenSV (nvarchar(20))
3. Nhập 1 dòng dữ liệu: (Lê Thành, Tâm)
4. Sao lưu FULL database vào file `D:\QTHCSDL\SaoLuu\QLSinhVien.bak`

### Cách thực hiện:

**Bước 1: Tạo database QLSinhVien**
```sql
-- Tạo database với Recovery Model là FULL
CREATE DATABASE QLSinhVien
GO

-- Đặt Recovery Model là FULL
ALTER DATABASE QLSinhVien SET RECOVERY FULL
GO
```

**Bước 2: Tạo table SinhVien**
```sql
USE QLSinhVien
GO

CREATE TABLE SinhVien
(
    MaSV INT PRIMARY KEY IDENTITY(1,1),
    HoSV NVARCHAR(50),
    TenSV NVARCHAR(20)
)
GO
```

**Bước 3: Nhập dữ liệu**
```sql
INSERT INTO SinhVien (HoSV, TenSV)
VALUES (N'Lê Thành', N'Tâm')
GO

-- Xem dữ liệu
SELECT * FROM SinhVien
```

**Kết quả:**
```
MaSV    HoSV        TenSV
1       Lê Thành    Tâm
```

**Bước 4: Tạo thư mục để lưu file backup**
```sql
-- Tạo thư mục (chạy trong CMD hoặc PowerShell)
-- mkdir D:\QTHCSDL\SaoLuu
```

**Bước 5: Sao lưu FULL database**
```sql
BACKUP DATABASE QLSinhVien
TO DISK = N'D:\QTHCSDL\SaoLuu\QLSinhVien.bak'
WITH FORMAT, INIT, NAME = N'QLSinhVien-Full Database Backup',
SKIP, NOREWIND, NOUNLOAD, STATS = 10
GO
```

Giải thích tham số:
- `FORMAT`: Tạo header mới cho backup media
- `INIT`: Ghi đè file backup cũ (nếu có)
- `NAME`: Tên mô tả cho backup set
- `SKIP`: Bỏ qua kiểm tra expiration
- `STATS = 10`: Hiển thị progress mỗi 10%

### Kết quả mong đợi:
- Thông báo: "Processed X pages for database 'QLSinhVien', file 'QLSinhVien' on file 1."
- Thông báo: "BACKUP DATABASE successfully processed..."
- File `QLSinhVien.bak` được tạo với dung lượng khoảng 3-4 MB

---

## CÂU 5: SAO LƯU CSDL DIFFERENTIAL

### Yêu cầu:
1. Nhập thêm 1 dòng dữ liệu: (Nguyễn Văn, Sáng)
2. Sao lưu DIFFERENTIAL vào file `D:\QTHCSDL\SaoLuu\QLSinhVien.bak`

### Cách thực hiện:

**Bước 1: Nhập thêm dữ liệu**
```sql
USE QLSinhVien
GO

INSERT INTO SinhVien (HoSV, TenSV)
VALUES (N'Nguyễn Văn', N'Sáng')
GO

-- Xem dữ liệu
SELECT * FROM SinhVien
```

**Kết quả:**
```
MaSV    HoSV         TenSV
1       Lê Thành     Tâm
2       Nguyễn Văn   Sáng
```

**Bước 2: Sao lưu DIFFERENTIAL**
```sql
BACKUP DATABASE QLSinhVien
TO DISK = N'D:\QTHCSDL\SaoLuu\QLSinhVien.bak'
WITH DIFFERENTIAL, NOINIT,
NAME = N'QLSinhVien-Differential Database Backup',
SKIP, NOREWIND, NOUNLOAD, STATS = 10
GO
```

Giải thích:
- `DIFFERENTIAL`: Chỉ định backup kiểu differential
- `NOINIT`: Không ghi đè, thêm vào cuối file backup (append)

### Kết quả mong đợi:
- Thông báo: "BACKUP DATABASE WITH DIFFERENTIAL successfully processed..."
- File `QLSinhVien.bak` tăng kích thước (khoảng 4-5 MB)
- File chứa 2 backup sets: 1 FULL + 1 DIFFERENTIAL

---

## CÂU 6: SAO LƯU TAIL LOG

### Yêu cầu:
1. Nhập thêm 1 dòng dữ liệu: (họ tên của sinh viên làm bài)
2. Sao lưu TAIL LOG vào file `D:\QTHCSDL\SaoLuu\QLSinhVien.bak`

### Cách thực hiện:

**Bước 1: Nhập thêm dữ liệu**
```sql
USE QLSinhVien
GO

INSERT INTO SinhVien (HoSV, TenSV)
VALUES (N'Nguyễn Nam Triều', N'Tiến')  -- Thay bằng họ tên của bạn
GO

-- Xem dữ liệu
SELECT * FROM SinhVien
```

**Kết quả:**
```
MaSV    HoSV                TenSV
1       Lê Thành            Tâm
2       Nguyễn Văn          Sáng
3       Nguyễn Nam Triều    Tiến
```

**Bước 2: Sao lưu TAIL LOG**
```sql
BACKUP LOG QLSinhVien
TO DISK = N'D:\QTHCSDL\SaoLuu\QLSinhVien.bak'
WITH NO_TRUNCATE, NOINIT,
NAME = N'QLSinhVien-Tail Log Backup',
SKIP, NOREWIND, NOUNLOAD, STATS = 10
GO
```

**LƯU Ý QUAN TRỌNG:**
- **TAIL LOG** là backup log transaction cuối cùng trước khi restore
- Sử dụng `WITH NO_TRUNCATE` để backup log mà không cắt bỏ log (thường dùng khi database bị lỗi)
- Hoặc có thể dùng `WITH NORECOVERY` nếu đang chuẩn bị restore

**Cách khác (chuẩn hơn cho Tail Log khi chuẩn bị restore):**
```sql
BACKUP LOG QLSinhVien
TO DISK = N'D:\QTHCSDL\SaoLuu\QLSinhVien.bak'
WITH NORECOVERY, NOINIT,
NAME = N'QLSinhVien-Tail-Log Backup'
GO
```

### Kết quả mong đợi:
- Thông báo: "BACKUP LOG successfully processed..."
- File `QLSinhVien.bak` tăng thêm kích thước
- File chứa 3 backup sets: 1 FULL + 1 DIFFERENTIAL + 1 LOG

---

## CÂU 7: PHỤC HỒI CSDL

### Yêu cầu:
1. Xóa CSDL QLSinhVien
2. Phục hồi CSDL từ file backup `QLSinhVien.bak`
3. Xem dữ liệu sau khi phục hồi (phải có đủ 3 dòng)

### Cách thực hiện:

**Bước 1: Xóa database**
```sql
USE master
GO

DROP DATABASE QLSinhVien
GO
```

**Bước 2: Phục hồi từ FULL backup**
```sql
-- Restore FULL backup (FILE = 1)
RESTORE DATABASE QLSinhVien
FROM DISK = N'D:\QTHCSDL\SaoLuu\QLSinhVien.bak'
WITH FILE = 1, NORECOVERY,
STATS = 10
GO
```

**Bước 3: Phục hồi từ DIFFERENTIAL backup**
```sql
-- Restore DIFFERENTIAL backup (FILE = 2)
RESTORE DATABASE QLSinhVien
FROM DISK = N'D:\QTHCSDL\SaoLuu\QLSinhVien.bak'
WITH FILE = 2, NORECOVERY,
STATS = 10
GO
```

**Bước 4: Phục hồi từ LOG backup (Tail Log)**
```sql
-- Restore LOG backup (FILE = 3)
RESTORE LOG QLSinhVien
FROM DISK = N'D:\QTHCSDL\SaoLuu\QLSinhVien.bak'
WITH FILE = 3, RECOVERY,
STATS = 10
GO
```

**LƯU Ý:**
- `NORECOVERY`: Database vẫn ở trạng thái restoring, có thể restore thêm
- `RECOVERY`: Hoàn tất quá trình restore, database sẵn sàng sử dụng
- `FILE = N`: Chỉ định backup set thứ N trong file .bak

**Bước 5: Kiểm tra dữ liệu**
```sql
USE QLSinhVien
GO

SELECT * FROM SinhVien
GO
```

### Kết quả mong đợi:
```
MaSV    HoSV                TenSV
1       Lê Thành            Tâm
2       Nguyễn Văn          Sáng
3       Nguyễn Nam Triều    Tiến
```

**Lưu ý về thứ tự thời gian:**
- Thời gian tạo các bản backup phải đúng thứ tự
- Dữ liệu phục hồi phải chính xác với MaSV tăng dần (1, 2, 3)

---

## CÂU 8: TẠO OPERATOR, JOB, SCHEDULE VÀ CHẠY THỬ JOB

### Yêu cầu:
1. Tạo **Operator** với tên là tên sinh viên, email là email trường cấp
2. Tạo **Job** tên **JobSaoLuuCSDL** để sao lưu FULL database AdventureWorks
3. File backup: `D:\QTHCSDL\SaoLuu\AdventureWorks.bak` (luôn chỉ có 1 bản backup)
4. Đặt lịch: 23:00 hàng ngày và 19:00 Chủ nhật hàng tuần
5. Gửi email cho operator dù thành công hay thất bại
6. Chạy thử job và kiểm tra kết quả

### Cách thực hiện:

**Bước 1: Tạo Operator**

Sử dụng GUI:
1. Trong SSMS, mở rộng **SQL Server Agent**
2. Click chuột phải vào **Operators** → **New Operator**
3. Nhập thông tin:
   - **Name**: `Nguyen Nam Trieu Tien` (tên sinh viên)
   - **Email name**: `2154053004@en.dou.edu.vn`
   - **Pager e-mail name**: (có thể để trống)
   - Đặt lịch trực: Chọn tất cả các ngày từ Monday đến Sunday
   - Workday begin time: 8:00:00 AM
   - Workday end time: 6:00:00 PM
4. Click **OK**

Hoặc dùng T-SQL:
```sql
USE [msdb]
GO

EXEC msdb.dbo.sp_add_operator
    @name=N'Nguyen Nam Trieu Tien',
    @enabled=1,
    @email_address=N'2154053004@en.dou.edu.vn',
    @weekday_pager_start_time=80000,
    @weekday_pager_end_time=180000,
    @saturday_pager_start_time=80000,
    @saturday_pager_end_time=180000,
    @sunday_pager_start_time=80000,
    @sunday_pager_end_time=180000
GO
```

**Bước 2: Tạo Job**

```sql
USE [msdb]
GO

-- Tạo Job
EXEC dbo.sp_add_job
    @job_name = N'JobSaoLuuCSDL'
GO

-- Thêm Job Step
EXEC sp_add_jobstep
    @job_name = N'JobSaoLuuCSDL',
    @step_name = N'JobSaoLuuCSDL',
    @subsystem = N'TSQL',
    @command = N'BACKUP DATABASE AdventureWorks
TO DISK = N''D:\QTHCSDL\SaoLuu\AdventureWorks.bak''
WITH FORMAT, INIT,
NAME = N''AdventureWorks-Full Database Backup'',
SKIP, NOREWIND, NOUNLOAD, STATS = 10',
    @database_name = N'master',
    @retry_attempts = 0,
    @retry_interval = 0
GO

-- Thêm Schedule 1: 23:00 hàng ngày
EXEC sp_add_schedule
    @schedule_name = N'LichSaoLuu23GioMoiNgay',
    @freq_type = 4, -- Daily
    @freq_interval = 1, -- Every 1 day
    @active_start_time = 230000 -- 11:00:00 PM
GO

-- Gán Schedule 1 cho Job
EXEC sp_attach_schedule
    @job_name = N'JobSaoLuuCSDL',
    @schedule_name = N'LichSaoLuu23GioMoiNgay'
GO

-- Thêm Schedule 2: 19:00 Chủ nhật hàng tuần
EXEC sp_add_schedule
    @schedule_name = N'LichSaoLuu19GioChuNhat',
    @freq_type = 8, -- Weekly
    @freq_interval = 1, -- Sunday (1=Sunday, 2=Monday, ... 64=Saturday)
    @freq_recurrence_factor = 1, -- Every week
    @active_start_time = 190000 -- 07:00:00 PM
GO

-- Gán Schedule 2 cho Job
EXEC sp_attach_schedule
    @job_name = N'JobSaoLuuCSDL',
    @schedule_name = N'LichSaoLuu19GioChuNhat'
GO

-- Đặt notification cho operator
EXEC sp_add_jobserver
    @job_name = N'JobSaoLuuCSDL',
    @server_name = N'(local)'
GO

EXEC sp_update_job
    @job_name = N'JobSaoLuuCSDL',
    @notify_level_email = 3, -- 1=On Success, 2=On Failure, 3=Always
    @notify_email_operator_name = N'Nguyen Nam Trieu Tien'
GO
```

**Giải thích freq_interval cho Weekly:**
- Sunday = 1
- Monday = 2
- Tuesday = 4
- Wednesday = 8
- Thursday = 16
- Friday = 32
- Saturday = 64

**Bước 3: Chạy thử Job**

Cách 1: Dùng GUI
1. Trong SQL Server Agent → Jobs
2. Click chuột phải vào **JobSaoLuuCSDL**
3. Chọn **Start Job at Step...**
4. Xem kết quả trong cửa sổ "Start Jobs"

Cách 2: Dùng T-SQL
```sql
USE msdb
GO

EXEC dbo.sp_start_job N'JobSaoLuuCSDL'
GO
```

**Bước 4: Kiểm tra kết quả**

```sql
-- Xem lịch sử chạy job
EXEC sp_help_jobhistory @job_name = N'JobSaoLuuCSDL'
GO
```

Hoặc click chuột phải vào Job → **View History**

**Bước 5: Kiểm tra file backup**
- Vào thư mục `D:\QTHCSDL\SaoLuu\`
- Xem properties của file `AdventureWorks.bak`
- Kiểm tra:
  - Kích thước file (khoảng 200+ MB)
  - Thời gian Modified phải là thời gian vừa chạy job

### Kết quả mong đợi:
- Operator được tạo thành công với email
- Job có 1 step với code backup
- Job có 2 schedule: 23:00 Daily và 19:00 Sunday
- Job notification: Always send email to operator
- Chạy thử job thành công
- File `AdventureWorks.bak` được tạo/cập nhật

---

## CÂU 9: TẠO VÀ GÁN QUYỀN CHO LOGIN VÀ DATABASE USER

### Câu 9a: Tạo Server Role và Login

### Yêu cầu:
1. Tạo **Server Role** tên **TaoLogin_KhongDuocXemTenCacCSDL**
   - Có quyền tạo login
   - Không có quyền xem tên các CSDL
2. Tạo **SQL Login** tên **HoTenSVKhongDau1** (ví dụ: NguyenVanAnh1)
3. Gán login vào Server Role trên
4. Test quyền bằng login này

### Cách thực hiện:

**Bước 1: Tạo Server Role**

```sql
USE [master]
GO

-- Tạo Server Role
CREATE SERVER ROLE [TaoLogin_KhongDuocXemTenCacCSDL]
GO

-- Gán quyền tạo login
GRANT ALTER ANY LOGIN TO [TaoLogin_KhongDuocXemTenCacCSDL]
GO

-- Từ chối quyền xem metadata của database
DENY VIEW ANY DATABASE TO [TaoLogin_KhongDuocXemTenCacCSDL]
GO
```

**Bước 2: Tạo Login mới**

```sql
-- Tạo SQL Login
CREATE LOGIN [NguyenVanAnh1] WITH PASSWORD=N'MatKhau123@'
GO

-- Gán login vào Server Role
ALTER SERVER ROLE [TaoLogin_KhongDuocXemTenCacCSDL]
ADD MEMBER [NguyenVanAnh1]
GO
```

**Bước 3: Test Server Role**

1. Đăng xuất khỏi SSMS hiện tại
2. Đăng nhập lại với:
   - **Server name**: (local) hoặc tên server
   - **Authentication**: SQL Server Authentication
   - **Login**: NguyenVanAnh1
   - **Password**: MatKhau123@
3. Sau khi đăng nhập:
   - Object Explorer **KHÔNG** hiển thị danh sách databases
   - Chỉ hiển thị: Security, Server Objects, Replication, ...
   - Có thể tạo login mới (quyền ALTER ANY LOGIN)

**Test tạo login:**
```sql
-- Login NguyenVanAnh1 có thể chạy lệnh này
CREATE LOGIN [TestLogin] WITH PASSWORD=N'Pass123@'
GO
```

### Kết quả mong đợi:
- Server Role được tạo với quyền ALTER ANY LOGIN
- Server Role bị từ chối quyền VIEW ANY DATABASE
- Login NguyenVanAnh1 là member của Server Role
- Khi đăng nhập bằng NguyenVanAnh1, không thấy danh sách databases

---

### Câu 9b: Tạo Database Role và gán quyền cấp cột

### Yêu cầu:
1. Tạo **Database Role** tên **XemDLBangNhanVien**
2. Gán quyền xem 5 cột: [EmployeeID], [LastName], [FirstName], [Title], [TitleOfCourtesy] của bảng `[Northwind].[dbo].[Employees]`
3. Không xem được các cột còn lại
4. Tạo **SQL Login** tên **HoTenSVKhongDau2** (ví dụ: NguyenVanAnh2)
5. Tạo **Database User** cùng tên trong database Northwind
6. Gán user vào Database Role
7. Test quyền

### Cách thực hiện:

**Bước 1: Tạo Database Role**

```sql
USE [Northwind]
GO

-- Tạo Database Role
CREATE ROLE [XemDLBangNhanVien]
GO

-- Gán quyền SELECT trên 5 cột cụ thể
GRANT SELECT ON [dbo].[Employees]
    ([EmployeeID], [LastName], [FirstName], [Title], [TitleOfCourtesy])
TO [XemDLBangNhanVien]
GO
```

**Bước 2: Tạo Login và Database User**

```sql
USE [master]
GO

-- Tạo SQL Login
CREATE LOGIN [NguyenVanAnh2] WITH PASSWORD=N'MatKhau123@'
GO

USE [Northwind]
GO

-- Tạo Database User
CREATE USER [NguyenVanAnh2] FOR LOGIN [NguyenVanAnh2]
GO

-- Gán User vào Database Role
ALTER ROLE [XemDLBangNhanVien] ADD MEMBER [NguyenVanAnh2]
GO
```

**Bước 3: Test quyền**

1. Đăng xuất và đăng nhập lại bằng login **NguyenVanAnh2**
2. Chạy các câu query sau:

**Test 1 - Select tất cả cột (sẽ BỊ LỖI):**
```sql
USE Northwind
GO

SELECT * FROM [dbo].[Employees]
-- Kết quả: Msg 230... The SELECT permission was denied...
```

**Test 2 - Select 5 cột được phép (THÀNH CÔNG):**
```sql
SELECT [EmployeeID], [LastName], [FirstName], [Title], [TitleOfCourtesy]
FROM [dbo].[Employees]
-- Kết quả: Hiển thị dữ liệu 5 cột
```

**Test 3 - Select cột không được phép (BỊ LỖI):**
```sql
SELECT [EmployeeID], [LastName], [FirstName], [BirthDate]
FROM [dbo].[Employees]
-- Kết quả: Msg 230... The SELECT permission was denied on the column 'BirthDate'...
```

### Kết quả mong đợi:
- Database Role **XemDLBangNhanVien** có quyền SELECT trên 5 cột cụ thể
- Login và User **NguyenVanAnh2** được tạo và gán vào role
- Khi test:
  - SELECT 5 cột được phép: **THÀNH CÔNG**
  - SELECT cột khác: **BỊ LỖI** (Permission denied)
  - SELECT * : **BỊ LỖI** (Permission denied)

---

## CÂU 10: CÀI ĐẶT SQL SERVER

### Yêu cầu:
Cài đặt một SQL Server mới có tên instance là **HoTenSV** (ví dụ: NguyenVanAnh). Sau khi cài đặt, đăng nhập vào server mới bằng login sa và chụp màn hình Server Properties.

### Cách thực hiện:

**Bước 1: Tải SQL Server Setup**
1. Nếu chưa có, tải SQL Server từ trang chủ Microsoft
2. Chạy file setup (ví dụ: SQLServer2019-SSEI-Dev.exe)

**Bước 2: Cài đặt SQL Server**

1. Chọn **New SQL Server stand-alone installation**
2. **Product Key**: Chọn Developer hoặc nhập key
3. **License Terms**: Accept
4. **Feature Selection**: Chọn ít nhất:
   - Database Engine Services
   - Client Tools Connectivity
   - Management Tools (SQL Server Management Studio) - nếu chưa có
5. **Instance Configuration**:
   - Chọn **Named instance**
   - **Instance name**: `HoTenSV` (ví dụ: NguyenVanAnh hoặc NGUYENTRIEUTIEN)
   - **Instance ID**: tự động điền giống Instance name
6. **Server Configuration**:
   - Để mặc định các service accounts
   - Hoặc chọn NT AUTHORITY\SYSTEM hoặc NT AUTHORITY\NETWORK SERVICE
7. **Database Engine Configuration**:
   - **Authentication Mode**: Chọn **Mixed Mode**
   - **Password**: Nhập password cho sa (ví dụ: Sa@123456)
   - **Confirm password**: Nhập lại password
   - **Specify SQL Server administrators**: Thêm Windows user hiện tại
8. **Ready to Install**: Click Install
9. Chờ cài đặt hoàn tất (khoảng 10-30 phút)

**Bước 3: Kết nối vào Instance mới**

1. Mở SQL Server Management Studio (SSMS)
2. Trong cửa sổ Connect to Server:
   - **Server type**: Database Engine
   - **Server name**: `TenMaySV\HoTenSV` (ví dụ: 638\NguyenVanAnh hoặc 638\NGUYENTRIEUTIEN)
   - **Authentication**: SQL Server Authentication
   - **Login**: sa
   - **Password**: Sa@123456 (password đã đặt lúc cài)
3. Click **Connect**

**Bước 4: Xem Server Properties**

1. Trong Object Explorer, click chuột phải vào server name (ở trên cùng)
2. Chọn **Properties**
3. Trong cửa sổ **Server Properties**, chọn tab **General**
4. Xem thông tin:
   - **Name**: 638\NGUYENTRIEUTIEN (hoặc tên instance của bạn)
   - **Product**: Microsoft SQL Server Developer (64-bit)
   - **Operating System**: Windows 10 Enterprise... (hoặc version của bạn)
   - **Platform**: Windows
   - **Version**: 15.0.2000.5 (hoặc version của bạn)
   - **Language**: English (United States)
   - **Memory**: ... MB
   - **Processors**: 12 (hoặc số processor của bạn)
   - **Root Directory**: `C:\Program Files\Microsoft SQL Server\MSSQL15.NGUYENTRIEUTIEN\MSSQL`
   - **Server Collation**: SQL_Latin1_General_CP1_CI_AS
   - **Is Clustered**: False
   - **Is XTP Supported**: True
   - **Is HADR Enabled**: False

### Kết quả mong đợi:
- SQL Server instance mới được cài đặt thành công
- Tên instance chứa họ tên sinh viên (không dấu)
- Đăng nhập thành công bằng sa
- Server Properties hiển thị:
  - Tên instance đầy đủ (TenMay\Instance)
  - Root Directory chứa tên instance
  - Danh sách System Databases trong Object Explorer (master, model, msdb, tempdb)

---

## TỔNG KẾT

Đề thi này kiểm tra các kỹ năng quản trị SQL Server cơ bản:

1. **Cấu hình kết nối**: Alias Server
2. **Đối tượng database**: Synonym
3. **Command-line tools**: SQLCMD
4. **Backup & Restore**: FULL, DIFFERENTIAL, LOG, TAIL-LOG
5. **Automation**: SQL Server Agent, Jobs, Schedules, Operators
6. **Security**: Server Roles, Database Roles, Column-level permissions
7. **Installation**: SQL Server setup

**Lưu ý quan trọng khi làm bài:**
- Đọc kỹ yêu cầu, làm đúng theo đề
- Chụp màn hình TOÀN màn hình (không crop, không edit)
- Hiển thị đầy đủ thông tin: tên server, Object Explorer, code, kết quả, đồng hồ
- Kiểm tra kỹ kết quả trước khi chụp
- Đặt tên file nộp bài đúng format: `MSSV_HoTenKhongDau.docx`

**Chúc các bạn làm bài tốt!**
