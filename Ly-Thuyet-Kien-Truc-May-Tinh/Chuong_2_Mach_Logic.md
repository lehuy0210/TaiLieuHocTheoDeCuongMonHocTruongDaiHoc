# CHƯƠNG 2: MẠCH LOGIC

## 2.1. GIỚI THIỆU

**Mạch logic** là nền tảng của máy tính số. Tất cả các hoạt động của máy tính đều dựa trên các mạch logic cơ bản.

**Mạch số vs Mạch tương tự:**

| Mạch số (Digital) | Mạch tương tự (Analog) |
|-------------------|------------------------|
| 2 trạng thái: 0, 1 | Vô số giá trị liên tục |
| Chống nhiễu tốt | Dễ bị nhiễu |
| Dễ thiết kế | Phức tạp |
| CPU, bộ nhớ | Khuếch đại âm thanh |

**Mức logic:**
- **Logic 0 (LOW):** 0V - 0.8V
- **Logic 1 (HIGH):** 2V - 5V

## 2.2. ĐẠI SỐ BOOLEAN VÀ CÁC CỔNG LOGIC

### 2.2.1. Đại số Boolean

(Đã trình bày chi tiết ở Chương 5 môn Toán Tin học)

**Tóm tắt:**
- AND (∧): A · B
- OR (∨): A + B
- NOT (¬): A' hoặc Ā

**Định luật quan trọng:**
- De Morgan: (A·B)' = A' + B'
- Phân phối: A·(B+C) = A·B + A·C

### 2.2.2. Các cổng logic

**1. NOT (Inverter):**
```
A ──o── Y = A'

Bảng chân lý:
A | Y
--|--
0 | 1
1 | 0
```

**2. AND:**
```
A ──┐
    ├─── Y = A·B
B ──┘

Bảng chân lý:
A B | Y
----|--
0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1
```

**3. OR:**
```
A ──┐
    ├─── Y = A+B
B ──┘

Bảng chân lý:
A B | Y
----|--
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 1
```

**4. NAND:**
```
A ──┐
    ├o── Y = (A·B)'
B ──┘

Bảng chân lý:
A B | Y
----|--
0 0 | 1
0 1 | 1
1 0 | 1
1 1 | 0
```

**5. NOR:**
```
A ──┐
    ├o── Y = (A+B)'
B ──┘

Bảng chân lý:
A B | Y
----|--
0 0 | 1
0 1 | 0
1 0 | 0
1 1 | 0
```

**6. XOR (Exclusive OR):**
```
A ──┐
    ├─── Y = A⊕B = A'B + AB'
B ──┘

Bảng chân lý:
A B | Y
----|--
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 0
```

**7. XNOR (Equivalence):**
```
A ──┐
    ├o── Y = (A⊕B)' = AB + A'B'
B ──┘

Bảng chân lý:
A B | Y
----|--
0 0 | 1
0 1 | 0
1 0 | 0
1 1 | 1
```

---

## 2.3. MẠCH TỔ HỢP

**Mạch tổ hợp (Combinational Circuit):** Đầu ra chỉ phụ thuộc vào đầu vào hiện tại, không có bộ nhớ.

### 2.3.1. Mạch cộng

**A. Half Adder (Bán cộng):**

Cộng 2 bit A, B → Tổng S (Sum) và nhớ C (Carry)

**Bảng chân lý:**
```
A B | S C
----|----
0 0 | 0 0
0 1 | 1 0
1 0 | 1 0
1 1 | 0 1
```

**Công thức:**
- S = A ⊕ B
- C = A · B

**Sơ đồ:**
```
A ──┬─────┐
    │     └─XOR── S
    └─AND─┐
          │
B ──┬─────┤
    │     └────── C
    └─────┘
```

**B. Full Adder (Toàn cộng):**

Cộng 3 bit: A, B, Cin → S, Cout

**Bảng chân lý:**
```
A B Cin | S Cout
--------|-------
0 0  0  | 0  0
0 0  1  | 1  0
0 1  0  | 1  0
0 1  1  | 0  1
1 0  0  | 1  0
1 0  1  | 0  1
1 1  0  | 0  1
1 1  1  | 1  1
```

**Công thức:**
- S = A ⊕ B ⊕ Cin
- Cout = AB + Cin(A⊕B) = AB + ACin + BCin

**Sơ đồ (dùng 2 Half Adder):**
```
      ┌─────────┐
A ────┤         ├──── S1
      │  Half   │
B ────┤ Adder 1 ├──── C1
      └─────────┘
           │
         S1│    ┌─────────┐
           └────┤         ├──── S
                │  Half   │
Cin ────────────┤ Adder 2 ├──── C2
                └─────────┘
                     │
              C1 ───┴─OR─── Cout
              C2 ────┘
```

