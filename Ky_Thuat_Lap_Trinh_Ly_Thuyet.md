# TÀI LIỆU LÝ THUYẾT - KỸ THUẬT LẬP TRÌNH

**Trường Đại học Mở Thành phố Hồ Chí Minh**
**Khoa Công nghệ Thông tin**

---

## MỤC LỤC

1. [Chương 1: Mảng nhiều chiều](#chương-1-mảng-nhiều-chiều)
2. [Chương 2: Đệ quy](#chương-2-đệ-quy)
3. [Chương 3: Con trỏ](#chương-3-con-trỏ)
4. [Chương 4: Chuỗi ký tự](#chương-4-chuỗi-ký-tự)
5. [Chương 5: Kiểu dữ liệu người dùng](#chương-5-kiểu-dữ-liệu-người-dùng)
6. [Chương 6: Tập tin và luồng](#chương-6-tập-tin-và-luồng)

---

## CHƯƠNG 1: MẢNG NHIỀU CHIỀU

### 1.1 Giới thiệu mảng nhiều chiều

**Khái niệm:**
- Mảng nhiều chiều là mảng có nhiều hơn một chiều (dimension)
- Mảng hai chiều có thể được hình dung như một bảng gồm các hàng và cột
- Mảng ba chiều có thể được hình dung như một khối lập phương

**Ứng dụng:**
- Ma trận trong toán học
- Bảng dữ liệu
- Lưu trữ hình ảnh (pixel)
- Lưu trữ dữ liệu không gian 3D

### 1.2 Khai báo và khởi tạo mảng hai chiều

**Cú pháp khai báo:**
```cpp
<kiểu_dữ_liệu> <tên_mảng>[số_hàng][số_cột];
```

**Ví dụ:**
```cpp
// Khai báo mảng 2 chiều có 3 hàng, 4 cột
int matrix[3][4];

// Khai báo và khởi tạo mảng 2 chiều
int arr[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

// Khởi tạo không đầy đủ (các phần tử còn lại = 0)
int arr2[3][3] = {
    {1, 2},
    {3},
    {4, 5, 6}
};

// Khai báo mảng mà không chỉ định số hàng (phải có khởi tạo)
int arr3[][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

**Truy xuất phần tử:**
```cpp
int matrix[3][4];

// Gán giá trị cho phần tử hàng 1, cột 2
matrix[1][2] = 10;

// Lấy giá trị từ phần tử hàng 0, cột 3
int value = matrix[0][3];
```

### 1.3 Nhập/xuất mảng hai chiều

**Nhập mảng:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int m, n;
    cout << "Nhap so hang: ";
    cin >> m;
    cout << "Nhap so cot: ";
    cin >> n;

    int arr[100][100]; // Khai báo mảng tối đa

    // Nhập dữ liệu
    cout << "Nhap cac phan tu:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << "arr[" << i << "][" << j << "] = ";
            cin >> arr[i][j];
        }
    }

    return 0;
}
```

**Xuất mảng:**
```cpp
// Xuất mảng dạng bảng
cout << "Ma tran:\n";
for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        cout << arr[i][j] << "\t";
    }
    cout << "\n";
}
```

### 1.4 Một số thao tác trên mảng hai chiều

**1. Tìm phần tử lớn nhất/nhỏ nhất:**
```cpp
int findMax(int arr[][100], int m, int n) {
    int max = arr[0][0];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[i][j] > max) {
                max = arr[i][j];
            }
        }
    }
    return max;
}
```

**2. Tính tổng các phần tử:**
```cpp
int sumArray(int arr[][100], int m, int n) {
    int sum = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            sum += arr[i][j];
        }
    }
    return sum;
}
```

**3. Tính tổng các phần tử trên đường chéo chính:**
```cpp
int sumDiagonal(int arr[][100], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i][i];
    }
    return sum;
}
```

**4. Chuyển vị ma trận:**
```cpp
void transpose(int arr[][100], int result[][100], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            result[j][i] = arr[i][j];
        }
    }
}
```

**5. Nhân hai ma trận:**
```cpp
void multiplyMatrix(int a[][100], int b[][100], int result[][100],
                    int m, int n, int p) {
    // a: m x n, b: n x p, result: m x p
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            result[i][j] = 0;
            for (int k = 0; k < n; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}
```

### 1.5 Truyền mảng hai chiều đến hàm

**Cách 1: Chỉ định kích thước cột:**
```cpp
void printArray(int arr[][100], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
}
```

**Cách 2: Sử dụng con trỏ:**
```cpp
void printArray(int (*arr)[100], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
}
```

**Ví dụ hoàn chỉnh:**
```cpp
#include <iostream>
using namespace std;

void inputMatrix(int arr[][100], int &m, int &n) {
    cout << "Nhap so hang va cot: ";
    cin >> m >> n;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
}

void printMatrix(int arr[][100], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << arr[i][j] << "\t";
        }
        cout << "\n";
    }
}

int main() {
    int matrix[100][100];
    int m, n;

    inputMatrix(matrix, m, n);
    cout << "Ma tran vua nhap:\n";
    printMatrix(matrix, m, n);

    return 0;
}
```

---

## CHƯƠNG 2: ĐỆ QUY

### 2.1 Giới thiệu

**Khái niệm:**
- Đệ quy là kỹ thuật lập trình mà một hàm gọi chính nó
- Là một phương pháp giải quyết bài toán bằng cách chia nhỏ thành các bài toán con tương tự nhưng đơn giản hơn

**Ví dụ trong thực tế:**
- Tính giai thừa: n! = n × (n-1)!
- Dãy Fibonacci: F(n) = F(n-1) + F(n-2)
- Duyệt cây thư mục

### 2.2 Định nghĩa

**Cấu trúc một hàm đệ quy:**
```cpp
kiểu_dữ_liệu tenHam(tham_số) {
    // 1. Điều kiện dừng (base case)
    if (điều_kiện_dừng) {
        return giá_trị_cơ_sở;
    }

    // 2. Bước đệ quy (recursive case)
    return tenHam(tham_số_nhỏ_hơn);
}
```

**Thành phần quan trọng:**
1. **Điều kiện dừng (Base case):** Điều kiện để kết thúc đệ quy
2. **Bước đệ quy (Recursive step):** Gọi lại chính hàm với tham số khác

### 2.3 Hàm đệ quy

#### 2.3.1 Cài đặt hàm

**Ví dụ 1: Tính giai thừa**
```cpp
// n! = n × (n-1) × (n-2) × ... × 2 × 1
// n! = n × (n-1)!
long long factorial(int n) {
    // Điều kiện dừng
    if (n == 0 || n == 1) {
        return 1;
    }
    // Bước đệ quy
    return n * factorial(n - 1);
}
```

**Ví dụ 2: Tính lũy thừa**
```cpp
// x^n = x × x^(n-1)
long long power(int x, int n) {
    if (n == 0) {
        return 1;
    }
    return x * power(x, n - 1);
}
```

**Ví dụ 3: Tính số Fibonacci**
```cpp
// F(0) = 0, F(1) = 1
// F(n) = F(n-1) + F(n-2)
int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

**Ví dụ 4: Tính tổng các chữ số**
```cpp
int sumDigits(int n) {
    if (n == 0) {
        return 0;
    }
    return n % 10 + sumDigits(n / 10);
}
```

**Ví dụ 5: Tính ước chung lớn nhất (GCD)**
```cpp
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}
```

#### 2.3.2 Sử dụng hàm

```cpp
#include <iostream>
using namespace std;

long long factorial(int n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << n << "! = " << factorial(n) << endl;

    return 0;
}
```

### 2.4 Một số loại đệ quy

**1. Đệ quy tuyến tính (Linear Recursion):**
- Hàm chỉ gọi chính nó một lần
```cpp
int sum(int n) {
    if (n == 0) return 0;
    return n + sum(n - 1);
}
```

**2. Đệ quy nhị phân (Binary Recursion):**
- Hàm gọi chính nó hai lần
```cpp
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

**3. Đệ quy đuôi (Tail Recursion):**
- Lời gọi đệ quy là câu lệnh cuối cùng trong hàm
```cpp
int factorialTail(int n, int result = 1) {
    if (n == 0) return result;
    return factorialTail(n - 1, n * result);
}
```

**4. Đệ quy lồng nhau (Nested Recursion):**
- Tham số của lời gọi đệ quy là một lời gọi đệ quy khác
```cpp
int ackermann(int m, int n) {
    if (m == 0) return n + 1;
    if (n == 0) return ackermann(m - 1, 1);
    return ackermann(m - 1, ackermann(m, n - 1));
}
```

**5. Đệ quy có nhớ (Memoization):**
```cpp
#include <map>
map<int, long long> memo;

long long fibMemo(int n) {
    if (n <= 1) return n;
    if (memo.find(n) != memo.end()) {
        return memo[n];
    }
    memo[n] = fibMemo(n - 1) + fibMemo(n - 2);
    return memo[n];
}
```

### 2.5 So sánh đệ quy với lặp

**Đệ quy:**
```cpp
// Tính giai thừa bằng đệ quy
long long factorialRecursive(int n) {
    if (n <= 1) return 1;
    return n * factorialRecursive(n - 1);
}
```

**Lặp:**
```cpp
// Tính giai thừa bằng vòng lặp
long long factorialIterative(int n) {
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
```

**So sánh:**

| Tiêu chí | Đệ quy | Lặp |
|----------|--------|-----|
| Mã nguồn | Ngắn gọn, dễ hiểu | Dài hơn |
| Bộ nhớ | Tốn nhiều bộ nhớ stack | Tiết kiệm bộ nhớ |
| Tốc độ | Chậm hơn | Nhanh hơn |
| Phù hợp | Bài toán có cấu trúc đệ quy tự nhiên | Bài toán đơn giản |

**Khi nào nên dùng đệ quy:**
- Bài toán có cấu trúc đệ quy tự nhiên (cây, đồ thị)
- Mã nguồn ngắn gọn, dễ hiểu quan trọng hơn hiệu năng
- Dữ liệu đầu vào không quá lớn

**Khi nào nên dùng lặp:**
- Cần tối ưu hiệu năng
- Dữ liệu đầu vào lớn
- Bài toán đơn giản

---

## CHƯƠNG 3: CON TRỎ

### 3.1 Giới thiệu

**Khái niệm:**
- Con trỏ (pointer) là một biến lưu trữ địa chỉ của một biến khác
- Con trỏ giúp truy xuất trực tiếp vào vùng nhớ
- Là công cụ mạnh mẽ trong C++ nhưng cũng dễ gây lỗi nếu sử dụng không đúng

**Lợi ích:**
- Cấp phát bộ nhớ động
- Truyền tham số theo tham chiếu hiệu quả
- Tạo các cấu trúc dữ liệu phức tạp (danh sách liên kết, cây, đồ thị)
- Thao tác với mảng hiệu quả

### 3.2 Sử dụng con trỏ

**Ứng dụng:**
1. Cấp phát bộ nhớ động
2. Truyền tham số cho hàm
3. Trả về nhiều giá trị từ hàm
4. Làm việc với mảng và chuỗi
5. Xây dựng cấu trúc dữ liệu động

### 3.3 Khai báo và khởi tạo con trỏ

**Cú pháp khai báo:**
```cpp
<kiểu_dữ_liệu>* <tên_con_trỏ>;
```

**Ví dụ:**
```cpp
int* ptr;      // Con trỏ trỏ đến int
double* dptr;  // Con trỏ trỏ đến double
char* cptr;    // Con trỏ trỏ đến char
```

#### 3.3.1 Toán tử * (Dereference operator)

Toán tử `*` được sử dụng để:
1. Khai báo con trỏ
2. Truy xuất giá trị mà con trỏ trỏ đến

```cpp
int x = 10;
int* ptr = &x;  // ptr lưu địa chỉ của x

cout << *ptr;   // In ra 10 (giá trị của x)
*ptr = 20;      // Thay đổi giá trị của x thành 20
```

#### 3.3.2 Toán tử & (Address-of operator)

Toán tử `&` dùng để lấy địa chỉ của một biến:

```cpp
int x = 5;
int* ptr = &x;  // ptr lưu địa chỉ của x

cout << &x;     // In địa chỉ của x
cout << ptr;    // In địa chỉ của x (giống nhau)
```

**Ví dụ chi tiết:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 100;
    int* ptr = &x;

    cout << "Gia tri cua x: " << x << endl;
    cout << "Dia chi cua x: " << &x << endl;
    cout << "Gia tri cua ptr: " << ptr << endl;
    cout << "Gia tri ma ptr tro den: " << *ptr << endl;

    // Thay đổi giá trị thông qua con trỏ
    *ptr = 200;
    cout << "Gia tri moi cua x: " << x << endl;

    return 0;
}
```

### 3.4 Con trỏ và địa chỉ

**Kích thước con trỏ:**
```cpp
int x;
int* ptr = &x;

cout << "Kich thuoc int: " << sizeof(x) << endl;      // 4 bytes
cout << "Kich thuoc con tro: " << sizeof(ptr) << endl; // 4 hoặc 8 bytes
```

**Con trỏ NULL:**
```cpp
int* ptr = nullptr;  // C++11
int* ptr2 = NULL;    // Cách cũ
int* ptr3 = 0;       // Cách cũ

// Kiểm tra con trỏ NULL
if (ptr == nullptr) {
    cout << "Con tro rong" << endl;
}
```

### 3.5 Một số phép toán trên con trỏ

#### 3.5.1 Khởi tạo
```cpp
int x = 10;
int* ptr1 = &x;        // Khởi tạo với địa chỉ
int* ptr2 = nullptr;   // Khởi tạo rỗng
```

#### 3.5.2 Truy xuất bằng toán tử *
```cpp
int x = 5;
int* ptr = &x;
cout << *ptr;  // In ra 5
```

#### 3.5.3 Nhập/xuất
```cpp
int x;
int* ptr = &x;

// Nhập
cout << "Nhap gia tri: ";
cin >> *ptr;  // Nhập vào biến x thông qua con trỏ

// Xuất
cout << "Gia tri: " << *ptr << endl;
```

#### 3.5.4 Gán
```cpp
int x = 10, y = 20;
int* ptr1 = &x;
int* ptr2 = &y;

ptr1 = ptr2;     // ptr1 trỏ đến y
*ptr1 = *ptr2;   // Gán giá trị của y cho x
```

#### 3.5.5 So sánh
```cpp
int arr[5] = {1, 2, 3, 4, 5};
int* ptr1 = &arr[0];
int* ptr2 = &arr[2];

if (ptr1 < ptr2) {
    cout << "ptr1 tro den phan tu truoc ptr2" << endl;
}
```

#### 3.5.6 Phép toán số học
```cpp
int arr[5] = {10, 20, 30, 40, 50};
int* ptr = arr;

cout << *ptr << endl;      // 10
ptr++;                     // Tăng con trỏ lên 1
cout << *ptr << endl;      // 20

ptr += 2;                  // Tăng con trỏ lên 2
cout << *ptr << endl;      // 40

ptr--;                     // Giảm con trỏ xuống 1
cout << *ptr << endl;      // 30
```

### 3.6 Toán tử new và delete

**Cấp phát bộ nhớ động với new:**
```cpp
// Cấp phát cho một biến
int* ptr = new int;
*ptr = 100;

// Cấp phát cho mảng
int* arr = new int[10];
for (int i = 0; i < 10; i++) {
    arr[i] = i * 10;
}
```

**Giải phóng bộ nhớ với delete:**
```cpp
// Giải phóng một biến
delete ptr;

// Giải phóng mảng
delete[] arr;
```

**Ví dụ hoàn chỉnh:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;

    // Cấp phát mảng động
    int* arr = new int[n];

    // Nhập dữ liệu
    for (int i = 0; i < n; i++) {
        cout << "arr[" << i << "] = ";
        cin >> arr[i];
    }

    // Xuất dữ liệu
    cout << "Mang vua nhap: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Giải phóng bộ nhớ
    delete[] arr;

    return 0;
}
```

### 3.7 Cấp phát động (Dynamic Allocation)

#### 3.7.1 Giới thiệu cấp phát động

**Khái niệm:**
- Cấp phát động là việc cấp phát bộ nhớ trong thời gian chạy chương trình (runtime)
- Khác với cấp phát tĩnh (khai báo mảng với kích thước cố định), cấp phát động cho phép xác định kích thước bộ nhớ khi chương trình đang chạy
- Bộ nhớ được cấp phát từ vùng nhớ Heap

**So sánh cấp phát tĩnh và động:**

| Tiêu chí | Cấp phát tĩnh | Cấp phát động |
|----------|---------------|---------------|
| Kích thước | Cố định tại compile-time | Linh hoạt tại runtime |
| Vùng nhớ | Stack | Heap |
| Tốc độ | Nhanh hơn | Chậm hơn một chút |
| Quản lý | Tự động giải phóng | Phải giải phóng thủ công |
| Giới hạn | Kích thước stack giới hạn | Kích thước heap lớn hơn |

#### 3.7.2 Cấp phát động mảng 1 chiều

**Cú pháp:**
```cpp
// Cấp phát
<kiểu_dữ_liệu>* <tên_con_trỏ> = new <kiểu_dữ_liệu>[kích_thước];

// Giải phóng
delete[] <tên_con_trỏ>;
```

**Ví dụ cơ bản:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;

    // Cấp phát mảng động
    int* arr = new int[n];

    // Nhập dữ liệu
    cout << "Nhap cac phan tu:\n";
    for (int i = 0; i < n; i++) {
        cout << "arr[" << i << "] = ";
        cin >> arr[i];
    }

    // Xuất dữ liệu
    cout << "Mang vua nhap: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Giải phóng bộ nhớ
    delete[] arr;
    arr = nullptr;  // Tốt nhất nên gán nullptr sau khi delete

    return 0;
}
```

**Ví dụ nâng cao - Quản lý danh sách sinh viên:**
```cpp
#include <iostream>
#include <cstring>
using namespace std;

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    float diemTB;
};

void nhapDanhSach(SinhVien* ds, int n) {
    for (int i = 0; i < n; i++) {
        cout << "\nNhap sinh vien thu " << i + 1 << ":\n";
        cout << "Ma SV: ";
        cin >> ds[i].maSV;
        cin.ignore();
        cout << "Ho ten: ";
        cin.getline(ds[i].hoTen, 50);
        cout << "Diem TB: ";
        cin >> ds[i].diemTB;
    }
}

void xuatDanhSach(SinhVien* ds, int n) {
    cout << "\n--- DANH SACH SINH VIEN ---\n";
    for (int i = 0; i < n; i++) {
        cout << ds[i].maSV << " - " << ds[i].hoTen
             << " - " << ds[i].diemTB << endl;
    }
}

int main() {
    int n;
    cout << "Nhap so luong sinh vien: ";
    cin >> n;

    // Cấp phát động cho mảng struct
    SinhVien* danhSach = new SinhVien[n];

    nhapDanhSach(danhSach, n);
    xuatDanhSach(danhSach, n);

    // Giải phóng bộ nhớ
    delete[] danhSach;
    danhSach = nullptr;

    return 0;
}
```

#### 3.7.3 Cấp phát động mảng nhiều chiều

**A. Cấp phát mảng 2 chiều - Cách 1: Sử dụng con trỏ cấp 2**

```cpp
#include <iostream>
using namespace std;

int main() {
    int m, n;
    cout << "Nhap so hang: ";
    cin >> m;
    cout << "Nhap so cot: ";
    cin >> n;

    // Cấp phát mảng 2 chiều
    int** matrix = new int*[m];  // Cấp phát m con trỏ
    for (int i = 0; i < m; i++) {
        matrix[i] = new int[n];  // Mỗi con trỏ trỏ đến 1 mảng n phần tử
    }

    // Nhập dữ liệu
    cout << "Nhap cac phan tu:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << "matrix[" << i << "][" << j << "] = ";
            cin >> matrix[i][j];
        }
    }

    // Xuất dữ liệu
    cout << "\nMa tran:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << "\n";
    }

    // Giải phóng bộ nhớ
    for (int i = 0; i < m; i++) {
        delete[] matrix[i];  // Giải phóng từng hàng
    }
    delete[] matrix;  // Giải phóng mảng con trỏ
    matrix = nullptr;

    return 0;
}
```

**B. Cấp phát mảng 2 chiều - Cách 2: Sử dụng mảng 1 chiều**

```cpp
#include <iostream>
using namespace std;

