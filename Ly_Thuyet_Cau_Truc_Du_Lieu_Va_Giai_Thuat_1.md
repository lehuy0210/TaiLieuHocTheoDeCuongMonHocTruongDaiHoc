# TÀI LIỆU LÝ THUYẾT VÀ ỨNG DỤNG THỰC TẾ
## CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT 1

---

## MỤC LỤC

1. [Chương 1: Danh Sách](#chương-1-danh-sách)
2. [Chương 2: Xếp Thứ Tự - Tìm Kiếm](#chương-2-xếp-thứ-tự---tìm-kiếm)
3. [Chương 3: Cây](#chương-3-cây)
4. [Chương 4: Bảng Băm](#chương-4-bảng-băm)
5. [Chương 5: B-Cây](#chương-5-b-cây)

---

## CHƯƠNG 1: DANH SÁCH

### 1.1. DANH SÁCH ĐẶC (ARRAY LIST)

#### **Lý thuyết:**

**Định nghĩa:**
- Danh sách đặc là cấu trúc dữ liệu lưu trữ các phần tử liên tiếp trong bộ nhớ
- Các phần tử có thể truy cập trực tiếp thông qua chỉ số (index)
- Kích thước cố định hoặc có thể thay đổi (dynamic array)

**Khai báo cấu trúc:**
```cpp
#define MAX_SIZE 100

struct ArrayList {
    int data[MAX_SIZE];
    int size;  // Số phần tử hiện tại
};
```

**Các thao tác cơ bản:**

1. **Khởi tạo danh sách rỗng:** O(1)
2. **Thêm phần tử:**
   - Thêm vào cuối: O(1)
   - Thêm vào vị trí bất kỳ: O(n)
3. **Xóa phần tử:** O(n)
4. **Tìm kiếm:** O(n)
5. **Truy cập phần tử:** O(1)

**Ưu điểm:**
- Truy cập ngẫu nhiên nhanh O(1)
- Đơn giản, dễ hiểu và cài đặt
- Tiết kiệm bộ nhớ (không cần lưu con trỏ)

**Nhược điểm:**
- Kích thước cố định (nếu dùng mảng tĩnh)
- Thao tác chèn/xóa tốn kém O(n)
- Lãng phí bộ nhớ nếu không sử dụng hết

#### **Ứng dụng thực tế:**

1. **Quản lý danh sách sinh viên:**
   ```cpp
   struct Student {
       int id;
       string name;
       float gpa;
   };
   Student students[100];
   ```

2. **Lưu trữ điểm số trong game:**
   - Bảng xếp hạng điểm cao
   - Lịch sử điểm của người chơi

3. **Buffer/Cache:**
   - Lưu trữ dữ liệu tạm thời
   - Hàng đợi in ấn

4. **Xử lý ảnh:**
   - Ma trận pixel
   - Bộ lọc ảnh

---

### 1.2. DANH SÁCH LIÊN KẾT ĐỠN (SINGLY LINKED LIST)

#### **Lý thuyết:**

**Định nghĩa:**
- Cấu trúc dữ liệu động gồm các node
- Mỗi node chứa dữ liệu và con trỏ trỏ đến node tiếp theo
- Node cuối cùng trỏ đến NULL

**Khai báo cấu trúc:**
```cpp
struct Node {
    int data;
    Node* next;
};

struct LinkedList {
    Node* head;
    int size;
};
```

**Các thao tác cơ bản:**

1. **Thêm node:**
   - Thêm vào đầu: O(1)
   - Thêm vào cuối: O(n)
   - Thêm vào vị trí bất kỳ: O(n)

2. **Xóa node:**
   - Xóa đầu: O(1)
   - Xóa cuối: O(n)
   - Xóa vị trí bất kỳ: O(n)

3. **Tìm kiếm:** O(n)

4. **Duyệt danh sách:** O(n)

**Ưu điểm:**
- Kích thước động, không lãng phí bộ nhớ
- Thêm/xóa đầu danh sách rất nhanh O(1)
- Không cần xác định kích thước trước

**Nhược điểm:**
- Không truy cập trực tiếp, phải duyệt tuần tự
- Tốn bộ nhớ cho con trỏ
- Khó debug hơn array

#### **Ứng dụng thực tế:**

1. **Trình duyệt web:**
   - Lịch sử duyệt web (back/forward)
   - Quản lý tab

2. **Trình phát nhạc:**
   - Danh sách phát (playlist)
   - Chuyển bài tiếp theo/trước đó

3. **Hệ điều hành:**
   - Quản lý tiến trình
   - Cấp phát bộ nhớ động

4. **Ứng dụng văn phòng:**
   - Undo/Redo operations
   - Danh sách gần đây (recent files)

---

### 1.3. DANH SÁCH LIÊN KẾT VÒNG (CIRCULAR LINKED LIST)

#### **Lý thuyết:**

**Định nghĩa:**
- Tương tự danh sách liên kết đơn
- Node cuối cùng trỏ về node đầu tiên (tạo thành vòng)

**Đặc điểm:**
- Có thể duyệt vòng lặp liên tục
- Không có điểm kết thúc (NULL)

**Ưu điểm:**
- Duyệt từ bất kỳ node nào
- Tiện lợi cho các ứng dụng vòng lặp

#### **Ứng dụng thực tế:**

1. **Game nhiều người chơi:**
   - Xác định lượt chơi (turn-based game)
   - Round-robin scheduling

2. **Trình chiếu:**
   - Slideshow tự động lặp
   - Carousel hình ảnh

3. **Hệ điều hành:**
   - CPU scheduling (Round Robin)
   - Phân phối tài nguyên

---

### 1.4. DANH SÁCH LIÊN KẾT KÉP (DOUBLY LINKED LIST)

#### **Lý thuyết:**

**Định nghĩa:**
- Mỗi node có 2 con trỏ: next và prev
- Có thể duyệt cả 2 chiều (tiến và lùi)

**Khai báo cấu trúc:**
```cpp
struct DNode {
    int data;
    DNode* next;
    DNode* prev;
};

struct DoublyLinkedList {
    DNode* head;
    DNode* tail;
    int size;
};
```

**Ưu điểm:**
- Duyệt 2 chiều
- Xóa node dễ dàng hơn (có prev)
- Thêm/xóa cả đầu và cuối đều O(1)

**Nhược điểm:**
- Tốn bộ nhớ hơn (2 con trỏ)
- Phức tạp hơn trong cài đặt

#### **Ứng dụng thực tế:**

1. **Trình soạn thảo văn bản:**
   - Di chuyển con trỏ qua lại
   - Undo/Redo với điều hướng 2 chiều

2. **Trình duyệt:**
   - Navigation stack (back/forward)

3. **LRU Cache:**
   - Quản lý cache hiệu quả

---

### 1.5. DANH SÁCH HẠN CHẾ

#### 1.5.1. STACK (Ngăn xếp)

**Lý thuyết:**

**Định nghĩa:**
- Cấu trúc LIFO (Last In First Out)
- Chỉ thao tác ở một đầu (top)

**Các thao tác:**
- Push: Thêm vào đỉnh O(1)
- Pop: Lấy ra khỏi đỉnh O(1)
- Top/Peek: Xem phần tử đỉnh O(1)
- IsEmpty: Kiểm tra rỗng O(1)

**Cài đặt:**
```cpp
struct Stack {
    int data[MAX_SIZE];
    int top;
};
```

**Ứng dụng thực tế:**

1. **Kiểm tra biểu thức:**
   - Kiểm tra ngoặc đúng/sai
   - Chuyển đổi infix sang postfix

2. **Undo mechanism:**
   - Photoshop, Word
   - IDE code editor

3. **Hàm đệ quy:**
   - Call stack của chương trình
   - Quay lui (backtracking)

4. **Duyệt đồ thị:**
   - DFS (Depth First Search)

#### 1.5.2. QUEUE (Hàng đợi)

**Lý thuyết:**

**Định nghĩa:**
- Cấu trúc FIFO (First In First Out)
- Thêm ở cuối (rear), lấy ra ở đầu (front)

**Các thao tác:**
- Enqueue: Thêm vào cuối O(1)
- Dequeue: Lấy ra khỏi đầu O(1)
- Front: Xem phần tử đầu O(1)
- IsEmpty: Kiểm tra rỗng O(1)

**Cài đặt:**
```cpp
struct Queue {
    int data[MAX_SIZE];
    int front, rear;
    int size;
};
```

**Ứng dụng thực tế:**

1. **Hệ thống in ấn:**
   - Print queue/spooler
   - Xử lý theo thứ tự

2. **Hệ điều hành:**
   - Process scheduling
   - Job queue

3. **Mạng máy tính:**
   - Packet queue trong router
   - Message queue

4. **Duyệt đồ thị:**
   - BFS (Breadth First Search)

5. **Call center:**
   - Hàng đợi khách hàng

---

## CHƯƠNG 2: XẾP THỨ TỰ - TÌM KIẾM

### 2.1. CÁC THUẬT TOÁN SẮP XẾP

#### 2.1.1. BUBBLE SORT (Sắp xếp nổi bọt)

**Lý thuyết:**

**Nguyên lý:**
- So sánh và đổi chỗ các cặp phần tử kề nhau
- Phần tử lớn nhất "nổi" lên cuối sau mỗi lượt

**Thuật toán:**
```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```

**Độ phức tạp:**
- Best case: O(n) - đã sắp xếp
- Average case: O(n²)
- Worst case: O(n²)
- Space: O(1)

**Đặc điểm:**
- Stable sort
- In-place sorting
- Đơn giản nhưng chậm

**Ứng dụng thực tế:**
- Giáo dục (học thuật toán)
- Dữ liệu nhỏ, gần như đã sắp xếp
- Kiểm tra xem mảng đã sắp xếp chưa

#### 2.1.2. SELECTION SORT (Sắp xếp chọn)

**Lý thuyết:**

**Nguyên lý:**
- Tìm phần tử nhỏ nhất và đưa về đầu
- Lặp lại với phần còn lại

**Thuật toán:**
```cpp
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        swap(arr[i], arr[minIdx]);
    }
}
```

**Độ phức tạp:**
- Best/Average/Worst case: O(n²)
- Space: O(1)

**Đặc điểm:**
- Không stable (có thể sửa)
- In-place sorting
- Ít swap hơn Bubble Sort

**Ứng dụng thực tế:**
- Sắp xếp khi việc ghi/swap tốn kém
- Dữ liệu nhỏ
- Memory write là expensive operation

#### 2.1.3. INSERTION SORT (Sắp xếp chèn)

**Lý thuyết:**

**Nguyên lý:**
- Xây dựng dần dãy đã sắp xếp
- Chèn từng phần tử vào đúng vị trí

**Thuật toán:**
```cpp
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

**Độ phức tạp:**
- Best case: O(n) - đã sắp xếp
- Average case: O(n²)
- Worst case: O(n²)
- Space: O(1)

**Đặc điểm:**
- Stable sort
- In-place sorting
- Tốt cho dữ liệu gần như đã sắp xếp
- Tốt cho online sorting

**Ứng dụng thực tế:**
- Dữ liệu nhỏ (< 20 phần tử)
- Dữ liệu gần như đã sắp xếp
- Kết hợp với Quick Sort trong thực tế
- Sắp xếp dữ liệu đến từng phần (streaming data)

#### 2.1.4. INTERCHANGE SORT (Đổi chỗ trực tiếp)

**Lý thuyết:**

**Nguyên lý:**
- So sánh từng phần tử với tất cả phần tử còn lại
- Đổi chỗ khi cần thiết

**Thuật toán:**
```cpp
void interchangeSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                swap(arr[i], arr[j]);
            }
        }
    }
}
```

**Độ phức tạp:**
- Best/Average/Worst case: O(n²)
- Space: O(1)

**Ứng dụng thực tế:**
- Giáo dục
- Dữ liệu rất nhỏ
- Ít được sử dụng trong thực tế

#### 2.1.5. HEAP SORT (Sắp xếp vun đống)

**Lý thuyết:**

**Nguyên lý:**
- Sử dụng cấu trúc heap (max-heap hoặc min-heap)
- Xây dựng heap từ mảng
- Lấy phần tử lớn nhất (root) đưa về cuối
- Heapify lại và lặp lại

**Thuật toán:**
```cpp
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extract elements from heap
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
```

**Độ phức tạp:**
- Best/Average/Worst case: O(n log n)
- Space: O(1) - in-place

**Đặc điểm:**
- Không stable
- In-place sorting
- Hiệu quả và ổn định về thời gian

**Ứng dụng thực tế:**

1. **Priority Queue:**
   - Hệ điều hành: Process scheduling
   - Dijkstra's algorithm
   - A* pathfinding

2. **K largest/smallest elements:**
   - Top K trending topics
   - K closest points

3. **Event-driven simulation:**
   - Quản lý sự kiện theo thời gian

4. **Heap memory management:**
   - Cấp phát bộ nhớ động

5. **Statistics:**
   - Median maintenance
   - Running median

#### 2.1.6. QUICK SORT (Sắp xếp nhanh)

**Lý thuyết:**

**Nguyên lý:**
- Divide and Conquer
- Chọn pivot
- Phân hoạch: phần tử < pivot bên trái, > pivot bên phải
- Đệ quy với 2 phần

**Thuật toán:**
```cpp
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

**Độ phức tạp:**
- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n²) - pivot luôn là min/max
- Space: O(log n) - stack recursion

