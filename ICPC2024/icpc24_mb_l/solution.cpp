#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 1e9 + 7;
static const int MAXA = 1000000;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) {
        return 0;
    }

    vector<int> freq(MAXA + 1, 0);
    for (int i = 0; i < n; ++i) {
        int val;
        cin >> val;
        if (val <= MAXA) {
            freq[val]++;
        }
    }

    long long total_pairs = 0;
    for (int val = 1; val <= MAXA; ++val) {
        if (freq[val] > 1) {
            long long k = freq[val];
            long long pairs = (k * (k - 1) / 2) % MOD;
            total_pairs = (total_pairs + pairs) % MOD;
        }
    }

    cout << total_pairs << "\n";

    return 0;
}
