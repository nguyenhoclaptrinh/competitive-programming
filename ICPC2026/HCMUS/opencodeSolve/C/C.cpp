#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007LL;

pair<long long,long long> fib_pair(long long n) {
    // returns {F(n), F(n+1)} with F0=0,F1=1, n>=0
    if (n == 0) return {0, 1};
    auto p = fib_pair(n >> 1);
    long long a = p.first;   // F(k)
    long long b = p.second;  // F(k+1)
    long long t1 = (2 * b % MOD - a + MOD) % MOD;
    long long c = a * t1 % MOD;              // F(2k)
    long long d = (a * a % MOD + b * b % MOD) % MOD; // F(2k+1)
    if ((n & 1) == 0) return {c, d};
    else return {d, (c + d) % MOD};
}

// Matrix Mx = M^x where M=[[1,1],[1,0]], for any integer x (possibly negative)
// Mx = [[F(x+1), F(x)],[F(x), F(x-1)]]
struct Mat {
    long long a00, a01, a10, a11;
};

Mat mat_pow_shift(long long x) {
    if (x == 0) return {1, 0, 0, 1};
    if (x > 0) {
        auto p = fib_pair(x);
        long long fx = p.first;   // F(x)
        long long fx1 = p.second; // F(x+1)
        long long fxm1 = (fx1 - fx + MOD) % MOD; // F(x-1)
        return {fx1, fx, fx, fxm1};
    } else {
        long long n = -x;
        auto p = fib_pair(n);
        long long fn = p.first;   // F(n)
        long long fn1 = p.second; // F(n+1)
        long long fnm1 = (fn1 - fn + MOD) % MOD; // F(n-1)
        long long s = (n & 1) ? MOD - 1 : 1; // (-1)^n
        // M^{-n} = (-1)^n * [[F(n-1), -F(n)],[-F(n), F(n+1)]]
        long long m00 = s * fnm1 % MOD;
        long long m01 = (MOD - s * fn % MOD) % MOD;
        long long m10 = (MOD - s * fn % MOD) % MOD;
        long long m11 = s * fn1 % MOD;
        return {m00, m01, m10, m11};
    }
}

const int MAXN = 200000;
int n, q;
vector<long long> sum0, sum1;
vector<long long> lz00, lz01, lz10, lz11;

void apply_node(int idx, const Mat &m) {
    long long ns1 = (m.a00 * sum1[idx] + m.a01 * sum0[idx]) % MOD;
    long long ns0 = (m.a10 * sum1[idx] + m.a11 * sum0[idx]) % MOD;
    sum1[idx] = ns1;
    sum0[idx] = ns0;
    long long n00 = (m.a00 * lz00[idx] + m.a01 * lz10[idx]) % MOD;
    long long n01 = (m.a00 * lz01[idx] + m.a01 * lz11[idx]) % MOD;
    long long n10 = (m.a10 * lz00[idx] + m.a11 * lz10[idx]) % MOD;
    long long n11 = (m.a10 * lz01[idx] + m.a11 * lz11[idx]) % MOD;
    lz00[idx] = n00; lz01[idx] = n01; lz10[idx] = n10; lz11[idx] = n11;
}

inline bool is_ident(int idx) {
    return lz00[idx]==1 && lz01[idx]==0 && lz10[idx]==0 && lz11[idx]==1;
}

void push(int idx) {
    if (is_ident(idx)) return;
    Mat m{lz00[idx], lz01[idx], lz10[idx], lz11[idx]};
    apply_node(idx<<1, m);
    apply_node(idx<<1|1, m);
    lz00[idx]=1; lz01[idx]=0; lz10[idx]=0; lz11[idx]=1;
}

void build(int idx, int l, int r, const vector<long long> &a) {
    lz00[idx]=1; lz01[idx]=0; lz10[idx]=0; lz11[idx]=1;
    if (l == r) {
        auto p = fib_pair(a[l]);
        sum0[idx] = p.first;
        sum1[idx] = p.second;
        return;
    }
    int mid = (l + r) >> 1;
    build(idx<<1, l, mid, a);
    build(idx<<1|1, mid+1, r, a);
    sum0[idx] = (sum0[idx<<1] + sum0[idx<<1|1]) % MOD;
    sum1[idx] = (sum1[idx<<1] + sum1[idx<<1|1]) % MOD;
}

void update(int idx, int l, int r, int ql, int qr, const Mat &m) {
    if (qr < l || r < ql) return;
    if (ql <= l && r <= qr) {
        apply_node(idx, m);
        return;
    }
    push(idx);
    int mid = (l + r) >> 1;
    update(idx<<1, l, mid, ql, qr, m);
    update(idx<<1|1, mid+1, r, ql, qr, m);
    sum0[idx] = (sum0[idx<<1] + sum0[idx<<1|1]) % MOD;
    sum1[idx] = (sum1[idx<<1] + sum1[idx<<1|1]) % MOD;
}

long long query(int idx, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return sum0[idx];
    push(idx);
    int mid = (l + r) >> 1;
    return (query(idx<<1, l, mid, ql, qr) + query(idx<<1|1, mid+1, r, ql, qr)) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];
    sum0.assign(4 * n + 4, 0);
    sum1.assign(4 * n + 4, 0);
    lz00.assign(4 * n + 4, 1);
    lz01.assign(4 * n + 4, 0);
    lz10.assign(4 * n + 4, 0);
    lz11.assign(4 * n + 4, 1);
    build(1, 1, n, a);
    for (int i = 0; i < q; ++i) {
        int type; cin >> type;
        if (type == 1) {
            int l, r; long long x;
            cin >> l >> r >> x;
            if (x != 0) {
                Mat m = mat_pow_shift(x);
                update(1, 1, n, l, r, m);
            }
        } else {
            int l, r; cin >> l >> r;
            cout << query(1, 1, n, l, r) % MOD << '\n';
        }
    }
    return 0;
}
