def find(x):
    if pai[x] != x:
         pai[x] = find(pai[x])

    return pai[x]

def union(x, y):
    paix = find(x)
    paiy = find(y)

    if tamanho[paiy] > tamanho[paix]:
        paix, paiy = paiy, paix

    tamanho[paix] += tamanho[paiy]
    pai[paiy] = paix

import sys
sys.setrecursionlimit(10 ** 6)
n, q = map(int, input().split())
pai = [-1] * n
tamanho = [1] * n

for i in range(n):
    pai[i] = i

for i in range(q):
    k, v1, v2 = map(int, input().split())

    if k == 0:
        union(v1, v2)
    else:
        if find(v1) == find(v2):
            print(1)
        else:
            print(0)

