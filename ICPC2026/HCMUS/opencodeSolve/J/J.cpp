#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> dist(n + 1);
    for (int i = 1; i <= n; ++i) cin >> dist[i];

    vector<int> rt(m);
    vector<long long> rc(m);
    vector<int> rem(m);
    vector<long long> rsum(m, 0);
    vector<vector<int>> adj(n + 1);

    for (int j = 0; j < m; ++j) {
        int t, k;
        long long c;
        cin >> t >> c >> k;
        rt[j] = t;
        rc[j] = c;
        rem[j] = k;
        for (int s = 0; s < k; ++s) {
            int a;
            cin >> a;
            adj[a].push_back(j);
        }
    }

    using pli = pair<long long,int>;
    priority_queue<pli, vector<pli>, greater<pli>> pq;
    for (int i = 1; i <= n; ++i) pq.emplace(dist[i], i);
    vector<char> done(n + 1, 0);

    while (!pq.empty()) {
        auto [d, v] = pq.top(); pq.pop();
        if (d != dist[v]) continue;
        if (done[v]) continue;
        done[v] = 1;
        for (int r : adj[v]) {
            int t = rt[r];
            if (done[t]) continue;
            rsum[r] += d;
            if (--rem[r] == 0) {
                long long cand = rsum[r] + rc[r];
                if (cand < dist[t]) {
                    dist[t] = cand;
                    pq.emplace(cand, t);
                }
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (i > 1) cout << ' ';
        cout << dist[i];
    }
    cout << '\n';
    return 0;
}