**Cải tiến:**
- Randomized Quick Sort
- 3-way Quick Sort
- Chọn pivot: median-of-three
- Chuyển sang Insertion Sort với mảng nhỏ

**Đặc điểm:**
- Không stable (có thể sửa)
- In-place sorting (gần như)
- Nhanh nhất trong thực tế với dữ liệu lớn
- Cache-friendly

**Ứng dụng thực tế:**

1. **Ngôn ngữ lập trình:**
   - C++ std::sort() sử dụng Introsort (Quick Sort + Heap Sort)
   - Java Arrays.sort() cho primitive types
   - Python's sort (Timsort - cải tiến)

2. **Database systems:**
   - Sắp xếp kết quả query
   - Index building

3. **Numerical computations:**
   - Sorting trong scientific computing

4. **Commercial applications:**
   - Sắp xếp sản phẩm theo giá
   - Ranking systems

5. **System utilities:**
   - Unix sort command

**So sánh Heap Sort vs Quick Sort:**

| Tiêu chí | Heap Sort | Quick Sort |
|----------|-----------|------------|
| Worst case | O(n log n) | O(n²) |
| Average case | O(n log n) | O(n log n) |
| Space | O(1) | O(log n) |
| Stable | No | No |
| Cache performance | Poor | Good |
| Practical speed | Slower | Faster |
| Predictability | Consistent | Variable |

