#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
    int n;
    cin >> n;
    multiset<int> heap;
    vector<string> respostas;

    for (int i = 0; i < n; i++) {
        string c;
        cin >> c;

        if (c == "insert") {
            int num; 
            cin >> num;
            heap.insert(num);
            respostas.push_back("insert " + to_string(num));

        } else if (c == "removeMin") {
            if (heap.empty()) {
                //ELE NAO DIZ NADA SOBRE SER INVALIDO TENAR REMOVER ALGO QUE NAO ESTA NO SET, SE FOR ISSO EU VOU FICAR MT PUTO
                respostas.push_back("insert 0");
                heap.insert(0);
            }
            heap.erase(heap.begin());
            respostas.push_back("removeMin");

        } else if (c == "getMin") {
            int num; 
            cin >> num;

            while (!heap.empty() && *heap.begin() < num) {
                heap.erase(heap.begin());
                respostas.push_back("removeMin");
            }

            if (heap.empty() || *heap.begin() > num) {
                heap.insert(num);
                respostas.push_back("insert " + to_string(num));
            }

            respostas.push_back("getMin " + to_string(num));
        }
    }

    cout << (int)respostas.size() << endl;
    for (auto &linha : respostas) {
        cout << linha << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}

