# CHƯƠNG 1: TẬP HỢP, ÁNH XẠ VÀ QUAN HỆ

## 1.1. GIỚI THIỆU VỀ LÝ THUYẾT TẬP HỢP

### 1.1.1. Định nghĩa

**Tập hợp** là một khái niệm cơ bản trong toán học, được hiểu là một tập hợp các đối tượng xác định.

**Các khái niệm cơ bản:**
- **Phần tử**: Các đối tượng trong tập hợp được gọi là phần tử
- **Ký hiệu**:
  - `x ∈ A`: x là phần tử của tập A
  - `x ∉ A`: x không là phần tử của tập A

**Cách biểu diễn tập hợp:**

1. **Liệt kê**: A = {1, 2, 3, 4, 5}
2. **Tính chất đặc trưng**: A = {x | x là số tự nhiên và 1 ≤ x ≤ 5}
3. **Quy nạp**: A = {2, 4, 6, 8, ...}

**Các tập hợp đặc biệt:**
- **Tập rỗng** (∅ hoặc {}): Tập không chứa phần tử nào
- **Tập hợp vũ trụ** (U): Tập chứa tất cả các phần tử đang xét
- **ℕ**: Tập số tự nhiên {0, 1, 2, 3, ...}
- **ℤ**: Tập số nguyên {..., -2, -1, 0, 1, 2, ...}
- **ℚ**: Tập số hữu tỉ
- **ℝ**: Tập số thực

**Lực lượng của tập hợp:**
- Số phần tử của tập A được ký hiệu: |A| hoặc card(A)
- Ví dụ: A = {1, 2, 3} thì |A| = 3

### 1.1.2. Tập hợp con

**Định nghĩa:**
Tập A được gọi là tập con của tập B nếu mọi phần tử của A đều là phần tử của B.

**Ký hiệu:** A ⊆ B hoặc B ⊇ A

**Biểu thức logic:** A ⊆ B ⟺ ∀x (x ∈ A → x ∈ B)

**Tính chất:**
1. A ⊆ A với mọi tập A (phản xạ)
2. Nếu A ⊆ B và B ⊆ C thì A ⊆ C (bắc cầu)
3. Nếu A ⊆ B và B ⊆ A thì A = B
4. ∅ ⊆ A với mọi tập A
5. A ⊆ U với mọi tập A (U là tập vũ trụ)

**Tập con thực sự:**
- A là tập con thực sự của B nếu A ⊆ B và A ≠ B
- Ký hiệu: A ⊂ B hoặc A ⊊ B

**Tập lũy thừa:**
- Tập lũy thừa của A, ký hiệu P(A) hoặc 2^A, là tập hợp tất cả các tập con của A
- Nếu |A| = n thì |P(A)| = 2^n
- Ví dụ: A = {1, 2} → P(A) = {∅, {1}, {2}, {1,2}}

### 1.1.3. Biểu diễn hình học của tập hợp

**Biểu đồ Venn (Venn Diagram):**

Biểu đồ Venn là cách biểu diễn trực quan các tập hợp và mối quan hệ giữa chúng bằng các hình khép kín (thường là hình tròn hoặc elip).

**Ứng dụng:**
- Biểu diễn các phép toán tập hợp
- Minh họa mối quan hệ giữa các tập hợp
- Giải các bài toán đếm

**Các trường hợp thường gặp:**
1. A ⊆ B: Hình tròn A nằm hoàn toàn trong hình tròn B
2. A ∩ B ≠ ∅: Hai hình tròn giao nhau
3. A ∩ B = ∅: Hai hình tròn rời nhau

### 1.1.4. Toán tử

**1. Phép hợp (Union):**
- **Định nghĩa:** A ∪ B = {x | x ∈ A hoặc x ∈ B}
- **Tính chất:**
  - Giao hoán: A ∪ B = B ∪ A
  - Kết hợp: (A ∪ B) ∪ C = A ∪ (B ∪ C)
  - Phần tử đơn vị: A ∪ ∅ = A
  - Idempotent: A ∪ A = A
  - A ∪ U = U

