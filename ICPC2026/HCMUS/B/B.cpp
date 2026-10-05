#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> e, q;
vector<vector<int>> good_by_e;
vector<vector<int>> bad_by_e;

bool check(int K, vector<pair<int, int>>& plan_out) {
    vector<int> pool_good;
    vector<int> pool_bad;
    plan_out.assign(K + 1, {0, 0});
    
    for (int d = K; d >= 1; --d) {
        if (d == K) {
            for (int ev = K; ev <= 2000; ++ev) {
                for (int id : good_by_e[ev]) pool_good.push_back(id);
                for (int id : bad_by_e[ev]) pool_bad.push_back(id);
            }
        } else {
            for (int id : good_by_e[d]) pool_good.push_back(id);
            for (int id : bad_by_e[d]) pool_bad.push_back(id);
        }
        
        if (pool_good.empty()) return false;
        
        int u = pool_good.back();
        pool_good.pop_back();
        
        int v = -1;
        if (!pool_bad.empty()) {
            v = pool_bad.back();
            pool_bad.pop_back();
        } else if (!pool_good.empty()) {
            v = pool_good.back();
            pool_good.pop_back();
        } else {
            return false;
        }
        
        plan_out[d] = {u, v};
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    if (!(cin >> n)) return 0;
    
    e.resize(n + 1);
    q.resize(n + 1);
    good_by_e.resize(2005);
    bad_by_e.resize(2005);
    
    for (int i = 1; i <= n; ++i) {
        cin >> e[i] >> q[i];
        if (q[i] < 4) continue;
        if (q[i] == 4) {
            bad_by_e[e[i]].push_back(i);
        } else {
            good_by_e[e[i]].push_back(i);
        }
    }
    
    int L = 0, R = n / 2, ans = 0;
    vector<pair<int, int>> best_plan;
    
    while (L <= R) {
        int mid = L + (R - L) / 2;
        vector<pair<int, int>> plan;
        if (check(mid, plan)) {
            ans = mid;
            best_plan = move(plan);
            L = mid + 1;
        } else {
            R = mid - 1;
        }
    }
    
    cout << ans << "\n";
    for (int i = 1; i <= ans; ++i) {
        cout << best_plan[i].first << " " << best_plan[i].second << "\n";
    }
    
    return 0;
}
