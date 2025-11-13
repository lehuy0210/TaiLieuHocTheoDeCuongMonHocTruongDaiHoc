# CHƯƠNG 1: GIỚI THIỆU KIẾN TRÚC MÁY TÍNH

## 1.1. GIỚI THIỆU KIẾN TRÚC MÁY TÍNH

### 1.1.1. Định nghĩa KTMT

**Kiến trúc máy tính (Computer Architecture)** là cách tổ chức và kết nối các thành phần phần cứng của máy tính để tạo thành một hệ thống hoàn chỉnh.

**Hai khía cạnh:**

1. **Kiến trúc tập lệnh (ISA - Instruction Set Architecture):**
   - Giao diện giữa phần cứng và phần mềm
   - Định nghĩa tập lệnh, thanh ghi, định dạng dữ liệu
   - Ví dụ: x86, ARM, MIPS, RISC-V

2. **Tổ chức máy tính (Computer Organization):**
   - Cách thức hiện thực phần cứng
   - Cấu trúc vật lý của các thành phần
   - Cách các thành phần làm việc với nhau

**Phân biệt:**
- **Kiến trúc:** WHAT - Máy tính làm gì
- **Tổ chức:** HOW - Máy tính làm như thế nào

### 1.1.2. Cấu trúc và chức năng của máy tính

**Kiến trúc Von Neumann:**

Mô hình cơ bản của máy tính hiện đại gồm 5 thành phần:

```
┌─────────────────────────────────────────┐
│         1. Bộ nhớ (Memory)             │
│    Chứa dữ liệu và chương trình        │
└──────────┬──────────────────────────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼────┐   ┌───▼────────┐
│2. Input│   │ 3. Output  │
│  (I/O) │   │   (I/O)    │
└────────┘   └────────────┘
           │
    ┌──────▼────────────────────────┐
    │   4. CPU (Bộ xử lý trung tâm)│
    │  ┌─────────────────────────┐ │
    │  │ 4.1 ALU (Số học/Logic) │ │
    │  └─────────────────────────┘ │
    │  ┌─────────────────────────┐ │
    │  │ 4.2 CU (Điều khiển)    │ │
    │  └─────────────────────────┘ │
    │  ┌─────────────────────────┐ │
    │  │ 4.3 Thanh ghi          │ │
    │  └─────────────────────────┘ │
    └───────────────────────────────┘
```

**Chức năng của từng thành phần:**

**1. Bộ nhớ (Memory):**
- Lưu trữ dữ liệu và chương trình
- RAM, ROM, Cache

**2. Thiết bị nhập (Input):**
- Bàn phím, chuột, scanner, micro
- Đưa dữ liệu vào máy tính

**3. Thiết bị xuất (Output):**
- Màn hình, máy in, loa
- Xuất kết quả ra ngoài

**4. CPU (Central Processing Unit):**
- **ALU:** Thực hiện phép toán số học và logic
- **CU:** Điều khiển hoạt động của máy tính
- **Thanh ghi:** Bộ nhớ tốc độ cao trong CPU

**5. Bus hệ thống:**
- Đường truyền dữ liệu giữa các thành phần

---

## 1.2. HOẠT ĐỘNG CỦA MÁY TÍNH

### 1.2.1. Phân loại máy tính điện tử

**A. Theo mục đích sử dụng:**

**1. Máy tính chuyên dụng (Special-purpose):**
- Được thiết kế cho một nhiệm vụ cụ thể
- Ví dụ: Máy tính nhúng trong ô tô, điều hòa

**2. Máy tính đa năng (General-purpose):**
- Thực hiện nhiều loại tác vụ khác nhau
- Ví dụ: PC, laptop, server

**B. Theo kích thước và năng lực:**

**1. Supercomputer (Siêu máy tính):**
- Hiệu năng cực cao
- Dùng cho nghiên cứu khoa học, mô phỏng
- Ví dụ: Fugaku, Summit

**2. Mainframe:**
- Máy tính lớn cho doanh nghiệp
- Xử lý khối lượng giao dịch lớn
- Ví dụ: IBM z Series

**3. Server:**
- Cung cấp dịch vụ cho nhiều client
- Web server, database server