**Khi nào dùng gì:**
- **Quick Sort:** Hầu hết các trường hợp, dữ liệu lớn
- **Heap Sort:** Khi cần đảm bảo O(n log n) worst case, ít bộ nhớ
- **Insertion Sort:** Dữ liệu nhỏ hoặc gần như đã sắp xếp
- **Merge Sort:** Khi cần stable sort

---

### 2.2. TÌM KIẾM

#### 2.2.1. TÌM KIẾM TUẦN TỰ (LINEAR SEARCH)

**Lý thuyết:**

**Nguyên lý:**
- Duyệt từng phần tử từ đầu đến cuối
- So sánh với giá trị cần tìm

**Thuật toán:**
```cpp
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}
```

**Độ phức tạp:**
- Best case: O(1)
- Average case: O(n)
- Worst case: O(n)

**Ứng dụng thực tế:**
- Dữ liệu nhỏ
- Dữ liệu chưa sắp xếp
- Tìm kiếm trong linked list
- Tìm kiếm đơn giản

#### 2.2.2. TÌM KIẾM NHỊ PHÂN (BINARY SEARCH)

**Lý thuyết:**

**Điều kiện:**
- Mảng đã được sắp xếp

**Nguyên lý:**
- So sánh với phần tử giữa
- Loại bỏ một nửa không chứa kết quả
- Lặp lại với nửa còn lại

