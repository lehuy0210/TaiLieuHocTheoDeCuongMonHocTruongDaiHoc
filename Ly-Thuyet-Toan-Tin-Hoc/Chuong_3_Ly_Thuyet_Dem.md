# CHƯƠNG 3: LÝ THUYẾT ĐẾM

## 3.1. CƠ SỞ CỦA PHÉP ĐÉM

### 3.1.1. Những nguyên lý cơ bản

**Nguyên lý cơ bản của phép đếm:**

Lý thuyết đếm giải quyết câu hỏi: "Có bao nhiêu cách để thực hiện một công việc?"

---

**1. Quy tắc cộng (Sum Rule / Addition Principle):**

**Phát biểu:**
Nếu một công việc có thể thực hiện bằng cách 1 HOẶC cách 2, và:
- Cách 1 có n₁ cách thực hiện
- Cách 2 có n₂ cách thực hiện
- Hai cách không trùng lặp

Thì số cách thực hiện công việc là: **n₁ + n₂**

**Tổng quát:**
Nếu có k cách loại trừ lẫn nhau với n₁, n₂, ..., nₖ cách thực hiện tương ứng, thì tổng số cách là:
```
n₁ + n₂ + ... + nₖ
```

**Dạng tập hợp:**
Nếu A và B là hai tập rời nhau (A ∩ B = ∅) thì:
```
|A ∪ B| = |A| + |B|
```

**Ví dụ 1:**
Trong lớp có 25 nam và 30 nữ. Chọn một học sinh làm lớp trưởng.

**Giải:**
- Chọn nam: 25 cách
- Chọn nữ: 30 cách
- Tổng: 25 + 30 = **55 cách**

**Ví dụ 2:**
Một chuỗi ký tự bắt đầu bằng chữ cái hoặc dấu gạch dưới. Có bao nhiêu cách chọn ký tự đầu tiên?

**Giải:**
- Chữ cái: 26 + 26 = 52 cách (hoa + thường)
- Dấu gạch dưới: 1 cách
- Tổng: 52 + 1 = **53 cách**

---

**2. Quy tắc nhân (Product Rule / Multiplication Principle):**

**Phát biểu:**
Nếu một công việc gồm hai bước:
- Bước 1 có n₁ cách thực hiện
- Bước 2 có n₂ cách thực hiện (với mỗi cách ở bước 1)

Thì số cách thực hiện công việc là: **n₁ × n₂**

**Tổng quát:**
Nếu công việc gồm k bước với n₁, n₂, ..., nₖ cách tương ứng, thì tổng số cách là:
```
n₁ × n₂ × ... × nₖ
```

**Dạng tập hợp:**
```
|A₁ × A₂ × ... × Aₖ| = |A₁| × |A₂| × ... × |Aₖ|
```

**Ví dụ 1:**
Có bao nhiêu cách đi từ A đến C qua B, biết từ A đến B có 3 con đường, từ B đến C có 4 con đường?

**Giải:**
- Chọn đường A→B: 3 cách
- Chọn đường B→C: 4 cách (với mỗi cách ở bước 1)
- Tổng: 3 × 4 = **12 cách**

**Ví dụ 2:**
Có bao nhiêu mật khẩu dài 6 ký tự, mỗi ký tự là chữ số từ 0-9?

**Giải:**
- Vị trí 1: 10 cách
- Vị trí 2: 10 cách
- ...
- Vị trí 6: 10 cách
- Tổng: 10⁶ = **1,000,000 cách**

**Ví dụ 3:**
Có bao nhiêu số tự nhiên có 3 chữ số?

**Giải:**
- Chữ số hàng trăm: 1-9 → 9 cách
- Chữ số hàng chục: 0-9 → 10 cách
- Chữ số hàng đơn vị: 0-9 → 10 cách
- Tổng: 9 × 10 × 10 = **900 số**

---

**3. Kết hợp quy tắc cộng và nhân:**

