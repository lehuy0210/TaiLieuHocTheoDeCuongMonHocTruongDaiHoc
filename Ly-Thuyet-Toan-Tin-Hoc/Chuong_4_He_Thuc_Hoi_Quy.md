# CHƯƠNG 4: HỆ THỨC HỒI QUY

## 4.1. CÁC KHÁI NIỆM

### 4.1.1. Định nghĩa hệ thức truy hồi

**Hệ thức truy hồi (Recurrence Relation):**

Là phương trình biểu diễn số hạng thứ n của dãy số theo một hoặc nhiều số hạng trước đó.

**Dạng tổng quát:**
```
aₙ = f(aₙ₋₁, aₙ₋₂, ..., aₙ₋ₖ)
```

Trong đó:
- aₙ: số hạng thứ n
- k: bậc của hệ thức
- f: hàm xác định quan hệ

---

**Điều kiện đầu (Initial Conditions):**

Các giá trị ban đầu cần thiết để xác định duy nhất dãy số.

Hệ thức bậc k cần k điều kiện đầu.

---

**Ví dụ 1: Dãy Fibonacci**

**Định nghĩa:**
```
F₀ = 0
F₁ = 1
Fₙ = Fₙ₋₁ + Fₙ₋₂  (n ≥ 2)
```

**Dãy:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

**Đặc điểm:**
- Bậc 2 (phụ thuộc 2 số hạng trước)
- Tuyến tính thuần nhất
- 2 điều kiện đầu: F₀ = 0, F₁ = 1

---

**Ví dụ 2: Tháp Hà Nội**

**Bài toán:** n đĩa, 3 cọc. Số bước tối thiểu để chuyển n đĩa?

**Hệ thức:**
```
H₁ = 1
Hₙ = 2Hₙ₋₁ + 1  (n ≥ 2)
```

**Dãy:** 1, 3, 7, 15, 31, 63, ...

**Đặc điểm:**
- Bậc 1
- Tuyến tính không thuần nhất (có số hạng tự do +1)

---

**Ví dụ 3: Lãi kép**

**Bài toán:** Gửi tiết kiệm P đồng, lãi suất r% mỗi tháng. Số tiền sau n tháng?

**Hệ thức:**
```
A₀ = P
Aₙ = Aₙ₋₁ × (1 + r)  (n ≥ 1)
```

**Nghiệm:** Aₙ = P × (1 + r)ⁿ

---

**Ví dụ 4: Số cách**

**Bài toán:** Số cách leo n bậc thang, mỗi bước leo 1 hoặc 2 bậc.

**Phân tích:**
- Bước cuối: leo 1 bậc từ vị trí n-1
- Bước cuối: leo 2 bậc từ vị trí n-2

**Hệ thức:**
```
a₁ = 1  (1 cách)
a₂ = 2  (1+1 hoặc 2)
aₙ = aₙ₋₁ + aₙ₋₂  (n ≥ 3)
```

Nhận xét: Giống Fibonacci nhưng điều kiện đầu khác!

---

**Phân loại hệ thức:**

**1. Theo bậc:**
- Bậc 1: aₙ = f(aₙ₋₁)
- Bậc 2: aₙ = f(aₙ₋₁, aₙ₋₂)
- Bậc k: aₙ = f(aₙ₋₁, ..., aₙ₋ₖ)

**2. Theo tính tuyến tính:**
- **Tuyến tính:** aₙ là tổ hợp tuyến tính của các số hạng trước
  - Ví dụ: aₙ = 2aₙ₋₁ + 3aₙ₋₂
- **Phi tuyến:** Chứa tích, lũy thừa, ...
  - Ví dụ: aₙ = aₙ₋₁ × aₙ₋₂

**3. Theo tính thuần nhất:**
- **Thuần nhất:** Không có số hạng tự do
  - Ví dụ: aₙ = 2aₙ₋₁ + aₙ₋₂
