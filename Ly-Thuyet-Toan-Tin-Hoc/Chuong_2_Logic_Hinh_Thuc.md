# CHƯƠNG 2: LOGIC HÌNH THỨC

## 2.1. LOGIC MỆNH ĐỀ

### 2.1.1. Khái niệm

**Mệnh đề (Proposition):**

Mệnh đề là một câu khẳng định có thể xác định được tính đúng hoặc sai, nhưng không thể vừa đúng vừa sai.

**Ví dụ:**
- "2 + 2 = 4" → Mệnh đề đúng (True)
- "5 là số chẵn" → Mệnh đề sai (False)
- "Hôm nay trời đẹp" → Mệnh đề (có giá trị đúng/sai cụ thể)

**Không phải mệnh đề:**
- "x + 2 = 5" → Chưa xác định (phụ thuộc x)
- "Hãy đi về!" → Câu mệnh lệnh
- "Bạn học lớp mấy?" → Câu hỏi

**Giá trị chân lý (Truth Value):**
- Đúng (True): ký hiệu T, 1, ⊤
- Sai (False): ký hiệu F, 0, ⊥

**Ký hiệu:**
- Mệnh đề thường được ký hiệu bằng các chữ cái: p, q, r, s, ...
- Công thức: P, Q, R, ...

**Mệnh đề nguyên tố:**
Là mệnh đề đơn giản, không thể phân tích thành các mệnh đề nhỏ hơn.

**Mệnh đề phức hợp:**
Là mệnh đề được tạo thành từ các mệnh đề đơn giản thông qua các phép toán logic.

### 2.1.2. Các phép toán logic mệnh đề

**1. Phép phủ định (Negation - NOT):**

**Ký hiệu:** ¬p, ~p, p', NOT p

**Định nghĩa:** ¬p đúng khi p sai, và ngược lại

**Bảng chân lý:**
```
| p | ¬p |
|---|-----|
| T | F   |
| F | T   |
```

**Ví dụ:**
- p: "Hôm nay trời mưa"
- ¬p: "Hôm nay trời không mưa"

**Tính chất:**
- ¬(¬p) ≡ p (Luật phủ định kép)

---

**2. Phép hội (Conjunction - AND):**

**Ký hiệu:** p ∧ q, p AND q

**Định nghĩa:** p ∧ q đúng khi và chỉ khi cả p và q đều đúng

**Bảng chân lý:**
```
| p | q | p ∧ q |
|---|---|-------|
| T | T |   T   |
| T | F |   F   |
| F | T |   F   |
| F | F |   F   |
```

**Ví dụ:**
- p: "Tôi đói"
- q: "Tôi khát"
- p ∧ q: "Tôi đói và tôi khát"

**Tính chất:**
- Giao hoán: p ∧ q ≡ q ∧ p
- Kết hợp: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)
- Idempotent: p ∧ p ≡ p
- Đơn vị: p ∧ T ≡ p
- Không: p ∧ F ≡ F
- Mâu thuẫn: p ∧ ¬p ≡ F

---

**3. Phép tuyển (Disjunction - OR):**

**Ký hiệu:** p ∨ q, p OR q

**Định nghĩa:** p ∨ q đúng khi ít nhất một trong p hoặc q đúng

**Bảng chân lý:**
```
| p | q | p ∨ q |
|---|---|-------|
| T | T |   T   |
| T | F |   T   |
| F | T |   T   |
| F | F |   F   |
```

**Ví dụ:**
- p: "Tôi học toán"
- q: "Tôi học lý"
- p ∨ q: "Tôi học toán hoặc tôi học lý (hoặc cả hai)"

**Tính chất:**
- Giao hoán: p ∨ q ≡ q ∨ p
- Kết hợp: (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)
- Idempotent: p ∨ p ≡ p
- Đơn vị: p ∨ F ≡ p
- Không: p ∨ T ≡ T
- Bài trung: p ∨ ¬p ≡ T

---

**4. Phép kéo theo (Implication - IF...THEN):**

**Ký hiệu:** p → q, p ⇒ q

**Định nghĩa:** p → q sai khi và chỉ khi p đúng và q sai

**Bảng chân lý:**
```
| p | q | p → q |
|---|---|-------|
| T | T |   T   |
| T | F |   F   |
| F | T |   T   |
| F | F |   T   |
```

