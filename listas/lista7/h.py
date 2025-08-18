def bfs(grafo, no):
    seq = []
    fila = deque([no])
    visitados = {no}

    while fila:
        vez = fila.popleft()
        seq.append(vez)
        for vizinho in grafo[vez]:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)

    return seq



from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n = int(input())

grafo = defaultdict(list)

for i in range(n -1):
    v1, v2 = map(int, input().split())
    grafo[v1].append(v2)
    grafo[v2].append(v1)

seq = list(map(int, input().split()))


pos = [0] * (n+1)
for i, v in enumerate(seq):
    pos[v] = i

for i in range(1, n+1):
    grafo[i].sort(key=lambda x: pos[x])

aux = bfs(grafo, 1)

if aux == seq:
    print("YES")
else:
    print("NO")

