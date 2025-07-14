#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    const int limit = 100000000;
    vector<bool> is_prime(limit + 1, true);

    is_prime[0] = false;
    is_prime[1] = false;

    for (int i = 2; i * i <= limit; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                is_prime[j] = false;
            }
        }
    }

    int count = 0;
    for (int i = 2; i < limit; i++) {
        if (is_prime[i]) {
            count++;
            if (count % 100 == 1) {
                cout << i << '\n';
            }
        }
    }

    return 0;
}

