# CHƯƠNG 3-6: CLOCK, BUS, BỘ XỬ LÝ, BỘ NHỚ VÀ TẬP LỆNH

## CHƯƠNG 3: CLOCK VÀ BUS

### 3.1. GIỚI THIỆU

Chương này tìm hiểu về Clock (xung nhịp) và Bus (bus hệ thống) - hai yếu tố quan trọng quyết định hiệu năng máy tính.

### 3.2. CLOCK VÀ BUS

#### 3.2.1. Khái niệm về Clock

**Clock (Xung nhịp):** Tín hiệu điện tử dao động đều đặn, đồng bộ hóa hoạt động của các thành phần trong máy tính.

**Hình dạng tín hiệu Clock:**
```
      ┌─┐ ┌─┐ ┌─┐ ┌─┐
CLK ──┘ └─┘ └─┘ └─┘ └─

      ◄──► ◄──►
    Chu kỳ (Period)
```

**Các khái niệm:**

**1. Tần số Clock (Clock Frequency):**
- Số chu kỳ trong 1 giây
- Đơn vị: Hz (Hertz)
- Ví dụ: 3.5 GHz = 3,500,000,000 chu kỳ/giây

**2. Chu kỳ Clock (Clock Period):**
- Thời gian 1 chu kỳ
- Period = 1 / Frequency
- Ví dụ: 3.5 GHz → Period = 1/3.5×10⁹ ≈ 0.286 ns

**3. Duty Cycle:**
- Tỷ lệ thời gian HIGH trong 1 chu kỳ
- Thường 50%

**Clock Generator:**
- Crystal Oscillator (Thạch anh)
- PLL (Phase-Locked Loop) để nhân tần số

#### 3.2.2. Tốc độ thực thi lệnh

**CPI (Cycles Per Instruction):** Số chu kỳ clock để thực thi 1 lệnh.

**Công thức tính thời gian:**

```
Thời gian thực thi = Số lệnh × CPI × Chu kỳ Clock

Hoặc:

MIPS = Clock Frequency (MHz) / CPI
```

**Ví dụ:**
```
CPU: 3 GHz, CPI = 2
Chương trình: 1 triệu lệnh

Thời gian = 10⁶ × 2 × (1/3×10⁹)
         = 0.67 ms
```

**IPC (Instructions Per Cycle):**
- IPC = 1/CPI
- CPU hiện đại: IPC > 1 (thực thi song song)

#### 3.2.3. Khái niệm về Bus

**Bus:** Tập hợp các đường dẫn điện để truyền dữ liệu giữa các thành phần.

**Phân loại Bus:**

**A. Theo chức năng:**

**1. Data Bus (Bus dữ liệu):**
- Truyền dữ liệu
- Hai chiều (bidirectional)
- Độ rộng: 8, 16, 32, 64 bit

**2. Address Bus (Bus địa chỉ):**
- Chỉ định địa chỉ bộ nhớ/thiết bị
- Một chiều (unidirectional)
- Số đường: n → Không gian địa chỉ 2ⁿ

**Ví dụ:**
```
Address Bus 32 bit → 2³² = 4GB địa chỉ
Address Bus 64 bit → 2⁶⁴ = 16 EB địa chỉ
```

**3. Control Bus (Bus điều khiển):**
- Tín hiệu điều khiển: Read, Write, Reset, Interrupt
- Hai chiều

**B. Theo vị trí:**

**1. Internal Bus (Bus nội bộ):**
- Bên trong CPU: ALU ↔ Register
- Tốc độ rất cao

**2. System Bus:**
- Kết nối CPU, RAM, Chipset
- FSB (Front Side Bus) - cũ
- QPI, UPI (Intel) - mới
- Infinity Fabric (AMD)

**3. Expansion Bus:**
- Kết nối thiết bị mở rộng
- PCIe, USB

**Thông số Bus:**

**1. Độ rộng (Width):**
- Số bit truyền song song
- 32-bit, 64-bit

**2. Tần số (Clock Speed):**
- MHz, GHz

**3. Băng thông (Bandwidth):**
```
Bandwidth = Width × Frequency

Ví dụ:
64-bit bus @ 1600 MHz
= 64 × 1600 × 10⁶ bits/s
= 102.4 Gb/s = 12.8 GB/s
```

