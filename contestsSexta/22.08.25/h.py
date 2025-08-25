import math

n, a, b, p, q = map(int, input().split())

k = a * b // math.gcd(a, b)

ini, fim = 0, n
ca = 0

while fim >= ini:
    meio = (ini + fim) // 2
    if meio * a <= n:
        ca = meio * a
        ini = meio + 1
    else:
        fim = meio - 1

ca = ca // a

ini, fim = 0, n
cb = 0

while fim >= ini:
    meio = (ini + fim) // 2
    if meio * b <= n:
        cb = meio * b
        ini = meio + 1
    else:
        fim = meio - 1

cb = cb // b

ini, fim = 0, n
ck = 0

while fim >= ini:
    meio = (ini + fim) // 2
    if meio * k <= n:
        ck = meio * k
        ini = meio + 1
    else:
        fim = meio - 1

ck = ck // k

ca -= ck
cb -= ck

r1 = ca * p
r2 = cb * q
r3 = ck * max(p, q)

print(r1 + r2 + r3)