**Ví dụ 1:**
Mật khẩu phải:
- Bắt đầu bằng chữ cái (26 chữ)
- Theo sau là 3 chữ số
- Kết thúc bằng chữ cái hoặc chữ số

Có bao nhiêu mật khẩu?

**Giải:**

**Trường hợp 1:** Kết thúc bằng chữ cái
- Vị trí 1: 26 cách
- Vị trí 2-4: 10³ cách
- Vị trí 5: 26 cách
- Tổng TH1: 26 × 10³ × 26 = 676,000

**Trường hợp 2:** Kết thúc bằng chữ số
- Vị trí 1: 26 cách
- Vị trí 2-4: 10³ cách
- Vị trí 5: 10 cách
- Tổng TH2: 26 × 10³ × 10 = 260,000

**Tổng:** 676,000 + 260,000 = **936,000 mật khẩu**

---

**4. Quy tắc bù trừ (Subtraction Rule):**

**Phát biểu:**
Nếu công việc A có thể thực hiện bằng n cách, trong đó có m cách không thỏa mãn điều kiện, thì số cách thỏa mãn là:
```
n - m
```

**Ví dụ:**
Có bao nhiêu chuỗi bit độ dài 8 có ít nhất một bit 1?

**Giải:**

**Cách 1 (Trực tiếp - khó):**
Đếm chuỗi có 1 bit 1, 2 bit 1, ..., 8 bit 1

**Cách 2 (Bù trừ - dễ):**
- Tổng chuỗi 8 bit: 2⁸ = 256
- Chuỗi toàn bit 0: 1
- Kết quả: 256 - 1 = **255 chuỗi**

---

**5. Quy tắc chia (Division Rule):**

**Phát biểu:**
Nếu có n cách thực hiện công việc, và mỗi kết quả được đếm d lần, thì số kết quả phân biệt là:
```
n / d
```

**Ví dụ:**
Có bao nhiêu cách xếp 10 người thành 2 hàng, mỗi hàng 5 người, nếu thứ tự các hàng không quan trọng?

**Giải:**
- Chọn 5 người hàng 1: C(10,5)
- 5 người còn lại hàng 2: 1 cách
- Nhưng mỗi cách xếp được đếm 2 lần (đổi 2 hàng cho nhau)
- Kết quả: C(10,5) / 2 = 252 / 2 = **126 cách**

### 3.1.2. Nguyên lý bù trừ

**Nguyên lý bao hàm - loại trừ (Inclusion-Exclusion Principle):**

**Hai tập hợp:**
```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

**Ba tập hợp:**
```
|A ∪ B ∪ C| = |A| + |B| + |C|
              - |A ∩ B| - |A ∩ C| - |B ∩ C|
              + |A ∩ B ∩ C|
```

**Tổng quát (n tập hợp):**
```
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
```

**Giải thích:**
- Cộng các tập đơn
- Trừ các giao của 2 tập
- Cộng các giao của 3 tập
- Trừ các giao của 4 tập
- ...

---

**Ví dụ 1:**
Trong 100 sinh viên:
- 40 người học Java
- 30 người học Python
- 15 người học cả Java và Python

Có bao nhiêu người học ít nhất một ngôn ngữ?

**Giải:**
- J: tập sinh viên học Java, |J| = 40
- P: tập sinh viên học Python, |P| = 30
- |J ∩ P| = 15

Áp dụng công thức:
```
|J ∪ P| = |J| + |P| - |J ∩ P|
        = 40 + 30 - 15
        = 55 người
