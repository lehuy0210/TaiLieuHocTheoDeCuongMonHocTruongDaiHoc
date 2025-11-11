# TÀI LIỆU HỆ ĐIỀU HÀNH - ĐẦY ĐỦ 6 CHƯƠNG

# CHƯƠNG 1: TỔNG QUAN VỀ HỆ ĐIỀU HÀNH

## 1.1. TỔNG QUAN VỀ HỆ THỐNG MÁY TÍNH

**Hệ thống máy tính gồm 4 thành phần:**

```
┌─────────────────────────────────┐
│        User (Người dùng)        │
├─────────────────────────────────┤
│   Application Programs          │
│   (Word, Browser, Games, ...)   │
├─────────────────────────────────┤
│   Operating System (HDH)        │
├─────────────────────────────────┤
│        Hardware                 │
│  (CPU, Memory, I/O, Storage)    │
└─────────────────────────────────┘
```

## 1.2. TỔNG QUAN VỀ HỆ ĐIỀU HÀNH

### 1.2.1. Khái niệm về hệ điều hành

**Định nghĩa:**

Hệ điều hành (Operating System - OS) là phần mềm hệ thống quản lý và điều phối tài nguyên phần cứng, cung cấp môi trường để chạy các chương trình ứng dụng.

**Hai vai trò:**

**1. Resource Manager (Quản lý tài nguyên):**
- Quản lý CPU, RAM, I/O
- Phân bổ công bằng, hiệu quả

**2. Extended Machine (Máy ảo mở rộng):**
- Che giấu chi tiết phần cứng phức tạp
- Cung cấp giao diện đơn giản (API, system calls)

### 1.2.2. Các chức năng cơ bản

**1. Quản lý tiến trình (Process Management):**
- Tạo, xóa process
- Scheduling (lập lịch)
- Đồng bộ, thông tin liên process

**2. Quản lý bộ nhớ (Memory Management):**
- Cấp phát, thu hồi bộ nhớ
- Virtual memory
- Swapping, paging

**3. Quản lý file (File Management):**
- Tạo, xóa, đọc, ghi file
- Hệ thống file (NTFS, ext4, FAT32)
- Quyền truy cập

**4. Quản lý I/O (I/O Management):**
- Driver
- Buffering, caching
- Interrupt handling

**5. Bảo mật (Security):**
- Xác thực người dùng
- Quyền truy cập
- Firewall

**6. Giao diện người dùng (UI):**
- CLI (Command Line)
- GUI (Graphical)

### 1.2.3. Lịch sử phát triển

**Thế hệ 1 (1945-1955): Không có OS**
- Lập trình bằng dây cắm
- Chạy từng chương trình

**Thế hệ 2 (1955-1965): Batch Systems**
- Xử lý hàng loạt
- Người vận hành nạp băng từ
- Không tương tác

**Thế hệ 3 (1965-1980): Multiprogramming**
- Nhiều chương trình trong RAM
- CPU chuyển đổi khi I/O
- Time-sharing: Chia sẻ thời gian CPU

**Thế hệ 4 (1980-nay): PC và mạng**
- MS-DOS, Windows, Mac OS
- UNIX → Linux
- Internet, GUI

**Thế hệ 5: Di động và Cloud**
- Android, iOS
- Cloud computing
- Virtualization

### 1.2.4. Phân loại hệ điều hành

**A. Theo số người dùng:**

**1. Single-user:**
- MS-DOS
- Windows (desktop)

**2. Multi-user:**
- Linux server
- UNIX

**B. Theo số tác vụ:**

**1. Single-tasking:**
- MS-DOS: Chỉ 1 chương trình

**2. Multi-tasking:**
- Windows, Linux: Nhiều chương trình đồng thời

**C. Theo thời gian thực:**

**1. Real-time OS (RTOS):**
- Phản hồi trong thời gian xác định
- Dùng cho: Robot, điều khiển công nghiệp
- Ví dụ: VxWorks, FreeRTOS

**2. Non-real-time:**
- Windows, Linux thông thường

**D. Theo kiến trúc:**

**1. Monolithic Kernel:**
- Tất cả dịch vụ trong kernel
- Nhanh nhưng phức tạp
- Linux, UNIX

**2. Microkernel:**
- Kernel nhỏ gọn
- Dịch vụ chạy ở user space
- Ổn định hơn
- Minix, QNX

**3. Hybrid:**
- Kết hợp cả hai
- Windows NT

---

# CHƯƠNG 2: TIẾN TRÌNH & LUỒNG

## 2.1. TIẾN TRÌNH (PROCESS)

### 2.1.1. Mô hình

**Định nghĩa:**

Process (tiến trình) là một chương trình đang thực thi.

**Thành phần:**
- **Code segment:** Mã máy
- **Data segment:** Biến toàn cục
- **Stack:** Biến cục bộ, tham số hàm
- **Heap:** Cấp phát động (malloc)
- **PCB:** Process Control Block

