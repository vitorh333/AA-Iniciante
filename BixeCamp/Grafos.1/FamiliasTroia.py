def dfs(grafo, no, visitados):
    visitados[no] = True

    for vizinho in grafo[no]:
        if not visitados[vizinho]:
            dfs(grafo, vizinho, visitados)


from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
grafo = defaultdict(list)

for i in range(m):
    v1, v2 = map(int, input().split())
    grafo[v1 - 1].append(v2 - 1)
    grafo[v2 - 1].append(v1 - 1)

visitados = [False] * n
cont = 0

for i in range(n):
    if not visitados[i]:
        cont += 1
        dfs(grafo, i, visitados)

print(cont)
