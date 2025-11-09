# CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT 2
## Lý thuyết và Ứng dụng Thực tế

---

## MỤC LỤC

1. [Giới thiệu về Thuật giải](#1-giới-thiệu-về-thuật-giải)
2. [Các thuật giải sắp xếp nâng cao](#2-các-thuật-giải-sắp-xếp-nâng-cao)
3. [Các thuật toán đồ thị cơ bản](#3-các-thuật-toán-đồ-thị-cơ-bản)
4. [Tìm đường đi ngắn nhất](#4-tìm-đường-đi-ngắn-nhất)
5. [Cây bao trùm nhỏ nhất](#5-cây-bao-trùm-nhỏ-nhất)

---

## 1. GIỚI THIỆU VỀ THUẬT GIẢI

### 1.1. Khái niệm Thuật giải

**Định nghĩa:**
- Thuật giải (Algorithm) là một tập hợp các bước được xác định rõ ràng để giải quyết một vấn đề cụ thể
- Mỗi bước phải được mô tả chính xác, không mơ hồ
- Thuật giải phải kết thúc sau một số hữu hạn bước

**Đặc điểm của thuật giải tốt:**
- Tính đúng đắn (Correctness)
- Tính hiệu quả (Efficiency)
- Tính rõ ràng (Clarity)
- Tính tổng quát (Generality)

### 1.2. Biểu diễn Thuật giải

**Các cách biểu diễn:**
1. **Ngôn ngữ tự nhiên**: Mô tả bằng lời văn
2. **Sơ đồ khối**: Sử dụng các ký hiệu đồ họa
3. **Mã giả (Pseudocode)**: Gần với ngôn ngữ lập trình nhưng không phụ thuộc cú pháp
4. **Ngôn ngữ lập trình**: C++, Python, Java...

### 1.3. Phân tích Thuật giải

**Độ phức tạp thời gian:**
- Đo lường thời gian thực hiện thuật giải
- Phụ thuộc vào kích thước đầu vào n

**Độ phức tạp không gian:**
- Đo lường bộ nhớ cần thiết
- Bao gồm bộ nhớ cho dữ liệu đầu vào và biến phụ

### 1.4. Ký pháp O (Big-O Notation)

**Định nghĩa:**
Ký pháp O mô tả giới hạn trên của tốc độ tăng trưởng của một hàm

**Các độ phức tạp thường gặp:**
- O(1): Hằng số
- O(log n): Logarit
- O(n): Tuyến tính
- O(n log n): Tuyến tính logarit
- O(n²): Bậc hai
- O(n³): Bậc ba
- O(2ⁿ): Mũ
- O(n!): Giai thừa

**Ví dụ phân tích:**
```cpp
// O(n) - Tuyến tính
for (int i = 0; i < n; i++) {
    cout << i << endl;
}

// O(n²) - Bậc hai
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        cout << i << " " << j << endl;
    }
}
```

### 1.5. Ứng dụng Thực tế

**1. Tối ưu hóa hiệu suất hệ thống:**
- Chọn thuật giải phù hợp giúp giảm thời gian xử lý
- Ví dụ: Sử dụng Binary Search (O(log n)) thay vì Linear Search (O(n)) cho danh sách đã sắp xếp

**2. Phân tích và dự đoán:**
- Dự đoán thời gian xử lý khi dữ liệu tăng lên
- Ví dụ: Ứng dụng xử lý 1000 bản ghi trong 1 giây với O(n), sẽ cần 1000 giây với 1 triệu bản ghi

**3. So sánh các giải pháp:**
- Đánh giá các cách tiếp cận khác nhau
- Chọn giải pháp tối ưu về mặt thời gian và không gian

---

## 2. CÁC THUẬT GIẢI SẮP XẾP NÂNG CAO

### 2.1. Shell Sort

**Lý thuyết:**
- Cải tiến của Insertion Sort
- Chia dãy thành các nhóm con với khoảng cách h (gap)
- Giảm dần h cho đến khi h = 1
- Độ phức tạp: O(n log n) đến O(n²) tùy thuộc vào dãy gap

**Thuật giải:**
```cpp
void shellSort(int arr[], int n) {
    // Bắt đầu với gap lớn, giảm dần
    for (int gap = n/2; gap > 0; gap /= 2) {
        // Insertion sort cho các phần tử cách nhau gap
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
    }
}
```

**Ưu điểm:**
- Nhanh hơn Insertion Sort
- Cài đặt đơn giản
- Không cần bộ nhớ phụ

**Nhược điểm:**
- Hiệu suất phụ thuộc vào dãy gap
- Không ổn định (stable)

**Ứng dụng thực tế:**
1. **Hệ thống nhúng**: Ít bộ nhớ, hiệu quả với dữ liệu vừa phải
2. **Sắp xếp nhanh dữ liệu gần đúng**: Dữ liệu gần như đã sắp xếp
3. **Game development**: Sắp xếp điểm số, ranking

### 2.2. Radix Sort

**Lý thuyết:**
- Sắp xếp không dựa trên so sánh
- Sắp xếp theo từng chữ số (digit)
- Độ phức tạp: O(d × (n + k))
  - d: số chữ số
  - n: số phần tử
  - k: cơ số (base)

**Thuật giải:**
```cpp
// Hàm đếm sort cho Radix Sort
void countingSort(int arr[], int n, int exp) {
    int output[n];
    int count[10] = {0};

    // Đếm số lần xuất hiện
    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    // Tính vị trí
    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    // Xây dựng mảng output
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    // Copy về mảng gốc
    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

void radixSort(int arr[], int n) {
    // Tìm số lớn nhất
    int max = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];

    // Sắp xếp theo từng digit
    for (int exp = 1; max / exp > 0; exp *= 10)
        countingSort(arr, n, exp);
}
```

**Ưu điểm:**
- Rất nhanh với dữ liệu số nguyên
- Ổn định (stable)
- Độ phức tạp tuyến tính trong nhiều trường hợp

**Nhược điểm:**
- Cần bộ nhớ phụ
- Chỉ áp dụng cho số nguyên hoặc chuỗi

**Ứng dụng thực tế:**
1. **Sắp xếp số điện thoại**: 10 chữ số, hiệu quả
2. **Sắp xếp mã bưu điện (ZIP code)**
3. **Sắp xếp số thẻ tín dụng**
4. **Database indexing**: Sắp xếp khóa số nguyên
5. **Sorting IP addresses**: Chia thành 4 phần, mỗi phần 0-255

**Ví dụ ứng dụng - Sắp xếp số điện thoại:**
```cpp
struct PhoneNumber {
    string number;  // "0123456789"
    string name;
};

void sortPhoneNumbers(vector<PhoneNumber>& phones) {
    // Chuyển đổi sang số và sắp xếp bằng Radix Sort
    // Giữ nguyên tính ổn định để bảo toàn thứ tự tên
}
```

### 2.3. Counting Sort

**Lý thuyết:**
- Sắp xếp không dựa trên so sánh
- Đếm số lần xuất hiện của mỗi giá trị
- Độ phức tạp: O(n + k), k là khoảng giá trị

**Thuật giải:**
```cpp
void countingSort(int arr[], int n) {
    // Tìm giá trị max
    int max = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];

    // Mảng đếm
    int* count = new int[max + 1]{0};

    // Đếm
    for (int i = 0; i < n; i++)
        count[arr[i]]++;

    // Tính vị trí
    for (int i = 1; i <= max; i++)
        count[i] += count[i - 1];

    // Xây dựng mảng kết quả
    int* output = new int[n];
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // Copy lại
    for (int i = 0; i < n; i++)
        arr[i] = output[i];

    delete[] count;
    delete[] output;
}
```

**Ứng dụng thực tế:**
1. **Sắp xếp điểm thi**: Điểm từ 0-100
2. **Sắp xếp độ tuổi**: Giá trị nhỏ, hữu hạn
3. **Histogram generation**: Phân tích phân bố dữ liệu

### 2.4. Bucket Sort

**Lý thuyết:**
- Chia dữ liệu vào các bucket (thùng)
- Sắp xếp từng bucket
- Ghép các bucket lại
- Độ phức tạp: O(n + k) trung bình

**Thuật giải:**
```cpp
void bucketSort(float arr[], int n) {
    // Tạo n bucket rỗng
    vector<float> buckets[n];

    // Phân phối vào bucket
    for (int i = 0; i < n; i++) {
        int idx = n * arr[i];
        buckets[idx].push_back(arr[i]);
    }

    // Sắp xếp từng bucket
    for (int i = 0; i < n; i++)
        sort(buckets[i].begin(), buckets[i].end());

    // Ghép lại
    int index = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < buckets[i].size(); j++)
            arr[index++] = buckets[i][j];
}
```

**Ứng dụng thực tế:**
1. **Sắp xếp số thực trong khoảng [0, 1)**
2. **External sorting**: Dữ liệu không fit vào RAM
3. **Parallel sorting**: Mỗi bucket xử lý độc lập
4. **Phân loại khách hàng theo thu nhập**

### 2.5. So sánh các thuật toán sắp xếp

| Thuật toán | Độ phức tạp TB | Độ phức tạp XN | Bộ nhớ | Ổn định | Ứng dụng |
|-----------|---------------|----------------|---------|---------|----------|
| Shell Sort | O(n log n) | O(n²) | O(1) | Không | Dữ liệu vừa |
| Radix Sort | O(d×n) | O(d×n) | O(n+k) | Có | Số nguyên |
| Counting Sort | O(n+k) | O(n+k) | O(k) | Có | Khoảng nhỏ |
| Bucket Sort | O(n+k) | O(n²) | O(n) | Có | Phân bố đều |

---

## 3. CÁC THUẬT TOÁN ĐỒ THỊ CƠ BẢN

### 3.1. Biểu diễn Đồ thị

**3.1.1. Khái niệm:**
- Đồ thị G = (V, E)
  - V: Tập đỉnh (vertices)
  - E: Tập cạnh (edges)
- Có hướng hoặc vô hướng
- Có trọng số hoặc không trọng số

**3.1.2. Ma trận kề (Adjacency Matrix):**

```cpp
class Graph {
private:
    int V;  // Số đỉnh
    int** adj;  // Ma trận kề

public:
    Graph(int vertices) {
        V = vertices;
        adj = new int*[V];
        for (int i = 0; i < V; i++) {
            adj[i] = new int[V];
            for (int j = 0; j < V; j++)
                adj[i][j] = 0;
        }
    }

    void addEdge(int u, int v, int weight = 1) {
        adj[u][v] = weight;
        // Nếu đồ thị vô hướng:
        // adj[v][u] = weight;
    }
};
```

**Ưu điểm:**
- Kiểm tra cạnh nhanh: O(1)
- Phù hợp với đồ thị dày đặc

**Nhược điểm:**
- Tốn bộ nhớ: O(V²)
- Duyệt láng giềng: O(V)

**3.1.3. Danh sách kề (Adjacency List):**

```cpp
class Graph {
private:
    int V;
    vector<pair<int, int>>* adj;  // pair<đỉnh, trọng số>

public:
    Graph(int vertices) {
        V = vertices;
        adj = new vector<pair<int, int>>[V];
    }

    void addEdge(int u, int v, int weight = 1) {
        adj[u].push_back({v, weight});
        // Nếu vô hướng:
        // adj[v].push_back({u, weight});
    }
};
```

**Ưu điểm:**
- Tiết kiệm bộ nhớ: O(V + E)
- Duyệt láng giềng nhanh: O(degree(v))

**Nhược điểm:**
- Kiểm tra cạnh chậm: O(V)

### 3.2. Tìm kiếm theo chiều rộng (BFS)

**Lý thuyết:**
- Duyệt từng mức (level)
- Sử dụng hàng đợi (Queue)
- Tìm đường đi ngắn nhất trên đồ thị không trọng số
- Độ phức tạp: O(V + E)

**Thuật giải:**
```cpp
void BFS(int start) {
    vector<bool> visited(V, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << " ";

        // Duyệt các đỉnh kề
        for (auto& edge : adj[u]) {
            int v = edge.first;
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}
```

**Tìm đường đi ngắn nhất:**
```cpp
vector<int> shortestPath(int start, int end) {
    vector<bool> visited(V, false);
    vector<int> parent(V, -1);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (u == end) break;

        for (auto& edge : adj[u]) {
            int v = edge.first;
            if (!visited[v]) {
                visited[v] = true;
                parent[v] = u;
                q.push(v);
            }
        }
    }

    // Truy vết đường đi
    vector<int> path;
    for (int v = end; v != -1; v = parent[v])
        path.push_back(v);
    reverse(path.begin(), path.end());

    return path;
}
```

**Ứng dụng thực tế:**

**1. Mạng xã hội:**
- Tìm bạn bè gợi ý (friends of friends)
- Đo độ phân cách (six degrees of separation)
- Tìm người có ảnh hưởng nhất

```cpp
// Tìm tất cả bạn bè cách 2 bước
vector<int> findFriendsOfFriends(int userId) {
    vector<int> friends;
    vector<int> distance(V, -1);
    queue<int> q;

    distance[userId] = 0;
    q.push(userId);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (distance[u] == 2) {
            friends.push_back(u);
            continue;
        }

        for (auto& edge : adj[u]) {
            int v = edge.first;
            if (distance[v] == -1) {
                distance[v] = distance[u] + 1;
                q.push(v);
            }
        }
    }

    return friends;
}
```

**2. Web Crawler:**
- Duyệt web theo mức độ ưu tiên
- Tìm tất cả trang trong một domain

**3. GPS Navigation:**
- Tìm đường đi qua ít ngã tư nhất

**4. Puzzle solving:**
- Giải Rubik, 8-puzzle
- Tìm số bước ít nhất

**5. Network Broadcasting:**
- Phát tín hiệu đến tất cả node

### 3.3. Tìm kiếm theo chiều sâu (DFS)

**Lý thuyết:**
- Đi sâu vào từng nhánh
- Sử dụng ngăn xếp (Stack) hoặc đệ quy
- Độ phức tạp: O(V + E)

**Thuật giải (Đệ quy):**
```cpp
void DFSUtil(int u, vector<bool>& visited) {
    visited[u] = true;
    cout << u << " ";

    for (auto& edge : adj[u]) {
        int v = edge.first;
        if (!visited[v])
            DFSUtil(v, visited);
    }
}

void DFS(int start) {
    vector<bool> visited(V, false);
    DFSUtil(start, visited);
}
```

**Thuật giải (Stack):**
```cpp
void DFS_Stack(int start) {
    vector<bool> visited(V, false);
    stack<int> s;

    s.push(start);

    while (!s.empty()) {
        int u = s.top();
        s.pop();

        if (!visited[u]) {
            visited[u] = true;
            cout << u << " ";

            for (auto& edge : adj[u]) {
                int v = edge.first;
                if (!visited[v])
                    s.push(v);
            }
        }
    }
}
```

**Phát hiện chu trình:**
```cpp
bool hasCycleUtil(int u, vector<bool>& visited, vector<bool>& recStack) {
    visited[u] = true;
    recStack[u] = true;

    for (auto& edge : adj[u]) {
        int v = edge.first;

        if (!visited[v]) {
            if (hasCycleUtil(v, visited, recStack))
                return true;
        }
        else if (recStack[v])
            return true;
    }

    recStack[u] = false;
    return false;
}

bool hasCycle() {
    vector<bool> visited(V, false);
    vector<bool> recStack(V, false);

    for (int i = 0; i < V; i++)
        if (!visited[i])
            if (hasCycleUtil(i, visited, recStack))
                return true;

    return false;
}
```

**Sắp xếp topo (Topological Sort):**
```cpp
void topologicalSortUtil(int u, vector<bool>& visited, stack<int>& s) {
    visited[u] = true;

    for (auto& edge : adj[u]) {
        int v = edge.first;
        if (!visited[v])
            topologicalSortUtil(v, visited, s);
    }

    s.push(u);
}

vector<int> topologicalSort() {
    stack<int> s;
    vector<bool> visited(V, false);

    for (int i = 0; i < V; i++)
        if (!visited[i])
            topologicalSortUtil(i, visited, s);

    vector<int> result;
    while (!s.empty()) {
        result.push_back(s.top());
        s.pop();
    }

    return result;
}
```

**Ứng dụng thực tế:**

**1. Phát hiện chu trình:**
- Deadlock detection
- Kiểm tra phụ thuộc vòng trong build system

**2. Sắp xếp topo:**
- Lập lịch công việc có ràng buộc
- Build dependencies (Makefile)
- Course prerequisites

```cpp
// Ví dụ: Lập lịch môn học
struct Course {
    string name;
    vector<int> prerequisites;  // Các môn tiên quyết
};

vector<string> planCourses(vector<Course>& courses) {
    // Xây dựng đồ thị phụ thuộc
    // Sắp xếp topo để tìm thứ tự học
}
```

**3. Tìm thành phần liên thông:**
```cpp
int countConnectedComponents() {
    vector<bool> visited(V, false);
    int count = 0;

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            DFSUtil(i, visited);
            count++;
        }
    }

    return count;
}
```

**4. Maze solving:**
- Tìm đường ra khỏi mê cung
- Path finding in games

**5. Web scraping:**
- Duyệt toàn bộ trang web
- Phát hiện broken links

**6. File system traversal:**
- Tìm kiếm file
- Tính dung lượng thư mục

### 3.4. So sánh BFS và DFS

| Tiêu chí | BFS | DFS |
|----------|-----|-----|
| Cấu trúc dữ liệu | Queue | Stack/Recursion |
| Bộ nhớ | O(V) | O(h) - h là chiều cao |
| Đường đi ngắn nhất | Có (không trọng số) | Không |
| Ứng dụng | Mạng xã hội, GPS | Chu trình, Topo sort |
| Hoàn chỉnh | Có | Không (với đồ thị vô hạn) |

---

## 4. TÌM ĐƯỜNG ĐI NGẮN NHẤT

### 4.1. Bài toán Đường đi ngắn nhất

**Định nghĩa:**
- Tìm đường đi có tổng trọng số nhỏ nhất từ đỉnh nguồn đến đỉnh đích
- Áp dụng cho đồ thị có trọng số

**Phân loại:**
1. **Single-source shortest path**: Từ 1 đỉnh đến tất cả
   - Dijkstra (không có cạnh âm)
   - Bellman-Ford (có cạnh âm)
2. **All-pairs shortest path**: Giữa mọi cặp đỉnh
   - Floyd-Warshall

### 4.2. Thuật giải Dijkstra

**Lý thuyết:**
- Tìm đường đi ngắn nhất từ 1 đỉnh
- Chỉ áp dụng với trọng số không âm
- Độ phức tạp: O((V + E) log V) với priority queue

**Ý tưởng:**
1. Khởi tạo khoảng cách đến nguồn = 0, các đỉnh khác = ∞
2. Chọn đỉnh chưa thăm có khoảng cách nhỏ nhất
3. Cập nhật khoảng cách đến các đỉnh kề
4. Lặp lại cho đến khi thăm hết

**Thuật giải:**
```cpp
struct Edge {
    int to, weight;
};

vector<int> dijkstra(int start, int V, vector<vector<Edge>>& adj) {
    vector<int> dist(V, INT_MAX);
    vector<bool> visited(V, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (visited[u]) continue;
        visited[u] = true;

        for (auto& edge : adj[u]) {
            int v = edge.to;
            int weight = edge.weight;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    return dist;
}
```

**Truy vết đường đi:**
```cpp
struct DijkstraResult {
    vector<int> dist;
    vector<int> parent;
};

DijkstraResult dijkstraWithPath(int start, int V, vector<vector<Edge>>& adj) {
    vector<int> dist(V, INT_MAX);
    vector<int> parent(V, -1);
    vector<bool> visited(V, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (visited[u]) continue;
        visited[u] = true;

        for (auto& edge : adj[u]) {
            int v = edge.to;
            int weight = edge.weight;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                parent[v] = u;
                pq.push({dist[v], v});
            }
        }
    }

    return {dist, parent};
}

vector<int> getPath(int start, int end, vector<int>& parent) {
    vector<int> path;
    for (int v = end; v != -1; v = parent[v])
        path.push_back(v);
    reverse(path.begin(), path.end());
    return path;
}
```

**Ứng dụng thực tế:**

**1. GPS và Navigation:**
- Google Maps, Waze
- Tìm đường đi ngắn nhất giữa 2 địa điểm

```cpp
struct Location {
    double lat, lon;
    string name;
};

struct Road {
    int to;
    double distance;
    double time;
    string roadName;
};

// Tìm đường đi nhanh nhất
vector<int> findFastestRoute(int start, int end, vector<vector<Road>>& roads) {
    // Sử dụng Dijkstra với trọng số = thời gian
}

// Tìm đường đi ngắn nhất
vector<int> findShortestRoute(int start, int end, vector<vector<Road>>& roads) {
    // Sử dụng Dijkstra với trọng số = khoảng cách
}
```

**2. Network Routing:**
- Định tuyến gói tin trong mạng
- OSPF (Open Shortest Path First) protocol

**3. Robot Path Planning:**
- Tìm đường đi tối ưu cho robot
- Tránh chướng ngại vật

**4. Game AI:**
- Pathfinding cho NPC
- Tìm đường đi tối ưu trên bản đồ

**5. Airline Route Planning:**
- Tìm chuyến bay với giá rẻ nhất
- Tìm tuyến với ít điểm dừng nhất

### 4.3. Thuật giải Bellman-Ford

**Lý thuyết:**
- Tìm đường đi ngắn nhất từ 1 đỉnh
- Xử lý được trọng số âm
- Phát hiện chu trình âm
- Độ phức tạp: O(VE)

**Ý tưởng:**
1. Khởi tạo khoảng cách
2. Thực hiện V-1 lần relax tất cả các cạnh
3. Kiểm tra chu trình âm

**Thuật giải:**
```cpp
struct BellmanFordResult {
    vector<int> dist;
    bool hasNegativeCycle;
};

BellmanFordResult bellmanFord(int start, int V, vector<tuple<int, int, int>>& edges) {
    vector<int> dist(V, INT_MAX);
    dist[start] = 0;

    // Relax V-1 lần
    for (int i = 0; i < V - 1; i++) {
        for (auto& edge : edges) {
            int u = get<0>(edge);
            int v = get<1>(edge);
            int weight = get<2>(edge);

            if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
            }
        }
    }

    // Kiểm tra chu trình âm
    bool hasNegativeCycle = false;
    for (auto& edge : edges) {
        int u = get<0>(edge);
        int v = get<1>(edge);
        int weight = get<2>(edge);

        if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
            hasNegativeCycle = true;
            break;
        }
    }

    return {dist, hasNegativeCycle};
}
```

**Ứng dụng thực tế:**

**1. Currency Exchange (Arbitrage):**
- Phát hiện cơ hội kiếm lời từ chênh lệch tỷ giá
- Chu trình âm = cơ hội arbitrage

```cpp
// Chuyển đổi tỷ giá thành log để tìm chu trình âm
double rate[100][100];  // Tỷ giá giữa các đồng tiền

void detectArbitrage(int n) {
    vector<tuple<int, int, int>> edges;

    // Chuyển đổi: weight = -log(rate)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j) {
                int weight = -log(rate[i][j]) * 1000;  // Scale để làm việc với int
                edges.push_back({i, j, weight});
            }
        }
    }

    auto result = bellmanFord(0, n, edges);
    if (result.hasNegativeCycle) {
        cout << "Có cơ hội arbitrage!" << endl;
    }
}
```

**2. Network với trễ âm:**
- Các hệ thống có phần thưởng
- Optimization problems

**3. Financial Modeling:**
- Tìm lợi nhuận tối đa trong giao dịch

### 4.4. Thuật giải Floyd-Warshall

**Lý thuyết:**
- Tìm đường đi ngắn nhất giữa **tất cả các cặp đỉnh** (All-pairs shortest path)
- Sử dụng Dynamic Programming
- Xử lý được trọng số âm
- Phát hiện chu trình âm
- Độ phức tạp: O(V³)

**Ý tưởng:**
- Sử dụng ma trận kề để lưu khoảng cách
- Xét từng đỉnh trung gian k (0 đến V-1)
- Với mỗi cặp đỉnh (i, j), kiểm tra xem đi qua k có ngắn hơn không
- Công thức: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

**Thuật giải:**
```cpp
struct FloydWarshallResult {
    vector<vector<int>> dist;
    vector<vector<int>> next;  // Để truy vết đường đi
    bool hasNegativeCycle;
};

FloydWarshallResult floydWarshall(int V, vector<vector<int>>& graph) {
    const int INF = 1e9;
    vector<vector<int>> dist = graph;
    vector<vector<int>> next(V, vector<int>(V, -1));

    // Khởi tạo next để truy vết
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (i != j && graph[i][j] != INF) {
                next[i][j] = j;
            }
        }
    }

    // Floyd-Warshall
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        next[i][j] = next[i][k];
                    }
                }
            }
        }
    }

    // Kiểm tra chu trình âm
    bool hasNegativeCycle = false;
    for (int i = 0; i < V; i++) {
        if (dist[i][i] < 0) {
            hasNegativeCycle = true;
            break;
        }
    }

    return {dist, next, hasNegativeCycle};
}
```

**Truy vết đường đi:**
```cpp
vector<int> reconstructPath(int u, int v, vector<vector<int>>& next) {
    if (next[u][v] == -1) {
        return {};  // Không có đường đi
    }

    vector<int> path = {u};
    while (u != v) {
        u = next[u][v];
        path.push_back(u);
    }

    return path;
}
```

**Ví dụ sử dụng:**
```cpp
int main() {
    int V = 4;
    const int INF = 1e9;

    // Khởi tạo đồ thị
    vector<vector<int>> graph(V, vector<int>(V, INF));

    // Khoảng cách từ đỉnh đến chính nó = 0
    for (int i = 0; i < V; i++)
        graph[i][i] = 0;

    // Thêm các cạnh
    graph[0][1] = 5;
    graph[0][3] = 10;
    graph[1][2] = 3;
    graph[2][3] = 1;

    // Chạy Floyd-Warshall
    auto result = floydWarshall(V, graph);

    // In ma trận khoảng cách
    cout << "Ma trận khoảng cách ngắn nhất:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (result.dist[i][j] == INF)
                cout << "INF ";
            else
                cout << result.dist[i][j] << " ";
        }
        cout << endl;
    }

    // In đường đi từ 0 đến 3
    auto path = reconstructPath(0, 3, result.next);
    cout << "\nĐường đi từ 0 đến 3: ";
    for (int v : path)
        cout << v << " ";

    return 0;
}
```

**Ứng dụng thực tế:**

**1. Tính khoảng cách giữa tất cả các cặp địa điểm:**
```cpp
// Ví dụ: Tính khoảng cách giữa tất cả các thành phố
struct CityNetwork {
    vector<string> cityNames;
    vector<vector<int>> distances;

    void findAllDistances() {
        int n = cityNames.size();
        auto result = floydWarshall(n, distances);

        // In bảng khoảng cách
        cout << "Khoảng cách giữa các thành phố:\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << cityNames[i] << " -> " << cityNames[j]
                     << ": " << result.dist[i][j] << "km\n";
            }
        }
    }

    // Tìm thành phố trung tâm (tổng khoảng cách đến các thành phố khác nhỏ nhất)
    int findCentralCity() {
        int n = cityNames.size();
        auto result = floydWarshall(n, distances);

        int centralCity = 0;
        int minTotalDist = INT_MAX;

        for (int i = 0; i < n; i++) {
            int totalDist = 0;
            for (int j = 0; j < n; j++) {
                totalDist += result.dist[i][j];
            }

            if (totalDist < minTotalDist) {
                minTotalDist = totalDist;
                centralCity = i;
            }
        }

        return centralCity;
    }
};
```

**2. Network Routing - Tính toán bảng định tuyến:**
```cpp
// Tính bảng định tuyến cho mỗi router
struct Router {
    int id;
    map<int, int> routingTable;  // destination -> next hop
};

vector<Router> buildRoutingTables(int V, vector<vector<int>>& network) {
    auto result = floydWarshall(V, network);
    vector<Router> routers(V);

    for (int i = 0; i < V; i++) {
        routers[i].id = i;
        for (int j = 0; j < V; j++) {
            if (i != j && result.next[i][j] != -1) {
                routers[i].routingTable[j] = result.next[i][j];
            }
        }
    }

    return routers;
}
```

**3. Game Development - Tính toán khoảng cách trên bản đồ:**
```cpp
// Pre-compute tất cả khoảng cách giữa các vị trí trên map
class GameMap {
private:
    vector<vector<int>> allDistances;

public:
    void precomputeDistances(vector<vector<int>>& mapGraph) {
        auto result = floydWarshall(mapGraph.size(), mapGraph);
        allDistances = result.dist;
    }

    // Truy vấn nhanh O(1)
    int getDistance(int from, int to) {
        return allDistances[from][to];
    }

    // Tìm kẻ địch gần nhất
    int findNearestEnemy(int playerPos, vector<int>& enemyPositions) {
        int nearest = -1;
        int minDist = INT_MAX;

        for (int enemyPos : enemyPositions) {
            int dist = allDistances[playerPos][enemyPos];
            if (dist < minDist) {
                minDist = dist;
                nearest = enemyPos;
            }
        }

        return nearest;
    }
};
```

**4. Social Network Analysis:**
```cpp
// Tính "closeness centrality" - đo độ gần của một người với mọi người khác
double calculateClosenessCentrality(int userId, vector<vector<int>>& socialGraph) {
    int n = socialGraph.size();
    auto result = floydWarshall(n, socialGraph);

    double totalDistance = 0;
    int reachableCount = 0;

    for (int i = 0; i < n; i++) {
        if (i != userId && result.dist[userId][i] != 1e9) {
            totalDistance += result.dist[userId][i];
            reachableCount++;
        }
    }

    if (reachableCount == 0) return 0;

    // Closeness = (n-1) / tổng khoảng cách
    return (reachableCount) / totalDistance;
}

// Tìm người có ảnh hưởng nhất
int findMostInfluentialPerson(vector<vector<int>>& socialGraph) {
    int n = socialGraph.size();
    int mostInfluential = 0;
    double maxCloseness = 0;

    for (int i = 0; i < n; i++) {
        double closeness = calculateClosenessCentrality(i, socialGraph);
        if (closeness > maxCloseness) {
            maxCloseness = closeness;
            mostInfluential = i;
        }
    }

    return mostInfluential;
}
```

**5. Transitive Closure - Kiểm tra khả năng đi được:**
```cpp
// Tìm tất cả các cặp đỉnh có đường đi
vector<vector<bool>> findTransitiveClosure(int V, vector<vector<int>>& graph) {
    auto result = floydWarshall(V, graph);
    vector<vector<bool>> reachable(V, vector<bool>(V, false));

    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            reachable[i][j] = (result.dist[i][j] != 1e9);
        }
    }

    return reachable;
}

// Ứng dụng: Kiểm tra prerequisite courses
bool canTakeCourse(int course, int student,
                   vector<int>& completedCourses,
                   vector<vector<bool>>& prerequisites) {
    // Kiểm tra xem sinh viên đã học tất cả các môn tiên quyết chưa
    for (int completed : completedCourses) {
        if (prerequisites[completed][course]) {
            return true;
        }
    }
    return false;
}
```

**6. Finding Graph Center/Median:**
```cpp
// Tìm "center" của đồ thị - đỉnh có khoảng cách max đến các đỉnh khác là nhỏ nhất
int findGraphCenter(int V, vector<vector<int>>& graph) {
    auto result = floydWarshall(V, graph);

    int center = 0;
    int minMaxDist = INT_MAX;

    for (int i = 0; i < V; i++) {
        int maxDist = 0;
        for (int j = 0; j < V; j++) {
            if (result.dist[i][j] != 1e9) {
                maxDist = max(maxDist, result.dist[i][j]);
            }
        }

        if (maxDist < minMaxDist) {
            minMaxDist = maxDist;
            center = i;
        }
    }

    return center;
}

// Ứng dụng: Đặt warehouse/data center ở vị trí tối ưu
int findOptimalWarehouseLocation(vector<vector<int>>& cityDistances) {
    return findGraphCenter(cityDistances.size(), cityDistances);
}
```

**Ưu điểm:**
- Tìm đường đi ngắn nhất giữa **tất cả** các cặp đỉnh
- Code đơn giản, dễ hiểu
- Xử lý được trọng số âm
- Phù hợp khi cần query nhiều lần

**Nhược điểm:**
- Độ phức tạp O(V³) - chậm với đồ thị lớn
- Tốn bộ nhớ O(V²)
- Nếu chỉ cần từ 1 đỉnh nguồn, Dijkstra/Bellman-Ford hiệu quả hơn

**Khi nào dùng Floyd-Warshall:**
- Đồ thị nhỏ (V < 400)
- Cần khoảng cách giữa **nhiều** cặp đỉnh
- Cần pre-compute để query nhanh O(1)
- Đồ thị dày đặc (nhiều cạnh)

### 4.5. So sánh các thuật toán tìm đường đi ngắn nhất

| Tiêu chí | Dijkstra | Bellman-Ford | Floyd-Warshall |
|----------|----------|--------------|----------------|
| Loại bài toán | Single-source | Single-source | All-pairs |
| Độ phức tạp | O((V+E) log V) | O(VE) | O(V³) |
| Bộ nhớ | O(V) | O(V) | O(V²) |
| Trọng số âm | Không | Có | Có |
| Chu trình âm | Không xử lý | Phát hiện được | Phát hiện được |
| Cấu trúc DL | Priority Queue | Mảng | Ma trận |
| Tốc độ | Nhanh nhất (1 nguồn) | Chậm | Chậm với V lớn |
| Khi nào dùng | 1 nguồn, không âm | 1 nguồn, có âm | Nhiều cặp đỉnh |
| Ứng dụng | GPS, routing | Arbitrage, tối ưu | Bảng định tuyến, Game |

**Ví dụ lựa chọn thuật toán:**

```cpp
// Kịch bản 1: GPS Navigation - tìm đường từ A đến B
// -> Dùng DIJKSTRA (1 nguồn, trọng số dương, nhanh nhất)
auto dist = dijkstra(sourceCity, V, roadNetwork);

// Kịch bản 2: Phát hiện arbitrage trong giao dịch tiền tệ
// -> Dùng BELLMAN-FORD (có trọng số âm, cần phát hiện chu trình âm)
auto result = bellmanFord(0, numCurrencies, exchangeRates);

// Kịch bản 3: Tính bảng khoảng cách cho game map (100 vị trí)
// -> Dùng FLOYD-WARSHALL (cần tất cả cặp, pre-compute, V nhỏ)
auto allDists = floydWarshall(numLocations, gameMap);

// Kịch bản 4: Tìm đường giữa 1000 thành phố (query nhiều lần)
// -> Nếu V lớn: Chạy Dijkstra cho mỗi nguồn, cache kết quả
// -> Nếu V nhỏ: Floyd-Warshall pre-compute
if (V < 400) {
    auto allDists = floydWarshall(V, graph);
} else {
    // Cache Dijkstra results cho các nguồn thường dùng
    map<int, vector<int>> cachedResults;
}
```

---

## 5. CÂY BAO TRÙM NHỎ NHẤT

### 5.1. Khái niệm

**Định nghĩa:**
- Cây khung (Spanning Tree): Đồ thị con liên thông, không chu trình, chứa tất cả đỉnh
- Cây khung nhỏ nhất (Minimum Spanning Tree - MST): Cây khung có tổng trọng số nhỏ nhất

**Tính chất:**
- Có V-1 cạnh (V là số đỉnh)
- Liên thông
- Không có chu trình
- Tổng trọng số nhỏ nhất

### 5.2. Thuật giải Kruskal

**Lý thuyết:**
- Thuật toán tham lam (greedy)
- Chọn cạnh có trọng số nhỏ nhất chưa tạo chu trình
- Sử dụng Union-Find (Disjoint Set)
- Độ phức tạp: O(E log E)

**Ý tưởng:**
1. Sắp xếp các cạnh theo trọng số tăng dần
2. Chọn cạnh nhỏ nhất chưa tạo chu trình
3. Lặp lại cho đến khi có V-1 cạnh

**Cấu trúc Union-Find:**
```cpp
class UnionFind {
private:
    vector<int> parent, rank;

public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);  // Path compression
        return parent[x];
    }

    bool unite(int x, int y) {
        int px = find(x);
        int py = find(y);

        if (px == py) return false;

        // Union by rank
        if (rank[px] < rank[py])
            parent[px] = py;
        else if (rank[px] > rank[py])
            parent[py] = px;
        else {
            parent[py] = px;
            rank[px]++;
        }

        return true;
    }
};
```

**Thuật giải Kruskal:**
```cpp
struct Edge {
    int u, v, weight;

    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

struct MSTResult {
    vector<Edge> edges;
    int totalWeight;
};

MSTResult kruskal(int V, vector<Edge>& edges) {
    sort(edges.begin(), edges.end());

    UnionFind uf(V);
    vector<Edge> mstEdges;
    int totalWeight = 0;

    for (auto& edge : edges) {
        if (uf.unite(edge.u, edge.v)) {
            mstEdges.push_back(edge);
            totalWeight += edge.weight;

            if (mstEdges.size() == V - 1)
                break;
        }
    }

    return {mstEdges, totalWeight};
}
```

**Ứng dụng thực tế:**

**1. Thiết kế mạng:**
- Kết nối các máy tính với chi phí dây cáp tối thiểu
- Thiết kế mạng điện, nước

```cpp
struct City {
    string name;
    double x, y;  // Tọa độ
};

// Tính khoảng cách giữa 2 thành phố
double distance(City& a, City& b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

// Thiết kế mạng kết nối các thành phố
MSTResult designNetwork(vector<City>& cities) {
    int n = cities.size();
    vector<Edge> edges;

    // Tạo đồ thị đầy đủ
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int dist = distance(cities[i], cities[j]) * 100;  // Scale
            edges.push_back({i, j, dist});
        }
    }

    return kruskal(n, edges);
}
```

**2. Cluster Analysis:**
- Phân nhóm dữ liệu
- Image segmentation

**3. Road Network Design:**
- Thiết kế đường giao thông
- Tối ưu chi phí xây dựng

### 5.3. Thuật giải Prim

**Lý thuyết:**
- Thuật toán tham lam
- Bắt đầu từ 1 đỉnh, mở rộng dần
- Độ phức tạp: O((V + E) log V) với priority queue

**Ý tưởng:**
1. Bắt đầu từ đỉnh bất kỳ
2. Chọn cạnh nhỏ nhất nối với cây hiện tại
3. Thêm đỉnh mới vào cây
4. Lặp lại cho đến khi đủ V đỉnh

**Thuật giải:**
```cpp
MSTResult prim(int V, vector<vector<Edge>>& adj) {
    vector<bool> inMST(V, false);
    vector<int> key(V, INT_MAX);
    vector<int> parent(V, -1);

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    int start = 0;
    key[start] = 0;
    pq.push({0, start});

    vector<Edge> mstEdges;
    int totalWeight = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (inMST[u]) continue;

        inMST[u] = true;
        if (parent[u] != -1) {
            mstEdges.push_back({parent[u], u, key[u]});
            totalWeight += key[u];
        }

        for (auto& edge : adj[u]) {
            int v = edge.to;
            int weight = edge.weight;

            if (!inMST[v] && weight < key[v]) {
                key[v] = weight;
                parent[v] = u;
                pq.push({key[v], v});
            }
        }
    }

    return {mstEdges, totalWeight};
}
```

**Ứng dụng thực tế:**

**1. Network Design:**
- Tương tự Kruskal
- Phù hợp khi đồ thị dày đặc

**2. Approximation Algorithms:**
- TSP (Traveling Salesman Problem)
- Metric TSP: sử dụng MST để tìm lời giải gần đúng

```cpp
// TSP Approximation sử dụng MST
double approximateTSP(int V, vector<vector<Edge>>& adj) {
    // 1. Tìm MST
    auto mst = prim(V, adj);

    // 2. DFS trên MST để tạo tour
    // 3. Tour này có độ dài <= 2 * MST

    return mst.totalWeight * 2;  // Worst case
}
```

**3. Image Segmentation:**
- Phân đoạn ảnh dựa trên MST

### 5.4. So sánh Kruskal và Prim

| Tiêu chí | Kruskal | Prim |
|----------|---------|------|
| Độ phức tạp | O(E log E) | O((V+E) log V) |
| Cấu trúc dữ liệu | Union-Find | Priority Queue |
| Phù hợp | Đồ thị thưa | Đồ thị dày |
| Cài đặt | Đơn giản hơn | Phức tạp hơn |
| Parallel | Dễ song song | Khó song song |

**5.5. Ứng dụng MST trong thực tế:**

**1. Telecommunication Networks:**
- Thiết kế mạng cáp quang
- Minimize installation cost

**2. Water/Gas Pipeline:**
- Thiết kế đường ống
- Tối ưu chi phí lắp đặt

**3. Electrical Grid:**
- Thiết kế mạng lưới điện
- Đảm bảo kết nối với chi phí thấp

**4. Transportation Network:**
- Thiết kế tuyến xe bus
- Kết nối các thành phố

**5. Clustering:**
```cpp
// Sử dụng MST để phân cụm
vector<vector<int>> clusterUsingMST(int V, vector<Edge>& edges, int k) {
    // 1. Tìm MST
    auto mst = kruskal(V, edges);

    // 2. Xóa k-1 cạnh lớn nhất
    sort(mst.edges.begin(), mst.edges.end(),
         [](const Edge& a, const Edge& b) {
             return a.weight > b.weight;
         });

    // 3. Các thành phần liên thông = các cụm
    UnionFind uf(V);
    for (int i = k - 1; i < mst.edges.size(); i++) {
        uf.unite(mst.edges[i].u, mst.edges[i].v);
    }

    // 4. Tạo các cụm
    map<int, vector<int>> clusters;
    for (int i = 0; i < V; i++) {
        clusters[uf.find(i)].push_back(i);
    }

    vector<vector<int>> result;
    for (auto& p : clusters) {
        result.push_back(p.second);
    }

    return result;
}
```

---

## 6. TỔNG KẾT VÀ MẸO HỌC TẬP

### 6.1. Chiến lược học tập

**1. Hiểu lý thuyết trước khi code:**
- Vẽ sơ đồ, minh họa
- Chạy thuật toán bằng tay với ví dụ nhỏ

**2. Practice, practice, practice:**
- Leetcode, HackerRank, Codeforces
- Làm bài tập từ dễ đến khó

**3. Phân tích độ phức tạp:**
- Luôn phân tích time và space complexity
- So sánh các giải pháp khác nhau

**4. Học từ code mẫu:**
- Đọc code của người khác
- Hiểu tại sao họ viết như vậy

### 6.2. Bảng tra cứu nhanh

**Độ phức tạp các thuật toán sắp xếp:**

| Thuật toán | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Shell Sort | O(n log n) | O(n log n) | O(n²) | O(1) | No |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n) | Yes |

**Độ phức tạp thuật toán đồ thị:**

| Thuật toán | Độ phức tạp | Không gian | Loại bài toán |
|-----------|-------------|------------|---------------|
| BFS | O(V+E) | O(V) | Duyệt, đường đi ngắn nhất (không trọng số) |
| DFS | O(V+E) | O(V) | Duyệt, chu trình, topo sort |
| Dijkstra | O((V+E) log V) | O(V) | Đường đi ngắn nhất 1 nguồn (không âm) |
| Bellman-Ford | O(VE) | O(V) | Đường đi ngắn nhất 1 nguồn (có âm) |
| Floyd-Warshall | O(V³) | O(V²) | Đường đi ngắn nhất tất cả cặp |
| Kruskal | O(E log E) | O(V) | Cây khung nhỏ nhất (đồ thị thưa) |
| Prim | O((V+E) log V) | O(V) | Cây khung nhỏ nhất (đồ thị dày) |

### 6.3. Khi nào dùng thuật toán nào?

**Sắp xếp:**
- Dữ liệu nhỏ (< 50): Insertion Sort
- Dữ liệu vừa: Quick Sort, Merge Sort
- Số nguyên, khoảng nhỏ: Counting Sort, Radix Sort
- Cần stable: Merge Sort, Radix Sort
- Ít bộ nhớ: Shell Sort, Heap Sort

**Đồ thị:**
- Tìm đường đi ngắn nhất (không trọng số): BFS
- Phát hiện chu trình: DFS
- Đường đi ngắn nhất (có trọng số dương): Dijkstra
- Đường đi ngắn nhất (có trọng số âm): Bellman-Ford
- Kết nối mạng tối ưu: Kruskal, Prim

### 6.4. Các lỗi thường gặp

**1. Quên khởi tạo:**
```cpp
// SAI
int visited[100];  // Không khởi tạo

// ĐÚNG
int visited[100] = {0};
// hoặc
vector<bool> visited(n, false);
```

**2. Tràn số:**
```cpp
// SAI
int dist[100];
dist[0] = 999999999;  // Có thể tràn khi cộng

// ĐÚNG
const int INF = 1e9;
int dist[100];
dist[0] = INF;
```

**3. So sánh sai:**
```cpp
// SAI trong Dijkstra
if (dist[u] + weight < dist[v] && !visited[v])

// ĐÚNG
if (!visited[v] && dist[u] + weight < dist[v])
```

### 6.5. Tips debug

**1. In ra trạng thái:**
```cpp
void printGraph() {
    for (int i = 0; i < V; i++) {
        cout << i << ": ";
        for (auto& e : adj[i])
            cout << "(" << e.to << "," << e.weight << ") ";
        cout << endl;
    }
}
```

**2. Kiểm tra với test nhỏ:**
- Bắt đầu với n = 3, 4, 5
- Vẽ sơ đồ để đối chiếu

**3. Sử dụng assert:**
```cpp
assert(u >= 0 && u < V);
assert(dist[u] != INF);
```

### 6.6. Tài nguyên học thêm

**Websites:**
- Visualgo.net: Minh họa thuật toán
- GeeksforGeeks: Lý thuyết và code mẫu
- Leetcode: Practice problems

**Books:**
- "Introduction to Algorithms" - CLRS
- "Competitive Programming" - Steven Halim
- "Algorithm Design Manual" - Skiena

**Videos:**
- MIT OpenCourseWare
- Abdul Bari's Algorithm Course
- William Fiset's Graph Theory

---

## 7. BÀI TẬP THỰC HÀNH

### 7.1. Sắp xếp

**Bài 1:** Cài đặt Shell Sort với các dãy gap khác nhau và so sánh hiệu suất

**Bài 2:** Sử dụng Radix Sort để sắp xếp danh sách sinh viên theo MSSV

**Bài 3:** Áp dụng Bucket Sort để phân loại điểm thi (0-10)

### 7.2. Đồ thị

**Bài 4:** Cài đặt BFS để tìm độ phân cách trong mạng xã hội

**Bài 5:** Sử dụng DFS để phát hiện chu trình trong đồ thị có hướng

**Bài 6:** Cài đặt Topological Sort để lập lịch công việc

### 7.3. Đường đi ngắn nhất

**Bài 7:** Xây dựng hệ thống GPS đơn giản với Dijkstra

**Bài 8:** Phát hiện arbitrage trong giao dịch tiền tệ với Bellman-Ford

### 7.4. MST

**Bài 9:** Thiết kế mạng kết nối các thành phố với chi phí tối thiểu

**Bài 10:** Phân cụm dữ liệu sử dụng MST

---

## KẾT LUẬN

Môn học Cấu trúc dữ liệu và Giải thuật 2 cung cấp nền tảng vững chắc về:

1. **Phân tích thuật toán**: Đánh giá hiệu suất, chọn giải pháp tối ưu
2. **Thuật toán sắp xếp nâng cao**: Shell, Radix, Counting, Bucket Sort
3. **Thuật toán đồ thị**: BFS, DFS và ứng dụng
4. **Đường đi ngắn nhất**: Dijkstra, Bellman-Ford
5. **Cây khung nhỏ nhất**: Kruskal, Prim

Những kiến thức này không chỉ quan trọng trong học tập mà còn là nền tảng cho:
- Phỏng vấn kỹ thuật (Google, Facebook, Amazon...)
- Giải quyết vấn đề thực tế
- Tối ưu hóa hệ thống
- Nghiên cứu khoa học

**Lời khuyên cuối:**
> "The best way to learn algorithms is to implement them yourself."

Chúc các bạn học tốt và áp dụng thành công vào thực tế!

---

**Người soạn:** Dựa trên đề cương môn học ITEC1328
**Ngày:** 2025-11-09
**Tài liệu tham khảo:**
- Lê Xuân Trường, Cấu trúc dữ liệu, NXB Thông tin và Truyền thông, 2018
- Thomas H. Cormen et al., Introduction to Algorithms, MIT Press, 2009
