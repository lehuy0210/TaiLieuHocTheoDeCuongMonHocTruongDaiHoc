# CHƯƠNG 6: LÝ THUYẾT ĐỒ THỊ

## 6.1. CÁC KHÁI NIỆM CƠ BẢN VỀ ĐỒ THỊ

### 6.1.1. Đồ thị vô hướng và có hướng

**Lịch sử:**

Lý thuyết đồ thị bắt đầu từ bài toán 7 cây cầu Königsberg của Euler (1736).

**Ứng dụng:**
- Mạng máy tính
- Mạng xã hội
- Bản đồ đường đi
- Cơ sở dữ liệu
- Trí tuệ nhân tạo

---

**A. ĐỒ THỊ VÔ HƯỚNG**

**Định nghĩa:**

Đồ thị vô hướng G = (V, E) gồm:
- V: tập hữu hạn các đỉnh (vertices, nodes)
- E: tập các cạnh (edges) - cặp không có thứ tự của các đỉnh

**Ký hiệu:**
- |V|: số đỉnh
- |E|: số cạnh
- Cạnh nối u và v: {u, v} hoặc (u, v) hoặc uv

---

**Ví dụ:**

G = (V, E)
- V = {1, 2, 3, 4}
- E = {{1,2}, {1,3}, {2,3}, {3,4}}

```
    1 ---- 2
     \    /
      \  /
       3 ---- 4
```

---

**Các khái niệm:**

**1. Đỉnh kề nhau (Adjacent vertices):**
Hai đỉnh u và v kề nhau nếu có cạnh nối chúng.

**2. Cạnh liên thuộc (Incident edge):**
Cạnh e liên thuộc với đỉnh v nếu v là một đầu mút của e.

**3. Bậc của đỉnh (Degree):**
Bậc của đỉnh v, ký hiệu deg(v), là số cạnh liên thuộc với v.

**Quy ước:** Khuyên (loop) được tính 2 lần.

**Ví dụ:**
```
    1 ---- 2
     \    /
      \  /
       3 ---- 4

deg(1) = 2
deg(2) = 2
deg(3) = 3
deg(4) = 1
```

**4. Định lý bắt tay (Handshaking Theorem):**

```
Σ deg(v) = 2|E|
```

**Giải thích:** Mỗi cạnh đóng góp 2 vào tổng bậc.

**Hệ quả:** Số đỉnh bậc lẻ luôn chẵn.

---

**5. Đồ thị đơn (Simple graph):**
- Không có khuyên (loop)
- Không có cạnh bội (multiple edges)

**6. Đồ thị đa (Multigraph):**
Có cạnh bội nhưng không có khuyên.

**7. Đồ thị giả (Pseudograph):**
Có thể có cả khuyên và cạnh bội.

---

**8. Đồ thị đầy đủ (Complete graph):**

Đồ thị Kₙ: Đồ thị đơn có n đỉnh, mỗi cặp đỉnh đều có cạnh nối.

**Số cạnh:** |E| = C(n, 2) = n(n-1)/2

**Ví dụ:**
- K₃: Tam giác
- K₄: Hình tứ giác đầy đủ
- K₅: Ngũ giác đầy đủ

---

**B. ĐỒ THỊ CÓ HƯỚNG**

**Định nghĩa:**

Đồ thị có hướng (digraph) G = (V, E) gồm:
- V: tập đỉnh
- E: tập các cung (arcs) - cặp có thứ tự của các đỉnh

**Ký hiệu cung:** (u, v) hoặc u → v

**Khác với đồ thị vô hướng:** (u, v) ≠ (v, u)

---

**Ví dụ:**

```
    1 → 2
    ↑   ↓
    4 ← 3
```

V = {1, 2, 3, 4}
E = {(1,2), (2,3), (3,4), (4,1)}

---

**Các khái niệm:**

**1. Bậc vào (In-degree):**
deg⁻(v) = số cung đi vào v

**2. Bậc ra (Out-degree):**
deg⁺(v) = số cung đi ra từ v

**Ví dụ:**
```
    1 → 2
    ↑   ↓
    4 ← 3

deg⁻(1) = 1, deg⁺(1) = 1
deg⁻(2) = 1, deg⁺(2) = 1
deg⁻(3) = 1, deg⁺(3) = 1
deg⁻(4) = 1, deg⁺(4) = 1
```

**Định lý:**
```
Σ deg⁺(v) = Σ deg⁻(v) = |E|
```

---

**3. Đồ thị có hướng đầy đủ:**

Mỗi cặp đỉnh có 2 cung (cả hai chiều).

Số cung: n(n-1)

---

### 6.1.2. Biểu diễn đồ thị

**A. MA TRẬN KỀ (Adjacency Matrix)**

**Định nghĩa:**

Cho đồ thị G = (V, E) với V = {v₁, v₂, ..., vₙ}

