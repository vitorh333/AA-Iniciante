
using namespace std;
#define endl '\n'


int euclides(int a, int b) {
	if (b > a) swap(a, b);
	while(b != 0) {
		int resto = a % b;
		a = b;
		b = resto;
	}

	return a;
}


void solve() {
	int n; cin >> n;
	vector<int> nums(n);

	for(int i = 0; i < n; i++) {
		cin >> nums[i];
	}

	int mdc = nums[0];

	for(int i = 1; i < n; i++) {
		mdc = euclides(mdc, nums[i]);
	}

	int cont = 0;

	// HAHAHAHHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHHAHAHAHAHHAHAHAHAHAHAHHAHA

	for(int i = 1; i * i <= mdc; i++) {
		if(mdc % i == 0) {
			if(i * i == mdc) {
				cont++;
			} else {
				cont += 2;
			}
		}
	}

	cout << cont<< endl;
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	solve();
    return 0;
}