**Cách đọc:**
- "Nếu p thì q"
- "p kéo theo q"
- "p chỉ khi q"
- "q nếu p"

**Các thuật ngữ:**
- p: giả thiết (hypothesis, premise, antecedent)
- q: kết luận (conclusion, consequent)

**Ví dụ:**
- "Nếu trời mưa thì đường ướt"
- "Nếu x > 5 thì x > 3"

**Lưu ý quan trọng:**
- Khi p sai, mệnh đề p → q luôn đúng (vacuously true)
- p → q không có nghĩa là p gây ra q

**Các mệnh đề liên quan:**
1. **Mệnh đề đảo (Converse):** q → p
2. **Mệnh đề phủ định (Inverse):** ¬p → ¬q
3. **Mệnh đề phản đảo (Contrapositive):** ¬q → ¬p

**Quan trọng:**
- p → q ≡ ¬q → ¬p (Tương đương logic)
- p → q ≢ q → p (Không tương đương)

**Biểu diễn khác:**
- p → q ≡ ¬p ∨ q
- p → q ≡ ¬(p ∧ ¬q)

---

**5. Phép tương đương (Biconditional - IFF):**

**Ký hiệu:** p ↔ q, p ⟺ q

**Định nghĩa:** p ↔ q đúng khi p và q có cùng giá trị chân lý

**Bảng chân lý:**
```
| p | q | p ↔ q |
|---|---|-------|
| T | T |   T   |
| T | F |   F   |
| F | T |   F   |
| F | F |   T   |
```

**Cách đọc:**
- "p khi và chỉ khi q"
- "p tương đương q"
- "p nếu và chỉ nếu q" (if and only if - iff)

**Ví dụ:**
- "Một số chia hết cho 2 khi và chỉ khi nó là số chẵn"
- x² = 4 ⟺ x = ±2

**Biểu diễn khác:**
- p ↔ q ≡ (p → q) ∧ (q → p)
- p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)

**Tính chất:**
- Giao hoán: p ↔ q ≡ q ↔ p
- Kết hợp: (p ↔ q) ↔ r ≡ p ↔ (q ↔ r)

---

**6. Phép tuyển loại trừ (Exclusive OR - XOR):**

**Ký hiệu:** p ⊕ q

**Định nghĩa:** p ⊕ q đúng khi p và q có giá trị chân lý khác nhau

**Bảng chân lý:**
```
| p | q | p ⊕ q |
|---|---|-------|
| T | T |   F   |
| T | F |   T   |
| F | T |   T   |
| F | F |   F   |
```

**Biểu diễn:**
- p ⊕ q ≡ (p ∨ q) ∧ ¬(p ∧ q)
- p ⊕ q ≡ (p ∧ ¬q) ∨ (¬p ∧ q)
- p ⊕ q ≡ ¬(p ↔ q)

---

**Thứ tự ưu tiên các phép toán:**

1. ¬ (Negation) - cao nhất
2. ∧ (Conjunction)
3. ∨ (Disjunction)
4. → (Implication)
5. ↔ (Biconditional) - thấp nhất

---

**Các định luật logic quan trọng:**

**1. Định luật De Morgan:**
- ¬(p ∧ q) ≡ ¬p ∨ ¬q
- ¬(p ∨ q) ≡ ¬p ∧ ¬q

**2. Luật phân phối:**
- p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
- p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)

**3. Luật hấp thụ:**
- p ∨ (p ∧ q) ≡ p
- p ∧ (p ∨ q) ≡ p

**4. Luật kết hợp:**
- (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)
- (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)

**5. Luật giao hoán:**
- p ∧ q ≡ q ∧ p
- p ∨ q ≡ q ∨ p

**6. Luật idempotent:**
- p ∧ p ≡ p
- p ∨ p ≡ p

**7. Luật phủ định kép:**
- ¬(¬p) ≡ p

**8. Luật đơn vị:**
- p ∧ T ≡ p
- p ∨ F ≡ p

**9. Luật thống trị:**
- p ∨ T ≡ T
- p ∧ F ≡ F

**10. Luật bù:**
- p ∨ ¬p ≡ T (Bài trung)
- p ∧ ¬p ≡ F (Mâu thuẫn)

