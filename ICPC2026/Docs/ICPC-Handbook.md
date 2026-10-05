# ICPC Master Handbook: Thuật toán & Cấu trúc dữ liệu nâng cao
> **Tài liệu tham khảo chuyên sâu cho kỳ thi ICPC & Lập trình thi đấu (Competitive Programming)**  
> Chuẩn hóa theo C++20 | Tối ưu thời gian & bộ nhớ | Khử đệ quy sâu | Phân tích toán học & bản chất từng dòng code.

---

## Mục lục toàn diện

1. [Cấu trúc dữ liệu](#1-cấu-trúc-dữ-liệu)
   - [1.1. Fenwick Tree 1D Cập nhật điểm và tính tổng đoạn](#11-fenwick-tree-1d-cập-nhật-điểm-và-tính-tổng-đoạn)
   - [1.2. Fenwick Tree Range Update Range Query](#12-fenwick-tree-range-update-range-query)
   - [1.3. Fenwick Tree 2D](#13-fenwick-tree-2d)
   - [1.4. Disjoint Set Union DSU](#14-disjoint-set-union-dsu)
   - [1.5. Sparse Table RMQ O1](#15-sparse-table-rmq-o1)
2. [Đồ thị cơ bản và đường đi ngắn nhất](#2-đồ-thị-cơ-bản-và-đường-đi-ngắn-nhất)
   - [2.1. Topological Sort Kahns BFS](#21-topological-sort-kahns-bfs)
   - [2.2. 0-1 BFS Đồ thị trọng số 0 và 1](#22-0-1-bfs-đồ-thị-trọng-số-0-và-1)
   - [2.3. Bellman-Ford và chu trình âm](#23-bellman-ford-và-chu-trình-âm)
   - [2.4. Floyd-Warshall](#24-floyd-warshall)
   - [2.5. LCA Binary Lifting không sợ Stack Overflow](#25-lca-binary-lifting-không-sợ-stack-overflow)
   - [2.6. 2-SAT Thỏa mãn mệnh đề logic](#26-2-sat-thỏa-mãn-mệnh-đề-logic)
3. [Luồng cực đại và cặp ghép](#3-luồng-cực-đại-và-cặp-ghép)
   - [3.1. Dinic Max-Flow](#31-dinic-max-flow)
   - [3.2. Hopcroft-Karp Bipartite Matching](#32-hopcroft-karp-bipartite-matching)
4. [Hình học tính toán](#4-hình-học-tính-toán)
   - [4.1. Điểm Vector và Tích có hướng CCW](#41-điểm-vector-và-tích-có-hướng-ccw)
   - [4.2. Giao hai đoạn thẳng Segment Intersection](#42-giao-hai-đoạn-thẳng-segment-intersection)
   - [4.3. Điểm nằm trong đa giác Point in Polygon](#43-điểm-nằm-trong-đa-giác-point-in-polygon)
   - [4.4. Bao lồi Andrews Monotone Chain](#44-bao-lồi-andrews-monotone-chain)
5. [Xâu ký tự](#5-xâu-ký-tự)
   - [5.1. Manacher Tìm mọi Palindrome ON](#51-manacher-tìm-mọi-palindrome-on)
   - [5.2. Aho-Corasick Automaton](#52-aho-corasick-automaton)
6. [Số học và tổ hợp cao cấp](#6-số-học-và-tổ-hợp-cao-cấp)
   - [6.1. Tổ hợp modulo nguyên tố O1 Fact và InvFact](#61-tổ-hợp-modulo-nguyên-tố-o1-fact-và-invfact)
   - [6.2. Chinese Remainder Theorem CRT tổng quát](#62-chinese-remainder-theorem-crt-tổng-quát)
   - [6.3. Pollard Rho Phân tích thừa số ON14](#63-pollard-rho-phân-tích-thừa-số-on14)

---

# 1. Cấu trúc dữ liệu

## 1.1. Fenwick Tree 1D Cập nhật điểm và tính tổng đoạn

### 1. Bản chất toán học & Cấu trúc nhị phân
Fenwick Tree (Binary Indexed Tree - BIT) biểu diễn một cây nhị phân tiềm ẩn trên mảng 1 chiều dựa trên thao tác bit:
$$\mathbf{p \ \& \ (-p)}$$
Đây là thao tác trích xuất **bit 1 nhỏ nhất (Least Significant Bit - LSB)** của số nguyên $p$.
- Mỗi vị trí $p$ trong cây BIT quản lý một đoạn có độ dài đúng bằng $p \ \& \ (-p)$, kết thúc tại $p$:
  $$\text{Đoạn quản lý: } \big(p - (p \ \& \ -p), \; p\big]$$
- **Ví dụ minh họa**:
  - $p = 6 = (110)_2 \implies 6 \ \& \ (-6) = (010)_2 = 2$. Vị trí 6 quản lý đoạn $(6 - 2, 6] = [5, 6]$.
  - $p = 8 = (1000)_2 \implies 8 \ \& \ (-8) = (1000)_2 = 8$. Vị trí 8 quản lý đoạn $(8 - 8, 8] = [1, 8]$.

### 2. Cơ chế hoạt động của Update và Query
- **Tính tổng tiền tố `query(p)` ($[1, p]$)**:
  Ta cần cộng các đoạn rời rạc phủ kín $[1, p]$. Bắt đầu từ $p$, tại mỗi bước ta cộng giá trị `tree[p]` rồi loại bỏ bit 1 cuối cùng bằng phép trừ: `p -= p & -p`.
  - Ví dụ $p = 7 = (111)_2$:
    - Cộng đoạn $[7, 7]$ tại $p = 7$. Giảm $p \to 6 = (110)_2$.
    - Cộng đoạn $[5, 6]$ tại $p = 6$. Giảm $p \to 4 = (100)_2$.
    - Cộng đoạn $[1, 4]$ tại $p = 4$. Giảm $p \to 0$ (dừng lại).
    - Tổng cộng: $[7, 7] + [5, 6] + [1, 4] = [1, 7]$. Mất tối đa $\log_2(p)$ bước!
- **Cập nhật điểm `add(p, v)`**:
  Khi giá trị tại $p$ tăng thêm $v$, ta cần cập nhật tất cả các nút cha quản lý chứa $p$. Ta lần lượt cộng bit 1 cuối cùng: `p += p & -p` cho đến khi vượt quá $n$.

### 3. Cạm bẫy sống còn khi thi ICPC
> [!CAUTION]
> **BẮT BUỘC DÙNG CHỈ SỐ 1-BASED**:
> Nếu bạn gọi `add(0, v)` hoặc `query(0)`, vì $0 \ \& \ (-0) = 0$, lệnh `p += p & -p` sẽ thành `0 += 0`, dẫn đến **vòng lặp vô tận (Infinite Loop / TLE)**. Nếu đề bài cho mảng 0-based, hãy luôn luôn cộng 1 vào chỉ số trước khi truyền vào hàm!

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Fenwick {
    int n;
    vector<ll> tree;

    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    // Cộng v vào vị trí p (1-based): O(log N)
    void add(int p, ll v) {
        for (; p <= n; p += p & -p) tree[p] += v;
    }

    // Tính tổng tiền tố a[1..p]: O(log N)
    ll query(int p) const {
        ll sum = 0;
        for (; p > 0; p -= p & -p) sum += tree[p];
        return sum;
    }

    // Tính tổng đoạn [l, r]: O(log N)
    ll queryRange(int l, int r) const {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};
```

---

## 1.2. Fenwick Tree Range Update Range Query

### 1. Bản chất toán học (Biến đổi mảng sai phân)
Làm thế nào để vừa **cộng một giá trị $v$ vào cả đoạn $[l, r]$**, vừa **truy vấn tổng đoạn bất kỳ $[l, r]$** trong $O(\log N)$ mà không cần viết Segment Tree Lazy dài 80 dòng?

Xét mảng sai phân: $D[i] = A[i] - A[i-1]$ (với quy ước $A[0] = 0$).
Khi đó, giá trị phần tử thứ $i$ chính là tổng tiền tố của mảng sai phân:
$$A[i] = \sum_{j=1}^i D[j]$$

Tổng tiền tố của mảng ban đầu từ $1$ đến $p$ là:
$$S(p) = \sum_{i=1}^p A[i] = \sum_{i=1}^p \sum_{j=1}^i D[j]$$
Quan sát số lần xuất hiện của từng phần tử $D[j]$ trong tổng trên:
- $D[1]$ xuất hiện $p$ lần (trong $A[1], A[2], \dots, A[p]$).
- $D[2]$ xuất hiện $p - 1$ lần.
- Tổng quát, $D[j]$ xuất hiện $(p - j + 1)$ lần.
Do đó:
$$S(p) = \sum_{j=1}^p (p - j + 1) D[j] = \sum_{j=1}^p (p + 1) D[j] - \sum_{j=1}^p j \cdot D[j]$$
Đưa $(p + 1)$ ra ngoài dấu tổng:
$$\mathbf{S(p) = (p + 1) \sum_{j=1}^p D[j] - \sum_{j=1}^p \big(j \cdot D[j]\big)}$$

### 2. Kiến trúc 2 cây BIT
Từ công thức trên, ta chỉ cần duy trì **2 cây Fenwick thông thường**:
1. **Cây `b1`**: Quản lý các giá trị $D[j]$.
2. **Cây `b2`**: Quản lý các giá trị $j \cdot D[j]$.

Khi cập nhật đoạn $[l, r]$ tăng thêm $v$:
- Mảng sai phân $D$ thay đổi: $D[l]$ tăng $v$, và $D[r+1]$ giảm $v$.
- Cây `b1`: cộng $+v$ tại $l$, cộng $-v$ tại $r+1$.
- Cây `b2`: cộng $+v \cdot l$ tại $l$, cộng $-v \cdot (r+1)$ tại $r+1$.

```cpp
struct RangeFenwick {
    int n;
    Fenwick b1, b2;

    RangeFenwick(int n) : n(n), b1(n), b2(n) {}

    // Cộng v vào mọi phần tử trong đoạn [l, r]: O(log N)
    void addRange(int l, int r, ll v) {
        b1.add(l, v);
        b1.add(r + 1, -v);
        b2.add(l, v * l);
        b2.add(r + 1, -v * (r + 1));
    }

    // Tính tổng tiền tố [1..p]: O(log N)
    ll queryPrefix(int p) const {
        return b1.query(p) * (p + 1) - b2.query(p);
    }

    // Tính tổng đoạn [l, r]: O(log N)
    ll queryRange(int l, int r) const {
        if (l > r) return 0;
        return queryPrefix(r) - queryPrefix(l - 1);
    }
};
```

---

## 1.3. Fenwick Tree 2D

### 1. Tại sao dùng BIT 2D thay vì Segment Tree 2D?
- **Segment Tree 2D**: Đòi hỏi mảng 2 chiều lồng nhau kích thước $(4N) \times (4M)$. Nếu $N, M = 2000$, nó ngốn $(8000 \times 8000 \times 8\text{ bytes}) \approx \mathbf{512\text{ MB}}$ $\to$ Tràn bộ nhớ (Memory Limit Exceeded) ngay lập tức!
- **Fenwick Tree 2D**: Chỉ cần đúng mảng $(N + 1) \times (M + 1)$, chiếm vỏn vẹn **$32\text{ MB}$**, đồng thời tốc độ thực thi nhanh gấp 5–10 lần nhờ tính liên tục của bộ nhớ cache.

### 2. Công thức bù trừ hình chữ nhật (Inclusion-Exclusion Principle)
Để tính tổng các ô trong hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$:
$$\text{Sum} = \text{Query}(x_2, y_2) - \text{Query}(x_1 - 1, y_2) - \text{Query}(x_2, y_1 - 1) + \text{Query}(x_1 - 1, y_1 - 1)$$

```cpp
struct Fenwick2D {
    int n, m;
    vector<vector<ll>> tree;

    Fenwick2D(int n, int m) : n(n), m(m), tree(n + 1, vector<ll>(m + 1, 0)) {}

    // Cộng v vào ô (x, y): O(log N * log M)
    void add(int x, int y, ll v) {
        for (int i = x; i <= n; i += i & -i)
            for (int j = y; j <= m; j += j & -j)
                tree[i][j] += v;
    }

    // Tổng tiền tố hình chữ nhật từ (1, 1) đến (x, y)
    ll query(int x, int y) const {
        ll sum = 0;
        for (int i = x; i > 0; i -= i & -i)
            for (int j = y; j > 0; j -= j & -j)
                sum += tree[i][j];
        return sum;
    }

    // Tổng hình chữ nhật [x1..x2][y1..y2]
    ll queryRect(int x1, int y1, int x2, int y2) const {
        return query(x2, y2) - query(x1 - 1, y2) 
             - query(x2, y1 - 1) + query(x1 - 1, y1 - 1);
    }
};
```

---

## 1.4. Disjoint Set Union DSU

### 1. Kỹ thuật mảng gộp `parentOrSize < 0`
Thay vì duy trì 2 mảng riêng biệt `parent[]` và `size[]`, kỹ thuật này lưu cả hai thông tin vào **một mảng duy nhất**:
- Nếu `parentOrSize[u] >= 0`: Nút $u$ không phải là gốc, và giá trị đó chính là chỉ số của **nút cha** của $u$.
- Nếu `parentOrSize[u] < 0`: Nút $u$ là **gốc của cây**, và **kích thước của cây đó chính là `-parentOrSize[u]`**.
  - Ví dụ: Ban đầu tất cả các phần tử đều là gốc có kích thước $1 \implies$ khởi tạo bằng `-1`.

### 2. Hai phép tối ưu hóa sống còn
1. **Nén đường đi (Path Compression)**: Trong hàm `find(u)`, ta gán trực tiếp cha của mọi nút trên đường đi về gốc:
   `parentOrSize[u] = find(parentOrSize[u])`.
2. **Gộp theo kích thước (Union by Size)**: Luôn gắn cây có kích thước nhỏ hơn vào làm con của cây có kích thước lớn hơn.
- Kết hợp cả hai kỹ thuật đưa độ phức tạp về $O(\alpha(N))$ cho mỗi thao tác, trong đó $\alpha$ là hàm nghịch đảo Ackermann ($\alpha(N) \le 4$ với mọi $N \le 10^{600}$).

```cpp
struct DSU {
    int n;
    vector<int> parentOrSize;

    DSU(int n) : n(n), parentOrSize(n + 1, -1) {}

    // Tìm gốc có nén đường đi: O(alpha(N))
    int find(int u) {
        return parentOrSize[u] < 0 ? u : parentOrSize[u] = find(parentOrSize[u]);
    }

    bool same(int u, int v) {
        return find(u) == find(v);
    }

    // Lấy kích thước tập hợp chứa u
    int size(int u) {
        return -parentOrSize[find(u)];
    }

    // Hợp nhất 2 tập hợp theo size
    bool unite(int u, int v) {
        int rootU = find(u), rootV = find(v);
        if (rootU == rootV) return false;
        // rootU luôn là cây có kích thước lớn hơn (giá trị âm hơn)
        if (parentOrSize[rootU] > parentOrSize[rootV]) swap(rootU, rootV);
        parentOrSize[rootU] += parentOrSize[rootV]; // Cộng dồn kích thước
        parentOrSize[rootV] = rootU;               // Gắn rootV vào rootU
        return true;
    }
};
```

---

## 1.5. Sparse Table RMQ O1

### 1. Ý nghĩa và cấu trúc mảng `st[j][i]`
- Mảng `st[j][i]` lưu giá trị nhỏ nhất của đoạn bắt đầu từ chỉ số `i` và có độ dài chính xác là $2^j$:
  $$[i, \; i + 2^j - 1]$$
- **Hàng cơ sở ($j = 0$)**: Đoạn có độ dài $2^0 = 1$, chính là giá trị mảng ban đầu: $st[0][i] = a[i]$.
- **Công thức quy hoạch động ($j \ge 1$)**: Để tìm $\min$ của đoạn độ dài $2^j$, ta chia đôi nó thành 2 nửa có độ dài $2^{j-1}$:
  $$\mathbf{st[j][i] = \min\Big(st[j - 1][i], \; st[j - 1][i + 2^{j-1}]\Big)}$$

### 2. Kỹ thuật đè đoạn (Overlap) để đạt truy vấn $O(1)$
- Đoạn cần truy vấn $[l, r]$ có độ dài $len = r - l + 1$.
- Ta chọn số mũ nguyên lớn nhất $k = \lfloor \log_2(len) 
floor \implies 2^k \le len < 2^{k+1}$.
- Ta phủ toàn bộ đoạn $[l, r]$ bằng 2 đoạn con có độ dài $2^k$:
  1. Đoạn từ đầu đi tới: $[l, \; l + 2^k - 1] \implies st[k][l]$
  2. Đoạn từ cuối lùi về: $[r - 2^k + 1, \; r] \implies st[k][r - 2^k + 1]$
- Nhờ tính chất lũy đẳng ($\min(x, x) = x$), phần chồng lấn ở giữa không làm thay đổi đáp số:
  $$\min_{[l, r]} a = \min\big(st[k][l], \; st[k][r - (1 \ll k) + 1]\big)$$

### 3. Tại sao dùng `31 - __builtin_clz(x)` thay vì `log2(x)`?
- `__builtin_clz(x)` (Count Leading Zeros) là lệnh hợp ngữ CPU (x86: `BSR` / `LZCNT`) chạy trong **đúng 1 chu kỳ vi xử lý**.
- Số 32-bit có bit 1 cao nhất tại vị trí $k$ thì phía trước có $31 - k$ bit 0. Do đó $\lfloor \log_2(x) 
floor = 31 - \text{clz}(x)$.
- Hàm `log2()` của `<cmath>` tính trên số thực `double`, tốn 30–50 chu kỳ và có thể sai số làm tròn (ví dụ $8 \to 7.9999999 \to 2$).

```cpp
struct SparseTable {
    int n, K;
    vector<vector<int>> st;

    SparseTable(const vector<int> &a) {
        n = a.size();
        K = 31 - __builtin_clz(n) + 1;
        st.assign(K, vector<int>(n));
        st[0] = a;

        for (int j = 1; j < K; ++j) {
            for (int i = 0; i + (1 << j) <= n; ++i) {
                st[j][i] = min(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
            }
        }
    }

    // Truy vấn min [l, r] (0-based) trong O(1)
    int query(int l, int r) const {
        int j = 31 - __builtin_clz(r - l + 1);
        return min(st[j][l], st[j][r - (1 << j) + 1]);
    }
};
```

---

# 2. Đồ thị cơ bản và đường đi ngắn nhất

## 2.1. Topological Sort Kahns BFS

### 1. Định nghĩa & Điều kiện tồn tại
- Thứ tự Topo là hoán vị các đỉnh trên đồ thị có hướng sao cho với mọi cung $u \to v$, đỉnh $u$ luôn xuất hiện **trước** đỉnh $v$.
- **Điều kiện**: Đồ thị phải là **DAG (Directed Acyclic Graph)** — không chứa chu trình có hướng.

### 2. Thuật toán Kahn (Bóc dần đỉnh nguồn)
- **Bán bậc vào `inDegree[u]`**: Số cung đi thẳng vào $u$.
  - Nếu `inDegree[u] == 0`: Đỉnh $u$ không bị phụ thuộc vào bất kỳ điều kiện tiên quyết nào $\implies$ Có thể thực hiện ngay $\implies$ Đẩy vào `queue`.
- **Cơ chế bóc tách**: Lấy $u$ ra khỏi queue, đưa vào kết quả `order`. Sau đó xóa các cạnh xuất phát từ $u$ bằng cách giảm bán bậc vào của các đỉnh kề: `--inDegree[v]`. Nếu `inDegree[v] == 0`, đẩy $v$ vào queue.
- **Phát hiện chu trình**: Các đỉnh nằm trên chu trình luôn có bán bậc vào $\ge 1$, không bao giờ được đẩy vào queue. Nếu `order.size() < n` $\implies$ Đồ thị **chắc chắn có chu trình có hướng**.

```cpp
vector<int> topoSort(int n, const vector<vector<int>> &adj) {
    vector<int> inDegree(n + 1, 0);
    for (int u = 1; u <= n; ++u)
        for (int v : adj[u]) inDegree[v]++;

    queue<int> q;
    for (int u = 1; u <= n; ++u)
        if (inDegree[u] == 0) q.push(u);

    vector<int> order;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : adj[u]) {
            if (--inDegree[v] == 0) q.push(v);
        }
    }

    if ((int)order.size() != n) return {}; // Có chu trình
    return order;
}
```

---

## 2.2. 0-1 BFS Đồ thị trọng số 0 và 1

### 1. Tại sao dùng `std::deque` thay cho Dijkstra?
- Dijkstra thông thường dùng `priority_queue` tốn $O(M \log N)$ vì phải duy trì thứ tự heap.
- Trên đồ thị có trọng số cạnh chỉ là $0$ hoặc $1$, khoảng cách từ nguồn đến các đỉnh trong hàng đợi tại mọi thời điểm chỉ chênh lệch nhau tối đa 1 đơn vị: $\{d, d+1\}$.
- Thay vì heap, ta dùng `std::deque`:
  - Cạnh trọng số $0$: Khoảng cách không đổi $\implies$ Đẩy vào **đầu hàng đợi (`push_front`)** để xét ngay.
  - Cạnh trọng số $1$: Khoảng cách tăng thêm 1 $\implies$ Đẩy vào **đuôi hàng đợi (`push_back`)**.
- Hàng đợi luôn luôn đảm bảo tính chất đơn điệu tăng dần $\implies$ Độ phức tạp tuyến tính **$O(V + E)$**.

```cpp
const int INF = 1e9;

vector<int> bfs01(int n, int startNode, const vector<vector<pair<int, int>>> &adj) {
    vector<int> dist(n + 1, INF);
    deque<int> dq;

    dist[startNode] = 0;
    dq.push_back(startNode);

    while (!dq.empty()) {
        int u = dq.front(); dq.pop_front();

        for (auto &[v, w] : adj[u]) {
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                if (w == 0) dq.push_front(v);
                else dq.push_back(v);
            }
        }
    }
    return dist;
}
```

---

## 2.3. Bellman-Ford và chu trình âm

### 1. Bản chất & Cơ chế nới lỏng (Relaxation)
- Đường đi ngắn nhất không chứa chu trình âm qua tối đa $N - 1$ cạnh.
- Do đó, thuật toán lặp đúng $N - 1$ lần, mỗi lần duyệt qua toàn bộ $M$ cạnh để nới lỏng:
  `if (dist[v] > dist[u] + w) dist[v] = dist[u] + w;`
- **Nhận diện chu trình âm**: Sau $N - 1$ lần lặp, nếu chạy thêm lần thứ $N$ mà **vẫn còn cạnh nào nới lỏng được**, điều đó chứng minh đồ thị **tồn tại chu trình âm**.

```cpp
struct Edge { int u, v; ll w; };
const ll INF_LL = 1e18;

// Trả về true nếu có chu trình âm đến được từ s: O(V * E)
bool bellmanFord(int n, int s, const vector<Edge> &edges, vector<ll> &dist) {
    dist.assign(n + 1, INF_LL);
    dist[s] = 0;

    for (int iter = 1; iter <= n - 1; ++iter) {
        bool any = false;
        for (const auto &e : edges) {
            if (dist[e.u] < INF_LL && dist[e.v] > dist[e.u] + e.w) {
                dist[e.v] = max(-INF_LL, dist[e.u] + e.w);
                any = true;
            }
        }
        if (!any) break; // Dừng sớm nếu không còn cạnh nào thay đổi
    }

    // Kiểm tra lần thứ n
    for (const auto &e : edges) {
        if (dist[e.u] < INF_LL && dist[e.v] > dist[e.u] + e.w)
            return true; // Có chu trình âm
    }
    return false;
}
```

---

## 2.4. Floyd-Warshall

### 1. Nguyên lý Quy hoạch động qua đỉnh trung gian
- `dist[i][j]` là độ dài đường đi ngắn nhất từ $i$ đến $j$ chỉ được phép đi qua các đỉnh trung gian thuộc tập $\{1, 2, \dots, k\}$.
- **BẮT BUỘC VÒNG LẶP `k` PHẢI Ở NGOÀI CÙNG**:
  Nếu đưa $k$ vào trong, bạn sẽ tính toán dựa trên các đường đi chưa được cập nhật đầy đủ từ các đỉnh trung gian trước đó, dẫn đến sai hoàn toàn.
- **Phát hiện chu trình âm**: Sau khi chạy xong, nếu tồn tại bất kỳ đỉnh $i$ nào có `dist[i][i] < 0`, tức là có một đường đi từ $i$ quay về chính nó với tổng trọng số âm.

```cpp
void floydWarshall(int n, vector<vector<ll>> &dist) {
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] < INF_LL && dist[k][j] < INF_LL) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}
```

---

## 2.5. LCA (Binary Lifting không sợ Stack Overflow)

### 1. Khử đệ quy sâu bằng BFS
- Cách cài đặt truyền thống dùng DFS đệ quy. Khi cây bị suy biến thành một đường thẳng $N = 3 \cdot 10^5$, hàm đệ quy $3 \cdot 10^5$ tầng sẽ gây **tràn bộ nhớ ngăn xếp (Stack Overflow)**.
- **Giải pháp**: Dùng hàng đợi **BFS** từ gốc để tính độ sâu `depth[u]` và cha trực tiếp `up[0][u]`. Tuyệt đối không dùng đệ quy.

### 2. Thuật toán nhảy nhị phân tìm LCA
- `up[j][u]` lưu tổ tiên thứ $2^j$ của nút $u$:
  $$\mathbf{up[j][u] = up[j - 1][up[j - 1][u]]}$$
- **Bước 1**: Đưa hai nút $u$ và $v$ về cùng một độ sâu (nhảy nút sâu hơn lên bằng các bước nhảy $2^j$).
- **Bước 2**: Nếu $u == v$, đó chính là LCA. Ngược lại, duyệt $j$ từ lớn về nhỏ, nếu `up[j][u] != up[j][v]` thì cho cả hai cùng nhảy lên. Điểm dừng cuối cùng sẽ ngay sát dưới LCA $\implies \text{LCA} = \text{up}[0][u]$.

```cpp
struct TreeLCA {
    int n, LOG;
    vector<int> depth;
    vector<vector<int>> up;

    TreeLCA(int n, int root, const vector<vector<int>> &adj) : n(n) {
        LOG = 31 - __builtin_clz(n) + 1;
        depth.assign(n + 1, 0);
        up.assign(LOG, vector<int>(n + 1, 0));

        queue<int> q;
        vector<bool> vis(n + 1, false);

        q.push(root);
        vis[root] = true;
        up[0][root] = root;

        // BFS an toàn 100% không tràn ngăn xếp
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (!vis[v]) {
                    vis[v] = true;
                    depth[v] = depth[u] + 1;
                    up[0][v] = u;
                    q.push(v);
                }
            }
        }

        // Tiền xử lý bảng nhảy nhị phân: O(N log N)
        for (int j = 1; j < LOG; ++j) {
            for (int i = 1; i <= n; ++i) {
                up[j][i] = up[j - 1][up[j - 1][i]];
            }
        }
    }

    // Truy vấn LCA(u, v): O(log N)
    int getLCA(int u, int v) const {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int j = 0; j < LOG; ++j) {
            if ((diff >> j) & 1) u = up[j][u];
        }
        if (u == v) return u;

        for (int j = LOG - 1; j >= 0; --j) {
            if (up[j][u] != up[j][v]) {
                u = up[j][u];
                v = up[j][v];
            }
        }
        return up[0][u];
    }

    int distance(int u, int v) const {
        return depth[u] + depth[v] - 2 * depth[getLCA(u, v)];
    }
};
```

---

## 2.6. 2-SAT Thỏa mãn mệnh đề logic

### 1. Mô hình hóa đồ thị suy diễn (Implication Graph)
Mỗi biến logic $x_i$ có 2 trạng thái đại diện bởi 2 nút trên đồ thị:
- Biến khẳng định $x_i$: Nút $2i$
- Biến phủ định $\neg x_i$: Nút $2i + 1$
Mệnh đề chuẩn tắc hội dạng $(u \lor v)$ có nghĩa là:
- Nếu $u$ sai ($\neg u$) thì $v$ bắt buộc phải đúng: $\neg u \implies v$.
- Nếu $v$ sai ($\neg v$) thì $u$ bắt buộc phải đúng: $\neg v \implies u$.
$\implies$ Ta thêm 2 cung có hướng vào đồ thị: $(\neg u \to v)$ và $(\neg v \to u)$.

### 2. Thuật toán Tarjan & Cách gán nghiệm
1. Chạy thuật toán Tarjan tìm các thành phần liên thông mạnh (SCC).
2. **Kiểm tra vô nghiệm**: Nếu tồn tại một biến $i$ mà cả $x_i$ và $\neg x_i$ cùng thuộc một SCC, điều đó có nghĩa $x_i \implies \neg x_i$ và $\neg x_i \implies x_i$ $\implies$ **Mâu thuẫn logic, hệ phương trình vô nghiệm**.
3. **Gán nghiệm**: Thuật toán Tarjan gán chỉ số SCC theo thứ tự Topo ngược. Do đó:
   - Nếu $\text{scc}[2i] < \text{scc}[2i + 1] \implies x_i = \mathbf{true}$.
   - Nếu $\text{scc}[2i] > \text{scc}[2i + 1] \implies x_i = \mathbf{false}$.

```cpp
struct TwoSat {
    int n; // Số biến (0..n-1)
    vector<vector<int>> adj;
    vector<int> dfn, low, scc;
    vector<bool> inStack;
    stack<int> st;
    int timer, sccCount;

    TwoSat(int n) : n(n), adj(2 * n), dfn(2 * n, 0), low(2 * n, 0), 
                    scc(2 * n, -1), inStack(2 * n, false), timer(0), sccCount(0) {}

    // Thêm mệnh đề: (u == valU) HOẶC (v == valV)
    void addClause(int u, bool valU, int v, bool valV) {
        int nodeU = 2 * u + (!valU);
        int nodeV = 2 * v + (!valV);
        int negU  = 2 * u + valU;
        int negV  = 2 * v + valV;
        adj[negU].push_back(nodeV);
        adj[negV].push_back(nodeU);
    }

    void dfs(int u) {
        dfn[u] = low[u] = ++timer;
        st.push(u);
        inStack[u] = true;
        for (int v : adj[u]) {
            if (!dfn[v]) {
                dfs(v);
                low[u] = min(low[u], low[v]);
            } else if (inStack[v]) {
                low[u] = min(low[u], dfn[v]);
            }
        }
        if (low[u] == dfn[u]) {
            sccCount++;
            while (true) {
                int v = st.top(); st.pop();
                inStack[v] = false;
                scc[v] = sccCount;
                if (v == u) break;
            }
        }
    }

    bool solve(vector<bool> &assignment) {
        for (int i = 0; i < 2 * n; ++i) {
            if (!dfn[i]) dfs(i);
        }
        assignment.assign(n, false);
        for (int i = 0; i < n; ++i) {
            if (scc[2 * i] == scc[2 * i + 1]) return false; // Vô nghiệm
            assignment[i] = (scc[2 * i] < scc[2 * i + 1]);
        }
        return true;
    }
};
```

---

# 3. Luồng cực đại và cặp ghép

## 3.1. Dinic Max-Flow

### 1. Hai giai đoạn trong thuật toán Dinic
Thuật toán Dinic vượt trội hơn Edmonds-Karp nhờ chia việc tìm luồng thành 2 pha lặp đi lặp lại:
1. **Pha 1 - BFS dựng đồ thị phân tầng (Level Graph)**:
   - Tính khoảng cách ngắn nhất `level[u]` từ nguồn $s$ đến mọi đỉnh trên đồ thị thặng dư.
   - Chỉ cho phép dòng luồng đi từ tầng $k$ sang tầng $k+1$ (`level[v] == level[u] + 1`).
2. **Pha 2 - DFS tìm luồng cản (Blocking Flow)**:
   - Dùng DFS đẩy luồng dọc theo các cạnh thỏa mãn phân tầng cho đến khi không còn đẩy thêm được nữa.

### 2. Vai trò sống còn của con trỏ `ptr[]`
Trong hàm DFS, dòng lệnh `for (int &cid = ptr[u]; cid < (int)adj[u].size(); ++cid)`:
- Dấu tham chiếu `int &cid = ptr[u]` cực kỳ quan trọng!
- Nó lưu lại chỉ số cạnh mà nút $u$ đang duyệt dở. Nếu một cạnh đã bão hòa hoặc không thể dẫn luồng tới đích, các lần gọi DFS sau sẽ **bỏ qua ngay lập tức mà không duyệt lại từ đầu**.
- Nếu thiếu `ptr[]`, độ phức tạp sẽ bị thoái hóa và nhận kết quả **Time Limit Exceeded (TLE)**.
- **Độ phức tạp**: $O(V^2 E)$, trên mạng luồng đơn vị (Unit Networks) đạt $O(E \sqrt{V})$.

```cpp
struct Dinic {
    struct Edge {
        int to;
        ll cap, flow;
        int rev;
    };

    int n, s, t;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n, int s, int t) : n(n), s(s), t(t), adj(n + 1), level(n + 1), ptr(n + 1) {}

    void addEdge(int from, int to, ll cap) {
        adj[from].push_back({to, cap, 0, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
    }

    bool bfs() {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q; q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : adj[u]) {
                if (e.cap - e.flow > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    ll dfs(int u, ll pushed) {
        if (pushed == 0 || u == t) return pushed;
        for (int &cid = ptr[u]; cid < (int)adj[u].size(); ++cid) {
            auto &e = adj[u][cid];
            int tr = e.to;
            if (level[u] + 1 != level[tr] || e.cap - e.flow == 0) continue;
            ll tr_pushed = dfs(tr, min(pushed, e.cap - e.flow));
            if (tr_pushed == 0) continue;
            e.flow += tr_pushed;
            adj[tr][e.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    ll maxFlow() {
        ll flow = 0;
        while (bfs()) {
            fill(ptr.begin(), ptr.end(), 0);
            while (ll pushed = dfs(s, INF_LL)) {
                flow += pushed;
            }
        }
        return flow;
    }
};
```

---

## 3.2. Hopcroft-Karp Bipartite Matching

### 1. Bản chất đường mở (Augmenting Path)
- Một đường đi xen kẽ giữa các cạnh chưa ghép và đã ghép, bắt đầu và kết thúc tại 2 đỉnh chưa ghép ở 2 phía. Đảo ngược trạng thái ghép trên đường này sẽ làm số lượng cặp ghép tăng thêm đúng 1.
- Thuật toán Kuhn truyền thống tìm từng đường mở một cách tuần tự mất $O(V \cdot E)$.
- **Hopcroft-Karp**: Dùng **BFS tìm tập hợp tất cả các đường mở ngắn nhất cùng một lúc**, sau đó dùng **DFS tăng luồng đồng thời** trên các đường mở không giao nhau.
- **Độ phức tạp**: Đạt ngưỡng tối ưu lý thuyết **$O(E \sqrt{V})$**.

```cpp
struct HopcroftKarp {
    int n, m; // n đỉnh bên trái (1..n), m đỉnh bên phải (1..m)
    vector<vector<int>> adj;
    vector<int> pairU, pairV, dist;

    HopcroftKarp(int n, int m) : n(n), m(m), adj(n + 1), pairU(n + 1, 0), 
                                pairV(m + 1, 0), dist(n + 1, 0) {}

    void addEdge(int u, int v) {
        adj[u].push_back(v);
    }

    bool bfs() {
        queue<int> q;
        for (int u = 1; u <= n; ++u) {
            if (pairU[u] == 0) {
                dist[u] = 0;
                q.push(u);
            } else dist[u] = INF;
        }
        dist[0] = INF;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            if (dist[u] < dist[0]) {
                for (int v : adj[u]) {
                    if (dist[pairV[v]] == INF) {
                        dist[pairV[v]] = dist[u] + 1;
                        q.push(pairV[v]);
                    }
                }
            }
        }
        return dist[0] != INF;
    }

    bool dfs(int u) {
        if (u != 0) {
            for (int v : adj[u]) {
                if (dist[pairV[v]] == dist[u] + 1) {
                    if (dfs(pairV[v])) {
                        pairV[v] = u;
                        pairU[u] = v;
                        return true;
                    }
                }
            }
            dist[u] = INF;
            return false;
        }
        return true;
    }

    int maxMatching() {
        int matching = 0;
        while (bfs()) {
            for (int u = 1; u <= n; ++u) {
                if (pairU[u] == 0 && dfs(u)) matching++;
            }
        }
        return matching;
    }
};
```

---

# 4. Hình học tính toán

## 4.1. Điểm Vector và Tích có hướng CCW

### 1. Tích vô hướng (Dot Product)
$$\vec{A} \cdot \vec{B} = x_A x_B + y_A y_B = |\vec{A}| \cdot |\vec{B}| \cdot \cos(\theta)$$
- $> 0$: Góc nhọn ($\theta < 90^\circ$).
- $= 0$: Hai vector vuông góc nhau.
- $< 0$: Góc tù ($\theta > 90^\circ$).

### 2. Tích có hướng (Cross Product) & Hàm `ccw`
$$\vec{A} \times \vec{B} = x_A y_B - x_B y_A = |\vec{A}| \cdot |\vec{B}| \cdot \sin(\theta)$$
Giá trị đại số của tích có hướng cho biết hướng quay từ vector $\vec{A}$ sang vector $\vec{B}$:
- $> 0$: **Rẽ trái (Counter-Clockwise - CCW)**, ngược chiều kim đồng hồ.
- $< 0$: **Rẽ phải (Clockwise - CW)**, cùng chiều kim đồng hồ.
- $= 0$: Hai vector **thẳng hàng (Collinear)**.

```cpp
struct Point {
    ll x, y;
    Point operator-(const Point &other) const { return {x - other.x, y - other.y}; }
    Point operator+(const Point &other) const { return {x + other.x, y + other.y}; }
    ll dot(const Point &other) const { return x * other.x + y * other.y; }
    ll cross(const Point &other) const { return x * other.y - y * other.x; }
    bool operator<(const Point &other) const {
        return x < other.x || (x == other.x && y < other.y);
    }
    bool operator==(const Point &other) const {
        return x == other.x && y == other.y;
    }
};

// Kiểm tra hướng rẽ của 3 điểm a -> b -> c
ll ccw(Point a, Point b, Point c) {
    return (b - a).cross(c - a);
}
```

---

## 4.2. Giao hai đoạn thẳng Segment Intersection

### 1. Điều kiện cắt nhau chuẩn xác
Hai đoạn thẳng $AB$ và $CD$ cắt nhau khi và chỉ khi thỏa mãn một trong hai trường hợp:
1. **Cắt thông thường (Proper Intersection)**:
   - Điểm $C$ và $D$ nằm về **hai phía đối diện** của đường thẳng $AB$: $\text{ccw}(A, B, C) \times \text{ccw}(A, B, D) < 0$.
   - **ĐỒNG THỜI**, điểm $A$ và $B$ nằm về hai phía đối diện của đường thẳng $CD$: $\text{ccw}(C, D, A) \times \text{ccw}(C, D, B) < 0$.
2. **Cắt suy biến (Điểm nằm trên đoạn)**:
   Một trong các đầu mút thẳng hàng với đoạn kia và nằm gọn trong hình hộp chữ nhật giới hạn (Bounding Box).

```cpp
bool onSegment(Point p, Point a, Point b) {
    return ccw(a, b, p) == 0 &&
           min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x) &&
           min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y);
}

bool intersect(Point a, Point b, Point c, Point d) {
    ll cp1 = ccw(a, b, c), cp2 = ccw(a, b, d);
    ll cp3 = ccw(c, d, a), cp4 = ccw(c, d, b);

    if (((cp1 > 0 && cp2 < 0) || (cp1 < 0 && cp2 > 0)) &&
        ((cp3 > 0 && cp4 < 0) || (cp3 < 0 && cp4 > 0)))
        return true;

    if (onSegment(c, a, b)) return true;
    if (onSegment(d, a, b)) return true;
    if (onSegment(a, c, d)) return true;
    if (onSegment(b, c, d)) return true;

    return false;
}
```

---

## 4.3. Điểm nằm trong đa giác Point in Polygon

### 1. Thuật toán bắn tia (Ray Casting Algorithm)
- Từ điểm cần kiểm tra $P$, ta tưởng tượng bắn một tia nằm ngang sang vô cực bên phải: $y = P.y, x \ge P.x$.
- Đếm số lần tia này cắt các cạnh của đa giác:
  - Nếu số giao điểm là **lẻ** $\implies$ Điểm nằm **bên trong (INSIDE)**.
  - Nếu số giao điểm là **chẵn** $\implies$ Điểm nằm **bên ngoài (OUTSIDE)**.
- **Xử lý điểm trên đỉnh/cạnh**: Quy ước cạnh $[A, B]$ với $A.y \le P.y < B.y$ (nửa khoảng nửa đoạn) để tránh việc một tia đi qua đỉnh của đa giác bị đếm trùng 2 lần.

```cpp
enum Position { OUTSIDE, BOUNDARY, INSIDE };

Position pointInPolygon(Point p, const vector<Point> &poly) {
    int n = poly.size();
    bool inside = false;

    for (int i = 0; i < n; ++i) {
        Point a = poly[i], b = poly[(i + 1) % n];
        if (onSegment(p, a, b)) return BOUNDARY;

        if (a.y > b.y) swap(a, b);
        if (a.y <= p.y && p.y < b.y) {
            if (ccw(a, b, p) > 0) inside = !inside;
        }
    }
    return inside ? INSIDE : OUTSIDE;
}
```

---

## 4.4. Bao lồi Andrews Monotone Chain

### 1. Tại sao dùng Andrew thay vì Graham Scan?
- **Graham Scan**: Đòi hỏi sắp xếp theo góc cực (Polar Angle), dễ sai số số thực hoặc cồng kềnh khi viết hàm so sánh cross product.
- **Andrew's Monotone Chain**: Chỉ sắp xếp theo tọa độ Descartes thông thường $(x, y)$. Cực kỳ ổn định và ngắn gọn.
- **Cơ chế**:
  - Dựng **Vỏ dưới (Lower Hull)**: Đi từ trái sang phải. Nếu gặp điểm làm cho đường đi rẽ phải (`ccw <= 0`), ta loại bỏ điểm trước đó khỏi bao lồi.
  - Dựng **Vỏ trên (Upper Hull)**: Đi ngược lại từ phải sang trái với cùng quy tắc.
  - Ghép 2 vỏ lại ta được bao lồi hoàn chỉnh trong $O(N \log N)$.

```cpp
vector<Point> convexHull(vector<Point> pts) {
    int n = pts.size(), k = 0;
    if (n <= 2) return pts;
    sort(pts.begin(), pts.end());

    vector<Point> h(2 * n);

    // Vỏ dưới
    for (int i = 0; i < n; ++i) {
        while (k >= 2 && ccw(h[k - 2], h[k - 1], pts[i]) <= 0) k--;
        h[k++] = pts[i];
    }

    // Vỏ trên
    for (int i = n - 2, t = k + 1; i >= 0; --i) {
        while (k >= t && ccw(h[k - 2], h[k - 1], pts[i]) <= 0) k--;
        h[k++] = pts[i];
    }

    h.resize(k - 1);
    return h;
}
```

---

# 5. Xâu ký tự

## 5.1. Manacher Tìm mọi Palindrome ON

### 1. Kỹ thuật chèn ký tự đặc biệt `'#'`
Một xâu đối xứng có thể có độ dài lẻ (tâm tại 1 ký tự, ví dụ `aba`) hoặc chẵn (tâm nằm giữa 2 ký tự, ví dụ `abba`).
- Bằng cách chèn ký tự `'#'` vào giữa mọi ký tự:
  - `aba` $\to$ `^ # a # b # a # $` (độ dài lẻ, tâm tại `b`)
  - `abba` $\to$ `^ # a # b # # b # a # $` (độ dài lẻ, tâm tại `#` ở giữa)
- Tất cả các palindrome đều quy về độ dài lẻ trên xâu mới! Hai ký tự lính canh `^` và `$` ở hai đầu giúp thuật toán không bao giờ chạy tràn ra ngoài biên mảng.

### 2. Tận dụng tâm đối xứng để đạt $O(N)$
Thuật toán duy trì:
- $C$: Tâm của palindrome có biên phải vươn xa nhất hiện tại.
- $R$: Biên phải xa nhất đạt được ($R = C + P[C]$).
Khi đang ở vị trí $i < R$, ta tìm điểm đối xứng của $i$ qua tâm $C$:
$$i' = 2C - i$$
Theo tính chất đối xứng, bán kính palindrome tại $i$ tối thiểu bằng bán kính tại $i'$:
$$P[i] \ge \min(R - i, \; P[i'])$$
Sau đó ta chỉ cần mở rộng tiếp từ biên đã biết. Vì con trỏ $R$ chỉ tăng đơn điệu từ đầu đến cuối xâu, tổng số phép so sánh ký tự không vượt quá $2N \implies$ Độ phức tạp đúng **$O(N)$**.

```cpp
vector<int> manacher(const string &s) {
    string t = "^";
    for (char c : s) { t += '#'; t += c; }
    t += "#$";

    int m = t.size();
    vector<int> p(m, 0);
    int c = 0, r = 0;

    for (int i = 1; i < m - 1; ++i) {
        int i_mirror = 2 * c - i;
        if (r > i) p[i] = min(r - i, p[i_mirror]);

        while (t[i + 1 + p[i]] == t[i - 1 - p[i]]) p[i]++;

        if (i + p[i] > r) {
            c = i;
            r = i + p[i];
        }
    }
    return p;
}
```

---

## 5.2. Aho-Corasick Automaton

### 1. Bản chất: Kết hợp Trie và KMP
- KMP tìm 1 mẫu trong văn bản bằng hàm tiền tố $\pi$.
- Aho-Corasick tìm **đồng thời hàng nghìn mẫu** trong văn bản bằng cách xây dựng **Cây Trie chứa tất cả các mẫu**, sau đó bổ sung các **liên kết hỏng (Failure Links)** tương tự như KMP.

### 2. Ý nghĩa của Failure Link
- `link[u]`: Nút đại diện cho hậu tố thực sự dài nhất của xâu tại $u$ mà cũng là tiền tố của một mẫu nào đó trong Trie.
- **Hoàn thiện Automaton (DFA)**:
  Nếu từ nút $u$ không có cạnh đi qua ký tự $c$, ta gán trực tiếp:
  `tree[u].next[c] = tree[fail].next[c]`.
  Điều này biến cây Trie thành một máy trạng thái hữu hạn hoàn chỉnh: Khi đọc văn bản, mỗi ký tự ta chỉ tốn đúng **1 bước chuyển trạng thái $O(1)$** mà không cần vòng lặp `while` lùi lại!

```cpp
struct AhoCorasick {
    static const int ALPHABET = 26;
    struct Node {
        int next[ALPHABET];
        int link = 0;      // Failure link
        int exitLink = 0;  // Link đến mẫu kết thúc gần nhất
        vector<int> patternIndices;
        Node() { fill(next, next + ALPHABET, 0); }
    };

    vector<Node> tree;

    AhoCorasick() { tree.emplace_back(); }

    void insert(const string &s, int id) {
        int u = 0;
        for (char c : s) {
            int ch = c - 'a';
            if (!tree[u].next[ch]) {
                tree[u].next[ch] = tree.size();
                tree.emplace_back();
            }
            u = tree[u].next[ch];
        }
        tree[u].patternIndices.push_back(id);
    }

    void build() {
        queue<int> q;
        for (int c = 0; c < ALPHABET; ++c) {
            if (tree[0].next[c]) q.push(tree[0].next[c]);
        }
        while (!q.empty()) {
            int u = q.front(); q.pop();
            int fail = tree[u].link;

            tree[u].exitLink = !tree[fail].patternIndices.empty() ? fail : tree[fail].exitLink;

            for (int c = 0; c < ALPHABET; ++c) {
                if (tree[u].next[c]) {
                    tree[tree[u].next[c]].link = tree[fail].next[c];
                    q.push(tree[u].next[c]);
                } else {
                    tree[u].next[c] = tree[fail].next[c]; // Hoàn thiện Automaton
                }
            }
        }
    }
};
```

---

# 6. Số học và tổ hợp cao cấp

## 6.1. Tổ hợp modulo nguyên tố O1 Fact và InvFact

### 1. Nghịch đảo Modular bằng Định lý Fermat nhỏ
Với $MOD$ là số nguyên tố và $\gcd(a, MOD) = 1$:
$$a^{MOD - 1} \equiv 1 \pmod{MOD} \implies a \cdot a^{MOD - 2} \equiv 1 \pmod{MOD}$$
Do đó, nghịch đảo modulo của $a$ là:
$$\mathbf{a^{-1} \equiv a^{MOD - 2} \pmod{MOD}}$$

### 2. Kỹ thuật tính nghịch đảo giai thừa ngược trong $O(N)$
Nếu tính nghịch đảo cho từng số $1 \dots N$ bằng hàm lũy thừa `power(i, MOD - 2)`, ta sẽ mất $O(N \log MOD)$.
- **Cách tối ưu $O(N)$**:
  Ta chỉ tính nghịch đảo **1 lần duy nhất** cho phần tử cuối cùng:
  $$\text{invFact}[N] = (N!)^{-1} \pmod{MOD}$$
  Sau đó tính lùi ngược về $0$ nhờ tính chất:
  $$(i - 1)!^{-1} \equiv i!^{-1} \times i \pmod{MOD}$$
  Truy vấn tổ hợp $C(n, r) = \frac{n!}{r!(n-r)!}$ chỉ mất đúng **1 phép nhân $O(1)$**:
  `fact[n] * invFact[r] % MOD * invFact[n - r] % MOD`.

```cpp
const int MOD = 1e9 + 7;
const int MAX = 1e6 + 5;

ll fact[MAX], invFact[MAX];

ll power(ll base, ll exp) {
    ll res = 1; base %= MOD;
    for (; exp > 0; exp >>= 1, base = base * base % MOD)
        if (exp & 1) res = res * base % MOD;
    return res;
}

ll modInverse(ll n) {
    return power(n, MOD - 2);
}

void precomputeComb() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = fact[i - 1] * i % MOD;

    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 0; --i) {
        invFact[i] = invFact[i + 1] * (i + 1) % MOD;
    }
}

ll nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

ll nPr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[n - r] % MOD;
}
```

---

## 6.2. Chinese Remainder Theorem CRT tổng quát

### 1. Giải hệ phương trình đồng dư khi $\gcd(m_1, m_2) > 1$
Định lý số dư Trung Hoa cổ điển chỉ áp dụng khi các modulo $m_i$ đôi một nguyên tố cùng nhau.
Trong các bài thi lập trình, đề bài thường cho các modulo **không nguyên tố cùng nhau**:
$$\begin{cases} x \equiv r_1 \pmod{m_1} \\ x \equiv r_2 \pmod{m_2} \end{cases}$$
Viết lại dưới dạng phương trình nghiệm nguyên:
$$x = m_1 \cdot p + r_1 = m_2 \cdot q + r_2 \implies m_1 \cdot p - m_2 \cdot q = r_2 - r_1$$
Đây là phương trình Diophantine tuyến tính:
- Gọi $g = \gcd(m_1, m_2)$.
- **Điều kiện có nghiệm**: Hiệu số dư $(r_2 - r_1)$ **bắt buộc phải chia hết cho $g$**. Nếu không chia hết $\implies$ Hệ vô nghiệm!
- Tìm được $p$ bằng Extended GCD, nghiệm gộp mới sẽ có chu kỳ là:
  $$\text{mod} = \text{lcm}(m_1, m_2) = \frac{m_1 \cdot m_2}{g}$$

```cpp
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

// Gộp 2 đồng dư thành 1 đồng dư mới: x = rem (mod mod)
bool crtMerge(ll r1, ll m1, ll r2, ll m2, ll &rem, ll &mod) {
    ll x, y;
    ll g = extgcd(m1, m2, x, y);
    if ((r2 - r1) % g != 0) return false; // Vô nghiệm

    ll step = m2 / g;
    ll k = ((r2 - r1) / g) % step * (x % step) % step;
    if (k < 0) k += step;

    mod = m1 / g * m2;
    rem = (r1 + k * m1) % mod;
    if (rem < 0) rem += mod;
    return true;
}
```

---

## 6.3. Pollard Rho Phân tích thừa số ON14

### 1. Nghịch lý ngày sinh (Birthday Paradox)
- Thay vì thử chia tất cả các số đến $\sqrt{N}$ mất $O(\sqrt{N})$ (với $N = 10^{18}$, $\sqrt{N} = 10^9$ sẽ bị TLE), Pollard's Rho sinh dãy số giả ngẫu nhiên:
  $$x_{k+1} = (x_k^2 + c) \pmod N$$
- Theo nghịch lý ngày sinh, chu trình modulo một ước $p$ của $N$ sẽ xuất hiện sau khoảng **$O(\sqrt{p}) \le O(N^{1/4})$** bước!
- Tại mỗi bước, ta tính $\gcd(|x - y|, N)$. Nếu $1 < \gcd < N$, ta đã tìm ra một **ước số nguyên tố thực sự của $N$**!
- Thuật toán tìm chu trình của Brent nhanh hơn 20–30% so với phương pháp rùa và thỏ của Floyd.

### 2. Miller-Rabin 64-bit chuẩn xác định
- Để thuật toán Pollard's Rho dừng đúng lúc, ta cần hàm kiểm tra số nguyên tố nhanh $O(\log N)$.
- Tập **12 cơ sở nguyên tố đầu tiên** đảm bảo kiểm tra số nguyên tố chính xác 100% cho mọi số nguyên 64-bit ($N \le 2^{64}$):
  $$\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37\}$$

```cpp
using u128 = __uint128_t;

ll mulMod(ll a, ll b, ll m) {
    return (u128)a * b % m;
}

ll powMod(ll a, ll b, ll m) {
    ll res = 1; a %= m;
    for (; b > 0; b >>= 1, a = mulMod(a, a, m))
        if (b & 1) res = mulMod(res, a, m);
    return res;
}

bool isPrime64(ll n) {
    if (n < 2) return false;
    static const ll bases[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (ll p : bases) if (n % p == 0) return n == p;
    ll d = n - 1; int s = 0;
    while ((d & 1) == 0) { d >>= 1; s++; }
    for (ll a : bases) {
        ll x = powMod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (int r = 1; r < s; ++r) {
            x = mulMod(x, x, n);
            if (x == n - 1) { composite = false; break; }
        }
        if (composite) return false;
    }
    return true;
}

ll pollardRho(ll n) {
    if (n % 2 == 0) return 2;
    if (isPrime64(n)) return n;

    auto f = [](ll x, ll c, ll n) {
        return (mulMod(x, x, n) + c) % n;
    };

    ll x = 2, y = 2, c = 1, g = 1;
    while (g == 1) {
        ll power = 1, lam = 1;
        y = x;
        while (g == 1) {
            if (power == lam) {
                x = y;
                power <<= 1;
                lam = 0;
            }
            y = f(y, c, n);
            lam++;
            g = std::gcd(std::abs(x - y), n);
        }
        if (g == n) {
            x = rand() % (n - 2) + 2;
            c = rand() % (n - 1) + 1;
            g = 1;
        }
    }
    return g;
}

// Phân tích n thành các thừa số nguyên tố: O(N^(1/4))
void factorize(ll n, vector<ll> &factors) {
    if (n == 1) return;
    if (isPrime64(n)) {
        factors.push_back(n);
        return;
    }
    ll d = pollardRho(n);
    factorize(d, factors);
    factorize(n / d, factors);
}
```
