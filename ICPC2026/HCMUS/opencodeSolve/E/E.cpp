#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long pos;
    uint8_t kind; // 0=addL,1=remL,2=addR,3=remR
    int idx;
    bool operator<(Event const& o) const { return pos < o.pos; }
};

string toString(__int128 x) {
    if (x == 0) return "0";
    bool neg = false;
    if (x < 0) { neg = true; x = -x; }
    string s;
    while (x > 0) {
        int d = int(x % 10);
        s.push_back('0' + d);
        x /= 10;
    }
    if (neg) s.push_back('-');
    reverse(s.begin(), s.end());
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> L(N), R(N);
    for (int i = 0; i < N; ++i) cin >> L[i] >> R[i];

    vector<long long> coords;
    coords.reserve(3LL * N);
    vector<long long> allL2; allL2.reserve(N);
    vector<long long> allR2; allR2.reserve(N);
    for (int i = 0; i < N; ++i) {
        long long l2 = 2 * L[i];
        long long r2 = 2 * R[i];
        long long m = L[i] + R[i];
        coords.push_back(l2);
        coords.push_back(m);
        coords.push_back(r2);
        allL2.push_back(l2);
        allR2.push_back(r2);
    }
    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());

    sort(allL2.begin(), allL2.end());
    allL2.erase(unique(allL2.begin(), allL2.end()), allL2.end());
    sort(allR2.begin(), allR2.end());
    allR2.erase(unique(allR2.begin(), allR2.end()), allR2.end());
    int nL = (int)allL2.size();
    int nR = (int)allR2.size();

    vector<Event> ev;
    ev.reserve(4LL * N);
    for (int i = 0; i < N; ++i) {
        long long l2 = 2 * L[i];
        long long r2 = 2 * R[i];
        long long m = L[i] + R[i];
        int il = lower_bound(allL2.begin(), allL2.end(), l2) - allL2.begin();
        int ir = lower_bound(allR2.begin(), allR2.end(), r2) - allR2.begin();
        ev.push_back({l2, 0, il});
        ev.push_back({m, 1, il});
        ev.push_back({m, 2, ir});
        ev.push_back({r2, 3, ir});
    }
    sort(ev.begin(), ev.end());

    priority_queue<int, vector<int>, greater<int>> pqL;
    priority_queue<int> pqR;
    vector<int> delL(nL, 0), delR(nR, 0);

    auto cleanL = [&]() {
        while (!pqL.empty() && delL[pqL.top()] > 0) {
            delL[pqL.top()]--;
            pqL.pop();
        }
    };
    auto cleanR = [&]() {
        while (!pqR.empty() && delR[pqR.top()] > 0) {
            delR[pqR.top()]--;
            pqR.pop();
        }
    };

    __int128 S = 0; // sum of (v0+v1)*D, answer = S/2
    size_t e = 0;
    int M = (int)coords.size();
    for (int k = 0; k + 1 < M; ++k) {
        long long P0 = coords[k];
        while (e < ev.size() && ev[e].pos == P0) {
            if (ev[e].kind == 0) pqL.push(ev[e].idx);
            else if (ev[e].kind == 1) delL[ev[e].idx]++;
            else if (ev[e].kind == 2) pqR.push(ev[e].idx);
            else delR[ev[e].idx]++;
            ++e;
        }
        // events with pos < P0 should already be consumed; defensively consume < P0 too
        // (not needed since pos set == coords set, but keep safe if duplicate handling)
        long long P1 = coords[k + 1];
        long long D = P1 - P0;
        if (D == 0) continue;
        cleanL();
        cleanR();
        bool hasA = !pqL.empty();
        bool hasB = !pqR.empty();
        if (!hasA && !hasB) continue;
        if (hasA && hasB) {
            long long a = allL2[pqL.top()];
            long long b = allR2[pqR.top()];
            long long vA0 = P0 - a;
            long long vA1 = P1 - a;
            long long vB0 = b - P0;
            long long vB1 = b - P1;
            // active sets guarantee non-negative, but min/max over active keeps it;
            // if due to stale entries negative appears, treat as absent (should not happen)
            if (vA0 < 0 || vA1 < 0) { hasA = false; }
            if (vB0 < 0 || vB1 < 0) { hasB = false; }
            if (hasA && hasB) {
                long long d0 = vA0 - vB0;
                long long d1 = vA1 - vB1;
                if (d0 >= 0 && d1 >= 0) {
                    S += (__int128)(vA0 + vA1) * D;
                } else if (d0 <= 0 && d1 <= 0) {
                    S += (__int128)(vB0 + vB1) * D;
                } else {
                    long long Xstar = (a + b) / 2; // a,b even -> exact
                    long long D1 = Xstar - P0;
                    long long D2 = P1 - Xstar;
                    long long Vc = (b - a) / 2;
                    if (d0 < 0) {
                        // B left, A right
                        S += (__int128)(vB0 + Vc) * D1 + (__int128)(Vc + vA1) * D2;
                    } else {
                        S += (__int128)(vA0 + Vc) * D1 + (__int128)(Vc + vB1) * D2;
                    }
                }
                continue;
            }
        }
        if (hasA) {
            long long a = allL2[pqL.top()];
            long long vA0 = P0 - a;
            long long vA1 = P1 - a;
            if (vA0 < 0) vA0 = 0;
            if (vA1 < 0) vA1 = 0;
            // if leg not actually covering (should not happen), skip when negative
            // covering check: v>=0 suffices since active implies covering
            S += (__int128)(vA0 + vA1) * D;
        } else if (hasB) {
            long long b = allR2[pqR.top()];
            long long vB0 = b - P0;
            long long vB1 = b - P1;
            if (vB0 < 0) vB0 = 0;
            if (vB1 < 0) vB1 = 0;
            S += (__int128)(vB0 + vB1) * D;
        }
    }

    __int128 ans = S / 2;
    cout << toString(ans) << "\n";
    return 0;
}
