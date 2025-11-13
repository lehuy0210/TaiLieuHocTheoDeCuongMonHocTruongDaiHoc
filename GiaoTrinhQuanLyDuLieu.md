# LẬP TRÌNH QUẢN LÝ DỮ LIỆU - GIÁO TRÌNH THỰC HÀNH

> **Dựa trên bài toán: Quản lý Thư viện Sách**
> 
> **Áp dụng cho: Mọi hệ thống quản lý có cấu trúc tương tự**

---

## PHẦN I: CƠ SỞ LÝ THUYẾT

### 1.1. Mô hình dữ liệu

Mọi hệ thống quản lý đều có 2 thành phần chính:

#### **A. Đối tượng chính (Main Entity)**
Đối tượng cần quản lý, có các thuộc tính:
- **Định danh**: ID, mã số, tên duy nhất
- **Thuộc tính mô tả**: Tên, loại, danh mục
- **Quan hệ**: Người sở hữu, người quản lý
- **Giá trị định lượng**: Số lượng, điểm số, giá trị
- **Trạng thái**: Tình trạng hiện tại

**Ví dụ thực tế (Bài1.cpp - dòng 12-16):**
```cpp
struct Sach {
    string tenSach;      // Định danh chính
    string tenDocGia;    // Quan hệ (ai đang mượn)
    int soLuongSach;     // Giá trị định lượng
};
```

**Áp dụng cho các hệ thống khác:**

| Hệ thống | Định danh | Quan hệ | Giá trị | Trạng thái |
|----------|-----------|---------|---------|------------|
| **Thư viện** | tenSach | tenDocGia | soLuong | tinhTrang |
| **Sinh viên** | maSV | giangVien | diem | xepLoai |
| **Kho hàng** | maSP | nhaCungCap | soLuongKho | trangThai |
| **Phòng ban** | maPhong | truongPhong | soBan | trangThai |

#### **B. Giao dịch (Transaction)**
Ghi nhận hoạt động, có các thuộc tính:
- **Thời điểm bắt đầu**: Ngày, giờ thực hiện
- **Thời điểm kết thúc**: Deadline, hạn chót
- **Người thực hiện**: Tùy chọn
- **Ghi chú**: Thông tin bổ sung

**Ví dụ thực tế (Bài1.cpp - dòng 17-21):**
```cpp
struct PhieuMuon {
    string thoiGianMuon;  // Thời điểm bắt đầu
    string thoiGianTra;   // Thời điểm kết thúc
};
```

**Áp dụng cho các hệ thống khác:**

| Hệ thống | Tên giao dịch | Bắt đầu | Kết thúc |
|----------|---------------|---------|----------|
| **Thư viện** | PhieuMuon | ngayMuon | ngayTra |
| **Sinh viên** | DangKyMonHoc | ngayDangKy | ngayKetThuc |
| **Kho hàng** | PhieuXuat | ngayXuat | ngayGiao |
| **Dự án** | TaskAssignment | startDate | deadline |

---

### 1.2. Nguyên tắc quản lý bộ nhớ động

#### **Định lý 1: Khởi tạo Counter**
```
Đối với biến đếm số phần tử thực tế trong mảng động:
    LUÔN khởi tạo = 0
    SAI khi khởi tạo = maxSize
```

**Chứng minh qua ví dụ (Bài1.cpp - dòng 331-333):**
```cpp
// ĐÚNG:
int dem = 0;              // ← Sẽ được cập nhật khi đọc file
int maxSach = 100;        // Giới hạn tối đa
Sach* dsSach = new Sach[maxSach];

// SAI:
int dem = 100;            // ← Sẽ ghi 100 dòng rác vào file!
```

**Hệ quả:**
- Nếu `dem = maxSize` → Khi ghi file sẽ ghi tất cả phần tử (kể cả rác)
- Nếu `dem = 0` → Chỉ ghi số phần tử thực tế đã đọc

**Áp dụng:**
```cpp
// Template cho mọi hệ thống:
int count = 0;           // Counter thực tế
int maxItems = 100;      // Giới hạn
Entity* array = new Entity[maxItems];
```

---

## PHẦN II: CÁC THUẬT TOÁN CƠ BẢN

### 2.1. Đọc dữ liệu từ file CSV

#### **Định nghĩa:**
CSV (Comma-Separated Values) là định dạng file text lưu dữ liệu dạng bảng, mỗi dòng là một record, các field phân cách bởi dấu phẩy.

