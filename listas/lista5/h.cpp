
using namespace std;
#define endl '\n'


int euclides(int a, int b) {
	if (b > a) swap(a, b);

	while(b != 0) {
		int resto = a% b;
		a = b;
		b = resto;
	}

	return a;

}


void solve() {
	int k; cin >> k;
	int maior = 1;
	int resp = 1;

	for(int i = 1; i < k; i++) {
		int mdc = euclides(k, i);
		if(mdc + i > maior) {
			maior = mdc + i;
			resp = i;
		}
	}

	cout << resp << endl;
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	int n; cin >> n;
	while(n--) {
		solve();
	}
    return 0;
}


