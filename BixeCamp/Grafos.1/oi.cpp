#include <bits/stdc++.h>
using namespace std;

struct Node {
    int i, j;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<string> grafo(n);
    for (int i = 0; i < n; i++) {
        cin >> grafo[i];
    }

    pair<int,int> start, end;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grafo[i][j] == 'A') start = {i, j};
            if (grafo[i][j] == 'B') end = {i, j};
        }
    }

    vector<vector<bool>> visitados(n, vector<bool>(m, false));
    vector<vector<pair<int,int>>> anterior(n, vector<pair<int,int>>(m, {-1, -1}));
    vector<vector<char>> passo(n, vector<char>(m));

    // Movimentos: D, U, L, R
    int di[4] = {1, -1, 0, 0};
    int dj[4] = {0, 0, -1, 1};
    char dir[4] = {'D', 'U', 'L', 'R'};

    queue<Node> fila;
    fila.push({start.first, start.second});
    visitados[start.first][start.second] = true;

    bool achou = false;
    while (!fila.empty()) {
        auto [i, j] = fila.front();
        fila.pop();

        if (make_pair(i, j) == end) {
            achou = true;
            break;
        }

        for (int k = 0; k < 4; k++) {
            int ni = i + di[k];
            int nj = j + dj[k];

            if (ni >= 0 && ni < n && nj >= 0 && nj < m &&
                !visitados[ni][nj] && grafo[ni][nj] != '#') {
                visitados[ni][nj] = true;
                anterior[ni][nj] = {i, j};
                passo[ni][nj] = dir[k];
                fila.push({ni, nj});
            }
        }
    }

    if (!achou) {
        cout << "NO\n";
    } else {
        cout << "YES\n";
        vector<char> caminho;
        int i = end.first, j = end.second;
        while (make_pair(i, j) != start) {
            caminho.push_back(passo[i][j]);
            auto p = anterior[i][j];
            i = p.first;
            j = p.second;
        }
        reverse(caminho.begin(), caminho.end());
        cout << caminho.size() << "\n";
        for (char c : caminho) cout << c;
        cout << "\n";
    }

    return 0;
}

