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

**Định nghĩa**: Che giấu thông tin bên trong object, chỉ cho phép truy cập qua các phương thức public.

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

**Lợi ích**:
- ✅ Bảo vệ dữ liệu khỏi truy cập trái phép
- ✅ Kiểm soát cách dữ liệu được thay đổi
- ✅ Dễ maintain và debug
- ✅ Tăng tính bảo mật

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

**Định nghĩa**: Ẩn đi chi tiết implementation, chỉ hiển thị những gì cần thiết.

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

**Lợi ích**:
- ✅ Giảm complexity
- ✅ Tập trung vào chức năng chính
- ✅ Dễ maintain
- ✅ Tăng tính bảo mật

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