```

---

**Ví dụ 2:**
Có bao nhiêu số từ 1 đến 100 chia hết cho 2 hoặc 3?

**Giải:**
- A: tập số chia hết cho 2 → |A| = ⌊100/2⌋ = 50
- B: tập số chia hết cho 3 → |B| = ⌊100/3⌋ = 33
- A ∩ B: số chia hết cho cả 2 và 3 = chia hết cho 6 → |A ∩ B| = ⌊100/6⌋ = 16

```
|A ∪ B| = 50 + 33 - 16 = 67 số
```

---

**Ví dụ 3:**
Có bao nhiêu số từ 1 đến 1000 chia hết cho 2, 3 hoặc 5?

**Giải:**
- A₂: chia hết cho 2 → |A₂| = 500
- A₃: chia hết cho 3 → |A₃| = 333
- A₅: chia hết cho 5 → |A₅| = 200
- |A₂ ∩ A₃| = ⌊1000/6⌋ = 166
- |A₂ ∩ A₅| = ⌊1000/10⌋ = 100
- |A₃ ∩ A₅| = ⌊1000/15⌋ = 66
- |A₂ ∩ A₃ ∩ A₅| = ⌊1000/30⌋ = 33

```
|A₂ ∪ A₃ ∪ A₅| = 500 + 333 + 200 - 166 - 100 - 66 + 33 = 734 số
```

---

**Ứng dụng: Hàm Euler φ(n)**

Hàm φ(n) đếm số các số nguyên dương ≤ n và nguyên tố cùng nhau với n.

**Công thức:**
Nếu n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ thì:
```
φ(n) = n × (1 - 1/p₁) × (1 - 1/p₂) × ... × (1 - 1/pₖ)
```

**Ví dụ:** φ(12) = ?
- 12 = 2² × 3
- φ(12) = 12 × (1 - 1/2) × (1 - 1/3) = 12 × 1/2 × 2/3 = 4

Thật vậy: {1, 5, 7, 11} nguyên tố cùng nhau với 12.

---

## 3.2. NGUYÊN LÝ PIGEONHOLE

### 3.2.1. Mở đầu

**Nguyên lý chuồng chim bồ câu (Pigeonhole Principle):**

Tên gọi khác: Nguyên lý Dirichlet, Nguyên lý hộp

**Ý nghĩa:** Một nguyên lý đơn giản nhưng có ứng dụng rất mạnh trong chứng minh.

### 3.2.2. Nguyên lý Dirichlet

**Dạng 1 (Cơ bản):**

Nếu có n + 1 con chim được xếp vào n chuồng, thì ít nhất một chuồng chứa từ 2 con chim trở lên.

**Tổng quát:**
Nếu có N đối tượng được xếp vào k hộp với N > k, thì ít nhất một hộp chứa ít nhất ⌈N/k⌉ đối tượng.

**Ký hiệu:** ⌈x⌉ là hàm trần (ceiling), số nguyên nhỏ nhất ≥ x

---

**Ví dụ 1:**
Trong 13 người bất kỳ, chắc chắn có ít nhất 2 người sinh cùng tháng.

**Chứng minh:**
- Số người: 13 (chim)
- Số tháng: 12 (chuồng)
- 13 > 12 → Theo nguyên lý Pigeonhole, ít nhất 2 người sinh cùng tháng.

---

**Ví dụ 2:**
Chứng minh rằng trong 5 điểm bất kỳ trong một tam giác đều cạnh 2, luôn tồn tại 2 điểm cách nhau không quá 1.

**Chứng minh:**
- Chia tam giác thành 4 tam giác đều nhỏ cạnh 1
- 5 điểm xếp vào 4 tam giác → Có tam giác chứa ≥ 2 điểm
- Hai điểm cùng tam giác cạnh 1 có khoảng cách ≤ 1

---

**Ví dụ 3:**
Chứng minh trong 101 số nguyên bất kỳ, tồn tại hai số có hiệu chia hết cho 100.

**Chứng minh:**
- Xét phần dư khi chia cho 100: 0, 1, 2, ..., 99 (100 giá trị)
- 101 số → 101 phần dư
- Theo Pigeonhole: Có 2 số có cùng phần dư
- → Hiệu của chúng chia hết cho 100

---

**Dạng 2 (Tổng quát):**

Nếu có N đối tượng được phân vào k hộp, thì:
- Có ít nhất 1 hộp chứa ít nhất ⌈N/k⌉ đối tượng
- Có ít nhất 1 hộp chứa nhiều nhất ⌊N/k⌋ đối tượng

---

**Dạng 3 (Nguyên lý Pigeonhole mạnh):**

Cho q₁, q₂, ..., qₙ là các số dương. Nếu q₁ + q₂ + ... + qₙ - n + 1 đối tượng được xếp vào n hộp, thì:
- Hộp 1 chứa ít nhất q₁ đối tượng, HOẶC
- Hộp 2 chứa ít nhất q₂ đối tượng, HOẶC
- ...
- Hộp n chứa ít nhất qₙ đối tượng

### 3.2.3. Ứng dụng

**Ví dụ 1: Bài toán dãy con tăng**

Mọi dãy n² + 1 số thực phân biệt đều chứa dãy con tăng có n + 1 phần tử HOẶC dãy con giảm có n + 1 phần tử.

**Chứng minh (ý tưởng):**
Gán mỗi phần tử aᵢ cặp (lᵢ, dᵢ):
- lᵢ: độ dài dãy tăng dài nhất kết thúc tại aᵢ
- dᵢ: độ dài dãy giảm dài nhất kết thúc tại aᵢ

Nếu mọi lᵢ ≤ n và mọi dᵢ ≤ n:
- Có n × n = n² cặp (l, d) khác nhau
- Nhưng có n² + 1 phần tử
- Theo Pigeonhole: Có 2 phần tử có cùng cặp (l, d) → Mâu thuẫn!

---

**Ví dụ 2: Dãy chia hết**

Cho n số nguyên a₁, a₂, ..., aₙ. Chứng minh tồn tại dãy con liên tiếp có tổng chia hết cho n.

**Chứng minh:**
Xét các tổng:
- S₁ = a₁
- S₂ = a₁ + a₂
- ...
- Sₙ = a₁ + a₂ + ... + aₙ

**Trường hợp 1:** Có Sₖ chia hết cho n → Xong

**Trường hợp 2:** Không có Sₖ nào chia hết cho n
- n số S₁, ..., Sₙ có phần dư: 1, 2, ..., n-1 (n-1 giá trị)
- Theo Pigeonhole: Có Sᵢ và Sⱼ (i < j) cùng phần dư
- → Sⱼ - Sᵢ = aᵢ₊₁ + ... + aⱼ chia hết cho n

---

**Ví dụ 3: Bài toán lịch**

Nếu 11 người được chọn từ 50 người, thì ít nhất 2 người trong số 11 người này sinh cùng tháng.

**Lời giải:**
- 11 người → 11 tháng sinh
- Nhưng chỉ có 12 tháng
- Nếu mỗi tháng ≤ 1 người: tối đa 12 người
- → Có tháng có ≥ 2 người? Sai!

**Sửa đề:** Trong 13 người, chắc chắn có 2 người sinh cùng tháng.

---

**Ví dụ 4: Bài toán đồ thị**

Trong một nhóm 6 người, luôn có 3 người quen lẫn nhau HOẶC 3 người không quen ai.

**Chứng minh:**
Xét người A và 5 người còn lại.
- Theo Pigeonhole: A quen ≥ 3 người HOẶC không quen ≥ 3 người

**Trường hợp 1:** A quen B, C, D (≥ 3 người)
- Nếu có 2 trong {B, C, D} quen nhau → 3 người quen lẫn nhau
- Nếu không → B, C, D không quen ai → 3 người không quen ai

**Trường hợp 2:** Tương tự

---

## 3.3. HOÁN VỊ, TỔ HỢP VÀ CHỈNH HỢP

### 3.3.1. Chỉnh hợp

**Định nghĩa:**

Chỉnh hợp chập k của n phần tử là cách chọn và sắp xếp k phần tử từ n phần tử.

**Ký hiệu:** A(n, k), P(n, k), A_n^k, P_n^k

**Công thức:**
```
A(n, k) = n × (n-1) × (n-2) × ... × (n-k+1)
        = n! / (n-k)!
