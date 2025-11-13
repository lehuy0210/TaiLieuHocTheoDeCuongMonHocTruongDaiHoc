# CHƯƠNG 5: ĐẠI SỐ BOOLE

## 5.1. CÁC KHÁI NIỆM

### 5.1.1. Định nghĩa đại số Boole

**Lịch sử:**

Đại số Boole được phát triển bởi George Boole (1815-1864), nhà toán học người Anh, để hình thức hóa logic.

Ngày nay, đại số Boole là nền tảng của:
- Thiết kế mạch số
- Lập trình
- Cơ sở dữ liệu
- Tối ưu hóa

---

**Định nghĩa (Đại số Boole):**

Một đại số Boole là một cấu trúc (B, +, ·, ', 0, 1) gồm:
- Một tập B
- Hai phép toán nhị phân: + (OR), · (AND)
- Một phép toán một ngôi: ' (NOT)
- Hai phần tử đặc biệt: 0, 1

Thỏa mãn các tiên đề sau:

---

**Các tiên đề (Axioms):**

**1. Tính giao hoán:**
- a + b = b + a
- a · b = b · a

**2. Tính kết hợp:**
- (a + b) + c = a + (b + c)
- (a · b) · c = a · (b · c)

**3. Phần tử đơn vị:**
- a + 0 = a
- a · 1 = a

**4. Phần tử bù:**
- a + a' = 1
- a · a' = 0

**5. Tính phân phối:**
- a + (b · c) = (a + b) · (a + c)
- a · (b + c) = (a · b) + (a · c)

---

**Ví dụ các đại số Boole:**

**1. Đại số Boole 2 phần tử:**
- B = {0, 1}
- + là OR
- · là AND
- ' là NOT

**Bảng chân lý:**
```
x | y | x+y | x·y
0 | 0 |  0  |  0
0 | 1 |  1  |  0
1 | 0 |  1  |  0
1 | 1 |  1  |  1

x | x'
0 | 1
1 | 0
```

**2. Đại số tập hợp:**
- B = P(S) (tập lũy thừa của S)
- + là ∪ (hợp)
- · là ∩ (giao)
- ' là phần bù
- 0 là ∅
- 1 là S

**3. Đại số chia hết:**
- B = {1, 2, 3, 5, 6, 10, 15, 30}
- + là LCM (bội chung nhỏ nhất)
- · là GCD (ước chung lớn nhất)
- a' = 30/a
- 0 là 1
- 1 là 30

---

**Nguyên lý đối ngẫu (Duality Principle):**

Nếu một đẳng thức đúng trong đại số Boole, thì đẳng thức đối ngẫu (thu được bằng cách đổi + ↔ ·, 0 ↔ 1) cũng đúng.

**Ví dụ:**
- a + 0 = a ⟺ a · 1 = a
- a + a' = 1 ⟺ a · a' = 0

### 5.1.2. Các tính chất

**Từ các tiên đề, ta suy ra các định lý sau:**

**1. Tính idempotent:**
- a + a = a
- a · a = a

**Chứng minh:**
```
a + a = (a + a) · 1            [Đơn vị]
      = (a + a) · (a + a')     [Bù]
      = a + (a · a')           [Phân phối]
      = a + 0                  [Bù]
      = a                      [Đơn vị]
```

---

**2. Luật thống trị (Domination):**
- a + 1 = 1
- a · 0 = 0

**Chứng minh:**
```
a + 1 = a + (a + a')          [Bù]
      = (a + a) + a'          [Kết hợp]
      = a + a'                [Idempotent]
      = 1                     [Bù]
```

---

**3. Luật hấp thụ (Absorption):**
- a + (a · b) = a
- a · (a + b) = a

**Chứng minh:**
```
a + (a · b) = a · 1 + a · b    [Đơn vị]
            = a · (1 + b)      [Phân phối]
            = a · 1            [Thống trị]
            = a                [Đơn vị]
```

---

**4. Luật phủ định kép:**
- (a')' = a

**Chứng minh:**
```
a' + (a')' = 1                [Bù]
a' · (a')' = 0                [Bù]

a + a' = 1                    [Bù]
a · a' = 0                    [Bù]

→ (a')' = a                   [Duy nhất phần tử bù]
```

---

**5. Định luật De Morgan:**
- (a + b)' = a' · b'
- (a · b)' = a' + b'

**Chứng minh (luật 1):**

Cần chứng minh: a' · b' là phần tử bù của a + b

**Bước 1:** (a + b) + (a' · b') = ?
```
(a + b) + (a' · b') = [(a + b) + a'] · [(a + b) + b']  [Phân phối]
                     = [(b + a) + a'] · [(a + b) + b']  [Giao hoán]
                     = [b + (a + a')] · [a + (b + b')]  [Kết hợp]
                     = [b + 1] · [a + 1]                [Bù]
                     = 1 · 1 = 1                        [Thống trị]
```

**Bước 2:** (a + b) · (a' · b') = ?
```
(a + b) · (a' · b') = [(a + b) · a'] · b'              [Kết hợp]
                     = [a · a' + b · a'] · b'          [Phân phối]
                     = [0 + b · a'] · b'               [Bù]
                     = (b · a') · b'                   [Đơn vị]
                     = b · b' · a'                     [Giao hoán, Kết hợp]
                     = 0 · a' = 0                      [Bù, Thống trị]
```

→ a' · b' là phần tử bù của a + b

→ (a + b)' = a' · b'

---

**6. Tính duy nhất:**
- Phần tử bù của mỗi phần tử là duy nhất
- 0 và 1 là duy nhất

---

**Tổng hợp các định luật:**

| Tên | Luật OR | Luật AND |
|-----|---------|----------|
| Đơn vị | a + 0 = a | a · 1 = a |
| Thống trị | a + 1 = 1 | a · 0 = 0 |
| Idempotent | a + a = a | a · a = a |
| Bù | a + a' = 1 | a · a' = 0 |
| Giao hoán | a + b = b + a | a · b = b · a |
| Kết hợp | (a+b)+c = a+(b+c) | (a·b)·c = a·(b·c) |
| Phân phối | a+(b·c) = (a+b)·(a+c) | a·(b+c) = a·b + a·c |
| Hấp thụ | a + a·b = a | a·(a+b) = a |
| De Morgan | (a+b)' = a'·b' | (a·b)' = a' + b' |
| Phủ định kép | (a')' = a | |

---

## 5.2. HÀM BOOLE

### 5.2.1. Định nghĩa

**Hàm Boole (Boolean Function):**

Hàm Boole n biến là ánh xạ:
```
f: Bⁿ → B
```

Trong đó B = {0, 1}

**Ký hiệu:** f(x₁, x₂, ..., xₙ)

---

**Ví dụ:**

**1. Hàm 1 biến:**
- f(x) = x
- f(x) = x'
- f(x) = 0
- f(x) = 1

Tổng cộng có 2² = 4 hàm Boole 1 biến.

**2. Hàm 2 biến:**

Có 2^(2²) = 16 hàm Boole 2 biến, bao gồm:
- f(x, y) = x + y (OR)
- f(x, y) = x · y (AND)
- f(x, y) = x ⊕ y (XOR)
- f(x, y) = x → y (Implication)
- ...

---

**Bảng chân lý (Truth Table):**

Cách biểu diễn hàm Boole bằng bảng liệt kê tất cả các giá trị đầu vào và đầu ra.

**Ví dụ:** f(x, y, z) = x·y + y·z'

```
| x | y | z | y·z' | x·y | f |
|---|---|---|------|-----|---|
| 0 | 0 | 0 |  0   |  0  | 0 |
| 0 | 0 | 1 |  0   |  0  | 0 |
| 0 | 1 | 0 |  1   |  0  | 1 |
| 0 | 1 | 1 |  0   |  0  | 0 |
| 1 | 0 | 0 |  0   |  0  | 0 |
| 1 | 0 | 1 |  0   |  0  | 0 |
| 1 | 1 | 0 |  1   |  1  | 1 |
| 1 | 1 | 1 |  0   |  1  | 1 |
```

---

**Số hàm Boole:**

Với n biến:
- Số bộ đầu vào: 2ⁿ
- Số hàm Boole: 2^(2ⁿ)

**Ví dụ:**
- n = 1: 2^(2¹) = 4 hàm
- n = 2: 2^(2²) = 16 hàm
- n = 3: 2^(2³) = 256 hàm
- n = 4: 2^(2⁴) = 65,536 hàm

### 5.2.2. Biểu diễn

**1. Literal (Hằng số):**

Biến hoặc phủ định của biến: x, x', y, y', ...

---

**2. Minterm (Tích chuẩn):**

Tích của n literal, mỗi biến xuất hiện đúng một lần.

**Ví dụ với 3 biến x, y, z:**
- m₀ = x'·y'·z' (tương ứng 000)
- m₁ = x'·y'·z  (tương ứng 001)
- m₂ = x'·y·z'  (tương ứng 010)
- m₃ = x'·y·z   (tương ứng 011)
- m₄ = x·y'·z'  (tương ứng 100)
- m₅ = x·y'·z   (tương ứng 101)
- m₆ = x·y·z'   (tương ứng 110)
- m₇ = x·y·z    (tương ứng 111)

**Tính chất:** Mỗi minterm bằng 1 tại đúng một bộ giá trị đầu vào.

---

**3. Maxterm (Tổng chuẩn):**

Tổng của n literal, mỗi biến xuất hiện đúng một lần.

**Ví dụ với 3 biến:**
- M₀ = x + y + z  (tương ứng 000)
- M₁ = x + y + z' (tương ứng 001)
- M₂ = x + y' + z (tương ứng 010)
- ...

**Tính chất:** Mỗi maxterm bằng 0 tại đúng một bộ giá trị đầu vào.

**Quan hệ:** Mᵢ = (mᵢ)'

---

**4. Dạng chuẩn tắc tổng của tích (Sum of Products - SOP):**

Tổng của các minterm:
```
f = Σ mᵢ
```

**Cách xây dựng từ bảng chân lý:**
- Lấy tất cả các hàng có f = 1
- Viết minterm tương ứng
- Cộng các minterm lại

**Ví dụ:**

Cho bảng chân lý:
```
| x | y | z | f |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |  → m₁
| 0 | 1 | 0 | 1 |  → m₂
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |  → m₄
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |  → m₆
| 1 | 1 | 1 | 0 |
```

**SOP:**
```
f = m₁ + m₂ + m₄ + m₆
  = x'y'z + x'yz' + xy'z' + xyz'
```

**Ký hiệu ngắn gọn:** f = Σm(1, 2, 4, 6)

---

**5. Dạng chuẩn tắc tích của tổng (Product of Sums - POS):**

Tích của các maxterm:
```
f = ∏ Mᵢ
```

**Cách xây dựng:**
- Lấy tất cả các hàng có f = 0
- Viết maxterm tương ứng
- Nhân các maxterm lại

**Ví dụ:** Với bảng trên:
```
f = 0 tại: 0, 3, 5, 7
f = M₀ · M₃ · M₅ · M₇
```

**Ký hiệu:** f = ∏M(0, 3, 5, 7)

---

**Chuyển đổi giữa SOP và POS:**

Nếu f = Σm(i₁, i₂, ..., iₖ)

Thì f = ∏M(j₁, j₂, ..., jₜ)

Trong đó {j₁, ..., jₜ} = {0, 1, ..., 2ⁿ-1} \ {i₁, ..., iₖ}

---

**6. Dạng không chuẩn tắc:**

Các biểu thức Boole tổng quát, không nhất thiết là SOP hay POS.

**Ví dụ:**
- f = x·y + z
- g = (x + y)·(y + z)
- h = x ⊕ y ⊕ z

### 5.2.3. Các cổng logic

**Cổng logic (Logic Gates):** Thiết bị điện tử thực hiện các phép toán Boole.

---

**1. Cổng NOT (Inverter):**

**Ký hiệu:**
```
    ┌───┐
A ──┤ ◯ ├── Y = A'
    └───┘
```

**Bảng chân lý:**
```
| A | Y |
|---|---|
| 0 | 1 |
| 1 | 0 |
```

---

**2. Cổng AND:**

**Ký hiệu:**
```
A ──┐
    │ D ├── Y = A·B
B ──┘
```

**Bảng chân lý:**
```
| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |
```

---

**3. Cổng OR:**

**Ký hiệu:**
```
A ──┐
    │ ≥1 ├── Y = A+B
B ──┘
```

**Bảng chân lý:**
```
| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |
```

---

**4. Cổng NAND (NOT AND):**

**Ký hiệu:**
```
A ──┐
    │ D◯├── Y = (A·B)'
B ──┘
```

**Bảng chân lý:**
```
| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
```

**Đặc biệt:** NAND là cổng vạn năng (universal gate) - có thể tạo mọi hàm Boole.

---

**5. Cổng NOR (NOT OR):**

**Ký hiệu:**
```
A ──┐
    │ ≥1◯├── Y = (A+B)'
B ──┘
```

**Bảng chân lý:**
```
| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |
```

**Đặc biệt:** NOR cũng là cổng vạn năng.

---

**6. Cổng XOR (Exclusive OR):**

**Ký hiệu:**
```
A ──┐
    │ =1 ├── Y = A ⊕ B
B ──┘
```

**Bảng chân lý:**
```
| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
```

**Công thức:** A ⊕ B = A'B + AB'

---

**7. Cổng XNOR (Exclusive NOR):**

**Ký hiệu:**
```
A ──┐
    │ =1◯├── Y = (A ⊕ B)'
B ──┘
```

**Bảng chân lý:**
```
| A | B | Y |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |
```

**Công thức:** A ⊙ B = AB + A'B' (equivalence)

---

**Tính vạn năng của NAND và NOR:**

**Dùng chỉ NAND:**
```
NOT A = A NAND A
A AND B = (A NAND B) NAND (A NAND B)
A OR B = (A NAND A) NAND (B NAND B)
```

**Dùng chỉ NOR:**
```
NOT A = A NOR A
A OR B = (A NOR B) NOR (A NOR B)
A AND B = (A NOR A) NOR (B NOR B)
```

---

## 5.3. ĐƠN GIẢN HÀM BOOLE

### 5.3.1. Các khái niệm

**Mục tiêu:** Tìm biểu thức tương đương đơn giản nhất.

**Lý do:**
- Giảm số cổng logic
- Giảm chi phí
- Tăng tốc độ
- Giảm tiêu thụ năng lượng

---

**Độ phức tạp:**

Đo bằng số literal trong biểu thức.

**Ví dụ:**
- f = xy + xz + yz có 6 literal
- f = xy + xz có 4 literal (đơn giản hơn)

---

**Tích và:**

Tích của các literal: xyz, xy'z, ...

**Tích và nguyên thủy (Prime Implicant):**

Tích và P là nguyên thủy nếu không thể bỏ bất kỳ literal nào mà P vẫn bao hàm f.

**Tích và nguyên thủy thiết yếu (Essential Prime Implicant):**

Là tích và nguyên thủy bắt buộc phải có trong biểu thức tối thiểu.

### 5.3.2. Phương pháp biến đổi

**Sử dụng các định luật đại số Boole để rút gọn.**

---

**Ví dụ 1:**
```
f = xy + xy'
  = x(y + y')    [Phân phối]
  = x · 1        [Bù]
  = x            [Đơn vị]
```

---

**Ví dụ 2:**
```
f = xyz + x'y'z + xyz'
  = xy(z + z') + x'y'z    [Phân phối]
  = xy · 1 + x'y'z         [Bù]
  = xy + x'y'z             [Đơn vị]
```

---

**Ví dụ 3:**
```
f = (x + y)(x + y')
  = x + yy'             [Phân phối]
  = x + 0               [Bù]
  = x                   [Đơn vị]
```

---

**Ví dụ 4:** Rút gọn f = AB + A'C + BC

**Giải:**
```
f = AB + A'C + BC
  = AB + A'C + BC(A + A')       [Bù: 1 = A + A']
  = AB + A'C + ABC + A'BC       [Phân phối]
  = AB + ABC + A'C + A'BC       [Giao hoán]
  = AB(1 + C) + A'C(1 + B)      [Phân phối]
  = AB · 1 + A'C · 1            [Thống trị]
  = AB + A'C                    [Đơn vị]
```

**Kết luận:** BC là thừa (do định lý Consensus)

---

**Định lý Consensus:**

```
xy + x'z + yz = xy + x'z
```

Số hạng yz là thừa.

**Chứng minh:**
```
xy + x'z + yz = xy + x'z + yz(x + x')
              = xy + x'z + xyz + x'yz
              = xy(1 + z) + x'z(1 + y)
              = xy + x'z
```

---

**Một số kỹ thuật:**

**1. Kết hợp:**
```
xy + xy' = x
```

**2. Hấp thụ:**
```
x + xy = x
```

**3. Thêm số hạng:**
```
xy + x'z = xy + x'z + yz
```
(Để dễ rút gọn sau)

**4. Nhân với 1:**
```
A = A(B + B')
```

### 5.3.3. Phương pháp biểu đồ Karnaugh

**Biểu đồ Karnaugh (K-map):**

Phương pháp đồ họa để rút gọn hàm Boole, dễ dàng hơn đại số.

---

**K-map 2 biến:**

```
      y
    0   1
x 0 [0] [1]
  1 [2] [3]
```

Mỗi ô tương ứng một minterm:
- Ô [0]: x'y' (00)
- Ô [1]: x'y  (01)
- Ô [2]: xy'  (10)
- Ô [3]: xy   (11)

---

**K-map 3 biến:**

```
       yz
     00  01  11  10
x 0  [0] [1] [3] [2]
  1  [4] [5] [7] [6]
```

**Lưu ý:** Mã Gray - chỉ thay đổi 1 bit giữa các ô kề nhau.

---

**K-map 4 biến:**

```
        yz
      00  01  11  10
wx 00 [0] [1] [3] [2]
   01 [4] [5] [7] [6]
   11 [12][13][15][14]
   10 [8] [9] [11][10]
```

---

**Cách sử dụng K-map:**

**Bước 1:** Điền giá trị hàm vào các ô (1 hoặc 0)

**Bước 2:** Nhóm các ô 1 kề nhau thành nhóm 2^k ô (1, 2, 4, 8, ...)

**Nguyên tắc nhóm:**
- Nhóm càng lớn càng tốt
- Mỗi ô 1 phải thuộc ít nhất một nhóm
- Nhóm có thể chồng lấn
- Nhóm có thể "wrap around" (quanh biên)

**Bước 3:** Viết tích và cho mỗi nhóm:
- Giữ lại các biến không đổi trong nhóm
- Bỏ các biến thay đổi

**Bước 4:** Tổng các tích và

---

**Ví dụ 1: K-map 2 biến**

f = Σm(0, 2, 3)

```
      y
    0   1
x 0 [1] [0]
  1 [1] [1]
```

**Nhóm:**
- Nhóm 1: ô [0] + [2] = x' (dọc)
- Nhóm 2: ô [2] + [3] = x  (ngang)

**Kết quả:** f = x' + x = 1

**Nhận xét:** Có thể nhóm khác: [0][2][3] → f = x' + y

---

**Ví dụ 2: K-map 3 biến**

f = Σm(1, 2, 3, 5, 7)

```
       yz
     00  01  11  10
x 0  [0] [1] [1] [1]
  1  [0] [1] [1] [0]
```

**Nhóm:**
- Nhóm 1: ô [1,3,5,7] (4 ô) → y (cột 01 + 11)
- Nhóm 2: ô [2,3] (2 ô) → x'z'

**Kiểm tra:**
- ô [1]: có trong nhóm 1 ✓
- ô [2]: có trong nhóm 2 ✓
- ô [3]: có trong cả 2 nhóm ✓
- ô [5]: có trong nhóm 1 ✓
- ô [7]: có trong nhóm 1 ✓

**Kết quả:** f = y + x'z'

---

**Ví dụ 3: K-map 4 biến**

f = Σm(0, 1, 2, 5, 8, 9, 10)

```
        yz
      00  01  11  10
wx 00 [1] [1] [0] [1]
   01 [0] [1] [0] [0]
   11 [0] [0] [0] [0]
   10 [1] [1] [0] [1]
```

**Nhóm:**
- Nhóm 1: ô [0,1,8,9] (4 ô) → w'z' (4 góc)
- Nhóm 2: ô [0,2,8,10] (4 ô) → x'y'
- Nhóm 3: ô [1,5] (2 ô) → w'xy'z

**Kết quả:** f = w'z' + x'y'

**Kiểm tra:**
- Ô [1] được bao phủ bởi nhóm 1
- Ô [5] cần nhóm riêng: w'xy'z
- Nếu không có ô [5], f = w'z' + x'y' đã đủ

**Sửa lại:** f = w'z' + x'y' + w'xy'z

Hoặc có thể nhóm khác tùy bài toán.

---

**K-map với don't care:**

Ký hiệu X hoặc d: Giá trị không quan trọng (có thể 0 hoặc 1)

**Cách dùng:**
- Coi X là 1 nếu giúp tạo nhóm lớn hơn
- Coi X là 0 nếu không cần

**Ví dụ:**

f = Σm(1, 3, 7, 11, 15), d = Σm(0, 2, 5)

```
       yz
     00  01  11  10
x 0  [X] [1] [1] [X]
  1  [X] [0] [1] [1]
```

Sử dụng X ở [0] và [2] để tạo nhóm 4 ô [0,1,2,3]:
- Nhóm: x'

Sử dụng X ở [5] không cần thiết.

**Kết quả:** f = x' + yz

---

**K-map cho POS:**

Nhóm các ô 0 thay vì ô 1, được tổng của các literal.

**Ví dụ:**

f = ∏M(0, 2, 4, 6)

```
       yz
     00  01  11  10
x 0  [0] [1] [1] [0]
  1  [0] [1] [1] [0]
```

**Nhóm các ô 0:**
- Nhóm [0,2,4,6] → z = 0 → z'

**Kết quả SOP:** f = z

**Hoặc POS:** f = z (giống nhau trong trường hợp này)

---

## KẾT LUẬN CHƯƠNG 5

**Nội dung đã học:**

1. **Đại số Boole:**
   - Định nghĩa và tiên đề
   - Các định luật: De Morgan, hấp thụ, phân phối, ...

2. **Hàm Boole:**
   - Biểu diễn: SOP, POS
   - Minterm, Maxterm

3. **Cổng logic:**
   - AND, OR, NOT, NAND, NOR, XOR, XNOR
   - Tính vạn năng của NAND và NOR

4. **Rút gọn hàm Boole:**
   - Phương pháp đại số
   - Phương pháp K-map

**Ứng dụng:**
- Thiết kế mạch số
- Tối ưu hóa phần cứng
- Lập trình logic

---

## BÀI TẬP ÔN TẬP CHƯƠNG 5

**Bài 1:** Chứng minh các đẳng thức sau bằng đại số Boole:
a) x + x'y = x + y
b) (x + y)(x + y') = x
c) xy + x'z + yz = xy + x'z

**Bài 2:** Tìm dạng SOP và POS của hàm:

```
| x | y | z | f |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |
```

**Bài 3:** Rút gọn các hàm sau bằng đại số:
a) f = ABC + ABC' + A'BC
b) g = (A + B)(A + C)(B + C)
c) h = AB'C + A'BC + ABC + ABC'

**Bài 4:** Rút gọn bằng K-map:
a) f(x, y, z) = Σm(0, 2, 4, 5, 6)
b) g(w, x, y, z) = Σm(0, 1, 2, 5, 8, 9, 10)
c) h(w, x, y, z) = Σm(0, 1, 3, 7, 15), d(5, 11, 13)

**Bài 5:** Vẽ mạch logic cho:
a) f = AB + BC
b) g = (A + B)(B + C)
c) h = A ⊕ B ⊕ C

**Bài 6:** Chứng minh NAND là cổng vạn năng bằng cách biểu diễn NOT, AND, OR chỉ bằng NAND.

**Bài 7:** Thiết kế mạch bán cộng (Half Adder):
- Đầu vào: A, B
- Đầu ra: S (tổng), C (nhớ)
- S = A ⊕ B
- C = AB

**Bài 8:** Thiết kế mạch toàn cộng (Full Adder):
- Đầu vào: A, B, Cᵢₙ
- Đầu ra: S, Cₒᵤₜ

**Bài 9:** Tìm tất cả các prime implicant của:
f(x, y, z) = Σm(1, 3, 4, 5, 7)

**Bài 10:** Chuyển đổi sang dạng NAND-NAND:
f = AB + CD + E
