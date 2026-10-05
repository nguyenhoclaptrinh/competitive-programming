#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

struct Matrix {
    long long mat[2][2];
    Matrix() {
        mat[0][0] = mat[0][1] = mat[1][0] = mat[1][1] = 0;
    }
    Matrix(long long a, long long b, long long c, long long d) {
        mat[0][0] = a; mat[0][1] = b;
        mat[1][0] = c; mat[1][1] = d;
    }
    Matrix operator*(const Matrix& other) const {
        Matrix res;
        for (int i = 0; i < 2; ++i) {
            for (int k = 0; k < 2; ++k) {
                for (int j = 0; j < 2; ++j) {
                    res.mat[i][j] = (res.mat[i][j] + mat[i][k] * other.mat[k][j]) % MOD;
                }
            }
        }
        return res;
    }
    Matrix operator+(const Matrix& other) const {
        Matrix res;
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                res.mat[i][j] = mat[i][j] + other.mat[i][j];
                if (res.mat[i][j] >= MOD) res.mat[i][j] -= MOD;
            }
        }
        return res;
    }
    bool isIdentity() const {
        return mat[0][0] == 1 && mat[0][1] == 0 && mat[1][0] == 0 && mat[1][1] == 1;
    }
};

Matrix Identity(1, 0, 0, 1);
Matrix M(1, 1, 1, 0);
Matrix Minv(0, 1, 1, MOD - 1);

Matrix power(Matrix a, long long b) {
    Matrix res = Identity;
    while (b > 0) {
        if (b & 1) res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}

const int MAXN = 200005;
Matrix tree[4 * MAXN];
Matrix lazy_tree[4 * MAXN];

void build(int node, int start, int end, const vector<long long>& arr) {
    lazy_tree[node] = Identity;
    if (start == end) {
        tree[node] = power(M, arr[start]);
    } else {
        int mid = (start + end) / 2;
        build(2 * node, start, mid, arr);
        build(2 * node + 1, mid + 1, end, arr);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
}

void push(int node, int start, int end) {
    if (!lazy_tree[node].isIdentity()) {
        tree[2 * node] = tree[2 * node] * lazy_tree[node];
        lazy_tree[2 * node] = lazy_tree[2 * node] * lazy_tree[node];
        
        tree[2 * node + 1] = tree[2 * node + 1] * lazy_tree[node];
        lazy_tree[2 * node + 1] = lazy_tree[2 * node + 1] * lazy_tree[node];
        
        lazy_tree[node] = Identity;
    }
}

void update(int node, int start, int end, int l, int r, const Matrix& val) {
    if (r < start || end < l) return;
    if (l <= start && end <= r) {
        tree[node] = tree[node] * val;
        lazy_tree[node] = lazy_tree[node] * val;
        return;
    }
    push(node, start, end);
    int mid = (start + end) / 2;
    update(2 * node, start, mid, l, r, val);
    update(2 * node + 1, mid + 1, end, l, r, val);
    tree[node] = tree[2 * node] + tree[2 * node + 1];
}

Matrix query(int node, int start, int end, int l, int r) {
    if (r < start || end < l) return Matrix();
    if (l <= start && end <= r) return tree[node];
    push(node, start, end);
    int mid = (start + end) / 2;
    return query(2 * node, start, mid, l, r) + query(2 * node + 1, mid + 1, end, l, r);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    
    build(1, 1, n, a);
    
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long x;
            cin >> l >> r >> x;
            Matrix val;
            if (x > 0) val = power(M, x);
            else if (x < 0) val = power(Minv, -x);
            else val = Identity;
            update(1, 1, n, l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            Matrix res = query(1, 1, n, l, r);
            cout << res.mat[0][1] << "\n";
        }
    }
    return 0;
}