Ma trận kề A = [aᵢⱼ]ₙₓₙ:
```
aᵢⱼ = số cạnh (cung) nối vᵢ và vⱼ
```

**Đồ thị vô hướng:** A đối xứng (aᵢⱼ = aⱼᵢ)

**Đồ thị có hướng:** A không nhất thiết đối xứng

---

**Ví dụ 1: Đồ thị vô hướng**

```
    1 ---- 2
     \    /
      \  /
       3
```

E = {{1,2}, {1,3}, {2,3}}

Ma trận kề:
```
    1  2  3
1 [ 0  1  1 ]
2 [ 1  0  1 ]
3 [ 1  1  0 ]
```

---

**Ví dụ 2: Đồ thị có hướng**

```
1 → 2
↓   ↑
3 → 4
```

E = {(1,2), (1,3), (3,4), (4,2)}

Ma trận kề:
```
    1  2  3  4
1 [ 0  1  1  0 ]
2 [ 0  0  0  0 ]
3 [ 0  0  0  1 ]
4 [ 0  1  0  0 ]
```

---

**Tính chất:**

1. **Bậc đỉnh (vô hướng):**
   ```
   deg(vᵢ) = Σⱼ aᵢⱼ
   ```

2. **Bậc đỉnh (có hướng):**
   ```
   deg⁺(vᵢ) = Σⱼ aᵢⱼ  (tổng hàng i)
   deg⁻(vᵢ) = Σⱼ aⱼᵢ  (tổng cột i)
   ```

3. **Số đường đi độ dài k:**

   Phần tử (i, j) của A^k là số đường đi độ dài k từ vᵢ đến vⱼ.

---

**B. DANH SÁCH KỀ (Adjacency List)**

**Định nghĩa:**

Với mỗi đỉnh v, lưu danh sách các đỉnh kề với v.

---

**Ví dụ: Đồ thị vô hướng**

```
    1 ---- 2
     \    /
      \  /
       3 ---- 4
```

Danh sách kề:
```
1: [2, 3]
2: [1, 3]
3: [1, 2, 4]
4: [3]
```

---

**Ví dụ: Đồ thị có hướng**

```
1 → 2
↓   ↑
3 → 4
```

Danh sách kề:
```
1: [2, 3]
2: []
3: [4]
4: [2]
```

---

**So sánh:**

| Đặc điểm | Ma trận kề | Danh sách kề |
|----------|------------|--------------|
| Bộ nhớ | O(V²) | O(V + E) |
| Kiểm tra cạnh (u,v) | O(1) | O(deg(u)) |
| Liệt kê đỉnh kề | O(V) | O(deg(u)) |
| Thêm đỉnh | O(V²) | O(1) |
| Thêm cạnh | O(1) | O(1) |

**Kết luận:**
- Đồ thị dày (dense): Ma trận kề
- Đồ thị thưa (sparse): Danh sách kề

---

**C. MA TRẬN LIÊN THUỘC (Incidence Matrix)**

**Định nghĩa:**

Ma trận M = [mᵢⱼ]ₙₓₘ với n đỉnh, m cạnh:
```
mᵢⱼ = 1 nếu đỉnh i liên thuộc với cạnh j
mᵢⱼ = 0 nếu không
```

**Đồ thị có hướng:**
```
mᵢⱼ = -1 nếu cung j đi ra từ đỉnh i
mᵢⱼ = 1 nếu cung j đi vào đỉnh i
mᵢⱼ = 0 nếu không liên quan
```

---

### 6.1.3. Một số đồ thị đặc biệt

**1. Đồ thị đầy đủ (Complete graph) Kₙ:**
- n đỉnh
- Mỗi cặp đỉnh có cạnh nối
- |E| = n(n-1)/2

---

**2. Đồ thị vòng (Cycle) Cₙ:**
- n đỉnh: v₁, v₂, ..., vₙ
- n cạnh: {v₁,v₂}, {v₂,v₃}, ..., {vₙ,v₁}

```
C₄:  1 ---- 2
     |      |
     4 ---- 3
```

---

**3. Đồ thị bánh xe (Wheel) Wₙ:**
- Cₙ cộng thêm 1 đỉnh trung tâm nối với mọi đỉnh khác
- n+1 đỉnh, 2n cạnh

```
W₄:    1
      /|\
     / | \
    4--5--2
     \ | /
      \|/
       3
```

---

**4. Đồ thị lưỡng phân (Bipartite graph):**

**Định nghĩa:** V có thể phân thành 2 tập V₁ và V₂ sao cho mọi cạnh đều nối đỉnh thuộc V₁ với đỉnh thuộc V₂.

**Ví dụ:**
```
V₁ = {1, 2}
V₂ = {3, 4, 5}

1 --- 3
 \   / \
  \ /   \
   X     5
  / \   /
 /   \ /
2 --- 4
```

