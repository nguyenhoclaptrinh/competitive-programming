#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> S(N);
    for (int i = 0; i < N; ++i) cin >> S[i];

    deque<int> q;
    int idx = 0;
    int ans = 0;
    for (int need = 1; need <= N; ++need) {
        if (!q.empty() && q.front() == need) {
            q.pop_front();
            ans = need;
            continue;
        }
        while (idx < N && S[idx] != need) {
            q.push_back(S[idx]);
            ++idx;
        }
        if (idx == N) break; // need blocked in siding or unreachable
        ++idx; // consume S[idx] == need directly to train
        ans = need;
    }
    cout << ans << "\n";
    return 0;
}
