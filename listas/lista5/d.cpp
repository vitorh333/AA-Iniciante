#include <bits/stdc++.h>
using namespace std;
#define endl '\n'


bool is_prime(int k) {
	if(k < 2) return false;
	if(k == 2) return true;
	if(k % 2 == 0) return false;

	int target = (int) sqrt(k) + 1;

	for(int i = 3; i < target; i+=2) {
		if(k % i == 0) return false;
	}

	return true;
}


vector<int> solve(int limit) {

	vector<int> aux;

	for(int x = 1; x * x <= limit; x++){
		for(int j = 1; j * j * j * j <= limit; j++) {
			int soma = (j*j*j*j) + (x*x);
			if(is_prime(soma)) {
				aux.push_back(soma);
			}
		}
	}

	// ISSO SO SORTA MESMO, NAO TEM NUMERO REPETIDO NAO NE IMBECIL
	sort(aux.begin(), aux.end());
	auto it = unique(aux.begin(), aux.end());
    aux.erase(it, aux.end());

	return aux;
}


int buscaBinaria(int k, vector<int> p) {
	int ini = 0;
	int fim = p.size() - 1;
	int resp = -1;
	while(fim >= ini) {
		int meio = (ini+fim)/2;

		if(p[meio] > k) {
			resp = meio;
			fim = meio - 1;
		} else {
			ini = meio + 1;
		}
	}

	return resp;
}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	vector<int> aux = solve(10000000);	
	int n; cin >> n;
	while(n--) {
		int k; cin >> k;
		cout << buscaBinaria(k, aux) << endl;
	}

    return 0;
}


