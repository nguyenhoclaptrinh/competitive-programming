#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;

struct Recipe {
    int id;
    int target;
    long long cost;
    int unsettled;
    long long current_sum;
};

int main() {
    // Optimize input/output operations for large input size
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> p(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> p[i];
    }

    vector<Recipe> recipes(m);
    vector<vector<int>> adj(n + 1);

    for (int j = 0; j < m; j++) {
        int t;
        long long c;
        int k;
        cin >> t >> c >> k;
        recipes[j].id = j;
        recipes[j].target = t;
        recipes[j].cost = c;
        recipes[j].unsettled = k;
        recipes[j].current_sum = c;

        for (int i = 0; i < k; i++) {
            int u;
            cin >> u;
            adj[u].push_back(j);
        }
    }

    // Priority queue to store {cost, component_id}, smallest cost first
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    vector<long long> best_cost(n + 1, INF);

    // Initialize with market prices
    for (int i = 1; i <= n; i++) {
        best_cost[i] = p[i];
        pq.push({best_cost[i], i});
    }

    // Dijkstra's algorithm modified for hypergraphs
    while (!pq.empty()) {
        auto [c, u] = pq.top();
        pq.pop();

        // If we already found a better cost, skip this stale entry
        if (c > best_cost[u]) continue;

        // Process all recipes that require component u as an input
        for (int r_id : adj[u]) {
            recipes[r_id].current_sum += c;
            recipes[r_id].unsettled--;

            // If all inputs for this recipe have been optimally resolved
            if (recipes[r_id].unsettled == 0) {
                // Check if this recipe offers a cheaper way to obtain its target component
                if (recipes[r_id].current_sum < best_cost[recipes[r_id].target]) {
                    best_cost[recipes[r_id].target] = recipes[r_id].current_sum;
                    pq.push({best_cost[recipes[r_id].target], recipes[r_id].target});
                }
            }
        }
    }

    // Output the results
    for (int i = 1; i <= n; i++) {
        cout << best_cost[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