**11. Luật kéo theo:**
- p → q ≡ ¬p ∨ q
- p → q ≡ ¬q → ¬p (Phản đảo)
- p → q ≡ ¬(p ∧ ¬q)

**12. Luật tương đương:**
- p ↔ q ≡ (p → q) ∧ (q → p)
- p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)

---

**Dạng chuẩn:**

**1. Dạng chuẩn tuyển (Disjunctive Normal Form - DNF):**

Là tuyển của các hội:
- (p ∧ q) ∨ (¬p ∧ r) ∨ (q ∧ ¬r)

**2. Dạng chuẩn hội (Conjunctive Normal Form - CNF):**

Là hội của các tuyển:
- (p ∨ q) ∧ (¬p ∨ r) ∧ (q ∨ ¬r)

**Mệnh đề hằng đúng (Tautology):**
Mệnh đề luôn đúng với mọi giá trị chân lý.
- Ví dụ: p ∨ ¬p, p → p, (p ∧ q) → p

**Mệnh đề hằng sai (Contradiction):**
Mệnh đề luôn sai với mọi giá trị chân lý.
- Ví dụ: p ∧ ¬p, ¬(p → p)

**Mệnh đề thỏa được (Contingency):**
Mệnh đề có thể đúng hoặc sai tùy giá trị.
- Ví dụ: p ∧ q, p → q

### 2.1.3. Các quy tắc suy diễn

**Suy diễn logic:**

Suy diễn là quá trình từ các mệnh đề tiền đề (premises) suy ra kết luận (conclusion).

**Dạng tổng quát:**
```
p₁, p₂, ..., pₙ ⊢ q
```
Hoặc:
```
p₁
p₂
...
pₙ
∴ q
```

**Lập luận hợp lệ (Valid argument):**

Lập luận hợp lệ nếu: (p₁ ∧ p₂ ∧ ... ∧ pₙ) → q là hằng đúng

---

**Các quy tắc suy diễn cơ bản:**

**1. Modus Ponens (MP):**
```
p → q
p
∴ q
```
Nếu p kéo theo q, và p đúng, thì q đúng.

**Ví dụ:**
- Nếu trời mưa thì đường ướt
- Trời mưa
- → Đường ướt

---

**2. Modus Tollens (MT):**
```
p → q
¬q
∴ ¬p
```
Nếu p kéo theo q, và q sai, thì p sai.

**Ví dụ:**
- Nếu tôi học chăm thì tôi đậu
- Tôi không đậu
- → Tôi không học chăm

---

**3. Luật tam đoạn luận (Hypothetical Syllogism - HS):**
```
p → q
q → r
∴ p → r
```

**Ví dụ:**
- Nếu mưa thì đường ướt
- Nếu đường ướt thì trơn
- → Nếu mưa thì đường trơn

---

**4. Tam đoạn luận tuyển (Disjunctive Syllogism - DS):**
```
p ∨ q
¬p
∴ q
```

**Ví dụ:**
- Hôm nay thứ 7 hoặc chủ nhật
- Hôm nay không phải thứ 7
- → Hôm nay là chủ nhật

---

**5. Bổ sung (Addition):**
```
p
∴ p ∨ q
```

Nếu p đúng thì p ∨ q đúng với mọi q.

---

**6. Đơn giản hóa (Simplification):**
```
p ∧ q
∴ p
```

Nếu p và q đều đúng thì p đúng.

---

**7. Kết hợp (Conjunction):**
```
p
q
∴ p ∧ q
```

Nếu p đúng và q đúng thì p ∧ q đúng.

---

**8. Giải quyết (Resolution):**
```
p ∨ q
¬p ∨ r
∴ q ∨ r
```

---

**9. Nghịch lý kiến thiết (Constructive Dilemma):**
```
(p → q) ∧ (r → s)
p ∨ r
∴ q ∨ s
```

---

**10. Nghịch lý phá hoại (Destructive Dilemma):**
```
(p → q) ∧ (r → s)
¬q ∨ ¬s
∴ ¬p ∨ ¬r
```

---

**Các quy tắc suy diễn mở rộng:**

**1. Quy tắc thêm giả thiết (Conditional Proof - CP):**
Để chứng minh p → q:
- Giả sử p đúng
- Suy ra q đúng
- Kết luận p → q