**4. Workstation:**
- Máy trạm cao cấp cho chuyên gia
- Đồ họa 3D, CAD, phân tích dữ liệu

**5. Personal Computer (PC):**
- Desktop, Laptop
- Sử dụng cá nhân

**6. Mobile Device:**
- Smartphone, Tablet
- Tính di động cao

**7. Embedded System:**
- Hệ thống nhúng
- Tích hợp trong thiết bị khác

**C. Theo kiến trúc:**

**1. CISC (Complex Instruction Set Computer):**
- Tập lệnh phức tạp
- Ví dụ: x86 (Intel, AMD)

**2. RISC (Reduced Instruction Set Computer):**
- Tập lệnh đơn giản
- Ví dụ: ARM, MIPS, RISC-V

### 1.2.2. Sơ đồ tổng quát của máy tính

**Sơ đồ khối chi tiết:**

```
┌─────────────────────────────────────────────────────┐
│                    Motherboard                       │
│                                                      │
│  ┌────────────────────────────────────────────┐    │
│  │              CPU (Processor)                │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐ │    │
│  │  │   Core   │  │  Cache   │  │Registers │ │    │
│  │  │   ALU    │  │  L1/L2   │  │          │ │    │
│  │  │   CU     │  │          │  │          │ │    │
│  │  └──────────┘  └──────────┘  └──────────┘ │    │
│  └────────────┬───────────────────────────────┘    │
│               │                                      │
│  ┌────────────┴───────────────┐                    │
│  │    System Bus              │                    │
│  │  ┌──────┐ ┌──────┐ ┌─────┐│                    │
│  │  │ Data │ │Addr. │ │Ctrl.││                    │
│  │  └──────┘ └──────┘ └─────┘│                    │
│  └────────┬────────────┬──────┘                    │
│           │            │                            │
│  ┌────────▼──┐    ┌───▼──────────┐                │
│  │    RAM    │    │   Chipset    │                │
│  │  (Memory) │    │   (North/    │                │
│  │           │    │    South     │                │
│  │           │    │   Bridge)    │                │
│  └───────────┘    └───┬──────────┘                │
│                       │                            │
│         ┌─────────────┴─────────────┐             │
│         │                           │             │
│    ┌────▼─────┐              ┌──────▼────┐       │
│    │   GPU    │              │    I/O    │       │
│    │ (VGA/    │              │   Slots   │       │
│    │  PCIe)   │              │ (PCIe,USB)│       │
│    └──────────┘              └───────────┘       │
└─────────────────────────────────────────────────┘
         │                           │
    ┌────▼────┐                 ┌───▼──────┐
    │ Monitor │                 │ Storage  │
    └─────────┘                 │HDD/SSD   │
                                └──────────┘
```

**Các thành phần chính:**

**1. CPU (Central Processing Unit):**
- Bộ vi xử lý trung tâm
- Thực thi lệnh của chương trình

**2. RAM (Random Access Memory):**
- Bộ nhớ tạm thời
- Mất dữ liệu khi tắt nguồn

**3. Storage (HDD/SSD):**
- Lưu trữ dài hạn
- Giữ dữ liệu khi tắt máy

**4. Motherboard:**
- Bo mạch chủ
- Kết nối tất cả linh kiện

**5. Power Supply (PSU):**
- Nguồn điện
- Cấp điện cho các linh kiện

**6. GPU (Graphics Processing Unit):**
- Xử lý đồ họa
- Card màn hình

**7. I/O Devices:**
- Thiết bị nhập/xuất
- Bàn phím, chuột, màn hình

### 1.2.3. Hoạt động của máy tính

**Chu trình lệnh (Instruction Cycle):**

Máy tính hoạt động dựa trên chu trình lệnh, gồm 4 bước:

```
┌──────────────┐
│1. FETCH      │ ─── Nạp lệnh từ bộ nhớ
│  (Nạp lệnh)  │
└──────┬───────┘
       │
┌──────▼───────┐
│2. DECODE     │ ─── Giải mã lệnh
│ (Giải mã)    │
└──────┬───────┘
       │
┌──────▼───────┐
│3. EXECUTE    │ ─── Thực thi lệnh
│ (Thực thi)   │
└──────┬───────┘
       │
┌──────▼───────┐
│4. STORE      │ ─── Lưu kết quả
│ (Lưu trữ)    │
└──────┬───────┘
       │
       └───────────► Lặp lại
```