#### 3.2.4. Các kiến trúc nhiều bus

**Kiến trúc 1 bus (cổ điển):**
```
CPU ─┬─ RAM
     │
     ├─ I/O
     │
     └─ Disk

Nhược điểm: Tắc nghẽn, chậm
```

**Kiến trúc nhiều bus (hiện đại):**
```
       ┌─────────────┐
       │     CPU     │
       └──────┬──────┘
              │
        ┌─────┴──────┐
        │  Northbridge│ (Memory Controller Hub)
        └─┬────────┬─┘
          │        │
        ┌─▼──┐  ┌─▼──┐
        │RAM │  │GPU │ (PCIe)
        └────┘  └────┘
          │
        ┌─▼─────────┐
        │Southbridge│ (I/O Controller Hub)
        └─┬─────┬───┘
          │     │
       ┌──▼─┐ ┌─▼──┐
       │USB │ │SATA│
       └────┘ └────┘
```

**Kiến trúc mới (Intel/AMD):**
- Memory controller tích hợp trong CPU
- Kết nối trực tiếp CPU ↔ RAM (nhanh hơn)

### 3.3. CẤU TRÚC BUS

#### 3.3.1. Cấu trúc bus của Core i

**Intel Core i (Haswell trở về sau):**

```
┌──────────────────────────┐
│          CPU             │
│  ┌──────────────────┐   │
│  │  Cores + Cache   │   │
│  └──────────────────┘   │
│  ┌──────────────────┐   │
│  │ Memory Controller│───┼──► DDR4/DDR5
│  └──────────────────┘   │
│  ┌──────────────────┐   │
│  │  PCIe Controller │───┼──► GPU (PCIe)
│  └──────────────────┘   │
└──────────┬───────────────┘
           │ DMI (Direct Media Interface)
       ┌───▼───────┐
       │ Chipset   │
       │  (PCH)    │
       └─┬───┬─────┘
         │   │
    ┌────▼┐ ┌▼────┐
    │SATA│ │ USB │
    └────┘ └─────┘
```

**DMI:** Kết nối CPU và Chipset
- DMI 3.0: 8 GT/s
- DMI 4.0: 16 GT/s

#### 3.3.2. Một số chuẩn của thiết bị nhập/xuất

**A. IDE (Integrated Drive Electronics) - Lỗi thời:**
- Chuẩn cũ cho HDD
- PATA (Parallel ATA)
- 40/80 pin ribbon cable
- Tốc độ: 133 MB/s (ATA-133)

**B. SATA (Serial ATA):**

**Đặc điểm:**
- Thay thế IDE
- Cable mỏng (7 pin)
- Hot-swappable

**Phiên bản:**
```
SATA I:   1.5 Gb/s = 150 MB/s
SATA II:  3 Gb/s   = 300 MB/s
SATA III: 6 Gb/s   = 600 MB/s
```

**C. USB (Universal Serial Bus):**

**Phiên bản:**
```
USB 1.1:  12 Mb/s    (Full Speed)
USB 2.0:  480 Mb/s   (High Speed) = 60 MB/s
USB 3.0:  5 Gb/s     (SuperSpeed) = 625 MB/s
USB 3.1:  10 Gb/s
USB 3.2:  20 Gb/s
USB 4:    40 Gb/s
```

**Đặc điểm:**
- Hot-plug
- Cấp nguồn (5V)
- Nhiều loại connector: Type-A, Type-B, Type-C

**D. Thunderbolt:**
- Phát triển bởi Intel + Apple
- Kết hợp PCIe + DisplayPort
- Thunderbolt 3/4: 40 Gb/s (qua USB-C)

#### 3.3.3. Bus PCI và PCI Express

**A. PCI (Peripheral Component Interconnect) - Cũ:**
- 32-bit / 33 MHz → 133 MB/s
- 64-bit / 66 MHz → 533 MB/s
- Parallel bus
- Shared bandwidth

**B. PCIe (PCI Express) - Hiện tại:**

**Đặc điểm:**
- Serial bus (điểm-điểm)
- Lane-based: x1, x4, x8, x16
- Mỗi lane: 2 đường (send + receive)

