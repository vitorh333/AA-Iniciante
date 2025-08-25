def djistkra(grafo, v1):
    dist = [INF] * n
    dist[v1] = 0

    fila = [(v1, 0)]

    while fila:
        v, d = heapq.heappop(fila)

        if d > dist[v]:
            continue

        for vizinho, d1 in grafo[v]:
            if dist[vizinho] > dist[v] + d1:
                dist[vizinho] = dist[v] + d1
                heapq.heappush(fila, (vizinho, dist[vizinho]))
    return dist

from collections import defaultdict
import heapq

INF = 10**9

n, a, b = map(int, input().split())

grafo = defaultdict(list)

for i in range(n - 1):
    v1, v2, d = map(int, input().split())
    grafo[v1-1].append((v2 - 1, d))
    grafo[v2-1].append((v1 - 1, d))

dist = djistkra(grafo, a -1)
print(dist[b-1])



