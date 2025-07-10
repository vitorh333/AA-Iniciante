#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void buscaBinaria(f, l) {
	int ini = 0;
	int fim = f.length -1;
	resp = -1;

	while(fim >= ini) {
		int meio = (ini + fim) / 2;
		if(f[meio] > l) {
			ini = meio + 1;
			resp = meio;
		} else {
			fim = ini -1
		}
	}
}

void solve() {
	int l, r, t; cin >> l >> r >> t;
	int n; cin >> n;
	vector<int> f (n);

	for(int i = 0; i < n; i++) {
		cin >> f[i];
	}

	int qtd = buscaBinaria(vector<int> f, int l);
	int best = -1;

	if(qtd == -1) {
		best = l;
	}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	solve();

    
    return 0;
}


