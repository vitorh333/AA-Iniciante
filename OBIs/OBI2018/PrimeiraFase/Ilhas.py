def dijkstra(ini):
    dist = [INF] * n
    dist[ini] = 0

    heap = [(0, ini)]

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue

        for v, peso in grafo[u]:
            if peso != 0:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    heapq.heappush(heap, (dist[v], v))
    return dist

from collections import defaultdict
import heapq

INF = 10**9 + 10

n, m = map(int, input().split())

grafo = defaultdict(list)

for i in range(m):
    v1, v2, d = map(int, input().split())
    info1 = (v1-1,d)
    info2 = (v2-1, d)
    grafo[v1 - 1].append(info2)
    grafo[v2 - 1].append(info1)


ini = int(input())
k = dijkstra(ini - 1)
k.sort()
print(k[n - 1] - k[1])
