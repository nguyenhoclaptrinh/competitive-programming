#include <bits/stdc++.h>
using namespace std;

struct Node {
    int e;
    int q;
    int idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> e(n + 1), q(n + 1);
    for (int i = 1; i <= n; ++i) cin >> e[i] >> q[i];

    vector<Node> v;
    v.reserve(n);
    for (int i = 1; i <= n; ++i) {
        if (q[i] >= 4) v.push_back({e[i], q[i], i});
    }
    sort(v.begin(), v.end(), [](const Node& a, const Node& b) {
        return a.e > b.e;
    });
    int m = (int)v.size();

    auto feasible = [&](int K) -> bool {
        vector<Node> poolA, poolB;
        poolA.reserve(m); poolB.reserve(m);
        int p = 0;
        for (int d = K; d >= 1; --d) {
            while (p < m && v[p].e >= d) {
                if (v[p].q == 4) poolA.push_back(v[p]);
                else poolB.push_back(v[p]);
                ++p;
            }
            if (poolB.empty()) return false;
            if (poolA.size() + poolB.size() < 2) return false;
            poolB.pop_back();
            if (!poolA.empty()) poolA.pop_back();
            else poolB.pop_back();
        }
        return true;
    };

    int lo = 0, hi = m / 2;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (feasible(mid)) lo = mid;
        else hi = mid - 1;
    }
    int K = lo;

    vector<pair<int,int>> ans(K + 1, {-1, -1});
    {
        vector<Node> poolA, poolB;
        poolA.reserve(m); poolB.reserve(m);
        int p = 0;
        for (int d = K; d >= 1; --d) {
            while (p < m && v[p].e >= d) {
                if (v[p].q == 4) poolA.push_back(v[p]);
                else poolB.push_back(v[p]);
                ++p;
            }
            // feasible guarantees success
            Node hb = poolB.back(); poolB.pop_back();
            Node other;
            if (!poolA.empty()) { other = poolA.back(); poolA.pop_back(); }
            else { other = poolB.back(); poolB.pop_back(); }
            ans[d] = {hb.idx, other.idx};
        }
    }

    cout << K << "\n";
    for (int d = 1; d <= K; ++d) {
        cout << ans[d].first << ' ' << ans[d].second << "\n";
    }
    return 0;
}