**Cấu trúc tổng quát:**
```
field1,field2,field3,...,fieldN
```

#### **Thuật toán:**
```
1. Mở file
2. Nếu không mở được → Thử vị trí khác (fallback)
3. Khởi tạo counter = 0
4. Đọc từng dòng:
   a. Parse dòng thành các field
   b. Lưu vào struct
   c. Tăng counter
5. Đóng file
```

#### **Cài đặt (Bài1.cpp - dòng 23-83):**

**Bước 1: Mở file với fallback**
```cpp
ifstream inFile("DanhSachSach.txt");
if (!inFile.is_open())
    inFile.open("../DanhSachSach.txt");  // Thử thư mục cha
```

**Nguyên lý:** 
- Working directory có thể khác nhau (Debug/, Release/, v.v.)
- Fallback đảm bảo tìm được file ở nhiều vị trí

**Bước 2: Parse CSV động**
```cpp
dem = 0;  // ← CRITICAL
string line;
while (getline(inFile, line))
{
    string field1 = "", field2 = "", field3 = "";
    int partIndex = 0;
    
    for (int i = 0; i < line.length(); i++)
    {
        if (line[i] == ',')
            partIndex++;
        else {
            if (partIndex == 0) field1 += line[i];
            else if (partIndex == 1) field2 += line[i];
            else if (partIndex == 2) field3 += line[i];
        }
    }
    
    array[dem].field1 = field1;
    array[dem].field2 = field2;
    array[dem].field3 = stoi(field3);  // Convert nếu cần
    dem++;
}
```

**Phân tích:**
- Biến `partIndex` đánh dấu đang ở field thứ mấy
- Gặp delimiter (`,`) → tăng `partIndex`
- Không gặp delimiter → nối ký tự vào field hiện tại

**Độ phức tạp:**
- Thời gian: O(n × m) với n = số dòng, m = độ dài trung bình
- Không gian: O(1) (không dùng thêm mảng phụ)

#### **Biến thể cho delimiter khác:**
```cpp
char delimiter = ';';  // Hoặc '|', '\t'

if (line[i] == delimiter)
    partIndex++;
```

#### **Tổng quát hóa:**
```cpp
void ReadCSV(Entity* arr, int& count, string filename, char delim = ',')
{
    ifstream file(filename);
    if (!file.is_open())
        file.open("../" + filename);
    
    count = 0;
    string line;
    
    while (getline(file, line)) {
        // Parse logic như trên
        count++;
    }
    
    file.close();
}
```

---

### 2.2. Loại bỏ trùng lặp khi hiển thị

#### **Bài toán:**
Cho mảng A có n phần tử, một số phần tử trùng nhau. Hiển thị danh sách các giá trị duy nhất (unique values).

**Ví dụ:**
```
Input:  ["A", "B", "A", "C", "B"]
Output: A, B, C
```

#### **Thuật toán Brute Force:**
```
Với mỗi phần tử i:
    Kiểm tra xem i có trùng với phần tử nào từ [0..i-1] không
    Nếu KHÔNG trùng → Hiển thị
```

#### **Cài đặt (Bài1.cpp - dòng 126-140):**
```cpp
for (int i = 0; i < n; i++)
{
    bool daTonTai = false;
    
    // Kiểm tra trùng với các phần tử trước đó
    for (int j = 0; j < i; j++)
    {
        if (array[i].field == array[j].field)
        {
            daTonTai = true;
            break;
        }
    }
    
    if (!daTonTai)
        cout << array[i].field << endl;
}
```

**Chứng minh tính đúng:**
- Với mỗi phần tử `i`, chỉ kiểm tra các phần tử từ `0` đến `i-1`
- Nếu `i` trùng với bất kỳ phần tử nào trước đó → Đã được in rồi
- Nếu `i` không trùng → Đây là lần xuất hiện đầu tiên → In ra

**Độ phức tạp:**
- Thời gian: O(n²) - không tối ưu nhưng đơn giản
- Không gian: O(1)

**Tối ưu hóa (sử dụng Set - nếu được dùng STL):**
```cpp
set<string> seen;
for (int i = 0; i < n; i++) {
    if (seen.find(array[i].field) == seen.end()) {
        cout << array[i].field << endl;
        seen.insert(array[i].field);
    }
}
// Độ phức tạp: O(n log n)
```