**Tốc độ (mỗi lane, cả 2 chiều):**
```
PCIe 1.0:  2.5 GT/s  → 250 MB/s
PCIe 2.0:  5 GT/s    → 500 MB/s
PCIe 3.0:  8 GT/s    → ~1 GB/s (984 MB/s)
PCIe 4.0:  16 GT/s   → ~2 GB/s
PCIe 5.0:  32 GT/s   → ~4 GB/s
PCIe 6.0:  64 GT/s   → ~8 GB/s
```

**Băng thông tổng:**
```
PCIe 3.0 x16: 16 GB/s (cả 2 chiều)
PCIe 4.0 x16: 32 GB/s
```

**Slot:**
- x1: Network card, sound card
- x4: NVMe SSD (M.2)
- x16: GPU

#### 3.3.4. Các phương pháp nhập/xuất

**A. Programmed I/O (PIO):**

CPU chủ động đọc/ghi từng byte.

**Quy trình:**
```
1. CPU kiểm tra trạng thái thiết bị
2. CPU gửi lệnh
3. CPU chờ thiết bị sẵn sàng
4. CPU đọc/ghi dữ liệu
```

**Nhược điểm:** CPU bận, lãng phí

**B. Interrupt-Driven I/O:**

Thiết bị gửi ngắt khi sẵn sàng.

**Quy trình:**
```
1. CPU gửi lệnh I/O
2. CPU làm việc khác
3. Thiết bị hoàn thành → Gửi IRQ (Interrupt)
4. CPU xử lý ngắt
```

**Ưu điểm:** CPU không chờ đợi

**C. DMA (Direct Memory Access):**

Thiết bị truyền dữ liệu trực tiếp với RAM, không qua CPU.

**Quy trình:**
```
1. CPU cấu hình DMA Controller:
   - Địa chỉ nguồn
   - Địa chỉ đích
   - Kích thước
2. DMA thực hiện truyền
3. DMA gửi ngắt khi hoàn thành
```

**Ưu điểm:** Giải phóng CPU, nhanh

**Ví dụ:** Đọc file từ HDD
```
Không DMA:
  HDD → CPU → RAM (CPU làm trung gian)

Có DMA:
  HDD → DMA Controller → RAM (CPU rảnh)
```

### 3.4. TÍN HIỆU TUẦN TỰ VÀ TÍN HIỆU SỐ

**A. Analog (Tín hiệu tương tự):**
- Giá trị liên tục
- Ví dụ: Âm thanh, nhiệt độ
```
Giá trị
  │    ╱╲
  │   ╱  ╲╱╲
  │  ╱      ╲
  └──────────► Thời gian
```

**B. Digital (Tín hiệu số):**
- Giá trị rời rạc (0, 1)
- Chống nhiễu tốt
```
Giá trị
  │ ┌─┐   ┌─┐
1 │ │ │   │ │
  │ │ └─┐ │ └─
0 │ │   └─┘
  └──────────► Thời gian
```

**ADC (Analog-to-Digital Converter):**
- Chuyển analog → digital
- Microphone → Số

**DAC (Digital-to-Analog Converter):**
- Chuyển digital → analog
- Số → Speaker

---

## CHƯƠNG 4: BỘ XỬ LÝ

### 4.1. CẤU TRÚC BỘ XỬ LÝ

#### 4.1.1. Cấu trúc tổng quát

**Sơ đồ khối CPU:**
```
┌──────────────────────────────────────┐
│              CPU                     │
│                                      │
│  ┌────────────────────────────────┐ │
│  │     Control Unit (CU)          │ │
│  │  - Instruction Decoder         │ │
│  │  - Control Logic               │ │
│  └────────────────────────────────┘ │
│                                      │
│  ┌────────────────────────────────┐ │
│  │        Registers               │ │
│  │  - PC, IR, MAR, MBR            │ │
│  │  - General Purpose Registers   │ │
│  └────────────────────────────────┘ │
│                                      │
│  ┌────────────────────────────────┐ │
│  │      ALU (Arithmetic Logic)    │ │
│  │  - Adder, Multiplier           │ │
│  │  - Logic Gates                 │ │
│  │  - Flags (Zero, Carry, ...)    │ │
│  └────────────────────────────────┘ │
│                                      │
│  ┌────────────────────────────────┐ │
│  │         Cache                  │ │
│  │   L1 I-Cache / D-Cache         │ │
│  │   L2 Cache                     │ │
│  └────────────────────────────────┘ │
└──────────────────────────────────────┘
```