**2. Phép giao (Intersection):**
- **Định nghĩa:** A ∩ B = {x | x ∈ A và x ∈ B}
- **Tính chất:**
  - Giao hoán: A ∩ B = B ∩ A
  - Kết hợp: (A ∩ B) ∩ C = A ∩ (B ∩ C)
  - Phần tử đơn vị: A ∩ U = A
  - Idempotent: A ∩ A = A
  - A ∩ ∅ = ∅

**3. Phép hiệu (Difference):**
- **Định nghĩa:** A \ B = {x | x ∈ A và x ∉ B}
- **Lưu ý:** A \ B ≠ B \ A (không giao hoán)

**4. Phép bù (Complement):**
- **Định nghĩa:** A' hoặc Ā = U \ A = {x | x ∈ U và x ∉ A}
- **Tính chất:**
  - (A')' = A
  - A ∪ A' = U
  - A ∩ A' = ∅
  - U' = ∅
  - ∅' = U

**5. Hiệu đối xứng (Symmetric Difference):**
- **Định nghĩa:** A ⊕ B = (A \ B) ∪ (B \ A) = (A ∪ B) \ (A ∩ B)
- **Tính chất:**
  - Giao hoán: A ⊕ B = B ⊕ A
  - Kết hợp: (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C)
  - A ⊕ ∅ = A
  - A ⊕ A = ∅

**Định luật De Morgan:**
1. (A ∪ B)' = A' ∩ B'
2. (A ∩ B)' = A' ∪ B'

**Luật phân phối:**
1. A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
2. A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

**Luật hấp thụ:**
1. A ∪ (A ∩ B) = A
2. A ∩ (A ∪ B) = A

---

## 1.2. ÁNH XẠ

### 1.2.1. Định nghĩa

**Ánh xạ** (hay hàm số, function, mapping) là một qui tắc tương ứng mỗi phần tử của tập này với đúng một phần tử của tập kia.

**Định nghĩa chính thức:**
Cho hai tập hợp A và B. Ánh xạ f từ A đến B là một qui tắc đặt tương ứng mỗi phần tử x ∈ A với duy nhất một phần tử y ∈ B.

**Ký hiệu:**
```
f: A → B
x ↦ f(x)
```

**Các khái niệm:**
- **Tập nguồn (Domain):** A
- **Tập đích (Codomain):** B
- **Ảnh của x:** f(x) hoặc y
- **Tập ảnh (Range/Image):** Im(f) = {f(x) | x ∈ A} ⊆ B
- **Tập xác định:** Tập con của A mà tại đó f được xác định

**Ví dụ:**
1. f: ℝ → ℝ, f(x) = x²
2. g: ℕ → ℕ, g(n) = 2n

### 1.2.2. Ánh xạ tập hợp

**1. Đơn ánh (Injection/One-to-one):**

Ánh xạ f: A → B là đơn ánh nếu mỗi phần tử của B là ảnh của nhiều nhất một phần tử của A.

**Định nghĩa:** ∀x₁, x₂ ∈ A: x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂)

Tương đương: ∀x₁, x₂ ∈ A: f(x₁) = f(x₂) ⇒ x₁ = x₂

**Ví dụ:**
- f: ℝ → ℝ, f(x) = 2x + 1 (đơn ánh)
- g: ℝ → ℝ, g(x) = x² (không đơn ánh vì g(-1) = g(1))

**2. Toàn ánh (Surjection/Onto):**

Ánh xạ f: A → B là toàn ánh nếu mọi phần tử của B đều là ảnh của ít nhất một phần tử của A.

**Định nghĩa:** ∀y ∈ B, ∃x ∈ A: f(x) = y

Tương đương: Im(f) = B

**Ví dụ:**
- f: ℝ → ℝ, f(x) = x³ (toàn ánh)
- g: ℝ → ℝ, g(x) = x² (không toàn ánh vì không có x sao cho x² = -1)

