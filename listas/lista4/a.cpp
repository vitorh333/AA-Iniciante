#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
	int t; cin >> t;

	while(t--) {
		int n; cin >> n;
		vector<int> entrada(n);
		vector<int> saida (n);
		for(int i = 0; i < n; i++) {
			int e, s; cin >> e >> s;
			entrada[i] = e;
			saida[i] = s;
		}

		int atual = 0;

		for(int i = 0; i < n; i++) {
			if(atual < entrada[i]) {
				atual = entrada[i];
				
			} 
			
			if(atual > saida[i]) {
				cout << 0 << " ";

			} else {
				cout << atual << " ";
				atual ++;
			}
		}

		cout << endl;
	}
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	solve();
	return 0;	
}

