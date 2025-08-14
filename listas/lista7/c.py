def dfs(no, total):
    if g[no - 1] == 1:
        total += 1
    else:
        total = 0

    if total > v:
        return 0

    if not grafo[no]:
        return 1

    s = 0

    for vizinhos in grafo[i]:
        s += dfs(vizinho, total)


    return s

from collections import defaultdict

n, v = map(int, input().split())
g = list(map(int, input().split()))

grafo = defaultdict(list)

for i in range(n - 1):
    v1, v2 = map(int, input().split())
    grafo[v1].append(v2)

print(dfs(1, 1))

print(grafo)