**PCB (Process Control Block):**
```
┌─────────────────────────┐
│ Process ID (PID)        │
│ Process State           │
│ Program Counter (PC)    │
│ CPU Registers           │
│ Memory Limits           │
│ List of Open Files      │
│ I/O Status              │
│ CPU Scheduling Info     │
└─────────────────────────┘
```

**Process States (Trạng thái):**

```
┌─────────┐
│  New    │ ─── Process được tạo
└────┬────┘
     │
┌────▼────┐
│  Ready  │ ◄─┐ ─── Sẵn sàng chạy, chờ CPU
└────┬────┘   │
     │       │
┌────▼────┐  │
│ Running │ ─┴─ ─── Đang chạy trên CPU
└────┬────┘
     │
┌────▼────┐
│ Waiting │ ─── Chờ I/O hoặc sự kiện
└────┬────┘
     │
┌────▼────┐
│Terminated│─── Kết thúc
└─────────┘
```

**State Transitions:**
- New → Ready: Admitted
- Ready → Running: Scheduler dispatch
- Running → Ready: Interrupt (time quantum hết)
- Running → Waiting: I/O request
- Waiting → Ready: I/O complete
- Running → Terminated: Exit

### 2.1.2. Hiện thực

**Process Operations:**

**1. Process Creation:**
```c
// UNIX: fork()
pid_t pid = fork();
if (pid == 0) {
    // Child process
    exec("program");
} else {
    // Parent process
    wait(NULL);
}
```

**2. Process Termination:**
```c
exit(0);  // Normal
abort();  // Abnormal
```

**Context Switch (Chuyển ngữ cảnh):**

```
Process A đang chạy
    │
    ├─ Interrupt/System call
    │
    ├─ Lưu state của A vào PCB_A
    ├─ Chọn Process B để chạy
    ├─ Nạp state từ PCB_B
    │
Process B đang chạy
```

**Overhead:** Mất thời gian (~1-1000 μs)

## 2.2. LUỒNG (THREAD)

### 2.2.1. Mô hình

**Định nghĩa:**

Thread (luồng) là đơn vị thực thi nhỏ nhất trong process.

**So sánh Process vs Thread:**

```
Process:
┌─────────────────────────┐
│  Code  │  Data  │ Files │ ← Riêng
├────────┴────────┴───────┤
│ Thread 1 │ Thread 2     │
│ ┌──────┐ │ ┌──────┐    │
│ │Stack1│ │ │Stack2│    │
│ │PC1   │ │ │PC2   │    │ ← Riêng
│ │Reg1  │ │ │Reg2  │    │
│ └──────┘ │ └──────┘    │
└─────────────────────────┘
```

**Chia sẻ:**
- Code, Data, Files
- Heap

**Riêng:**
- Stack
- Registers
- Program Counter

**Lợi ích:**

**1. Responsiveness (Đáp ứng):**
- UI thread + Worker thread
- UI không bị đóng băng

**2. Resource Sharing:**
- Dễ chia sẻ dữ liệu (cùng address space)

**3. Economy (Tiết kiệm):**
- Tạo thread nhanh hơn process
- Context switch nhẹ hơn

**4. Scalability:**
- Tận dụng multi-core

### 2.2.2. Hiện thực

**A. User-level Threads:**
- Quản lý bởi thư viện (pthreads, Java threads)
- Kernel không biết
- Nhanh nhưng 1 thread block → Toàn process block

**B. Kernel-level Threads:**
- Quản lý bởi OS
- Chậm hơn nhưng linh hoạt
- 1 thread block → Thread khác vẫn chạy

**C. Hybrid:**
- Kết hợp cả hai (M:N model)

**Ví dụ code (Pthreads):**
```c
#include <pthread.h>

void* worker(void* arg) {
    printf("Thread running\n");
    return NULL;
}

int main() {
    pthread_t tid;
    pthread_create(&tid, NULL, worker, NULL);
    pthread_join(tid, NULL);
    return 0;
}
```

## 2.3. TRUYỀN THÔNG GIỮA CÁC TIẾN TRÌNH (IPC)

**Inter-Process Communication (IPC):**

**1. Shared Memory:**
- Process chia sẻ vùng nhớ
- Nhanh
- Cần đồng bộ

```c
// POSIX Shared Memory
shm_fd = shm_open("/myshm", O_CREAT | O_RDWR, 0666);
ptr = mmap(0, SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);
```

**2. Message Passing:**
- Gửi/nhận message
- An toàn hơn
- Chậm hơn

**a) Pipe:**
```bash
ls | grep txt  # Pipe output của ls vào grep
```

**b) Message Queue:**
```c
msgsnd(msgid, &msg, sizeof(msg), 0);
msgrcv(msgid, &msg, sizeof(msg), 0, 0);
```

**c) Socket:**
- Network communication

**3. Signal:**
- Thông báo sự kiện
```c
kill(pid, SIGTERM);  // Gửi signal
```

**4. Semaphore:**
- Đồng bộ (xem phần sau)

## 2.4. ĐỒNG BỘ HÓA TIẾN TRÌNH