int main() {
    int m, n;
    cout << "Nhap so hang va cot: ";
    cin >> m >> n;

    // Cấp phát mảng 1 chiều, truy xuất như mảng 2 chiều
    int* matrix = new int[m * n];

    // Nhập dữ liệu
    cout << "Nhap cac phan tu:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << "matrix[" << i << "][" << j << "] = ";
            cin >> matrix[i * n + j];  // Công thức: [i][j] = i * n + j
        }
    }

    // Xuất dữ liệu
    cout << "\nMa tran:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i * n + j] << "\t";
        }
        cout << "\n";
    }

    // Giải phóng bộ nhớ (đơn giản hơn)
    delete[] matrix;
    matrix = nullptr;

    return 0;
}
```

**C. Cấp phát mảng 3 chiều**

```cpp
#include <iostream>
using namespace std;

int main() {
    int x, y, z;
    cout << "Nhap kich thuoc (x y z): ";
    cin >> x >> y >> z;

    // Cấp phát mảng 3 chiều
    int*** arr3D = new int**[x];
    for (int i = 0; i < x; i++) {
        arr3D[i] = new int*[y];
        for (int j = 0; j < y; j++) {
            arr3D[i][j] = new int[z];
        }
    }

    // Gán giá trị
    int value = 0;
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < y; j++) {
            for (int k = 0; k < z; k++) {
                arr3D[i][j][k] = value++;
            }
        }
    }

    // In một số giá trị
    cout << "arr3D[0][0][0] = " << arr3D[0][0][0] << endl;
    cout << "arr3D[1][1][1] = " << arr3D[1][1][1] << endl;

    // Giải phóng bộ nhớ
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < y; j++) {
            delete[] arr3D[i][j];
        }
        delete[] arr3D[i];
    }
    delete[] arr3D;
    arr3D = nullptr;

    return 0;
}
```

#### 3.7.4 Lợi ích của cấp phát động

**1. Tiết kiệm bộ nhớ:**
```cpp
// Không hiệu quả - cấp phát tĩnh
int arr[10000];  // Luôn chiếm 40KB ngay cả khi chỉ dùng 10 phần tử

