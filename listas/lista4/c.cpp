#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
	int n, m; cin >> n >> m;
	vector<int> p (n);

	for(int i = 0; i < n; i++) {
		cin >> p[i];
	}

	int cap = 0;
	int k = 0;
	int cont = 0;

	while(k < n) {
		if(cap + p[k] <= m) {
			cap += p[k];
			k++;
		} else {
			cont++;
			cap = 0;
		}
	}

	if(cap != 0) {
		cont++;
	}

	cout << cont << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	solve();
    
    return 0;
}


