#include <bits/stdc++.h>
using namespace std;

const int MAXV = 400005;
const int MAXE = 600005;

int n, m;
int r_coord[MAXE], c_coord[MAXE];
vector<pair<int, int>> adj[MAXV];
bool used_edge[MAXE];
vector<int> path_edges;

void get_path(int start_node) {
    vector<pair<int, int>> st;
    st.push_back({start_node, -1});
    while (!st.empty()) {
        int u = st.back().first;
        bool found = false;
        while (!adj[u].empty()) {
            auto edge = adj[u].back();
            adj[u].pop_back();
            if (used_edge[edge.second]) continue;
            used_edge[edge.second] = true;
            st.push_back(edge);
            found = true;
            break;
        }
        if (!found) {
            int id = st.back().second;
            st.pop_back();
            if (id != -1) {
                path_edges.push_back(id);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n >> m)) return 0;

    for (int i = 1; i <= m; i++) {
        cin >> r_coord[i] >> c_coord[i];
        adj[r_coord[i]].push_back({n + c_coord[i], i});
        adj[n + c_coord[i]].push_back({r_coord[i], i});
    }

    int dummy_edges = m + 1;
    for (int i = 1; i <= 2 * n; i++) {
        if (adj[i].size() % 2 != 0) {
            adj[0].push_back({i, dummy_edges});
            adj[i].push_back({0, dummy_edges});
            dummy_edges++;
        }
    }

    vector<vector<int>> sequences;

    // Process all odd components (connected to dummy vertex 0)
    get_path(0);
    if (!path_edges.empty()) {
        vector<int> current_seq;
        for (int i = (int)path_edges.size() - 1; i >= 0; i--) {
            int id = path_edges[i];
            if (id > m) {
                if (!current_seq.empty()) {
                    sequences.push_back(current_seq);
                    current_seq.clear();
                }
            } else {
                current_seq.push_back(id);
            }
        }
        if (!current_seq.empty()) {
            sequences.push_back(current_seq);
        }
        path_edges.clear();
    }

    // Process remaining even components
    for (int i = 1; i <= 2 * n; i++) {
        if (!adj[i].empty()) {
            get_path(i);
            if (!path_edges.empty()) {
                vector<int> current_seq;
                for (int j = (int)path_edges.size() - 1; j >= 0; j--) {
                    int id = path_edges[j];
                    if (id > m) {
                        // Should not happen for isolated even components
                        if (!current_seq.empty()) {
                            sequences.push_back(current_seq);
                            current_seq.clear();
                        }
                    } else {
                        current_seq.push_back(id);
                    }
                }
                if (!current_seq.empty()) {
                    sequences.push_back(current_seq);
                }
                path_edges.clear();
            }
        }
    }

    cout << sequences.size() << "\n";
    for (auto& seq : sequences) {
        cout << seq.size() << "\n";
        for (int id : seq) {
            cout << r_coord[id] << " " << c_coord[id] << "\n";
        }
    }

    return 0;
}