### 2.4.1. Vấn đề tranh chấp tài nguyên

**Race Condition:**

Nhiều process/thread truy xuất dữ liệu dùng chung → Kết quả phụ thuộc thứ tự thực thi.

**Ví dụ:**
```c
int counter = 0;  // Shared variable

// Thread 1:           // Thread 2:
counter++;             counter++;

// counter++ thực chất:
// 1. Load counter → R1
// 2. R1 = R1 + 1
// 3. Store R1 → counter

// Nếu xen kẽ:
T1: Load 0 → R1
T2: Load 0 → R2
T1: R1 = 1
T2: R2 = 1
T1: Store 1 → counter
T2: Store 1 → counter

// Kết quả: counter = 1 (sai! Phải là 2)
```

**Critical Section (Vùng găng):**

Đoạn code truy xuất dữ liệu dùng chung.

**Yêu cầu:**
1. **Mutual Exclusion:** Chỉ 1 process trong CS tại 1 thời điểm
2. **Progress:** Quyết định ai vào CS phải nhanh
3. **Bounded Waiting:** Không đói (starvation)

### 2.4.2. Các giải pháp đồng bộ

**A. Lock (Khóa):**

```c
lock.acquire();
// Critical section
lock.release();
```

**B. Semaphore:**

**Định nghĩa:**

Biến nguyên S với 2 thao tác atomic:
- **wait(S):** S--; nếu S < 0 thì block
- **signal(S):** S++; đánh thức process đang chờ

**Loại:**

**1. Binary Semaphore (Mutex):**
```c
semaphore mutex = 1;

wait(mutex);    // P operation
// Critical section
signal(mutex);  // V operation
```

**2. Counting Semaphore:**
```c
semaphore resources = 5;  // 5 tài nguyên

wait(resources);
// Dùng tài nguyên
signal(resources);
```

**C. Monitor:**

Cấu trúc cấp cao, tự động mutual exclusion.

```java
class Monitor {
    synchronized void method() {
        // Chỉ 1 thread tại 1 thời điểm
    }
}
```

**D. Condition Variables:**

```c
pthread_cond_wait(&cond, &mutex);
pthread_cond_signal(&cond);
```

**Bài toán Producer-Consumer:**

```c
semaphore mutex = 1;
semaphore empty = N;  // N buffer slots
semaphore full = 0;

// Producer:
while (1) {
    item = produce();
    wait(empty);
    wait(mutex);
    buffer[in] = item;
    in = (in + 1) % N;
    signal(mutex);
    signal(full);
}

// Consumer:
while (1) {
    wait(full);
    wait(mutex);
    item = buffer[out];
    out = (out + 1) % N;
    signal(mutex);
    signal(empty);
    consume(item);
}
```

## 2.5. ĐIỀU PHỐI TIẾN TRÌNH (CPU SCHEDULING)

### 2.5.1. Mục tiêu

**1. CPU Utilization:** Tối đa hóa sử dụng CPU
**2. Throughput:** Số process hoàn thành/đơn vị thời gian
**3. Turnaround Time:** Thời gian từ submit → complete
**4. Waiting Time:** Thời gian chờ trong ready queue
**5. Response Time:** Thời gian từ request → response đầu tiên

### 2.5.2. Các giải thuật điều phối

**A. FCFS (First-Come, First-Served):**

**Quy tắc:** Ai đến trước phục vụ trước.

**Ví dụ:**
```
Process  Burst Time
P1       24
P2       3
P3       3

Timeline:
|----P1----|P2|P3|
0         24  27 30

Waiting time:
P1: 0
P2: 24
P3: 27
Average: (0+24+27)/3 = 17
```

**Nhược điểm:** Convoy effect (process ngắn chờ lâu)

**B. SJF (Shortest Job First):**

**Quy tắc:** Process có burst time ngắn nhất được chạy trước.

**Ví dụ:**
```
Process  Burst Time
P1       24
P2       3
P3       3

Timeline:
|P2|P3|-------P1-------|
0   3  6              30

Waiting time:
P1: 6
P2: 0
P3: 3
Average: (6+0+3)/3 = 3
```

**Tối ưu** về average waiting time!

**Nhược điểm:** Starvation (process dài đói)

**C. Priority Scheduling:**

**Quy tắc:** Process có priority cao nhất được chạy.

**Giải pháp starvation:** Aging (tăng priority theo thời gian chờ)

**D. Round Robin (RR):**

**Quy tắc:** Mỗi process được CPU một khoảng thời gian q (time quantum), sau đó chuyển sang process tiếp theo.

**Ví dụ:** q = 4
```
Process  Burst Time
P1       24
P2       3
P3       3

Timeline:
|P1(4)|P2(3)|P3(3)|P1(4)|P1(4)|P1(4)|P1(4)|P1(4)|
```

**Đặc điểm:**
- Fair
- Response time tốt
- Turnaround time phụ thuộc q

**Chọn q:**
- q quá lớn → FCFS
- q quá nhỏ → Context switch overhead