**Chi tiết từng bước:**

**1. FETCH (Nạp lệnh):**
- PC (Program Counter) chứa địa chỉ lệnh tiếp theo
- CPU nạp lệnh từ bộ nhớ vào IR (Instruction Register)
- PC tăng lên chỉ đến lệnh tiếp theo

**2. DECODE (Giải mã):**
- Bộ giải mã lệnh phân tích IR
- Xác định lệnh cần thực hiện
- Xác định toán hạng

**3. EXECUTE (Thực thi):**
- ALU thực hiện phép toán
- Hoặc CU điều khiển hoạt động I/O
- Hoặc truy xuất bộ nhớ

**4. STORE (Lưu trữ):**
- Lưu kết quả vào thanh ghi hoặc bộ nhớ
- Cập nhật cờ trạng thái

**Ví dụ: Thực hiện lệnh ADD A, B**

```
Bước 1 - FETCH:
  PC = 1000 (địa chỉ lệnh)
  IR = [ADD A, B] (nạp lệnh vào IR)
  PC = 1001 (tăng PC)

Bước 2 - DECODE:
  Opcode = ADD (phép cộng)
  Operand1 = A (địa chỉ A)
  Operand2 = B (địa chỉ B)

Bước 3 - EXECUTE:
  Đọc giá trị tại địa chỉ A → Reg1
  Đọc giá trị tại địa chỉ B → Reg2
  ALU: Result = Reg1 + Reg2

Bước 4 - STORE:
  Lưu Result vào địa chỉ A
```

**Sơ đồ luồng dữ liệu:**

```
Memory ──(1)──> IR ──(2)──> Decoder ──(3)──> ALU ──(4)──> Memory
   ↑                                            │
   └────────────────────────────────────────────┘
```

---

## 1.3. TỔ CHỨC MÁY TÍNH

### 1.3.1. Tổ chức vật lý

**Cấu trúc phần cứng:**

**A. Case (Vỏ máy):**
- Tower case: Đứng
- Desktop case: Ngang
- Bảo vệ linh kiện, làm mát

**B. Motherboard (Bo mạch chủ):**

**Các thành phần trên Mainboard:**

1. **CPU Socket:**
   - LGA (Intel): Chân trên socket
   - PGA (AMD): Chân trên CPU
   - Ví dụ: LGA 1700, AM5

2. **Chipset:**
   - **Northbridge:** Kết nối CPU, RAM, GPU
   - **Southbridge:** Kết nối I/O, storage
   - Hiện đại: Tích hợp vào CPU

3. **RAM Slots:**
   - DIMM slots (Desktop)
   - SO-DIMM (Laptop)
   - DDR4, DDR5

4. **Expansion Slots:**
   - PCIe x16: GPU
   - PCIe x1/x4: Mở rộng

5. **Storage Connectors:**
   - SATA: HDD/SSD
   - M.2: NVMe SSD

6. **Power Connectors:**
   - ATX 24-pin: Main power
   - EPS 8-pin: CPU power

7. **I/O Ports:**
   - USB, Audio, LAN, Video

8. **BIOS/UEFI Chip:**
   - Firmware khởi động

**C. Cooling System:**

1. **Air Cooling:**
   - CPU cooler: Tản nhiệt khí
   - Case fans: Quạt thoát nhiệt

2. **Liquid Cooling:**
   - AIO (All-in-One)
   - Custom loop

**D. Cấu trúc bên trong Case:**

```
┌─────────────────────────────────┐
│         Front Panel             │
│  [LED] [Power] [Reset] [USB]   │
├─────────────────────────────────┤
│                                 │
│  ┌────────────┐  ┌───────────┐│
│  │   PSU      │  │  Storage  ││
│  │            │  │  Bays     ││
│  └────────────┘  └───────────┘│
│                                 │
│  ┌──────────────────────────┐ │
│  │      Motherboard          │ │
│  │  ┌────┐ ┌──────┐ ┌────┐ │ │
│  │  │CPU │ │ RAM  │ │GPU │ │ │
│  │  └────┘ └──────┘ └────┘ │ │
│  └──────────────────────────┘ │
│                                 │
│  [Cable Management]             │
└─────────────────────────────────┘
```