#### 4.1.2. Các thanh ghi

**A. Thanh ghi đặc biệt:**

**1. PC (Program Counter):**
- Chứa địa chỉ lệnh tiếp theo
- Tự động tăng sau mỗi lệnh

**2. IR (Instruction Register):**
- Chứa lệnh đang thực thi

**3. MAR (Memory Address Register):**
- Chứa địa chỉ bộ nhớ cần truy xuất

**4. MBR/MDR (Memory Buffer/Data Register):**
- Chứa dữ liệu đọc/ghi từ bộ nhớ

**5. SP (Stack Pointer):**
- Trỏ đến đỉnh stack

**6. FLAGS/PSW (Program Status Word):**
- **Z (Zero):** Kết quả = 0
- **C (Carry):** Có nhớ
- **S (Sign):** Âm/dương
- **O (Overflow):** Tràn số
- **P (Parity):** Chẵn lẻ

**B. Thanh ghi đa năng (General Purpose):**

**x86:**
- EAX, EBX, ECX, EDX (32-bit)
- RAX, RBX, RCX, RDX (64-bit)

**ARM:**
- R0-R15
- R13 = SP, R14 = LR, R15 = PC

#### 4.1.3. Đơn vị số học và luận lý (ALU)

**Chức năng:**

**1. Số học:**
- Cộng, trừ, nhân, chia
- Increment, Decrement

**2. Logic:**
- AND, OR, NOT, XOR
- Shift, Rotate

**3. So sánh:**
- CMP (Compare)
- Cập nhật FLAGS

**Sơ đồ ALU:**
```
     Operand A    Operand B
        │              │
        ▼              ▼
    ┌───────────────────────┐
    │                       │
    │  ┌─────────────────┐ │
    │  │   Adder         │ │
    │  ├─────────────────┤ │
    │  │   Multiplier    │ │
    │  ├─────────────────┤ │
    │  │   Logic Unit    │ │
    │  ├─────────────────┤ │
    │  │   Shifter       │ │
    │  └─────────────────┘ │
    │          │            │
    │      MUX (Opcode)     │
    └──────────┬────────────┘
               │
               ▼
           Result + Flags
```

#### 4.1.4. Đơn vị điều khiển (CU)

**Chức năng:**
1. Nạp lệnh (Fetch)
2. Giải mã lệnh (Decode)
3. Tạo tín hiệu điều khiển
4. Điều phối hoạt động ALU, Register, Memory

**Loại CU:**

**1. Hardwired (Cứng):**
- Logic cố định
- Nhanh
- Khó thay đổi
- RISC

**2. Microprogrammed (Vi chương trình):**
- Dùng microcode
- Linh hoạt
- Chậm hơn
- CISC

### 4.2. CÁC PHƯƠNG PHÁP NÂNG CAO

#### 4.2.1. Tác động Clock

**Tăng tần số Clock:**
- 3 GHz → 4 GHz → +33% hiệu năng
- Nhưng: Tăng nhiệt, tiêu thụ điện

**Giới hạn:**
- Công nghệ chế tạo
- Tản nhiệt
- Power Wall

#### 4.2.2. Cơ chế đường ống (Pipelining)

**Ý tưởng:** Chia nhỏ việc thực thi lệnh thành nhiều giai đoạn, xử lý song song nhiều lệnh.

**5-stage Pipeline:**
```
1. IF (Instruction Fetch)
2. ID (Instruction Decode)
3. EX (Execute)
4. MEM (Memory Access)
5. WB (Write Back)
```