**3. Song ánh (Bijection/One-to-one correspondence):**

Ánh xạ f: A → B là song ánh nếu f vừa đơn ánh vừa toàn ánh.

**Đặc điểm:**
- Mỗi phần tử của B là ảnh của đúng một phần tử của A
- Tồn tại ánh xạ ngược f⁻¹: B → A

**Ví dụ:**
- f: ℝ → ℝ, f(x) = 2x + 1 (song ánh)
- g: ℝ⁺ → ℝ⁺, g(x) = x² (song ánh)

**4. Các phép toán trên ánh xạ:**

**a) Hợp của hai ánh xạ (Composition):**

Cho f: A → B và g: B → C

Hợp g ∘ f: A → C được định nghĩa: (g ∘ f)(x) = g(f(x))

**Tính chất:**
- Kết hợp: (h ∘ g) ∘ f = h ∘ (g ∘ f)
- Không giao hoán: g ∘ f ≠ f ∘ g (nói chung)

**b) Ánh xạ đồng nhất (Identity):**

Ánh xạ I_A: A → A được định nghĩa I_A(x) = x với mọi x ∈ A

**Tính chất:** f ∘ I_A = I_B ∘ f = f

**c) Ánh xạ ngược (Inverse):**

Nếu f: A → B là song ánh, tồn tại ánh xạ ngược f⁻¹: B → A sao cho:
- f⁻¹ ∘ f = I_A
- f ∘ f⁻¹ = I_B

### 1.2.3. Lực lượng của tập hợp

**Định nghĩa:**

Hai tập hợp A và B được gọi là có cùng lực lượng (cardinality) nếu tồn tại song ánh f: A → B.

**Ký hiệu:** |A| = |B| hoặc A ~ B

**Tập hợp đếm được:**

Tập A được gọi là đếm được nếu:
- A là tập hữu hạn, hoặc
- Tồn tại song ánh f: ℕ → A

**Ví dụ:**
- ℕ là đếm được (hiển nhiên)
- ℤ là đếm được (có song ánh với ℕ)
- ℚ là đếm được
- ℝ không đếm được (Định lý Cantor)

**Số lượng ánh xạ:**

1. **Số ánh xạ từ A đến B:** |B|^|A|
2. **Số đơn ánh từ A đến B (|A| ≤ |B|):** P(|B|, |A|) = |B|!/(|B|-|A|)!
3. **Số song ánh từ A đến A:** |A|!

**Định lý Cantor:**

Với mọi tập A: |A| < |P(A)|

**Hệ quả:** Tồn tại vô số "cấp độ" vô hạn khác nhau.

---

## 1.3. QUAN HỆ HAI NGÔI

### 1.3.1. Các khái niệm

**Tích Descartes:**

Cho A và B là hai tập hợp. Tích Descartes của A và B là:

A × B = {(a, b) | a ∈ A và b ∈ B}

**Tính chất:**
- |A × B| = |A| × |B|
- A × B ≠ B × A (nói chung)
- A × ∅ = ∅ × A = ∅

**Quan hệ hai ngôi:**

**Định nghĩa:** Quan hệ hai ngôi R từ A đến B là một tập con của A × B.

R ⊆ A × B

**Ký hiệu:**
- (a, b) ∈ R hoặc aRb: a có quan hệ R với b
- (a, b) ∉ R hoặc a R̸ b: a không có quan hệ R với b

**Quan hệ trên tập A:** Là quan hệ từ A đến chính nó, tức R ⊆ A × A

**Miền và tầm:**
- **Miền (Domain):** dom(R) = {a ∈ A | ∃b ∈ B: (a,b) ∈ R}
- **Tầm (Range):** ran(R) = {b ∈ B | ∃a ∈ A: (a,b) ∈ R}

**Ví dụ:**
1. Quan hệ "nhỏ hơn" trên ℕ: R = {(a,b) | a < b}
2. Quan hệ "chia hết" trên ℕ: R = {(a,b) | a | b}

