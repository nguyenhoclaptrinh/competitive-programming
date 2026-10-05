// Fenwick Tree - template chuẩn mang vào phòng thi (C++17)
// 1-based. Mọi tổng dùng long long.
#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n = 0;
    vector<long long> bit;
    Fenwick() {}
    Fenwick(int n_) { init(n_); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 1, 0);
    }
    // cộng v vào a[p]
    void add(int p, long long v) {
        for (; p >= 1 && p <= n; p += p & -p) bit[p] += v;
    }
    // tổng a[1..p]
    long long sumPrefix(int p) const {
        long long s = 0;
        for (; p > 0; p -= p & -p) s += bit[p];
        return s;
    }
    long long rangeSum(int l, int r) const {
        if (l > r) return 0;
        return sumPrefix(r) - sumPrefix(l - 1);
    }
    // tìm p nhỏ nhất sao cho sumPrefix(p) >= k (k >= 1, mảng 0/1 hoặc tần suất)
    // trả về -1 nếu không tồn tại
    int kth(long long k) const {
        if (k <= 0 || k > sumPrefix(n)) return -1;
        int p = 0;
        int pw = 1;
        while ((pw << 1) <= n) pw <<= 1;
        for (; pw; pw >>= 1) {
            int nxt = p + pw;
            if (nxt <= n && bit[nxt] < k) {
                k -= bit[nxt];
                p = nxt;
            }
        }
        return p + 1;
    }
};

// Nén tọa độ: đưa giá trị tới 1e9 về 1..m
vector<int> compressVals(const vector<long long> &a) {
    vector<long long> v(a.begin(), a.end());
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    vector<int> c(a.size());
    for (size_t i = 0; i < a.size(); i++)
        c[i] = int(lower_bound(v.begin(), v.end(), a[i]) - v.begin()) + 1; // 1-based
    return c;
}

// ---- self-test nhỏ: biên dịch và chạy, phải in OK ----
#ifdef LOCAL_TEST_FENWICK
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Fenwick f(5);
    for (int i = 1; i <= 5; i++) f.add(i, i); // a = [1,2,3,4,5]
    assert(f.sumPrefix(3) == 6);
    assert(f.rangeSum(2, 4) == 9);
    // kth trên mảng tần suất [1,1,1,1,1]
    Fenwick g(5);
    for (int i = 1; i <= 5; i++) g.add(i, 1);
    assert(g.kth(1) == 1 && g.kth(5) == 5 && g.kth(6) == -1);
    cout << "OK\n";
    return 0;
}
#endif