- **Không thuần nhất:** Có số hạng không phụ thuộc vào a
  - Ví dụ: aₙ = 2aₙ₋₁ + 3

**4. Theo hệ số:**
- **Hệ số hằng:** Hệ số không phụ thuộc n
  - Ví dụ: aₙ = 2aₙ₋₁ + 3aₙ₋₂
- **Hệ số biến:** Hệ số phụ thuộc n
  - Ví dụ: aₙ = naₙ₋₁

### 4.1.2. Nghiệm của hệ thức truy hồi

**Nghiệm tường minh (Closed form):**

Công thức biểu diễn aₙ theo n, không dựa vào các số hạng trước.

**Ví dụ:**
- Fibonacci: Fₙ = [φⁿ - ψⁿ] / √5
  với φ = (1+√5)/2, ψ = (1-√5)/2

---

**Cách tìm nghiệm:**

1. **Đoán và chứng minh quy nạp**
2. **Phương pháp lặp (Iteration)**
3. **Hàm sinh (Generating functions)**
4. **Phương trình đặc trưng (Characteristic equation)**

---

**Phương pháp lặp:**

**Ví dụ:** Giải aₙ = 2aₙ₋₁ + 1, a₀ = 1

```
a₁ = 2a₀ + 1 = 2×1 + 1 = 3
a₂ = 2a₁ + 1 = 2×3 + 1 = 7
a₃ = 2a₂ + 1 = 2×7 + 1 = 15
...

aₙ = 2aₙ₋₁ + 1
   = 2(2aₙ₋₂ + 1) + 1 = 2²aₙ₋₂ + 2 + 1
   = 2²(2aₙ₋₃ + 1) + 2 + 1 = 2³aₙ₋₃ + 2² + 2 + 1
   ...
   = 2ⁿa₀ + (2ⁿ⁻¹ + 2ⁿ⁻² + ... + 2 + 1)
   = 2ⁿ×1 + (2ⁿ - 1)
   = 2ⁿ⁺¹ - 1
```

**Nghiệm:** aₙ = 2ⁿ⁺¹ - 1

---

## 4.2. GIẢI TOÁN BẰNG MÔ HÌNH HỆ THỨC TRUY HỒI

**Các bước:**

1. **Xác định biến:** aₙ là gì?
2. **Tìm điều kiện đầu:** a₀, a₁, ...
3. **Thiết lập hệ thức:** Tìm mối quan hệ giữa aₙ và các số hạng trước
4. **Giải hệ thức:** Tìm nghiệm tường minh
5. **Trả lời:** Kết luận

---

**Ví dụ 1: Bài toán đếm chuỗi bit**

**Đề bài:** Đếm số chuỗi bit độ dài n không chứa hai bit 1 liên tiếp.

**Giải:**

**Bước 1:** Đặt aₙ = số chuỗi thỏa mãn độ dài n

**Bước 2:** Điều kiện đầu:
- a₁ = 2: {0, 1}
- a₂ = 3: {00, 01, 10}

**Bước 3:** Hệ thức:

Xét chuỗi độ dài n:
- **Kết thúc bằng 0:** n-1 bit đầu tùy ý thỏa mãn → aₙ₋₁ cách
- **Kết thúc bằng 1:** Bit n-1 phải là 0, n-2 bit đầu tùy ý → aₙ₋₂ cách

**Hệ thức:** aₙ = aₙ₋₁ + aₙ₋₂ (n ≥ 3)

**Bước 4:** Nhận xét: Giống Fibonacci!
```
a₁ = 2, a₂ = 3, a₃ = 5, a₄ = 8, a₅ = 13, ...
aₙ = Fₙ₊₂
```

**Bước 5:** Số chuỗi là Fₙ₊₂

---

**Ví dụ 2: Bài toán xếp domino**

**Đề bài:** Có bao nhiêu cách xếp các quân domino 2×1 lấp đầy bảng 2×n?

