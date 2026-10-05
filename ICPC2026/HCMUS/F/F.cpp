#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> S;

bool check(int M) {
    vector<int> S_M;
    int F_M = -1;
    for (int i = 0; i < N; ++i) {
        if (S[i] <= M) {
            S_M.push_back(S[i]);
        }
        if (S[i] > M && F_M == -1) {
            F_M = i;
        }
    }
    
    int t1 = -1, t2 = -1;
    for (int x : S_M) {
        if (x > t2) {
            t2 = x;
        } else if (x > t1) {
            t1 = x;
        } else {
            return false;
        }
    }
    
    if (F_M != -1) {
        int last = -1;
        for (int i = F_M + 1; i < N; ++i) {
            if (S[i] <= M) {
                if (S[i] <= last) return false;
                last = S[i];
            }
        }
    }
    
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    if (!(cin >> N)) return 0;
    S.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }
    
    int low = 1, high = N, ans = 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