**Ví dụ:**
```
Không pipeline:
Lệnh 1: IF-ID-EX-MEM-WB (5 chu kỳ)
Lệnh 2:                   IF-ID-EX-MEM-WB (5 chu kỳ)
Tổng: 10 chu kỳ cho 2 lệnh

Có pipeline:
Chu kỳ: 1   2   3   4   5   6   7   8   9
Lệnh 1: IF  ID  EX  MEM WB
Lệnh 2:     IF  ID  EX  MEM WB
Lệnh 3:         IF  ID  EX  MEM WB
Lệnh 4:             IF  ID  EX  MEM WB
Tổng: 9 chu kỳ cho 4 lệnh (lý tưởng: 1 lệnh/chu kỳ)
```

**Hazards (Xung đột):**

**1. Data Hazard:**
```
ADD R1, R2, R3  # R1 = R2 + R3
SUB R4, R1, R5  # R4 = R1 - R5 (cần chờ R1)
```

**Giải pháp:**
- Forwarding/Bypassing
- Stall (chờ)

**2. Control Hazard:**
- Branch (rẽ nhánh) → Không biết lệnh tiếp theo

**Giải pháp:**
- Branch Prediction (dự đoán)
- Speculative Execution

**3. Structural Hazard:**
- Xung đột tài nguyên phần cứng

#### 4.2.3. Thực thi lệnh song song

**A. Superscalar:**

Nhiều pipeline song song.

```
Pipeline 1: Lệnh 1  Lệnh 3  Lệnh 5
Pipeline 2: Lệnh 2  Lệnh 4  Lệnh 6

→ Thực thi 2 lệnh/chu kỳ
```

**B. Out-of-Order Execution:**

Thực thi lệnh không theo thứ tự nếu không phụ thuộc.

```
Lệnh 1: ADD R1, R2, R3
Lệnh 2: MUL R4, R5, R6  ← Không phụ thuộc Lệnh 1
Lệnh 3: SUB R7, R1, R8  ← Phụ thuộc Lệnh 1

Thứ tự thực thi: 1, 2, 3 (song song 1 và 2)
```

**C. SIMD (Single Instruction Multiple Data):**

Một lệnh xử lý nhiều dữ liệu.

```
Lệnh: ADD V1, V2, V3  (Vector)

V1 = [1, 2, 3, 4]
V2 = [5, 6, 7, 8]
V3 = [6, 8, 10, 12]  (song song)
```

**Ứng dụng:** Đồ họa, AI

**Ví dụ:**
- SSE, AVX (Intel)
- NEON (ARM)

#### 4.2.4. Sử dụng bộ nhớ Cache

**Cache:** Bộ nhớ nhỏ, rất nhanh, gần CPU.

**Phân cấp:**
```
Registers: < 1 KB, ~0.3 ns
L1 Cache:   32-64 KB, ~1 ns
L2 Cache:   256-512 KB, ~3 ns
L3 Cache:   8-32 MB, ~10 ns
RAM:        8-64 GB, ~50-100 ns
SSD:        500 GB+, ~100 μs
HDD:        1 TB+, ~5-10 ms
```

**Nguyên lý Locality:**

**1. Temporal Locality:**
- Dữ liệu vừa dùng sẽ được dùng lại sớm
- Ví dụ: Biến trong vòng lặp

**2. Spatial Locality:**
- Dữ liệu gần nhau sẽ được dùng cùng lúc
- Ví dụ: Mảng

**Cache Hit/Miss:**
- **Hit:** Dữ liệu có trong cache
- **Miss:** Không có, phải lấy từ RAM

**Tỷ lệ Hit:**
```
Hit Rate = Hits / (Hits + Misses)

Ví dụ: 95% hit rate
Average Access Time = 0.95 × 1ns + 0.05 × 100ns = 5.95ns
```

### 4.3. TỔ CHỨC CPU ĐA NHÂN

**Multi-core:** Nhiều lõi xử lý trong 1 chip.

**Lợi ích:**
- Tăng hiệu năng đa tác vụ
- Tiết kiệm điện (so với tăng tần số)

**Kiến trúc:**

**A. Homogeneous (Đồng nhất):**

Tất cả core giống nhau.

```
┌──────────────────────────┐
│  Core 1   Core 2         │
│  ┌────┐  ┌────┐          │
│  │ L1 │  │ L1 │          │
│  └────┘  └────┘          │
│      └────┬────┘          │
│       L2 Cache            │
│           │               │
│       L3 Cache (Shared)   │
└───────────┴───────────────┘
```

