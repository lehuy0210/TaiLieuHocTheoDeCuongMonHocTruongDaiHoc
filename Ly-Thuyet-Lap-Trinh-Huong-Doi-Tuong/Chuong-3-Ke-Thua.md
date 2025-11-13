# CHƯƠNG 3: KẾ THỪA (INHERITANCE)

## 📚 Mục Lục

1. [Khái niệm kế thừa](#1-khái-niệm-kế-thừa)
2. [Phương thức khởi tạo trong quan hệ kế thừa](#2-phương-thức-khởi-tạo-trong-quan-hệ-kế-thừa)
3. [Ghi đè (Overriding)](#3-ghi-đè-overriding)
4. [Phạm vi truy cập protected](#4-phạm-vi-truy-cập-protected)
5. [Từ khoá super/base](#5-từ-khoá-superbase)
6. [Lớp Object](#6-lớp-object)
7. [Ký hiệu UML](#7-ký-hiệu-uml)

---

## 1. Khái niệm kế thừa

### 1.1. Kế thừa là gì?

**Kế thừa (Inheritance)** là khả năng một lớp (lớp con) kế thừa các thuộc tính và phương thức từ lớp khác (lớp cha).

**Thuật ngữ**:
- **Base Class / Parent Class / Super Class**: Lớp cha
- **Derived Class / Child Class / Sub Class**: Lớp con

**Ký hiệu UML**:
```
    ┌─────────────┐
    │   Animal    │
    │  (Lớp cha)  │
    └──────▲──────┘
           │
      ┌────┴────┐
      │         │
┌─────┴────┐ ┌──┴───────┐
│   Dog    │ │   Cat    │
│ (Lớp con)│ │(Lớp con) │
└──────────┘ └──────────┘
```

---

### 1.2. Tại sao sử dụng kế thừa?

**Lợi ích**:
- ✅ **Tái sử dụng code**: Không phải viết lại code giống nhau
- ✅ **Mở rộng dễ dàng**: Thêm tính năng mới mà không ảnh hưởng lớp cha
- ✅ **Tổ chức tốt**: Tạo hierarchy rõ ràng
- ✅ **Polymorphism**: Cơ sở cho tính đa hình

**Ví dụ thực tế**:
```
    Nhân Viên (Lớp cha)
         ↑
    ┌────┴────────┐
    │             │
Lập Trình Viên  Kế Toán
```

---

### 1.3. Kế thừa trong C++

**Cú pháp**:
```cpp
class BaseClass {
    // Base class members
};

class DerivedClass : access_specifier BaseClass {
    // Derived class members
};
```

**Ví dụ**:
```cpp
#include <iostream>
#include <string>
using namespace std;

// Lớp cha
class ConVat {
protected:  // Cho phép lớp con truy cập
    string ten;
    int tuoi;

public:
    ConVat(string t, int age) : ten(t), tuoi(age) {
        cout << "Constructor ConVat: " << ten << endl;
    }

    void an() {
        cout << ten << " dang an" << endl;
    }

    void ngu() {
        cout << ten << " dang ngu" << endl;
    }

    void hienThiThongTin() {
        cout << "Ten: " << ten << ", Tuoi: " << tuoi << endl;
    }
};

// Lớp con - Chó
class Cho : public ConVat {
private:
    string giong;

public:
    Cho(string t, int age, string g)
        : ConVat(t, age), giong(g) {
        cout << "Constructor Cho: " << t << endl;
    }

    void sua() {
        cout << ten << " sua: Gau gau!" << endl;
    }

    void batBong() {
        cout << ten << " dang bat bong" << endl;
    }

    void hienThiChiTiet() {
        hienThiThongTin();  // Từ lớp cha
        cout << "Giong: " << giong << endl;
    }
};

// Lớp con - Mèo
class Meo : public ConVat {
public:
    Meo(string t, int age) : ConVat(t, age) {
        cout << "Constructor Meo: " << t << endl;
    }

    void keu() {
        cout << ten << " keu: Meo meo!" << endl;
    }

    void baoMong() {
        cout << ten << " dang bao mong" << endl;
    }
};

int main() {
    cout << "=== Tao doi tuong Cho ===" << endl;
    Cho cho("Buddy", 3, "Golden Retriever");

    // Sử dụng methods từ lớp cha
    cho.an();
    cho.ngu();

    // Sử dụng methods từ lớp con
    cho.sua();
    cho.batBong();
    cho.hienThiChiTiet();

    cout << "\n=== Tao doi tuong Meo ===" << endl;
    Meo meo("Kitty", 2);

    meo.an();    // Từ lớp cha
    meo.keu();   // Từ lớp con
    meo.baoMong(); // Từ lớp con

    return 0;
}
```

**Output**:
```
=== Tao doi tuong Cho ===
Constructor ConVat: Buddy
Constructor Cho: Buddy
Buddy dang an
Buddy dang ngu
Buddy sua: Gau gau!
Buddy dang bat bong
Ten: Buddy, Tuoi: 3
Giong: Golden Retriever

=== Tao doi tuong Meo ===
Constructor ConVat: Kitty
Constructor Meo: Kitty
Kitty dang an
Kitty keu: Meo meo!
Kitty dang bao mong
```

---

### 1.4. Kế thừa trong C#

**Cú pháp**:
```csharp
class BaseClass {
    // Base class members
}

class DerivedClass : BaseClass {
    // Derived class members
}
```

**Ví dụ**:
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
        Console.WriteLine($"Constructor ConVat: {ten}");
    }

    public void An()
    {
        Console.WriteLine($"{ten} dang an");
    }

    public void Ngu()
    {
        Console.WriteLine($"{ten} dang ngu");
    }

    public void HienThiThongTin()
    {
        Console.WriteLine($"Ten: {ten}, Tuoi: {tuoi}");
    }
}

// Lớp con - Chó
class Cho : ConVat
{
    private string giong;

    public Cho(string t, int age, string g)
        : base(t, age)
    {
        giong = g;
        Console.WriteLine($"Constructor Cho: {t}");
    }

    public void Sua()
    {
        Console.WriteLine($"{ten} sua: Gau gau!");
    }

    public void BatBong()
    {
        Console.WriteLine($"{ten} dang bat bong");
    }

    public void HienThiChiTiet()
    {
        HienThiThongTin();  // Từ lớp cha
        Console.WriteLine($"Giong: {giong}");
    }
}

// Lớp con - Mèo
class Meo : ConVat
{
    public Meo(string t, int age) : base(t, age)
    {
        Console.WriteLine($"Constructor Meo: {t}");
    }

    public void Keu()
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
        Console.WriteLine("=== Tao doi tuong Cho ===");
        Cho cho = new Cho("Buddy", 3, "Golden Retriever");

        // Sử dụng methods từ lớp cha
        cho.An();
        cho.Ngu();

        // Sử dụng methods từ lớp con
        cho.Sua();
        cho.BatBong();
        cho.HienThiChiTiet();

        Console.WriteLine("\n=== Tao doi tuong Meo ===");
        Meo meo = new Meo("Kitty", 2);

        meo.An();    // Từ lớp cha
        meo.Keu();   // Từ lớp con
        meo.BaoMong(); // Từ lớp con
    }
}
```

---

### 1.5. Access Specifiers trong kế thừa C++

```cpp
// Public inheritance - Phổ biến nhất
class Derived : public Base {
    // public -> public
    // protected -> protected
    // private -> không truy cập được
};

// Protected inheritance
class Derived : protected Base {
    // public -> protected
    // protected -> protected
    // private -> không truy cập được
};

// Private inheritance
class Derived : private Base {
    // public -> private
    // protected -> private
    // private -> không truy cập được
};
```

**Bảng so sánh**:

| Base Class Member | Public Inheritance | Protected Inheritance | Private Inheritance |
|-------------------|--------------------|-----------------------|---------------------|
| `public` | `public` | `protected` | `private` |
| `protected` | `protected` | `protected` | `private` |
| `private` | ❌ Not accessible | ❌ Not accessible | ❌ Not accessible |

**Lưu ý**: Trong C#, mặc định và duy nhất là **public inheritance**.

---

## 2. Phương thức khởi tạo trong quan hệ kế thừa

### 2.1. Thứ tự gọi Constructor

**Thứ tự**:
1. Constructor của lớp cha được gọi trước
2. Constructor của lớp con được gọi sau

**Thứ tự gọi Destructor (C++)**: Ngược lại
1. Destructor của lớp con được gọi trước
2. Destructor của lớp cha được gọi sau

---

### 2.2. Constructor trong C++

```cpp
#include <iostream>
#include <string>
using namespace std;

class NhanVien {
protected:
    string hoTen;
    int tuoi;
    double luongCoBan;

public:
    NhanVien() {
        cout << "Constructor NhanVien (default)" << endl;
        hoTen = "";
        tuoi = 0;
        luongCoBan = 0;
    }

    NhanVien(string ten, int age, double luong)
        : hoTen(ten), tuoi(age), luongCoBan(luong) {
        cout << "Constructor NhanVien: " << hoTen << endl;
    }

    ~NhanVien() {
        cout << "Destructor NhanVien: " << hoTen << endl;
    }

    void hienThiThongTin() {
        cout << "Ten: " << hoTen << ", Tuoi: " << tuoi
             << ", Luong: " << luongCoBan << endl;
    }
};

class LapTrinhVien : public NhanVien {
private:
    string ngonNgu;
    int namKinhNghiem;

public:
    // Constructor - gọi constructor lớp cha
    LapTrinhVien(string ten, int age, double luong,
                 string lang, int exp)
        : NhanVien(ten, age, luong),  // Gọi constructor cha
          ngonNgu(lang),
          namKinhNghiem(exp) {
        cout << "Constructor LapTrinhVien: " << ten << endl;
    }

    ~LapTrinhVien() {
        cout << "Destructor LapTrinhVien: " << hoTen << endl;
    }

    void hienThiChiTiet() {
        hienThiThongTin();
        cout << "Ngon ngu: " << ngonNgu
             << ", Kinh nghiem: " << namKinhNghiem << " nam" << endl;
    }

    double tinhLuong() {
        return luongCoBan + (namKinhNghiem * 1000000);
    }
};

int main() {
    cout << "=== Tao doi tuong ===" << endl;
    LapTrinhVien ltv("Nguyen Van A", 25, 10000000, "C++", 3);

    cout << "\n=== Su dung doi tuong ===" << endl;
    ltv.hienThiChiTiet();
    cout << "Luong thuc te: " << ltv.tinhLuong() << endl;

    cout << "\n=== Ket thuc ===" << endl;
    return 0;
}
```

**Output**:
```
=== Tao doi tuong ===
Constructor NhanVien: Nguyen Van A
Constructor LapTrinhVien: Nguyen Van A

=== Su dung doi tuong ===
Ten: Nguyen Van A, Tuoi: 25, Luong: 10000000
Ngon ngu: C++, Kinh nghiem: 3 nam
Luong thuc te: 13000000

=== Ket thuc ===
Destructor LapTrinhVien: Nguyen Van A
Destructor NhanVien: Nguyen Van A
```

---

### 2.3. Constructor trong C#

```csharp
using System;

class NhanVien
{
    protected string hoTen;
    protected int tuoi;
    protected double luongCoBan;

    public NhanVien()
    {
        Console.WriteLine("Constructor NhanVien (default)");
        hoTen = "";
        tuoi = 0;
        luongCoBan = 0;
    }

    public NhanVien(string ten, int age, double luong)
    {
        hoTen = ten;
        tuoi = age;
        luongCoBan = luong;
        Console.WriteLine($"Constructor NhanVien: {hoTen}");
    }

    ~NhanVien()
    {
        Console.WriteLine($"Destructor NhanVien: {hoTen}");
    }

    public void HienThiThongTin()
    {
        Console.WriteLine($"Ten: {hoTen}, Tuoi: {tuoi}, Luong: {luongCoBan}");
    }
}

class LapTrinhVien : NhanVien
{
    private string ngonNgu;
    private int namKinhNghiem;

    // Constructor - gọi constructor lớp cha bằng base()
    public LapTrinhVien(string ten, int age, double luong,
                        string lang, int exp)
        : base(ten, age, luong)  // Gọi constructor cha
    {
        ngonNgu = lang;
        namKinhNghiem = exp;
        Console.WriteLine($"Constructor LapTrinhVien: {ten}");
    }

    ~LapTrinhVien()
    {
        Console.WriteLine($"Destructor LapTrinhVien: {hoTen}");
    }

    public void HienThiChiTiet()
    {
        HienThiThongTin();
        Console.WriteLine($"Ngon ngu: {ngonNgu}, Kinh nghiem: {namKinhNghiem} nam");
    }

    public double TinhLuong()
    {
        return luongCoBan + (namKinhNghiem * 1000000);
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("=== Tao doi tuong ===");
        LapTrinhVien ltv = new LapTrinhVien("Nguyen Van A", 25, 10000000, "C#", 3);

        Console.WriteLine("\n=== Su dung doi tuong ===");
        ltv.HienThiChiTiet();
        Console.WriteLine($"Luong thuc te: {ltv.TinhLuong()}");

        Console.WriteLine("\n=== Ket thuc ===");
    }
}
```

---

## 3. Ghi đè (Overriding)

### 3.1. Khái niệm

**Ghi đè (Overriding)** là việc lớp con định nghĩa lại phương thức của lớp cha.

**Phân biệt**:
- **Overloading**: Cùng tên, khác tham số (compile-time)
- **Overriding**: Cùng tên, cùng tham số (runtime)

---

### 3.2. Overriding trong C++

**Sử dụng từ khóa**:
- `virtual`: Khai báo method có thể override (trong base class)
- `override`: Đánh dấu method đang override (trong derived class)

```cpp
#include <iostream>
#include <string>
using namespace std;

class HinhHoc {
protected:
    string ten;

public:
    HinhHoc(string t) : ten(t) {}

    // Virtual method - có thể override
    virtual double tinhDienTich() {
        return 0;
    }

    virtual double tinhChuVi() {
        return 0;
    }

    virtual void hienThi() {
        cout << "Hinh: " << ten << endl;
    }

    // Virtual destructor - quan trọng!
    virtual ~HinhHoc() {
        cout << "Destructor HinhHoc: " << ten << endl;
    }
};

class HinhTron : public HinhHoc {
private:
    double banKinh;

public:
    HinhTron(double r) : HinhHoc("Hinh tron"), banKinh(r) {}

    // Override methods
    double tinhDienTich() override {
        return 3.14159 * banKinh * banKinh;
    }

    double tinhChuVi() override {
        return 2 * 3.14159 * banKinh;
    }

    void hienThi() override {
        HinhHoc::hienThi();  // Gọi method của lớp cha
        cout << "Ban kinh: " << banKinh << endl;
        cout << "Dien tich: " << tinhDienTich() << endl;
        cout << "Chu vi: " << tinhChuVi() << endl;
    }

    ~HinhTron() {
        cout << "Destructor HinhTron" << endl;
    }
};

class HinhChuNhat : public HinhHoc {
private:
    double dai, rong;

public:
    HinhChuNhat(double d, double r)
        : HinhHoc("Hinh chu nhat"), dai(d), rong(r) {}

    double tinhDienTich() override {
        return dai * rong;
    }

    double tinhChuVi() override {
        return 2 * (dai + rong);
    }

    void hienThi() override {
        HinhHoc::hienThi();
        cout << "Dai: " << dai << ", Rong: " << rong << endl;
        cout << "Dien tich: " << tinhDienTich() << endl;
        cout << "Chu vi: " << tinhChuVi() << endl;
    }

    ~HinhChuNhat() {
        cout << "Destructor HinhChuNhat" << endl;
    }
};

int main() {
    // Polymorphism - sử dụng base class pointer
    HinhHoc* hinh1 = new HinhTron(5);
    HinhHoc* hinh2 = new HinhChuNhat(4, 6);

    cout << "=== Hinh 1 ===" << endl;
    hinh1->hienThi();
    cout << "\nDien tich: " << hinh1->tinhDienTich() << endl;

    cout << "\n=== Hinh 2 ===" << endl;
    hinh2->hienThi();
    cout << "\nDien tich: " << hinh2->tinhDienTich() << endl;

    // Cleanup
    cout << "\n=== Cleanup ===" << endl;
    delete hinh1;
    delete hinh2;

    return 0;
}
```

**Lưu ý quan trọng**:
- ✅ Phải khai báo `virtual` trong base class
- ✅ Nên dùng `override` trong derived class (C++11)
- ✅ Base class destructor phải là `virtual`

---

### 3.3. Overriding trong C#

**Sử dụng từ khóa**:
- `virtual`: Khai báo method có thể override (trong base class)
- `override`: Override method (trong derived class)
- `sealed`: Ngăn override tiếp (trong derived class)

```csharp
using System;

class HinhHoc
{
    protected string ten;

    public HinhHoc(string t)
    {
        ten = t;
    }

    // Virtual method - có thể override
    public virtual double TinhDienTich()
    {
        return 0;
    }

    public virtual double TinhChuVi()
    {
        return 0;
    }

    public virtual void HienThi()
    {
        Console.WriteLine($"Hinh: {ten}");
    }
}

class HinhTron : HinhHoc
{
    private double banKinh;

    public HinhTron(double r) : base("Hinh tron")
    {
        banKinh = r;
    }

    // Override methods
    public override double TinhDienTich()
    {
        return Math.PI * banKinh * banKinh;
    }

    public override double TinhChuVi()
    {
        return 2 * Math.PI * banKinh;
    }

    public override void HienThi()
    {
        base.HienThi();  // Gọi method của lớp cha
        Console.WriteLine($"Ban kinh: {banKinh}");
        Console.WriteLine($"Dien tich: {TinhDienTich():F2}");
        Console.WriteLine($"Chu vi: {TinhChuVi():F2}");
    }
}

class HinhChuNhat : HinhHoc
{
    private double dai, rong;

    public HinhChuNhat(double d, double r) : base("Hinh chu nhat")
    {
        dai = d;
        rong = r;
    }

    public override double TinhDienTich()
    {
        return dai * rong;
    }

    public override double TinhChuVi()
    {
        return 2 * (dai + rong);
    }

    // Sealed override - không thể override thêm
    public sealed override void HienThi()
    {
        base.HienThi();
        Console.WriteLine($"Dai: {dai}, Rong: {rong}");
        Console.WriteLine($"Dien tich: {TinhDienTich():F2}");
        Console.WriteLine($"Chu vi: {TinhChuVi():F2}");
    }
}

class Program
{
    static void Main()
    {
        // Polymorphism - sử dụng base class reference
        HinhHoc hinh1 = new HinhTron(5);
        HinhHoc hinh2 = new HinhChuNhat(4, 6);

        Console.WriteLine("=== Hinh 1 ===");
        hinh1.HienThi();
        Console.WriteLine($"\nDien tich: {hinh1.TinhDienTich():F2}");

        Console.WriteLine("\n=== Hinh 2 ===");
        hinh2.HienThi();
        Console.WriteLine($"\nDien tich: {hinh2.TinhDienTich():F2}");
    }
}
```

---

### 3.4. Phân biệt Override vs Hide

**C++ - Name Hiding**:
```cpp
class Base {
public:
    void show() {
        cout << "Base::show()" << endl;
    }
};

class Derived : public Base {
public:
    void show() {  // Hiding, not overriding
        cout << "Derived::show()" << endl;
    }
};

int main() {
    Derived d;
    d.show();  // Derived::show()

    Base* b = &d;
    b->show();  // Base::show() - không phải polymorphism

    return 0;
}
```

**C# - new vs override**:
```csharp
class Base
{
    public virtual void Show()
    {
        Console.WriteLine("Base::Show()");
    }
}

class Derived1 : Base
{
    // Override - polymorphism
    public override void Show()
    {
        Console.WriteLine("Derived1::Show()");
    }
}

class Derived2 : Base
{
    // Hide - không phải polymorphism
    public new void Show()
    {
        Console.WriteLine("Derived2::Show()");
    }
}

class Program
{
    static void Main()
    {
        Base b1 = new Derived1();
        b1.Show();  // Derived1::Show() - polymorphism

        Base b2 = new Derived2();
        b2.Show();  // Base::Show() - không phải polymorphism
    }
}
```

---

## 4. Phạm vi truy cập protected

### 4.1. Khái niệm

`protected` cho phép:
- ✅ Truy cập trong class
- ✅ Truy cập trong derived class
- ❌ Không truy cập từ bên ngoài

**So sánh với private và public**:

| Access Modifier | Same Class | Derived Class | Outside |
|-----------------|------------|---------------|---------|
| `private` | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ |

---

### 4.2. Ví dụ protected trong C++

```cpp
#include <iostream>
#include <string>
using namespace std;

class TaiKhoan {
private:
    string matKhau;  // Chỉ class này truy cập được

protected:
    string soTaiKhoan;  // Class này và derived class
    double soDu;

public:
    string tenChuTK;  // Mọi nơi đều truy cập được

    TaiKhoan(string stk, string ten, double so, string mk)
        : soTaiKhoan(stk), tenChuTK(ten), soDu(so), matKhau(mk) {}

    void hienThiThongTin() {
        cout << "So TK: " << soTaiKhoan << endl;
        cout << "Chu TK: " << tenChuTK << endl;
        cout << "So du: " << soDu << endl;
        // Có thể truy cập matKhau ở đây
    }

private:
    bool kiemTraMatKhau(string mk) {
        return matKhau == mk;
    }
};

class TaiKhoanTietKiem : public TaiKhoan {
private:
    double laiSuat;

public:
    TaiKhoanTietKiem(string stk, string ten, double so, string mk, double ls)
        : TaiKhoan(stk, ten, so, mk), laiSuat(ls) {}

    void tinhLai() {
        // Có thể truy cập soTaiKhoan và soDu (protected)
        double tienLai = soDu * laiSuat / 100;
        cout << "Tai khoan " << soTaiKhoan << endl;
        cout << "Tien lai: " << tienLai << endl;

        // Không thể truy cập matKhau (private)
        // cout << matKhau;  // ERROR!
    }

    void capNhatLaiSuat(double ls) {
        laiSuat = ls;
        // Có thể đọc/ghi soDu (protected)
        soDu += soDu * laiSuat / 100;
    }
};

int main() {
    TaiKhoanTietKiem tk("123456", "Nguyen Van A", 10000000, "secret123", 5.0);

    // Truy cập public member
    cout << "Chu TK: " << tk.tenChuTK << endl;

    // Không thể truy cập protected
    // cout << tk.soTaiKhoan;  // ERROR!
    // cout << tk.soDu;        // ERROR!

    tk.hienThiThongTin();
    tk.tinhLai();

    return 0;
}
```

---

### 4.3. Ví dụ protected trong C#

```csharp
using System;

class TaiKhoan
{
    private string matKhau;  // Chỉ class này

    protected string soTaiKhoan;  // Class này và derived class
    protected double soDu;

    public string TenChuTK { get; set; }  // Mọi nơi

    public TaiKhoan(string stk, string ten, double so, string mk)
    {
        soTaiKhoan = stk;
        TenChuTK = ten;
        soDu = so;
        matKhau = mk;
    }

    public void HienThiThongTin()
    {
        Console.WriteLine($"So TK: {soTaiKhoan}");
        Console.WriteLine($"Chu TK: {TenChuTK}");
        Console.WriteLine($"So du: {soDu}");
        // Có thể truy cập matKhau ở đây
    }

    private bool KiemTraMatKhau(string mk)
    {
        return matKhau == mk;
    }
}

class TaiKhoanTietKiem : TaiKhoan
{
    private double laiSuat;

    public TaiKhoanTietKiem(string stk, string ten, double so, string mk, double ls)
        : base(stk, ten, so, mk)
    {
        laiSuat = ls;
    }

    public void TinhLai()
    {
        // Có thể truy cập soTaiKhoan và soDu (protected)
        double tienLai = soDu * laiSuat / 100;
        Console.WriteLine($"Tai khoan {soTaiKhoan}");
        Console.WriteLine($"Tien lai: {tienLai}");

        // Không thể truy cập matKhau (private)
        // Console.WriteLine(matKhau);  // ERROR!
    }

    public void CapNhatLaiSuat(double ls)
    {
        laiSuat = ls;
        // Có thể đọc/ghi soDu (protected)
        soDu += soDu * laiSuat / 100;
    }
}

class Program
{
    static void Main()
    {
        TaiKhoanTietKiem tk = new TaiKhoanTietKiem(
            "123456", "Nguyen Van A", 10000000, "secret123", 5.0);

        // Truy cập public member
        Console.WriteLine($"Chu TK: {tk.TenChuTK}");

        // Không thể truy cập protected
        // Console.WriteLine(tk.soTaiKhoan);  // ERROR!
        // Console.WriteLine(tk.soDu);        // ERROR!

        tk.HienThiThongTin();
        tk.TinhLai();
    }
}
```

---

## 5. Từ khoá super/base

### 5.1. Khái niệm

Từ khóa để truy cập members của lớp cha:
- **C++**: Sử dụng `BaseClass::`
- **C#**: Sử dụng `base`

**Công dụng**:
- Gọi constructor của lớp cha
- Truy cập method/property của lớp cha
- Tránh name hiding

---

### 5.2. Sử dụng trong C++

```cpp
#include <iostream>
#include <string>
using namespace std;

class Nguoi {
protected:
    string hoTen;
    int tuoi;

public:
    Nguoi(string ten, int age) : hoTen(ten), tuoi(age) {
        cout << "Constructor Nguoi" << endl;
    }

    void gioi Thieu() {
        cout << "Xin chao, toi la " << hoTen << endl;
    }

    void hienThiThongTin() {
        cout << "Ho ten: " << hoTen << ", Tuoi: " << tuoi << endl;
    }
};

class SinhVien : public Nguoi {
private:
    string maSV;
    double diemTB;

public:
    SinhVien(string ten, int age, string ma, double diem)
        : Nguoi(ten, age),  // Gọi constructor lớp cha
          maSV(ma), diemTB(diem) {
        cout << "Constructor SinhVien" << endl;
    }

    // Override method
    void hienThiThongTin() {
        // Gọi method của lớp cha
        Nguoi::hienThiThongTin();

        // Thêm thông tin riêng
        cout << "Ma SV: " << maSV << ", Diem TB: " << diemTB << endl;
    }

    void gioiThieuDayDu() {
        // Gọi method lớp cha
        Nguoi::gioiThieu();

        // Truy cập member lớp cha
        cout << "Toi la sinh vien, ma so: " << maSV << endl;
        cout << "Tuoi cua toi: " << Nguoi::tuoi << endl;  // Rõ ràng
        cout << "Tuoi cua toi: " << tuoi << endl;  // Cũng được
    }
};

int main() {
    SinhVien sv("Nguyen Van A", 20, "SV001", 8.5);

    sv.hienThiThongTin();
    cout << endl;
    sv.gioiThieuDayDu();

    return 0;
}
```

---

### 5.3. Sử dụng trong C#

```csharp
using System;

class Nguoi
{
    protected string hoTen;
    protected int tuoi;

    public Nguoi(string ten, int age)
    {
        hoTen = ten;
        tuoi = age;
        Console.WriteLine("Constructor Nguoi");
    }

    public void GioiThieu()
    {
        Console.WriteLine($"Xin chao, toi la {hoTen}");
    }

    public virtual void HienThiThongTin()
    {
        Console.WriteLine($"Ho ten: {hoTen}, Tuoi: {tuoi}");
    }
}

class SinhVien : Nguoi
{
    private string maSV;
    private double diemTB;

    public SinhVien(string ten, int age, string ma, double diem)
        : base(ten, age)  // Gọi constructor lớp cha
    {
        maSV = ma;
        diemTB = diem;
        Console.WriteLine("Constructor SinhVien");
    }

    // Override method
    public override void HienThiThongTin()
    {
        // Gọi method của lớp cha
        base.HienThiThongTin();

        // Thêm thông tin riêng
        Console.WriteLine($"Ma SV: {maSV}, Diem TB: {diemTB}");
    }

    public void GioiThieuDayDu()
    {
        // Gọi method lớp cha
        base.GioiThieu();

        // Truy cập member lớp cha
        Console.WriteLine($"Toi la sinh vien, ma so: {maSV}");
        Console.WriteLine($"Tuoi cua toi: {tuoi}");
    }
}

class Program
{
    static void Main()
    {
        SinhVien sv = new SinhVien("Nguyen Van A", 20, "SV001", 8.5);

        sv.HienThiThongTin();
        Console.WriteLine();
        sv.GioiThieuDayDu();
    }
}
```

---

## 6. Lớp Object

### 6.1. Trong C++

C++ không có lớp Object base tự động. Nhưng có thể tự định nghĩa:

```cpp
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

// Tự định nghĩa base class như Object
class Object {
public:
    virtual ~Object() {}

    virtual string toString() {
        ostringstream oss;
        oss << "Object@" << this;
        return oss.str();
    }

    virtual bool equals(const Object& obj) {
        return this == &obj;
    }
};

class Person : public Object {
private:
    string name;
    int age;

public:
    Person(string n, int a) : name(n), age(a) {}

    string toString() override {
        return "Person{name: " + name + ", age: " + to_string(age) + "}";
    }

    bool equals(const Object& obj) override {
        const Person* p = dynamic_cast<const Person*>(&obj);
        if (p == nullptr) return false;
        return name == p->name && age == p->age;
    }
};

int main() {
    Person p1("John", 25);
    Person p2("John", 25);

    cout << p1.toString() << endl;
    cout << "p1 equals p2: " << (p1.equals(p2) ? "true" : "false") << endl;

    return 0;
}
```

---

### 6.2. Trong C#

Tất cả các class trong C# tự động kế thừa từ `System.Object`.

**Methods của Object class**:
- `ToString()`: Trả về string representation
- `Equals()`: So sánh 2 objects
- `GetHashCode()`: Trả về hash code
- `GetType()`: Trả về Type của object

```csharp
using System;

class Person
{
    private string name;
    private int age;

    public Person(string n, int a)
    {
        name = n;
        age = a;
    }

    // Override ToString()
    public override string ToString()
    {
        return $"Person{{name: {name}, age: {age}}}";
    }

    // Override Equals()
    public override bool Equals(object obj)
    {
        if (obj == null || GetType() != obj.GetType())
            return false;

        Person p = (Person)obj;
        return name == p.name && age == p.age;
    }

    // Override GetHashCode()
    public override int GetHashCode()
    {
        return HashCode.Combine(name, age);
    }
}

class Program
{
    static void Main()
    {
        Person p1 = new Person("John", 25);
        Person p2 = new Person("John", 25);
        Person p3 = new Person("Jane", 30);

        // ToString()
        Console.WriteLine(p1.ToString());  // Person{name: John, age: 25}

        // Equals()
        Console.WriteLine($"p1 equals p2: {p1.Equals(p2)}");  // True
        Console.WriteLine($"p1 equals p3: {p1.Equals(p3)}");  // False

        // GetType()
        Console.WriteLine($"Type: {p1.GetType().Name}");  // Person

        // GetHashCode()
        Console.WriteLine($"HashCode: {p1.GetHashCode()}");
    }
}
```

---

## 7. Ký hiệu UML

### 7.1. Inheritance trong UML

**Ký hiệu**: Mũi tên tam giác rỗng từ lớp con đến lớp cha

```
        ┌──────────────────┐
        │   ConVat         │
        ├──────────────────┤
        │ # ten: string    │
        │ # tuoi: int      │
        ├──────────────────┤
        │ + an()           │
        │ + ngu()          │
        └────────▲─────────┘
                 │
         ┌───────┴───────┐
         │               │
┌────────┴────────┐ ┌────┴──────────┐
│     Cho         │ │     Meo       │
├─────────────────┤ ├───────────────┤
│ - giong: string │ │               │
├─────────────────┤ ├───────────────┤
│ + sua()         │ │ + keu()       │
│ + batBong()     │ │ + baoMong()   │
└─────────────────┘ └───────────────┘
```

---

### 7.2. Ví dụ UML đầy đủ

```
┌─────────────────────────────┐
│ <<abstract>>                │
│      HinhHoc                │
├─────────────────────────────┤
│ # ten: string               │
├─────────────────────────────┤
│ + HinhHoc(ten)              │
│ + tinhDienTich(): double    │
│   {abstract}                │
│ + tinhChuVi(): double       │
│   {abstract}                │
│ + hienThi()                 │
│   {virtual}                 │
└────────────▲────────────────┘
             │
      ┌──────┴──────┐
      │             │
┌─────┴─────────┐ ┌─┴───────────────┐
│  HinhTron     │ │ HinhChuNhat     │
├───────────────┤ ├─────────────────┤
│ - banKinh: d  │ │ - dai: double   │
│               │ │ - rong: double  │
├───────────────┤ ├─────────────────┤
│ + HinhTron(r) │ │ + HinhChuNhat() │
│ + tinhDienT() │ │ + tinhDienTich()│
│ + tinhChuVi() │ │ + tinhChuVi()   │
│ + hienThi()   │ │ + hienThi()     │
└───────────────┘ └─────────────────┘
```

---

## 📝 Tóm tắt Chương 3

### Các điểm chính:

1. **Kế thừa (Inheritance)**:
   - Lớp con kế thừa từ lớp cha
   - Tái sử dụng code hiệu quả
   - Tạo hierarchy rõ ràng

2. **Constructor & Destructor**:
   - Constructor cha được gọi trước con
   - Destructor con được gọi trước cha
   - Sử dụng initializer list (C++) hoặc base() (C#)

3. **Overriding**:
   - Lớp con định nghĩa lại method của cha
   - Sử dụng `virtual` và `override`
   - Virtual destructor quan trọng (C++)

4. **Protected**:
   - Truy cập trong class và derived class
   - Không truy cập từ bên ngoài

5. **base/super**:
   - Truy cập members của lớp cha
   - Gọi constructor lớp cha

### Bài tập:

1. Tạo lớp `NhanVien` và các lớp con `LapTrinhVien`, `KeToan`, `QuanLy`
2. Implement hierarchy `PhuongTien` -> `XeHoi`, `XeMay`, `XeDap`
3. Override methods `toString()` và `equals()` cho các lớp
4. Vẽ UML cho hệ thống quản lý sinh viên với inheritance
5. So sánh overloading vs overriding với ví dụ cụ thể

---

**Chương tiếp theo**: [Chương 4: Đa Hình](Chuong-4-Da-Hinh.md)
