#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    bool operator<(const Point& o) const {
        if (x != o.x) return x < o.x;
        return y < o.y;
    }
    bool operator==(const Point& o) const {
        return x == o.x && y == o.y;
    }
};

long long cross(Point O, Point A, Point B) {
    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

vector<Point> convex_hull(vector<Point> P) {
    int n = P.size(), k = 0;
    if (n <= 2) return P;
    vector<Point> H(2 * n);
    sort(P.begin(), P.end());
    for (int i = 0; i < n; ++i) {
        while (k >= 2 && cross(H[k - 2], H[k - 1], P[i]) <= 0) k--;
        H[k++] = P[i];
    }
    for (int i = n - 2, t = k + 1; i >= 0; i--) {
        while (k >= t && cross(H[k - 2], H[k - 1], P[i]) <= 0) k--;
        H[k++] = P[i];
    }
    H.resize(k - 1);
    return H;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int q;
    if (!(cin >> q)) return 0;
    vector<Point> S;
    long long max_area = 0;
    for (int i = 0; i < q; ++i) {
        Point p;
        cin >> p.x >> p.y;
        bool inside = false;
        if (S.size() >= 3) {
            inside = true;
            for (size_t j = 0; j < S.size(); ++j) {
                size_t nxt = (j + 1) % S.size();
                if (cross(S[j], S[nxt], p) < 0) {
                    inside = false;
                    break;
                }
            }
        }

        if (!inside) {
            S.push_back(p);
            if (S.size() > 1) {
                sort(S.begin(), S.end());
                S.erase(unique(S.begin(), S.end()), S.end());
            }
            if (S.size() >= 3) {
                S = convex_hull(S);
                int k = S.size();
                for (int u = 0; u < k; ++u) {
                    for (int v = u + 1; v < k; ++v) {
                        for (int l = v + 1; l < k; ++l) {
                            max_area = max(max_area, abs(cross(S[u], S[v], S[l])));
                        }
                    }
                }
            }
        }
        cout << max_area << "\n";
    }
    return 0;
}