**B. Heterogeneous (Không đồng nhất):**

Core khác nhau (Performance + Efficiency).

**Ví dụ:** ARM big.LITTLE, Intel Alder Lake
```
┌──────────────────────────┐
│ P-cores     E-cores      │
│ (Mạnh)      (Tiết kiệm)  │
│  ┌────┐     ┌────┐       │
│  │ P1 │     │ E1 │       │
│  └────┘     └────┘       │
└──────────────────────────┘
```

**Ứng dụng:**
- Tác vụ nặng → P-cores
- Background → E-cores
- Tiết kiệm pin

---

## CHƯƠNG 5: BỘ NHỚ

### 5.1. SỰ PHÂN CẤP BỘ NHỚ

**Memory Hierarchy:**

```
        Nhanh, đắt, nhỏ
            ↑
    ┌─────────────┐
    │  Registers  │  < 1 KB
    ├─────────────┤
    │  L1 Cache   │  32-64 KB
    ├─────────────┤
    │  L2 Cache   │  256-512 KB
    ├─────────────┤
    │  L3 Cache   │  8-32 MB
    ├─────────────┤
    │     RAM     │  8-64 GB
    ├─────────────┤
    │     SSD     │  500 GB+
    ├─────────────┤
    │     HDD     │  1 TB+
    └─────────────┘
            ↓
    Chậm, rẻ, lớn
```

### 5.2. BỘ NHỚ TRONG

#### 5.2.1. Bit nhớ

**Lưu trữ 1 bit:**

**A. SRAM (Static RAM):**

Dùng 6 transistor (flip-flop).

**Ưu điểm:**
- Nhanh
- Không cần refresh

**Nhược điểm:**
- Đắt
- Kích thước lớn

**Dùng cho:** Cache

**B. DRAM (Dynamic RAM):**

Dùng 1 transistor + 1 capacitor.

**Đặc điểm:**
- Capacitor lưu điện tích (0/1)
- Cần refresh (điện tích rò rỉ)

**Ưu điểm:**
- Rẻ
- Nhỏ gọn

**Nhược điểm:**
- Chậm hơn SRAM
- Cần refresh

**Dùng cho:** RAM chính

#### 5.2.2. Tổ chức bộ nhớ

**Cấu trúc:**

```
Address Bus (n bit) → 2ⁿ địa chỉ
Data Bus (m bit) → m bit/địa chỉ

Tổng dung lượng = 2ⁿ × m bits
```

**Ví dụ:**
```
16-bit address, 8-bit data
→ 2¹⁶ = 64K địa chỉ
→ 64K × 8 bit = 512 Kbit = 64 KB
```

**Tổ chức ma trận:**

```
Row Decoder ──┐
              ▼
         ┌─────────────┐
         │ Memory Cell │
         │   Array     │
         │  (Rows×Cols)│
         └─────┬───────┘
               ▼
          Column Decoder
               │
               ▼
           Sense Amplifier
               │
               ▼
           Data Output
```

#### 5.2.3. Phân loại bộ nhớ

**A. ROM (Read-Only Memory):**

**1. Mask ROM:**
- Lập trình khi sản xuất
- Không thể thay đổi

**2. PROM (Programmable ROM):**
- Lập trình 1 lần bằng fuse

**3. EPROM (Erasable PROM):**
- Xóa bằng tia UV
- Lập trình lại được

**4. EEPROM (Electrically EPROM):**
- Xóa bằng điện
- Lập trình lại từng byte

**5. Flash Memory:**
- Xóa theo block
- Nhanh hơn EEPROM
- **Dùng cho:** SSD, USB

**B. RAM (Random Access Memory):**

**1. SRAM:**
- Dùng cho Cache
- Không cần refresh

**2. DRAM:**

**Các loại:**
```
SDRAM (Synchronous):
  - Đồng bộ với clock

DDR (Double Data Rate):
  - DDR1: 2.5V, 200-400 MHz
  - DDR2: 1.8V, 400-800 MHz
  - DDR3: 1.5V, 800-2133 MHz
  - DDR4: 1.2V, 2133-3200 MHz
  - DDR5: 1.1V, 4800-6400 MHz
```