**C. Ripple Carry Adder (Bộ cộng 4 bit):**

Ghép nối 4 Full Adder:

```
A3 B3    A2 B2    A1 B1    A0 B0
  │ │      │ │      │ │      │ │
  ▼ ▼      ▼ ▼      ▼ ▼      ▼ ▼
┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
│ FA  │◄─│ FA  │◄─│ FA  │◄─│ FA  │◄─ 0
└──┬──┘  └──┬──┘  └──┬──┘  └──┬──┘
   │        │        │        │
  S3       S2       S1       S0

Cout ◄────┘
```

**Nhược điểm:** Chậm (carry ripple through)

**Cải tiến:**
- **Carry Look-Ahead Adder:** Tính carry song song
- **Carry Select Adder**
- **Carry Save Adder**

### 2.3.2. Mạch trừ

**A. Half Subtractor:**

Trừ 2 bit A - B → D (Difference), Borrow

**Bảng chân lý:**
```
A B | D Borrow
----|----------
0 0 | 0   0
0 1 | 1   1
1 0 | 1   0
1 1 | 0   0
```

**Công thức:**
- D = A ⊕ B
- Borrow = A'·B

**B. Full Subtractor:**

A - B - Bin → D, Bout

**Công thức:**
- D = A ⊕ B ⊕ Bin
- Bout = A'B + A'Bin + BBin