**Giải:**

**Bước 1:** aₙ = số cách xếp

**Bước 2:**
- a₁ = 1: (một quân dọc)
- a₂ = 2: (hai quân dọc, hoặc hai quân ngang)

**Bước 3:**

Xét cột đầu tiên:
- **Một quân dọc:** n-1 cột còn lại → aₙ₋₁ cách
- **Hai quân ngang:** n-2 cột còn lại → aₙ₋₂ cách

**Hệ thức:** aₙ = aₙ₋₁ + aₙ₋₂

**Bước 4:** aₙ = Fₙ₊₁

---

**Ví dụ 3: Bài toán gửi thư**

**Đề bài:** n người gửi thư, mỗi người một lá. Số cách phân phối sao cho không ai nhận đúng thư của mình?

**Giải:**

**Bước 1:** Dₙ = số hoán vị lỗi (derangement)

**Bước 2:** D₀ = 1, D₁ = 0, D₂ = 1

**Bước 3:** (Phức tạp - dùng nguyên lý bù trừ)

**Hệ thức:**
```
Dₙ = (n-1)[Dₙ₋₁ + Dₙ₋₂]
```

Hoặc:
```
Dₙ = n! × Σ (-1)ᵏ/k!  (k từ 0 đến n)
   ≈ n!/e
```

**Dãy:** 1, 0, 1, 2, 9, 44, 265, ...

---

**Ví dụ 4: Bài toán chia kẹo**

**Đề bài:** Chia n viên kẹo giống nhau cho 3 người, mỗi người ít nhất 1 viên. Có bao nhiêu cách?

**Giải:**

**Phương pháp 1 (Tổ hợp):**
- Đổi biến: yᵢ = xᵢ - 1 ≥ 0
- y₁ + y₂ + y₃ = n - 3
- Đáp án: C(n-1, 2)

**Phương pháp 2 (Hệ thức):**
- aₙ = số cách chia n viên
- a₃ = 1: (1,1,1)
- aₙ = aₙ₋₁ + ... (phức tạp hơn)

Phương pháp 1 đơn giản hơn!

---

## 4.3. GIẢI HỆ THỨC TRUY HỒI

### 4.3.1. Hệ thức truy hồi tuyến tính thuần nhất

**Định nghĩa:**

Hệ thức tuyến tính thuần nhất bậc k với hệ số hằng có dạng:
```
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ
```

Trong đó: c₁, c₂, ..., cₖ là các hằng số, cₖ ≠ 0

---

**Phương trình đặc trưng (Characteristic Equation):**

Giả sử nghiệm có dạng aₙ = rⁿ

Thay vào hệ thức:
```
rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻² + ... + cₖrⁿ⁻ᵏ
```

Chia cho rⁿ⁻ᵏ:
```
rᵏ - c₁rᵏ⁻¹ - c₂rᵏ⁻² - ... - cₖ = 0
```

Đây là **phương trình đặc trưng**.

---

**Định lý (Nghiệm tổng quát):**

Nếu phương trình đặc trưng có:
- k nghiệm phân biệt r₁, r₂, ..., rₖ

Thì nghiệm tổng quát:
```
aₙ = α₁r₁ⁿ + α₂r₂ⁿ + ... + αₖrₖⁿ
```

Các hằng số α₁, α₂, ..., αₖ được xác định từ điều kiện đầu.

---

**Trường hợp nghiệm kép:**

Nếu r là nghiệm bội m của phương trình đặc trưng, thì các số hạng tương ứng trong nghiệm là:
```
(β₁ + β₂n + β₃n² + ... + βₘnᵐ⁻¹)rⁿ
```

---

### 4.3.2. Giải hệ thức truy hồi bậc 2, bậc 3

**A. HỆ THỨC BẬC 2**

**Dạng:** aₙ = c₁aₙ₋₁ + c₂aₙ₋₂