**Định lý:** Đồ thị là lưỡng phân ⟺ Không chứa vòng lẻ

---

**5. Đồ thị lưỡng phân đầy đủ Kₘ,ₙ:**
- V₁ có m đỉnh
- V₂ có n đỉnh
- Mọi đỉnh trong V₁ nối với mọi đỉnh trong V₂
- |E| = m × n

**Ví dụ:** K₃,₃

```
1 --- 4
|\ /||
| X |
|/ \|
2 --- 5
|\ /||
| X |
|/ \|
3 --- 6
```

---

**6. Đồ thị đường (Path) Pₙ:**
- n đỉnh
- n-1 cạnh: {v₁,v₂}, {v₂,v₃}, ..., {vₙ₋₁,vₙ}

```
P₅: 1 --- 2 --- 3 --- 4 --- 5
```

---

**7. Đồ thị chính quy (Regular graph):**

Mọi đỉnh có cùng bậc k.

**Ví dụ:**
- Cₙ: 2-regular
- Kₙ: (n-1)-regular

---

**8. Đồ thị Petersen:**

Đồ thị đặc biệt 10 đỉnh, 15 cạnh, 3-regular.

```
      1
     / \
   10   2
   |\ /|
   | 6 |
   |/ \|
   9   3
    \ /
     8---7---4
         |
         5
```

(Vẽ đơn giản hóa - thực tế phức tạp hơn)

---

**9. Đồ thị khối (Hypercube) Qₙ:**

- 2ⁿ đỉnh (chuỗi bit độ dài n)
- Hai đỉnh kề nhau nếu khác nhau đúng 1 bit
- n-regular

**Ví dụ:** Q₃

```
    000 ---- 001
    /|       /|
  010----- 011|
   | |      | |
   |100 ----|-101
   |/       |/
  110 ---- 111
```

---

## 6.2. ĐỒ THỊ PHẲNG VÀ KHÔNG PHẲNG

### 6.2.1. Đồ thị thành phần và đồ thị con

**A. ĐƯỜNG ĐI VÀ CHU TRÌNH**

**Đường đi (Path):**

Dãy đỉnh v₀, v₁, ..., vₙ sao cho {vᵢ, vᵢ₊₁} ∈ E với mọi i.

**Độ dài đường đi:** Số cạnh trong đường đi (n)

**Đường đi đơn (Simple path):** Không có đỉnh lặp lại

---

**Chu trình (Cycle):**

Đường đi có v₀ = vₙ (đầu = cuối)

**Chu trình đơn:** Không có đỉnh lặp (trừ đầu = cuối)

---

**Ví dụ:**

```
    1 ---- 2
    |      |
    4 ---- 3
```

- Đường đi: 1-2-3-4
- Chu trình: 1-2-3-4-1

---

**B. TÍNH LIÊN THÔNG**

**Đồ thị liên thông (Connected graph):**

Với mọi cặp đỉnh u, v, tồn tại đường đi từ u đến v.

---

**Thành phần liên thông (Connected component):**

Đồ thị con liên thông cực đại.

**Ví dụ:**

```
G:  1---2    5---6
    |   |    |
    3---4    7

Có 2 thành phần:
- {1, 2, 3, 4}
- {5, 6, 7}
```

---

**Đỉnh cắt (Cut vertex):**

Đỉnh mà khi loại bỏ làm tăng số thành phần liên thông.

**Cầu (Bridge):**

Cạnh mà khi loại bỏ làm tăng số thành phần liên thông.

---

**Tính liên thông mạnh (Strongly connected) - Đồ thị có hướng:**

Với mọi u, v, tồn tại đường đi có hướng từ u đến v VÀ từ v đến u.

**Tính liên thông yếu (Weakly connected):**

Đồ thị vô hướng tương ứng liên thông.

---

**C. ĐỒ THỊ CON**

**Định nghĩa:**

H = (V', E') là đồ thị con của G = (V, E) nếu:
- V' ⊆ V
- E' ⊆ E

---

**Đồ thị con sinh bởi tập đỉnh S ⊆ V:**

G[S]: Đồ thị con gồm S và mọi cạnh có cả 2 đầu mút trong S.

**Đồ thị con sinh bởi tập cạnh F ⊆ E:**

Đồ thị con gồm F và các đỉnh là đầu mút của cạnh trong F.

---

### 6.2.2. Đồ thị phẳng và đặc tính của đồ thị

**A. ĐỒ THỊ PHẲNG**

**Định nghĩa:**

Đồ thị phẳng (Planar graph) là đồ thị có thể vẽ trên mặt phẳng sao cho các cạnh chỉ giao nhau tại đỉnh.

---

**Ví dụ 1:** K₄ là đồ thị phẳng

```
Vẽ không phẳng:      Vẽ phẳng:
    1---2                1
    |\ /|               /|\
    | X |              / | \
    |/ \|             2--3--4
    3---4
```

