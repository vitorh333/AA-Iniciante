import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    aux = 2

    while math.gcd(k, aux) > 1:
        aux += 1

    for i in range(n):
        while a[i] % aux != 0:
            a[i] += k

    print(*a)

