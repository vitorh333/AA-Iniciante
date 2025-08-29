import sys
sys.setrecursionlimit(10 ** 6)

def find(x):
    if pai[x] != x:
        pai[x] = find(pai[x])

    return pai[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if tamanho[py] > tamanho[px]:
        px, py = py, px

    tamanho[px] += tamanho[py]
    pai[py] = px

t = int(input())

for _ in range(t):
    n = int(input())
    pai = [-1] * (2 * (n+1))
    tamanho = [0] * (2 * (n + 1))

    for i in range(2 * (n + 1)):
        pai[i] = i
    
    aux = []

    for i in range(n):
        a, b = map(int, input().split())
        aux.append((a, b, i+1))

    resp = []

    for i in range(n):
        if find(aux[i][0]) != find(aux[i][1]):
            union(aux[i][0], aux[i][1])
            resp.append(aux[i][2])

    print(len(resp))
    print(*resp)
