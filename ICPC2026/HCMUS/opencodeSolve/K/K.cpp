#include <bits/stdc++.h>
using namespace std;

static int parse2(const string &s) {
    // s like "5.0" or "5.5", 0.0..9.0
    size_t pos = s.find('.');
    int ip = stoi(s.substr(0, pos));
    int half = 0;
    if (pos != string::npos && pos + 1 < s.size() && s[pos + 1] == '5')
        half = 1;
    return ip * 2 + half;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (!(cin >> T)) return 0;
    for (int t = 0; t < T; ++t) {
        string sl, sr, sw, ss;
        cin >> sl >> sr >> sw >> ss;
        int s2 = parse2(sl) + parse2(sr) + parse2(sw) + parse2(ss);
        int k = (s2 + 2) / 4; // round(s2/4) half-up, overall*2
        cout << (k / 2) << '.' << ((k % 2) ? '5' : '0') << '\n';
    }
    return 0;
}