// Hiệu quả - cấp phát động
int n;
cin >> n;  // Giả sử n = 10
int* arr = new int[n];  // Chỉ chiếm 40 bytes
```

**2. Linh hoạt về kích thước:**
```cpp
// Có thể thay đổi kích thước trong quá trình chạy
int n;
cout << "Ban muon nhap bao nhieu so? ";
cin >> n;
int* numbers = new int[n];  // Kích thước phụ thuộc vào input người dùng
```

**3. Vượt qua giới hạn Stack:**
```cpp
// Stack có giới hạn (thường ~1-8MB)
// int bigArray[10000000];  // Có thể gây stack overflow!

// Heap có kích thước lớn hơn nhiều
int* bigArray = new int[10000000];  // OK - dùng heap
```

**4. Trả về mảng từ hàm:**
```cpp
int* createArray(int n) {
    // Mảng cục bộ sẽ bị hủy khi thoát hàm
    // int arr[100];  // KHÔNG được!

    // Mảng động vẫn tồn tại sau khi thoát hàm
    int* arr = new int[n];  // OK
    for (int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }
    return arr;  // Trả về con trỏ
}

int main() {
    int* myArray = createArray(5);
    // Sử dụng myArray...
    delete[] myArray;  // Nhớ giải phóng
    return 0;
}
```

**5. Tạo cấu trúc dữ liệu phức tạp:**
```cpp
// Danh sách liên kết (Linked List)
struct Node {
    int data;
    Node* next;
};