---

**Ví dụ 2:** K₅ không phải đồ thị phẳng

**Ví dụ 3:** K₃,₃ không phải đồ thị phẳng

---

**Miền (Region/Face):**

Khi vẽ đồ thị phẳng, mặt phẳng được chia thành các miền.

**Miền ngoài (Outer region):** Miền không bị chặn

**Miền trong (Inner region):** Miền bị chặn

---

**Ví dụ:**

```
    1---2
    |   |
    3---4

4 miền:
- Miền ngoài
- Miền trong (1-2-4-3-1)
- (Nếu có thêm cạnh 1-4)
```

---

**B. CÔNG THỨC EULER**

**Định lý Euler:**

Cho đồ thị phẳng liên thông với:
- V đỉnh
- E cạnh
- F miền

Thì:
```
V - E + F = 2
```

---

**Chứng minh (ý tưởng):**

Quy nạp theo số cạnh:
- Cơ sở: Cây (E = V - 1, F = 1) → V - E + F = V - (V-1) + 1 = 2
- Quy nạp: Thêm cạnh tạo chu trình → Tăng E và F mỗi cái 1 → Không đổi V - E + F

---

**Ví dụ:**

```
K₄: V = 4, E = 6
4 - 6 + F = 2 → F = 4
```

Thật vậy: 1 miền ngoài + 3 miền trong = 4 miền

---

**Hệ quả 1:**

Đồ thị phẳng đơn liên thông với V ≥ 3:
```
E ≤ 3V - 6
```

**Hệ quả 2:**

Đồ thị phẳng đơn liên thông không có tam giác với V ≥ 3:
```
E ≤ 2V - 4
```

---

**C. ĐỊNH LÝ KURATOWSKI**

**Định lý:**

Đồ thị G là phẳng ⟺ G không chứa đồ thị con đồng phôi với K₅ hoặc K₃,₃.

**Đồng phôi (Homeomorphic):** Có thể thu được từ nhau bằng cách thêm/bớt đỉnh bậc 2 trên cạnh.

---

**Ví dụ ứng dụng:**

Chứng minh K₅ không phẳng:
- V = 5, E = 10
- Nếu phẳng: E ≤ 3V - 6 = 3×5 - 6 = 9
- Nhưng E = 10 > 9 → Mâu thuẫn
- → K₅ không phẳng

Chứng minh K₃,₃ không phẳng:
- V = 6, E = 9
- Không có tam giác (lưỡng phân)
- Nếu phẳng: E ≤ 2V - 4 = 2×6 - 4 = 8
- Nhưng E = 9 > 8 → Mâu thuẫn
- → K₃,₃ không phẳng

---

### 6.2.3. Chu trình Euler và chu trình Hamilton

**A. CHU TRÌNH EULER**

**Định nghĩa:**

**Đường đi Euler:** Đường đi qua mỗi cạnh đúng một lần

**Chu trình Euler:** Đường đi Euler có đầu = cuối

**Đồ thị Euler:** Đồ thị có chu trình Euler

---

**Định lý Euler:**

Đồ thị liên thông G có chu trình Euler ⟺ Mọi đỉnh có bậc chẵn.

Đồ thị liên thông G có đường đi Euler (không phải chu trình) ⟺ Có đúng 2 đỉnh bậc lẻ.

---

**Chứng minh (→):**

Nếu có chu trình Euler:
- Mỗi khi đi qua đỉnh v: dùng 2 cạnh (vào và ra)
- → deg(v) chẵn

---

**Thuật toán Fleury tìm chu trình Euler:**

```
1. Bắt đầu từ đỉnh bất kỳ (hoặc đỉnh bậc lẻ nếu tìm đường đi)
2. Đi theo cạnh bất kỳ, ưu tiên cạnh không phải cầu
3. Xóa cạnh vừa đi
4. Lặp lại cho đến khi không còn cạnh
```

---

**Ví dụ:**

```
    1---2
    |   |
    3---4

deg(1) = 2, deg(2) = 2, deg(3) = 2, deg(4) = 2
→ Có chu trình Euler: 1-2-4-3-1
```

---

**Bài toán 7 cầu Königsberg:**

```
       A
      /|\
    1/ | \2
    /  |  \
   B   |3  C
    \  |  /
    4\ | /5
      \|/
       D

Kết nối: A-B (2 cầu), A-C (2 cầu), A-D (1 cầu), B-D (1 cầu), C-D (1 cầu)

deg(A) = 5, deg(B) = 3, deg(C) = 3, deg(D) = 3
→ 4 đỉnh bậc lẻ → Không có đường đi Euler
```

**Kết luận:** Không thể đi qua mỗi cầu đúng một lần.

---

**B. CHU TRÌNH HAMILTON**

**Định nghĩa:**

**Đường đi Hamilton:** Đường đi qua mỗi đỉnh đúng một lần