#### **Áp dụng:**
- Hiển thị danh sách độc giả (không trùng)
- Hiển thị danh sách thể loại sách
- Hiển thị danh sách ngành (sinh viên)
- Hiển thị danh sách nhà cung cấp (sản phẩm)

---

### 2.3. Tìm và cập nhật một phần tử

#### **Bài toán:**
Cho mảng A có n phần tử, tìm phần tử có `id = targetId` và cập nhật giá trị của nó.

**Yêu cầu quan trọng:**
- Chỉ cập nhật **MỘT** phần tử tìm được đầu tiên
- Dừng ngay sau khi tìm thấy (không duyệt hết mảng)

#### **Thuật toán:**
```
Với i từ 0 đến n-1:
    Nếu array[i].id == targetId:
        Cập nhật array[i].value
        BREAK  ← CRITICAL
```

#### **Cài đặt (Bài1.cpp - dòng 194-207):**
```cpp
void Update(Entity* arr, int n, string targetId, int amount)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i].id == targetId)
        {
            arr[i].value -= amount;  // Hoặc +=, =
            break;  // ← BẮT BUỘC
        }
    }
}
```

**Phân tích lỗi thường gặp:**

**SAI:**
```cpp
// Cập nhật TẤT CẢ phần tử
for (int i = 0; i < n; i++)
    arr[i].value -= amount;  // ← Giảm hết!
```

**SAI:**
```cpp
// Quên break → Tiếp tục duyệt (lãng phí)
for (int i = 0; i < n; i++) {
    if (arr[i].id == targetId)
        arr[i].value -= amount;
    // Không có break!
}
```

**ĐÚNG:**
```cpp
for (int i = 0; i < n; i++) {
    if (arr[i].id == targetId) {
        arr[i].value -= amount;
        break;  // ← Dừng ngay
    }
}
```

#### **Các loại cập nhật:**

| Nghiệp vụ | Code | Ví dụ |
|-----------|------|-------|
| Giảm giá trị | `value -= amount` | Mượn sách, bán hàng |
| Tăng giá trị | `value += amount` | Trả sách, nhập kho |
| Gán giá trị | `value = newValue` | Sửa điểm |
| Đổi trạng thái | `status = newStatus` | Đánh dấu đã mượn |
| Xóa logic | `isDeleted = true` | Soft delete |

---

### 2.4. Ghi dữ liệu ra file

#### **Nguyên tắc vàng:**
```
CHỈ ghi `count` phần tử thực tế
KHÔNG ghi `maxSize` phần tử
```

#### **Cài đặt (Bài1.cpp - dòng 209-224):**
```cpp
ofstream outFile("data.txt", ios::out);  // Overwrite mode

for (int i = 0; i < dem; i++)  // ← ĐÚNG: dem (không phải maxSach)
{
    outFile << array[i].field1 << "," 
            << array[i].field2 << "," 
            << array[i].field3 << endl;
}

outFile.close();
```

**Chứng minh:**
- `dem` = số phần tử thực tế đã đọc (ví dụ: 3)
- `maxSize` = kích thước mảng (ví dụ: 100)
- Nếu ghi `maxSize` → ghi 97 dòng rác!

**File modes:**

| Mode | Code | Ý nghĩa | Sử dụng |
|------|------|---------|---------|
| Overwrite | `ios::out` | Xóa cũ, ghi mới | Cập nhật dữ liệu |
| Append | `ios::app` | Ghi thêm vào cuối | Log, history |

---

## PHẦN III: XỬ LÝ NGÀY THÁNG

### 3.1. Parse ngày từ chuỗi

#### **Định dạng chuẩn:**
```
dd/mm/yyyy  hoặc  dd-mm-yyyy
```

#### **Thuật toán:**
```
1. Khởi tạo 3 chuỗi: ngày, tháng, năm
2. Duyệt từng ký tự:
   - Nếu gặp delimiter ('/' hoặc '-') → Tăng part
   - Ngược lại → Nối vào chuỗi tương ứng
3. Convert chuỗi → số
```

