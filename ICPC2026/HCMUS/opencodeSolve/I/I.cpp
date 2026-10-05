#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n + 1, 0);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    const long long NEG = (long long)-4e18;
    vector<long long> dp(n + 1, NEG);
    dp[0] = 0;

    long long ans = NEG;
    // Special case: jump directly off from 0 (possible iff n < 2)
    if (n < 2) ans = 0;

    long long Tprev = 0; // T_{t-1}
    for (long long t = 1; ; ++t) {
        long long Tt = t * (t + 1) / 2;
        if (Tt > n) break;
        for (long long b = 0; b <= t; ++b) {
            long long p = Tt + b;
            if (p > n) break;
            if (p < 1) continue;
            long long best;
            if (b == 0) {
                best = dp[Tprev]; // q = T_{t-1}
            } else if (b == t) {
                best = dp[Tprev + t - 1]; // q = T_{t-1}+t-1
            } else {
                best = max(dp[Tprev + b], dp[Tprev + b - 1]);
            }
            dp[p] = a[(size_t)p] + best;
            if (p + t + 2 > n) ans = max(ans, dp[p]);
        }
        Tprev = Tt;
    }
    cout << ans << '\n';
    return 0;
}