**Các tính chất của quan hệ:**

**1. Phản xạ (Reflexive):**
R là phản xạ nếu: ∀a ∈ A: (a, a) ∈ R

Ví dụ: Quan hệ "≤" trên ℝ

**2. Đối xứng (Symmetric):**
R là đối xứng nếu: ∀a, b ∈ A: (a, b) ∈ R ⇒ (b, a) ∈ R

Ví dụ: Quan hệ "=" trên ℝ

**3. Phản đối xứng (Antisymmetric):**
R là phản đối xứng nếu: ∀a, b ∈ A: [(a, b) ∈ R ∧ (b, a) ∈ R] ⇒ a = b

Ví dụ: Quan hệ "≤" trên ℝ

**4. Bắc cầu (Transitive):**
R là bắc cầu nếu: ∀a, b, c ∈ A: [(a, b) ∈ R ∧ (b, c) ∈ R] ⇒ (a, c) ∈ R

Ví dụ: Quan hệ "<" trên ℝ

**Các phép toán trên quan hệ:**

**1. Quan hệ ngược (Inverse):**
R⁻¹ = {(b, a) | (a, b) ∈ R}

**2. Hợp (Composition):**
Cho R ⊆ A × B và S ⊆ B × C

S ∘ R = {(a, c) | ∃b ∈ B: (a, b) ∈ R ∧ (b, c) ∈ S}

**3. Lũy thừa:**
- R⁰ = {(a, a) | a ∈ A} (quan hệ đồng nhất)
- R^(n+1) = R^n ∘ R

**4. Bao đóng:**
- **Bao đóng phản xạ:** Thêm tất cả các cặp (a, a)
- **Bao đóng đối xứng:** Thêm (b, a) nếu có (a, b)
- **Bao đóng bắc cầu:** R⁺ = R ∪ R² ∪ R³ ∪ ...

### 1.3.2. Quan hệ thứ tự

**Định nghĩa:**

Quan hệ R trên A là quan hệ thứ tự nếu R có 3 tính chất:
1. Phản xạ
2. Phản đối xứng
3. Bắc cầu

**Ký hiệu:** Thường dùng ≤, ⪯

**(A, ≤)** được gọi là tập có thứ tự (poset - partially ordered set)

**Ví dụ:**
1. (ℕ, ≤): Thứ tự thông thường
2. (P(A), ⊆): Quan hệ bao hàm
3. (ℕ⁺, |): Quan hệ chia hết

**Quan hệ thứ tự toàn phần:**

Quan hệ thứ tự ≤ trên A là toàn phần nếu:
∀a, b ∈ A: a ≤ b hoặc b ≤ a

**Ví dụ:**
- (ℝ, ≤) là thứ tự toàn phần
- (P({1,2}), ⊆) không phải thứ tự toàn phần (vì {1} và {2} không so sánh được)

**Các phần tử đặc biệt:**

Cho (A, ≤) và B ⊆ A

**1. Phần tử cực đại của B:**
a ∈ B là cực đại nếu: ∀b ∈ B: a ≤ b ⇒ a = b

**2. Phần tử cực tiểu của B:**
a ∈ B là cực tiểu nếu: ∀b ∈ B: b ≤ a ⇒ a = b

**3. Phần tử lớn nhất (greatest element):**
a ∈ B là lớn nhất nếu: ∀b ∈ B: b ≤ a

**4. Phần tử nhỏ nhất (least element):**
a ∈ B là nhỏ nhất nếu: ∀b ∈ B: a ≤ b

**5. Cận trên (upper bound):**
a ∈ A là cận trên của B nếu: ∀b ∈ B: b ≤ a

**6. Cận dưới (lower bound):**
a ∈ A là cận dưới của B nếu: ∀b ∈ B: a ≤ b

**7. Chặn trên đúng (supremum - lub):**
Cận trên nhỏ nhất của B, ký hiệu: sup(B)