#### **Cài đặt (Bài1.cpp - dòng 239-264):**
```cpp
void ParseDate(string dateStr, int& day, int& month, int& year)
{
    string d = "", m = "", y = "";
    int part = 0;
    
    for (int i = 0; i < dateStr.length(); i++)
    {
        if (dateStr[i] == '/' || dateStr[i] == '-')
            part++;
        else {
            if (part == 0) d += dateStr[i];
            else if (part == 1) m += dateStr[i];
            else if (part == 2) y += dateStr[i];
        }
    }
    
    try {
        day = stoi(d);
        month = stoi(m);
        year = stoi(y);
    }
    catch (...) {
        day = month = year = 0;  // Default nếu lỗi
    }
}
```

**Test cases:**

| Input | Output |
|-------|--------|
| `"15/01/2025"` | `day=15, month=1, year=2025` |
| `"25-12-2024"` | `day=25, month=12, year=2024` |
| `"abc"` | `day=0, month=0, year=0` (lỗi) |

#### **Tổng quát hóa:**
```cpp
// Hỗ trợ nhiều delimiter
vector<char> delimiters = {'/', '-', '.', ' '};

if (find(delimiters.begin(), delimiters.end(), c) != delimiters.end())
    part++;
```

---

### 3.2. So sánh ngày tháng

#### **Nguyên tắc:**
So sánh theo thứ tự: **Năm → Tháng → Ngày**

#### **Thuật toán:**
```
Hàm IsEarlier(date1, date2):
    Nếu year1 < year2 → ĐÚNG
    Nếu year1 == year2:
        Nếu month1 < month2 → ĐÚNG
        Nếu month1 == month2:
            Nếu day1 < day2 → ĐÚNG
    Trả về SAI
```

#### **Cài đặt (Bài1.cpp - dòng 273-288):**
```cpp
bool IsEarlier(int d1, int m1, int y1, int d2, int m2, int y2)
{
    if (y1 < y2) return true;
    if (y1 == y2) {
        if (m1 < m2) return true;
        if (m1 == m2 && d1 < d2) return true;
    }
    return false;
}
```

**Ví dụ:**
```cpp
IsEarlier(15, 1, 2024,  20, 1, 2024)  → true  (cùng tháng, ngày < )
IsEarlier(31, 12, 2023, 1, 1, 2024)   → true  (năm < )
IsEarlier(15, 1, 2025,  15, 1, 2025)  → false (bằng nhau)
```

#### **Ứng dụng:**
```cpp
// Kiểm tra quá hạn
bool IsOverdue(string deadline) {
    int dDL, mDL, yDL;
    ParseDate(deadline, dDL, mDL, yDL);
    
    int dNow, mNow, yNow;
    GetCurrentDate(dNow, mNow, yNow);
    
    return IsEarlier(dDL, mDL, yDL, dNow, mNow, yNow);
}
```

---

### 3.3. Lấy ngày hiện tại

#### **Sử dụng thư viện `<ctime>`:**

```cpp
void GetCurrentDate(int& day, int& month, int& year)
{
    time_t now = time(0);
    tm* t = localtime(&now);
    
    day = t->tm_mday;
    month = t->tm_mon + 1;      // +1 vì bắt đầu từ 0
    year = t->tm_year + 1900;   // +1900 vì tính từ 1900
}
```

**Bảng tra cứu `tm` struct:**

| Field | Giá trị | Công thức |
|-------|---------|-----------|
| `tm_mday` | 1-31 | `ngay = t->tm_mday` |
| `tm_mon` | 0-11 | `thang = t->tm_mon + 1` |
| `tm_year` | Từ 1900 | `nam = t->tm_year + 1900` |
| `tm_hour` | 0-23 | `gio = t->tm_hour` |
| `tm_min` | 0-59 | `phut = t->tm_min` |
| `tm_sec` | 0-59 | `giay = t->tm_sec` |

**Lưu ý:**
- `#define _CRT_SECURE_NO_WARNINGS` để tắt warning C4996 với `localtime()`

---

## PHẦN IV: LOGGING & ERROR HANDLING

### 4.1. Ghi log với timestamp

#### **Mục đích:**
- Tracking hoạt động của hệ thống
- Debug khi có lỗi
- Audit trail (kiểm tra sau này)

#### **Cài đặt (Bài1.cpp - dòng 301-322):**
```cpp
void Log(string message)
{
    ofstream file("log.txt", ios::app);  // Append mode
    
    time_t now = time(0);
    tm* t = localtime(&now);
    
    file << "[" << t->tm_mday << "/" 
         << (t->tm_mon + 1) << "/" 
         << (t->tm_year + 1900) << " "
         << t->tm_hour << ":" 
         << t->tm_min << ":" 
         << t->tm_sec << "] " 
         << message << endl;
    
    file.close();
}
```