**Thuật toán (đệ quy):**
```cpp
int binarySearch(int arr[], int left, int right, int key) {
    if (left > right)
        return -1;

    int mid = left + (right - left) / 2;

    if (arr[mid] == key)
        return mid;

    if (arr[mid] > key)
        return binarySearch(arr, left, mid - 1, key);

    return binarySearch(arr, mid + 1, right, key);
}
```

**Thuật toán (vòng lặp):**
```cpp
int binarySearch(int arr[], int n, int key) {
    int left = 0, right = n - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == key)
            return mid;

        if (arr[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}
```

**Độ phức tạp:**
- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)

**Ứng dụng thực tế:**

1. **Dictionary/Từ điển:**
   - Tra từ trong từ điển
   - Tìm kiếm trong phonebook

2. **Database:**
   - Index search
   - B-tree traversal

3. **Version control:**
   - Git bisect (tìm commit lỗi)

4. **Debugging:**
   - Tìm điểm lỗi trong code

5. **Game development:**
   - Collision detection (sorted objects)
   - AI decision trees

---

## CHƯƠNG 3: CÂY

### 3.1. CÁC KHÁI NIỆM CƠ BẢN

**Định nghĩa:**
- Cấu trúc dữ liệu phi tuyến
- Có một nút gốc (root)
- Mỗi nút có 0 hoặc nhiều nút con