**2. Quy tắc phản chứng (Proof by Contradiction):**
Để chứng minh p:
- Giả sử ¬p
- Suy ra mâu thuẫn
- Kết luận p đúng

---

## 2.2. LOGIC VỊ TỪ

### 2.2.1. Khái niệm vị từ

**Hạn chế của logic mệnh đề:**

Logic mệnh đề không thể biểu diễn cấu trúc bên trong của mệnh đề.

**Ví dụ:**
- "Mọi người đều phải chết" - Không thể phân tích bằng logic mệnh đề
- Cần logic vị từ để biểu diễn "mọi người", "phải chết"

**Vị từ (Predicate):**

Vị từ là một mệnh đề có chứa biến, và trở thành mệnh đề khi thay biến bằng giá trị cụ thể.

**Ký hiệu:** P(x), Q(x, y), R(x, y, z), ...

**Ví dụ:**
- P(x): "x là số chẵn"
- Q(x, y): "x > y"
- R(x): "x là sinh viên"

**Miền (Domain/Universe of Discourse):**

Tập hợp các giá trị mà biến có thể nhận.

**Ví dụ:**
- Miền của x có thể là ℕ, ℤ, ℝ, tập sinh viên, ...

**Mệnh đề hóa vị từ:**

1. **Thay biến bằng hằng:**
   - P(x): "x là số chẵn"
   - P(4): "4 là số chẵn" → Đúng
   - P(3): "3 là số chẵn" → Sai

2. **Dùng lượng từ:** ∀, ∃

### 2.2.2. Lượng từ

**1. Lượng từ vũ trụ (Universal Quantifier):**

**Ký hiệu:** ∀ (for all, for every, for each)

**Định nghĩa:** ∀x P(x) đúng khi P(x) đúng với mọi x trong miền.

**Đọc:** "Với mọi x, P(x)" hoặc "Mọi x đều có tính chất P"

**Ví dụ:**
- ∀x (x² ≥ 0) [trên ℝ] → Đúng
- ∀x (x > 0) [trên ℤ] → Sai
- ∀x ∈ ℕ (x + 1 > x) → Đúng

**Phủ định:**
- ¬(∀x P(x)) ≡ ∃x ¬P(x)

---

**2. Lượng từ tồn tại (Existential Quantifier):**

**Ký hiệu:** ∃ (there exists, there is)

**Định nghĩa:** ∃x P(x) đúng khi P(x) đúng cho ít nhất một x trong miền.

**Đọc:** "Tồn tại x sao cho P(x)" hoặc "Có x thỏa mãn P"

**Ví dụ:**
- ∃x (x² = 4) [trên ℝ] → Đúng (x = ±2)
- ∃x (x² < 0) [trên ℝ] → Sai
- ∃x ∈ ℕ (x + 5 = 0) → Sai

**Phủ định:**
- ¬(∃x P(x)) ≡ ∀x ¬P(x)

---

**3. Lượng từ tồn tại duy nhất:**

**Ký hiệu:** ∃! (there exists a unique)

**Định nghĩa:** ∃!x P(x) đúng khi có đúng một x thỏa mãn P(x).

**Biểu diễn:**
- ∃!x P(x) ≡ ∃x (P(x) ∧ ∀y (P(y) → y = x))

**Ví dụ:**
- ∃!x (x + 5 = 0) [trên ℝ] → Đúng (x = -5)

---

**Miền của lượng từ:**

Có thể giới hạn miền của biến:
- ∀x ∈ A P(x)
- ∃x ∈ B Q(x)

**Biến đổi:**
- ∀x ∈ A P(x) ≡ ∀x (x ∈ A → P(x))
- ∃x ∈ A P(x) ≡ ∃x (x ∈ A ∧ P(x))

---

**Biến tự do và biến ràng buộc:**

**Biến ràng buộc (Bound variable):**
Biến bị ràng buộc bởi lượng từ.

**Biến tự do (Free variable):**
Biến không bị ràng buộc.

**Ví dụ:**
- ∀x (x + y = 5): x là biến ràng buộc, y là biến tự do
- ∀x ∃y (x < y): cả x và y đều là biến ràng buộc

---

**Thứ tự lượng từ:**

Thứ tự của các lượng từ rất quan trọng!

