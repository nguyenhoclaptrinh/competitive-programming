# ICPC HCMUS Miki Cheatsheet

## Mục lục

- [1. Cấu trúc dữ liệu](#1-cấu-trúc-dữ-liệu)
  - [1.1. Segment tree](#11-segment-tree)
  - [1.2. Segment tree lazy](#12-segment-tree-lazy)
  - [1.3. Segment tree vector](#13-segment-tree-vector)
  - [1.4. Segment tree Kth](#14-segment-tree-kth)
  - [1.5. Segment tree 2D](#15-segment-tree-2d)
  - [1.6. Ordered set](#16-ordered-set)
  - [1.7. Trie](#17-trie)
  - [1.8. Trie Multiset](#18-trie-multiset)
- [2. Đồ thị](#2-đồ-thị)
  - [2.1. Dijkstra](#21-dijkstra)
  - [2.2. Tìm khớp cầu](#22-tìm-khớp-cầu)
  - [2.3. Cây khung nhỏ nhất – Kruskal](#23-cây-khung-nhỏ-nhất--kruskal)
  - [2.4. Tìm TPLT mạnh – Tarjan](#24-tìm-tplt-mạnh--tarjan)
  - [2.5. LCA](#25-lca)
- [3. Số học](#3-số-học)
  - [3.1. Sàng nguyên tố](#31-sàng-nguyên-tố)
  - [3.2. Kiểm tra SNT – Miller Rabin](#32-kiểm-tra-snt--miller-rabin)
  - [3.3. Bignum add, subtract, multiply](#33-bignum-add-subtract-multiply)
  - [3.4. Bignum mod](#34-bignum-mod)
  - [3.5. Bignum div](#35-bignum-div)
  - [3.6. Tổ hợp – Chỉnh hợp](#36-tổ-hợp--chỉnh-hợp)
  - [3.7. Extended GCD](#37-extended-gcd)
  - [3.8. Diophantine](#38-diophantine)
  - [3.9. Nhân nhanh (O(log) + O(1))](#39-nhân-nhanh-olog--o1)
  - [3.10. Luỹ thừa nhanh (O(log))](#310-luỹ-thừa-nhanh-olog)
  - [3.11. Inverse mod](#311-inverse-mod)
  - [3.12. Phi hàm Euler](#312-phi-hàm-euler)
  - [3.13. Nhân ma trận](#313-nhân-ma-trận)
- [4. Hình học](#4-hình-học)
  - [4.1. Viết đường thẳng](#41-viết-đường-thẳng)
  - [4.2. Kiểm tra điểm thuộc tia](#42-kiểm-tra-điểm-thuộc-tia)
  - [4.3. Tìm điểm giao giữa 2 đường thẳng](#43-tìm-điểm-giao-giữa-2-đường-thẳng)
- [5. Quy hoạch động](#5-quy-hoạch-động)
  - [5.1. Dãy con chung tăng dài nhất](#51-dãy-con-chung-tăng-dài-nhất)
  - [5.2. Số lượng số đoạn [L, R] có tổng các chữ số bằng K](#52-số-lượng-số-đoạn-l-r-có-tổng-các-chữ-số-bằng-k)
  - [5.3. Tìm mỗi hàng, mỗi cột 1 phần tử sao cho tổng lớn nhất (bitmask)](#53-tìm-mỗi-hàng-mỗi-cột-1-phần-tử-sao-cho-tổng-lớn-nhất-bitmask)
- [6. Xâu](#6-xâu)
  - [6.1. KMP](#61-kmp)
  - [6.2. Z-Function](#62-z-function)
- [7. Khác](#7-khác)
  - [7.1. Hash cặp số, toạ độ](#71-hash-cặp-số-toạ-độ)
  - [7.2. Hash phân số](#72-hash-phân-số)
  - [7.3. Hash xâu](#73-hash-xâu)
  - [7.4. Min, max, gcd trong đoạn tịnh tiến](#74-min-max-gcd-trong-đoạn-tịnh-tiến)

---

# 1. Cấu trúc dữ liệu

## 1.1. Segment tree

```cpp
// Cập nhật điểm, truy vấn tổng đoạn
int n, a[N];
int t[N << 2];

void build(int id, int l, int r)
{
    if (l == r) {t[id] = a[l]; return;}
    int mid = (l + r) / 2;
    build(id*2, l, mid);
    build(id*2 + 1, mid + 1, r);
    t[id] = t[id*2] + t[id*2 + 1];
}

int get(int id, int l, int r, int u, int v)
{
    if (r < u || l > v) return 0;
    if (u <= l && r <= v)
        return t[id];

    int mid = (l + r) / 2;
    int t1 = get(id*2, l, mid, u, v),
        t2 = get(id*2 + 1, mid + 1, r, u, v);
    return t1 + t2;
}

void upd(int id, int l, int r, int p, int val)
{
    if (p < l || p > r) return;
    if (l == r) return void(t[id] = a[p] = val);
    int mid = (l + r) / 2;
    upd(id*2, l, mid, p, val);
    upd(id*2 + 1, mid + 1, p, val);
    t[id] = t[id*2] + t[id*2 + 1];
}
```

## 1.2. Segment tree lazy

```cpp
struct LazyIT {int val, laz;} t[N << 4];
void down(int id)
{
    t[id*2].val     += t[id].laz;
    t[id*2].laz     += t[id].laz;
    t[id*2 + 1].val += t[id].laz;
    t[id*2 + 1].laz += t[id].laz;
    t[id].laz = 0;
}

void upd(int id, int l, int r, int u, int v, int val)
{
    if (u > r || v < l) return;
    if (u <= l && r <= v) {
        t[id].val += val;
        t[id].laz += val;
        return;
    }

    down(id);

    int mid = (l + r) / 2;
    upd(id*2, l, mid, u, v, val);
    upd(id*2 + 1, mid + 1, r, u, v, val);

    t[id].val = max(t[id*2].val, t[id*2 + 1].val);
}

int get(int id, int l, int r, int u, int v)
{
    if (u > r || v < l) return 0;
    if (u <= l && r <= v)
        return t[id].val;

    int mid = (l + r) / 2;
    down(id);

    int t1 = get(id*2, l, mid, u, v),
        t2 = get(id*2 + 1, mid + 1, r, u, v);

    return max(t1, t2);
}
```

## 1.3. Segment tree vector

```cpp
// Truy vấn số phần tử trong đoạn LỚN HƠN K
// Không cập nhật
int n, a[N], q;
vector<int> t[N << 4];
void build(int id, int l, int r)
{
    if (l == r) {t[id].pub(a[l]); return;}
    int mid = (l + r) / 2;
    build(id*2, l, mid);
    build(id*2 + 1, mid + 1, r);

    int sz1 = t[id*2].size(), sz2 = t[id*2 + 1].size();

    t[id].reserve(sz1 + sz2);
    int i = 0, j = 0;
    while(i < sz1 && j < sz2)
    {
        if (t[id*2][i] < t[id*2 + 1][j])
t[id].pub(t[id*2][i++]);
        else
t[id].pub(t[id*2 + 1][j++]);
    }
    while(i < sz1) t[id].pub(t[id*2][i++]);
    while(j < sz2) t[id].pub(t[id*2 + 1][j++]);
}

// return number of elements > val
int get(int id, int l, int r, int u, int v, int val)
{
    if (r < u || l > v) return 0;
    if (u <= l && r <= v)
        return int(t[id].end() - upper_bound(t[id].begin(), t[id].end(), val));
    int mid = (l + r) / 2;
    int t1 = get(id*2, l, mid, u, v, val),
        t2 = get(id*2 + 1, mid + 1, r, u, v, val);
    return t1 + t2;
}
```

## 1.4. Segment tree Kth

```cpp
// tìm vị trí số nhỏ thứ Kth trong đoạn [L, R]
int n, q;
ii a[N];
vi t[N << 2];
void Inp()
{
    cin >> n >> q;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i].fi;
        a[i].se = i;
    }
}

void build(int id, int l, int r)
{
    if (l == r) return void(t[id].pub(a[l].se));
    int mid = (l + r) / 2;
    build(id*2, l, mid);
    build(id*2 + 1, mid + 1, r);
    merge(all(t[id*2]), all(t[id*2 + 1]), back_inserter(t[id]));
}

// tìm vị trí số nhỏ thứ Kth trong đoạn [L, R]
int get(int id, int l, int r, int u, int v, int kth)
{
    if (l == r) return t[id].back();
    int cnt = upper_bound(all(t[id*2]), v)
            - lower_bound(all(t[id*2]), u);

    int mid = (l + r) / 2;
    if (cnt >= kth)
        return get(id*2, l, mid, u, v, kth);
    else
        return get(id*2 + 1, mid + 1, r, u, v, kth - cnt);
}
void Solve()
{
    sort(a + 1, a + n + 1, [](const ii &x, const ii &y) {
        return x.fi < y.fi;
    });

    build(1, 1, n);

    sort(a + 1, a + n + 1, [](const ii &x, const ii &y) {
        return x.se < y.se;
    });

    while(q-- > 0) {
        int l, r; cin >> l >> r >> k;
        cout << get(1, 1, n, l, r, k);
    }
}
```

## 1.5. Segment tree 2D

```cpp
// buildx(1, 1, n)
// -> xây dựng cây IT2D

// updatex(1, 1, n, x, y, w)
// -> thay giá trị tại ô (x, y) thành w

// getx(1, 1, n, x1, y1, x2, y2)
// -> tính tổng giá trị từ ô (x1, y1) đến (x2, y2)

int n, m;
ll a[N][N], t[N << 2][N << 2];
void buildy(int idX, int lx, int rx, int idY, int ly, int ry)
{
    if (ly == ry) {
        if (lx == rx)
            return void(t[idX][idY] = a[lx][ly]);
        else
            return void(t[idX][idY] = t[idX*2][idY] + t[idX*2 + 1][idY]);
    }

    int mid = (ly + ry) / 2;
    buildy(idX, lx, rx, idY*2, ly, mid);
    buildy(idX, lx, rx, idY*2 + 1, mid + 1, ry);

    t[idX][idY] = t[idX][idY*2] + t[idX][idY*2 + 1];
}

void buildx(int idX, int lx, int rx)
{
    if (lx == rx) {
        buildy(idX, lx, rx, 1, 1, m);
        return;
    }

    int mid = (lx + rx) / 2;
    buildx(idX*2, lx, mid);
    buildx(idX*2 + 1, mid + 1, rx);

    buildy(idX, lx, rx, 1, 1, m);
}

void updy(int idX, int lx, int rx, int idY, int ly, int ry, int x, int y, ll val)
{
    if (ly == ry) {
        if (lx == rx)
            return void(t[idX][idY] = val);
        else
            return void(t[idX][idY] = t[idX*2][idY] + t[idX*2 + 1][idY]);
    }

    int mid = (ly + ry) / 2;
    if (ly <= y && y <= mid)
        updy(idX, lx, rx, idY*2, ly, mid, x, y, val);
    else                    
        updy(idX, lx, rx, idY*2 + 1, mid + 1, ry, x, y, val);

    t[idX][idY] = t[idX][idY*2] + t[idX][idY*2 + 1];
}

void updx(int idX, int lx, int rx, int x, int y, ll val)
{
    if (lx == rx) {
        updy(idX, lx, rx, 1, 1, m, x, y, val);
        return;
    }

    int mid = (lx + rx) / 2;
    if (lx <= x && x <= mid)
        updx(idX*2, lx, mid, x, y, val);
    else                     
        updx(idX*2 + 1, mid + 1, rx, x, y, val);

    updy(idX, lx, rx, 1, 1, m, x, y, val);
}

ll gety(int idX, int idY, int ly, int ry, int y1, int y2)
{
    if (ry < y1 || y2 < ly) return 0LL;

    if (ly == ry)
        return t[idX][idY];
    if (y1 <= ly && ry <= y2)
        return t[idX][idY];

    int mid = (ly + ry) / 2;
    ll t1 = gety(idX, idY*2, ly, mid, y1, y2),
       t2 = gety(idX, idY*2 + 1, mid + 1, ry, y1, y2);

    return t1 + t2;
}

ll getx(int idX, int lx, int rx, int x1, int y1, int x2, int y2)
{
    if (rx < x1 || x2 < lx) return 0LL;

    if (lx == rx)
        return gety(idX, 1, 1, m, y1, y2);
    if (x1 <= lx && rx <= x2)
        return gety(idX, 1, 1, m, y1, y2);

    int mid = (lx + rx) / 2;
    ll t1 = getx(idX*2, lx, mid, x1, y1, x2, y2),
       t2 = getx(idX*2 + 1, mid + 1, rx, x1, y1, x2, y2);

    return t1 + t2; 
}
```

## 1.6. Ordered set

```cpp
#include <iostream>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;

typedef tree <int, null_type, less <int>, rb_tree_tag, tree_order_statistics_node_update> odered_set;
odered_set o_set;

int main() //n là số lượng phần tử hiện có trong set
{
    // độ phức tạp O(log(n)) khi thêm phần tử
    o_set.insert(4); o_set.insert(1);
    o_set.insert(0); o_set.insert(9);
    o_set.insert(4); o_set.insert(5);
    o_set.insert(8);

    for (auto it = o_set.begin(); it != o_set.end(); it++)
        cout << *it << " ";
    cout << "\n\n";

    int k;
    // số nhỏ thứ k = 4;       //độ phức tạp O(log(n))
    k = 4; cout << *(o_set.find_by_order(k-1)) << "\n\n";
    // số lượng số < k (= 5);  //độ phức tạp O(log(n))
    k = 5; cout << o_set.order_of_key(k)       << "\n\n"; 

    // áp dụng làm bài toán tính số lượng số
    // trong đoạn [l, r] = số lượng số [1; r + 1) - [1; l)
    // độ phức tạp O(2*log(n))
    int l = 4, r = 9;
    cout << o_set.order_of_key(r+1) - o_set.order_of_key(l) << "\n\n";

    cout << "o_set size: " << o_set.size() << "\n\n";
    cout << "//o_set.erase(" << k << ")\n\n";    o_set.erase(k); //độ phức tạp O(log(n))
    cout << "o_set size: " << o_set.size() << "\n\n";

    for (auto it = o_set.begin(); it != o_set.end(); it++)
        cout << *it << " ";
}
```

## 1.7. Trie

```cpp
const int TrieSz = 26;
struct TrieNode
{
    TrieNode *child[TrieSz];
    int cnt;

    TrieNode()
    {
        for (int i = 0; i < TrieSz; i++) child[i] = NULL;
        cnt = 0;
    }

    void insert(const string &s)
    {
        int n = s.length();
        TrieNode* p = this;
        for (int i = 0; i < n; i++)
        {
            int nxt = s[i] - 'a';
            if (p->child[nxt] == NULL) p->child[nxt] = new TrieNode();
            p = p->child[nxt];
        }
        ++(p->cnt);
    }

    bool find(const string &s)  // return true if string s exists exactly in trie
    {
        int n = s.length();
        TrieNode* p = this;
        for (int i = 0; i < n; i++)
        {
            int nxt = s[i] - 'a';
            if (p->child[nxt] == NULL) return false;
            p = p->child[nxt];
        }
        return (p->cnt) > 0;
    }

    bool find_suffix(const string &s) // return true if s is suffix of atleast one string in trie
    {
        int n = s.length();
        TrieNode* p = this;
        for (int i = 0; i < n; i++)
        {
            int nxt = s[i] - 'a';
            if (p->child[nxt] == NULL) return false;
            p = p->child[nxt];
        }
        return true;
    }
};
```

## 1.8. Trie Multiset

```cpp
//multiset using trie
struct Tnode
{
    int next[2];
    int p;
    int stop;
    int cnt;
    int sum;
};

// Them x vao multiset
void InsertNum(int x)
{
    int v = 0;
    for (int i = 18; i >= 0; --i) 
        int k = (x >> i) & 1;
        if (Trie[v].next[k] == 0) {
            Trie[v].next[k] = ++nT;
            Trie[nT].p = v;
        }
        v = Trie[v].next[k];
    }
    ++Trie[v].stop;
    while (v) ++Trie[v].cnt, Trie[v].sum += x, v = Trie[v].p;
    ++Trie[v].cnt;
    Trie[v].sum += x;
}

// Bo x khoi multiset
void RemoveNum(int x)
{
    int v = 0;
    for (int i = 18; i >= 0; --i) {
        int k = (x >> i) & 1;
        if (Trie[v].next[k] == 0)
            return;
        v = Trie[v].next[k];
    }
    --Trie[v].stop;
    while (v) --Trie[v].cnt, Trie[v].sum -= x, v = Trie[v].p;
    --Trie[v].cnt;
    Trie[v].sum -= x;
}

// Tim so dung thu k trong multiset k<=so luong so
int Rank(int k)
{
    int v = 0, x = 0;
    for (int i = 18; i >= 0; --i) {
        int C0 = (Trie[v].next[0]) ? Trie[Trie[v].next[0]].cnt : 0;
        if (k > C0) {
            x |= (1 << i);
            k -= C0;
            v = Trie[v].next[1];
        }
        else
            v = Trie[v].next[0];
    }
    return x;
}

// Tinh tong gia tri cac so trong multiset <=x
int SumLE(int x)
{
    int v = 0;
    int res = 0;
    for (int i = 18; i >= 0; --i) {
        int k = (x >> i) & 1;
        if (k && Trie[v].next[0])
            res += Trie[Trie[v].next[0]].sum;
        if (Trie[v].next[k] == 0)
            return res;
        v = Trie[v].next[k];
    }
    res += Trie[v].sum;
    return res;
}

// Tinh tong cac gia tri tu thu 1 den thu k<=so luong so
int SumRankLE(int k)
{
    int v = 0;
    int res = 0;
    for (int i = 18; i >= 0; --i) {
        int C0=(Trie[v].next[0])?Trie[Trie[v].next[0]].cnt :0;
        int T0=(Trie[v].next[0])?Trie[Trie[v].next[0]].sum :0;
        if (k > C0) {
            res += T0;
            k -= C0;
            v = Trie[v].next[1];
        }
        else
            v = Trie[v].next[0];
    }
    res += Trie[v].sum / Trie[v].stop * k;
    return res;
}

// Dem xem co bao nhieu so <=x
int CountLE(int x)
{
    int v = 0;
    int res = 0;
    for (int i = 18; i >= 0; --i)     {
        int k = (x >> i) & 1;
        if (k && Trie[v].next[0])
            res += Trie[Trie[v].next[0]].cnt;
        if (Trie[v].next[k] == 0)
            return res;
        v = Trie[v].next[k];
    }
    res += Trie[v].stop;
    return res;
}
```

# 2. Đồ thị

## 2.1. Dijkstra

```cpp
#define INF 0x3f3f3f3f

typedef pair<int, int> ii;
typedef priority_queue<ii, vector<ii>, greater<ii>> min_heap;

const int N = 1e5 + 1;

int numNode, numEdge, S, T;
vector<ii> adj[N];
int dist[N];

void addEdge(int u, int v, int w)
{
    adj[u].push_back({v, w});
    adj[v].push_back({u, w});
}

void Inp()
{
    cin >> numNode >> numEdge >> S >> T;
    int u, v, w;
    while(numEdge-- > 0)
    {
        cin >> u >> v >> w;
        addEdge(u, v, w);
    }
}

// min path to go from s to t
int dijkstra(int s, int t)
{
    for (int i = 1; i <= numNode; i++) dist[i] = INF;

    min_heap pq;
    pq.push({0, s});
    dist[s] = 0;

    while(!pq.empty()) {
        int u  = pq.top().second,
            wu = pq.top().first;
        pq.pop();

        if (wu > dist[u]) continue;

        for (auto x : adj[u])
        {
            int v = x.first;
            int weight = x.second;

            if (dist[v] > dist[u] + weight)
            {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    return dist[t];
}
```

## 2.2. Tìm khớp cầu

```cpp
#include <bits/stdc++.h>
using namespace std;
const int ioo = INT_MAX;
const int N   = 1e5 + 5;

int n, m;
vector<int> adj[N]; 
bool joint[N], seen[N];
int low[N], num[N], timeDfs, cnt_joint, cnt_bridge;

void addEdge(int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void Inp()
{
    cin >> n >> m; int u, v;
    while(m-- > 0)
        cin >> u >> v,
        addEdge(u, v);
}
void dfs(int u, int pre)
{
    low[u] = num[u] = ++timeDfs; seen[u] = 1;
    int child = 0;

    for (int v : adj[u])
    {
        if (v == pre) continue;
        if (!seen[v])   // gặp cung xuôi
        {
            dfs(v, u);
            low[u] = min(low[u], low[v]);   

            if (low[v] == num[v]) ++cnt_bridge;

            ++child; // tăng số lượng con của u

            // nếu u là gốc cây dfs
            if (u == pre) {
                // và nếu u có nhiều hơn 1 con
                if (child > 1)      
                    joint[u] = 1; // -> u là khớp
            }

            // ngược lại nếu u không phải là gốc cây
            // nhưng low[v] >= num[u]
            else if (low[v] >= num[u])
                joint[u] = 1; // -> u vẫn sẽ là khớp
        }
        else // gặp cung ngược
            low[u] = min(low[u], num[v]);
    }
}

void Solve()
{
    for (int i = 1; i <= n; i++)
        if (!num[i])
            dfs(i, i);

    for (int i = 1; i <= n; i++)
        cnt_joint += joint[i];
    cout << cnt_joint << ' ' << cnt_bridge;
}
```

## 2.3. Cây khung nhỏ nhất – Kruskal

```cpp
#include <bits/stdc++.h>
using namespace std;
const int N = 5e5 + 5;

int p, n, m;
int root[N];

// {u, v, weight, index}
pair<pair<int, int>, pair<int, int>> edge[N];

void Inp()
{
    cin >> p;
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
        // u, v, w
        cin >> edge[i].second.first >>
               edge[i].second.second >>
               edge[i].first.first;
        edge[i].first.second = i;
    }
}

// int getroot(int u) {return (root[u] < 0 ? u : root[u] = getroot(root[u]));}
int getroot(int u)
{
    if (root[u] < 0) return u;
    return root[u] = getroot(root[u]);
}

void Union(int u, int v)
{
    if (root[u] < root[v]) swap(u, v); 
    root[v] += root[u];
    root[u]  = v;
}

void Solve()
{
    memset(root, -1, sizeof(root));
    sort(edge + 1, edge + m + 1);
    vector<int> res;
    for (int i = 1; i <= m; i++)
    {
        int u = getroot(edge[i].second.first),
            v = getroot(edge[i].second.second);

        if (u == v) continue;

        Union(u, v);
        res.push_back(edge[i].first.second);
        if (res.size() == n - 1) break;
    }
    for (int &x : res) cout << x << ' ';
}
```

## 2.4. Tìm TPLT mạnh – Tarjan

```cpp
#include <bits/stdc++.h>

using namespace std;
const int N = 1e5 + 5;

int numNode; // number of nodes
vector<int> adj[N];
int low[N], num[N], timeDfs, cnt_TPLT;
bool deleted[N];
stack<int> st;

// directed graph
void addEdge(int u, int v)
{
    adj[u].push_back(v);
}

void tarjan(int u)
{
    low[u] = num[u] = ++timeDfs;
    st.push(u);
    for (int v : adj[u])
    {
        if (deleted[v]) continue;
        if (!num[v])
            tarjan(v),
            low[u] = min(low[u], low[v]);
        else
            low[u] = min(low[u], num[v]);
    }

    if (low[u] == num[u])
    {
        ++cnt_TPLT;
        int v = numNode + 1; // set v = inf
        do
        {
            v = st.top(); st.pop();
            deleted[v] = 1;
        }
        while(v != u);
    }

}

void Solve()
{
    for (int i = 1; i <= numNode; i++)
        if (!num[i])
            tarjan(i);
    cout << cnt_TPLT; // đếm thành phần liên thông mạnh
}
```

## 2.5. LCA

```cpp
// adj[i]: danh sách các đỉnh kề với đỉnh i
// h[i]: độ cao của đỉnh i (h[root] = 0)
// st[i]: thời điểm đầu tiên gặp đỉnh i (trên euler tour)
// R[x][0]: đỉnh đang xét tại đời điểm x (tgian bắt đầu từ 1)
// R[x][j]: đỉnh có độ cao nhỏ nhất trong đoạn (time) [x, x + 2^j - 1]
// Đỉnh có độ cao nhỏ nhất trong đoạn (time) st[u] đến st[v] là LCA(u,v)

vector<int> adj[MAXN];
int h[MAXN], st[MAXN];
int R[2 * MAXN][20];

// dfs đỉnh u có cha là đỉnh p
void dfs(int u, int p) 
{
    h[u] = h[p] + 1;
    R[++now][0] = u;
    st[u] = now;
    for (int &v : adj[u])
        if (v != p)
        {
            dfs(v, u);
            R[++now][0] = u;
        }
}

// tính mảng R (sparse table)
void initLCA() 
{
    now = 0;
    dfs(1, 0);

    for (int k = 0; (1 << (k + 1)) <= now; k++)
        for (int i = 1; i + (1 << (k + 1)) - 1 <= now; i++)
            if (h[R[i][k]] < h[R[i + (1 << k)][k]])
                R[i][k + 1] = R[i][k];
            else
                R[i][k + 1] = R[i + (1 << k)][k];
}

int findLCA(int u, int v)
{
    u = st[u];
    v = st[v];
    if (u > v)
        swap(u, v);
    int k = log2(v - u + 1);
    if (h[R[u][k]] < h[R[v - (1 << k) + 1][k]])
        return R[u][k];
    else
        return R[v - (1 << k) + 1][k];
}
```

# 3. Số học

## 3.1. Sàng nguyên tố

```cpp
// sieve primes in [1, R]
// O(R * log(log(R)))
vector<bool> primeSieve(int R)
{
    vector<bool> isPrime(R + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= R; i++)
        if (isPrime[i])
            for (int j = i * i; j <= R; j += i)
                isPrime[i] = false;

    // isPrime[x] = true (x = [1, R])
    // -> x là số nguyên tố

    return isPrime;
}

// sieve primes in [L, R]
// O(sqrt(R) * K): K is constant
vector<bool> primeSieve_range(int L, int R)
{
    vector<bool> isPrime(R - L + 1, true);

    for (long long i = 2; i * i <= R; i++)
        for (long long j = max(i * i, (L + i - 1) / i * i); j <= R; j += i)
            isPrime[j - L] = false;

    // Xét riêng trường hợp số 1
    if (1 >= L) isPrime[1 - L] = false;

    // isPrime[x] = true (x = [L, R])
    // -> x là số nguyên tố

    return isPrime;
}
```

## 3.2. Kiểm tra SNT – Miller Rabin

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

pair<ull, ull> factor(ull n) // phân tích n = 2^s * d
{
    ull s = 0;
    while ((n & 1) == 0) {
        s++;
        n >>= 1;
    }
    return {s, n};
}

ull Pow(ull a, ull b, ull c) // a^b % c
{
    ull ans = 1;
    a %=s c;
    while (b > 0)
    {s
        if (b & 1) ans = ans * a % c;
        b >>= 1;
        a = a * a s% c;
    }
    return ans;
}
// nếu a^d % n != 1 % n và (a^d)^(2^r) với mọi 0 <= r < s
// thì n ko phải là snt --> false
bool test_a(ull s, ull d, ull n, ull a)
{
    if (n == a) return true;

    ull p = Pow(a, d, n);
    if (p == 1) return true;

    for (; s > 0; s--) {
        if (p == n - 1)
            return true;s
        p = p * p % n;
    }

    return false;
}

bool miller(ull n)
{
    if (n < 2)
        return false;
    if ((n & 1) == 0)
        return n == 2;

    ull s, d;
    tie(s, d) = factor(n - 1);
    int list_a[] = {2, 7, 61};

    // return test_a(s, d, n, 2) && test_a(s, d, n, 7) && test_a(s, d, n, 61);
    for (auto &a : list_a)
        if (!test_a(s, d, n, a))
            return false;s
    return true;
}
```

## 3.3. Bignum add, subtract, multiply

```cpp
#include <iostream>
#include <vector>
#define taskname "BIGNUM"

using namespace std;s

struct bigint{char si = '+'; string val;};

bigint a, b;

void Inp()
{
    string x, y;
    cin >> a.val; a.si = '+';
    cin >> b.val; b.si = '+';
}

void equalSize(bigint &a, bigint &b)
{
    bool SWAP = false;
    if (a.val.size() > b.val.size()) {swap(a, b); SWAP = true;}
    string tmp = "";
    for (int i = 0; i < b.val.size() - a.val.size(); i++)
        tmp = tmp + '0';
    a.val = tmp + a.val;
    if (SWAP) swap(a, b);
}

bigint Plus(bigint x, bigint y)
{
    if (x.val == "0") return y;
    if (y.val == "0") return x;

    if (x.val.size() != y.val.size()) equalSize(x, y);

    bigint res; res.val = "";
    int tmp, carry = 0;
    for (int i = x.val.size() - 1; i >= 0; i--)
    {
        tmp = x.val[i] + y.val[i] - 96 + carry;
        res.val = char(tmp % 10 + 48) + res.val;
        carry = tmp / 10;
    }
    if (carry) res.val = '1' + res.val;
    return res;
}

bigint dif(bigint x, bigint y)
{
    if (x.si == '+' && y.si == '-') return Plus(x, y);
    if (x.si == '-' && y.si == '-') return dif(y, x);
    if (x.si == '-' && y.si == '+')
    {
        bigint res = Plus(x, y); res.si = '-';
        return res;
    }

    bool check = false;
    if (x.val < y.val) swap(x, y), check = true;
    bigint res; res.val = "";
    int tmp, carry = 0;
    for (int i = x.val.size() - 1; i >= 0; i--)
    { 
        tmp = x.val[i] - y.val[i] - carry;
        if (tmp < 0)
        {
            tmp += 10;
            carry = 1;
        }
        else
            carry = 0;
        res.val = char(tmp + 48) + res.val;
    }
    if (check) res.si = '-';
    else       res.si = '+';
    return res;
}

bigint BigMultSmall(string x, int y)
{
    bigint res; res.val = "";
    int tmp, carry = 0;
    for (int i = x.size() - 1; i >= 0; i--)
    {
        tmp = int(x[i] - 48) * y + carry;
        res.val = char(tmp % 10 + 48) + res.val;
        carry = tmp / 10;
    }
    if (carry) res.val = char(carry + 48) + res.val;
    return res;
}

bigint mul(bigint x, bigint y)
{
    vector<bigint> rem; rem.resize(x.val.size() + y.val.size());

    string zero = "";
    bigint tmp; tmp.val = "";
    int tmpY;
    for (int i = y.val.size() - 1; i >= 0; i--)
    {
        tmpY = int(y.val[i] - 48);
        if (tmpY == 0)
        {
            tmp.val = "0";
            tmp.si  = '+';
            zero = zero + '0';
            continue;
        }
        tmp = BigMultSmall(x.val, tmpY);
        tmp.val += zero;
        zero = zero + '0';
        rem.push_back(tmp);
    }
    bigint res; res.val = "0"; res.si = '+';
    for (int i = 0; i < rem.size(); i++)
        res = Plus(res, rem[i]);
    return res;
}

void Out(bigint x)
{
    while(x.val[0] == '0' && x.val.size() > 1) x.val.erase(0, 1);
    if (x.si == '-' && x.val[0] != '0') cout << '-';
    cout << x.val << '\n';
}

void Solve()
{
    equalSize(a, b);
    Out(Plus(a, b));
    Out(dif(a, b));
    Out(mul(a, b));
}
```

## 3.4. Bignum mod

```cpp
int smallMod(string a, int b)
{
    ll res = 0;
    for (int i = 0; i < a.size(); i++)
        (res = 10LL*res + ll(a[i] - '0')) %= b;
    return res;
}
```

## 3.5. Bignum div

```cpp
string longDivision(string number, int divisor)
{
    string ans;

    // Find prefix of number that is larger than divisor.
    int idx = 0;
    int temp = number[idx] - '0';
    while (temp < divisor)
        temp = temp * 10 + (number[++idx] - '0');

    // Repeatedly divide divisor with temp. 
    // After every division, update temp to include one more digit.
    while (number.size() > idx) {
        // Store result in answer i.e. temp / divisor
        ans += (temp / divisor) + '0';

        // Take next digit of number
        temp = (temp % divisor) * 10 + (number[++idx] - '0');
    }

    // If divisor is greater than number
    if (ans.length() == 0)
        return "0";

    // else return ans
    return ans;
}
```

## 3.6. Tổ hợp – Chỉnh hợp

```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to find the nCr
void printNcR(int n, int r)
{

    // p holds the value of n*(n-1)*(n-2)...,
    // k holds the value of r*(r-1)...
    long long p = 1, k = 1;

    // C(n, r) == C(n, n-r),
    // choosing the smaller value
    if (n - r < r) r = n - r;

    if (r != 0) {
        while (r) {
            p *= n;
            k *= r;

            // gcd of p, k
            long long m = __gcd(p, k);

            // dividing by gcd, to simplify
            // product division by their gcd
            // saves from the overflow
            p /= m;
            k /= m;

            n--;
            r--;
        }

        // k should be simplified to 1
        // as C(n, r) is a natural number
        // (denominator should be 1 ) .
    }

    else
        p = 1;
    // if our approach is correct p = ans and k =1
    cout << p << endl;
}
```

## 3.7. Extended GCD

```cpp
void ext_gcd(ll A, ll B, ll &X, ll &Y)
{
    long long x2, y2,
              x1, y1,
              x,  y,
              r2, r1,
              q,  r;

    x2 = 1; y2 = 0;
    x1 = 0; y1 = 1;
    for (r2 = A, r1 = B; r1 != 0; r2 = r1, r1 = r, x2 = x1, y2 = y1, x1 = x, y1 = y) {
        q = r2 / r1;
        r = r2 % r1;
        x = x2 - (q * x1);
        y = y2 - (q * y1);
    }
    X = x2; Y = y2;
}
```

## 3.8. Diophantine

```cpp
ll MOD(ll a, ll m)
{
    return (a % m + m) % m;
}
int Diophantine(int a, int b, int c)
{
    ll m = a, n = b, xA = 1, xB = 0;
    while (n > 0)
    {
        ll q = m / n;
        ll r = m - q * n;
        ll xr = xA - q * xB;
        m = n; xA = xB;
        n = r; xB = xr;
    }
    if (c % m != 0) return 0;
    ll p = b / m;
    ll xMax = (c - b) / a;
    xA = MOD(xA * c / m, p);
    ll res = (xMax - xA) / p + (xA != 0);

    return ((xMax < xA)? 0 : res);
}
```

## 3.9. Nhân nhanh (O(log) + O(1))

```cpp
ll Mult(ll a, ll b, ll m) // O(log(b))
{
    if (b == 0) return 0;
    ll t = Mult(a, b / 2, m);
    t = (t + t) % m;
    if (b & 1) return (t + a % m) % m;
    return t;
}

ll Mult(ll a, ll b, ll m) // O(1)
{
    a %= m; b %= m;
    ull q = (long double) a * b / m;
    ll  r = ll(a * b - q * m) % ll(m);
    if (r < 0) r += m;
    return r;
}
```

## 3.10. Luỹ thừa nhanh (O(log))

```cpp
ll Pow(ll a, ll b, ll m)
{
    if (b == 0) return 1 % m;
    ll t = Pow(a, b / 2, m);
    t = (t * t) % m;
    if (b & 1) return (t * (a % m)) % m;
    return t;
}
```

## 3.11. Inverse mod

```cpp
int Inv(int n, int MOD)
{
    return fastPow(n, phi(MOD) - 1);
}
```

## 3.12. Phi hàm Euler

```cpp
// Định nghĩa: phi(N) là số số nguyên tố cùng nhau với N trong đoạn từ 1 đến N.
// O(sqrt(n))
int phi(int n)
{
    int res = n;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
            }
            res -= res / i;
        }
    }
    if (n != 1) {
        res -= res / n;
    }
    return res;
}
```

## 3.13. Nhân ma trận

```cpp
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

// matrix type
using type = ll;

struct Matrix
{
    vector<vector<type>> data;
    int row() const {return data.size();}
    int col() const {return data[0].size();}

    auto & operator [](int i) {return data[i];}
    const auto & operator [](int i) const {return data[i];}

    Matrix() = default;
    Matrix(int r, int c) : data(r, vector<type> (c)) {}
    Matrix(const vector<vector<type>> &d) : data(d)  {}

    friend ostream & operator << (ostream &out, const Matrix &d)
    {
        for (auto x : d.data) {
            for (auto y : x) out << y << ' ';
            out << '\n';
        }
        return out;
    }

    static Matrix identity(long long n)
    {
        Matrix a = Matrix(n, n);
        while (n--) a[n][n] = 1;
        return a;
    }

    Matrix operator * (const Matrix &b)
    {
        Matrix a = *this;
        assert(a.col() == b.row());

        Matrix c(a.row(), b.col());
        for (int i = 0; i < a.row(); ++i)
            for (int j = 0; j < b.col(); ++j)
                for (int k = 0; k < a.col(); ++k)
                    c[i][j] += a[i][k] * b[k][j];
        return c;
    }

    Matrix pow(long long exp)
    {

        assert(row() == col());
        Matrix base = *this, ans = identity(row());
        for (; exp > 0; exp >>= 1, base = base * base)
            if (exp & 1) ans = ans * base;
        return ans;
    }
};

int main()
{
    Matrix a({
        {1, 2},
        {3, 4}
    });

    Matrix b({
        {0, 10, 100},
        {1,  1,  10}
    });

    cout << a * b << '\n';
    // 2 12 120
    // 4 34 340

    cout << a.pow(3) << '\n';
    // 37 54
    // 81 118

    b = a;
    cout << b << '\n';
    // 1 2
    // 3 4

    b = Matrix::identity(3);
    cout << b << '\n';
    // 1 0 0
    // 0 1 0
    // 0 0 1

    b = Matrix(2, 3);
    cout << b << '\n';
    // 0 0 0
    // 0 0 0

    Matrix c(3, 2);
    cout << c << '\n';
    // 0 0
    // 0 0
    // 0 0
}
```

# 4. Hình học

## 4.1. Viết đường thẳng

```cpp
line writeLine(point P, point Q)
{
    ll A = P.y.fi - Q.y.fi;
    ll B = Q.x.fi - P.x.fi;
    ll C = -(A*P.x.fi + B*P.y.fi);
    return {A, B, C};
}
```

## 4.2. Kiểm tra điểm thuộc tia

```cpp
// point là phân số
bool pointInLaser(point M, point A, point B)
{
    db Ax = (db) A.x.fi / A.x.se,
       Ay = (db) A.y.fi / A.y.se,
       Bx = (db) B.x.fi / B.x.se,
       By = (db) B.y.fi / B.y.se,
       Mx = (db) M.x.fi / M.x.se,
       My = (db) M.y.fi / M.y.se;

    db t1 = Mx - Ax,
       t2 = Bx - Ax,
       t3 = My - Ay,
       t4 = By - Ay;

    return ((db) t1*t2 >= 0.0 && (db) t3*t4 >= 0.0);
}
```

## 4.3. Tìm điểm giao giữa 2 đường thẳng

```cpp
point intersect(line l1, line l2)
{
    ll a1 = l1.a, b1 = l1.b, c1 = l1.c,
       a2 = l2.a, b2 = l2.b, c2 = l2.c;
    ll D  = a1*b2 - a2*b1,
       Dx = c2*b1 - c1*b2,
       Dy = a2*c1 - a1*c2;

    if (D == Dx && Dx == Dy && Dy == 0)
        return {{(ll)  N + 1, 1LL}, {(ll)  N + 1, 1LL}};

    if (D == 0 && (Dx || Dy))
        return {{(ll) -N - 1, 1LL}, {(ll) -N - 1, 1LL}};

    point M = {{Dx, D}, {Dy, D}};

    return M;
}
```

# 5. Quy hoạch động

## 5.1. Dãy con chung tăng dài nhất

```cpp
void Solve()
{
    for (int i = 1; i <= n; i++) {
        int Max = 0;
        for (int j = 1; j <= m; j++) {
            if (a[i] == b[j]) f[j] = max(f[j], Max + 1);
            if (a[i] > b[j])   Max = max(f[j], Max);
        }
    }
    cout << *max_element(f + 1, f + m + 1);
}
```

## 5.2. Số lượng số đoạn [L, R] có tổng các chữ số bằng K

```cpp
ll l, r; int k;
ll f[20][200][2];
ll dp(string &s, int id, int sum, bool isSmaller)
{
    if (id == s.size())
        return sum == k;

    if (f[id][sum][isSmaller] != -1)
        return f[id][sum][isSmaller];

    ll res = 0;
    int maxDigit = (isSmaller ? 9 : int(s[id] - '0'));

    for (int i = 0; i <= maxDigit; i++) {
        bool curSmaller = isSmaller;
        if (i < maxDigit)
            curSmaller = 1;
        res += dp(s, id + 1, sum + i, curSmaller);
    }

    return f[id][sum][isSmaller] = res;
}

ll cnt(ll x) // đếm đoạn [1, X]
{
    string s = std::to_string(x);
    memset(f, -1, sizeof(f));
    return dp(s, 0, 0, 0);
}
```

## 5.3. Tìm mỗi hàng, mỗi cột 1 phần tử sao cho tổng lớn nhất (bitmask)

```cpp
#include <bits/stdc++.h>
using namespace std;
const int oo = 2e9;
const int N = 2e1 + 5;

int n, m, k;
int a[N][N];

void Inp()
{
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }
}

void Solve()
{
    if (k == 0) return void(cout << "0\n0");

    int dp[(1 << n)][m];

    fill(dp[0], dp[0] + m, 0);
    for (int i = 1; i < (1 << n); i++)
        dp[i][0] = -oo;
    for (int x = 0; x < n; x++)
        dp[(1 << x)][0] = a[x][0];
      for (int d = 1; d < m; d++) {
        for (int s = 0; s < (1 << n); s++) {
            dp[s][d] = dp[s][d-1];
            for (int x = 0; x < n; x++) {
                if (s & (1 << x)) {
                dp[s][d] = max(dp[s][d], dp[s ^ (1 << x)][d - 1] + a[x][d]);
                }
            }
        }
    }

    int res = 0;
    for (int s = 0; s < (1 << n); s++)
        if (__builtin_popcount(s) == k)
            res = max(res, dp[s][m - 1]);

    cout << k << '\n' << res;
}
```

# 6. Xâu

## 6.1. KMP

```cpp
// tìm các pi[i] là giá trị K <= i lớn I sao cho:
// - s[0, K-1] == s[i - K + 1, i]
// Lưu ý: pi[0] = 0
// đặt N = s.size()
// O(N)
vector<int> prefix_function(string s)
{
    int n = s.size();
    vector<int> pi(n);
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j])
            j = pi[j - 1];

        if (s[i] == s[j])
            j++;

        pi[i] = j;
    }
    return pi;
}

// Tìm các vị trí xâu T xuất hiện trong S
// SUBMIT LINK: https://oj.vnoi.info/problem/substr
// đặt M = t.size(), N = s.size()
// tìm các vị trí i trong xâu S
// mà S[i, i + M - 1] == T
// O(N + M)
vector<int> string_matching(string s, string t)
{
    string p = t + '#' + s;
    int m = t.size();
    int n = s.size();
    vector<int> pi = prefix_function(p);

    vector<int> res;
    for (int i = m + 1; i <= m + n; ++i) {
        // Tìm thấy KQ:
        // p[0, m - 1] == p[i - pi[i] + 1, i] == T
        // -> tồn tại xâu con trong S bằng T
        if (pi[i] == m)
            res.push_back(i - 2*m + 1);
    }

    return res;
}
```

## 6.2. Z-Function

```cpp
// đặt N = s.size()
// tìm các z[i] là giá trị K < N lớn I sao cho:
// - s[0, K-1] == s[i, i + K - 1]
// Lưu ý: z[0] = 0
// O(N)
vector<int> z_function(string s)
{
    int n = s.size();
    vector<int> z(n);
    for (int i = 1; i < n; ++i)
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            ++z[i];

    return z;
}

// Tìm các vị trí xâu T xuất hiện trong S
// SUBMIT LINK: https://oj.vnoi.info/problem/substr
// đặt M = t.size(), N = s.size()
// tìm các vị trí i trong xâu S
// mà S[i, i + M - 1] == T
// O(N + M)
vector<int> string_matching(string s, string t)
{
    string p = t + '#' + s;
    int m = t.size();
    int n = s.size();
    vector<int> z = z_function(p);
    vector<int> res;
    for (int i = m + 1; i <= m + n; ++i) {
        // Tìm thấy KQ:
        // p[0, m - 1] == p[i, i + z[i] - 1] == T
        // -> tồn tại xâu con trong S bằng T
        if (z[i] == m)
            res.push_back(i - m);
    }
    return res;
}

// Đếm s.lượng xâu con liên tiếp phân biệt trong S
// đặt N = s.size()
// O(N^2)
int num_substr(string s)
{
    // Ý tưởng: giả sử số lượng xâu phân biệt
    //          là K, khi ta thêm kí tự c vào
    //          thì cần đếm thêm số lượng xâu
    //          khác nhau có hậu tố với chuỗi s + c
    vector<int> z = z_function(s);
    string tmp;
    int k = 0;
    int n = s.size();
    for (int i = 0; i < n; ++i) {
        tmp = s[i] + tmp;
        vector<int> z = z_function(tmp);
        int zmax = *max_element(z.begin(), z.end());
        k += (i + 1) - zmax;
    }
    return k;
}
```

# 7. Khác

## 7.1. Hash cặp số, toạ độ

```cpp
const ll seed = 1e6 + 3;  // prime
ll _hashCood(int id)
{
    ii point = {p[id].fi + int(1e6), sp[id].se + int(1e6)};
    return (ll) point.fi*seed + point.se;
}
```

## 7.2. Hash phân số

```cpp
const ll seed = 1e6 + 3;  // prime
const ll  neg = 1e3 + 9;  // prime

ll _hash(int id1, int id2)
{
    int x = p[id1].se - p[id2].se,
        y = p[id1].fi - p[id2].fi;

    if (y == 0) return ll(1e18);
    if (x == 0) return 0LL;

    int gcd = __gcd(x, y);
    x /= gcd;
    y /= gcd;

    if (x*y < 0) return (ll) neg*(labs(x)*seed + labs(y));
                 return (ll)      labs(x)*seed + labs(y);
}
```

## 7.3. Hash xâu

```cpp
typedef long long ll;

const int base = 31; // prime
const ll MOD = 1000000003;
const ll maxn = 1000111;

using namespace std;

ll POW[maxn], hashT[maxn];

ll getHashT(int i, int j) {
    return (hashT[j] - hashT[i - 1] * POW[j - i + 1] + MOD * MOD) % MOD;
}

int main()
{
    string T, P; cin >> T >> P;

    // Initialize
    int lenT = T.size(), lenP = P.size();
    T = " " + T; P = " " + P;
    POW[0] = 1;

    // Precalculate base^i
    for (int i = 1; i <= lenT; i++)
         POW[i] = (POW[i-1] * base) % MOD;

    // Calculate hash value of T[1..i]
    for (int i = 1; i <= lenT; i++)
         hashT[i] = (hashT[i-1] * base + T[i] - 'a' + 1) % MOD;

    // Calculate hash value of P
    ll hashP = 0;
    for (int i = 1; i <= lenP; i++)
         hashP = (hashP * base + P[i] - 'a' + 1) % MOD;
}
```

## 7.4. Min, max, gcd trong đoạn tịnh tiến

```cpp
for (int i = 1; i <= n; i++) {
    lmn[i] = (i % len == 1) ? a[i] : min(lmn[i-1], a[i]);
    lmx[i] = (i % len == 1) ? a[i] : max(lmx[i-1], a[i]);
}

for (int i = n; i >= 1; i--) {
    rmn[i] = (i % len==0 || i==n) ? a[i] : min(rmn[i+1], a[i]);
    rmx[i] = (i % len==0 || i==n) ? a[i] : max(rmx[i+1], a[i]);
}

for (int i = len; i <= n; i++) {
    int Min = min(rmn[i - len + 1], lmn[i]);
        Max = max(rmx[i - len + 1], lmx[i]);      
}
```

- [8. Kỹ thuật ICPC 2026 HCMUS (Mới bổ sung)](#8-kỹ-thuật-icpc-2026-hcmus-mới-bổ-sung)
  - [8.1. Hierholzer (Đường đi / Chu trình Euler)](#81-hierholzer-đường-đi--chu-trình-euler)
  - [8.2. Segment Tree + Nhân ma trận (Trạng thái DP)](#82-segment-tree--nhân-ma-trận-trạng-thái-dp)
  - [8.3. Quét mặt phẳng (Sweep Line) tính Area of Union](#83-quét-mặt-phẳng-sweep-line-tính-area-of-union)
  - [8.4. I/O cho __int128_t](#84-io-cho-__int128_t)
