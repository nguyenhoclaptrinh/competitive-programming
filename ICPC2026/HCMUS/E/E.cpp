#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using u128 = unsigned __int128;

struct Interval {
    long long l, r;
    bool operator<(const Interval& other) const {
        if (l != other.l)
            return l < other.l;
        return r > other.r;
    }
};

void print128(u128 n) {
    if (n == 0) {
        cout << "0\n";
        return;
    }
    string s;
    while (n > 0) {
        s += (char)('0' + (n % 10));
        n /= 10;
    }
    reverse(s.begin(), s.end());
    cout << s << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<Interval> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].l >> a[i].r;
    }

    sort(a.begin(), a.end());

    vector<Interval> valid;
    long long max_r = -2000000000000000000LL; // Smaller than any possible coordinate

    for (int i = 0; i < n; i++) {
        if (a[i].r > max_r) {
            valid.push_back(a[i]);
            max_r = a[i].r;
        }
    }

    u128 ans = 0;
    for (size_t i = 0; i < valid.size(); i++) {
        u128 len = valid[i].r - valid[i].l;
        ans += len * len;
        
        if (i > 0) {
            long long overlap = valid[i-1].r - valid[i].l;
            if (overlap > 0) {
                u128 ov = overlap;
                ans -= ov * ov;
            }
        }
    }

    print128(ans);

    return 0;
}