**E. Multilevel Queue:**

Nhiều queue, mỗi queue một priority và algorithm.

```
┌───────────────┐
│ System        │ ← Highest priority, RR
├───────────────┤
│ Interactive   │ ← RR
├───────────────┤
│ Batch         │ ← FCFS
└───────────────┘
```

**F. Multilevel Feedback Queue:**

Process có thể di chuyển giữa các queue (dựa vào hành vi).

### 2.5.3. Vấn đề điều phối luồng

**Scope:**

**1. Process-Contention Scope (PCS):**
- Điều phối thread trong cùng process
- User-level threads

**2. System-Contention Scope (SCS):**
- Điều phối tất cả kernel threads
- Kernel-level threads

---

# CHƯƠNG 3: DEADLOCK

## 3.1. ĐẶC ĐIỂM SỬ DỤNG TÀI NGUYÊN

**Resource (Tài nguyên):**
- CPU, memory, printer, file, ...

**Sử dụng tài nguyên:**
1. **Request:** Yêu cầu
2. **Use:** Sử dụng
3. **Release:** Giải phóng

## 3.2. TÌNH TRẠNG DEADLOCK

**Định nghĩa:**

Deadlock (bế tắc) xảy ra khi các process chờ lẫn nhau, không process nào tiến triển được.

**Ví dụ:**
```
Process P1:
  Lock(A);
  Lock(B);
  ...
  Unlock(B);
  Unlock(A);

Process P2:
  Lock(B);
  Lock(A);
  ...
  Unlock(A);
  Unlock(B);

Timeline:
P1: Lock(A) ✓
P2: Lock(B) ✓
P1: Lock(B) ← Chờ P2 release B
P2: Lock(A) ← Chờ P1 release A
→ Deadlock!
```

**4 điều kiện cần thiết:**

1. **Mutual Exclusion:** Tài nguyên không chia sẻ được
2. **Hold and Wait:** Process giữ tài nguyên và chờ tài nguyên khác
3. **No Preemption:** Không thể cướp tài nguyên
4. **Circular Wait:** Chuỗi vòng process chờ lẫn nhau

**Resource Allocation Graph:**

```
Process: ○
Resource: □

P1 → R1: P1 request R1
R1 → P1: R1 allocated to P1

Deadlock nếu có cycle:
P1 → R1 → P2 → R2 → P1
```

## 3.3. GIẢI PHÁP XỬ LÝ

### 3.3.1. Không xử lý

**Ostrich Algorithm:** Chôn đầu như đà điểu, làm ngơ.

**Lý do:** Deadlock hiếm, overhead cao nếu xử lý.

**Dùng cho:** UNIX, Windows (một phần)

### 3.3.2. Ngăn chặn Deadlock (Prevention)

**Phá vỡ 1 trong 4 điều kiện:**

**1. Phá Mutual Exclusion:**
- Không thể (một số tài nguyên phải exclusive)

**2. Phá Hold and Wait:**
- **Giải pháp:** Request tất cả tài nguyên một lúc
```c
Lock(A, B, C);  // Atomic
...
Unlock(A, B, C);
```
- **Nhược điểm:** Lãng phí, starvation

**3. Phá No Preemption:**
- **Giải pháp:** Cho phép cướp tài nguyên
- **Nhược điểm:** Phức tạp, không áp dụng được cho tất cả

**4. Phá Circular Wait:**
- **Giải pháp:** Đánh số tài nguyên, luôn request theo thứ tự tăng dần
```c
// R1 < R2 < R3
Lock(R1);
Lock(R2);
Lock(R3);
```

### 3.3.3. Tránh Deadlock (Avoidance)

**Banker's Algorithm (Dijkstra):**

**Ý tưởng:** Chỉ cấp phát nếu hệ thống vẫn ở trạng thái an toàn (safe state).

**Safe state:** Tồn tại chuỗi process có thể hoàn thành.

**Ví dụ:**
```
3 process, 12 tài nguyên

Process  Max  Allocated  Need
P1       10      5        5
P2       4       2        2
P3       9       2        7

Available: 3

Safe sequence: P2 → P1 → P3
- P2: Need 2, Available 3 → Chạy, release 2+3=5
- P1: Need 5, Available 5 → Chạy, release 5+5=10
- P3: Need 7, Available 10 → Chạy
```

**Nhược điểm:** Cần biết max trước, overhead cao.

### 3.3.4. Phát hiện và xử lý Deadlock

**A. Phát hiện (Detection):**

Chạy thuật toán định kỳ để tìm cycle trong Resource Allocation Graph.

**B. Khôi phục (Recovery):**

**1. Process Termination:**
- Kill tất cả process deadlock
- Kill từng process cho đến hết deadlock

**2. Resource Preemption:**
- Cướp tài nguyên từ process
- Rollback process

**Chi phí:** Mất công việc đã làm.

---

# CHƯƠNG 4: QUẢN LÝ BỘ NHỚ

