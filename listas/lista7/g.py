def bfs(grafo, no):
    seq = []
    fila = deque([no])
    visitados = {no}

    while fila:
        vez = fila.popleft()
        seq.append(vez)

        for vizinho in grafo[vez]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    return seq



from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n = int(input())
grafo = defaultdict(list)

for i in range(n):
    v1, v2 = map(int, input().split())
    grafo[v1].append(v2)
    grafo[v2].append(v1)

v = -1
menor = 10**8 + 10
for k in grafo:
    if len(grafo[k]) == 1:
        v = k
        break
caminho = bfs(grafo, v)
print(*caminho)