**Ví dụ output:**
```
[15/1/2025 10:30:45] Doc file thanh cong
[15/1/2025 10:31:12] User chon: LapTrinhC++
[15/1/2025 10:31:30] Cap nhat thanh cong
```

#### **Vị trí nên ghi log:**

| Sự kiện | Ví dụ |
|---------|-------|
| Bắt đầu/Kết thúc | `Log("=== START ===")` |
| Đọc file thành công | `Log("Doc file: 10 ban ghi")` |
| Đọc file thất bại | `Log("Loi: File not found")` |
| User action | `Log("User chon: " + itemName)` |
| Cập nhật dữ liệu | `Log("Update: " + id)` |
| Điều kiện đặc biệt | `Log("PHAT HIEN QUA HAN")` |
| Exception | `Log("Exception: " + e.what())` |

---

### 4.2. Try-Catch pattern

#### **Template chuẩn:**
```cpp
void Function()
{
    try {
        // Code có thể sinh lỗi
        ifstream file("data.txt");
        if (!file.is_open())
            throw runtime_error("Cannot open file!");
        
        // Xử lý...
        
        file.close();
        Log("Success");
    }
    catch (exception& e) {
        cout << "Error: " << e.what() << endl;
        Log("Error: " + string(e.what()));
    }
}
```

#### **Các điểm cần try-catch:**
1. ✅ Mở file (`ifstream`, `ofstream`)
2. ✅ Convert string → số (`stoi`, `stof`)
3. ✅ Truy cập mảng (nếu có dynamic bounds)
4. ✅ Parse dữ liệu user input

---

## PHẦN V: CẤU TRÚC CHƯƠNG TRÌNH HOÀN CHỈNH

### 5.1. Luồng thực thi

```
MAIN
 ├─→ 1. Ghi log bắt đầu
 ├─→ 2. Khai báo biến & cấp phát bộ nhớ
 ├─→ 3. Đọc dữ liệu từ file
 ├─→ 4. Kiểm tra dữ liệu rỗng
 ├─→ 5. Tìm kiếm & Lựa chọn
 ├─→ 6. Cập nhật dữ liệu
 ├─→ 7. Kiểm tra điều kiện (nếu có)
 ├─→ 8. Lưu kết quả
 ├─→ 9. Giải phóng bộ nhớ
 └─→ 10. Ghi log kết thúc
```

### 5.2. Template main()

```cpp
int main()
{
    // 1. Log bắt đầu
    Log("=== START ===");
    
    // 2. Khai báo
    int count = 0;
    int maxSize = 100;
    Entity* entities = new Entity[maxSize];
    Transaction* trans = new Transaction;
    
    // 3. Đọc dữ liệu
    ReadFile(entities, count);
    
    // 4. Kiểm tra rỗng
    if (count == 0) {
        cout << "No data!" << endl;
        Log("No data to process.");
        delete[] entities;
        delete trans;
        return 0;
    }
    
    // 5-8. Xử lý nghiệp vụ
    string selected;
    int value;
    bool done = false;
    
    Search(entities, count, selected, done);
    Update(entities, count, selected, value, done);
    Validate(trans);
    SaveResult(trans);
    
    // 9. Giải phóng
    delete[] entities;
    delete trans;
    entities = nullptr;
    trans = nullptr;
    
    // 10. Log kết thúc
    Log("=== END ===");
    return 0;
}
```

---

## PHẦN VI: ÁP DỤNG CHO CÁC DỰ ÁN KHÁC

### 6.1. Bảng chuyển đổi thuật ngữ

#### **Từ Bài1.cpp sang các dự án khác:**

| Bài1.cpp | Sinh viên | Kho hàng | Nhân viên | Dự án |
|----------|-----------|----------|-----------|-------|
| `Sach` | `SinhVien` | `SanPham` | `NhanVien` | `Task` |
| `tenSach` | `maSV` | `maSP` | `maNV` | `taskID` |
| `tenDocGia` | `giangVien` | `nhaCungCap` | `truongPhong` | `assignee` |
| `soLuongSach` | `diem` | `soLuongKho` | `luong` | `priority` |
| `PhieuMuon` | `DangKyMon` | `PhieuXuat` | `HopDong` | `Sprint` |
| `thoiGianMuon` | `ngayDangKy` | `ngayXuat` | `ngayBatDau` | `startDate` |
| `thoiGianTra` | `ngayKetThuc` | `ngayGiao` | `ngayKetThuc` | `endDate` |

