def dist(ini):
    dist = [INF] * n
    dist[ini] = 0
    pai = [-1] * n

    fila = [(0, ini)]

    while fila:
        d, no = heapq.heappop(fila)

        if d > dist[no]:
            continue

        for v, d1 in grafo[no]:
            if dist[v] != 0:
                if dist[no] + d1 < dist[v]:
                    dist[v] = dist[no] + d1
                    pai[v] = no
                    heapq.heappush(fila, (dist[v], v))
    return dist, pai


from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline
INF = 10**9

n, m = map(int, input().split())
grafo = defaultdict(list)

for i in range(m):
    v1, v2 = map(int, input().split())
    info1 = (v1 -1, 1)
    info2 = (v2 - 1, 1)

    grafo[v1-1].append(info2)
    grafo[v2 - 1].append(info1)

k, pai = dist(0)

if k[n-1] >= INF:
    print("IMPOSSIBLE")
else:

    s = pai[n -1]
    resp = [n]

    while s != 0:
        resp.append(s+1)
        s = pai[s]

    resp.append(1)
    sys.stdout.writelines(f"{len(resp)} \n")
    for i in range(len(resp) -1, -1, -1):
        sys.stdout.writelines(f"{resp[i]} ")
    print()