### 1.3.2. Quá trình khởi động máy tính

**Boot Process (Quy trình khởi động):**

```
┌──────────────┐
│ 1. Power On  │ ─── Bật nguồn
└──────┬───────┘
       │
┌──────▼───────┐
│ 2. POST      │ ─── Power-On Self Test
│   (BIOS)     │     Kiểm tra phần cứng
└──────┬───────┘
       │
┌──────▼───────┐
│ 3. BIOS/UEFI │ ─── Khởi tạo phần cứng
│  Bootstrap   │
└──────┬───────┘
       │
┌──────▼───────┐
│4. Boot Loader│ ─── GRUB, Windows Boot Manager
│   (MBR/GPT)  │
└──────┬───────┘
       │
┌──────▼───────┐
│5. Load OS    │ ─── Nạp Kernel
│   Kernel     │
└──────┬───────┘
       │
┌──────▼───────┐
│6. Init System│ ─── systemd, init
│              │
└──────┬───────┘
       │
┌──────▼───────┐
│ 7. Login     │ ─── Màn hình đăng nhập
└──────────────┘
```

**Chi tiết từng bước:**

**Bước 1: Power On**
- Nhấn nút nguồn
- PSU cấp điện cho mainboard
- CPU bắt đầu hoạt động

**Bước 2: POST (Power-On Self Test)**
- BIOS/UEFI kiểm tra:
  - CPU hoạt động không?
  - RAM có lỗi không?
  - GPU có tín hiệu không?
  - Storage kết nối chưa?
- Beep codes nếu có lỗi

**Bước 3: Bootstrap**
- BIOS/UEFI khởi tạo phần cứng
- Tìm boot device (HDD, SSD, USB)
- Đọc boot sector

**Bước 4: Boot Loader**
- MBR (Master Boot Record) hoặc GPT (GUID Partition Table)
- GRUB (Linux) hoặc Windows Boot Manager
- Menu chọn OS (nếu dual boot)

**Bước 5: Load OS Kernel**
- Nạp kernel vào RAM
- Kernel khởi tạo drivers
- Mount root filesystem

**Bước 6: Init System**
- systemd (Linux hiện đại)
- Khởi động các services
- Network, GUI, ...

**Bước 7: Login**
- Hiển thị màn hình đăng nhập
- Sẵn sàng sử dụng

**BIOS vs UEFI:**

| BIOS | UEFI |
|------|------|
| 16-bit | 32/64-bit |
| MBR (2TB max) | GPT (> 2TB) |
| Text UI | Graphical UI |
| Chậm | Nhanh |
| Legacy | Hiện đại |

### 1.3.3. Tổng quan về phần mềm

**Phân loại phần mềm:**

```
        Software (Phần mềm)
              │
    ┌─────────┴─────────┐
    │                   │
System Software    Application Software
(Phần mềm hệ thống)  (Phần mềm ứng dụng)
    │                   │
    ├─ OS              ├─ Word, Excel
    ├─ Driver          ├─ Photoshop
    ├─ Utility         ├─ Games
    └─ Compiler        └─ Browsers
```

**A. System Software (Phần mềm hệ thống):**

**1. Operating System (Hệ điều hành):**
- Windows, Linux, macOS
- Quản lý tài nguyên phần cứng
- Cung cấp giao diện cho người dùng

**2. Device Drivers:**
- Điều khiển phần cứng
- GPU driver, printer driver

**3. Utilities:**
- Antivirus, Disk cleaner
- Backup tools

**4. Compilers/Interpreters:**
- GCC, Python, Java
- Dịch code thành machine code

**B. Application Software:**

**1. Productivity:**
- Microsoft Office
- Google Workspace

**2. Creative:**
- Adobe Photoshop, Premiere
- Blender, AutoCAD

**3. Entertainment:**
- Games, Media players

**4. Communication:**
- Browsers, Email clients