**Chu trình Hamilton:** Đường đi Hamilton có đầu = cuối

**Đồ thị Hamilton:** Đồ thị có chu trình Hamilton

---

**Lưu ý:** Không có điều kiện đủ đơn giản như Euler!

**Bài toán Hamilton là NP-đầy đủ.**

---

**Điều kiện cần:**

Nếu G có chu trình Hamilton H, và S ⊆ V, thì H - S có nhiều nhất |S| thành phần.

---

**Điều kiện đủ (Định lý Dirac):**

Nếu G là đồ thị đơn n đỉnh (n ≥ 3) và deg(v) ≥ n/2 với mọi v, thì G có chu trình Hamilton.

---

**Điều kiện đủ (Định lý Ore):**

Nếu G là đồ thị đơn n đỉnh (n ≥ 3) và deg(u) + deg(v) ≥ n với mọi cặp u, v không kề nhau, thì G có chu trình Hamilton.

---

**Ví dụ:**

```
Đồ thị K₅:
Mọi đỉnh có bậc 4 = 5-1
→ Có chu trình Hamilton: 1-2-3-4-5-1
```

---

**Bài toán người giao hàng (Traveling Salesman Problem - TSP):**

Cho đồ thị có trọng số, tìm chu trình Hamilton có tổng trọng số nhỏ nhất.

**Ứng dụng:**
- Logistics
- Thiết kế mạch
- Lập lịch

**Độ phức tạp:** NP-hard

---

**So sánh Euler và Hamilton:**

| Euler | Hamilton |
|-------|----------|
| Qua mỗi **cạnh** đúng 1 lần | Qua mỗi **đỉnh** đúng 1 lần |
| Có điều kiện đủ đơn giản | Không có điều kiện đủ đơn giản |
| Giải được trong O(E) | NP-đầy đủ |

---

## 6.3. CÂY VÀ RỪNG

### 6.3.1. Khái niệm cơ bản

**A. ĐỊNH NGHĨA CÂY**

**Cây (Tree):**

Đồ thị vô hướng liên thông không có chu trình.

---

**Rừng (Forest):**

Đồ thị không có chu trình (có thể không liên thông).

Mỗi thành phần liên thông là một cây.

---

**Ví dụ cây:**

```
      1
     / \
    2   3
   / \
  4   5
```

---

**Các định nghĩa tương đương:**

Cho G = (V, E) với |V| = n. Các mệnh đề sau tương đương:

1. G là cây
2. G liên thông và |E| = n - 1
3. G không có chu trình và |E| = n - 1
4. G liên thông và mọi cạnh là cầu
5. Với mọi u, v ∈ V, có duy nhất một đường đi từ u đến v
6. G không có chu trình, nhưng thêm bất kỳ cạnh nào cũng tạo thành đúng một chu trình

---

**Tính chất cây:**

1. Cây n đỉnh có n-1 cạnh
2. Bất kỳ hai đỉnh nào cũng có đúng một đường đi nối chúng
3. Mọi cạnh đều là cầu
4. Loại bỏ bất kỳ cạnh nào cũng làm đồ thị không liên thông
5. Thêm bất kỳ cạnh nào cũng tạo đúng một chu trình

---

**B. CÂY CÓ GỐC**

**Cây có gốc (Rooted tree):**

Cây có một đỉnh được chỉ định là gốc.

---

**Các khái niệm:**

**1. Mức (Level):**
- Gốc: mức 0
- Con của gốc: mức 1
- Con của mức i: mức i+1

**2. Chiều cao (Height):**
Mức lớn nhất trong cây.

**3. Nút cha - con:**
Nếu (u, v) là cạnh và u gần gốc hơn, thì u là cha của v, v là con của u.

**4. Nút anh em (Siblings):**
Các nút có cùng cha.

**5. Nút tổ tiên (Ancestor):**
Các nút trên đường đi từ nút đó lên gốc.

**6. Nút hậu duệ (Descendant):**
Các nút trong cây con gốc tại nút đó.

**7. Nút lá (Leaf):**
Nút không có con.

**8. Nút trong (Internal node):**
Nút không phải lá.

---

**Ví dụ:**

```
        1 (gốc)
       / \
      2   3
     / \   \
    4   5   6

Mức 0: {1}
Mức 1: {2, 3}
Mức 2: {4, 5, 6}
Chiều cao: 2

Cha của 4: 2
Con của 2: {4, 5}
Anh em của 4: {5}
Tổ tiên của 4: {2, 1}
Hậu duệ của 2: {4, 5}
Lá: {4, 5, 6}
Nút trong: {1, 2, 3}
```

---

**C. CÂY NHỊ PHÂN**

**Cây nhị phân (Binary tree):**

Cây có gốc, mỗi nút có nhiều nhất 2 con (con trái và con phải).

---

**Cây nhị phân đầy đủ (Full binary tree):**