**8. Chặn dưới đúng (infimum - glb):**
Cận dưới lớn nhất của B, ký hiệu: inf(B)

**Lưu ý:**
- Phần tử lớn nhất/nhỏ nhất là duy nhất (nếu có)
- Có thể có nhiều phần tử cực đại/cực tiểu

**Sơ đồ Hasse:**

Là cách biểu diễn đồ họa của quan hệ thứ tự:
- Mỗi phần tử là một đỉnh
- a < b và không có c nào sao cho a < c < b thì vẽ cạnh từ a đến b
- Phần tử nhỏ hơn ở dưới, lớn hơn ở trên

### 1.3.3. Quan hệ tương đương

**Định nghĩa:**

Quan hệ R trên A là quan hệ tương đương nếu R có 3 tính chất:
1. Phản xạ
2. Đối xứng
3. Bắc cầu

**Ký hiệu:** Thường dùng ~, ≡, ≈

**Ví dụ:**
1. Quan hệ "=" trên ℝ
2. Quan hệ đồng dư modulo n: a ≡ b (mod n) ⟺ n | (a-b)
3. Quan hệ "có cùng số phần tử" trên tập các tập hữu hạn

**Lớp tương đương:**

Cho quan hệ tương đương ~ trên A và a ∈ A

Lớp tương đương của a là: [a] = {x ∈ A | x ~ a}

**Tính chất:**
1. a ∈ [a]
2. b ∈ [a] ⟺ [b] = [a]
3. [a] = [b] hoặc [a] ∩ [b] = ∅

**Phân hoạch (Partition):**

Phân hoạch của tập A là họ các tập con {A₁, A₂, ..., Aₙ} sao cho:
1. Aᵢ ≠ ∅ với mọi i
2. Aᵢ ∩ Aⱼ = ∅ với i ≠ j
3. A₁ ∪ A₂ ∪ ... ∪ Aₙ = A

**Định lý:**

Mỗi quan hệ tương đương trên A xác định duy nhất một phân hoạch của A, và ngược lại.

**Tập thương:**

Tập các lớp tương đương của A theo ~, ký hiệu: A/~ hoặc A/R

A/~ = {[a] | a ∈ A}

**Ví dụ:**
- ℤ/≡ₙ = {[0], [1], ..., [n-1]} (các lớp thặng dư modulo n)

### 1.3.4. Biểu diễn quan hệ hai ngôi

**1. Ma trận quan hệ:**

Cho R ⊆ A × B, A = {a₁, ..., aₘ}, B = {b₁, ..., bₙ}

Ma trận M_R = [mᵢⱼ]_{m×n} với:
```
mᵢⱼ = 1 nếu (aᵢ, bⱼ) ∈ R
mᵢⱼ = 0 nếu (aᵢ, bⱼ) ∉ R
```

**Tính chất:**
- M_{R⁻¹} = M_R^T (chuyển vị)
- M_{S∘R} = M_R × M_S (nhân ma trận Boolean)

**Kiểm tra tính chất:**
- Phản xạ: Đường chéo chính toàn 1
- Đối xứng: M_R = M_R^T
- Phản đối xứng: Nếu M_R[i,j] = M_R[j,i] = 1 thì i = j

**2. Đồ thị quan hệ:**

Biểu diễn quan hệ R trên A = {a₁, ..., aₙ} bằng đồ thị có hướng:
- Mỗi phần tử aᵢ là một đỉnh
- Vẽ cung từ aᵢ đến aⱼ nếu (aᵢ, aⱼ) ∈ R

**Đặc điểm:**
- Phản xạ: Mỗi đỉnh có khuyên (loop)
- Đối xứng: Nếu có cung a→b thì có cung b→a
- Bắc cầu: Nếu có đường đi a→b→c thì có cung a→c

---

## 1.4. QUAN HỆ N-NGÔI

### 1.4.1. Định nghĩa

**Quan hệ n-ngôi:**