**Các lớp phần mềm:**

```
┌─────────────────────────────────┐
│   Applications (Ứng dụng)       │
├─────────────────────────────────┤
│   System Libraries (Thư viện)   │
├─────────────────────────────────┤
│   Operating System (HDH)        │
├─────────────────────────────────┤
│   Firmware (BIOS/UEFI)          │
├─────────────────────────────────┤
│   Hardware (Phần cứng)          │
└─────────────────────────────────┘
```

---

## 1.4. MỘT SỐ THIẾT BỊ NGOẠI VI

### 1.4.1. Đĩa từ (Magnetic Disk)

**A. HDD (Hard Disk Drive):**

**Cấu tạo:**

```
    ┌─────────────────────────┐
    │       Disk Platter      │ ── Đĩa từ
    │      (Từ tính)          │
    ├─────────────────────────┤
    │     Read/Write Head     │ ── Đầu đọc/ghi
    │         (Arm)           │
    ├─────────────────────────┤
    │       Spindle Motor     │ ── Động cơ quay
    │      (5400-7200 RPM)    │
    ├─────────────────────────┤
    │        PCB Board        │ ── Bo mạch điều khiển
    └─────────────────────────┘
```

**Cấu trúc dữ liệu:**

```
Track (Rãnh):
  ┌──────────────────┐
  │ ┌──┐             │
  │ │  │  Sector     │
  │ │  │  (512B/4KB) │
  │ └──┘             │
  │    Cluster       │
  └──────────────────┘

Cylinder: Tập các track cùng vị trí trên nhiều đĩa
```

**Thông số:**
- **Capacity:** 500GB - 20TB
- **Speed:** 5400/7200/10000 RPM
- **Cache:** 64MB - 256MB
- **Interface:** SATA III (6 Gb/s)
- **Latency:** 5-10ms

**Ưu điểm:**
- Dung lượng lớn
- Giá rẻ
- Tuổi thọ cao

**Nhược điểm:**
- Chậm
- Ồn
- Tiêu thụ điện nhiều
- Dễ hỏng khi va đập

**B. SSD (Solid State Drive):**

**Công nghệ NAND Flash:**

```
SLC (Single-Level Cell):   1 bit/cell
MLC (Multi-Level Cell):    2 bit/cell
TLC (Triple-Level Cell):   3 bit/cell
QLC (Quad-Level Cell):     4 bit/cell
```

**Cấu trúc:**

```
┌──────────────────────────┐
│    NAND Flash Chips      │ ── Chip nhớ
├──────────────────────────┤
│    Controller            │ ── Bộ điều khiển
├──────────────────────────┤
│    DRAM Cache (option)   │ ── Cache
├──────────────────────────┤
│    Interface             │ ── SATA/NVMe
└──────────────────────────┘
```

**So sánh HDD vs SSD:**

| Đặc điểm | HDD | SSD |
|----------|-----|-----|
| Tốc độ đọc | 100-200 MB/s | 500-7000 MB/s |
| Độ trễ | 5-10ms | 0.1ms |
| Giá/GB | Rẻ | Đắt |
| Tuổi thọ | 5-10 năm | 5-10 năm (P/E cycles) |
| Tiếng ồn | Có | Không |
| Năng lượng | Cao | Thấp |
| Va đập | Dễ hỏng | Chịu tốt |

### 1.4.2. Đĩa CD và DVD

**A. Compact Disc (CD):**

**Đặc điểm:**
- Đường kính: 12cm
- Dung lượng: 700MB
- Tốc độ: 1x = 150 KB/s

**Loại:**
- **CD-ROM:** Read-Only
- **CD-R:** Recordable (ghi 1 lần)
- **CD-RW:** ReWritable (ghi nhiều lần)

**Cấu trúc:**

```
┌──────────────────────┐
│  Polycarbonate       │ ── Lớp nhựa
├──────────────────────┤
│  Reflective Layer    │ ── Lớp phản xạ (nhôm)
├──────────────────────┤
│  Protective Coating  │ ── Lớp bảo vệ
└──────────────────────┘

Pit (Rãnh) và Land (Phẳng) mã hóa dữ liệu
```

