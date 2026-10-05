# Bài 4 - Supplement (bổ sung tối thiểu cho Regional)

Mỗi mục chỉ giữ 1 template 15-30 dòng, đủ in 1-2 trang.

## 4.1 DSU (hợp nhất tập rời rạc)

Dùng cho Kruskal, đếm thành phần liên thông, jump-pointer.

```cpp
struct DSU {
    vector<int> p, sz;
    DSU(int n = 0) { init(n); }
    void init(int n) { p.resize(n+1); sz.assign(n+1,1); iota(p.begin(),p.end(),0); }
    int find(int x){ return p[x]==x?x:p[x]=find(p[x]); }
    bool unite(int a,int b){
        a=find(a); b=find(b); if(a==b) return false;
        if(sz[a]<sz[b]) swap(a,b);
        p[b]=a; sz[a]+=sz[b]; return true;
    }
};
```

## 4.2 Topo sort (Kahn)

```cpp
// adj có hướng, trả {} nếu có chu trình
vector<int> topo(int n, const vector<vector<int>>& adj){
    vector<int> deg(n+1,0);
    for(int u=1;u<=n;u++) for(int v:adj[u]) deg[v]++;
    queue<int> q;
    for(int i=1;i<=n;i++) if(!deg[i]) q.push(i);
    vector<int> o;
    while(!q.empty()){int u=q.front();q.pop();o.push_back(u);
        for(int v:adj[u]) if(--deg[v]==0) q.push(v);}
    return (int)o.size()==n?o:vector<int>{};
}
```

## 4.3 Đường ngắn

* `0-1 BFS`: cạnh 0/1, deque O(E).
* `Bellman-Ford`: có cạnh âm, phát hiện chu trình âm, O(VE).
* `Floyd`: mọi cặp, n <= 400, `dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])`, dùng `long long INF=4e14`.

Dijkstra bản `long long` + `priority_queue` đã có ở cheatsheet cũ nhưng nhớ
đồ thị có hướng thì đừng `addEdge` 2 chiều.

## 4.4 Tổ hợp mod 1e9+7

```cpp
const int MOD=1000000007;
long long modPow(long long a,long long e=MOD-2){
    long long r=1; while(e){if(e&1)r=r*a%MOD;a=a*a%MOD;e>>=1;} return r;
}
// build 1 lần: fact[i], invFact[i]
fact[0]=1; for(...) fact[i]=fact[i-1]*i%MOD;
invFact[N]=modPow(fact[N]); for(...) invFact[i-1]=invFact[i]*i%MOD;
C(n,k)= k<0||k>n?0:fact[n]*invFact[k]%MOD*invFact[n-k]%MOD;
```

Đây là thứ thiếu trong cheatsheet cũ (chỉ có `printNcR` tràn số, không mod).

## 4.5 Số nguyên tố nhanh

* Sàng tuyến tính `O(n)` cho `n` tới 1e7.
* Miller-Rabin deterministic cho 64-bit + Pollard-Rho khi cần phân tích thừa số.
  Đừng dùng bản 3 cơ số `{2,7,61}` cho số > 2^32.

## 4.6 Hình học tối thiểu

```cpp
struct Pt{ long long x,y; };
long long cross(const Pt&a,const Pt&b,const Pt&c){
    // (b-a) x (c-a)
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);
}
// cross>0: rẽ trái, <0: rẽ phải, =0: thẳng hàng
// Segment intersect + Andrew convex hull chỉ thêm ~30 dòng nữa.
```

 convex hull Andrew: sort điểm, dựng bao trên/dưới bằng cross, O(n log n).

## 4.7 Xâu

* Rolling hash **kép** (2 mod) thay vì 1 mod như cheatsheet cũ.
* KMP giữ nguyên (đã đúng, chỉ cần ghi chú 1-based).
* Z-function bản linear có window `[l,r]`.
* Aho-Corasick khi nhiều pattern, Manacher khi palindrome dài nhất.

## Bài tập gộp

1. Kruskal + DSU: SPOJ `mst`.
2. Topo: CSES 1679 Course Schedule.
3. Floyd/Bellman: CSES 1672, 1673.
4. C(n,k) mod: VNOJ `nkc`.
5. Hull: Kattis `convexhull`.