Mỗi nút trong có đúng 2 con.

**Cây nhị phân hoàn chỉnh (Complete binary tree):**

Mọi mức đều đầy, trừ mức cuối có thể thiếu ở bên phải.

**Cây nhị phân hoàn hảo (Perfect binary tree):**

Mọi mức đều đầy (2^(h+1) - 1 nút với chiều cao h).

---

**Số nút:**

Cây nhị phân chiều cao h:
- Tối thiểu: h + 1 nút
- Tối đa: 2^(h+1) - 1 nút

---

**Duyệt cây nhị phân:**

**1. Tiền thứ tự (Preorder):**
Gốc → Trái → Phải

**2. Trung thứ tự (Inorder):**
Trái → Gốc → Phải

**3. Hậu thứ tự (Postorder):**
Trái → Phải → Gốc

**Ví dụ:**

```
      1
     / \
    2   3
   / \
  4   5

Preorder: 1, 2, 4, 5, 3
Inorder: 4, 2, 5, 1, 3
Postorder: 4, 5, 2, 3, 1
```

---

**D. CÂY KHUNG**

**Cây khung (Spanning tree):**

Cây con của G chứa tất cả các đỉnh của G.

---

**Tính chất:**

1. Đồ thị G liên thông ⟺ G có cây khung
2. Cây khung của G có n-1 cạnh (n = |V|)
3. Một đồ thị có thể có nhiều cây khung

---

**Thuật toán tìm cây khung (DFS/BFS):**

**DFS (Depth-First Search):**
```
1. Bắt đầu từ đỉnh v
2. Đánh dấu v
3. Với mỗi đỉnh u kề với v chưa được đánh dấu:
   - Thêm cạnh (v, u) vào cây khung
   - Đệ quy DFS(u)
```

**BFS (Breadth-First Search):**
```
1. Bắt đầu từ đỉnh v, cho v vào hàng đợi
2. Trong khi hàng đợi không rỗng:
   - Lấy u ra khỏi hàng đợi
   - Với mỗi đỉnh w kề với u chưa được đánh dấu:
     - Thêm cạnh (u, w) vào cây khung
     - Đánh dấu w, cho w vào hàng đợi
```

---

### 6.3.2. Mã hóa Prufer

**Mã Prufer:**

Phương pháp biểu diễn cây có nhãn bằng dãy số.

**Định lý Cayley:** Có n^(n-2) cây khác nhau trên n đỉnh có nhãn.

---

**Chuyển cây → Mã Prufer:**

```
1. Tìm lá có nhãn nhỏ nhất
2. Ghi nhãn của đỉnh kề với nó
3. Xóa lá đó
4. Lặp lại cho đến khi còn 2 đỉnh
```

**Ví dụ:**

```
Cây: 1---2---3
         |
         4

Bước 1: Lá nhỏ nhất = 1, kề với 2 → Ghi 2, xóa 1
Bước 2: Lá nhỏ nhất = 3, kề với 2 → Ghi 2, xóa 3
Bước 3: Lá nhỏ nhất = 4, kề với 2 → Ghi 2, xóa 4
Còn 2 đỉnh → Dừng

Mã Prufer: [2, 2, 2]
```

---

**Chuyển mã Prufer → Cây:**

```
1. Tập lá = tất cả đỉnh không xuất hiện trong mã
2. Lấy phần tử đầu tiên a trong mã, lá nhỏ nhất b
3. Nối a và b, xóa b khỏi tập lá, xóa a khỏi mã
4. Nếu a không còn trong mã, thêm a vào tập lá
5. Lặp lại cho đến khi mã rỗng
6. Nối 2 đỉnh còn lại
```

---

### 6.3.3. Cây khung tối thiểu

**Bài toán:**

Cho đồ thị có trọng số G = (V, E, w), tìm cây khung có tổng trọng số nhỏ nhất.

**Ứng dụng:**
- Thiết kế mạng
- Hệ thống đường ống
- Mạch điện

---

**A. THUẬT TOÁN KRUSKAL**

**Ý tưởng:** Chọn cạnh nhỏ nhất chưa tạo chu trình.

**Thuật toán:**
```
1. Sắp xếp các cạnh theo trọng số tăng dần
2. T = ∅ (cây khung)
3. Với mỗi cạnh e theo thứ tự:
   - Nếu T ∪ {e} không tạo chu trình:
     - T = T ∪ {e}
4. Trả về T
```

**Độ phức tạp:** O(E log E)

---

**Ví dụ:**

```
Đồ thị:
    1
   /|\
  1 2 3
 /  |  \
2---3---4
 \  |  /
  4 5 6

Cạnh:
(1,2):1
(2,3):2
(1,3):3
(2,4):4
(3,4):5
(1,4):6

Bước 1: Chọn (1,2): 1
Bước 2: Chọn (2,3): 2
Bước 3: Bỏ qua (1,3): 3 (tạo chu trình với 1-2-3)
Bước 4: Chọn (2,4): 4

Tổng: 1 + 2 + 4 = 7
```

