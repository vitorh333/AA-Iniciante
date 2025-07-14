#include <bits/stdc++.h>
using namespace std;
#define endl '\n'


bool isPrime(int k) {

	if(k == 1) return false;
	if(k == 2) return true;
	if(k % 2 == 0) return false;

	int target = (int) sqrt(k) + 1;

	for(int i = 3; i <= target; i+=2) {
		if(k % i == 0) return false;
	}

	return true;
}

void solve() {
	int n; cin >> n;
	int geral = 0;

	for(int i = 1; i <= n; i++) {
		int cont = 0;
		for(int j = 1; j <= i; j++) {
			if(i % j == 0 && isPrime(j)) {
				cont++;
			}

			if(cont > 2) break;
		}

		if(cont == 2) geral++;
	}

	cout << geral << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	solve();
    
    return 0;
}