```

**Điều kiện:** 0 ≤ k ≤ n

**Đặc biệt:**
- A(n, 0) = 1
- A(n, n) = n!
- A(n, 1) = n

---

**Ý nghĩa:**
- Số cách chọn k phần tử từ n phần tử và sắp xếp chúng theo thứ tự
- **Có thứ tự**, **không lặp lại**

---

**Ví dụ 1:**
Có bao nhiêu cách chọn 3 người từ 10 người để làm chủ tịch, phó chủ tịch, thư ký?

**Giải:**
- Chức vụ khác nhau → Có thứ tự
- A(10, 3) = 10 × 9 × 8 = **720 cách**

---

**Ví dụ 2:**
Có bao nhiêu số gồm 4 chữ số khác nhau được tạo từ {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}?

**Giải:**
- Chữ số đầu: 1-9 → 9 cách
- 3 chữ số còn lại: A(9, 3) = 9 × 8 × 7 = 504 cách
- Tổng: 9 × 504 = **4536 số**

---

**Ví dụ 3:**
Có bao nhiêu cách sắp xếp 5 quyển sách khác nhau trên kệ?

**Giải:**
- A(5, 5) = 5! = **120 cách**

### 3.3.2. Tổ hợp

**Định nghĩa:**

Tổ hợp chập k của n phần tử là cách chọn k phần tử từ n phần tử (không quan tâm thứ tự).

**Ký hiệu:** C(n, k), C_n^k, (n k), "n choose k"

**Công thức:**
```
C(n, k) = n! / [k! × (n-k)!]
        = A(n, k) / k!