### 6.2. Checklist chuyển đổi dự án

Khi áp dụng cho dự án mới:

- [ ] **Bước 1:** Định nghĩa struct Entity với 3-5 field
- [ ] **Bước 2:** Định nghĩa struct Transaction (nếu cần)
- [ ] **Bước 3:** Tạo file dữ liệu CSV mẫu
- [ ] **Bước 4:** Copy hàm ReadCSV, đổi tên biến
- [ ] **Bước 5:** Copy hàm Update, đổi logic nghiệp vụ
- [ ] **Bước 6:** Copy hàm ParseDate, IsEarlier (nếu cần)
- [ ] **Bước 7:** Copy hàm Log
- [ ] **Bước 8:** Copy template main(), điều chỉnh
- [ ] **Bước 9:** Test với dữ liệu mẫu
- [ ] **Bước 10:** Thêm validation & error handling

---

## PHẦN VII: BÀI TẬP VÀ VÍ DỤ

### Bài tập 1: Quản lý Sinh viên

**Yêu cầu:**
- Đọc danh sách sinh viên từ `SinhVien.txt` (maSV, hoTen, diem)
- Tìm kiếm theo mã SV hoặc xếp loại
- Cập nhật điểm
- Kiểm tra đạt/không đạt (điểm >= 5)

**Gợi ý:**
```cpp
struct SinhVien {
    string maSV;      // ← tenSach
    string hoTen;
    int diem;         // ← soLuongSach
};

// Sử dụng lại:
// - Hàm ReadCSV (đổi delimiter nếu cần)
// - Hàm Update (cập nhật điểm)
// - Logic kiểm tra: diem >= 5
```

### Bài tập 2: Quản lý Kho hàng

**Yêu cầu:**
- Đọc danh sách sản phẩm từ `SanPham.txt`
- Xuất kho (giảm số lượng)
- Nhập kho (tăng số lượng)
- Cảnh báo hết hàng (số lượng <= 10)

**Gợi ý:**
```cpp
struct SanPham {
    string maSP;
    string tenSP;
    int soLuongKho;
};

// Logic:
// Xuất kho: arr[i].soLuongKho -= amount;
// Nhập kho: arr[i].soLuongKho += amount;
// Cảnh báo: if (arr[i].soLuongKho <= 10) ...
```

---

## PHỤ LỤC

### A. Bảng tra cứu nhanh

**Các lỗi thường gặp:**

| Lỗi | Nguyên nhân | Cách sửa |
|-----|-------------|----------|
| Ghi file toàn rác | `dem = maxSize` | `dem = 0` |
| Cập nhật tất cả | Thiếu `break` | Thêm `break` sau `if` |
| File not found | Sai working directory | Thêm fallback `"../file"` |
| Convert lỗi | String không phải số | Thêm try-catch |
| Ngày sai | Quên `+1`, `+1900` | Xem bảng `tm` struct |

**Headers cần thiết:**
```cpp
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>   // cout, cin
#include <fstream>    // ifstream, ofstream
#include <string>     // string
#include <stdexcept>  // runtime_error
#include <ctime>      // time, localtime
using namespace std;
```

---

## KẾT LUẬN

Giáo trình này đã trình bày:
1. ✅ Mô hình dữ liệu tổng quát (Entity + Transaction)
2. ✅ Các thuật toán cơ bản (Read, Parse, Update, Write)
3. ✅ Xử lý ngày tháng (Parse, Compare, Current)
4. ✅ Logging & Error handling
5. ✅ Template áp dụng cho mọi dự án

**Nguyên tắc vàng:**
- 🔥 `dem = 0` khi khởi tạo
- 🔥 `break` sau khi tìm thấy
- 🔥 Ghi log mọi thứ
- 🔥 Try-catch cho I/O
- 🔥 Fallback khi mở file

---

*Giáo trình thực hành - Phiên bản 2025*
*Dựa trên bài toán thực tế: Quản lý Thư viện Sách*
*Áp dụng cho: Sinh viên, Kho hàng, Nhân viên, Dự án, v.v.*