**Các khái niệm:**
- **Nút (Node):** Phần tử cơ bản của cây
- **Cạnh (Edge):** Liên kết giữa 2 nút
- **Nút gốc (Root):** Nút đầu tiên, không có cha
- **Nút lá (Leaf):** Nút không có con
- **Nút trong (Internal node):** Nút có ít nhất 1 con
- **Bậc của nút:** Số con của nút đó
- **Bậc của cây:** Bậc lớn nhất của các nút
- **Chiều cao (Height):** Đường đi dài nhất từ root đến leaf
- **Mức (Level):** Khoảng cách từ root (root ở level 0)

### 3.2. CÂY NHỊ PHÂN (BINARY TREE)

**Định nghĩa:**
- Mỗi nút có tối đa 2 con (trái và phải)

**Khai báo:**
```cpp
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
};
```

**Các loại cây nhị phân:**
1. **Full Binary Tree:** Mỗi nút có 0 hoặc 2 con
2. **Complete Binary Tree:** Tất cả mức đều đầy trừ mức cuối
3. **Perfect Binary Tree:** Tất cả mức đều đầy
4. **Balanced Binary Tree:** Height(left) - Height(right) ≤ 1

**Các phép duyệt cây:**

1. **Pre-order (NLR):** Node - Left - Right
```cpp
void preOrder(TreeNode* root) {
    if (root == NULL) return;
    cout << root->data << " ";
    preOrder(root->left);
    preOrder(root->right);
}
```

2. **In-order (LNR):** Left - Node - Right
```cpp
void inOrder(TreeNode* root) {
    if (root == NULL) return;
    inOrder(root->left);
    cout << root->data << " ";
    inOrder(root->right);
}
```

3. **Post-order (LRN):** Left - Right - Node
```cpp
void postOrder(TreeNode* root) {
    if (root == NULL) return;
    postOrder(root->left);
    postOrder(root->right);
    cout << root->data << " ";
}
```

**Ứng dụng:**
- Expression trees (biểu thức toán học)
- Decision trees (AI, Machine Learning)
- File systems (thư mục)

### 3.3. CÂY NHỊ PHÂN TÌM KIẾM (BINARY SEARCH TREE - BST)

**Định nghĩa:**
- Cây nhị phân thỏa mãn:
  - Tất cả nút con trái < nút cha
  - Tất cả nút con phải > nút cha

**Các thao tác:**

1. **Tìm kiếm:** O(h) - h là chiều cao
```cpp
TreeNode* search(TreeNode* root, int key) {
    if (root == NULL || root->data == key)
        return root;

    if (key < root->data)
        return search(root->left, key);

    return search(root->right, key);
}
```

2. **Chèn:** O(h)
```cpp
TreeNode* insert(TreeNode* root, int key) {
    if (root == NULL)
        return new TreeNode(key);

    if (key < root->data)
        root->left = insert(root->left, key);
    else if (key > root->data)
        root->right = insert(root->right, key);

    return root;
}
```

3. **Xóa:** O(h)
- Xóa nút lá: Xóa trực tiếp
- Xóa nút có 1 con: Thay bằng con
- Xóa nút có 2 con: Thay bằng successor/predecessor

**Ưu điểm:**
- Tìm kiếm, chèn, xóa trung bình O(log n)
- Duyệt In-order cho dãy tăng dần

**Nhược điểm:**
- Worst case O(n) khi cây bị lệch
- Cần cân bằng (AVL, Red-Black Tree)