```

**Điều kiện:** 0 ≤ k ≤ n

---

**Ý nghĩa:**
- Số cách chọn k phần tử từ n phần tử
- **Không thứ tự**, **không lặp lại**

---

**Tính chất:**

1. **C(n, k) = C(n, n-k)**
   - Chọn k phần tử = Loại bỏ n-k phần tử

2. **C(n, 0) = C(n, n) = 1**

3. **C(n, 1) = n**

4. **Công thức Pascal:**
   ```
   C(n, k) = C(n-1, k-1) + C(n-1, k)
   ```

5. **Đẳng thức Vandermonde:**
   ```
   C(m+n, r) = Σ C(m, k) × C(n, r-k)
   ```

6. **Tổng:**
   ```
   Σ C(n, k) = 2^n  (k từ 0 đến n)
   ```

---

**Ví dụ 1:**
Từ 10 người, chọn 3 người vào ban đại diện. Có bao nhiêu cách?

**Giải:**
- Không phân biệt chức vụ → Không thứ tự
- C(10, 3) = 10!/(3!×7!) = (10×9×8)/(3×2×1) = **120 cách**

---

**Ví dụ 2:**
Trong lớp có 25 nam và 20 nữ. Chọn 5 người sao cho có đúng 2 nữ.

**Giải:**
- Chọn 2 nữ từ 20: C(20, 2)
- Chọn 3 nam từ 25: C(25, 3)
- Tổng: C(20, 2) × C(25, 3) = 190 × 2300 = **437,000 cách**

---

**Ví dụ 3:**
Có bao nhiêu cách chia 10 người thành 2 nhóm 5 người?

**Giải:**
- Chọn 5 người nhóm 1: C(10, 5) = 252
- 5 người còn lại tự động vào nhóm 2
- Nhưng hai nhóm không phân biệt → Chia cho 2
- Kết quả: C(10, 5) / 2 = **126 cách**

---

**Tam giác Pascal:**

```
n=0:                    1
n=1:                  1   1
n=2:                1   2   1
n=3:              1   3   3   1
n=4:            1   4   6   4   1
n=5:          1   5  10  10   5   1
n=6:        1   6  15  20  15   6   1
```

Mỗi số = tổng hai số trên nó (Công thức Pascal)

### 3.3.3. Hoán vị

**Định nghĩa:**

Hoán vị của n phần tử là cách sắp xếp n phần tử theo một thứ tự.

**Ký hiệu:** P(n), n!

**Công thức:**
```
P(n) = n!
```

---

**Ý nghĩa:**
- Số cách sắp xếp n phần tử
- **Có thứ tự**, **không lặp**, **lấy hết**

---

**Ví dụ 1:**
Có bao nhiêu cách sắp xếp 6 người vào 6 ghế?

**Giải:**
- 6! = **720 cách**

---

**Ví dụ 2:**
Có bao nhiêu từ có thể tạo từ các chữ cái của "MATH"?

**Giải:**
- 4 chữ cái khác nhau
- 4! = **24 từ**

---

**Hoán vị có lặp:**

Nếu có n phần tử, trong đó:
- n₁ phần tử loại 1 (giống nhau)
- n₂ phần tử loại 2 (giống nhau)
- ...
- nₖ phần tử loại k (giống nhau)

Thì số hoán vị là:
```
P(n; n₁, n₂, ..., nₖ) = n! / (n₁! × n₂! × ... × nₖ!)
```

---

**Ví dụ 3:**
Có bao nhiêu từ có thể tạo từ "MISSISSIPPI"?

**Giải:**
- Tổng 11 chữ cái
- M: 1, I: 4, S: 4, P: 2
- Số từ = 11! / (1! × 4! × 4! × 2!) = **34,650 từ**

---

**Hoán vị vòng tròn:**

Số cách sắp xếp n phần tử khác nhau thành vòng tròn:
```
(n - 1)!
```

**Giải thích:** Cố định 1 phần tử, sắp xếp n-1 phần tử còn lại.

**Ví dụ:**
Sắp xếp 6 người ngồi quanh bàn tròn: (6-1)! = 5! = **120 cách**

### 3.3.4. Hệ thức Newton

**Định lý nhị thức Newton:**

```
(x + y)^n = Σ C(n, k) × x^(n-k) × y^k  (k từ 0 đến n)
          = C(n,0)x^n + C(n,1)x^(n-1)y + C(n,2)x^(n-2)y^2 + ... + C(n,n)y^n
