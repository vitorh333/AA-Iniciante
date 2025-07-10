#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {

	int n; cin >> n;
	vector<int> p (n);

	for(int i = 0; i < n; i++) {
		cin >> p[i];
	}

	int vida = 0;
	int cont = 0;

	for(int i = 0; i < n; i++) {
		if(vida + p[i] >= 0) {
			cont++;
			vida += p[i];
		}
	}

	cout << cont << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	solve();

    
    return 0;
}


