# CHƯƠNG 2: LỚP VÀ ĐỐI TƯỢNG

## 📚 Mục Lục

1. [Lớp (Class)](#1-lớp-class)
2. [Đối tượng (Object)](#2-đối-tượng-object)
3. [Tham chiếu this / self](#3-tham-chiếu-this--self)
4. [Thành viên tĩnh (Static Members)](#4-thành-viên-tĩnh-static-members)
5. [Khối khởi động (Initialization Block)](#5-khối-khởi-động-initialization-block)
6. [Nạp chồng (Overloading)](#6-nạp-chồng-overloading)
7. [Gói (Package/Namespace)](#7-gói-packagenamespace)
8. [Quan hệ giữa lớp và đối tượng](#8-quan-hệ-giữa-lớp-và-đối-tượng)
9. [Quan hệ giữa hai lớp](#9-quan-hệ-giữa-hai-lớp)
10. [Lớp trong (Inner/Nested Class)](#10-lớp-trong-innernested-class)
11. [Xử lý ngoại lệ (Exception Handling)](#11-xử-lý-ngoại-lệ-exception-handling)
12. [Ký hiệu UML](#12-ký-hiệu-uml)

---

## 1. Lớp (Class)

### 1.1. Khái niệm

**Lớp (Class)** là bản thiết kế (blueprint) để tạo ra các đối tượng. Lớp định nghĩa:
- **Thuộc tính (Attributes)**: Dữ liệu của đối tượng
- **Phương thức (Methods)**: Hành vi của đối tượng

**Ví dụ thực tế**:
- Lớp `XeHoi` là bản thiết kế
- Các xe cụ thể (Toyota Camry, Honda Civic) là đối tượng

---

### 1.2. Khai báo lớp trong C++

```cpp
#include <iostream>
#include <string>
using namespace std;

class SinhVien {
private:  // Phạm vi truy cập
    // Thuộc tính (fields)
    string maSV;
    string hoTen;
    int namSinh;
    double diemTB;

public:
    // Constructor - hàm khởi tạo
    SinhVien() {
        maSV = "";
        hoTen = "";
        namSinh = 2000;
        diemTB = 0.0;
    }

    // Constructor có tham số
    SinhVien(string ma, string ten, int nam, double diem) {
        maSV = ma;
        hoTen = ten;
        namSinh = nam;
        diemTB = diem;
    }

    // Getter
    string getMaSV() const {
        return maSV;
    }

    string getHoTen() const {
        return hoTen;
    }

    double getDiemTB() const {
        return diemTB;
    }

    // Setter
    void setDiemTB(double diem) {
        if (diem >= 0 && diem <= 10) {
            diemTB = diem;
        }
    }

    // Phương thức
    void hienThiThongTin() const {
        cout << "Ma SV: " << maSV << endl;
        cout << "Ho ten: " << hoTen << endl;
        cout << "Nam sinh: " << namSinh << endl;
        cout << "Diem TB: " << diemTB << endl;
    }

    string xepLoai() const {
        if (diemTB >= 8.5) return "Gioi";
        if (diemTB >= 7.0) return "Kha";
        if (diemTB >= 5.5) return "Trung binh";
        return "Yeu";
    }

    // Destructor
    ~SinhVien() {
        cout << "Destructor called for " << hoTen << endl;
    }
};
```

---

### 1.3. Khai báo lớp trong C#

```csharp
using System;

class SinhVien
{
    // Thuộc tính (fields) - private
    private string maSV;
    private string hoTen;
    private int namSinh;
    private double diemTB;

    // Constructor mặc định
    public SinhVien()
    {
        maSV = "";
        hoTen = "";
        namSinh = 2000;
        diemTB = 0.0;
    }

    // Constructor có tham số
    public SinhVien(string ma, string ten, int nam, double diem)
    {
        maSV = ma;
        hoTen = ten;
        namSinh = nam;
        diemTB = diem;
    }

    // Properties (C# style)
    public string MaSV
    {
        get { return maSV; }
        set { maSV = value; }
    }

    public string HoTen
    {
        get { return hoTen; }
        set { hoTen = value; }
    }

    // Auto-implemented property
    public int NamSinh { get; set; }

    // Property với validation
    public double DiemTB
    {
        get { return diemTB; }
        set
        {
            if (value >= 0 && value <= 10)
                diemTB = value;
        }
    }

    // Phương thức
    public void HienThiThongTin()
    {
        Console.WriteLine($"Ma SV: {maSV}");
        Console.WriteLine($"Ho ten: {hoTen}");
        Console.WriteLine($"Nam sinh: {namSinh}");
        Console.WriteLine($"Diem TB: {diemTB}");
    }

    public string XepLoai()
    {
        if (diemTB >= 8.5) return "Gioi";
        if (diemTB >= 7.0) return "Kha";
        if (diemTB >= 5.5) return "Trung binh";
        return "Yeu";
    }

    // Destructor (Finalizer)
    ~SinhVien()
    {
        Console.WriteLine($"Destructor called for {hoTen}");
    }
}
```

---

### 1.4. Phạm vi truy cập (Access Modifiers)

**Trong C++**:
```cpp
class MyClass {
public:
    int publicVar;      // Truy cập từ mọi nơi
    void publicMethod() { }

protected:
    int protectedVar;   // Truy cập trong class và class con
    void protectedMethod() { }

private:
    int privateVar;     // Chỉ truy cập trong class
    void privateMethod() { }
};
```

**Trong C#**:
```csharp
class MyClass
{
    public int publicVar;           // Truy cập từ mọi nơi
    protected int protectedVar;     // Truy cập trong class và class con
    private int privateVar;         // Chỉ truy cập trong class
    internal int internalVar;       // Truy cập trong cùng assembly

    protected internal int protIntVar;  // protected OR internal
    private protected int privProtVar;  // protected AND internal (C# 7.2+)
}
```

**Bảng so sánh**:

| Access Modifier | C++ | C# | Mô tả |
|-----------------|-----|-----|-------|
| `public` | ✅ | ✅ | Truy cập từ mọi nơi |
| `private` | ✅ | ✅ | Chỉ trong class |
| `protected` | ✅ | ✅ | Class và class con |
| `internal` | ❌ | ✅ | Trong cùng assembly |
| `protected internal` | ❌ | ✅ | Protected hoặc Internal |
| `private protected` | ❌ | ✅ | Protected và Internal |

---

### 1.5. Phương thức getter và setter

**Mục đích**: Kiểm soát truy cập vào thuộc tính private

**C++ - Sử dụng hàm getter/setter**:
```cpp
class NhanVien {
private:
    string hoTen;
    double luong;

public:
    // Getter
    string getHoTen() const {
        return hoTen;
    }

    double getLuong() const {
        return luong;
    }

    // Setter với validation
    void setHoTen(string ten) {
        if (!ten.empty()) {
            hoTen = ten;
        }
    }

    void setLuong(double l) {
        if (l >= 0) {
            luong = l;
        }
    }
};
```

**C# - Sử dụng Properties**:
```csharp
class NhanVien
{
    private string hoTen;
    private double luong;

    // Property
    public string HoTen
    {
        get { return hoTen; }
        set
        {
            if (!string.IsNullOrEmpty(value))
                hoTen = value;
        }
    }

    public double Luong
    {
        get { return luong; }
        set
        {
            if (value >= 0)
                luong = value;
        }
    }

    // Auto-implemented property
    public string ChucVu { get; set; }

    // Read-only property
    public double ThuongNam
    {
        get { return luong * 0.1; }
    }

    // Expression-bodied property (C# 7.0+)
    public double LuongThucLinh => luong + ThuongNam;
}
```

---

### 1.6. Phương thức khởi tạo (Constructor)

**Constructor** là phương thức đặc biệt được gọi tự động khi tạo đối tượng.

**C++ - Constructor**:
```cpp
class HinhChuNhat {
private:
    double chieuDai;
    double chieuRong;

public:
    // Default constructor
    HinhChuNhat() {
        chieuDai = 0;
        chieuRong = 0;
        cout << "Default constructor called" << endl;
    }

    // Parameterized constructor
    HinhChuNhat(double dai, double rong) {
        chieuDai = dai;
        chieuRong = rong;
        cout << "Parameterized constructor called" << endl;
    }

    // Constructor với giá trị mặc định
    HinhChuNhat(double canh = 1) {
        chieuDai = chieuRong = canh;
    }

    // Copy constructor
    HinhChuNhat(const HinhChuNhat &h) {
        chieuDai = h.chieuDai;
        chieuRong = h.chieuRong;
        cout << "Copy constructor called" << endl;
    }

    double tinhDienTich() const {
        return chieuDai * chieuRong;
    }
};

int main() {
    HinhChuNhat h1;              // Default constructor
    HinhChuNhat h2(5, 3);        // Parameterized constructor
    HinhChuNhat h3(h2);          // Copy constructor
    HinhChuNhat h4 = h2;         // Copy constructor

    return 0;
}
```

**C# - Constructor**:
```csharp
class HinhChuNhat
{
    private double chieuDai;
    private double chieuRong;

    // Default constructor
    public HinhChuNhat()
    {
        chieuDai = 0;
        chieuRong = 0;
        Console.WriteLine("Default constructor called");
    }

    // Parameterized constructor
    public HinhChuNhat(double dai, double rong)
    {
        chieuDai = dai;
        chieuRong = rong;
        Console.WriteLine("Parameterized constructor called");
    }

    // Constructor với giá trị mặc định
    public HinhChuNhat(double canh = 1)
    {
        chieuDai = chieuRong = canh;
    }

    // Constructor chaining
    public HinhChuNhat(double dai) : this(dai, dai)
    {
        Console.WriteLine("Constructor chaining");
    }

    public double TinhDienTich()
    {
        return chieuDai * chieuRong;
    }
}

class Program
{
    static void Main()
    {
        HinhChuNhat h1 = new HinhChuNhat();        // Default
        HinhChuNhat h2 = new HinhChuNhat(5, 3);    // Parameterized
        HinhChuNhat h3 = new HinhChuNhat(4);       // Chaining
    }
}
```

---

## 2. Đối tượng (Object)

### 2.1. Khái niệm

**Đối tượng (Object)** là:
- Thực thể cụ thể được tạo từ lớp
- Có trạng thái (giá trị thuộc tính) riêng
- Có hành vi (phương thức) giống class

**Ví dụ**:
- Lớp: `SinhVien`
- Đối tượng: `sv1`, `sv2`, `sv3`

---

### 2.2. Tạo đối tượng

**C++ - Tạo đối tượng**:
```cpp
#include <iostream>
using namespace std;

class SanPham {
private:
    string ten;
    double gia;

public:
    SanPham(string t, double g) : ten(t), gia(g) {}

    void hienThi() const {
        cout << "San pham: " << ten << ", Gia: " << gia << endl;
    }
};

int main() {
    // Cách 1: Tạo object trên stack
    SanPham sp1("Laptop", 15000000);
    sp1.hienThi();

    // Cách 2: Tạo object trên heap (con trỏ)
    SanPham* sp2 = new SanPham("Mouse", 200000);
    sp2->hienThi();
    delete sp2;  // Phải giải phóng bộ nhớ

    // Cách 3: Sử dụng smart pointer (C++11)
    #include <memory>
    auto sp3 = make_unique<SanPham>("Keyboard", 500000);
    sp3->hienThi();
    // Tự động giải phóng

    return 0;
}
```

**C# - Tạo đối tượng**:
```csharp
using System;

class SanPham
{
    private string ten;
    private double gia;

    public SanPham(string t, double g)
    {
        ten = t;
        gia = g;
    }

    public void HienThi()
    {
        Console.WriteLine($"San pham: {ten}, Gia: {gia}");
    }
}

class Program
{
    static void Main()
    {
        // Cách 1: Tạo object thông thường
        SanPham sp1 = new SanPham("Laptop", 15000000);
        sp1.HienThi();

        // Cách 2: Sử dụng var
        var sp2 = new SanPham("Mouse", 200000);
        sp2.HienThi();

        // Cách 3: Object initializer
        var sp3 = new SanPham("Keyboard", 500000);
        sp3.HienThi();

        // Garbage collector tự động giải phóng bộ nhớ
    }
}
```

---

### 2.3. Truyền đối tượng vào phương thức

**C++ - Pass by value vs Pass by reference**:
```cpp
#include <iostream>
using namespace std;

class Diem {
public:
    int x, y;

    Diem(int xx = 0, int yy = 0) : x(xx), y(yy) {}

    void hienThi() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

// Pass by value - Sao chép đối tượng
void tangX_Value(Diem d) {
    d.x += 10;
    cout << "Trong ham: ";
    d.hienThi();
}

// Pass by reference - Truyền tham chiếu
void tangX_Reference(Diem &d) {
    d.x += 10;
    cout << "Trong ham: ";
    d.hienThi();
}

// Pass by pointer - Truyền con trỏ
void tangX_Pointer(Diem *d) {
    d->x += 10;
    cout << "Trong ham: ";
    d->hienThi();
}

int main() {
    Diem d1(5, 10);

    cout << "Ban dau: ";
    d1.hienThi();

    cout << "\n=== Pass by value ===" << endl;
    tangX_Value(d1);
    cout << "Sau ham: ";
    d1.hienThi();  // Không thay đổi

    cout << "\n=== Pass by reference ===" << endl;
    tangX_Reference(d1);
    cout << "Sau ham: ";
    d1.hienThi();  // Thay đổi

    cout << "\n=== Pass by pointer ===" << endl;
    tangX_Pointer(&d1);
    cout << "Sau ham: ";
    d1.hienThi();  // Thay đổi

    return 0;
}
```

**C# - Pass by value vs Pass by reference**:
```csharp
using System;

class Diem
{
    public int X { get; set; }
    public int Y { get; set; }

    public Diem(int x = 0, int y = 0)
    {
        X = x;
        Y = y;
    }

    public void HienThi()
    {
        Console.WriteLine($"({X}, {Y})");
    }
}

class Program
{
    // Pass by value (default cho class - truyền reference value)
    static void TangX_Value(Diem d)
    {
        d.X += 10;
        Console.Write("Trong ham: ");
        d.HienThi();
    }

    // Pass by reference - truyền reference
    static void TangX_Reference(ref Diem d)
    {
        d.X += 10;
        Console.Write("Trong ham: ");
        d.HienThi();
    }

    static void Main()
    {
        Diem d1 = new Diem(5, 10);

        Console.Write("Ban dau: ");
        d1.HienThi();

        Console.WriteLine("\n=== Pass by value ===");
        TangX_Value(d1);
        Console.Write("Sau ham: ");
        d1.HienThi();  // Thay đổi (vì class là reference type)

        Console.WriteLine("\n=== Pass by reference ===");
        TangX_Reference(ref d1);
        Console.Write("Sau ham: ");
        d1.HienThi();  // Thay đổi
    }
}
```

**Lưu ý quan trọng**:
- **C++**: Default là pass by value (copy), dùng `&` hoặc `*` để pass by reference
- **C#**: Class là reference type, default đã pass reference value. Dùng `ref` để pass reference của reference

---

## 3. Tham chiếu this / self

### 3.1. Khái niệm

`this` (C++) hoặc `this` (C#) là con trỏ/tham chiếu đến đối tượng hiện tại.

**Sử dụng khi**:
- Phân biệt thuộc tính và tham số cùng tên
- Gọi constructor từ constructor khác (constructor chaining)
- Truyền đối tượng hiện tại vào phương thức khác

---

### 3.2. Sử dụng this trong C++

```cpp
#include <iostream>
#include <string>
using namespace std;

class NhanVien {
private:
    string ten;
    int tuoi;
    double luong;

public:
    // Constructor - sử dụng this để phân biệt
    NhanVien(string ten, int tuoi, double luong) {
        this->ten = ten;
        this->tuoi = tuoi;
        this->luong = luong;
    }

    // Setter - sử dụng this
    void setTen(string ten) {
        this->ten = ten;
    }

    void setTuoi(int tuoi) {
        this->tuoi = tuoi;
    }

    // Method chaining - return *this
    NhanVien& setLuong(double luong) {
        this->luong = luong;
        return *this;
    }

    NhanVien& tangLuong(double phanTram) {
        this->luong += this->luong * phanTram / 100;
        return *this;
    }

    void hienThi() const {
        cout << "Ten: " << ten << ", Tuoi: " << tuoi
             << ", Luong: " << luong << endl;
    }

    // So sánh với object khác
    bool luongCaoHon(const NhanVien &nv) const {
        return this->luong > nv.luong;
    }
};

int main() {
    NhanVien nv1("Nguyen Van A", 25, 10000000);
    NhanVien nv2("Tran Thi B", 30, 15000000);

    // Method chaining
    nv1.setLuong(12000000).tangLuong(10).tangLuong(5);
    nv1.hienThi();

    // So sánh
    if (nv1.luongCaoHon(nv2)) {
        cout << "NV1 luong cao hon NV2" << endl;
    } else {
        cout << "NV2 luong cao hon NV1" << endl;
    }

    return 0;
}
```

---

### 3.3. Sử dụng this trong C#

```csharp
using System;

class NhanVien
{
    private string ten;
    private int tuoi;
    private double luong;

    // Constructor - sử dụng this để phân biệt
    public NhanVien(string ten, int tuoi, double luong)
    {
        this.ten = ten;
        this.tuoi = tuoi;
        this.luong = luong;
    }

    // Constructor chaining
    public NhanVien(string ten) : this(ten, 18, 5000000)
    {
        Console.WriteLine("Constructor chaining");
    }

    // Setter - sử dụng this
    public void SetTen(string ten)
    {
        this.ten = ten;
    }

    // Method chaining - return this
    public NhanVien SetLuong(double luong)
    {
        this.luong = luong;
        return this;
    }

    public NhanVien TangLuong(double phanTram)
    {
        this.luong += this.luong * phanTram / 100;
        return this;
    }

    public void HienThi()
    {
        Console.WriteLine($"Ten: {ten}, Tuoi: {tuoi}, Luong: {luong}");
    }

    // So sánh với object khác
    public bool LuongCaoHon(NhanVien nv)
    {
        return this.luong > nv.luong;
    }
}

class Program
{
    static void Main()
    {
        NhanVien nv1 = new NhanVien("Nguyen Van A", 25, 10000000);
        NhanVien nv2 = new NhanVien("Tran Thi B");

        // Method chaining
        nv1.SetLuong(12000000).TangLuong(10).TangLuong(5);
        nv1.HienThi();

        nv2.HienThi();

        // So sánh
        if (nv1.LuongCaoHon(nv2))
        {
            Console.WriteLine("NV1 luong cao hon NV2");
        }
        else
        {
            Console.WriteLine("NV2 luong cao hon NV1");
        }
    }
}
```

---

## 4. Thành viên tĩnh (Static Members)

### 4.1. Khái niệm

**Static members** thuộc về lớp, không thuộc về đối tượng cụ thể.

**Đặc điểm**:
- Được chia sẻ bởi tất cả đối tượng
- Truy cập qua tên lớp, không cần tạo đối tượng
- Được khởi tạo một lần duy nhất

---

### 4.2. Static trong C++

```cpp
#include <iostream>
#include <string>
using namespace std;

class SinhVien {
private:
    string maSV;
    string hoTen;
    static int demSinhVien;  // Static variable - chia sẻ

public:
    // Constructor
    SinhVien(string ma, string ten) : maSV(ma), hoTen(ten) {
        demSinhVien++;  // Tăng mỗi khi tạo object
    }

    // Destructor
    ~SinhVien() {
        demSinhVien--;
    }

    // Static method
    static int getDemSinhVien() {
        return demSinhVien;
        // Không thể truy cập non-static members
        // return maSV;  // ERROR!
    }

    // Static method khác
    static void thongKe() {
        cout << "Tong so sinh vien: " << demSinhVien << endl;
    }

    void hienThi() const {
        cout << "Ma: " << maSV << ", Ten: " << hoTen << endl;
    }
};

// Khởi tạo static variable BÊN NGOÀI class
int SinhVien::demSinhVien = 0;

int main() {
    cout << "So SV ban dau: " << SinhVien::getDemSinhVien() << endl;

    SinhVien sv1("SV001", "Nguyen Van A");
    SinhVien sv2("SV002", "Tran Thi B");
    SinhVien sv3("SV003", "Le Van C");

    // Gọi static method qua class name
    SinhVien::thongKe();  // 3 sinh viên

    {
        SinhVien sv4("SV004", "Pham Thi D");
        SinhVien::thongKe();  // 4 sinh viên
    }  // sv4 bị destroy

    SinhVien::thongKe();  // 3 sinh viên

    return 0;
}
```

---

### 4.3. Static trong C#

```csharp
using System;

class SinhVien
{
    private string maSV;
    private string hoTen;
    private static int demSinhVien = 0;  // Static variable

    // Constructor
    public SinhVien(string ma, string ten)
    {
        maSV = ma;
        hoTen = ten;
        demSinhVien++;
    }

    // Static property
    public static int DemSinhVien
    {
        get { return demSinhVien; }
    }

    // Static method
    public static void ThongKe()
    {
        Console.WriteLine($"Tong so sinh vien: {demSinhVien}");
        // Không thể truy cập non-static members
        // Console.WriteLine(maSV);  // ERROR!
    }

    public void HienThi()
    {
        Console.WriteLine($"Ma: {maSV}, Ten: {hoTen}");
    }

    // Static constructor - chạy một lần duy nhất
    static SinhVien()
    {
        Console.WriteLine("Static constructor called");
        demSinhVien = 0;
    }
}

// Static class - chỉ chứa static members
static class MathUtils
{
    public static double PI = 3.14159;

    public static int Cong(int a, int b)
    {
        return a + b;
    }

    public static int Tru(int a, int b)
    {
        return a - b;
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine($"So SV ban dau: {SinhVien.DemSinhVien}");

        SinhVien sv1 = new SinhVien("SV001", "Nguyen Van A");
        SinhVien sv2 = new SinhVien("SV002", "Tran Thi B");

        SinhVien.ThongKe();  // 2 sinh viên

        // Sử dụng static class
        int tong = MathUtils.Cong(5, 3);
        Console.WriteLine($"Tong: {tong}");
        Console.WriteLine($"PI: {MathUtils.PI}");
    }
}
```

---

### 4.4. Ứng dụng của Static

**1. Đếm số lượng đối tượng**:
```cpp
class Counter {
    static int count;
public:
    Counter() { count++; }
    ~Counter() { count--; }
    static int getCount() { return count; }
};
int Counter::count = 0;
```

**2. Utility class**:
```csharp
static class StringUtils
{
    public static string ToUpperCase(string s) => s.ToUpper();
    public static string ToLowerCase(string s) => s.ToLower();
    public static bool IsEmpty(string s) => string.IsNullOrEmpty(s);
}
```

**3. Singleton pattern**:
```cpp
class Database {
private:
    static Database* instance;
    Database() {}  // Private constructor
public:
    static Database* getInstance() {
        if (instance == nullptr) {
            instance = new Database();
        }
        return instance;
    }
};
Database* Database::instance = nullptr;
```

---

## 5. Khối khởi động (Initialization Block)

### 5.1. Trong C++

C++ có **initializer list** để khởi tạo members:

```cpp
class HocSinh {
private:
    const int id;        // Constant member
    string& tenRef;      // Reference member
    string hoTen;

public:
    // Initializer list - khởi tạo trước khi vào constructor body
    HocSinh(int i, string& ref, string ten)
        : id(i), tenRef(ref), hoTen(ten)  // Initializer list
    {
        // Constructor body
        cout << "Constructor body" << endl;
    }

    void hienThi() const {
        cout << "ID: " << id << ", Ten: " << hoTen << endl;
    }
};

int main() {
    string tenLop = "10A1";
    HocSinh hs(1, tenLop, "Nguyen Van A");
    hs.hienThi();
    return 0;
}
```

**Khi nào phải dùng initializer list**:
- ✅ Khởi tạo const members
- ✅ Khởi tạo reference members
- ✅ Khởi tạo base class
- ✅ Hiệu suất tốt hơn (tránh khởi tạo 2 lần)

---

### 5.2. Trong C#

C# có **Object Initializer** và **Field Initializer**:

```csharp
class HocSinh
{
    // Field initializer - khởi tạo trực tiếp
    private int id;
    private string hoTen = "Unknown";  // Default value
    private DateTime ngayTao = DateTime.Now;

    // Property initializer
    public string Lop { get; set; } = "10A1";

    // Constructor
    public HocSinh(int i, string ten)
    {
        id = i;
        hoTen = ten;
    }

    public void HienThi()
    {
        Console.WriteLine($"ID: {id}, Ten: {hoTen}, Lop: {Lop}");
    }
}

class Program
{
    static void Main()
    {
        // Object initializer
        HocSinh hs1 = new HocSinh(1, "Nguyen Van A")
        {
            Lop = "10A2"
        };

        hs1.HienThi();
    }
}
```

---

## 6. Nạp chồng (Overloading)

### 6.1. Method Overloading

**Định nghĩa**: Nhiều phương thức cùng tên nhưng khác tham số.

**C++ - Method Overloading**:
```cpp
#include <iostream>
#include <string>
using namespace std;

class MayTinh {
public:
    // Cùng tên, khác số lượng tham số
    int cong(int a, int b) {
        return a + b;
    }

    int cong(int a, int b, int c) {
        return a + b + c;
    }

    // Cùng tên, khác kiểu tham số
    double cong(double a, double b) {
        return a + b;
    }

    // Cùng tên, khác kiểu và số lượng
    string cong(string a, string b) {
        return a + b;
    }
};

int main() {
    MayTinh mt;

    cout << mt.cong(5, 3) << endl;           // 8
    cout << mt.cong(1, 2, 3) << endl;        // 6
    cout << mt.cong(5.5, 3.2) << endl;       // 8.7
    cout << mt.cong("Hello", " World") << endl; // Hello World

    return 0;
}
```

**C# - Method Overloading**:
```csharp
using System;

class MayTinh
{
    // Overloading
    public int Cong(int a, int b)
    {
        return a + b;
    }

    public int Cong(int a, int b, int c)
    {
        return a + b + c;
    }

    public double Cong(double a, double b)
    {
        return a + b;
    }

    public string Cong(string a, string b)
    {
        return a + b;
    }

    // Optional parameters - alternative to overloading
    public int Tong(int a, int b = 0, int c = 0)
    {
        return a + b + c;
    }
}

class Program
{
    static void Main()
    {
        MayTinh mt = new MayTinh();

        Console.WriteLine(mt.Cong(5, 3));           // 8
        Console.WriteLine(mt.Cong(1, 2, 3));        // 6
        Console.WriteLine(mt.Cong(5.5, 3.2));       // 8.7
        Console.WriteLine(mt.Cong("Hello", " World")); // Hello World

        // Optional parameters
        Console.WriteLine(mt.Tong(1));       // 1
        Console.WriteLine(mt.Tong(1, 2));    // 3
        Console.WriteLine(mt.Tong(1, 2, 3)); // 6
    }
}
```

---

### 6.2. Constructor Overloading

**C++**:
```cpp
class Diem {
private:
    int x, y;

public:
    // Constructor overloading
    Diem() {
        x = y = 0;
    }

    Diem(int xx) {
        x = y = xx;
    }

    Diem(int xx, int yy) {
        x = xx;
        y = yy;
    }

    void hienThi() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};
```

**C#**:
```csharp
class Diem
{
    private int x, y;

    // Constructor overloading
    public Diem()
    {
        x = y = 0;
    }

    public Diem(int xx)
    {
        x = y = xx;
    }

    public Diem(int xx, int yy)
    {
        x = xx;
        y = yy;
    }

    // Constructor chaining
    public Diem(int xx) : this(xx, xx) { }

    public void HienThi()
    {
        Console.WriteLine($"({x}, {y})");
    }
}
```

---

### 6.3. Operator Overloading

**C++ - Operator Overloading**:
```cpp
#include <iostream>
using namespace std;

class PhanSo {
private:
    int tu, mau;

public:
    PhanSo(int t = 0, int m = 1) : tu(t), mau(m) {}

    // Overload toán tử +
    PhanSo operator+(const PhanSo &ps) const {
        return PhanSo(tu * ps.mau + ps.tu * mau, mau * ps.mau);
    }

    // Overload toán tử -
    PhanSo operator-(const PhanSo &ps) const {
        return PhanSo(tu * ps.mau - ps.tu * mau, mau * ps.mau);
    }

    // Overload toán tử *
    PhanSo operator*(const PhanSo &ps) const {
        return PhanSo(tu * ps.tu, mau * ps.mau);
    }

    // Overload toán tử ==
    bool operator==(const PhanSo &ps) const {
        return tu * ps.mau == ps.tu * mau;
    }

    // Overload toán tử <<
    friend ostream& operator<<(ostream &os, const PhanSo &ps) {
        os << ps.tu << "/" << ps.mau;
        return os;
    }

    // Overload toán tử >>
    friend istream& operator>>(istream &is, PhanSo &ps) {
        is >> ps.tu >> ps.mau;
        return is;
    }
};

int main() {
    PhanSo ps1(1, 2), ps2(1, 3);

    PhanSo tong = ps1 + ps2;
    PhanSo hieu = ps1 - ps2;
    PhanSo tich = ps1 * ps2;

    cout << ps1 << " + " << ps2 << " = " << tong << endl;
    cout << ps1 << " - " << ps2 << " = " << hieu << endl;
    cout << ps1 << " * " << ps2 << " = " << tich << endl;

    return 0;
}
```

**C# - Operator Overloading**:
```csharp
using System;

class PhanSo
{
    private int tu, mau;

    public PhanSo(int t = 0, int m = 1)
    {
        tu = t;
        mau = m;
    }

    // Overload toán tử +
    public static PhanSo operator +(PhanSo ps1, PhanSo ps2)
    {
        return new PhanSo(ps1.tu * ps2.mau + ps2.tu * ps1.mau,
                         ps1.mau * ps2.mau);
    }

    // Overload toán tử -
    public static PhanSo operator -(PhanSo ps1, PhanSo ps2)
    {
        return new PhanSo(ps1.tu * ps2.mau - ps2.tu * ps1.mau,
                         ps1.mau * ps2.mau);
    }

    // Overload toán tử *
    public static PhanSo operator *(PhanSo ps1, PhanSo ps2)
    {
        return new PhanSo(ps1.tu * ps2.tu, ps1.mau * ps2.mau);
    }

    // Overload toán tử ==
    public static bool operator ==(PhanSo ps1, PhanSo ps2)
    {
        return ps1.tu * ps2.mau == ps2.tu * ps1.mau;
    }

    public static bool operator !=(PhanSo ps1, PhanSo ps2)
    {
        return !(ps1 == ps2);
    }

    public override string ToString()
    {
        return $"{tu}/{mau}";
    }
}

class Program
{
    static void Main()
    {
        PhanSo ps1 = new PhanSo(1, 2);
        PhanSo ps2 = new PhanSo(1, 3);

        PhanSo tong = ps1 + ps2;
        PhanSo hieu = ps1 - ps2;
        PhanSo tich = ps1 * ps2;

        Console.WriteLine($"{ps1} + {ps2} = {tong}");
        Console.WriteLine($"{ps1} - {ps2} = {hieu}");
        Console.WriteLine($"{ps1} * {ps2} = {tich}");
    }
}
```

---

## 7. Gói (Package/Namespace)

### 7.1. Namespace trong C++

```cpp
// MathUtils.h
#ifndef MATHUTILS_H
#define MATHUTILS_H

namespace MyMath {
    class Calculator {
    public:
        static int add(int a, int b);
        static int subtract(int a, int b);
    };

    const double PI = 3.14159;

    double calculateCircleArea(double radius);
}

#endif

// MathUtils.cpp
#include "MathUtils.h"

namespace MyMath {
    int Calculator::add(int a, int b) {
        return a + b;
    }

    int Calculator::subtract(int a, int b) {
        return a - b;
    }

    double calculateCircleArea(double radius) {
        return PI * radius * radius;
    }
}

// main.cpp
#include <iostream>
#include "MathUtils.h"

int main() {
    // Cách 1: Sử dụng fully qualified name
    int sum = MyMath::Calculator::add(5, 3);
    std::cout << "Sum: " << sum << std::endl;

    // Cách 2: Using namespace
    using namespace MyMath;
    double area = calculateCircleArea(5);
    std::cout << "Area: " << area << std::endl;

    // Cách 3: Using declaration
    using MyMath::Calculator;
    int diff = Calculator::subtract(10, 3);
    std::cout << "Diff: " << diff << std::endl;

    return 0;
}
```

---

### 7.2. Namespace trong C#

```csharp
// MathUtils.cs
namespace MyCompany.Math
{
    public class Calculator
    {
        public static int Add(int a, int b)
        {
            return a + b;
        }

        public static int Subtract(int a, int b)
        {
            return a - b;
        }
    }

    public class Constants
    {
        public const double PI = 3.14159;
    }

    public static class CircleHelper
    {
        public static double CalculateArea(double radius)
        {
            return Constants.PI * radius * radius;
        }
    }
}

// Program.cs
using System;
using MyCompany.Math;  // Import namespace

namespace MyApp
{
    class Program
    {
        static void Main()
        {
            // Sử dụng sau khi import
            int sum = Calculator.Add(5, 3);
            Console.WriteLine($"Sum: {sum}");

            double area = CircleHelper.CalculateArea(5);
            Console.WriteLine($"Area: {area}");

            // Hoặc sử dụng fully qualified name
            int diff = MyCompany.Math.Calculator.Subtract(10, 3);
            Console.WriteLine($"Diff: {diff}");
        }
    }
}
```

**Lợi ích của namespace**:
- ✅ Tránh xung đột tên (name collision)
- ✅ Tổ chức code tốt hơn
- ✅ Phân cấp module rõ ràng
- ✅ Dễ quản lý dự án lớn

---

## 8. Quan hệ giữa lớp và đối tượng

### 8.1. Mối quan hệ

```
        Class (Blueprint)
             ↓
    ┌────────┼────────┐
    ↓        ↓        ↓
Object 1  Object 2  Object 3
```

**Đặc điểm**:
- Một class có thể tạo nhiều objects
- Mỗi object có state riêng
- Objects chia sẻ behavior từ class

**Ví dụ**:
```cpp
class XeHoi {
    string bien so;
    string mauXe;
public:
    void chay() { }
};

// 3 objects khác nhau
XeHoi xe1;  // biển số: 30A-12345
XeHoi xe2;  // biển số: 29B-67890
XeHoi xe3;  // biển số: 51C-11111
```

---

## 9. Quan hệ giữa hai lớp

### 9.1. Association (Liên kết)

**Định nghĩa**: Lớp A sử dụng lớp B, hai lớp độc lập.

**Ký hiệu UML**: `A ────────> B`

**Ví dụ C++**:
```cpp
class GiangVien {
private:
    string hoTen;
public:
    GiangVien(string ten) : hoTen(ten) {}
    string getHoTen() const { return hoTen; }
};

class MonHoc {
private:
    string tenMon;
    GiangVien* giangVien;  // Association
public:
    MonHoc(string ten) : tenMon(ten), giangVien(nullptr) {}

    void ganGiangVien(GiangVien* gv) {
        giangVien = gv;
    }

    void hienThi() const {
        cout << "Mon: " << tenMon;
        if (giangVien != nullptr) {
            cout << ", GV: " << giangVien->getHoTen();
        }
        cout << endl;
    }
};

int main() {
    GiangVien gv("Nguyen Van A");
    MonHoc mon("OOP");
    mon.ganGiangVien(&gv);  // Liên kết
    mon.hienThi();
    return 0;
}
```

---

### 9.2. Aggregation (Tổng hợp)

**Định nghĩa**: Lớp A chứa lớp B, nhưng B có thể tồn tại độc lập.

**Ký hiệu UML**: `A ◇────────> B`

**Ví dụ C++**:
```cpp
class SinhVien {
private:
    string hoTen;
public:
    SinhVien(string ten) : hoTen(ten) {}
    string getHoTen() const { return hoTen; }
};

class LopHoc {
private:
    string tenLop;
    vector<SinhVien*> dsSinhVien;  // Aggregation
public:
    LopHoc(string ten) : tenLop(ten) {}

    void themSinhVien(SinhVien* sv) {
        dsSinhVien.push_back(sv);
    }

    void hienThiDanhSach() const {
        cout << "Lop: " << tenLop << endl;
        for (const auto& sv : dsSinhVien) {
            cout << "- " << sv->getHoTen() << endl;
        }
    }

    ~LopHoc() {
        // Không delete sinh viên vì có thể tồn tại ngoài lớp
    }
};

int main() {
    SinhVien sv1("Nguyen Van A");
    SinhVien sv2("Tran Thi B");

    LopHoc lop("10A1");
    lop.themSinhVien(&sv1);
    lop.themSinhVien(&sv2);

    lop.hienThiDanhSach();
    // sv1, sv2 vẫn tồn tại sau khi lop bị destroy

    return 0;
}
```

---

### 9.3. Composition (Hợp thành)

**Định nghĩa**: Lớp A chứa lớp B, B không thể tồn tại độc lập.

**Ký hiệu UML**: `A ◆────────> B`

**Ví dụ C++**:
```cpp
class PhongHoc {
private:
    string soPhong;
public:
    PhongHoc(string so) : soPhong(so) {
        cout << "Phong " << soPhong << " duoc tao" << endl;
    }

    ~PhongHoc() {
        cout << "Phong " << soPhong << " bi huy" << endl;
    }

    string getSoPhong() const { return soPhong; }
};

class ToaNha {
private:
    string tenToaNha;
    vector<PhongHoc*> dsPhong;  // Composition
public:
    ToaNha(string ten) : tenToaNha(ten) {
        // Tạo các phòng - life cycle phụ thuộc vào tòa nhà
        dsPhong.push_back(new PhongHoc("P101"));
        dsPhong.push_back(new PhongHoc("P102"));
        dsPhong.push_back(new PhongHoc("P103"));
    }

    ~ToaNha() {
        // Hủy các phòng khi tòa nhà bị hủy
        for (auto phong : dsPhong) {
            delete phong;
        }
    }

    void hienThiDanhSach() const {
        cout << "Toa nha: " << tenToaNha << endl;
        for (const auto& phong : dsPhong) {
            cout << "- Phong " << phong->getSoPhong() << endl;
        }
    }
};

int main() {
    {
        ToaNha toaNha("A");
        toaNha.hienThiDanhSach();
    }  // Tòa nhà và các phòng đều bị hủy

    return 0;
}
```

---

### 9.4. Dependency (Phụ thuộc)

**Định nghĩa**: Lớp A sử dụng lớp B như tham số hoặc local variable.

**Ký hiệu UML**: `A ········> B`

**Ví dụ C++**:
```cpp
class Email {
private:
    string noiDung;
public:
    Email(string nd) : noiDung(nd) {}
    string getNoiDung() const { return noiDung; }
};

class EmailService {
public:
    // Dependency - nhận Email như tham số
    void guiEmail(const Email& email, string nguoiNhan) {
        cout << "Gui email den " << nguoiNhan << endl;
        cout << "Noi dung: " << email.getNoiDung() << endl;
    }
};

int main() {
    EmailService service;
    Email email("Hello World");
    service.guiEmail(email, "test@example.com");
    return 0;
}
```

---

### 9.5. Inheritance (Kế thừa)

**Định nghĩa**: Lớp con kế thừa từ lớp cha.

**Ký hiệu UML**: `LớpCon ──────▷ LớpCha`

**Sẽ được trình bày chi tiết ở Chương 3**.

---

## 10. Lớp trong (Inner/Nested Class)

### 10.1. Nested Class trong C++

```cpp
#include <iostream>
#include <string>
using namespace std;

class Outer {
private:
    int outerData;

public:
    Outer(int data) : outerData(data) {}

    // Nested class
    class Inner {
    private:
        int innerData;

    public:
        Inner(int data) : innerData(data) {}

        void display() {
            cout << "Inner data: " << innerData << endl;
            // Không thể truy cập outerData trực tiếp
        }
    };

    void showInner() {
        Inner inner(100);
        inner.display();
    }
};

int main() {
    Outer outer(50);
    outer.showInner();

    // Tạo nested class object
    Outer::Inner inner(200);
    inner.display();

    return 0;
}
```

---

### 10.2. Nested Class trong C#

```csharp
using System;

class Outer
{
    private int outerData;

    public Outer(int data)
    {
        outerData = data;
    }

    // Nested class
    public class Inner
    {
        private int innerData;

        public Inner(int data)
        {
            innerData = data;
        }

        public void Display()
        {
            Console.WriteLine($"Inner data: {innerData}");
        }
    }

    // Private nested class
    private class PrivateInner
    {
        public void Display()
        {
            Console.WriteLine("Private inner class");
        }
    }

    public void ShowInner()
    {
        Inner inner = new Inner(100);
        inner.Display();

        PrivateInner privateInner = new PrivateInner();
        privateInner.Display();
    }
}

class Program
{
    static void Main()
    {
        Outer outer = new Outer(50);
        outer.ShowInner();

        // Tạo nested class object
        Outer.Inner inner = new Outer.Inner(200);
        inner.Display();

        // Không thể truy cập private nested class
        // Outer.PrivateInner x = new Outer.PrivateInner(); // ERROR
    }
}
```

**Khi nào sử dụng nested class**:
- ✅ Helper class chỉ được dùng bởi outer class
- ✅ Tăng tính encapsulation
- ✅ Tổ chức code tốt hơn

---

## 11. Xử lý ngoại lệ (Exception Handling)

### 11.1. Exception trong C++

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

class TaiKhoan {
private:
    double soDu;

public:
    TaiKhoan(double soDuBanDau) {
        if (soDuBanDau < 0) {
            throw invalid_argument("So du khong the am!");
        }
        soDu = soDuBanDau;
    }

    void rutTien(double soTien) {
        if (soTien <= 0) {
            throw invalid_argument("So tien phai lon hon 0!");
        }
        if (soTien > soDu) {
            throw runtime_error("So du khong du!");
        }
        soDu -= soTien;
        cout << "Rut " << soTien << " thanh cong" << endl;
    }

    double getSoDu() const {
        return soDu;
    }
};

// Custom exception class
class SoDuKhongDuException : public exception {
private:
    string message;

public:
    SoDuKhongDuException(const string& msg) : message(msg) {}

    const char* what() const noexcept override {
        return message.c_str();
    }
};

int main() {
    try {
        TaiKhoan tk(1000000);

        tk.rutTien(500000);   // OK
        cout << "So du: " << tk.getSoDu() << endl;

        tk.rutTien(700000);   // Exception
    }
    catch (const invalid_argument& e) {
        cout << "Loi tham so: " << e.what() << endl;
    }
    catch (const runtime_error& e) {
        cout << "Loi runtime: " << e.what() << endl;
    }
    catch (const exception& e) {
        cout << "Loi: " << e.what() << endl;
    }
    catch (...) {
        cout << "Loi khong xac dinh!" << endl;
    }

    return 0;
}
```

---

### 11.2. Exception trong C#

```csharp
using System;

class TaiKhoan
{
    private double soDu;

    public TaiKhoan(double soDuBanDau)
    {
        if (soDuBanDau < 0)
        {
            throw new ArgumentException("So du khong the am!");
        }
        soDu = soDuBanDau;
    }

    public void RutTien(double soTien)
    {
        if (soTien <= 0)
        {
            throw new ArgumentException("So tien phai lon hon 0!");
        }
        if (soTien > soDu)
        {
            throw new InvalidOperationException("So du khong du!");
        }
        soDu -= soTien;
        Console.WriteLine($"Rut {soTien} thanh cong");
    }

    public double SoDu => soDu;
}

// Custom exception class
class SoDuKhongDuException : Exception
{
    public SoDuKhongDuException(string message) : base(message) { }

    public SoDuKhongDuException(string message, Exception inner)
        : base(message, inner) { }
}

class Program
{
    static void Main()
    {
        try
        {
            TaiKhoan tk = new TaiKhoan(1000000);

            tk.RutTien(500000);   // OK
            Console.WriteLine($"So du: {tk.SoDu}");

            tk.RutTien(700000);   // Exception
        }
        catch (ArgumentException e)
        {
            Console.WriteLine($"Loi tham so: {e.Message}");
        }
        catch (InvalidOperationException e)
        {
            Console.WriteLine($"Loi thao tac: {e.Message}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Loi: {e.Message}");
        }
        finally
        {
            Console.WriteLine("Finally block - luon chay");
        }
    }
}
```

**Các exception phổ biến**:

| C++ | C# | Mô tả |
|-----|-----|-------|
| `exception` | `Exception` | Base class |
| `invalid_argument` | `ArgumentException` | Tham số không hợp lệ |
| `runtime_error` | `InvalidOperationException` | Lỗi runtime |
| `out_of_range` | `IndexOutOfRangeException` | Index vượt quá |
| `logic_error` | `LogicException` | Lỗi logic |

---

## 12. Ký hiệu UML

### 12.1. Class Diagram

**Cú pháp**:
```
┌─────────────────────────────┐
│      TênLớp                 │
├─────────────────────────────┤
│ - thuộcTínhPrivate: Type    │
│ + thuộcTínhPublic: Type     │
│ # thuộcTínhProtected: Type  │
├─────────────────────────────┤
│ + phươngThứcPublic(): Type  │
│ - phươngThứcPrivate(): Type │
└─────────────────────────────┘
```

**Ký hiệu**:
- `+` : public
- `-` : private
- `#` : protected
- `~` : package/internal
- `_` : static (gạch chân)
- *italic* : abstract

**Ví dụ UML cho lớp SinhVien**:
```
┌───────────────────────────────┐
│       SinhVien                │
├───────────────────────────────┤
│ - maSV: string                │
│ - hoTen: string               │
│ - namSinh: int                │
│ - diemTB: double              │
│ - demSinhVien: int            │
│   {static, underline}         │
├───────────────────────────────┤
│ + SinhVien(ma, ten, nam, diem)│
│ + getMaSV(): string           │
│ + getDiemTB(): double         │
│ + setDiemTB(diem: double)     │
│ + hienThiThongTin()           │
│ + xepLoai(): string           │
│ + getDemSinhVien(): int       │
│   {static}                    │
└───────────────────────────────┘
```

---

### 12.2. Quan hệ trong UML

```
Association:
    A ────────> B

Aggregation:
    A ◇────────> B

Composition:
    A ◆────────> B

Inheritance:
    B ──────▷ A

Dependency:
    A ········> B

Interface Implementation:
    B ········▷ <<Interface>> A
```

---

## 📝 Tóm tắt Chương 2

### Các điểm chính:

1. **Lớp và Đối tượng**:
   - Class là blueprint, Object là instance
   - Encapsulation với access modifiers
   - Constructor & Destructor

2. **Thành viên tĩnh**:
   - Thuộc về class, không thuộc object
   - Truy cập qua class name
   - Chia sẻ giữa các objects

3. **Quan hệ giữa các lớp**:
   - Association: Liên kết
   - Aggregation: Tổng hợp
   - Composition: Hợp thành
   - Dependency: Phụ thuộc

4. **Overloading**:
   - Method overloading
   - Constructor overloading
   - Operator overloading

5. **Exception Handling**:
   - try-catch-finally (C#)
   - try-catch (C++)
   - Custom exceptions

### Bài tập:

1. Tạo lớp `HocSinh` với đầy đủ properties, constructors, methods
2. Implement lớp `PhanSo` với operator overloading
3. Tạo lớp `LopHoc` và `SinhVien` với quan hệ Aggregation
4. Vẽ UML cho hệ thống quản lý thư viện
5. Viết chương trình xử lý exception cho việc nhập điểm sinh viên

---

**Chương tiếp theo**: [Chương 3: Kế Thừa](Chuong-3-Ke-Thua.md)
