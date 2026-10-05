#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long n, m;
        cin >> n >> m;
        long long lo = 1, hi = 1;
        int par = 1; // 1 = odd, 0 = even; start row 1 odd
        bool ok = true;
        for (long long j = 1; j <= m; ++j) {
            long long l, r;
            cin >> l >> r;
            long long L = l + 1;
            long long R = n - r;
            if (j == 1) {
                // S1 = {1}, guaranteed L1==1 and R1>=1
                lo = 1; hi = 1; par = 1;
                if (L > R) ok = false; // safety, should not happen
                continue;
            }
            if (!ok) continue;
            long long nl = lo - 1;
            long long nh = hi + 1;
            int npar = par ^ 1;
            long long cl = max(nl, L);
            long long ch = min(nh, R);
            if (cl > ch) { ok = false; continue; }
            // cl>=1 here if cl<=ch and R>=1, L>=1; but guard negative parity
            // adjust to required parity (odd=1, even=0)
            long long clOdd = ((cl & 1LL) != 0) ? 1 : 0;
            // for safety with cl<=0 (only possible if L<=0, not possible since L>=1), handle via ((cl%2+2)%2)
            if (L <= 0) clOdd = ((cl % 2 + 2) % 2);
            long long chOdd = ((ch & 1LL) != 0) ? 1 : 0;
            if (ch <= 0) chOdd = ((ch % 2 + 2) % 2);
            if (clOdd != npar) ++cl;
            if (chOdd != npar) --ch;
            if (cl > ch) { ok = false; continue; }
            lo = cl; hi = ch; par = npar;
        }
        cout << (ok ? "YES\n" : "NO\n");
    }
    return 0;
}