Node* createNode(int value) {
    Node* newNode = new Node;
    newNode->data = value;
    newNode->next = nullptr;
    return newNode;
}

// Cây nhị phân (Binary Tree)
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
};

TreeNode* createTreeNode(int value) {
    TreeNode* node = new TreeNode;
    node->data = value;
    node->left = nullptr;
    node->right = nullptr;
    return node;
}
```

#### 3.7.5 Khi nào nên sử dụng cấp phát động

**NÊN sử dụng cấp phát động khi:**

1. **Không biết kích thước trước:**
```cpp
// Ví dụ: Đọc dữ liệu từ file hoặc từ người dùng
int n;
cout << "Nhap so luong phan tu: ";
cin >> n;
int* arr = new int[n];
```

2. **Kích thước lớn (có thể vượt quá stack):**
```cpp
// Mảng rất lớn
int* bigData = new int[1000000];  // 4MB - phù hợp dùng heap
```

3. **Cần dữ liệu tồn tại ngoài phạm vi hàm:**
```cpp
int* getData() {
    int* result = new int[100];
    // Xử lý dữ liệu...
    return result;  // OK - dữ liệu vẫn tồn tại
}
```

4. **Tạo cấu trúc dữ liệu động:**
```cpp
// Linked list, tree, graph, etc.
struct Node {
    int data;
    Node* next;
};

Node* head = new Node;  // Tạo node đầu tiên
```

5. **Quản lý tài nguyên hiệu quả:**
```cpp
// Chỉ cấp phát khi cần, giải phóng khi không dùng
if (needProcessing) {
    int* tempData = new int[10000];
    // Xử lý...
    delete[] tempData;  // Giải phóng ngay
}
```

**KHÔNG NÊN sử dụng cấp phát động khi:**

1. **Kích thước nhỏ và cố định:**
```cpp
// Tốt hơn dùng mảng tĩnh
int small[10];  // Tốt hơn
// int* small = new int[10];  // Không cần thiết
```

2. **Dữ liệu tạm trong hàm:**
```cpp
void processData() {
    int temp[100];  // OK - tự động giải phóng khi thoát hàm
    // Không cần: int* temp = new int[100];
}
```

3. **Không muốn quản lý bộ nhớ thủ công:**
```cpp
// Nếu có thể, dùng vector (C++ STL)
#include <vector>
vector<int> arr(n);  // Tự động quản lý bộ nhớ, an toàn hơn
```

#### 3.7.6 Lưu ý quan trọng khi sử dụng cấp phát động

**1. Luôn kiểm tra cấp phát thành công:**
```cpp
int* arr = new(nothrow) int[n];
if (arr == nullptr) {
    cout << "Khong du bo nho!" << endl;
    return 1;
}
```

**2. Luôn giải phóng bộ nhớ:**
```cpp
int* arr = new int[10];
// Sử dụng arr...
delete[] arr;  // BẮT BUỘC!
arr = nullptr;  // Tốt nhất nên gán nullptr
```

**3. Không được truy xuất sau khi delete:**
```cpp
int* arr = new int[10];
delete[] arr;
// cout << arr[0];  // LỖI! - Undefined behavior
```

**4. Không được delete nhiều lần:**
```cpp
int* ptr = new int;
delete ptr;
// delete ptr;  // LỖI! - Double free
ptr = nullptr;  // Gán nullptr để an toàn
```

**5. Nhớ dùng delete[] cho mảng:**
```cpp
int* arr = new int[10];
delete[] arr;  // ĐÚNG - dùng delete[]
// delete arr;  // SAI - chỉ giải phóng 1 phần tử
```

**6. Tránh memory leak:**
```cpp
// SAI - memory leak
void badFunction() {
    int* arr = new int[100];
    // Quên delete[] arr
}  // Bộ nhớ bị rò rỉ!

// ĐÚNG
void goodFunction() {
    int* arr = new int[100];
    // Sử dụng arr...
    delete[] arr;  // Giải phóng trước khi thoát
}
```

**7. Sử dụng smart pointer (C++11 trở lên):**
```cpp
#include <memory>

// unique_ptr - tự động giải phóng
unique_ptr<int[]> arr(new int[10]);
// Không cần delete[], tự động giải phóng khi ra khỏi scope

// shared_ptr - quản lý tham chiếu
shared_ptr<int> ptr = make_shared<int>(100);
```

**Ví dụ tổng hợp:**
```cpp
#include <iostream>
using namespace std;