**B. Digital Versatile Disc (DVD):**

**Đặc điểm:**
- Đường kính: 12cm
- Dung lượng:
  - DVD-5 (Single Layer): 4.7GB
  - DVD-9 (Dual Layer): 8.5GB
  - DVD-10 (Double Side, SL): 9.4GB
  - DVD-18 (DS, DL): 17GB
- Tốc độ: 1x = 1.35 MB/s

**Loại:**
- **DVD-ROM**
- **DVD-R/DVD+R**
- **DVD-RW/DVD+RW**

**C. Blu-ray Disc:**

**Đặc điểm:**
- Laser xanh (405nm vs 650nm của DVD)
- Dung lượng:
  - BD-R SL: 25GB
  - BD-R DL: 50GB
  - BD-R XL: 100GB/128GB
- Tốc độ: 1x = 4.5 MB/s

### 1.4.3. Màn hình

**A. Công nghệ hiển thị:**

**1. CRT (Cathode Ray Tube) - Lỗi thời:**
- Ống tia âm cực
- Cồng kềnh, nặng
- Tiêu thụ điện cao

**2. LCD (Liquid Crystal Display):**
- Màn hình tinh thể lỏng
- Cần đèn nền (backlight)
- Mỏng, nhẹ

**Các loại LCD Panel:**

**a) TN (Twisted Nematic):**
- Rẻ
- Thời gian phản hồi nhanh (1ms)
- Góc nhìn hẹp
- Màu sắc kém
- Dùng cho gaming

**b) IPS (In-Plane Switching):**
- Góc nhìn rộng (178°)
- Màu sắc chính xác
- Thời gian phản hồi chậm hơn (4-5ms)
- Đắt hơn TN
- Dùng cho thiết kế, văn phòng

**c) VA (Vertical Alignment):**
- Tương phản cao
- Màu đen sâu
- Trung gian giữa TN và IPS

**3. LED:**
- Thực chất là LCD với đèn nền LED
- Tiết kiệm điện
- Mỏng hơn LCD

**4. OLED (Organic LED):**
- Tự phát sáng, không cần backlight
- Tương phản vô hạn (đen tuyệt đối)
- Màu sắc rực rỡ
- Mỏng
- Đắt
- Dùng trên smartphone, TV cao cấp

**B. Thông số màn hình:**

**1. Độ phân giải (Resolution):**
```
HD:      1280×720    (0.9 MP)
Full HD: 1920×1080   (2 MP)
2K:      2560×1440   (3.7 MP)
4K UHD:  3840×2160   (8.3 MP)
8K:      7680×4320   (33 MP)
```

**2. Tỷ lệ khung hình (Aspect Ratio):**
- 4:3 (cũ)
- 16:9 (phổ biến)
- 21:9 (ultrawide)
- 32:9 (super ultrawide)

**3. Tần số quét (Refresh Rate):**
- 60Hz (tiêu chuẩn)
- 120Hz, 144Hz, 240Hz (gaming)

**4. Thời gian phản hồi (Response Time):**
- 1ms (TN, gaming)
- 4-5ms (IPS)

**5. Độ sáng (Brightness):**
- 250-400 nits (thông thường)
- 500-1000 nits (HDR)

**6. Gam màu (Color Gamut):**
- sRGB: 100%
- Adobe RGB: Rộng hơn
- DCI-P3: Cho video

**C. Cổng kết nối:**

```
VGA (D-Sub):  Analog, cũ
DVI:          Digital, cũ
HDMI:         Digital, phổ biến, có âm thanh
DisplayPort:  Digital, cao cấp, daisy-chain
USB-C/TB3:    Kết hợp nhiều chức năng
```

### 1.4.4. Máy in

**A. Phân loại theo công nghệ:**

**1. Máy in kim (Dot Matrix):**
- Dùng kim đâm qua ruy băng mực
- Ồn
- In được liên tục (hóa đơn)
- Lỗi thời

**2. Máy in phun (Inkjet):**

**Nguyên lý:**
- Phun giọt mực nhỏ lên giấy
- Đầu phun (printhead) di chuyển ngang

**Ưu điểm:**
- Rẻ
- In màu đẹp
- Nhỏ gọn