**Ví dụ:**
1. ∀x ∃y (x < y): "Với mọi x, tồn tại y sao cho x < y" → Đúng [trên ℝ]
2. ∃y ∀x (x < y): "Tồn tại y sao cho mọi x đều x < y" → Sai [trên ℝ]

**Quy tắc:**
- ∀x ∀y P(x, y) ≡ ∀y ∀x P(x, y)
- ∃x ∃y P(x, y) ≡ ∃y ∃x P(x, y)
- ∀x ∃y P(x, y) ≢ ∃y ∀x P(x, y)

---

**Phủ định lượng từ (Định luật De Morgan cho lượng từ):**

1. ¬(∀x P(x)) ≡ ∃x ¬P(x)
2. ¬(∃x P(x)) ≡ ∀x ¬P(x)

**Ví dụ:**
- ¬(∀x (x² ≥ 0)) ≡ ∃x (x² < 0)
- ¬(∃x (x > 10)) ≡ ∀x (x ≤ 10)

**Phủ định phức tạp:**
```
¬(∀x ∃y P(x, y)) ≡ ∃x ∀y ¬P(x, y)
¬(∃x ∀y P(x, y)) ≡ ∀x ∃y ¬P(x, y)
```

---

**Lượng từ với phép toán logic:**

**Phân phối:**
- ∀x (P(x) ∧ Q(x)) ≡ ∀x P(x) ∧ ∀x Q(x)
- ∃x (P(x) ∨ Q(x)) ≡ ∃x P(x) ∨ ∃x Q(x)

**Không phân phối:**
- ∀x (P(x) ∨ Q(x)) ⇏ ∀x P(x) ∨ ∀x Q(x)
- ∃x (P(x) ∧ Q(x)) ⇏ ∃x P(x) ∧ ∃x Q(x)

### 2.2.3. Các quy tắc suy luận với lượng từ

**1. Cụ thể hóa vũ trụ (Universal Instantiation - UI):**
```
∀x P(x)
∴ P(c)
```
Nếu P(x) đúng với mọi x thì P(c) đúng với hằng c cụ thể.

**Ví dụ:**
- ∀x (x² ≥ 0)
- ∴ 3² ≥ 0

---

**2. Tổng quát hóa vũ trụ (Universal Generalization - UG):**
```
P(c) với c tùy ý
∴ ∀x P(x)
```
Nếu P(c) đúng với c tùy ý thì P(x) đúng với mọi x.

**Điều kiện:** c phải là phần tử tùy ý (không có điều kiện ràng buộc).

---

**3. Cụ thể hóa tồn tại (Existential Instantiation - EI):**
```
∃x P(x)
∴ P(c) cho một c nào đó
```

**Lưu ý:** c là phần tử cụ thể (nhưng chưa biết) thỏa mãn P.

---

**4. Tổng quát hóa tồn tại (Existential Generalization - EG):**
```
P(c)
∴ ∃x P(x)
```
Nếu P(c) đúng với c cụ thể thì tồn tại x thỏa mãn P(x).

---

**Ví dụ suy luận:**

**Ví dụ 1:**
```
Tiền đề: ∀x (P(x) → Q(x))
Tiền đề: P(a)
Kết luận: Q(a)
```

**Chứng minh:**
1. ∀x (P(x) → Q(x))    [Tiền đề]
2. P(a) → Q(a)         [UI từ (1)]
3. P(a)                [Tiền đề]
4. Q(a)                [MP từ (2), (3)]

---

**Ví dụ 2:**
```
Tiền đề: ∀x (P(x) → Q(x))
Tiền đề: ∃x P(x)
Kết luận: ∃x Q(x)
```

**Chứng minh:**
1. ∀x (P(x) → Q(x))    [Tiền đề]
2. ∃x P(x)             [Tiền đề]
3. P(c)                [EI từ (2)]
4. P(c) → Q(c)         [UI từ (1)]
5. Q(c)                [MP từ (3), (4)]
6. ∃x Q(x)             [EG từ (5)]

---

**Các quy tắc quan trọng:**

**1. Quy tắc phổ dụng (Universal Modus Ponens):**
```
∀x (P(x) → Q(x))
P(a)
∴ Q(a)
```

**2. Quy tắc phổ dụng phủ định (Universal Modus Tollens):**
```
∀x (P(x) → Q(x))
¬Q(a)
∴ ¬P(a)
```

---

## 2.3. PHƯƠNG PHÁP CHỨNG MINH