**DDR:**
- Truyền dữ liệu cả cạnh lên VÀ cạnh xuống của clock
- → Gấp đôi băng thông

---

## CHƯƠNG 6: TẬP LỆNH

### 6.1. GIỚI THIỆU

**Instruction Set Architecture (ISA):** Tập hợp các lệnh mà CPU có thể thực thi.

**Ví dụ:**
- x86 (Intel, AMD)
- ARM
- MIPS
- RISC-V

### 6.2. BIỂU DIỄN LỆNH

**Cấu trúc lệnh:**

```
┌─────────┬──────────┬──────────┬──────────┐
│ Opcode  │ Operand1 │ Operand2 │ Operand3 │
└─────────┴──────────┴──────────┴──────────┘
```

**Opcode (Operation Code):** Xác định phép toán (ADD, SUB, MOV, ...)

**Operand:** Toán hạng (register, memory, immediate)

**Ví dụ:**
```
ADD R1, R2, R3  # R1 = R2 + R3

Opcode = ADD
Operand1 = R1 (đích)
Operand2 = R2 (nguồn)
Operand3 = R3 (nguồn)
```

**Độ dài lệnh:**

**1. Fixed-length (Cố định):**
- RISC: 32-bit
- Đơn giản, pipeline dễ

**2. Variable-length (Thay đổi):**
- x86: 1-15 bytes
- Phức tạp, linh hoạt

### 6.3. CÁC DẠNG DỮ LIỆU

**1. Integer (Số nguyên):**
- 8-bit (byte): -128 ~ 127
- 16-bit (word): -32768 ~ 32767
- 32-bit (dword): -2³¹ ~ 2³¹-1
- 64-bit (qword)

**2. Unsigned Integer:**
- 8-bit: 0 ~ 255
- 16-bit: 0 ~ 65535
- 32-bit: 0 ~ 4,294,967,295

**3. Float (Số thực):**

**IEEE 754:**
- Float (32-bit): 1 bit sign, 8 bit exponent, 23 bit mantissa
- Double (64-bit): 1 bit sign, 11 bit exponent, 52 bit mantissa

**4. Character:**
- ASCII: 8-bit
- Unicode UTF-8: 1-4 bytes

**5. Boolean:**
- True/False (1 bit, nhưng thường dùng 1 byte)

### 6.4. CÁC PHƯƠNG PHÁP ĐỊNH ĐỊA CHỈ

**1. Immediate (Tức thời):**

Operand là hằng số trong lệnh.

```
MOV R1, #5   # R1 = 5
```

**2. Direct (Trực tiếp):**

Operand là địa chỉ bộ nhớ.

```
MOV R1, [1000]  # R1 = Memory[1000]
```

**3. Indirect (Gián tiếp):**

Operand là địa chỉ chứa địa chỉ.

```
MOV R1, [[1000]]  # R1 = Memory[Memory[1000]]
```

**4. Register (Thanh ghi):**

Operand là thanh ghi.

```
MOV R1, R2   # R1 = R2
```

**5. Register Indirect (Gián tiếp qua thanh ghi):**

```
MOV R1, [R2]   # R1 = Memory[R2]
```

**6. Indexed (Chỉ số):**

```
MOV R1, [R2 + 100]  # R1 = Memory[R2 + 100]
```

**Dùng cho:** Mảng
```
int arr[100];
arr[i] → Base + i × size
```

**7. Stack:**

```
PUSH R1    # Stack[SP] = R1; SP--
POP R2     # R2 = Stack[SP]; SP++
```

---

## KẾT LUẬN CHƯƠNG 3-6

Đã trình bày:
- **Clock & Bus:** Đồng bộ và truyền dữ liệu
- **CPU:** Cấu trúc, pipeline, multi-core
- **Memory:** Phân cấp, SRAM/DRAM
- **ISA:** Tập lệnh và định địa chỉ

## BÀI TẬP

**Bài 1:** Tính băng thông của bus 128-bit @ 3200 MHz.

**Bài 2:** So sánh SRAM và DRAM.

**Bài 3:** Giải thích pipeline và hazard.

**Bài 4:** Tại sao cache lại quan trọng?

**Bài 5:** Phân biệt các phương pháp định địa chỉ với ví dụ.
