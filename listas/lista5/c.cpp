#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

bool contaSubdivisoes(int k, const vector<bool>& primes) {
    int fator = 10;

    while (fator <= k) {
		int t = k / fator;

        if (!primes[t]) {
            return false;
        }
        fator *= 10;
    }
    return true;
}

vector<int> solve(int limit) {
    vector<bool> primes(limit + 1, true);
    primes[0] = primes[1] = false;

    for (int i = 2; i * i <= limit; i++) {
        if (primes[i]) {
            for (int j = i * i; j <= limit; j += i) {
                primes[j] = false;
            }
        }
    }

    vector<int> aux;
    for (int i = 2; i <= limit; i++) {
        if (primes[i] && contaSubdivisoes(i, primes)) {
            aux.push_back(i);
        }
    }
    return aux;
}


// HAHAHHA A BUSCA BINARIA TAVA ERRADA HAHAHHAHAHAHAHHAHAH

int buscaBinaria(int k, const vector<int>& aux) {
    int ini = 0; 
	int fim = aux.size() - 1;
    int resp = -1;

    while (fim >= ini) {
        int meio = (ini + fim) / 2;
        if (aux[meio] <= k) {
            resp = meio;
            ini = meio +1;
        } else {
            fim = meio - 1;
        }
    }
    return resp + 1;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    vector<int> aux = solve(1000000 + 100);
    int n;
    cin >> n;
    while (n--) {
        int k;
        cin >> k;
        cout << buscaBinaria(k, aux) << endl;
    }
    return 0;
}

