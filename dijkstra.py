import sys
import heapq

input = sys.stdin.readline
INF = 10**18

def dijkstra(grafo, n, origem):
    dist = [INF] * n
    dist[origem] = 0
    caminho = [-1] * n
    caminho[origem] = origem

    fila = [(0, origem)]

    while fila:
        d, v = heapq.heappop(fila)
        if d != dist[v]:
            continue
        for vizinho, peso in grafo[v]:
            nd = d + peso
            if nd < dist[vizinho]:
                dist[vizinho] = nd
                caminho[vizinho] = v
                heapq.heappush(fila, (nd, vizinho))
    return dist, caminho


def main():
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        v1, v2, d = map(int, input().split())
        v1 -= 1
        v2 -= 1
        grafo[v1].append((v2, d))
        grafo[v2].append((v1, d))

    dist, caminho = dijkstra(grafo, n, 0)

    if caminho[n - 1] == -1:
        print(-1)
        return

    c = []
    atual = n - 1
    while atual != caminho[atual]:
        c.append(atual + 1)
        atual = caminho[atual]
    c.append(1)

    sys.stdout.write(" ".join(map(str, reversed(c))) + "\n")


if __name__ == "__main__":
    main()