**Nhược điểm:**
- Tốn mực
- Chậm
- Mực khô nếu không dùng lâu

**Dùng cho:**
- Gia đình
- In ảnh

**3. Máy in laser:**

**Nguyên lý:**

```
1. Charging:   Tích điện cho drum
2. Exposing:   Laser vẽ ảnh lên drum
3. Developing: Mực bám vào vùng laser
4. Transfer:   Chuyển mực lên giấy
5. Fusing:     Nung nóng để mực dính vào giấy
```

**Ưu điểm:**
- Nhanh
- In nhiều, giá mỗi trang rẻ
- Chất lượng tốt (văn bản)
- Bền

**Nhược điểm:**
- Đắt
- Lớn
- In màu kém hơn inkjet (với ảnh)

**Dùng cho:**
- Văn phòng
- In khối lượng lớn

**4. Máy in nhiệt (Thermal):**
- Dùng nhiệt in lên giấy nhiệt
- In hóa đơn, mã vạch
- Nhanh, không cần mực

**B. Thông số máy in:**

**1. DPI (Dots Per Inch):**
- 600 dpi: Văn bản
- 1200 dpi: Đồ họa
- 4800+ dpi: In ảnh

**2. PPM (Pages Per Minute):**
- 10-20 ppm: Gia đình
- 30-50 ppm: Văn phòng
- 100+ ppm: Công nghiệp

**3. Kết nối:**
- USB
- WiFi
- Ethernet
- Bluetooth

**4. Tính năng:**
- Duplex: In 2 mặt tự động
- ADF: Nạp giấy tự động
- Scanner tích hợp

**So sánh Inkjet vs Laser:**

| Đặc điểm | Inkjet | Laser |
|----------|--------|-------|
| Giá mua | Rẻ | Đắt |
| Giá mực/trang | Cao | Thấp |
| Tốc độ | Chậm | Nhanh |
| Chất lượng văn bản | Tốt | Rất tốt |
| Chất lượng ảnh | Rất tốt | Trung bình |
| Kích thước | Nhỏ | Lớn |
| Phù hợp | Gia đình, ít in | Văn phòng, in nhiều |

---

## KẾT LUẬN CHƯƠNG 1

**Tóm tắt nội dung:**

1. **Kiến trúc máy tính:** Cấu trúc và tổ chức của máy tính
2. **Kiến trúc Von Neumann:** 5 thành phần cơ bản
3. **Chu trình lệnh:** Fetch-Decode-Execute-Store
4. **Boot process:** Quy trình khởi động máy
5. **Thiết bị ngoại vi:** HDD, SSD, CD/DVD, màn hình, máy in

**Kiến thức cần nắm:**
- Phân biệt kiến trúc và tổ chức
- Vai trò của từng thành phần trong máy tính
- Cách máy tính thực thi chương trình
- Quy trình khởi động máy
- Đặc điểm các thiết bị lưu trữ và ngoại vi

---

## BÀI TẬP ÔN TẬP CHƯƠNG 1

**Bài 1:** Phân biệt kiến trúc máy tính và tổ chức máy tính. Cho ví dụ.

**Bài 2:** Vẽ sơ đồ khối kiến trúc Von Neumann và giải thích chức năng từng thành phần.

**Bài 3:** Mô tả chu trình lệnh của CPU. Cho ví dụ cụ thể với lệnh SUB A, B.

**Bài 4:** Trình bày quy trình khởi động máy tính từ khi bật nguồn đến khi hiển thị màn hình đăng nhập.

**Bài 5:** So sánh HDD và SSD về cấu tạo, nguyên lý hoạt động, ưu nhược điểm.

**Bài 6:** Phân loại màn hình theo công nghệ hiển thị. Ưu nhược điểm của IPS và TN panel?

**Bài 7:** So sánh máy in phun và máy in laser. Khi nào nên dùng loại nào?

**Bài 8:** Tại sao SSD nhanh hơn HDD rất nhiều?

**Bài 9:** BIOS/UEFI là gì? Vai trò trong quá trình khởi động?

**Bài 10:** Giải thích sự khác biệt giữa CISC và RISC.