## 4.1. VẤN ĐỀ QUẢN LÝ BỘ NHỚ

**Mục tiêu:**
1. Cấp phát bộ nhớ cho process
2. Bảo vệ (process không truy cập nhầm vùng nhớ của nhau)
3. Tối ưu sử dụng RAM

**Address Binding:**

```
Compile time: Địa chỉ tuyệt đối (hiếm)
Load time:    Địa chỉ có thể thay đổi
Run time:     MMU translate (phổ biến)
```

**MMU (Memory Management Unit):**

Chuyển địa chỉ logic → địa chỉ vật lý.

```
Logical Address (process thấy)
      │
      ▼
    MMU
      │
      ▼
Physical Address (RAM thực)
```

## 4.2. MÔ HÌNH QUẢN LÝ BỘ NHỚ THỰC

### 4.2.1. Cấp phát liên tục

**A. Fixed Partitioning (Phân vùng cố định):**

Chia RAM thành các vùng cố định.

```
┌──────┐
│ OS   │
├──────┤
│ P1   │ 100K
├──────┤
│ P2   │ 200K
├──────┤
│ P3   │ 300K
└──────┘
```

**Nhược điểm:** Internal fragmentation (lãng phí trong vùng)

**B. Dynamic Partitioning (Phân vùng động):**

Cấp phát đúng kích thước process cần.

**Vấn đề:** External fragmentation (mảnh vỡ ngoài)

**Giải pháp:**

**1. Compaction (Nén):**
Dồn các process về một đầu.

**2. Placement Algorithms:**

**a) First Fit:** Chọn vùng trống đầu tiên đủ lớn
- Nhanh

**b) Best Fit:** Chọn vùng trống nhỏ nhất đủ lớn
- Tiết kiệm nhưng chậm, tạo mảnh nhỏ

**c) Worst Fit:** Chọn vùng trống lớn nhất
- Tạo mảnh lớn (dễ dùng lại)

### 4.2.2. Cấp phát không liên tục

**A. Paging (Phân trang):**

**Ý tưởng:** Chia bộ nhớ thành các **page** (logic) và **frame** (physical) cùng kích thước.

**Kích thước page:** 4KB (thông thường)

**Page Table:** Ánh xạ page → frame

```
Logical Address:
┌─────────┬────────┐
│Page No. │ Offset │
└─────────┴────────┘
     │
     ▼ (Page Table)
Physical Address:
┌──────────┬────────┐
│Frame No. │ Offset │
└──────────┴────────┘
```

**Ví dụ:**
```
Page size = 4KB = 2^12 bytes
Logical address = 8192 (decimal) = 0x2000

Logical: Page 2, Offset 0
Page Table: Page 2 → Frame 5
Physical: Frame 5, Offset 0 = 5 × 4096 + 0 = 20480
```

**Ưu điểm:**
- Không external fragmentation
- Dễ cấp phát

**Nhược điểm:**
- Internal fragmentation (page cuối)
- Page table lớn

**B. Segmentation (Phân đoạn):**

Chia chương trình theo logic: code, data, stack.

**Segment Table:**
```
Segment  Base  Limit
Code     1000  500
Data     2000  300
Stack    3000  200
```

**Logical Address:**
```
┌──────────┬────────┐
│Segment # │ Offset │
└──────────┴────────┘
```

**Ưu điểm:** Phản ánh cấu trúc logic

**Nhược điểm:** External fragmentation

**C. Segmentation + Paging:**

Kết hợp cả hai (x86 cũ).

## 4.3. MÔ HÌNH QUẢN LÝ BỘ NHỚ ẢO

### 4.3.1. Đặc điểm

**Virtual Memory:** Cho phép process lớn hơn RAM vật lý.

**Ý tưởng:** Chỉ load page cần thiết vào RAM, còn lại ở disk.

**Demand Paging:**
- Load page khi cần (on demand)
- Không load toàn bộ chương trình

**Page Fault:**

Khi truy cập page không có trong RAM:
```
1. CPU trap to OS
2. OS tìm page trên disk
3. Load page vào frame trống
4. Cập nhật page table
5. Restart instruction
```

**Performance:**

```
Effective Access Time = (1-p) × Memory Access + p × Page Fault Time

p: Page fault rate
Memory Access: ~100ns
Page Fault Time: ~8ms (đọc disk)

Ví dụ: p = 0.001 (1 fault / 1000 access)
EAT = 0.999 × 100ns + 0.001 × 8ms
    ≈ 8.1 μs (chậm hơn 80 lần!)
```

### 4.3.2. Phân trang theo yêu cầu

**Page Replacement Algorithms:**

Khi RAM đầy, phải chọn page để thay thế (swap out).

**A. FIFO (First-In, First-Out):**

Thay thế page cũ nhất.

**Ví dụ:**
```
Reference string: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
Frames: 3

Timeline:
7 → [7] - - (fault)
0 → [7, 0] - (fault)
1 → [7, 0, 1] (fault)
2 → [2, 0, 1] (fault, replace 7)
0 → [2, 0, 1] (hit)
3 → [2, 3, 1] (fault, replace 0)
...

Faults: 15
```