### 2.3.1. Chứng minh trực tiếp

**1. Chứng minh trực tiếp (Direct Proof):**

**Phương pháp:** Để chứng minh p → q:
- Giả sử p đúng
- Sử dụng các định lý, định nghĩa, công thức đã biết
- Suy ra q đúng

**Ví dụ 1:** Chứng minh rằng nếu n là số lẻ thì n² là số lẻ.

**Chứng minh:**
- Giả sử n là số lẻ
- → n = 2k + 1 với k ∈ ℤ
- → n² = (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1
- → n² có dạng 2m + 1 (với m = 2k² + 2k)
- → n² là số lẻ

**Ví dụ 2:** Chứng minh nếu n là số nguyên và 3n + 2 là số lẻ thì n là số lẻ.

**Chứng minh:**
- Giả sử 3n + 2 là số lẻ
- → 3n + 2 = 2k + 1 với k ∈ ℤ
- → 3n = 2k - 1 = 2(k - 1)
- → 3n là số chẵn
- → n phải là số chẵn... (SAI!)

*Sửa lại bằng phản chứng (xem phần 2.3.2)*

---

**2. Chứng minh theo trường hợp (Proof by Cases):**

**Phương pháp:** Để chứng minh p:
- Chia thành các trường hợp: p₁ ∨ p₂ ∨ ... ∨ pₙ
- Chứng minh p đúng trong mỗi trường hợp

**Ví dụ:** Chứng minh |xy| = |x||y| với mọi x, y ∈ ℝ.

**Chứng minh:**

**Trường hợp 1:** x ≥ 0, y ≥ 0
- xy ≥ 0 → |xy| = xy
- |x| = x, |y| = y → |x||y| = xy
- → |xy| = |x||y|

**Trường hợp 2:** x ≥ 0, y < 0
- xy ≤ 0 → |xy| = -xy
- |x| = x, |y| = -y → |x||y| = x(-y) = -xy
- → |xy| = |x||y|

**Trường hợp 3:** x < 0, y ≥ 0 (tương tự trường hợp 2)

**Trường hợp 4:** x < 0, y < 0
- xy > 0 → |xy| = xy
- |x| = -x, |y| = -y → |x||y| = (-x)(-y) = xy
- → |xy| = |x||y|

**Kết luận:** |xy| = |x||y| với mọi x, y ∈ ℝ.

---

**3. Chứng minh tương đương (Proof of Equivalence):**

**Phương pháp:** Để chứng minh p ↔ q:

**Cách 1:** Chứng minh p → q và q → p

**Cách 2:** Chứng minh chuỗi tương đương:
p ↔ p₁ ↔ p₂ ↔ ... ↔ pₙ ↔ q

**Ví dụ:** Chứng minh n là số chẵn ↔ n² là số chẵn.

**Chứng minh:**

**(→)** Nếu n chẵn thì n² chẵn:
- n = 2k → n² = 4k² = 2(2k²) → n² chẵn

**(←)** Nếu n² chẵn thì n chẵn:
- Chứng minh phản đảo: Nếu n lẻ thì n² lẻ (đã chứng minh ở trên)

**Kết luận:** n chẵn ↔ n² chẵn.

---

**4. Chứng minh tồn tại (Existence Proof):**

**Chứng minh kiến thiết (Constructive):**
Chỉ ra cụ thể đối tượng tồn tại.

**Ví dụ:** Chứng minh tồn tại số vô tỷ a, b sao cho a^b hữu tỷ.

**Chứng minh:**
- Xét √2^(√2)
- Nếu nó hữu tỷ → chọn a = b = √2
- Nếu nó vô tỷ → chọn a = √2^(√2), b = √2
  - Khi đó: a^b = (√2^(√2))^(√2) = √2^(√2·√2) = √2² = 2 (hữu tỷ)

**Chứng minh không kiến thiết (Non-constructive):**
Chứng minh sự tồn tại mà không chỉ ra cụ thể.

---

**5. Chứng minh duy nhất (Uniqueness Proof):**

**Phương pháp:**
1. Chứng minh tồn tại
2. Chứng minh duy nhất (giả sử có hai, chứng minh chúng bằng nhau)

**Ví dụ:** Chứng minh phương trình x + 5 = 0 có nghiệm duy nhất trên ℝ.

**Chứng minh:**

**Tồn tại:** x = -5 là nghiệm.

**Duy nhất:** Giả sử x₁, x₂ là hai nghiệm:
- x₁ + 5 = 0 → x₁ = -5
- x₂ + 5 = 0 → x₂ = -5
- → x₁ = x₂

**Kết luận:** Nghiệm duy nhất là x = -5.

### 2.3.2. Chứng minh gián tiếp

**1. Chứng minh phản đảo (Contrapositive Proof):**

**Phương pháp:** Để chứng minh p → q, chứng minh ¬q → ¬p

**Cơ sở:** p → q ≡ ¬q → ¬p

**Ví dụ:** Chứng minh nếu n² là số lẻ thì n là số lẻ.

**Chứng minh phản đảo:**
Chứng minh: Nếu n chẵn thì n² chẵn
- n = 2k → n² = 4k² = 2(2k²) → n² chẵn

**Kết luận:** Nếu n² lẻ thì n lẻ.

---

**2. Chứng minh phản chứng (Proof by Contradiction):**

**Phương pháp:** Để chứng minh p:
- Giả sử ¬p đúng
- Suy ra mâu thuẫn (Q ∧ ¬Q)
- Kết luận p đúng

**Cơ sở:** [¬p → (Q ∧ ¬Q)] → p

**Ví dụ 1:** Chứng minh √2 là số vô tỷ.

**Chứng minh:**

Giả sử √2 là số hữu tỷ.
- → √2 = p/q với p, q ∈ ℤ, q ≠ 0, gcd(p, q) = 1
- → 2 = p²/q²
- → 2q² = p²
- → p² chẵn → p chẵn → p = 2k
- → 2q² = 4k² → q² = 2k² → q² chẵn → q chẵn
- → p và q đều chẵn → gcd(p, q) ≥ 2 (mâu thuẫn!)

**Kết luận:** √2 là số vô tỷ.

---

**Ví dụ 2:** Chứng minh có vô số số nguyên tố.

**Chứng minh:**

Giả sử có hữu hạn số nguyên tố: p₁, p₂, ..., pₙ

Xét số: N = p₁ · p₂ · ... · pₙ + 1

**Trường hợp 1:** N là số nguyên tố
- → Tồn tại số nguyên tố không nằm trong danh sách (mâu thuẫn!)

**Trường hợp 2:** N là hợp số
- → N có ước nguyên tố p
- p không thể là p₁, p₂, ..., pₙ (vì N chia cho bất kỳ pᵢ nào đều dư 1)
- → Tồn tại số nguyên tố không nằm trong danh sách (mâu thuẫn!)

**Kết luận:** Có vô số số nguyên tố.

---

**3. Chứng minh quy nạp (Mathematical Induction):**

**Phương pháp:** Để chứng minh P(n) đúng với mọi n ≥ n₀:

**Bước 1 (Cơ sở):** Chứng minh P(n₀) đúng

**Bước 2 (Quy nạp):**
- Giả thiết quy nạp: Giả sử P(k) đúng với k ≥ n₀
- Chứng minh: P(k+1) đúng

**Kết luận:** P(n) đúng với mọi n ≥ n₀

---

**Ví dụ 1:** Chứng minh 1 + 2 + 3 + ... + n = n(n+1)/2

**Chứng minh:**

**Bước cơ sở:** n = 1
- VT = 1
- VP = 1(1+1)/2 = 1
- → P(1) đúng

**Bước quy nạp:**
Giả sử P(k) đúng: 1 + 2 + ... + k = k(k+1)/2

Chứng minh P(k+1):
```
1 + 2 + ... + k + (k+1) = [1 + 2 + ... + k] + (k+1)
                         = k(k+1)/2 + (k+1)
                         = [k(k+1) + 2(k+1)]/2
                         = [(k+1)(k+2)]/2
                         = (k+1)[(k+1)+1]/2
```
→ P(k+1) đúng

**Kết luận:** Công thức đúng với mọi n ≥ 1.

---

**Ví dụ 2:** Chứng minh 2ⁿ > n² với mọi n ≥ 5

**Chứng minh:**

**Bước cơ sở:** n = 5
- 2⁵ = 32 > 25 = 5² ✓

**Bước quy nạp:**
Giả sử 2^k > k² với k ≥ 5

Chứng minh 2^(k+1) > (k+1)²:
```
2^(k+1) = 2 · 2^k > 2 · k² (theo giả thiết quy nạp)
```

Cần chứng minh: 2k² > (k+1)² = k² + 2k + 1

⟺ k² > 2k + 1
⟺ k² - 2k - 1 > 0

Với k ≥ 5: k² - 2k - 1 ≥ 25 - 10 - 1 = 14 > 0 ✓

**Kết luận:** 2ⁿ > n² với mọi n ≥ 5.

---

**4. Quy nạp mạnh (Strong Induction):**

**Giả thiết quy nạp mạnh:**
Giả sử P(n₀), P(n₀+1), ..., P(k) đều đúng

**Chứng minh:** P(k+1) đúng

**Ví dụ:** Mọi số nguyên n ≥ 2 đều có thể phân tích thành tích các số nguyên tố.

**Chứng minh:**

**Cơ sở:** n = 2 là số nguyên tố ✓

**Quy nạp:** Giả sử mọi số từ 2 đến k đều phân tích được.

Xét k+1:
- Nếu k+1 là số nguyên tố → xong
- Nếu k+1 hợp số → k+1 = a·b với 2 ≤ a, b ≤ k
  - Theo giả thiết: a, b đều phân tích được
  - → k+1 phân tích được

**Kết luận:** Định lý đúng.

---

**5. Quy nạp cấu trúc (Structural Induction):**

Dùng cho các cấu trúc đệ quy (cây, danh sách, công thức, ...).

**Ví dụ:** Chứng minh mọi công thức logic được xây dựng đúng có số dấu ngoặc trái bằng số dấu ngoặc phải.

---

## KẾT LUẬN CHƯƠNG 2

Chương 2 đã trình bày:

1. **Logic mệnh đề:**
   - Các phép toán logic: ¬, ∧, ∨, →, ↔
   - Các định luật logic
   - Quy tắc suy diễn

2. **Logic vị từ:**
   - Vị từ và lượng từ: ∀, ∃
   - Phủ định lượng từ
   - Suy luận với lượng từ

3. **Phương pháp chứng minh:**
   - Chứng minh trực tiếp
   - Chứng minh phản đảo
   - Chứng minh phản chứng
   - Chứng minh quy nạp

**Kỹ năng cần đạt được:**
- Xác định giá trị chân lý của mệnh đề
- Chuyển đổi giữa các dạng mệnh đề
- Áp dụng quy tắc suy diễn
- Lượng hóa mệnh đề bằng logic vị từ
- Lựa chọn phương pháp chứng minh phù hợp

---

## BÀI TẬP ÔN TẬP CHƯƠNG 2

**Bài 1:** Cho p, q là mệnh đề. Lập bảng chân lý:
a) (p → q) ∧ (q → p)
b) (p ∨ q) → (p ∧ q)
c) ¬(p ↔ q) ↔ (p ⊕ q)

