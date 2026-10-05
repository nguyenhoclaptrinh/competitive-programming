// Sparse Table RMQ + LCA binary lifting - template in phòng thi
#include <bits/stdc++.h>
using namespace std;

// ---------- Sparse Table cho min (đổi min -> max/gcd đều được) ----------
struct SparseMin {
    int n = 0, K = 0;
    vector<vector<int>> st;
    vector<int> lg;
    SparseMin() {}
    SparseMin(const vector<int> &a) { build(a); }
    void build(const vector<int> &a) {
        n = (int)a.size();
        K = 1;
        while ((1 << K) <= n) K++;
        st.assign(K, vector<int>(n));
        st[0] = a;
        for (int k = 1; k < K; k++)
            for (int i = 0; i + (1 << k) <= n; i++)
                st[k][i] = min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
        lg.assign(n + 1, 0);
        for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
    }
    // min trên [l, r] inclusive, 0-based
    int query(int l, int r) const {
        int k = lg[r - l + 1];
        return min(st[k][l], st[k][r - (1 << k) + 1]);
    }
};

// ---------- LCA binary lifting, 1-based, BFS không đệ quy ----------
struct LCA {
    int n = 0, LOG = 20;
    vector<vector<int>> adj, up;
    vector<int> depth;
    LCA() {}
    LCA(int n_) { init(n_); }
    void init(int n_) {
        n = n_;
        LOG = 20;
        while ((1 << LOG) <= n) LOG++;
        adj.assign(n + 1, {});
        up.assign(LOG, vector<int>(n + 1, 0));
        depth.assign(n + 1, 0);
    }
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    void build(int root = 1) {
        // BFS để tránh đệ quy sâu
        vector<int> st{root};
        up[0][root] = root;
        depth[root] = 0;
        vector<int> par(n + 1, 0);
        par[root] = root;
        size_t head = 0;
        // order BFS
        vector<int> order{root};
        while (head < order.size()) {
            int u = order[head++];
            for (int v : adj[u]) if (v != par[u]) {
                par[v] = u;
                depth[v] = depth[u] + 1;
                up[0][v] = u;
                order.push_back(v);
            }
        }
        for (int k = 1; k < LOG; k++)
            for (int v = 1; v <= n; v++)
                up[k][v] = up[k - 1][up[k - 1][v]];
    }
    int lca(int u, int v) const {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if (diff >> k & 1) u = up[k][u];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[k][u] != up[k][v]) {
                u = up[k][u];
                v = up[k][v];
            }
        return up[0][u];
    }
    int dist(int u, int v) const {
        int w = lca(u, v);
        return depth[u] + depth[v] - 2 * depth[w];
    }
};

#ifdef LOCAL_TEST_RMQ_LCA
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    SparseMin sp(vector<int>{5, 2, 8, 1, 9});
    assert(sp.query(1, 3) == 1);
    assert(sp.query(0, 4) == 1);
    LCA l(5);
    l.addEdge(1, 2); l.addEdge(1, 3); l.addEdge(2, 4); l.addEdge(2, 5);
    l.build(1);
    assert(l.lca(4, 5) == 2);
    assert(l.lca(4, 3) == 1);
    assert(l.dist(4, 5) == 2);
    cout << "OK\n";
    return 0;
}
#endif