**Belady's Anomaly:** Tăng frame có thể tăng fault!

**B. Optimal (OPT):**

Thay thế page sẽ không dùng lâu nhất (không thực tế, chỉ là lý thuyết).

**C. LRU (Least Recently Used):**

Thay thế page chưa dùng lâu nhất.

**Ví dụ:**
```
Reference: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
Frames: 3

7 → [7] - -
0 → [7, 0] -
1 → [7, 0, 1]
2 → [2, 0, 1] (replace 7, vì 7 chưa dùng lâu nhất)
0 → [2, 0, 1] (hit)
3 → [2, 0, 3] (replace 1)
...
```

**Hiện thực LRU:**
- **Counter:** Gắn timestamp mỗi page
- **Stack:** Dùng stack, page dùng gần nhất ở đỉnh

**D. Clock (Second Chance):**

Cải tiến FIFO, dùng reference bit.

**E. LFU (Least Frequently Used):**

Thay thế page dùng ít nhất.

**Thrashing:**

Khi process liên tục page fault → CPU idle (chờ I/O).

**Nguyên nhân:** Quá nhiều process, RAM không đủ.

**Giải pháp:**
- Giảm multiprogramming degree
- Tăng RAM
- Working Set Model

---

# CHƯƠNG 5: QUẢN LÝ HỆ THỐNG FILE

## 5.1. FILE VÀ THƯ MỤC

### 5.1.1. Ý nghĩa

**File:** Tập hợp dữ liệu có tên, lưu trữ lâu dài.

**Thư mục (Directory):** Tổ chức file theo cây.

### 5.1.2. Các khái niệm

**Thuộc tính file:**
- Name, Type, Location
- Size, Protection, Time

**File Types:**
- Regular file: .txt, .exe, .jpg
- Directory
- Special file: /dev/sda (device)

### 5.1.3. Các thao tác với file

- Create, Delete
- Open, Close
- Read, Write
- Seek (di chuyển file pointer)

**File Descriptor / Handle:**

Số nguyên đại diện file đang mở.

```c
int fd = open("file.txt", O_RDONLY);
read(fd, buffer, size);
close(fd);
```

### 5.1.4. Thư mục

**Cấu trúc:**

**A. Single-Level:**
```
/ (root)
├─ file1
├─ file2
└─ file3
```

**B. Two-Level:**
```
/ (root)
├─ user1
│  ├─ file1
│  └─ file2
└─ user2
   └─ file3
```

**C. Tree (Hierarchical):**
```
/
├─ home
│  ├─ user1
│  │  └─ documents
│  │     └─ file.txt
│  └─ user2
└─ etc
   └─ config.conf
```

**Đường dẫn:**
- **Absolute:** /home/user1/documents/file.txt
- **Relative:** documents/file.txt (từ /home/user1)

## 5.2. HIỆN THỰC HỆ THỐNG FILE

### 5.2.1. Cấp phát liên tục (Contiguous Allocation)

**Ý tưởng:** File chiếm các block liên tiếp trên đĩa.

```
File A: Block 0-9 (10 blocks)
File B: Block 10-14 (5 blocks)
```

**Ưu điểm:**
- Đơn giản
- Truy xuất nhanh (sequential & random)

**Nhược điểm:**
- External fragmentation
- Khó mở rộng file

### 5.2.2. Cấp phát dùng danh sách liên kết (Linked Allocation)

**Ý tưởng:** Mỗi block chứa pointer đến block tiếp theo.

```
File A:
Block 0 → Block 5 → Block 7 → NULL

Directory:
File A: Start = 0, Length = 3
```

**Ưu điểm:**
- Không external fragmentation
- Dễ mở rộng

**Nhược điểm:**
- Chỉ sequential access (không random)
- Pointer chiếm chỗ
- Không tin cậy (1 pointer hỏng → mất file)

### 5.2.3. Bảng FAT (File Allocation Table)

**Ý tưởng:** Tách pointer thành bảng riêng.

```
FAT:
0 → 5
5 → 7
7 → EOF

Directory:
File A: Start = 0
```

**Ưu điểm:**
- Random access
- Bảng FAT trong RAM → Nhanh

**Nhược điểm:**
- Bảng FAT lớn với đĩa lớn

**Dùng:** FAT12, FAT16, FAT32

### 5.2.4. Cấp phát dùng index (Indexed Allocation)

**Ý tưởng:** Mỗi file có 1 index block chứa danh sách block dữ liệu.

```
File A:
Index Block: [2, 5, 9, 11]

Directory:
File A: Index = 10
```

**Ưu điểm:**
- Random access
- Không fragmentation

**Nhược điểm:**
- Lãng phí index block (file nhỏ)

**Multi-level Index:**

File lớn → Index block chứa pointer đến index block khác.

### 5.2.5. I-node (UNIX)

**I-node (Index node):** Cấu trúc chứa metadata và pointer đến block dữ liệu.