**Bài 2:** Chứng minh các đẳng thức:
a) p → q ≡ ¬p ∨ q
b) ¬(p → q) ≡ p ∧ ¬q
c) (p → q) ∧ (p → r) ≡ p → (q ∧ r)

**Bài 3:** Sử dụng quy tắc suy diễn để chứng minh:
```
Tiền đề: p → (q ∨ r)
Tiền đề: ¬q ∧ ¬r
Kết luận: ¬p
```

**Bài 4:** Phủ định các mệnh đề:
a) ∀x ∃y (x + y = 0)
b) ∃x ∀y (x ≤ y)
c) ∀x (P(x) → ∃y Q(x, y))

**Bài 5:** Chứng minh nếu n² là số chẵn thì n là số chẵn (dùng phản đảo).

**Bài 6:** Chứng minh √3 là số vô tỷ (dùng phản chứng).

**Bài 7:** Chứng minh bằng quy nạp:
a) 1² + 2² + ... + n² = n(n+1)(2n+1)/6
b) 3ⁿ - 1 chia hết cho 2 với mọi n ≥ 1
c) n! > 2ⁿ với mọi n ≥ 4

**Bài 8:** Viết dạng logic vị từ:
a) "Mọi sinh viên đều học toán"
b) "Có sinh viên học cả toán và lý"
c) "Không có sinh viên nào học tất cả các môn"
