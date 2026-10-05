#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> s(n + 1);
    for (int i = 1; i <= n; ++i) cin >> s[i];

    vector<vector<int>> pred(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        pred[s[i]].push_back(i);
        indeg[s[i]]++;
    }

    // tentative choice: one incoming per node if exists
    vector<int> choice(n + 1, -1);
    for (int v = 1; v <= n; ++v) {
        if (!pred[v].empty()) choice[v] = pred[v][0];
    }

    // find cycle nodes via peeling
    vector<int> deg = indeg;
    queue<int> q;
    for (int v = 1; v <= n; ++v) if (deg[v] == 0) q.push(v);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        int v = s[u];
        if (--deg[v] == 0) q.push(v);
    }
    vector<char> isCycle(n + 1, 0);
    for (int v = 1; v <= n; ++v) if (deg[v] > 0) isCycle[v] = 1;

    vector<char> visCyc(n + 1, 0);
    for (int v = 1; v <= n; ++v) if (isCycle[v] && !visCyc[v]) {
        // collect one cycle
        vector<int> cyc;
        int cur = v;
        while (!visCyc[cur]) {
            visCyc[cur] = 1;
            cyc.push_back(cur);
            cur = s[cur];
        }
        // cyc may contain tail if v wasn't on cycle? But v is cycle node,
        // walking from cycle node stays on cycle, so cyc is exactly the cycle
        // (possibly rotated). Verify: cur should be v.
        // Build cycle predecessor map: pred along cycle
        // cyc is in s-order: cyc[i+1] = s[cyc[i]] (with wrap if closed).
        // Check closure:
        // If walk returned to v, cyc is the cycle.
        unordered_map<int,int> pos;
        pos.reserve(cyc.size()*2);
        for (int i = 0; i < (int)cyc.size(); ++i) pos[cyc[i]] = i;
        // In case cyc includes extra (shouldn't happen), trim to actual cycle:
        // Find start of cycle within cyc: since start v is on cycle, whole cyc is cycle.
        int k = (int)cyc.size();
        // Build cycle_pred for each node in cyc
        vector<int> cycPred(n + 1, -2); // only use for nodes in cyc; use map instead
        // Since cyc follows s, predecessor of cyc[(i+1)%k] is cyc[i] provided s[cyc[k-1]]==cyc[0]
        // Verify closure:
        if (s[cyc.back()] != cyc.front()) {
            // Should not happen for cycle start, but handle generally:
            // find actual cycle: walk again to extract
            // Fallback: extract cycle containing v
            cyc.clear();
            cur = v;
            do {
                cyc.push_back(cur);
                cur = s[cur];
            } while (cur != v);
            k = (int)cyc.size();
        }
        unordered_map<int,int> cyc_pred;
        for (int i = 0; i < k; ++i) {
            int node = cyc[(i + 1) % k];
            int pr = cyc[i];
            cyc_pred[node] = pr;
        }
        bool fully = true;
        for (int node : cyc) {
            if (choice[node] != cyc_pred[node]) { fully = false; break; }
        }
        if (fully) {
            int swapNode = -1;
            int swapAlt = -1;
            for (int node : cyc) {
                if ((int)pred[node].size() >= 2) {
                    for (int u : pred[node]) if (u != cyc_pred[node]) {
                        swapNode = node; swapAlt = u; break;
                    }
                    break;
                }
            }
            if (swapNode != -1) {
                choice[swapNode] = swapAlt;
            } else {
                // pure cycle: drop one edge
                choice[cyc[0]] = -1;
            }
        }
    }

    vector<int> nxt(n + 1, -1);
    for (int u = 1; u <= n; ++u) {
        int v = s[u];
        if (choice[v] == u) nxt[u] = v;
    }

    vector<int> order;
    order.reserve(n);
    vector<char> seen(n + 1, 0);
    for (int v = 1; v <= n; ++v) if (choice[v] == -1) {
        int cur = v;
        while (cur != -1 && !seen[cur]) {
            seen[cur] = 1;
            order.push_back(cur);
            cur = nxt[cur];
        }
    }
    // Any leftover (should be none since acyclic, but safety)
    for (int v = 1; v <= n; ++v) if (!seen[v]) {
        int cur = v;
        while (cur != -1 && !seen[cur]) {
            seen[cur] = 1;
            order.push_back(cur);
            cur = nxt[cur];
        }
    }

    // order = students on chairs 1..n
    vector<int> c(n + 1);
    for (int i = 0; i < n; ++i) c[order[i]] = i + 1;

    int M = 0;
    for (int i = 0; i + 1 < n; ++i) {
        int u = order[i];
        if (s[u] == order[i + 1]) ++M;
    }

    cout << M << "\n";
    for (int i = 1; i <= n; ++i) {
        if (i > 1) cout << ' ';
        cout << c[i];
    }
    cout << "\n";
    return 0;
}
