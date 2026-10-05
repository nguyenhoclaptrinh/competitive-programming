#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    
    bool possible = true;
    int min_r = 1, max_r = 1;
    
    for (int j = 1; j <= m; ++j) {
        int l, r;
        cin >> l >> r;
        
        if (!possible) {
            continue;
        }
        
        if (j == 1) {
            min_r = 1;
            max_r = 1;
            if (l >= 1 || 1 > n - r) {
                possible = false;
            }
        } else {
            int new_min_r = min_r - 1;
            int new_max_r = max_r + 1;
            
            new_min_r = max(new_min_r, l + 1);
            new_max_r = min(new_max_r, n - r);
            
            if (new_min_r % 2 != j % 2) {
                new_min_r++;
            }
            if (new_max_r % 2 != j % 2) {
                new_max_r--;
            }
            
            if (new_min_r > new_max_r) {
                possible = false;
            } else {
                min_r = new_min_r;
                max_r = new_max_r;
            }
        }
    }
    
    if (possible) cout << "YES\n";
    else cout << "NO\n";
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
