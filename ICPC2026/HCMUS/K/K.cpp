#include <iostream>
#include <cmath>

using namespace std;

void solve() {
    double l, r, w, s;
    cin >> l >> r >> w >> s;
    int x = round((l + r + w + s) * 10.0);
    int q = x / 40;
    int rem = x % 40;
    
    int ans10 = q * 10;
    if (rem >= 30) {
        ans10 += 10;
    } else if (rem >= 10) {
        ans10 += 5;
    }
    
    cout << ans10 / 10 << "." << ans10 % 10 << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