**Ứng dụng thực tế:**

1. **Database indexing:**
   - B-tree (cải tiến từ BST)
   - MySQL, PostgreSQL

2. **File systems:**
   - Directory structures
   - File organization

3. **Networking:**
   - Router tables
   - IP routing

4. **Compiler:**
   - Symbol tables
   - Syntax trees

5. **Autocomplete:**
   - Trie (prefix tree)
   - Search suggestions

---

## CHƯƠNG 4: BẢNG BĂM (HASH TABLE)

### 4.1. CÁC KHÁI NIỆM

**Định nghĩa:**
- Cấu trúc dữ liệu ánh xạ key -> value
- Sử dụng hàm băm để tính chỉ số lưu trữ

**Hàm băm (Hash Function):**
- Chuyển đổi key thành chỉ số của mảng
- Ví dụ: h(key) = key % table_size

**Yêu cầu hàm băm tốt:**
- Tính toán nhanh
- Phân bố đều
- Ít xung đột

**Đụng độ (Collision):**
- Khi 2 key khác nhau có cùng hash value
- Cần phương pháp giải quyết

### 4.2. GIẢI QUYẾT ĐỤNG ĐỘ

#### 4.2.1. NỐI KẾT TRỰC TIẾP (SEPARATE CHAINING)

**Nguyên lý:**
- Mỗi ô của bảng băm là một danh sách liên kết
- Các phần tử bị đụng độ được thêm vào danh sách

**Cài đặt:**
```cpp
struct HashNode {
    int key;
    int value;
    HashNode* next;
};

class HashTable {
private:
    HashNode** table;
    int capacity;

public:
    int hashFunction(int key) {
        return key % capacity;
    }

    void insert(int key, int value) {
        int index = hashFunction(key);
        HashNode* newNode = new HashNode(key, value);

        if (table[index] == NULL) {
            table[index] = newNode;
        } else {
            HashNode* temp = table[index];
            while (temp->next != NULL)
                temp = temp->next;
            temp->next = newNode;
        }
    }
};
```

**Độ phức tạp:**
- Average: O(1)
- Worst: O(n) - tất cả vào 1 chain

**Ưu điểm:**
- Đơn giản
- Không bị đầy (như open addressing)
- Deletion dễ dàng

**Nhược điểm:**
- Tốn bộ nhớ cho con trỏ
- Cache performance kém

#### 4.2.2. NỐI KẾT HỢP NHẤT (OPEN ADDRESSING)

**Các phương pháp:**

1. **Linear Probing:**
   - h(key, i) = (h(key) + i) % table_size
   - Tìm ô trống tiếp theo

2. **Quadratic Probing:**
   - h(key, i) = (h(key) + c1*i + c2*i²) % table_size
   - Giảm clustering

3. **Double Hashing:**
   - h(key, i) = (h1(key) + i*h2(key)) % table_size
   - Sử dụng 2 hàm băm

**Ưu điểm:**
- Không cần con trỏ
- Cache-friendly
- Tốt cho bộ nhớ

**Nhược điểm:**
- Có thể bị đầy
- Deletion phức tạp
- Clustering

**Ứng dụng thực tế:**

1. **Database:**
   - Hash join
   - Hash index

2. **Caching:**
   - LRU cache
   - Redis
   - Memcached

3. **Language implementations:**
   - Python dict
   - JavaScript objects
   - Java HashMap

4. **Security:**
   - Password hashing
   - Digital signatures
   - Blockchain

5. **Deduplication:**
   - Tìm dữ liệu trùng lặp
   - File comparison

---

## CHƯƠNG 5: B-CÂY (B-TREE)

### 5.1. TỔNG QUAN

**Định nghĩa:**
- Cây tìm kiếm cân bằng
- Mỗi nút có thể có nhiều con (không chỉ 2)
- Tối ưu cho hệ thống lưu trữ ngoài (disk)

**Đặc điểm B-Tree bậc m:**
- Mỗi nút có tối đa m con
- Mỗi nút (trừ root) có ít nhất ⌈m/2⌉ con
- Root có ít nhất 2 con (nếu không phải leaf)
- Tất cả leaf ở cùng một mức
- Nút có k con thì có k-1 khóa