```

---

**Trường hợp đặc biệt:**

**1. x = y = 1:**
```
2^n = Σ C(n, k)  (k từ 0 đến n)
```

**2. x = 1, y = -1:**
```
0 = Σ (-1)^k × C(n, k)  (n ≥ 1)
```

**3. x = 2, y = 1:**
```
3^n = Σ C(n, k) × 2^k
```

---

**Ví dụ 1:**
Khai triển (x + y)⁴

**Giải:**
```
(x + y)⁴ = C(4,0)x⁴ + C(4,1)x³y + C(4,2)x²y² + C(4,3)xy³ + C(4,4)y⁴
         = x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴
```

---

**Ví dụ 2:**
Tìm hệ số của x⁷ trong (2x + 3)¹⁰

**Giải:**
Số hạng tổng quát: C(10, k) × (2x)^(10-k) × 3^k

Để có x⁷: 10 - k = 7 → k = 3

Hệ số = C(10, 3) × 2⁷ × 3³ = 120 × 128 × 27 = **414,720**

---

**Ví dụ 3:**
Tính tổng: S = C(n, 0) + C(n, 1) + C(n, 2) + ... + C(n, n)

**Giải:**
Áp dụng (x + y)^n với x = y = 1:
```
2^n = Σ C(n, k)
```

Vậy **S = 2^n**

---

**Đẳng thức tổ hợp quan trọng:**

1. **C(n, k) = C(n, n-k)**

2. **C(n, k) = C(n-1, k-1) + C(n-1, k)** (Pascal)

3. **k × C(n, k) = n × C(n-1, k-1)**

4. **Σ C(n, k) = 2^n**

5. **Σ k × C(n, k) = n × 2^(n-1)**

6. **Σ C(n, k)² = C(2n, n)** (Đẳng thức Vandermonde)

---

## 3.4. CHỈNH HỢP VÀ TỔ HỢP SUY RỘNG

### 3.4.1. Chỉnh hợp lặp

**Định nghĩa:**

Chỉnh hợp lặp chập k của n phần tử là cách chọn k phần tử từ n phần tử có thứ tự, mỗi phần tử có thể được chọn nhiều lần.

**Ký hiệu:** Ā(n, k), n^k

**Công thức:**
```
Ā(n, k) = n^k
```

---

**Ý nghĩa:**
- **Có thứ tự**, **có lặp lại**
- Mỗi vị trí có n lựa chọn

---

**Ví dụ 1:**
Có bao nhiêu mật khẩu dài 6 ký tự từ 26 chữ cái (không phân biệt hoa thường)?

**Giải:**
- Mỗi vị trí: 26 chọn
- 6 vị trí, có lặp
- Ā(26, 6) = 26⁶ = **308,915,776 mật khẩu**

---

**Ví dụ 2:**
Tung một con xúc xắc 4 lần. Có bao nhiêu kết quả khả dĩ?

**Giải:**
- Mỗi lần: 6 kết quả
- 4 lần, có lặp
- 6⁴ = **1,296 kết quả**

---

**Ví dụ 3:**
Có bao nhiêu hàm f: A → B với |A| = m, |B| = n?

**Giải:**
- Mỗi phần tử của A có n lựa chọn ảnh trong B
- m phần tử, có lặp (nhiều phần tử có thể cùng ảnh)
- **n^m hàm**

### 3.4.2. Tổ hợp lặp

**Định nghĩa:**

Tổ hợp lặp chập k của n phần tử là cách chọn k phần tử từ n phần tử không quan tâm thứ tự, mỗi phần tử có thể được chọn nhiều lần.

**Ký hiệu:** C̄(n, k), ((n k)), H(n, k)

**Công thức:**
```
C̄(n, k) = C(n + k - 1, k)
        = C(n + k - 1, n - 1)
        = (n + k - 1)! / [k! × (n - 1)!]
