#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    // Optimize input/output operations
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long d[10];
    for (int i = 0; i < 10; ++i) {
        cin >> d[i];
    }

    // Single digits that are divisible by 3: 0, 3, 6, 9
    long long ans = d[0] + d[3] + d[6] + d[9];

    // Digits that leave a remainder of 1 when divided by 3
    long long c1 = d[1] + d[4] + d[7];

    // Digits that leave a remainder of 2 when divided by 3
    long long c2 = d[2] + d[5] + d[8];

    // Pair one digit from c1 and one digit from c2 to form a sum divisible by 3
    long long pairs = min(c1, c2);
    ans += pairs;

    // Remaining digits from either c1 or c2 can be grouped in threes
    ans += (max(c1, c2) - pairs) / 3;

    cout << ans << "\n";

    return 0;
}
