#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<int> R(m), C(m);
    for (int i = 0; i < m; ++i) cin >> R[i] >> C[i];

    if (m == 0) {
        cout << 0 << "\n";
        return 0;
    }

    int N = 2 * n;
    vector<vector<pair<int,int>>> adj(N);
    adj.reserve(N);
    vector<int> U;
    vector<int> V;
    U.reserve(m + n + 5);
    V.reserve(m + n + 5);
    vector<char> isDummy;
    isDummy.reserve(m + n + 5);

    for (int i = 0; i < m; ++i) {
        int u = R[i] - 1;
        int v = n + (C[i] - 1);
        U.push_back(u); V.push_back(v); isDummy.push_back(0);
        adj[u].emplace_back(v, i);
        adj[v].emplace_back(u, i);
    }

    vector<char> vis(N, 0);
    vector<int> compVerts;
    compVerts.reserve(1024);
    vector<int> stack;
    // Process each component: find odds, add dummy edges
    // To avoid O(N^2), iterate vertices with degree>0
    int totalEdges = m;
    for (int s = 0; s < N; ++s) {
        if (adj[s].empty() || vis[s]) continue;
        compVerts.clear();
        stack.clear();
        stack.push_back(s);
        vis[s] = 1;
        while (!stack.empty()) {
            int v = stack.back(); stack.pop_back();
            compVerts.push_back(v);
            for (auto [to, id] : adj[v]) {
                if (!vis[to]) { vis[to] = 1; stack.push_back(to); }
            }
        }
        vector<int> odds;
        for (int v : compVerts) if ((int)adj[v].size() % 2 == 1) odds.push_back(v);
        // pair odds
        for (size_t i = 0; i + 1 < odds.size(); i += 2) {
            int a = odds[i], b = odds[i+1];
            int id = totalEdges++;
            U.push_back(a); V.push_back(b); isDummy.push_back(1);
            adj[a].emplace_back(b, id);
            adj[b].emplace_back(a, id);
        }
    }

    vector<size_t> ptr(N, 0);
    vector<char> used(totalEdges, 0);
    // Note: totalEdges grew during pairing; 'used' sized after pairing? We sized before.
    // Fix: resize (new dummies marked unused)
    // used already has size = final totalEdges because totalEdges updated; but we created with old size.
    // Recreate correctly:
    used.assign(totalEdges, 0);

    vector<char> compDone(N, 0);
    // Need component traversal for Eulerian: reuse BFS via unused edges.
    // We'll run Hierholzer starting from each unprocessed vertex with unused edges.
    // Since each augmented component is Eulerian, one circuit covers it.
    vector<vector<int>> trails; // list of edge ids (real only) per trail
    vector<int> st_v;
    vector<int> st_e;
    vector<int> circ;

    for (int s = 0; s < N; ++s) {
        if (adj[s].empty()) continue;
        // check if there's any unused edge incident (quick: if all used skip via pointer? simpler: try start only if exists unused)
        bool hasUnused = false;
        for (auto [to, id] : adj[s]) if (!used[id]) { hasUnused = true; break; }
        if (!hasUnused) continue;
        // Hierholzer from s
        st_v.clear(); st_e.clear(); circ.clear();
        st_v.push_back(s);
        st_e.push_back(-1);
        while (!st_v.empty()) {
            int v = st_v.back();
            // advance ptr to unused edge
            int nid = -1, nto = -1;
            while (ptr[v] < adj[v].size()) {
                auto [to, id] = adj[v][ptr[v]++];
                if (!used[id]) { nid = id; nto = to; break; }
            }
            if (nid != -1) {
                used[nid] = 1;
                st_v.push_back(nto);
                st_e.push_back(nid);
            } else {
                int eid = st_e.back();
                st_v.pop_back(); st_e.pop_back();
                if (eid != -1) circ.push_back(eid);
            }
        }
        if (circ.empty()) continue;
        reverse(circ.begin(), circ.end());
        // circ is closed trail (Eulerian circuit of this component). Split at dummies.
        int L = (int)circ.size();
        int dummyCnt = 0;
        for (int id : circ) if (isDummy[id]) ++dummyCnt;
        if (dummyCnt == 0) {
            // one trail, keep only real edges (all real)
            trails.push_back(circ);
        } else {
            // rotate to start after a dummy
            int start = 0;
            for (int i = 0; i < L; ++i) if (isDummy[circ[i]]) { start = (i + 1) % L; break; }
            vector<int> cur;
            cur.reserve(64);
            for (int k = 0; k < L; ++k) {
                int id = circ[(start + k) % L];
                if (isDummy[id]) {
                    if (!cur.empty()) { trails.push_back(cur); cur.clear(); }
                } else {
                    cur.push_back(id);
                }
            }
            if (!cur.empty()) trails.push_back(cur);
        }
    }

    // Safety: any leftover unused real edges (shouldn't happen) -> each as singleton
    for (int id = 0; id < m; ++id) if (!used[id]) {
        trails.push_back(vector<int>{id});
    }

    cout << trails.size() << "\n";
    for (auto &tr : trails) {
        cout << tr.size() << "\n";
        for (int eid : tr) {
            cout << R[eid] << ' ' << C[eid] << "\n";
        }
    }
    return 0;
}