**Khái niệm:**
- **Order (m):** Số con tối đa
- **Key:** Giá trị lưu trong nút
- **Child pointer:** Con trỏ tới nút con
- **Leaf node:** Nút lá không có con

### 5.2. CÁC THAO TÁC

#### 5.2.1. TẠO B-CÂY

**Cấu trúc:**
```cpp
struct BTreeNode {
    int* keys;          // Mảng khóa
    BTreeNode** children; // Mảng con trỏ con
    int n;              // Số khóa hiện tại
    bool leaf;          // Là nút lá?
    int t;              // Bậc tối thiểu
};
```

#### 5.2.2. TÌM KIẾM

**Thuật toán:**
```cpp
BTreeNode* search(BTreeNode* root, int key) {
    int i = 0;
    while (i < root->n && key > root->keys[i])
        i++;

    if (i < root->n && key == root->keys[i])
        return root;

    if (root->leaf)
        return NULL;

    return search(root->children[i], key);
}
```

**Độ phức tạp:** O(log n)

#### 5.2.3. CHÈN KHÓA

**Nguyên tắc:**
- Chèn vào nút lá
- Nếu nút đầy, split thành 2 nút
- Đẩy khóa giữa lên cha

**Độ phức tạp:** O(log n)

#### 5.2.4. XÓA KHÓA

**Trường hợp:**
1. Khóa ở nút lá: Xóa trực tiếp
2. Khóa ở nút trong: Thay bằng predecessor/successor
3. Nút thiếu khóa: Borrow từ anh em hoặc merge

**Độ phức tạp:** O(log n)

**Ưu điểm:**
- Cân bằng tự động
- Tối ưu cho I/O disk
- Tìm kiếm, chèn, xóa đều O(log n)
- Giảm số lần truy cập disk

**Nhược điểm:**
- Phức tạp trong cài đặt
- Overhead khi dữ liệu nhỏ

**Ứng dụng thực tế:**

1. **Database systems:**
   - MySQL InnoDB (B+ Tree)
   - PostgreSQL
   - SQLite
   - Index structures

2. **File systems:**
   - NTFS (Windows)
   - HFS+ (macOS)
   - ext4 (Linux)
   - Directory indexing

3. **NoSQL databases:**
   - MongoDB
   - CouchDB
   - Cassandra

4. **Cloud storage:**
   - Amazon S3 indexing
   - Google Cloud Storage

5. **Operating systems:**
   - Memory management
   - Virtual memory

---

## PHỤ LỤC: SO SÁNH CÁC THUẬT TOÁN SẮP XẾP

| Thuật toán | Best | Average | Worst | Space | Stable | Notes |
|------------|------|---------|-------|-------|--------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Chậm, dùng học tập |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Ít swap |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Tốt cho dữ liệu nhỏ |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Ổn định, in-place |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Nhanh nhất thực tế |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Stable, không in-place |

---

## KẾT LUẬN

### Tầm quan trọng của Cấu trúc Dữ liệu và Giải thuật:

1. **Hiệu suất:** Lựa chọn đúng cấu trúc dữ liệu giúp tối ưu thời gian và bộ nhớ
2. **Khả năng mở rộng:** Code có thể xử lý được lượng dữ liệu lớn
3. **Maintainability:** Code dễ đọc, dễ bảo trì
4. **Problem solving:** Rèn luyện tư duy logic và giải quyết vấn đề

### Lời khuyên học tập:

1. **Hiểu lý thuyết:** Nắm vững nguyên lý hoạt động
2. **Thực hành nhiều:** Cài đặt và test các thuật toán
3. **Phân tích độ phức tạp:** Luôn quan tâm Big-O
4. **Áp dụng thực tế:** Nhận biết khi nào dùng cấu trúc nào
5. **Luyện tập:** LeetCode, HackerRank, Codeforces

### Tài nguyên tham khảo:

- **Sách:** Introduction to Algorithms (CLRS)
- **Online:** GeeksforGeeks, VisuAlgo
- **Practice:** LeetCode, HackerRank
- **Video:** MIT OpenCourseWare, YouTube

---

**Biên soạn:** Dựa trên đề cương môn Cấu trúc Dữ liệu và Giải thuật 1
**Trường:** Đại học Mở Thành phố Hồ Chí Minh
**Năm học:** 2024-2025