Cho n tập hợp A₁, A₂, ..., Aₙ. Quan hệ n-ngôi R trên các tập này là tập con của tích Descartes:

R ⊆ A₁ × A₂ × ... × Aₙ

**Các khái niệm:**
- **Bậc (degree):** n
- **Bộ (tuple):** (a₁, a₂, ..., aₙ) ∈ R
- **Thuộc tính (attribute):** Tên của mỗi vị trí trong bộ

**Ví dụ:**

Quan hệ SINHVIEN(MSSV, HoTen, NgaySinh, DiaChi) là quan hệ 4-ngôi

**Miền giá trị (Domain):**

Miền giá trị của thuộc tính Aᵢ là tập hợp các giá trị có thể của thuộc tính đó.

**Lược đồ (Schema):**

R(A₁: D₁, A₂: D₂, ..., Aₙ: Dₙ)

Trong đó:
- R: tên quan hệ
- Aᵢ: tên thuộc tính
- Dᵢ: miền giá trị của Aᵢ

### 1.4.2. Toán tử trên quan hệ n-ngôi

Các toán tử quan hệ là nền tảng của đại số quan hệ trong cơ sở dữ liệu.

**1. Phép chọn (Selection - σ):**

Chọn các bộ thỏa mãn điều kiện P:

σ_P(R) = {t ∈ R | P(t) là đúng}

**Ví dụ:**
```
σ_{Tuổi > 20}(SINHVIEN)
```
Chọn các sinh viên có tuổi > 20

**2. Phép chiếu (Projection - π):**

Chọn một số thuộc tính từ quan hệ:

π_{A₁, A₂, ..., Aₖ}(R)

**Ví dụ:**
```
π_{HoTen, DiaChi}(SINHVIEN)
```
Lấy họ tên và địa chỉ của sinh viên

**Lưu ý:** Phép chiếu loại bỏ các bộ trùng lặp

**3. Phép hợp (Union - ∪):**

R ∪ S: Hợp của hai quan hệ có cùng lược đồ

**Điều kiện:** R và S phải tương thích về kiểu (type-compatible)

**4. Phép giao (Intersection - ∩):**

R ∩ S: Giao của hai quan hệ có cùng lược đồ

**5. Phép hiệu (Difference - −):**

R − S = {t | t ∈ R và t ∉ S}

**6. Tích Descartes (Cartesian Product - ×):**

R × S: Kết hợp mỗi bộ của R với mỗi bộ của S

Nếu R có n thuộc tính và S có m thuộc tính thì R × S có n+m thuộc tính

**7. Phép kết (Join):**

**a) Kết tự nhiên (Natural Join - ⋈):**

R ⋈ S: Kết hợp các bộ có giá trị bằng nhau trên các thuộc tính chung

**b) Theta-Join (θ-join):**

R ⋈_θ S: Tích Descartes theo sau phép chọn với điều kiện θ

R ⋈_θ S = σ_θ(R × S)

**c) Kết ngoài (Outer Join):**
- **Left outer join (⟕):** Giữ tất cả bộ của R
- **Right outer join (⟖):** Giữ tất cả bộ của S
- **Full outer join (⟗):** Giữ tất cả bộ của cả R và S

**8. Phép chia (Division - ÷):**

R ÷ S: Tìm các bộ trong R liên kết với tất cả các bộ trong S

**Ứng dụng:** Truy vấn "tất cả", "mọi"

**9. Phép gán (Assignment):**

Gán kết quả của biểu thức quan hệ cho biến:

T ← σ_{Tuổi > 20}(SINHVIEN)

**10. Phép đổi tên (Rename - ρ):**

ρ_{S(A₁, ..., Aₙ)}(R): Đổi tên quan hệ R thành S và đổi tên thuộc tính

**Tính chất:**

1. **Giao hoán:**
   - Chọn: σ_P(σ_Q(R)) = σ_Q(σ_P(R))
   - Chiếu: π_A(π_B(R)) = π_A(R) nếu A ⊆ B