```

---

**Ý nghĩa:**
- **Không thứ tự**, **có lặp lại**

---

**Bài toán tương đương:**

1. **Bài toán phân phối:**
   Số cách phân k vật giống nhau vào n hộp khác nhau.

2. **Bài toán phương trình:**
   Số nghiệm nguyên không âm của:
   ```
   x₁ + x₂ + ... + xₙ = k
   ```

---

**Chứng minh công thức:**

Biểu diễn: n-1 vách ngăn (|) và k sao (★)

Ví dụ: n=4, k=7: ★★|★★★||★★
- Hộp 1: 2 vật
- Hộp 2: 3 vật
- Hộp 3: 0 vật
- Hộp 4: 2 vật

Tổng n-1+k vị trí, chọn k vị trí cho sao:
```
C(n + k - 1, k)
```

---

**Ví dụ 1:**
Có 10 quả táo giống nhau, chia cho 4 người. Có bao nhiêu cách?

**Giải:**
- k = 10 (táo), n = 4 (người)
- C̄(4, 10) = C(4+10-1, 10) = C(13, 10) = C(13, 3) = **286 cách**

---

**Ví dụ 2:**
Tìm số nghiệm nguyên không âm của: x₁ + x₂ + x₃ = 10

**Giải:**
- n = 3, k = 10
- C(3+10-1, 10) = C(12, 10) = C(12, 2) = **66 nghiệm**

---

**Ví dụ 3:**
Có bao nhiêu cách chọn 5 viên kẹo từ 3 loại (mỗi loại có nhiều viên)?

**Giải:**
- n = 3 (loại), k = 5 (viên)
- C̄(3, 5) = C(3+5-1, 5) = C(7, 5) = C(7, 2) = **21 cách**

---

**Tổ hợp lặp với ràng buộc:**

**Bài toán:** Tìm số nghiệm nguyên dương của x₁ + x₂ + ... + xₙ = k

**Đổi biến:** yᵢ = xᵢ - 1 ≥ 0

Phương trình trở thành: y₁ + y₂ + ... + yₙ = k - n

**Đáp án:** C(k - 1, n - 1)

---

**Ví dụ 4:**
Tìm số nghiệm nguyên dương của: x₁ + x₂ + x₃ + x₄ = 20

**Giải:**
- Đổi: yᵢ = xᵢ - 1 ≥ 0
- y₁ + y₂ + y₃ + y₄ = 16
- C(16+4-1, 16) = C(19, 16) = C(19, 3) = **969 nghiệm**

### 3.4.3. Hoán vị lặp

**Hoán vị có phần tử lặp lại:** (Đã nói ở 3.3.3)

Nếu có n phần tử với n₁, n₂, ..., nₖ phần tử giống nhau:
```
P(n; n₁, n₂, ..., nₖ) = n! / (n₁! × n₂! × ... × nₖ!)
```

---

**Hoán vị với vị trí lặp lại:**

Số cách đặt n phần tử khác nhau vào k vị trí (có thể trống):
```
Σ C(n, i) × i! × S(k, i)  (i từ 0 đến min(n,k))
```

Trong đó S(k, i) là số Stirling loại 2.

---

**Ví dụ:**
Số cách xếp 3 quyển sách khác nhau vào 5 ngăn (sách cùng ngăn không quan trọng thứ tự):

**Giải:**
- Mỗi sách chọn 1 ngăn trong 5 ngăn
- 5³ = **125 cách**

---

## TỔNG KẾT CHƯƠNG 3

**Bảng tổng kết các công thức:**

| Loại | Thứ tự | Lặp | Công thức | Ký hiệu |
|------|--------|-----|-----------|---------|
| Chỉnh hợp | Có | Không | n!/(n-k)! | A(n,k) |
| Tổ hợp | Không | Không | n!/[k!(n-k)!] | C(n,k) |
| Hoán vị | Có | Không | n! | P(n) |
| Chỉnh hợp lặp | Có | Có | n^k | Ā(n,k) |
| Tổ hợp lặp | Không | Có | C(n+k-1,k) | C̄(n,k) |

---

**Cách nhận biết bài toán:**

1. **Có thứ tự?**
   - Có → Chỉnh hợp hoặc Hoán vị
   - Không → Tổ hợp

2. **Lấy hết?**
   - Có → Hoán vị
   - Không → Chỉnh hợp hoặc Tổ hợp

3. **Lặp lại?**
   - Có → Thêm "lặp"
   - Không → Bình thường

---

## BÀI TẬP ÔN TẬP CHƯƠNG 3

**Bài 1:** Có bao nhiêu số tự nhiên gồm 5 chữ số khác nhau?

**Bài 2:** Từ 10 người, chọn 1 ban đại diện gồm 1 trưởng ban, 1 phó ban, 2 ủy viên. Có bao nhiêu cách?

**Bài 3:** Có bao nhiêu cách chia 20 người thành 4 nhóm, mỗi nhóm 5 người?

**Bài 4:** Chứng minh trong 367 người, có ít nhất 2 người sinh cùng ngày.

**Bài 5:** Chứng minh trong dãy n² + 1 số, luôn có dãy con tăng dài n+1 hoặc dãy con giảm dài n+1.

**Bài 6:** Tính:
a) A(10, 3)
b) C(10, 3)
c) Ā(10, 3)
d) C̄(10, 3)

**Bài 7:** Tìm hệ số của x⁵ trong khai triển (x + 2)⁸

**Bài 8:** Tìm số nghiệm nguyên không âm của: x₁ + x₂ + x₃ + x₄ = 15

**Bài 9:** Có bao nhiêu từ tạo từ chữ cái "HELLO"?

**Bài 10:** Trong 100 số nguyên bất kỳ, chứng minh tồn tại 2 số có tổng hoặc hiệu chia hết cho 157.

**Bài 11:** Chứng minh: Σ C(n, k)² = C(2n, n)

**Bài 12:** Có bao nhiêu cách xếp 5 người A, B, C, D, E sao cho A và B không đứng cạnh nhau?
