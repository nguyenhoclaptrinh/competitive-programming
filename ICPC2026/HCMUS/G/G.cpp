#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> s(n + 1);
    vector<vector<int>> adj_in(n + 1);
    vector<vector<int>> adj_undir(n + 1);

    for (int i = 1; i <= n; ++i) {
        cin >> s[i];
        adj_in[s[i]].push_back(i);
        adj_undir[i].push_back(s[i]);
        adj_undir[s[i]].push_back(i);
    }

    vector<bool> visited(n + 1, false);
    vector<int> chosen_in_edge(n + 1, -1);
    int max_fulfilled = 0;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            vector<int> wcc;
            vector<int> q;
            q.push_back(i);
            visited[i] = true;
            int head = 0;
            while (head < q.size()) {
                int u = q[head++];
                wcc.push_back(u);
                for (int v : adj_undir[u]) {
                    if (!visited[v]) {
                        visited[v] = true;
                        q.push_back(v);
                    }
                }
            }

            vector<int> state(n + 1, 0); 
            int curr = wcc[0];
            while (state[curr] == 0) {
                state[curr] = 1;
                curr = s[curr];
            }
            
            vector<int> cycle;
            int cycle_start = curr;
            do {
                cycle.push_back(curr);
                curr = s[curr];
            } while (curr != cycle_start);

            vector<bool> in_cycle(n + 1, false);
            for (int u : cycle) in_cycle[u] = true;

            if (wcc.size() == cycle.size()) {
                for (size_t j = 1; j < cycle.size(); ++j) {
                    chosen_in_edge[cycle[j]] = cycle[j - 1];
                    max_fulfilled++;
                }
            } else {
                int v_break = -1;
                int u_break = -1;
                for (int v : cycle) {
                    for (int u : adj_in[v]) {
                        if (!in_cycle[u]) {
                            v_break = v;
                            u_break = u;
                            break;
                        }
                    }
                    if (v_break != -1) break;
                }

                for (int x : wcc) {
                    if (adj_in[x].empty()) continue;
                    if (x == v_break) {
                        chosen_in_edge[x] = u_break;
                        max_fulfilled++;
                    } else {
                        chosen_in_edge[x] = adj_in[x][0];
                        max_fulfilled++;
                    }
                }
            }
        }
    }

    vector<int> chosen_out_edge(n + 1, -1);
    vector<int> in_deg_chosen(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        if (chosen_in_edge[i] != -1) {
            chosen_out_edge[chosen_in_edge[i]] = i;
            in_deg_chosen[i]++;
        }
    }

    vector<int> seq;
    for (int i = 1; i <= n; ++i) {
        if (in_deg_chosen[i] == 0) {
            int curr = i;
            while (curr != -1) {
                seq.push_back(curr);
                curr = chosen_out_edge[curr];
            }
        }
    }

    vector<int> c(n + 1);
    for (int i = 0; i < n; ++i) {
        c[seq[i]] = i + 1;
    }

    cout << max_fulfilled << "\n";
    for (int i = 1; i <= n; ++i) {
        cout << c[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
