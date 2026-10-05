#include <bits/stdc++.h>
using namespace std;

struct Pt {
    long long x, y;
    bool operator<(Pt const& o) const {
        if (x != o.x) return x < o.x;
        return y < o.y;
    }
    bool operator==(Pt const& o) const { return x == o.x && y == o.y; }
};

static inline __int128 cross(const Pt& O, const Pt& A, const Pt& B) {
    return (__int128)(A.x - O.x) * (B.y - O.y) - (__int128)(A.y - O.y) * (B.x - O.x);
}
static inline __int128 abs128(__int128 v) { return v >= 0 ? v : -v; }

vector<Pt> convex_hull(vector<Pt> pts) {
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    int n = (int)pts.size();
    if (n <= 1) return pts;
    vector<Pt> lo, hi;
    for (auto& p : pts) {
        while (lo.size() >= 2 && cross(lo[lo.size()-2], lo.back(), p) <= 0)
            lo.pop_back();
        lo.push_back(p);
    }
    for (int i = n - 1; i >= 0; --i) {
        Pt p = pts[i];
        while (hi.size() >= 2 && cross(hi[hi.size()-2], hi.back(), p) <= 0)
            hi.pop_back();
        hi.push_back(p);
    }
    lo.pop_back();
    hi.pop_back();
    lo.insert(lo.end(), hi.begin(), hi.end());
    return lo; // CCW, minimal vertices
}

bool pointInConvex(const vector<Pt>& h, const Pt& p) {
    int n = (int)h.size();
    if (n == 0) return false;
    if (n == 1) return p == h[0];
    if (n == 2) {
        if (cross(h[0], h[1], p) != 0) return false;
        long long mnx = min(h[0].x, h[1].x), mxx = max(h[0].x, h[1].x);
        long long mny = min(h[0].y, h[1].y), mxy = max(h[0].y, h[1].y);
        return p.x >= mnx && p.x <= mxx && p.y >= mny && p.y <= mxy;
    }
    for (int i = 0; i < n; ++i) {
        if (cross(h[i], h[(i + 1) % n], p) < 0) return false;
    }
    return true;
}

// Max doubled area of inscribed triangle in convex polygon (CCW), O(n^2).
long long maxDoubleArea(const vector<Pt>& h) {
    int n = (int)h.size();
    if (n < 3) return 0;
    vector<Pt> q(2 * n);
    for (int i = 0; i < 2 * n; ++i) q[i] = h[i % n];
    __int128 best = 0;
    for (int i = 0; i < n; ++i) {
        int k = i + 2;
        for (int j = i + 1; j < i + n - 1; ++j) {
            if (k < j + 1) k = j + 1;
            while (k + 1 < i + n) {
                __int128 cur = abs128(cross(q[i], q[j], q[k]));
                __int128 nxt = abs128(cross(q[i], q[j], q[k + 1]));
                if (nxt > cur) ++k;
                else break;
            }
            __int128 a = abs128(cross(q[i], q[j], q[k]));
            if (a > best) best = a;
        }
    }
    return (long long)best;
}

static inline __int128 dist2(const Pt& a, const Pt& b) {
    __int128 dx = (__int128)a.x - b.x, dy = (__int128)a.y - b.y;
    return dx * dx + dy * dy;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    vector<Pt> hull;
    hull.reserve(64);
    long long cur = 0;
    for (int t = 0; t < q; ++t) {
        Pt p;
        cin >> p.x >> p.y;
        if (hull.empty()) {
            hull.push_back(p);
        } else if (hull.size() == 1) {
            if (!(p == hull[0])) {
                hull.push_back(p);
            }
        } else if (hull.size() == 2) {
            Pt a = hull[0], b = hull[1];
            if (cross(a, b, p) == 0) {
                // collinear: keep diameter pair among {a,b,p}
                __int128 d_ab = dist2(a, b);
                __int128 d_ap = dist2(a, p);
                __int128 d_bp = dist2(b, p);
                if (d_ap >= d_ab && d_ap >= d_bp) {
                    hull[1] = p;
                } else if (d_bp >= d_ab && d_bp >= d_ap) {
                    hull[0] = p;
                } // else unchanged
            } else {
                vector<Pt> tmp = {a, b, p};
                hull = convex_hull(tmp);
                cur = maxDoubleArea(hull);
            }
        } else {
            if (!pointInConvex(hull, p)) {
                vector<Pt> tmp = hull;
                tmp.push_back(p);
                hull = convex_hull(tmp);
                cur = maxDoubleArea(hull);
            }
        }
        cout << cur << '\n';
    }
    return 0;
}