```
I-node:
- File size, owner, permissions, timestamps
- Direct pointers (10): Trỏ trực tiếp block
- Single indirect: Trỏ đến block chứa pointers
- Double indirect
- Triple indirect
```

**Ưu điểm:**
- Linh hoạt với file nhỏ và lớn
- Tiết kiệm

### 5.2.6. NTFS (New Technology File System)

**Windows NT trở đi.**

**Đặc điểm:**
- MFT (Master File Table): Mỗi file có 1 MFT entry
- Journaling: Ghi log trước khi thay đổi (phục hồi)
- Compression, Encryption
- Large file support (16 EB)
- ACL (Access Control List)

**MFT Entry:**
```
- File attributes
- Timestamps
- Data (nhỏ: trong MFT, lớn: pointer)
- Security descriptor
```

### 5.2.7. Quản lý các vùng trống trên đĩa

**A. Bitmap:**

Mỗi block: 1 bit (0 = free, 1 = allocated)

```
Disk: 16 blocks
Bitmap: 0110 1100 0000 0011

Block 0: Free
Block 1: Allocated
...
```

**B. Linked List:**

Danh sách liên kết các block trống.

**C. Grouping:**

Block đầu chứa danh sách n block trống, block thứ n trỏ đến nhóm tiếp theo.

## 5.3. HỆ THỐNG FILE TRONG MS-DOS

**FAT12/FAT16:**

**Cấu trúc đĩa:**
```
┌──────────────┐
│ Boot Sector  │ ← MBR
├──────────────┤
│     FAT 1    │
├──────────────┤
│     FAT 2    │ (backup)
├──────────────┤
│ Root Dir     │
├──────────────┤
│ Data Area    │
└──────────────┘
```

**Giới hạn:**
- FAT16: Max 2GB partition (4GB với cluster 64KB)
- 8.3 filename (DOS)

---

# CHƯƠNG 6: QUẢN LÝ NHẬP XUẤT

## 6.1. NGUYÊN LÝ PHẦN CỨNG NHẬP/XUẤT

### 6.1.1. Thiết bị nhập/xuất

**Phân loại:**

**A. Theo tốc độ:**
- Low speed: Keyboard, mouse
- Medium: Printer
- High: Disk, network

**B. Theo loại:**
- Block device: Disk (đọc/ghi block)
- Character device: Keyboard (đọc/ghi ký tự)

### 6.1.2. Bộ điều khiển thiết bị (Device Controller)

**Chức năng:**
- Giao tiếp giữa CPU và thiết bị
- Chuyển đổi tín hiệu
- Buffering

**Ví dụ:** Disk controller, GPU

### 6.1.3. Các thanh ghi nhập/xuất

**Device Controller có:**
- **Status Register:** Trạng thái thiết bị (busy, ready, error)
- **Command Register:** Lệnh cho thiết bị
- **Data Register:** Dữ liệu

**Memory-Mapped I/O:**

Thanh ghi thiết bị ánh xạ vào không gian địa chỉ bộ nhớ.

```
Địa chỉ 0xFF00: Status Register của thiết bị X
```

**Port-Mapped I/O:**

Thanh ghi có không gian địa chỉ riêng, dùng lệnh IN/OUT.

```asm
IN AL, 0x60   ; Đọc từ port 0x60 (keyboard)
OUT 0x60, AL  ; Ghi vào port 0x60
```

### 6.1.4. Kỹ thuật DMA

**Direct Memory Access:**

DMA controller truyền dữ liệu trực tiếp giữa thiết bị và RAM, không qua CPU.

**Quy trình:**
```
1. CPU setup DMA:
   - Source address (thiết bị)
   - Destination address (RAM)
   - Count (số byte)
2. DMA thực hiện transfer
3. DMA gửi interrupt khi xong
```

**Ưu điểm:** Giải phóng CPU

### 6.1.5. Ngắt (Interrupt)

**Interrupt Request (IRQ):**

Thiết bị gửi tín hiệu IRQ khi cần CPU xử lý.

**Quy trình xử lý ngắt:**
```
1. Device gửi IRQ
2. CPU hoàn thành instruction hiện tại
3. Save context (registers, PC)
4. Jump to ISR (Interrupt Service Routine)
5. ISR xử lý
6. Restore context
7. Resume
```

**Interrupt Vector Table:**

Bảng ánh xạ IRQ → ISR address.

```
IRQ 0: Timer
IRQ 1: Keyboard
IRQ 6: Floppy
IRQ 14: Primary IDE
...
```

## 6.2. NGUYÊN LÝ PHẦN MỀM NHẬP/XUẤT

### 6.2.1. Mục tiêu

- Độc lập với thiết bị (device independence)
- Đặt tên thống nhất
- Xử lý lỗi
- Buffering

**Layered Structure:**
```
┌────────────────────┐
│ User Process       │
├────────────────────┤
│ Device-Independent │ ← open, close, read, write
│ OS Software        │
├────────────────────┤
│ Device Drivers     │ ← Specific to device
├────────────────────┤
│ Interrupt Handlers │
├────────────────────┤
│ Hardware           │
└────────────────────┘
```