**C. Phương pháp bù 2 (Two's Complement):**

Để tính A - B, ta tính A + (-B):
- -B = (B' + 1) (Bù 2 của B)

**Ví dụ: 5 - 3 (4 bit)**
```
A = 5  = 0101
B = 3  = 0011
-B: Bù 1 của B = 1100
    Cộng 1      = 1101

A + (-B):
  0101
+ 1101
-------
 10010

Bỏ bit tràn → 0010 = 2 ✓
```

**Ưu điểm:** Dùng chung mạch cộng cho cả trừ!

---

## 2.4. MẠCH TUẦN TỰ

**Mạch tuần tự (Sequential Circuit):** Đầu ra phụ thuộc vào đầu vào hiện tại VÀ trạng thái trước đó (có bộ nhớ).

**A. SR Latch (Set-Reset):**

**Dùng NOR:**
```
S ──┐
    └─NOR──┐
    ┌──────┘
    │
Q ◄─┤
    │
    └─NOR──┐
    ┌──────┘
R ──┘

Q' ◄────────┘
```

**Bảng chân lý:**
```
S R | Q  Q' | Trạng thái
----|-------|----------
0 0 | Q  Q' | Giữ nguyên
0 1 | 0  1  | Reset
1 0 | 1  0  | Set
1 1 | X  X  | Không xác định (Cấm)
```

**B. D Latch (Data Latch):**

Có thêm Enable (E):
```
D ──┬─────┐
    │     └─AND──S
    │          ┌──┐
E ──┼─────────┤  │
    │          │SR│──── Q
    │     ┌────┤  │
    └─NOT─┤    └──┘──── Q'
          └─AND──R
```

**Hoạt động:**
- E = 0: Giữ nguyên Q
- E = 1: Q = D

**C. D Flip-Flop:**

**Khác Latch:** Kích hoạt theo cạnh xung Clock (edge-triggered), không phải mức (level-triggered).

**Ký hiệu:**
```
     ┌─────┐
D ───┤ D   ├──── Q
     │     │
CLK ─┤>CLK ├──── Q'
     └─────┘

> : Cạnh lên (positive edge)
```

**Loại:**
- **Positive edge-triggered:** Kích hoạt khi CLK: 0→1
- **Negative edge-triggered:** Kích hoạt khi CLK: 1→0

**Timing diagram:**
```
CLK  ──┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐
       └─┘ └─┘ └─┘ └─┘ └─

D    ───────┐   ┌─────────
            └───┘

Q    ───────┐   ┌─────────
      (delay)└───┘
```

**D. JK Flip-Flop:**

**Bảng chân lý:**
```
J K | Q(t+1) | Trạng thái
----|--------|----------
0 0 |  Q(t)  | Giữ nguyên
0 1 |   0    | Reset
1 0 |   1    | Set
1 1 | Q'(t)  | Toggle
```

**E. T Flip-Flop (Toggle):**

**Bảng chân lý:**
```
T | Q(t+1)
--|--------
0 |  Q(t)
1 | Q'(t)  ← Đảo
```

**Ứng dụng:** Bộ đếm

---

## 2.5. THANH GHI

**Thanh ghi (Register):** Nhóm các flip-flop để lưu trữ nhiều bit.

### 2.5.1. Thanh ghi song song

**Parallel Register:** Nạp/đọc tất cả bit cùng lúc.

**Sơ đồ 4-bit:**
```
D3 ──┐     D2 ──┐     D1 ──┐     D0 ──┐
     ▼         ▼         ▼         ▼
   ┌───┐     ┌───┐     ┌───┐     ┌───┐
   │ D │     │ D │     │ D │     │ D │
   │   │     │   │     │   │     │   │
CLK┤>  │ CLK┤>  │ CLK┤>  │ CLK┤>  │
   └─┬─┘     └─┬─┘     └─┬─┘     └─┬─┘
     │         │         │         │
     ▼         ▼         ▼         ▼
    Q3        Q2        Q1        Q0
```

**Clock chung cho tất cả FF.**

### 2.5.2. Thanh ghi dịch

**Shift Register:** Dịch bit sang trái/phải mỗi xung clock.

**A. SISO (Serial In Serial Out):**

```
Din ──┐   ┌───┐   ┌───┐   ┌───┐
      ▼   │ D │   │ D │   │ D │
    ┌───┐ │   ├──►│   ├──►│   ├──► Dout
    │ D │ │   │   │   │   │   │
    │   │ └───┘   └───┘   └───┘
CLK┤>  │
    └───┘
```

**Ví dụ:**
```
Nạp 1011 (từ trái sang phải):

CLK 0: [ ][ ][ ][ ]  Din=1
CLK 1: [1][ ][ ][ ]  Din=0
CLK 2: [0][1][ ][ ]  Din=1
CLK 3: [1][0][1][ ]  Din=1
CLK 4: [1][1][0][1]  Dout=1
CLK 5: [ ][1][1][0]  Dout=0
...
```

**B. SIPO (Serial In Parallel Out):**

Nạp tuần tự, đọc song song.

```
Din ──► FF3 ──► FF2 ──► FF1 ──► FF0
         │       │       │       │
         ▼       ▼       ▼       ▼
        Q3      Q2      Q1      Q0
```

**C. PISO (Parallel In Serial Out):**

Nạp song song, đọc tuần tự.

**D. PIPO (Parallel In Parallel Out):**

= Thanh ghi song song (đã nói ở trên).

**Ứng dụng Shift Register:**

**1. Chuyển đổi Serial ↔ Parallel:**
- UART communication
- SPI, I2C

**2. Delay Line:**
- Tạo độ trễ cho tín hiệu

**3. Nhân/chia 2:**
- Shift left 1 bit = ×2
- Shift right 1 bit = ÷2

**4. Checksum, CRC:**
- Tính toán tuần tự

**Ví dụ: Nhân với 2 bằng shift left**
```
Số ban đầu: 5 = 0101

Shift left 1 bit:
    0101
<<  1
---------
   1010 = 10 = 5×2 ✓
```

---

## KẾT LUẬN CHƯƠNG 2

**Tóm tắt:**

1. **Đại số Boolean:** Nền tảng logic số
2. **Cổng logic:** AND, OR, NOT, NAND, NOR, XOR
3. **Mạch tổ hợp:**
   - Half/Full Adder
   - Half/Full Subtractor
   - Bộ cộng nhiều bit
4. **Mạch tuần tự:**
   - Latch, Flip-Flop
   - Có bộ nhớ (trạng thái)
5. **Thanh ghi:**
   - Parallel Register
   - Shift Register (SISO, SIPO, PISO, PIPO)

**Kiến thức cần nắm:**
- Thiết kế mạch logic từ bảng chân lý
- Hiểu sự khác biệt mạch tổ hợp và tuần tự
- Cách hoạt động của flip-flop
- Ứng dụng của thanh ghi dịch

---

## BÀI TẬP ÔN TẬP CHƯƠNG 2

**Bài 1:** Vẽ sơ đồ và viết bảng chân lý của Full Adder. Chứng minh công thức Sum và Carry.

**Bài 2:** Thiết kế mạch cộng 8 bit sử dụng Full Adder.

**Bài 3:** Giải thích tại sao có thể dùng mạch cộng để thực hiện phép trừ (phương pháp bù 2).

**Bài 4:** Tính (-7) trong hệ nhị phân 8 bit bằng phương pháp bù 2.

**Bài 5:** Phân biệt Latch và Flip-Flop. Khi nào nên dùng loại nào?

**Bài 6:** Vẽ timing diagram cho D Flip-Flop với đầu vào D và CLK cho trước.

**Bài 7:** Thiết kế bộ đếm 4 bit (0→15) sử dụng T Flip-Flop.

**Bài 8:** Giải thích cách hoạt động của SIPO Shift Register. Cho ví dụ cụ thể.

**Bài 9:** Tại sao XOR gate được gọi là "inequality detector"?

**Bài 10:** Thiết kế mạch so sánh 2 số 4 bit (A, B) cho biết A>B, A=B, hay A<B.
