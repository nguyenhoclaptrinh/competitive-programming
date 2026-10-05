#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long d[10];
    for (int i = 0; i < 10; ++i) {
        if (!(cin >> d[i])) return 0;
    }
    long long c0 = d[0] + d[3] + d[6] + d[9];
    long long c1 = d[1] + d[4] + d[7];
    long long c2 = d[2] + d[5] + d[8];

    long long pairs = min(c1, c2);
    c1 -= pairs;
    c2 -= pairs;
    long long ans = c0 + pairs + c1 / 3 + c2 / 3;
    cout << ans << "\n";
    return 0;
}
