# CHƯƠNG 1: TỔNG QUAN LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG

## 📚 Mục Lục

1. [Giới thiệu các phương pháp lập trình](#1-giới-thiệu-các-phương-pháp-lập-trình)
2. [Các đặc điểm của lập trình hướng đối tượng](#2-các-đặc-điểm-của-lập-trình-hướng-đối-tượng)
3. [Giới thiệu ngôn ngữ UML](#3-giới-thiệu-ngôn-ngữ-uml)
4. [Giới thiệu các ngôn ngữ lập trình hướng đối tượng](#4-giới-thiệu-các-ngôn-ngữ-lập-trình-hướng-đối-tượng)
5. [Lập trình C++ và C# căn bản](#5-lập-trình-c-và-c-căn-bản)

---

## 1. Giới thiệu các phương pháp lập trình

### 1.1. Lập trình tuyến tính (Linear Programming)

**Định nghĩa**: Chương trình được viết theo trình tự từ trên xuống dưới, thực hiện tuần tự các câu lệnh.

**Đặc điểm**:
- Code được viết liên tục không có cấu trúc
- Sử dụng câu lệnh GOTO để nhảy giữa các đoạn code
- Khó đọc, khó bảo trì
- Chỉ phù hợp với chương trình nhỏ

**Ví dụ**:
```basic
10 PRINT "Nhap so a:"
20 INPUT A
30 PRINT "Nhap so b:"
40 INPUT B
50 C = A + B
60 PRINT "Tong = "; C
70 END
```

**Nhược điểm**:
- ❌ Khó hiểu với chương trình lớn
- ❌ Khó bảo trì và mở rộng
- ❌ Code bị lặp lại nhiều
- ❌ Khó tìm lỗi

---

### 1.2. Lập trình thủ tục / Lập trình cấu trúc (Procedural Programming)

**Định nghĩa**: Chương trình được chia thành các hàm/thủ tục độc lập, mỗi hàm thực hiện một nhiệm vụ cụ thể.

**Đặc điểm**:
- Chia chương trình thành các hàm nhỏ
- Tái sử dụng code thông qua các hàm
- Cấu trúc rõ ràng hơn lập trình tuyến tính
- Data và functions tách biệt

**Ví dụ C++**:
```cpp
#include <iostream>
using namespace std;

// Hàm nhập số
int nhapSo(string thongBao) {
    int so;
    cout << thongBao;
    cin >> so;
    return so;
}

// Hàm tính tổng
int tinhTong(int a, int b) {
    return a + b;
}

// Hàm in kết quả
void inKetQua(int tong) {
    cout << "Tong = " << tong << endl;
}

int main() {
    int a = nhapSo("Nhap so a: ");
    int b = nhapSo("Nhap so b: ");
    int tong = tinhTong(a, b);
    inKetQua(tong);
    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;

class Program
{
    // Hàm nhập số
    static int NhapSo(string thongBao)
    {
        Console.Write(thongBao);
        return int.Parse(Console.ReadLine());
    }

    // Hàm tính tổng
    static int TinhTong(int a, int b)
    {
        return a + b;
    }

    // Hàm in kết quả
    static void InKetQua(int tong)
    {
        Console.WriteLine($"Tong = {tong}");
    }

    static void Main()
    {
        int a = NhapSo("Nhap so a: ");
        int b = NhapSo("Nhap so b: ");
        int tong = TinhTong(a, b);
        InKetQua(tong);
    }
}
```

**Ưu điểm**:
- ✅ Dễ đọc, dễ hiểu hơn
- ✅ Tái sử dụng code qua functions
- ✅ Dễ tìm và sửa lỗi
- ✅ Phù hợp với chương trình vừa và nhỏ

**Nhược điểm**:
- ❌ Data và functions vẫn tách biệt
- ❌ Khó quản lý với chương trình lớn
- ❌ Khó mô phỏng thế giới thực

---

### 1.3. Lập trình module (Modular Programming)

**Định nghĩa**: Chương trình được chia thành các module độc lập, mỗi module chứa các functions liên quan.

**Đặc điểm**:
- Chia chương trình thành các module/file riêng biệt
- Mỗi module có trách nhiệm riêng
- Dễ làm việc nhóm
- Tăng tính tái sử dụng

**Ví dụ cấu trúc C++**:
```
Project/
├── main.cpp
├── MathUtils.h
├── MathUtils.cpp
├── InputUtils.h
└── InputUtils.cpp
```

**MathUtils.h**:
```cpp
#ifndef MATHUTILS_H
#define MATHUTILS_H

int tinhTong(int a, int b);
int tinhHieu(int a, int b);
int tinhTich(int a, int b);
double tinhThuong(int a, int b);

#endif
```

**MathUtils.cpp**:
```cpp
#include "MathUtils.h"

int tinhTong(int a, int b) {
    return a + b;
}

int tinhHieu(int a, int b) {
    return a - b;
}

int tinhTich(int a, int b) {
    return a * b;
}

double tinhThuong(int a, int b) {
    if (b == 0) return 0;
    return (double)a / b;
}
```

**Ví dụ cấu trúc C#**:
```
Project/
├── Program.cs
├── MathUtils.cs
└── InputUtils.cs
```

**MathUtils.cs**:
```csharp
namespace Calculator
{
    public static class MathUtils
    {
        public static int TinhTong(int a, int b) => a + b;
        public static int TinhHieu(int a, int b) => a - b;
        public static int TinhTich(int a, int b) => a * b;
        public static double TinhThuong(int a, int b) => b == 0 ? 0 : (double)a / b;
    }
}
```

**Ưu điểm**:
- ✅ Tổ chức code tốt hơn
- ✅ Dễ làm việc nhóm
- ✅ Tái sử dụng module
- ✅ Dễ bảo trì

**Nhược điểm**:
- ❌ Vẫn chưa mô phỏng tốt thế giới thực
- ❌ Data và behavior vẫn tách biệt

---

### 1.4. Lập trình hướng đối tượng (Object-Oriented Programming)

**Định nghĩa**: Phương pháp lập trình dựa trên khái niệm "đối tượng", kết hợp data (thuộc tính) và behavior (phương thức) vào một đơn vị.

**Khái niệm cơ bản**:
- **Lớp (Class)**: Bản thiết kế để tạo đối tượng
- **Đối tượng (Object)**: Thực thể cụ thể được tạo từ lớp
- **Thuộc tính (Attributes)**: Dữ liệu của đối tượng
- **Phương thức (Methods)**: Hành vi của đối tượng

**Ví dụ C++**:
```cpp
#include <iostream>
#include <string>
using namespace std;

// Định nghĩa lớp
class SinhVien {
private:
    string maSV;
    string hoTen;
    int tuoi;
    double diemTB;

public:
    // Constructor
    SinhVien(string ma, string ten, int t, double diem) {
        maSV = ma;
        hoTen = ten;
        tuoi = t;
        diemTB = diem;
    }

    // Phương thức
    void hienThiThongTin() {
        cout << "Ma SV: " << maSV << endl;
        cout << "Ho ten: " << hoTen << endl;
        cout << "Tuoi: " << tuoi << endl;
        cout << "Diem TB: " << diemTB << endl;
    }

    string xepLoai() {
        if (diemTB >= 8.5) return "Gioi";
        if (diemTB >= 7.0) return "Kha";
        if (diemTB >= 5.5) return "Trung binh";
        return "Yeu";
    }
};

int main() {
    // Tạo đối tượng
    SinhVien sv1("SV001", "Nguyen Van A", 20, 8.5);
    SinhVien sv2("SV002", "Tran Thi B", 21, 7.2);

    // Sử dụng đối tượng
    sv1.hienThiThongTin();
    cout << "Xep loai: " << sv1.xepLoai() << endl;
    cout << "\n";

    sv2.hienThiThongTin();
    cout << "Xep loai: " << sv2.xepLoai() << endl;

    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;

// Định nghĩa lớp
class SinhVien
{
    // Thuộc tính
    private string maSV;
    private string hoTen;
    private int tuoi;
    private double diemTB;

    // Constructor
    public SinhVien(string ma, string ten, int t, double diem)
    {
        maSV = ma;
        hoTen = ten;
        tuoi = t;
        diemTB = diem;
    }

    // Phương thức
    public void HienThiThongTin()
    {
        Console.WriteLine($"Ma SV: {maSV}");
        Console.WriteLine($"Ho ten: {hoTen}");
        Console.WriteLine($"Tuoi: {tuoi}");
        Console.WriteLine($"Diem TB: {diemTB}");
    }

    public string XepLoai()
    {
        if (diemTB >= 8.5) return "Gioi";
        if (diemTB >= 7.0) return "Kha";
        if (diemTB >= 5.5) return "Trung binh";
        return "Yeu";
    }
}

class Program
{
    static void Main()
    {
        // Tạo đối tượng
        SinhVien sv1 = new SinhVien("SV001", "Nguyen Van A", 20, 8.5);
        SinhVien sv2 = new SinhVien("SV002", "Tran Thi B", 21, 7.2);

        // Sử dụng đối tượng
        sv1.HienThiThongTin();
        Console.WriteLine($"Xep loai: {sv1.XepLoai()}");
        Console.WriteLine();

        sv2.HienThiThongTin();
        Console.WriteLine($"Xep loai: {sv2.XepLoai()}");
    }
}
```

**Ưu điểm**:
- ✅ Mô phỏng tốt thế giới thực
- ✅ Data và behavior gắn liền nhau
- ✅ Dễ bảo trì và mở rộng
- ✅ Tái sử dụng code cao
- ✅ Bảo mật tốt (encapsulation)
- ✅ Phù hợp với dự án lớn

---

### 1.5. So sánh các phương pháp lập trình

| Tiêu chí | Procedural | Modular | OOP |
|----------|-----------|---------|-----|
| **Tổ chức code** | Functions | Modules | Classes & Objects |
| **Data & Functions** | Tách biệt | Tách biệt | Gắn liền |
| **Tái sử dụng** | Thấp | Trung bình | Cao |
| **Bảo mật** | Thấp | Trung bình | Cao |
| **Mở rộng** | Khó | Trung bình | Dễ |
| **Dự án lớn** | Không phù hợp | Trung bình | Rất phù hợp |
| **Mô phỏng thực tế** | Kém | Trung bình | Tốt |

---

## 2. Các đặc điểm của lập trình hướng đối tượng

### 2.1. Tính đóng gói (Encapsulation)

**Định nghĩa**:
Tính đóng gói là cơ chế gói gọn dữ liệu (thuộc tính) và các phương thức xử lý dữ liệu đó vào bên trong một đơn vị duy nhất (class), đồng thời che giấu thông tin bên trong object và chỉ cho phép truy cập thông qua các phương thức public được định nghĩa sẵn.

**Mục đích chính**:
1. **Information Hiding (Che giấu thông tin)**: Ẩn các chi tiết cài đặt nội bộ
2. **Data Protection (Bảo vệ dữ liệu)**: Ngăn chặn truy cập và thay đổi dữ liệu trái phép
3. **Controlled Access (Kiểm soát truy cập)**: Chỉ cho phép thao tác với dữ liệu qua các phương thức được kiểm soát
4. **Maintainability (Dễ bảo trì)**: Có thể thay đổi cài đặt bên trong mà không ảnh hưởng code bên ngoài

**Nguyên tắc**:
- Các thuộc tính (fields) nên được khai báo `private` hoặc `protected`
- Cung cấp các phương thức `public` (getter/setter) để truy cập dữ liệu
- Kiểm tra tính hợp lệ của dữ liệu trong setter
- Chỉ public những gì thực sự cần thiết

**Access Modifiers trong C++**:
```cpp
public:     // Truy cập từ mọi nơi
private:    // Chỉ truy cập trong class
protected:  // Truy cập trong class và class con
```

**Access Modifiers trong C#**:
```csharp
public          // Truy cập từ mọi nơi
private         // Chỉ truy cập trong class
protected       // Truy cập trong class và class con
internal        // Truy cập trong cùng assembly
protected internal  // Kết hợp protected và internal
private protected   // Kết hợp private và protected (C# 7.2+)
```

**Ví dụ C++**:
```cpp
#include <iostream>
#include <string>
using namespace std;

class TaiKhoanNganHang {
private:
    string soTaiKhoan;
    double soDu;

public:
    // Constructor
    TaiKhoanNganHang(string stk, double soDuBanDau) {
        soTaiKhoan = stk;
        if (soDuBanDau >= 0)
            soDu = soDuBanDau;
        else
            soDu = 0;
    }

    // Getter
    double getSoDu() const {
        return soDu;
    }

    // Phương thức nạp tiền
    void napTien(double soTien) {
        if (soTien > 0) {
            soDu += soTien;
            cout << "Nap " << soTien << " thanh cong. So du: " << soDu << endl;
        } else {
            cout << "So tien khong hop le!" << endl;
        }
    }

    // Phương thức rút tiền
    bool rutTien(double soTien) {
        if (soTien <= 0) {
            cout << "So tien khong hop le!" << endl;
            return false;
        }
        if (soTien > soDu) {
            cout << "So du khong du!" << endl;
            return false;
        }
        soDu -= soTien;
        cout << "Rut " << soTien << " thanh cong. So du: " << soDu << endl;
        return true;
    }
};

int main() {
    TaiKhoanNganHang tk("123456", 1000000);

    tk.napTien(500000);
    tk.rutTien(200000);
    cout << "So du hien tai: " << tk.getSoDu() << endl;

    // Không thể truy cập trực tiếp
    // tk.soDu = -1000000; // ERROR: private

    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;

class TaiKhoanNganHang
{
    // Private fields
    private string soTaiKhoan;
    private double soDu;

    // Constructor
    public TaiKhoanNganHang(string stk, double soDuBanDau)
    {
        soTaiKhoan = stk;
        soDu = soDuBanDau >= 0 ? soDuBanDau : 0;
    }

    // Property (getter)
    public double SoDu
    {
        get { return soDu; }
    }

    // Phương thức nạp tiền
    public void NapTien(double soTien)
    {
        if (soTien > 0)
        {
            soDu += soTien;
            Console.WriteLine($"Nap {soTien} thanh cong. So du: {soDu}");
        }
        else
        {
            Console.WriteLine("So tien khong hop le!");
        }
    }

    // Phương thức rút tiền
    public bool RutTien(double soTien)
    {
        if (soTien <= 0)
        {
            Console.WriteLine("So tien khong hop le!");
            return false;
        }
        if (soTien > soDu)
        {
            Console.WriteLine("So du khong du!");
            return false;
        }
        soDu -= soTien;
        Console.WriteLine($"Rut {soTien} thanh cong. So du: {soDu}");
        return true;
    }
}

class Program
{
    static void Main()
    {
        TaiKhoanNganHang tk = new TaiKhoanNganHang("123456", 1000000);

        tk.NapTien(500000);
        tk.RutTien(200000);
        Console.WriteLine($"So du hien tai: {tk.SoDu}");

        // Không thể truy cập trực tiếp
        // tk.soDu = -1000000; // ERROR: private
    }
}
```

**Ví dụ về Getter/Setter với Validation**:

**C++ - Sử dụng Getter/Setter**:
```cpp
#include <iostream>
#include <string>
using namespace std;

class SinhVien {
private:
    string maSV;
    string hoTen;
    int tuoi;
    double diemTB;

public:
    // Constructor
    SinhVien(string ma, string ten, int t, double diem) {
        maSV = ma;
        hoTen = ten;
        setTuoi(t);      // Sử dụng setter để validate
        setDiemTB(diem); // Sử dụng setter để validate
    }

    // Getter methods
    string getMaSV() const { return maSV; }
    string getHoTen() const { return hoTen; }
    int getTuoi() const { return tuoi; }
    double getDiemTB() const { return diemTB; }

    // Setter với validation
    void setTuoi(int t) {
        if (t >= 18 && t <= 100) {
            tuoi = t;
        } else {
            cout << "Tuoi khong hop le! Gan gia tri mac dinh 18." << endl;
            tuoi = 18;
        }
    }

    void setDiemTB(double diem) {
        if (diem >= 0 && diem <= 10) {
            diemTB = diem;
        } else {
            cout << "Diem khong hop le! Gan gia tri mac dinh 0." << endl;
            diemTB = 0;
        }
    }

    void hienThi() const {
        cout << "Ma SV: " << maSV << endl;
        cout << "Ho ten: " << hoTen << endl;
        cout << "Tuoi: " << tuoi << endl;
        cout << "Diem TB: " << diemTB << endl;
    }
};

int main() {
    SinhVien sv("SV001", "Nguyen Van A", 20, 8.5);
    sv.hienThi();

    // Thay đổi thông qua setter
    sv.setTuoi(22);
    sv.setDiemTB(9.0);

    cout << "\nSau khi cap nhat:" << endl;
    sv.hienThi();

    // Thử set giá trị không hợp lệ
    sv.setTuoi(200);    // Sẽ báo lỗi
    sv.setDiemTB(15);   // Sẽ báo lỗi

    return 0;
}
```

**C# - Sử dụng Properties (Auto-Property và Full Property)**:
```csharp
using System;

class SinhVien
{
    // Auto-implemented property (getter và setter tự động)
    public string MaSV { get; set; }
    public string HoTen { get; set; }

    // Full property với validation
    private int tuoi;
    public int Tuoi
    {
        get { return tuoi; }
        set
        {
            if (value >= 18 && value <= 100)
                tuoi = value;
            else
            {
                Console.WriteLine("Tuoi khong hop le! Gan gia tri mac dinh 18.");
                tuoi = 18;
            }
        }
    }

    // Property với backing field và validation
    private double diemTB;
    public double DiemTB
    {
        get => diemTB;
        set
        {
            if (value >= 0 && value <= 10)
                diemTB = value;
            else
            {
                Console.WriteLine("Diem khong hop le! Gan gia tri mac dinh 0.");
                diemTB = 0;
            }
        }
    }

    // Read-only property
    public string XepLoai
    {
        get
        {
            if (diemTB >= 8.5) return "Gioi";
            if (diemTB >= 7.0) return "Kha";
            if (diemTB >= 5.5) return "Trung binh";
            return "Yeu";
        }
    }

    // Constructor
    public SinhVien(string ma, string ten, int t, double diem)
    {
        MaSV = ma;
        HoTen = ten;
        Tuoi = t;      // Sử dụng property để validate
        DiemTB = diem; // Sử dụng property để validate
    }

    public void HienThi()
    {
        Console.WriteLine($"Ma SV: {MaSV}");
        Console.WriteLine($"Ho ten: {HoTen}");
        Console.WriteLine($"Tuoi: {Tuoi}");
        Console.WriteLine($"Diem TB: {DiemTB}");
        Console.WriteLine($"Xep loai: {XepLoai}");
    }
}

class Program
{
    static void Main()
    {
        SinhVien sv = new SinhVien("SV001", "Nguyen Van A", 20, 8.5);
        sv.HienThi();

        Console.WriteLine("\nSau khi cap nhat:");
        sv.Tuoi = 22;
        sv.DiemTB = 9.0;
        sv.HienThi();

        // Thử set giá trị không hợp lệ
        sv.Tuoi = 200;    // Sẽ báo lỗi
        sv.DiemTB = 15;   // Sẽ báo lỗi
    }
}
```

**Ví dụ thực tế - Quản lý Email**:
```csharp
using System;
using System.Text.RegularExpressions;

class User
{
    private string email;

    public string Email
    {
        get => email;
        set
        {
            // Validate email format
            string pattern = @"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$";
            if (Regex.IsMatch(value, pattern))
                email = value;
            else
                throw new ArgumentException("Email khong hop le!");
        }
    }

    private string password;

    // Write-only property (chỉ set, không get)
    public string Password
    {
        set
        {
            if (value.Length >= 8)
                password = HashPassword(value); // Mã hóa password
            else
                throw new ArgumentException("Password phai co it nhat 8 ky tu!");
        }
    }

    private string HashPassword(string pwd)
    {
        // Simplified - trong thực tế dùng bcrypt, SHA256, etc.
        return Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes(pwd));
    }

    public bool VerifyPassword(string inputPassword)
    {
        return HashPassword(inputPassword) == password;
    }
}
```

**Lợi ích**:
- ✅ **Bảo vệ dữ liệu**: Ngăn chặn truy cập trái phép và đảm bảo tính toàn vẹn dữ liệu
- ✅ **Kiểm soát thay đổi**: Validate dữ liệu trước khi cập nhật
- ✅ **Dễ maintain**: Thay đổi implementation mà không ảnh hưởng code bên ngoài
- ✅ **Tăng bảo mật**: Ẩn các chi tiết nhạy cảm (password, số thẻ tín dụng, etc.)
- ✅ **Flexibility**: Có thể thêm logic xử lý trong getter/setter sau này
- ✅ **Debugging dễ dàng**: Có thể đặt breakpoint trong setter để track thay đổi

**Best Practices**:
1. ✅ Luôn khai báo fields là `private`
2. ✅ Cung cấp getter/setter hoặc properties public khi cần
3. ✅ Validate dữ liệu trong setter
4. ✅ Sử dụng const/readonly cho dữ liệu không đổi
5. ✅ Không trả về reference đến mutable object từ getter
6. ✅ Sử dụng properties (C#) thay vì getter/setter methods

---

### 2.2. Tính kế thừa (Inheritance)

**Định nghĩa**: Class con kế thừa thuộc tính và phương thức từ class cha.

**Ví dụ C++**:
```cpp
#include <iostream>
#include <string>
using namespace std;

// Lớp cha
class ConVat {
protected:
    string ten;
    int tuoi;

public:
    ConVat(string t, int age) : ten(t), tuoi(age) {}

    virtual void phatRa() {
        cout << ten << " phat ra tieng keu" << endl;
    }

    void ngu() {
        cout << ten << " dang ngu" << endl;
    }
};

// Lớp con - Chó
class Cho : public ConVat {
private:
    string giong;

public:
    Cho(string t, int age, string g) : ConVat(t, age), giong(g) {}

    void phatRa() override {
        cout << ten << " sua: Gau gau!" << endl;
    }

    void batBong() {
        cout << ten << " dang bat bong" << endl;
    }
};

// Lớp con - Mèo
class Meo : public ConVat {
public:
    Meo(string t, int age) : ConVat(t, age) {}

    void phatRa() override {
        cout << ten << " keu: Meo meo!" << endl;
    }

    void baoMong() {
        cout << ten << " dang bao mong" << endl;
    }
};

int main() {
    Cho cho("Buddy", 3, "Golden Retriever");
    Meo meo("Kitty", 2);

    cho.phatRa();      // Buddy sua: Gau gau!
    cho.ngu();         // Buddy dang ngu
    cho.batBong();     // Buddy dang bat bong

    meo.phatRa();      // Kitty keu: Meo meo!
    meo.ngu();         // Kitty dang ngu
    meo.baoMong();     // Kitty dang bao mong

    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;

// Lớp cha
class ConVat
{
    protected string ten;
    protected int tuoi;

    public ConVat(string t, int age)
    {
        ten = t;
        tuoi = age;
    }

    public virtual void PhatRa()
    {
        Console.WriteLine($"{ten} phat ra tieng keu");
    }

    public void Ngu()
    {
        Console.WriteLine($"{ten} dang ngu");
    }
}

// Lớp con - Chó
class Cho : ConVat
{
    private string giong;

    public Cho(string t, int age, string g) : base(t, age)
    {
        giong = g;
    }

    public override void PhatRa()
    {
        Console.WriteLine($"{ten} sua: Gau gau!");
    }

    public void BatBong()
    {
        Console.WriteLine($"{ten} dang bat bong");
    }
}

// Lớp con - Mèo
class Meo : ConVat
{
    public Meo(string t, int age) : base(t, age) { }

    public override void PhatRa()
    {
        Console.WriteLine($"{ten} keu: Meo meo!");
    }

    public void BaoMong()
    {
        Console.WriteLine($"{ten} dang bao mong");
    }
}

class Program
{
    static void Main()
    {
        Cho cho = new Cho("Buddy", 3, "Golden Retriever");
        Meo meo = new Meo("Kitty", 2);

        cho.PhatRa();      // Buddy sua: Gau gau!
        cho.Ngu();         // Buddy dang ngu
        cho.BatBong();     // Buddy dang bat bong

        meo.PhatRa();      // Kitty keu: Meo meo!
        meo.Ngu();         // Kitty dang ngu
        meo.BaoMong();     // Kitty dang bao mong
    }
}
```

**Lợi ích**:
- ✅ Tái sử dụng code
- ✅ Tạo hierarchy rõ ràng
- ✅ Dễ mở rộng chức năng
- ✅ Giảm duplicate code

---

### 2.3. Tính đa hình (Polymorphism)

**Định nghĩa**: Một method có thể có nhiều hình thái khác nhau.

**Compile-time Polymorphism (Method Overloading)**:

**Ví dụ C++**:
```cpp
#include <iostream>
using namespace std;

class MayTinh {
public:
    // Overloading - cùng tên, khác tham số
    int cong(int a, int b) {
        return a + b;
    }

    double cong(double a, double b) {
        return a + b;
    }

    int cong(int a, int b, int c) {
        return a + b + c;
    }
};

int main() {
    MayTinh mt;
    cout << mt.cong(5, 3) << endl;           // 8
    cout << mt.cong(5.5, 3.2) << endl;       // 8.7
    cout << mt.cong(1, 2, 3) << endl;        // 6
    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;

class MayTinh
{
    // Overloading
    public int Cong(int a, int b) => a + b;

    public double Cong(double a, double b) => a + b;

    public int Cong(int a, int b, int c) => a + b + c;
}

class Program
{
    static void Main()
    {
        MayTinh mt = new MayTinh();
        Console.WriteLine(mt.Cong(5, 3));           // 8
        Console.WriteLine(mt.Cong(5.5, 3.2));       // 8.7
        Console.WriteLine(mt.Cong(1, 2, 3));        // 6
    }
}
```

**Runtime Polymorphism (Method Overriding)**:

**Ví dụ C++**:
```cpp
#include <iostream>
#include <cmath>
using namespace std;

class HinhHoc {
public:
    virtual double tinhDienTich() {
        return 0;
    }

    virtual void ve() {
        cout << "Ve hinh" << endl;
    }
};

class HinhTron : public HinhHoc {
private:
    double banKinh;

public:
    HinhTron(double r) : banKinh(r) {}

    double tinhDienTich() override {
        return M_PI * banKinh * banKinh;
    }

    void ve() override {
        cout << "Ve hinh tron" << endl;
    }
};

class HinhChuNhat : public HinhHoc {
private:
    double rong, cao;

public:
    HinhChuNhat(double w, double h) : rong(w), cao(h) {}

    double tinhDienTich() override {
        return rong * cao;
    }

    void ve() override {
        cout << "Ve hinh chu nhat" << endl;
    }
};

int main() {
    HinhHoc* hinh1 = new HinhTron(5);
    HinhHoc* hinh2 = new HinhChuNhat(4, 6);

    hinh1->ve();
    cout << "Dien tich: " << hinh1->tinhDienTich() << endl;

    hinh2->ve();
    cout << "Dien tich: " << hinh2->tinhDienTich() << endl;

    delete hinh1;
    delete hinh2;

    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;

class HinhHoc
{
    public virtual double TinhDienTich()
    {
        return 0;
    }

    public virtual void Ve()
    {
        Console.WriteLine("Ve hinh");
    }
}

class HinhTron : HinhHoc
{
    private double banKinh;

    public HinhTron(double r)
    {
        banKinh = r;
    }

    public override double TinhDienTich()
    {
        return Math.PI * banKinh * banKinh;
    }

    public override void Ve()
    {
        Console.WriteLine("Ve hinh tron");
    }
}

class HinhChuNhat : HinhHoc
{
    private double rong, cao;

    public HinhChuNhat(double w, double h)
    {
        rong = w;
        cao = h;
    }

    public override double TinhDienTich()
    {
        return rong * cao;
    }

    public override void Ve()
    {
        Console.WriteLine("Ve hinh chu nhat");
    }
}

class Program
{
    static void Main()
    {
        HinhHoc hinh1 = new HinhTron(5);
        HinhHoc hinh2 = new HinhChuNhat(4, 6);

        hinh1.Ve();
        Console.WriteLine($"Dien tich: {hinh1.TinhDienTich()}");

        hinh2.Ve();
        Console.WriteLine($"Dien tich: {hinh2.TinhDienTich()}");
    }
}
```

**Lợi ích**:
- ✅ Code linh hoạt hơn
- ✅ Dễ mở rộng
- ✅ Giảm code duplication
- ✅ Tăng tính tái sử dụng

---

### 2.4. Tính trừu tượng (Abstraction)

**Định nghĩa**:
Tính trừu tượng là quá trình ẩn đi các chi tiết cài đặt phức tạp và chỉ hiển thị những chức năng thiết yếu cho người dùng. Abstraction tập trung vào **"cái gì"** (what) hơn là **"như thế nào"** (how).

**Mục đích chính**:
1. **Simplification (Đơn giản hóa)**: Giảm độ phức tạp bằng cách ẩn chi tiết không cần thiết
2. **Focus on Interface (Tập trung vào giao diện)**: Người dùng chỉ cần biết cách sử dụng, không cần biết cách hoạt động
3. **Reduce Complexity (Giảm phức tạp)**: Chia hệ thống lớn thành các phần nhỏ dễ quản lý
4. **Increase Flexibility (Tăng tính linh hoạt)**: Có thể thay đổi implementation mà không ảnh hưởng người dùng

**Phân biệt Abstraction vs Encapsulation**:

| Tiêu chí | Abstraction | Encapsulation |
|----------|-------------|---------------|
| **Mục đích** | Ẩn độ phức tạp | Che giấu dữ liệu |
| **Tập trung** | Interface/Behavior | Data protection |
| **Câu hỏi** | "Cái gì" được cung cấp? | "Làm sao" bảo vệ dữ liệu? |
| **Cài đặt** | Abstract class, Interface | Access modifiers (private/protected) |
| **Level** | Design level | Implementation level |
| **Ví dụ** | Remote TV chỉ có nút bấm | Private fields + Public methods |

**Ví dụ thực tế**:
- 🚗 **Lái xe**: Bạn chỉ cần biết ga/phanh/vô lăng (abstraction), không cần biết động cơ hoạt động ra sao
- 📱 **Smartphone**: Bạn chạm vào icon để mở app, không cần biết CPU xử lý như thế nào
- ☕ **Máy pha cà phê**: Bạn nhấn nút, không cần biết cách nó pha

**Cách thực hiện Abstraction**:
1. **Abstract Classes**: Lớp có ít nhất một phương thức thuần ảo (pure virtual)
2. **Interfaces**: Chỉ định nghĩa các method signature, không có implementation
3. **Polymorphism**: Cùng interface, khác implementation

**Ví dụ C++**:
```cpp
#include <iostream>
#include <string>
using namespace std;

// Abstract class
class PhuongTien {
protected:
    string hangSX;
    string mauXe;

public:
    PhuongTien(string hang, string mau) : hangSX(hang), mauXe(mau) {}

    // Pure virtual functions - bắt buộc override
    virtual void khongDong() = 0;
    virtual void dungLai() = 0;

    // Virtual function - có thể override
    virtual void bopCoi() {
        cout << "Beep beep!" << endl;
    }

    // Normal function
    void hienThiThongTin() {
        cout << "Hang: " << hangSX << ", Mau: " << mauXe << endl;
    }
};

class OTo : public PhuongTien {
private:
    int soCua;

public:
    OTo(string hang, string mau, int cua)
        : PhuongTien(hang, mau), soCua(cua) {}

    void khongDong() override {
        cout << "O to khoi dong" << endl;
    }

    void dungLai() override {
        cout << "O to dung lai" << endl;
    }
};

class XeMay : public PhuongTien {
public:
    XeMay(string hang, string mau) : PhuongTien(hang, mau) {}

    void khongDong() override {
        cout << "Xe may khoi dong" << endl;
    }

    void dungLai() override {
        cout << "Xe may dung lai" << endl;
    }

    void bopCoi() override {
        cout << "Beep beep beep!" << endl;
    }
};

int main() {
    // Không thể khởi tạo abstract class
    // PhuongTien pt; // ERROR

    OTo oto("Toyota", "Den", 4);
    XeMay xemay("Honda", "Do");

    oto.hienThiThongTin();
    oto.khongDong();
    oto.bopCoi();

    xemay.hienThiThongTin();
    xemay.khongDong();
    xemay.bopCoi();

    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;

// Abstract class
abstract class PhuongTien
{
    protected string hangSX;
    protected string mauXe;

    public PhuongTien(string hang, string mau)
    {
        hangSX = hang;
        mauXe = mau;
    }

    // Abstract methods - bắt buộc override
    public abstract void KhoiDong();
    public abstract void DungLai();

    // Virtual method - có thể override
    public virtual void BopCoi()
    {
        Console.WriteLine("Beep beep!");
    }

    // Normal method
    public void HienThiThongTin()
    {
        Console.WriteLine($"Hang: {hangSX}, Mau: {mauXe}");
    }
}

class OTo : PhuongTien
{
    private int soCua;

    public OTo(string hang, string mau, int cua)
        : base(hang, mau)
    {
        soCua = cua;
    }

    public override void KhoiDong()
    {
        Console.WriteLine("O to khoi dong");
    }

    public override void DungLai()
    {
        Console.WriteLine("O to dung lai");
    }
}

class XeMay : PhuongTien
{
    public XeMay(string hang, string mau) : base(hang, mau) { }

    public override void KhoiDong()
    {
        Console.WriteLine("Xe may khoi dong");
    }

    public override void DungLai()
    {
        Console.WriteLine("Xe may dung lai");
    }

    public override void BopCoi()
    {
        Console.WriteLine("Beep beep beep!");
    }
}

class Program
{
    static void Main()
    {
        // Không thể khởi tạo abstract class
        // PhuongTien pt = new PhuongTien(); // ERROR

        OTo oto = new OTo("Toyota", "Den", 4);
        XeMay xemay = new XeMay("Honda", "Do");

        oto.HienThiThongTin();
        oto.KhoiDong();
        oto.BopCoi();

        Console.WriteLine();

        xemay.HienThiThongTin();
        xemay.KhoiDong();
        xemay.BopCoi();
    }
}
```

**Ví dụ về Interface - Payment System**:

**C# - Interface Pattern**:
```csharp
using System;

// Interface định nghĩa "contract"
interface IPaymentMethod
{
    bool ProcessPayment(double amount);
    bool RefundPayment(double amount);
    string GetPaymentInfo();
}

// Implementation 1: Credit Card
class CreditCardPayment : IPaymentMethod
{
    private string cardNumber;
    private string cardHolder;

    public CreditCardPayment(string number, string holder)
    {
        cardNumber = number;
        cardHolder = holder;
    }

    public bool ProcessPayment(double amount)
    {
        Console.WriteLine($"Processing credit card payment: ${amount}");
        Console.WriteLine($"Card: {MaskCardNumber()}");
        // Logic xử lý thanh toán thẻ tín dụng
        return true;
    }

    public bool RefundPayment(double amount)
    {
        Console.WriteLine($"Refunding ${amount} to credit card");
        return true;
    }

    public string GetPaymentInfo()
    {
        return $"Credit Card ending in {cardNumber.Substring(cardNumber.Length - 4)}";
    }

    private string MaskCardNumber()
    {
        return "**** **** **** " + cardNumber.Substring(cardNumber.Length - 4);
    }
}

// Implementation 2: PayPal
class PayPalPayment : IPaymentMethod
{
    private string email;

    public PayPalPayment(string email)
    {
        this.email = email;
    }

    public bool ProcessPayment(double amount)
    {
        Console.WriteLine($"Processing PayPal payment: ${amount}");
        Console.WriteLine($"Account: {email}");
        // Logic xử lý thanh toán PayPal
        return true;
    }

    public bool RefundPayment(double amount)
    {
        Console.WriteLine($"Refunding ${amount} to PayPal account");
        return true;
    }

    public string GetPaymentInfo()
    {
        return $"PayPal: {email}";
    }
}

// Implementation 3: Bank Transfer
class BankTransferPayment : IPaymentMethod
{
    private string accountNumber;
    private string bankName;

    public BankTransferPayment(string account, string bank)
    {
        accountNumber = account;
        bankName = bank;
    }

    public bool ProcessPayment(double amount)
    {
        Console.WriteLine($"Processing bank transfer: ${amount}");
        Console.WriteLine($"Bank: {bankName}");
        Console.WriteLine($"Account: {accountNumber}");
        return true;
    }

    public bool RefundPayment(double amount)
    {
        Console.WriteLine($"Refunding ${amount} via bank transfer");
        return true;
    }

    public string GetPaymentInfo()
    {
        return $"Bank Transfer: {bankName} - {accountNumber}";
    }
}

// Class sử dụng abstraction
class PaymentProcessor
{
    public void ProcessOrder(IPaymentMethod paymentMethod, double amount)
    {
        Console.WriteLine($"\n=== Processing Order ===");
        Console.WriteLine($"Amount: ${amount}");
        Console.WriteLine($"Payment Method: {paymentMethod.GetPaymentInfo()}");

        if (paymentMethod.ProcessPayment(amount))
        {
            Console.WriteLine("Payment successful!");
        }
        else
        {
            Console.WriteLine("Payment failed!");
        }
    }
}

class Program
{
    static void Main()
    {
        PaymentProcessor processor = new PaymentProcessor();

        // Sử dụng các payment method khác nhau
        // Nhưng code xử lý giống nhau (abstraction)
        IPaymentMethod creditCard = new CreditCardPayment("1234567890123456", "John Doe");
        IPaymentMethod paypal = new PayPalPayment("john@example.com");
        IPaymentMethod bankTransfer = new BankTransferPayment("9876543210", "Vietcombank");

        processor.ProcessOrder(creditCard, 100.50);
        processor.ProcessOrder(paypal, 75.25);
        processor.ProcessOrder(bankTransfer, 200.00);
    }
}
```

**Ví dụ về Levels of Abstraction - Database Layer**:

```csharp
using System;
using System.Collections.Generic;

// Level 1: High-level abstraction (Interface)
interface IDataRepository<T>
{
    void Add(T item);
    T GetById(int id);
    List<T> GetAll();
    void Update(T item);
    void Delete(int id);
}

// Level 2: Abstract implementation
abstract class DatabaseRepository<T> : IDataRepository<T>
{
    protected string connectionString;

    public DatabaseRepository(string connString)
    {
        connectionString = connString;
    }

    // Abstract methods - phải implement
    public abstract void Add(T item);
    public abstract T GetById(int id);
    public abstract List<T> GetAll();
    public abstract void Update(T item);
    public abstract void Delete(int id);

    // Concrete methods - có implementation
    protected void LogOperation(string operation)
    {
        Console.WriteLine($"[{DateTime.Now}] Operation: {operation}");
    }
}

// Level 3: Concrete implementation
class SqlServerRepository<T> : DatabaseRepository<T>
{
    public SqlServerRepository(string connString) : base(connString) { }

    public override void Add(T item)
    {
        LogOperation($"Adding {typeof(T).Name} to SQL Server");
        // SQL Server specific implementation
        Console.WriteLine($"INSERT INTO {typeof(T).Name} ...");
    }

    public override T GetById(int id)
    {
        LogOperation($"Getting {typeof(T).Name} by ID: {id}");
        return default(T);
    }

    public override List<T> GetAll()
    {
        LogOperation($"Getting all {typeof(T).Name}");
        return new List<T>();
    }

    public override void Update(T item)
    {
        LogOperation($"Updating {typeof(T).Name}");
    }

    public override void Delete(int id)
    {
        LogOperation($"Deleting {typeof(T).Name} ID: {id}");
    }
}

class MongoDBRepository<T> : DatabaseRepository<T>
{
    public MongoDBRepository(string connString) : base(connString) { }

    public override void Add(T item)
    {
        LogOperation($"Adding {typeof(T).Name} to MongoDB");
        // MongoDB specific implementation
        Console.WriteLine($"db.{typeof(T).Name}.insertOne(...)");
    }

    public override T GetById(int id)
    {
        LogOperation($"Getting {typeof(T).Name} by ID: {id}");
        return default(T);
    }

    public override List<T> GetAll()
    {
        LogOperation($"Getting all {typeof(T).Name}");
        return new List<T>();
    }

    public override void Update(T item)
    {
        LogOperation($"Updating {typeof(T).Name}");
    }

    public override void Delete(int id)
    {
        LogOperation($"Deleting {typeof(T).Name} ID: {id}");
    }
}

// Business layer - chỉ biết đến interface
class UserService
{
    private IDataRepository<string> repository;

    public UserService(IDataRepository<string> repo)
    {
        repository = repo;
    }

    public void CreateUser(string user)
    {
        // Không quan tâm database nào được dùng
        repository.Add(user);
    }
}

class Program
{
    static void Main()
    {
        // Có thể switch database mà không thay đổi business logic
        IDataRepository<string> sqlRepo = new SqlServerRepository<string>("SqlConnection");
        IDataRepository<string> mongoRepo = new MongoDBRepository<string>("MongoConnection");

        UserService service1 = new UserService(sqlRepo);
        service1.CreateUser("John Doe");

        Console.WriteLine();

        UserService service2 = new UserService(mongoRepo);
        service2.CreateUser("Jane Smith");
    }
}
```

**Lợi ích**:
- ✅ **Giảm complexity**: Người dùng không cần biết chi tiết cài đặt
- ✅ **Tập trung vào chức năng**: Chỉ quan tâm đến "cái gì" chứ không phải "như thế nào"
- ✅ **Dễ maintain**: Thay đổi implementation không ảnh hưởng client code
- ✅ **Tăng tính bảo mật**: Ẩn các chi tiết nhạy cảm
- ✅ **Reusability**: Interface có thể tái sử dụng cho nhiều implementation
- ✅ **Testability**: Dễ dàng mock/stub cho unit testing
- ✅ **Flexibility**: Dễ dàng thêm implementation mới

**Best Practices**:
1. ✅ Định nghĩa interface rõ ràng và tối giản
2. ✅ Sử dụng abstract class khi cần chia sẻ code giữa các subclass
3. ✅ Sử dụng interface khi chỉ cần định nghĩa contract
4. ✅ Áp dụng "Program to an interface, not an implementation"
5. ✅ Giữ interface ổn định, tránh thay đổi thường xuyên
6. ✅ Sử dụng dependency injection để inject abstractions
7. ✅ Tách biệt abstraction level (high-level vs low-level)

**Khi nào dùng Abstract Class vs Interface**:

**Abstract Class** khi:
- Muốn chia sẻ code giữa các class liên quan
- Có common behavior cần implement
- Muốn định nghĩa non-public members

**Interface** khi:
- Muốn định nghĩa contract cho các class không liên quan
- Cần multiple inheritance (C# không hỗ trợ multiple class inheritance)
- Chỉ cần định nghĩa behavior, không cần implementation

---

## 3. Giới thiệu ngôn ngữ UML

### 3.1. UML là gì?

**UML (Unified Modeling Language)** là ngôn ngữ mô hình hóa thống nhất, được sử dụng để:
- Thiết kế hệ thống phần mềm
- Mô hình hóa các lớp và mối quan hệ
- Giao tiếp giữa các developer
- Tài liệu hóa hệ thống

### 3.2. Class Diagram (Sơ đồ lớp)

**Class Diagram** mô tả:
- Cấu trúc của các lớp
- Thuộc tính và phương thức
- Mối quan hệ giữa các lớp

**Ký hiệu**:
```
┌─────────────────────────┐
│      TênLớp             │
├─────────────────────────┤
│ - thuộcTínhPrivate      │
│ + thuộcTínhPublic       │
│ # thuộcTínhProtected    │
├─────────────────────────┤
│ + phươngThứcPublic()    │
│ - phươngThứcPrivate()   │
└─────────────────────────┘
```

**Ký hiệu access modifiers**:
- `+` : public
- `-` : private
- `#` : protected
- `~` : package/internal

**Ví dụ UML cho lớp SinhVien**:
```
┌─────────────────────────┐
│      SinhVien           │
├─────────────────────────┤
│ - maSV: string          │
│ - hoTen: string         │
│ - tuoi: int             │
│ - diemTB: double        │
├─────────────────────────┤
│ + SinhVien(...)         │
│ + hienThiThongTin()     │
│ + xepLoai(): string     │
└─────────────────────────┘
```

### 3.3. Các mối quan hệ trong UML

**1. Association (Quan hệ liên kết)**:
```
Lớp A ────────> Lớp B
```

**2. Aggregation (Quan hệ tổng hợp)**:
```
Lớp A ◇────────> Lớp B
```

**3. Composition (Quan hệ hợp thành)**:
```
Lớp A ◆────────> Lớp B
```

**4. Inheritance (Quan hệ kế thừa)**:
```
Lớp Con ──────▷ Lớp Cha
```

**5. Dependency (Quan hệ phụ thuộc)**:
```
Lớp A ········> Lớp B
```

---

## 4. Giới thiệu các ngôn ngữ lập trình hướng đối tượng

### 4.1. C++ (1985)

**Đặc điểm**:
- ✅ Hiệu suất cao, gần với phần cứng
- ✅ Hỗ trợ đa hình, kế thừa, trừu tượng
- ✅ Quản lý bộ nhớ thủ công (pointers)
- ✅ Multiple inheritance
- ❌ Phức tạp, dễ gặp lỗi
- ❌ Không có garbage collection

**Ứng dụng**:
- Game engine (Unreal Engine)
- System software
- Embedded systems
- High-performance applications

---

### 4.2. C# (2000)

**Đặc điểm**:
- ✅ Cú pháp đơn giản, dễ học
- ✅ Garbage collection tự động
- ✅ Hỗ trợ đầy đủ OOP
- ✅ Rich library (.NET Framework)
- ✅ Cross-platform (.NET Core)
- ❌ Phụ thuộc vào .NET Framework
- ❌ Hiệu suất thấp hơn C++

**Ứng dụng**:
- Desktop applications (WPF, WinForms)
- Web applications (ASP.NET)
- Game development (Unity)
- Mobile apps (Xamarin)

---

### 4.3. Java (1995)

**Đặc điểm**:
- ✅ Write once, run anywhere
- ✅ Garbage collection tự động
- ✅ Rich ecosystem
- ✅ Strong community
- ❌ Hiệu suất thấp hơn C++
- ❌ Cú pháp dài dòng

**Ứng dụng**:
- Enterprise applications
- Android development
- Web applications
- Backend services

---

### 4.4. Python (1991)

**Đặc điểm**:
- ✅ Cú pháp đơn giản, dễ học
- ✅ Dynamic typing
- ✅ Rich libraries
- ❌ Hiệu suất thấp
- ❌ OOP không bắt buộc

**Ứng dụng**:
- Data science
- Machine learning
- Web development
- Automation

---

### 4.5. So sánh C++ và C#

| Tiêu chí | C++ | C# |
|----------|-----|-----|
| **Năm ra đời** | 1985 | 2000 |
| **Platform** | Cross-platform | Windows, .NET Core |
| **Hiệu suất** | Rất cao | Cao |
| **Quản lý bộ nhớ** | Manual (pointers) | Automatic (GC) |
| **Cú pháp** | Phức tạp | Đơn giản |
| **Multiple inheritance** | Có | Không (chỉ interfaces) |
| **Ứng dụng** | Games, Systems | Desktop, Web, Games |
| **Độ khó** | Khó | Trung bình |

---

## 5. Lập trình C++ và C# căn bản

### 5.1. Cấu trúc chương trình C++

```cpp
#include <iostream>        // Thư viện I/O
#include <string>          // Thư viện string
using namespace std;       // Sử dụng namespace std

// Hàm main - điểm bắt đầu
int main() {
    // Khai báo biến
    int tuoi = 20;
    double diem = 8.5;
    string ten = "Nguyen Van A";

    // Xuất dữ liệu
    cout << "Ten: " << ten << endl;
    cout << "Tuoi: " << tuoi << endl;
    cout << "Diem: " << diem << endl;

    // Nhập dữ liệu
    cout << "Nhap tuoi: ";
    cin >> tuoi;

    // Cấu trúc điều khiển
    if (diem >= 8.0) {
        cout << "Gioi" << endl;
    } else if (diem >= 6.5) {
        cout << "Kha" << endl;
    } else {
        cout << "Trung binh" << endl;
    }

    // Vòng lặp
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    return 0;  // Trả về 0 = thành công
}
```

---

### 5.2. Cấu trúc chương trình C#

```csharp
using System;              // Thư viện cơ bản

namespace MyProgram        // Namespace
{
    // Class chứa hàm Main
    class Program
    {
        // Hàm Main - điểm bắt đầu
        static void Main()
        {
            // Khai báo biến
            int tuoi = 20;
            double diem = 8.5;
            string ten = "Nguyen Van A";

            // Xuất dữ liệu
            Console.WriteLine($"Ten: {ten}");
            Console.WriteLine($"Tuoi: {tuoi}");
            Console.WriteLine($"Diem: {diem}");

            // Nhập dữ liệu
            Console.Write("Nhap tuoi: ");
            tuoi = int.Parse(Console.ReadLine());

            // Cấu trúc điều khiển
            if (diem >= 8.0)
            {
                Console.WriteLine("Gioi");
            }
            else if (diem >= 6.5)
            {
                Console.WriteLine("Kha");
            }
            else
            {
                Console.WriteLine("Trung binh");
            }

            // Vòng lặp
            for (int i = 0; i < 5; i++)
            {
                Console.Write($"{i} ");
            }
            Console.WriteLine();
        }
    }
}
```

---

### 5.3. So sánh cú pháp C++ vs C#

| Tính năng | C++ | C# |
|-----------|-----|-----|
| **Include/Using** | `#include <iostream>` | `using System;` |
| **Namespace** | `using namespace std;` | `namespace MyApp` |
| **Xuất dữ liệu** | `cout << "Hello";` | `Console.WriteLine("Hello");` |
| **Nhập dữ liệu** | `cin >> x;` | `x = Console.ReadLine();` |
| **String** | `string s = "text";` | `string s = "text";` |
| **Array** | `int arr[5];` | `int[] arr = new int[5];` |
| **Class** | `class MyClass { };` | `class MyClass { }` |
| **Pointer** | `int* p = &x;` | Không có (unsafe) |
| **Memory** | Manual (new/delete) | Automatic (GC) |

---

## 📝 Tóm tắt Chương 1

### Các điểm chính:

1. **Phương pháp lập trình**:
   - Lập trình tuyến tính → Thủ tục → Module → OOP
   - OOP là phương pháp tốt nhất cho dự án lớn

2. **4 tính chất OOP**:
   - **Encapsulation**: Che giấu thông tin
   - **Inheritance**: Kế thừa từ lớp cha
   - **Polymorphism**: Nhiều hình thái
   - **Abstraction**: Trừu tượng hóa

3. **UML**: Ngôn ngữ mô hình hóa thống nhất

4. **Ngôn ngữ OOP**:
   - C++: Hiệu suất cao, phức tạp
   - C#: Đơn giản, .NET ecosystem

### Bài tập:

1. So sánh ưu nhược điểm của procedural programming và OOP
2. Vẽ class diagram cho lớp HocSinh với các thuộc tính và phương thức
3. Viết chương trình C++ và C# đơn giản nhập xuất thông tin sinh viên
4. Giải thích 4 tính chất của OOP bằng ví dụ thực tế

---

**Chương tiếp theo**: [Chương 2: Lớp và Đối Tượng](Chuong-2-Lop-Va-Doi-Tuong.md)