**Phương trình đặc trưng:** r² - c₁r - c₂ = 0

---

**Trường hợp 1: Hai nghiệm phân biệt r₁ ≠ r₂**

**Nghiệm tổng quát:**
```
aₙ = α₁r₁ⁿ + α₂r₂ⁿ
```

**Ví dụ 1:** Giải Fibonacci: Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1

**Giải:**

**Bước 1:** Phương trình đặc trưng:
```
r² = r + 1
r² - r - 1 = 0
```

**Bước 2:** Giải phương trình:
```
r = (1 ± √5) / 2
r₁ = (1 + √5) / 2 = φ  (tỷ lệ vàng)
r₂ = (1 - √5) / 2 = ψ
```

**Bước 3:** Nghiệm tổng quát:
```
Fₙ = α₁φⁿ + α₂ψⁿ
```

**Bước 4:** Xác định α₁, α₂ từ điều kiện đầu:
```
F₀ = 0: α₁ + α₂ = 0
F₁ = 1: α₁φ + α₂ψ = 1
```

Giải hệ:
```
α₂ = -α₁
α₁(φ - ψ) = 1
α₁ = 1/√5
α₂ = -1/√5
```

**Bước 5:** Nghiệm:
```
Fₙ = [φⁿ - ψⁿ] / √5
```

---

**Ví dụ 2:** Giải aₙ = 4aₙ₋₁ - 3aₙ₋₂, a₀ = 1, a₁ = 2

**Giải:**

**Bước 1:** r² - 4r + 3 = 0

**Bước 2:** (r - 1)(r - 3) = 0 → r₁ = 1, r₂ = 3

**Bước 3:** aₙ = α₁×1ⁿ + α₂×3ⁿ = α₁ + α₂×3ⁿ

**Bước 4:**
```
a₀ = 1: α₁ + α₂ = 1
a₁ = 2: α₁ + 3α₂ = 2
```

Giải: α₂ = 1/2, α₁ = 1/2

**Bước 5:** aₙ = (1 + 3ⁿ) / 2

---

**Trường hợp 2: Nghiệm kép r₁ = r₂ = r**

**Nghiệm tổng quát:**
```
aₙ = (α₁ + α₂n)rⁿ
```

**Ví dụ 3:** Giải aₙ = 6aₙ₋₁ - 9aₙ₋₂, a₀ = 1, a₁ = 3

**Giải:**

**Bước 1:** r² - 6r + 9 = 0

**Bước 2:** (r - 3)² = 0 → r = 3 (nghiệm kép)

**Bước 3:** aₙ = (α₁ + α₂n)×3ⁿ

**Bước 4:**
```
a₀ = 1: α₁ = 1
a₁ = 3: (α₁ + α₂)×3 = 3 → α₁ + α₂ = 1 → α₂ = 0
```

**Bước 5:** aₙ = 3ⁿ

---

**B. HỆ THỨC BẬC 3**

**Dạng:** aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + c₃aₙ₋₃

**Phương trình đặc trưng:** r³ - c₁r² - c₂r - c₃ = 0

---

**Ví dụ 4:** Giải aₙ = 6aₙ₋₁ - 11aₙ₋₂ + 6aₙ₋₃, a₀ = 1, a₁ = 0, a₂ = 1

**Giải:**

**Bước 1:** r³ - 6r² + 11r - 6 = 0

**Bước 2:** Thử nghiệm: r = 1 là nghiệm
```
1 - 6 + 11 - 6 = 0 ✓
```

Phân tích: (r - 1)(r² - 5r + 6) = 0

(r - 1)(r - 2)(r - 3) = 0

r₁ = 1, r₂ = 2, r₃ = 3

**Bước 3:** aₙ = α₁×1ⁿ + α₂×2ⁿ + α₃×3ⁿ

