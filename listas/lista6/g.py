import math

t = int(input())
mod = 998244353

for _ in range(t):
    n = int(input())

    if n % 2 == 1:
        print(0)

    else:
        print(math.factorial(n // 2) ** 2 % mod)