---

**B. THUẬT TOÁN PRIM**

**Ý tưởng:** Mở rộng cây từ một đỉnh bằng cạnh nhỏ nhất nối cây với đỉnh ngoài cây.

**Thuật toán:**
```
1. Chọn đỉnh bất kỳ làm gốc, T = {gốc}
2. Trong khi T chưa chứa tất cả đỉnh:
   - Tìm cạnh (u, v) có trọng số nhỏ nhất với u ∈ T, v ∉ T
   - T = T ∪ {v}, thêm cạnh (u, v)
3. Trả về T
```

**Độ phức tạp:** O(E log V) với heap

---

**Ví dụ:**

```
Đồ thị:
    1--1--2
    |     |
    2     3
    |     |
    3--4--4

Bước 1: Bắt đầu từ đỉnh 1
Bước 2: Chọn cạnh (1,2): 1 (nhỏ nhất từ 1)
Bước 3: Chọn cạnh (1,3): 2 (nhỏ nhất từ {1,2})
Bước 4: Chọn cạnh (2,4): 3 (nhỏ nhất từ {1,2,3})

Tổng: 1 + 2 + 3 = 6
```

---

**So sánh Kruskal và Prim:**

| Kruskal | Prim |
|---------|------|
| Dựa trên cạnh | Dựa trên đỉnh |
| Sắp xếp cạnh trước | Không cần sắp xếp |
| Tốt cho đồ thị thưa | Tốt cho đồ thị dày |
| Dùng Union-Find | Dùng Heap |

---

## 6.4. CÁC BÀI TOÁN

### 6.4.1. Bài toán tìm đường đi

**A. THUẬT TOÁN DIJKSTRA (Đường đi ngắn nhất)**

**Bài toán:** Tìm đường đi ngắn nhất từ một đỉnh nguồn đến các đỉnh khác.

**Điều kiện:** Trọng số không âm.

---

**Thuật toán:**

```
1. Khởi tạo:
   - d[s] = 0 (khoảng cách từ nguồn s đến chính nó)
   - d[v] = ∞ với v ≠ s
   - S = ∅ (tập đỉnh đã xét)

2. Trong khi S ≠ V:
   - Chọn u ∉ S có d[u] nhỏ nhất
   - S = S ∪ {u}
   - Với mỗi v kề với u:
     - Nếu d[v] > d[u] + w(u,v):
       - d[v] = d[u] + w(u,v)
       - prev[v] = u

3. Trả về d, prev
```

**Độ phức tạp:** O(V²) hoặc O((V+E) log V) với heap

---

**Ví dụ:**

```
Đồ thị:
   s --2-- 1
   |       |
   4       1
   |       |
   2 --1-- 3

Tìm đường đi ngắn nhất từ s:

Khởi tạo: d[s]=0, d[1]=∞, d[2]=∞, d[3]=∞
Bước 1: Chọn s, cập nhật d[1]=2, d[2]=4
Bước 2: Chọn 1, cập nhật d[3]=3
Bước 3: Chọn 3, cập nhật d[2]=4 (không đổi)
Bước 4: Chọn 2

Kết quả:
- s → 1: 2 (s-1)
- s → 2: 4 (s-2)
- s → 3: 3 (s-1-3)
```

---

**B. THUẬT TOÁN BELLMAN-FORD**

**Đặc điểm:** Chấp nhận trọng số âm, phát hiện chu trình âm.

**Thuật toán:**

```
1. Khởi tạo: d[s] = 0, d[v] = ∞ với v ≠ s

2. Lặp V-1 lần:
   - Với mỗi cạnh (u, v):
     - Nếu d[v] > d[u] + w(u,v):
       - d[v] = d[u] + w(u,v)

3. Kiểm tra chu trình âm:
   - Với mỗi cạnh (u, v):
     - Nếu d[v] > d[u] + w(u,v):
       - Có chu trình âm!

4. Trả về d
```

**Độ phức tạp:** O(VE)

---

**C. THUẬT TOÁN FLOYD-WARSHALL (Mọi cặp đỉnh)**

**Bài toán:** Tìm đường đi ngắn nhất giữa mọi cặp đỉnh.

**Thuật toán:**

```
1. Khởi tạo:
   - d[i][j] = w(i,j) nếu có cạnh
   - d[i][j] = ∞ nếu không có
   - d[i][i] = 0

2. Với k = 1 đến n:
   - Với i = 1 đến n:
     - Với j = 1 đến n:
       - d[i][j] = min(d[i][j], d[i][k] + d[k][j])

3. Trả về d
```

**Độ phức tạp:** O(V³)

---

### 6.4.2. Bài toán tô màu

**Tô màu đồ thị (Graph Coloring):**