**Bước 4:**
```
a₀ = 1: α₁ + α₂ + α₃ = 1
a₁ = 0: α₁ + 2α₂ + 3α₃ = 0
a₂ = 1: α₁ + 4α₂ + 9α₃ = 1
```

Giải hệ: α₁ = 3/2, α₂ = -4, α₃ = 5/2

**Bước 5:** aₙ = (3 - 8×2ⁿ + 5×3ⁿ) / 2

---

**C. HỆ THỨC KHÔNG THUẦN NHẤT**

**Dạng:** aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ + f(n)

---

**Định lý:**

Nghiệm tổng quát = Nghiệm thuần nhất + Nghiệm riêng

```
aₙ = aₙ⁽ʰ⁾ + aₙ⁽ᵖ⁾
```

Trong đó:
- aₙ⁽ʰ⁾: nghiệm của hệ thức thuần nhất
- aₙ⁽ᵖ⁾: một nghiệm riêng của hệ thức không thuần nhất

---

**Tìm nghiệm riêng:**

Phụ thuộc vào dạng của f(n):

| f(n) | Dạng nghiệm riêng aₙ⁽ᵖ⁾ |
|------|--------------------------|
| Pₙ (đa thức bậc t) | nˢQₙ |
| sⁿ | nˢCsⁿ |
| Pₙ×sⁿ | nˢQₙ×sⁿ |

Trong đó:
- Qₙ: đa thức bậc t
- s: số mũ nghiệm đặc trưng
- C: hằng số

---

**Ví dụ 5:** Giải aₙ = 2aₙ₋₁ + 3, a₀ = 1

**Giải:**

**Bước 1:** Nghiệm thuần nhất:
- r - 2 = 0 → r = 2
- aₙ⁽ʰ⁾ = α×2ⁿ

**Bước 2:** Nghiệm riêng:
- f(n) = 3 (hằng số)
- Thử aₙ⁽ᵖ⁾ = C (hằng số)
- Thay vào: C = 2C + 3 → C = -3

**Bước 3:** Nghiệm tổng quát:
```
aₙ = α×2ⁿ - 3
```

**Bước 4:** Điều kiện đầu:
```
a₀ = 1: α - 3 = 1 → α = 4
```

**Bước 5:** aₙ = 4×2ⁿ - 3 = 2ⁿ⁺² - 3

---

**Ví dụ 6:** Giải aₙ = 3aₙ₋₁ + 2ⁿ, a₀ = 1

**Giải:**

**Bước 1:** aₙ⁽ʰ⁾ = α×3ⁿ

**Bước 2:** f(n) = 2ⁿ
- Thử aₙ⁽ᵖ⁾ = C×2ⁿ
- C×2ⁿ = 3C×2ⁿ⁻¹ + 2ⁿ
- C×2ⁿ = (3C/2)×2ⁿ + 2ⁿ
- C = 3C/2 + 1
- -C/2 = 1 → C = -2

**Bước 3:** aₙ = α×3ⁿ - 2×2ⁿ

**Bước 4:** a₀ = 1: α - 2 = 1 → α = 3

**Bước 5:** aₙ = 3ⁿ⁺¹ - 2ⁿ⁺¹

---

**Ví dụ 7:** Giải aₙ = 2aₙ₋₁ + n, a₀ = 1

**Giải:**

**Bước 1:** aₙ⁽ʰ⁾ = α×2ⁿ

**Bước 2:** f(n) = n (đa thức bậc 1)
- Thử aₙ⁽ᵖ⁾ = An + B
- An + B = 2A(n-1) + 2B + n
- An + B = 2An - 2A + 2B + n
- An + B = (2A + 1)n + (-2A + 2B)

So sánh hệ số:
- A = 2A + 1 → A = -1
- B = -2A + 2B → B = 2A = -2

**Bước 3:** aₙ = α×2ⁿ - n - 2

**Bước 4:** a₀ = 1: α - 2 = 1 → α = 3

**Bước 5:** aₙ = 3×2ⁿ - n - 2

