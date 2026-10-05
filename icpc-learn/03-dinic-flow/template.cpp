// Dinic max flow - template chuẩn (long long cap)
#include <bits/stdc++.h>
using namespace std;

struct Dinic {
    struct Edge { int to, rev; long long cap; };
    int n;
    vector<vector<Edge>> g;
    vector<int> level, it;
    Dinic(int n_ = 0) { init(n_); }
    void init(int n_) {
        n = n_;
        g.assign(n, {});
    }
    // đánh số đỉnh 0-based. Đồ thị có hướng.
    void addEdge(int u, int v, long long c) {
        Edge a{v, (int)g[v].size(), c};
        Edge b{u, (int)g[u].size(), 0};
        g[u].push_back(a);
        g[v].push_back(b);
    }
    bool bfs(int s, int t) {
        level.assign(n, -1);
        queue<int> q;
        level[s] = 0; q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : g[u])
                if (e.cap > 0 && level[e.to] < 0) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
        }
        return level[t] >= 0;
    }
    long long dfs(int u, int t, long long f) {
        if (u == t) return f;
        for (int &i = it[u]; i < (int)g[u].size(); i++) {
            Edge &e = g[u][i];
            if (e.cap > 0 && level[u] < level[e.to]) {
                long long d = dfs(e.to, t, min(f, e.cap));
                if (d > 0) {
                    e.cap -= d;
                    g[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }
    long long maxFlow(int s, int t) {
        long long flow = 0, INF = (long long)4e14;
        while (bfs(s, t)) {
            it.assign(n, 0);
            long long f;
            while ((f = dfs(s, t, INF)) > 0) flow += f;
        }
        return flow;
    }
    // sau maxFlow: đỉnh nào reachable từ s trên residual
    vector<char> minCutSide(int s) {
        vector<char> vis(n, 0);
        queue<int> q; q.push(s); vis[s] = 1;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : g[u])
                if (e.cap > 0 && !vis[e.to]) { vis[e.to] = 1; q.push(e.to); }
        }
        return vis;
    }
};

#ifdef LOCAL_TEST_DINIC
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // s=0, A=1, B=2, t=3
    Dinic d(4);
    d.addEdge(0, 1, 10); d.addEdge(0, 2, 5);
    d.addEdge(1, 3, 10); d.addEdge(2, 3, 5);
    d.addEdge(1, 2, 3);
    assert(d.maxFlow(0, 3) == 15);
    cout << "OK\n";
    return 0;
}
#endif