Gán màu cho các đỉnh sao cho hai đỉnh kề nhau có màu khác nhau.

---

**Số màu sắc (Chromatic number):**

χ(G) = Số màu tối thiểu cần để tô G.

---

**Tính chất:**

1. χ(Kₙ) = n
2. χ(Cₙ) = 2 nếu n chẵn, 3 nếu n lẻ
3. χ(G) ≤ Δ(G) + 1 (Δ = bậc lớn nhất)
4. Đồ thị lưỡng phân: χ(G) = 2

---

**Định lý 4 màu:**

Mọi đồ thị phẳng đều có thể tô bằng 4 màu.

*Chứng minh phức tạp, dùng máy tính.*

---

**Thuật toán tham lam (Greedy Coloring):**

```
1. Với mỗi đỉnh v theo thứ tự:
   - Chọn màu nhỏ nhất chưa được dùng bởi đỉnh kề với v
2. Trả về số màu đã dùng
```

**Lưu ý:** Kết quả phụ thuộc thứ tự đỉnh, không đảm bảo tối ưu.

---

**Ứng dụng:**

1. **Lập lịch:** Các công việc xung đột là đỉnh kề, màu là thời gian.
2. **Phân bổ thanh ghi:** Biến xung đột là đỉnh kề, màu là thanh ghi.
3. **Tô màu bản đồ:** Các nước kề nhau có màu khác.

---

**Ví dụ:**

```
Đồ thị:
    1---2
    |\ /|
    | X |
    |/ \|
    3---4

Tô màu:
- Đỉnh 1: Màu 1
- Đỉnh 2: Màu 2 (kề 1)
- Đỉnh 3: Màu 2 (kề 1, không kề 2)
- Đỉnh 4: Màu 1 (kề 2, 3)

Nhưng 1 kề 4 → Sai!

Sửa lại:
- Đỉnh 1: Màu 1
- Đỉnh 2: Màu 2
- Đỉnh 3: Màu 2
- Đỉnh 4: Màu 3

χ(G) = 3
```

---

## KẾT LUẬN CHƯƠNG 6

**Nội dung đã học:**

1. **Đồ thị cơ bản:**
   - Vô hướng, có hướng
   - Biểu diễn: Ma trận, danh sách
   - Các loại đồ thị đặc biệt

2. **Đồ thị phẳng:**
   - Công thức Euler: V - E + F = 2
   - K₅, K₃,₃ không phẳng

3. **Chu trình:**
   - Euler: Qua mỗi cạnh 1 lần
   - Hamilton: Qua mỗi đỉnh 1 lần

4. **Cây:**
   - Cây khung
   - Cây khung tối thiểu: Kruskal, Prim
   - Mã Prufer

5. **Thuật toán:**
   - Đường đi ngắn nhất: Dijkstra, Bellman-Ford, Floyd-Warshall
   - Tô màu đồ thị

---

## BÀI TẬP ÔN TẬP CHƯƠNG 6

**Bài 1:** Cho đồ thị G = (V, E) với V = {1,2,3,4,5}, E = {{1,2}, {1,3}, {2,3}, {2,4}, {3,5}, {4,5}}
a) Vẽ đồ thị
b) Viết ma trận kề
c) Tìm bậc của mỗi đỉnh
d) G có chu trình Euler không? Hamilton không?

**Bài 2:** Chứng minh trong một buổi tiệc có ít nhất 2 người có cùng số bạn bè (dùng lý thuyết đồ thị).

**Bài 3:** Chứng minh đồ thị sau không phẳng:
- K₅
- K₃,₃

**Bài 4:** Tìm cây khung tối thiểu bằng Kruskal và Prim:

```
    1--2--2
    |     |
    3     4
    |     |
    3--5--4
```

**Bài 5:** Tìm đường đi ngắn nhất từ đỉnh 1 đến các đỉnh khác bằng Dijkstra:

```
    1--3--2
    |     |
    1     2
    |     |
    3--4--4
```

**Bài 6:** Tìm số màu sắc χ(G) của các đồ thị:
a) K₅
b) C₆
c) K₃,₃

**Bài 7:** Chứng minh rằng nếu G là đồ thị đơn có n đỉnh và nhiều hơn (n-1)(n-2)/2 cạnh, thì G là đồ thị Hamilton.

**Bài 8:** Tìm mã Prufer của cây:
```
   1---2---3
       |
       4
```

**Bài 9:** Áp dụng BFS và DFS để tìm cây khung của đồ thị:
```
    1---2
    |\ /|
    | X |
    |/ \|
    3---4
```

**Bài 10:** Chứng minh rằng mọi cây với ít nhất 2 đỉnh đều có ít nhất 2 lá.

---

# HẾT CHƯƠNG 6 VÀ TOÀN BỘ MÔN TOÁN TIN HỌC

**Chúc các bạn học tốt!**