// Hàm cấp phát và khởi tạo mảng
int* createAndInitArray(int n, int initValue = 0) {
    int* arr = new(nothrow) int[n];
    if (arr == nullptr) {
        return nullptr;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = initValue;
    }
    return arr;
}

// Hàm tái cấp phát mảng với kích thước mới
int* resizeArray(int* oldArr, int oldSize, int newSize) {
    int* newArr = new(nothrow) int[newSize];
    if (newArr == nullptr) {
        return nullptr;
    }

    // Copy dữ liệu cũ
    int copySize = (oldSize < newSize) ? oldSize : newSize;
    for (int i = 0; i < copySize; i++) {
        newArr[i] = oldArr[i];
    }

    // Khởi tạo phần mở rộng
    for (int i = oldSize; i < newSize; i++) {
        newArr[i] = 0;
    }

    delete[] oldArr;  // Giải phóng mảng cũ
    return newArr;
}

int main() {
    int n = 5;
    int* arr = createAndInitArray(n, 10);

    if (arr == nullptr) {
        cout << "Khong du bo nho!" << endl;
        return 1;
    }

    cout << "Mang ban dau: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Tăng kích thước mảng
    int newSize = 10;
    arr = resizeArray(arr, n, newSize);

    if (arr == nullptr) {
        cout << "Khong du bo nho de mo rong!" << endl;
        return 1;
    }

    cout << "Mang sau khi mo rong: ";
    for (int i = 0; i < newSize; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Giải phóng bộ nhớ
    delete[] arr;
    arr = nullptr;

    return 0;
}
```

### 3.8 Con trỏ và mảng

**Quan hệ giữa con trỏ và mảng:**
```cpp
int arr[5] = {10, 20, 30, 40, 50};
int* ptr = arr;  // Tên mảng là con trỏ đến phần tử đầu tiên

cout << arr[0] << endl;    // 10
cout << *ptr << endl;      // 10
cout << *(ptr + 1) << endl; // 20
cout << ptr[2] << endl;    // 30
```

**Duyệt mảng bằng con trỏ:**
```cpp
int arr[5] = {1, 2, 3, 4, 5};
int* ptr = arr;

// Cách 1
for (int i = 0; i < 5; i++) {
    cout << *(ptr + i) << " ";
}

// Cách 2
for (int i = 0; i < 5; i++) {
    cout << *ptr << " ";
    ptr++;
}
```

**Con trỏ và mảng hai chiều:**
```cpp
int arr[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Con trỏ đến mảng
int (*ptr)[4] = arr;

cout << ptr[1][2] << endl;  // 7
cout << *(*(ptr + 1) + 2) << endl;  // 7
```

### 3.9 Hàm có tham số con trỏ

**Truyền con trỏ vào hàm:**
```cpp
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    cout << "Truoc: x = " << x << ", y = " << y << endl;

    swap(&x, &y);

    cout << "Sau: x = " << x << ", y = " << y << endl;
    return 0;
}
```

**Truyền mảng vào hàm bằng con trỏ:**
```cpp
void printArray(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void inputArray(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        cout << "arr[" << i << "] = ";
        cin >> arr[i];
    }
}

int main() {
    int arr[5];
    inputArray(arr, 5);
    printArray(arr, 5);
    return 0;
}
```

**Hàm trả về con trỏ:**
```cpp
int* createArray(int n) {
    int* arr = new int[n];
    for (int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }
    return arr;
}

int main() {
    int* myArray = createArray(5);

    for (int i = 0; i < 5; i++) {
        cout << myArray[i] << " ";
    }

    delete[] myArray;  // Nhớ giải phóng bộ nhớ
    return 0;
}
```

---

## CHƯƠNG 4: CHUỖI KÝ TỰ

### 4.1 Giới thiệu

**Khái niệm:**
- Chuỗi ký tự là một dãy các ký tự liên tiếp
- Trong C++, có hai cách biểu diễn chuỗi:
  1. Mảng ký tự kiểu C (C-string)
  2. Lớp string của C++

**Đặc điểm chuỗi kiểu C:**
- Kết thúc bằng ký tự NULL ('\0')
- Được lưu trữ trong mảng ký tự

### 4.2 Khai báo chuỗi

#### 4.2.1 Sử dụng mảng

```cpp
// Khai báo và khởi tạo
char str1[20] = "Hello";
char str2[] = "World";
char str3[10] = {'H', 'i', '\0'};

// Khai báo mảng rỗng
char str4[100];
```

#### 4.2.2 Sử dụng con trỏ

```cpp
// Con trỏ đến hằng chuỗi
char* str1 = "Hello";  // Không nên sửa đổi

// Con trỏ đến chuỗi có thể sửa đổi
char buffer[20] = "Hello";
char* str2 = buffer;
```

**Sử dụng lớp string:**
```cpp
#include <string>
using namespace std;

string str1 = "Hello";
string str2("World");
string str3;  // Chuỗi rỗng
```

### 4.3 Nhập/xuất chuỗi

#### 4.3.1 Xuất chuỗi

```cpp
#include <iostream>
using namespace std;

int main() {
    char str1[20] = "Hello World";
    string str2 = "C++ Programming";

    // Xuất chuỗi kiểu C
    cout << str1 << endl;

    // Xuất chuỗi kiểu string
    cout << str2 << endl;

    return 0;
}
```

#### 4.3.2 Nhập chuỗi

**Toán tử >> và cin:**
- Chỉ đọc đến khoảng trắng đầu tiên
```cpp
char str[100];
string s;

cout << "Nhap chuoi: ";
cin >> str;   // Dừng khi gặp khoảng trắng
cin >> s;     // Dừng khi gặp khoảng trắng
```

**Hàm thành viên ignore():**
```cpp
cin.ignore();  // Bỏ qua 1 ký tự
cin.ignore(100, '\n');  // Bỏ qua đến 100 ký tự hoặc đến khi gặp '\n'
```

**Hàm thành viên get():**
```cpp
char ch;
cin.get(ch);  // Đọc 1 ký tự

char str[100];
cin.get(str, 100);  // Đọc chuỗi, dừng khi gặp '\n'
```

**Hàm thành viên getline():**
```cpp
// Với chuỗi kiểu C
char str[100];
cin.getline(str, 100);  // Đọc cả dòng

// Với string
string s;
getline(cin, s);  // Đọc cả dòng
```

**Ví dụ:**
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    char name[50];
    string address;

    cout << "Nhap ho ten: ";
    cin.getline(name, 50);

    cout << "Nhap dia chi: ";
    getline(cin, address);

    cout << "\nThong tin:\n";
    cout << "Ho ten: " << name << endl;
    cout << "Dia chi: " << address << endl;

    return 0;
}
```

### 4.4 Một số phép toán trên chuỗi

#### 4.4.1 Truy xuất từng phần tử

```cpp
char str[] = "Hello";

// Truy xuất bằng chỉ số
for (int i = 0; i < 5; i++) {
    cout << str[i] << " ";
}

// Với string
string s = "World";
for (int i = 0; i < s.length(); i++) {
    cout << s[i] << " ";
}
```

#### 4.4.2 Xác định chiều dài

```cpp
#include <cstring>

char str[] = "Hello";
int len = strlen(str);  // 5

string s = "World";
int length = s.length();  // 5
int size = s.size();      // 5
```

#### 4.4.3 Gán chuỗi

**Với chuỗi kiểu C:**
```cpp
#include <cstring>

char str1[20];
char str2[] = "Hello";

strcpy(str1, str2);  // str1 = "Hello"
```

**Với string:**
```cpp
string s1, s2 = "Hello";
s1 = s2;  // Gán trực tiếp
```

#### 4.4.4 Hàm thành viên

**Với string:**
```cpp
string s = "Hello";

// Thêm chuỗi
s.append(" World");   // "Hello World"
s += "!";            // "Hello World!"

// Chèn chuỗi
s.insert(5, ",");    // "Hello, World!"

// Xóa
s.erase(5, 1);       // "Hello World!"

// Tìm kiếm
int pos = s.find("World");  // Vị trí của "World"

// Lấy chuỗi con
string sub = s.substr(0, 5);  // "Hello"

// So sánh
if (s.compare("Hello World!") == 0) {
    cout << "Giong nhau" << endl;
}
```

### 4.5 Hàm thư viện xử lý chuỗi

**Thư viện `<cstring>` cho chuỗi kiểu C:**

```cpp
#include <cstring>

// strlen() - Độ dài chuỗi
char str[] = "Hello";
int len = strlen(str);

// strcpy() - Sao chép chuỗi
char dest[20];
strcpy(dest, str);

// strcat() - Nối chuỗi
char str1[20] = "Hello";
char str2[] = " World";
strcat(str1, str2);  // "Hello World"

// strcmp() - So sánh chuỗi
int result = strcmp(str1, str2);
// = 0: bằng nhau
// > 0: str1 > str2
// < 0: str1 < str2

// strchr() - Tìm ký tự
char* pos = strchr(str, 'l');

// strstr() - Tìm chuỗi con
char* substr = strstr(str1, "World");
```

**Ví dụ tổng hợp:**
```cpp
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main() {
    // Chuỗi kiểu C
    char str1[50] = "Hello";
    char str2[50];

    strcpy(str2, str1);
    strcat(str1, " World");

    cout << "str1: " << str1 << endl;
    cout << "Do dai: " << strlen(str1) << endl;

    // Chuỗi kiểu string
    string s1 = "C++";
    string s2 = " Programming";

    s1 += s2;
    cout << "s1: " << s1 << endl;
    cout << "Do dai: " << s1.length() << endl;

    return 0;
}
```

**Hàm xử lý ký tự `<cctype>`:**
```cpp
#include <cctype>

char ch = 'a';

// Kiểm tra
isalpha(ch);   // Ký tự chữ cái
isdigit(ch);   // Ký tự số
isalnum(ch);   // Chữ cái hoặc số
isspace(ch);   // Khoảng trắng
isupper(ch);   // Chữ hoa
islower(ch);   // Chữ thường

// Chuyển đổi
toupper(ch);   // Chuyển sang chữ hoa
tolower(ch);   // Chuyển sang chữ thường
```

---

## CHƯƠNG 5: KIỂU DỮ LIỆU NGƯỜI DÙNG

### 5.1 Khai báo typedef

**Khái niệm:**
- `typedef` cho phép tạo tên mới cho kiểu dữ liệu đã có
- Giúp code dễ đọc và bảo trì hơn

**Cú pháp:**
```cpp
typedef <kiểu_dữ_liệu_cũ> <tên_mới>;
```

**Ví dụ:**
```cpp
// Tạo tên mới cho kiểu dữ liệu cơ bản
typedef unsigned int uint;
typedef long long ll;

uint x = 10;
ll y = 1000000000LL;

// Tạo tên mới cho con trỏ
typedef int* IntPtr;
IntPtr p1, p2;  // Cả hai đều là con trỏ

// Tạo tên mới cho mảng
typedef int Array10[10];
Array10 arr;  // Mảng 10 phần tử
```

### 5.2 Kiểu struct

#### 5.2.1 Khai báo

**Cú pháp:**
```cpp
struct <tên_struct> {
    <kiểu_dữ_liệu> <tên_thành_viên_1>;
    <kiểu_dữ_liệu> <tên_thành_viên_2>;
    ...
};
```

**Ví dụ:**
```cpp
struct SinhVien {
    char maSV[10];
    char hoTen[50];
    int namSinh;
    float diemTB;
};

struct Diem {
    float x;
    float y;
};

struct HinhChuNhat {
    Diem topLeft;
    Diem bottomRight;
};
```

**Khai báo biến:**
```cpp
// Cách 1
struct SinhVien sv1;

// Cách 2 (khuyến nghị trong C++)
SinhVien sv2;

// Khai báo và khởi tạo
SinhVien sv3 = {"SV001", "Nguyen Van A", 2005, 8.5};

// Khai báo mảng
SinhVien danhSach[100];
```

#### 5.2.2 Truy xuất các thành phần

**Toán tử dấu chấm (.):**
```cpp
SinhVien sv;

// Gán giá trị
strcpy(sv.maSV, "SV001");
strcpy(sv.hoTen, "Nguyen Van A");
sv.namSinh = 2005;
sv.diemTB = 8.5;

// Đọc giá trị
cout << "Ma SV: " << sv.maSV << endl;
cout << "Ho ten: " << sv.hoTen << endl;
cout << "Nam sinh: " << sv.namSinh << endl;
cout << "Diem TB: " << sv.diemTB << endl;
```

**Toán tử mũi tên (->) với con trỏ:**
```cpp
SinhVien* ptr = new SinhVien;

// Sử dụng ->
strcpy(ptr->maSV, "SV002");
ptr->namSinh = 2006;

// Hoặc sử dụng (*)
strcpy((*ptr).maSV, "SV002");
(*ptr).namSinh = 2006;

delete ptr;
```

**Ví dụ hoàn chỉnh:**
```cpp
#include <iostream>
#include <cstring>
using namespace std;

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    int namSinh;
    float diemTB;
};

// Hàm nhập thông tin sinh viên
void nhapSV(SinhVien& sv) {
    cout << "Nhap ma SV: ";
    cin >> sv.maSV;
    cin.ignore();
    cout << "Nhap ho ten: ";
    cin.getline(sv.hoTen, 50);
    cout << "Nhap nam sinh: ";
    cin >> sv.namSinh;
    cout << "Nhap diem TB: ";
    cin >> sv.diemTB;
}

// Hàm xuất thông tin sinh viên
void xuatSV(const SinhVien& sv) {
    cout << "\n--- Thong tin sinh vien ---\n";
    cout << "Ma SV: " << sv.maSV << endl;
    cout << "Ho ten: " << sv.hoTen << endl;
    cout << "Nam sinh: " << sv.namSinh << endl;
    cout << "Diem TB: " << sv.diemTB << endl;
}

// Hàm nhập danh sách sinh viên
void nhapDanhSach(SinhVien ds[], int n) {
    for (int i = 0; i < n; i++) {
        cout << "\nNhap sinh vien thu " << i + 1 << ":\n";
        nhapSV(ds[i]);
    }
}

// Hàm xuất danh sách sinh viên
void xuatDanhSach(const SinhVien ds[], int n) {
    for (int i = 0; i < n; i++) {
        cout << "\nSinh vien thu " << i + 1 << ":";
        xuatSV(ds[i]);
    }
}

// Hàm tìm sinh viên có điểm TB cao nhất
SinhVien timSVDiemCaoNhat(const SinhVien ds[], int n) {
    SinhVien max = ds[0];
    for (int i = 1; i < n; i++) {
        if (ds[i].diemTB > max.diemTB) {
            max = ds[i];
        }
    }
    return max;
}

int main() {
    int n;
    cout << "Nhap so luong sinh vien: ";
    cin >> n;

    SinhVien* danhSach = new SinhVien[n];

    nhapDanhSach(danhSach, n);
    xuatDanhSach(danhSach, n);

    SinhVien svGioi = timSVDiemCaoNhat(danhSach, n);
    cout << "\n\nSinh vien co diem cao nhat:";
    xuatSV(svGioi);

    delete[] danhSach;
    return 0;
}
```

**Struct lồng nhau:**
```cpp
struct DiaChi {
    char soNha[20];
    char duong[50];
    char quan[30];
    char thanhPho[30];
};

struct NhanVien {
    char maNV[10];
    char hoTen[50];
    DiaChi diaChi;
    float luong;
};

int main() {
    NhanVien nv;

    strcpy(nv.maNV, "NV001");
    strcpy(nv.hoTen, "Tran Van B");
    strcpy(nv.diaChi.soNha, "123");
    strcpy(nv.diaChi.duong, "Le Loi");
    strcpy(nv.diaChi.quan, "Quan 1");
    strcpy(nv.diaChi.thanhPho, "TP.HCM");
    nv.luong = 10000000;

    return 0;
}
```

### 5.3 Kiểu dữ liệu enum

**Khái niệm:**
- `enum` (enumeration) là kiểu dữ liệu liệt kê
- Giúp code dễ đọc hơn khi làm việc với tập hợp các hằng số liên quan

**Cú pháp:**
```cpp
enum <tên_enum> {
    <hằng_1>,
    <hằng_2>,
    ...
};
```

**Ví dụ:**
```cpp
enum Color {
    RED,      // 0
    GREEN,    // 1
    BLUE,     // 2
    YELLOW    // 3
};

enum Month {
    JAN = 1,  // Gán giá trị tường minh
    FEB,      // 2
    MAR,      // 3
    APR,      // 4
    MAY,      // 5
    JUN,      // 6
    JUL,      // 7
    AUG,      // 8
    SEP,      // 9
    OCT,      // 10
    NOV,      // 11
    DEC       // 12
};

enum DayOfWeek {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
};
```

**Sử dụng enum:**
```cpp
#include <iostream>
using namespace std;

enum TrangThai {
    DANG_HOC,
    DA_TOT_NGHIEP,
    BO_HOC,
    BAO_LUU
};

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    TrangThai trangThai;
};

void inTrangThai(TrangThai tt) {
    switch (tt) {
        case DANG_HOC:
            cout << "Dang hoc";
            break;
        case DA_TOT_NGHIEP:
            cout << "Da tot nghiep";
            break;
        case BO_HOC:
            cout << "Bo hoc";
            break;
        case BAO_LUU:
            cout << "Bao luu";
            break;
    }
}

int main() {
    SinhVien sv;
    strcpy(sv.maSV, "SV001");
    strcpy(sv.hoTen, "Nguyen Van A");
    sv.trangThai = DANG_HOC;

    cout << "Trang thai: ";
    inTrangThai(sv.trangThai);

    return 0;
}
```

**Enum class (C++11):**
```cpp
enum class TrafficLight {
    RED,
    YELLOW,
    GREEN
};

int main() {
    TrafficLight light = TrafficLight::RED;

    if (light == TrafficLight::RED) {
        cout << "Dung lai!" << endl;
    }

    return 0;
}
```

---

## CHƯƠNG 6: TẬP TIN VÀ LUỒNG

### 6.1 Giới thiệu

**Khái niệm:**
- Tập tin (file) là nơi lưu trữ dữ liệu trên đĩa
- Luồng (stream) là kênh truyền dữ liệu giữa chương trình và thiết bị ngoại vi

**Phân loại tập tin:**
1. **Tập tin văn bản (Text file):** Lưu dữ liệu dạng ký tự ASCII
2. **Tập tin nhị phân (Binary file):** Lưu dữ liệu dưới dạng nhị phân

**Thư viện:**
```cpp
#include <fstream>  // File stream
```

### 6.2 Nhập/xuất chuẩn

#### 6.2.1 Lớp istream

**Các hàm quan trọng:**
```cpp
// Đọc dữ liệu
cin >> variable;

// Đọc ký tự
char ch;
cin.get(ch);

// Đọc dòng
char str[100];
cin.getline(str, 100);

// Bỏ qua ký tự
cin.ignore();
cin.ignore(100, '\n');

// Kiểm tra trạng thái
cin.good();  // Luồng hoạt động tốt
cin.eof();   // Đã đến cuối file
cin.fail();  // Thao tác thất bại
cin.bad();   // Lỗi nghiêm trọng

// Xóa trạng thái lỗi
cin.clear();
```

#### 6.2.2 Lớp ostream

**Các hàm quan trọng:**
```cpp
// Xuất dữ liệu
cout << variable;

// Xuất ký tự
cout.put('A');

// Định dạng
cout.width(10);      // Độ rộng
cout.precision(2);   // Độ chính xác
cout.fill('0');      // Ký tự điền

// Manipulator
#include <iomanip>
cout << setw(10) << setprecision(2) << fixed;
```

### 6.3 Nhập/xuất tập tin

**Ba lớp chính:**
1. `ifstream`: Đọc từ tập tin (input file stream)
2. `ofstream`: Ghi vào tập tin (output file stream)
3. `fstream`: Đọc và ghi tập tin (file stream)

**Chế độ mở file:**
```cpp
ios::in      // Mở để đọc
ios::out     // Mở để ghi (xóa nội dung cũ)
ios::app     // Mở để ghi (thêm vào cuối)
ios::binary  // Mở ở chế độ nhị phân
ios::trunc   // Xóa nội dung file cũ
```

#### Lớp ifstream - Đọc tập tin

**Cú pháp:**
```cpp
#include <fstream>

ifstream fin;
fin.open("filename.txt");

// Hoặc
ifstream fin("filename.txt");
```

**Ví dụ:**
```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream fin("input.txt");

    if (!fin) {
        cout << "Khong mo duoc file!" << endl;
        return 1;
    }

    int x;
    while (fin >> x) {
        cout << x << " ";
    }

    fin.close();
    return 0;
}
```

#### Lớp ofstream - Ghi tập tin

**Cú pháp:**
```cpp
ofstream fout;
fout.open("filename.txt");

// Hoặc
ofstream fout("filename.txt");
```

**Ví dụ:**
```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream fout("output.txt");

    if (!fout) {
        cout << "Khong tao duoc file!" << endl;
        return 1;
    }

    fout << "Hello, File!" << endl;
    fout << "This is a test." << endl;

    for (int i = 1; i <= 10; i++) {
        fout << i << " ";
    }

    fout.close();
    return 0;
}
```

#### Đọc/ghi tập tin văn bản

**Đọc từng dòng:**
```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream fin("data.txt");
    string line;

    while (getline(fin, line)) {
        cout << line << endl;
    }

    fin.close();
    return 0;
}
```

**Ghi dữ liệu có định dạng:**
```cpp
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    float diemTB;
};

int main() {
    ofstream fout("sinhvien.txt");

    SinhVien sv = {"SV001", "Nguyen Van A", 8.5};

    fout << sv.maSV << endl;
    fout << sv.hoTen << endl;
    fout << fixed << setprecision(2) << sv.diemTB << endl;

    fout.close();
    return 0;
}
```

**Đọc dữ liệu có định dạng:**
```cpp
#include <iostream>
#include <fstream>
using namespace std;

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    float diemTB;
};

int main() {
    ifstream fin("sinhvien.txt");
    SinhVien sv;

    fin >> sv.maSV;
    fin.ignore();
    fin.getline(sv.hoTen, 50);
    fin >> sv.diemTB;

    cout << "Ma SV: " << sv.maSV << endl;
    cout << "Ho ten: " << sv.hoTen << endl;
    cout << "Diem TB: " << sv.diemTB << endl;

    fin.close();
    return 0;
}
```

#### Đọc/ghi tập tin nhị phân

**Ghi tập tin nhị phân:**
```cpp
#include <iostream>
#include <fstream>
using namespace std;

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    float diemTB;
};

int main() {
    ofstream fout("sinhvien.dat", ios::binary);

    SinhVien sv = {"SV001", "Nguyen Van A", 8.5};

    fout.write((char*)&sv, sizeof(SinhVien));

    fout.close();
    return 0;
}
```

**Đọc tập tin nhị phân:**
```cpp
#include <iostream>
#include <fstream>
using namespace std;

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    float diemTB;
};

int main() {
    ifstream fin("sinhvien.dat", ios::binary);
    SinhVien sv;

    fin.read((char*)&sv, sizeof(SinhVien));

    cout << "Ma SV: " << sv.maSV << endl;
    cout << "Ho ten: " << sv.hoTen << endl;
    cout << "Diem TB: " << sv.diemTB << endl;

    fin.close();
    return 0;
}
```

**Ghi/đọc nhiều bản ghi:**
```cpp
// Ghi
ofstream fout("students.dat", ios::binary);
SinhVien ds[3] = {
    {"SV001", "Nguyen Van A", 8.5},
    {"SV002", "Tran Thi B", 7.8},
    {"SV003", "Le Van C", 9.0}
};

for (int i = 0; i < 3; i++) {
    fout.write((char*)&ds[i], sizeof(SinhVien));
}
fout.close();

// Đọc
ifstream fin("students.dat", ios::binary);
SinhVien sv;

while (fin.read((char*)&sv, sizeof(SinhVien))) {
    cout << sv.maSV << " - " << sv.hoTen << " - " << sv.diemTB << endl;
}
fin.close();
```

### 6.4 Một số hàm thành viên của lớp fstream

**Hàm kiểm tra trạng thái:**
```cpp
ifstream fin("test.txt");

// Kiểm tra file có mở thành công không
if (fin.is_open()) {
    cout << "File da mo" << endl;
}

// Kiểm tra đã đến cuối file chưa
if (fin.eof()) {
    cout << "Het file" << endl;
}

// Kiểm tra có lỗi không
if (fin.fail()) {
    cout << "Co loi xay ra" << endl;
}

// Kiểm tra trạng thái tốt
if (fin.good()) {
    cout << "Luong hoat dong tot" << endl;
}
```

**Hàm di chuyển con trỏ file:**
```cpp
ifstream fin("data.txt");

// Di chuyển vị trí đọc
fin.seekg(0, ios::beg);     // Đầu file
fin.seekg(0, ios::end);     // Cuối file
fin.seekg(10, ios::cur);    // 10 bytes từ vị trí hiện tại

// Lấy vị trí hiện tại
int pos = fin.tellg();

ofstream fout("output.txt");

// Di chuyển vị trí ghi
fout.seekp(0, ios::beg);
fout.seekp(0, ios::end);
fout.seekp(10, ios::cur);

// Lấy vị trí ghi
int writePos = fout.tellp();
```

**Ví dụ tổng hợp:**
```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct SinhVien {
    char maSV[10];
    char hoTen[50];
    float diemTB;
};

// Ghi danh sách sinh viên vào file
void ghiFile(const char* filename, SinhVien ds[], int n) {
    ofstream fout(filename, ios::binary);

    if (!fout) {
        cout << "Khong tao duoc file!" << endl;
        return;
    }

    fout.write((char*)&n, sizeof(int));
    for (int i = 0; i < n; i++) {
        fout.write((char*)&ds[i], sizeof(SinhVien));
    }

    fout.close();
    cout << "Da ghi " << n << " sinh vien vao file." << endl;
}

// Đọc danh sách sinh viên từ file
void docFile(const char* filename) {
    ifstream fin(filename, ios::binary);

    if (!fin) {
        cout << "Khong mo duoc file!" << endl;
        return;
    }

    int n;
    fin.read((char*)&n, sizeof(int));

    cout << "\nDanh sach sinh vien:\n";
    SinhVien sv;
    for (int i = 0; i < n; i++) {
        fin.read((char*)&sv, sizeof(SinhVien));
        cout << sv.maSV << " - " << sv.hoTen << " - " << sv.diemTB << endl;
    }

    fin.close();
}

int main() {
    SinhVien ds[3] = {
        {"SV001", "Nguyen Van A", 8.5},
        {"SV002", "Tran Thi B", 7.8},
        {"SV003", "Le Van C", 9.0}
    };

    ghiFile("students.dat", ds, 3);
    docFile("students.dat");

    return 0;
}
```

---

## KẾT LUẬN

Tài liệu này đã trình bày đầy đủ các nội dung chính của môn Kỹ thuật Lập Trình:

1. **Mảng nhiều chiều:** Khai báo, khởi tạo, thao tác với mảng 2 chiều
2. **Đệ quy:** Khái niệm, cài đặt và các loại đệ quy
3. **Con trỏ:** Sử dụng con trỏ, cấp phát động, mối quan hệ với mảng
4. **Chuỗi ký tự:** Làm việc với chuỗi kiểu C và lớp string
5. **Kiểu dữ liệu người dùng:** Struct, enum, typedef
6. **Tập tin và luồng:** Đọc/ghi file văn bản và nhị phân

**Lời khuyên:**
- Thực hành thường xuyên các bài tập
- Tham khảo thêm tài liệu từ giáo trình
- Làm bài tập trên LMS
- Tham gia thảo luận với giảng viên và bạn học

---

**Tài liệu tham khảo:**
- [1] Stephen Prata. C++ Primer Plus. Addison-Wesley, 2012
- [2] Paul Deitel, Harvey Deitel. C++ How To Program. Pearson, 2017

**Biên soạn:** Dựa trên đề cương môn học Kỹ thuật Lập Trình
**Trường Đại học Mở TP.HCM - Khoa Công nghệ Thông tin**
