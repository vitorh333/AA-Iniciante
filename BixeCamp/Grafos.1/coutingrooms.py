import sys
input = sys.stdin.readline

n, m = map(int, input().split())

greed = [list(input().strip()) for _ in range(n)]

visitados = set()
cont = 0

def valid(i, j):
    return 0 <= i < n and 0 <= j < m and greed[i][j] != "#"

def dfs_iterativo(i, j):
    pilha = [(i, j)]
    while pilha:
        ci, cj = pilha.pop()
        if (ci, cj) in visitados:
            continue
        visitados.add((ci, cj))
        for ni, nj in [(ci, cj+1), (ci, cj-1), (ci+1, cj), (ci-1, cj)]:
            if valid(ni, nj) and (ni, nj) not in visitados:
                pilha.append((ni, nj))


for i in range(n):
    for j in range(m):
        if greed[i][j] == "." and (i, j) not in visitados:
            cont += 1
            dfs_iterativo(i, j)

print(cont)