---

## TỔNG KẾT CHƯƠNG 4

**Các bước giải hệ thức truy hồi tuyến tính:**

1. **Xác định loại:** Thuần nhất hay không thuần nhất?

2. **Viết phương trình đặc trưng**

3. **Giải phương trình đặc trưng:** Tìm nghiệm

4. **Viết nghiệm tổng quát:**
   - Nghiệm phân biệt: Σ αᵢrᵢⁿ
   - Nghiệm kép bội m: (α₁ + α₂n + ... + αₘnᵐ⁻¹)rⁿ
   - Không thuần nhất: Thêm nghiệm riêng

5. **Xác định hệ số:** Dùng điều kiện đầu

6. **Kết luận:** Viết công thức tường minh

---

**Bảng tóm tắt:**

| Hệ thức | Phương trình đặc trưng | Nghiệm |
|---------|------------------------|---------|
| aₙ = raₙ₋₁ | r₁ - r = 0 | aₙ = α×rⁿ |
| aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ | r² - c₁r - c₂ = 0 | α₁r₁ⁿ + α₂r₂ⁿ |
| Fibonacci | r² - r - 1 = 0 | [φⁿ - ψⁿ]/√5 |
| Tháp Hà Nội | Không thuần nhất | 2ⁿ - 1 |

---

## BÀI TẬP ÔN TẬP CHƯƠNG 4

**Bài 1:** Thiết lập hệ thức truy hồi cho:
a) Số cách xếp n người thành hàng, mỗi người đeo nón đỏ hoặc xanh, không có 2 người liên tiếp đeo nón đỏ
b) Số chuỗi nhị phân độ dài n không chứa "00"

**Bài 2:** Giải các hệ thức sau:
a) aₙ = 5aₙ₋₁ - 6aₙ₋₂, a₀ = 1, a₁ = 0
b) aₙ = 4aₙ₋₁ - 4aₙ₋₂, a₀ = 2, a₁ = 4
c) aₙ = 6aₙ₋₁ - 9aₙ₋₂, a₀ = 0, a₁ = 3

**Bài 3:** Giải hệ thức không thuần nhất:
a) aₙ = 3aₙ₋₁ + 2, a₀ = 1
b) aₙ = 2aₙ₋₁ + 3ⁿ, a₀ = 1
c) aₙ = aₙ₋₁ + 2n, a₀ = 0

**Bài 4:** Tìm công thức tường minh cho dãy:
a) a₀ = 1, a₁ = 3, aₙ = 3aₙ₋₁ - 2aₙ₋₂
b) a₀ = 2, a₁ = 7, aₙ = aₙ₋₁ + 6aₙ₋₂

**Bài 5:** Chứng minh bằng quy nạp:
Nếu Fₙ là dãy Fibonacci thì Fₙ < 2ⁿ với mọi n ≥ 1.

**Bài 6:** Số tiền sau n năm gửi tiết kiệm:
- Gửi ban đầu: 100 triệu
- Lãi suất: 6%/năm
- Hằng năm gửi thêm: 10 triệu

Thiết lập hệ thức và tìm số tiền sau 10 năm.

**Bài 7:** Giải hệ thức bậc 3:
aₙ = aₙ₋₁ + 5aₙ₋₂ + 6aₙ₋₃, a₀ = 1, a₁ = 0, a₂ = 1

**Bài 8:** Tìm mối quan hệ giữa Fₙ và Lucas Lₙ:
- Fₙ: 0, 1, 1, 2, 3, 5, 8, ...
- Lₙ: 2, 1, 3, 4, 7, 11, 18, ...

**Bài 9:** Chứng minh: F₁ + F₃ + F₅ + ... + F₂ₙ₋₁ = F₂ₙ

**Bài 10:** Số cách phủ kín bảng 3×2n bằng các quân domino 2×1. Tìm hệ thức truy hồi.
