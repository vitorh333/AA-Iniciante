
using namespace std;
#define endl '\n'

void solve() {
    int n; 
    cin >> n;
    vector<int> p(n);

    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

    int resp = 0;
    while (true) {
        int maior = -1;
        int idx = -1;
        for (int i = 1; i < n; i++) {
            if (p[i] > maior) {
                maior = p[i];
                idx = i;
            }
        }

        if (p[0] > maior) break;
        p[0]++;
        p[idx]--;
        resp++;
    }

    cout << resp << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}