2. **Phân tán:**
   - σ_{P∧Q}(R) = σ_P(σ_Q(R))
   - π_A(R ∪ S) = π_A(R) ∪ π_A(S)

3. **Kết hợp:**
   - R ⋈ (S ⋈ T) = (R ⋈ S) ⋈ T

**Ví dụ tổng hợp:**

Cho quan hệ:
- SINHVIEN(MSSV, HoTen, LopID)
- LOP(LopID, TenLop, GiaoVien)

Tìm họ tên sinh viên học lớp "CTRR":

```
π_{HoTen}(σ_{TenLop = 'CTRR'}(SINHVIEN ⋈ LOP))
```

---

## KẾT LUẬN CHƯƠNG 1

Chương 1 đã trình bày các khái niệm nền tảng của Toán học rời rạc:

1. **Lý thuyết tập hợp:** Các phép toán cơ bản, tập con, biểu đồ Venn
2. **Ánh xạ:** Đơn ánh, toàn ánh, song ánh, và lực lượng tập hợp
3. **Quan hệ hai ngôi:** Quan hệ thứ tự và quan hệ tương đương
4. **Quan hệ n-ngôi:** Các toán tử đại số quan hệ

Những kiến thức này là nền tảng cho:
- Lý thuyết cơ sở dữ liệu
- Logic toán học
- Lý thuyết đồ thị
- Khoa học máy tính nói chung

**Các khái niệm quan trọng cần nhớ:**
- Phép toán tập hợp và định luật De Morgan
- Ba loại ánh xạ: đơn, toàn, song
- Tính chất của quan hệ: phản xạ, đối xứng, phản đối xứng, bắc cầu
- Quan hệ thứ tự và quan hệ tương đương
- Các toán tử đại số quan hệ

---

## BÀI TẬP ÔN TẬP CHƯƠNG 1

**Bài 1:** Cho A = {1, 2, 3}, B = {2, 3, 4}. Tìm:
a) A ∪ B, A ∩ B, A \ B, B \ A
b) A ⊕ B (hiệu đối xứng)
c) P(A ∩ B)

**Bài 2:** Chứng minh các đẳng thức:
a) A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
b) (A ∪ B)' = A' ∩ B'

**Bài 3:** Xét tính đơn, toàn, song ánh của các ánh xạ:
a) f: ℝ → ℝ, f(x) = 3x - 5
b) g: ℝ → ℝ, g(x) = x² + 1
c) h: ℝ⁺ → ℝ⁺, h(x) = x²

**Bài 4:** Cho quan hệ R trên ℤ: aRb ⟺ a - b chia hết cho 3
a) Chứng minh R là quan hệ tương đương
b) Tìm [0], [1], [2]
c) Tìm ℤ/R

**Bài 5:** Cho quan hệ R trên A = {1, 2, 3, 4}:
R = {(1,1), (1,2), (2,2), (2,3), (3,3), (4,4)}
a) Vẽ đồ thị quan hệ
b) Viết ma trận quan hệ
c) Kiểm tra các tính chất: phản xạ, đối xứng, phản đối xứng, bắc cầu
d) R có phải là quan hệ thứ tự không?

**Bài 6:** Cho (P({1, 2, 3}), ⊆)
a) Vẽ sơ đồ Hasse
b) Tìm các phần tử cực đại, cực tiểu
c) Tìm phần tử lớn nhất, nhỏ nhất (nếu có)

**Bài 7:** Cho quan hệ SINHVIEN và MONHOC:
- SINHVIEN(MSSV, HoTen, Lop)
- KETQUA(MSSV, MaMon, Diem)
- MONHOC(MaMon, TenMon, SoTC)

Viết biểu thức đại số quan hệ:
a) Tìm họ tên sinh viên lớp "CNTT1"
b) Tìm mã số sinh viên có điểm môn "Toán" > 8
c) Tìm tên môn học mà sinh viên "Nguyễn Văn A" đã học