### 6.2.2. Lập trình nhập/xuất

**A. Programmed I/O (Polling):**

CPU liên tục kiểm tra status register.

```c
while (status != READY);  // Busy wait
write_data();
```

**Nhược điểm:** Lãng phí CPU

**B. Interrupt-Driven I/O:**

CPU làm việc khác, thiết bị gửi interrupt khi sẵn sàng.

### 6.2.3. Cơ chế ngắt

**Interrupt Handling:**

```c
void keyboard_isr() {
    char c = inb(KEYBOARD_PORT);
    buffer[head++] = c;
    // Acknowledge interrupt
}
```

**Priority:**

Ngắt có mức ưu tiên:
- NMI (Non-Maskable): Cao nhất (error)
- Maskable: Có thể disable

### 6.2.4. Kỹ thuật DMA

**Scatter-Gather DMA:**

DMA có thể đọc/ghi vào nhiều vùng nhớ không liên tục.

## 6.3. ĐĨA CỨNG

### 6.3.1. Giới thiệu

**Cấu tạo:** (Đã nói ở Chương 1 Kiến trúc máy tính)

- Platter, Track, Sector, Cylinder

**Thời gian truy xuất:**
```
Access Time = Seek Time + Rotational Latency + Transfer Time
```

- **Seek Time:** Di chuyển head đến track (3-10ms)
- **Rotational Latency:** Chờ sector quay đến (0-5ms)
- **Transfer Time:** Đọc/ghi dữ liệu (~μs)

### 6.3.2. Định dạng đĩa

**Low-level format:**
- Chia track thành sector
- Thêm preamble, ECC

**Partitioning:**
- Chia đĩa thành partition

**High-level format:**
- Tạo file system (NTFS, ext4, ...)

### 6.3.3. Các thuật toán điều phối đĩa

**Disk Scheduling:** Chọn request nào xử lý trước để giảm seek time.

**A. FCFS (First-Come, First-Served):**

Theo thứ tự yêu cầu.

**Ví dụ:**
```
Queue: 98, 183, 37, 122, 14, 124, 65, 67
Head start: 53

Total movement:
|53-98| + |98-183| + |183-37| + ... = 640 cylinders
```

**B. SSTF (Shortest Seek Time First):**

Chọn request gần head nhất.

```
Head: 53
Queue: 98, 183, 37, 122, 14, 124, 65, 67

Sequence: 53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Total: 236 cylinders
```

**Nhược điểm:** Starvation

**C. SCAN (Elevator Algorithm):**

Head di chuyển qua lại đầu-cuối đĩa, phục vụ request trên đường đi.

```
Head: 53, Direction: →

Sequence: 53 → 65 → 67 → 98 → 122 → 124 → 183 (đến cuối) → 37 → 14
Total: 236 cylinders
```

**D. C-SCAN (Circular SCAN):**

Chỉ phục vụ khi đi một chiều, về đầu không phục vụ.

```
Sequence: 53 → 65 → 67 → 98 → 122 → 124 → 183 (về 0) → 14 → 37
```

**E. LOOK:**

Giống SCAN nhưng chỉ đến request cuối cùng, không đến đầu/cuối đĩa.

**F. C-LOOK:**

Giống C-SCAN + LOOK.

**So sánh:**

| Algorithm | Fairness | Performance | Starvation |
|-----------|----------|-------------|------------|
| FCFS      | Tốt      | Xấu         | Không      |
| SSTF      | Xấu      | Tốt         | Có         |
| SCAN      | Tốt      | Tốt         | Không      |
| C-SCAN    | Rất tốt  | Tốt         | Không      |

---

# KẾT LUẬN TOÀN BỘ MÔN HỆ ĐIỀU HÀNH

Đã trình bày đầy đủ 6 chương:
1. **Tổng quan:** Khái niệm, chức năng, lịch sử
2. **Process & Thread:** Quản lý, scheduling, IPC, đồng bộ
3. **Deadlock:** Phòng tránh, phát hiện, xử lý
4. **Memory:** Paging, segmentation, virtual memory
5. **File System:** Tổ chức, cấp phát, FAT, NTFS, i-node
6. **I/O:** Interrupt, DMA, disk scheduling

## BÀI TẬP TỔNG HỢP

**1.** So sánh process và thread.
**2.** Giải thích race condition và cách khắc phục.
**3.** Producer-Consumer với semaphore.
**4.** So sánh FCFS, SJF, RR scheduling.
**5.** 4 điều kiện Deadlock và cách phá vỡ.
**6.** Banker's Algorithm với ví dụ cụ thể.
**7.** So sánh Paging và Segmentation.
**8.** Page Replacement: FIFO, LRU, Optimal.
**9.** So sánh FAT, NTFS, i-node.
**10.** Disk Scheduling: FCFS, SSTF, SCAN.
