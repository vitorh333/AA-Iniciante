import math
import heapq
import sys
from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline
INF = 10**18 + 10


def sortComParametro(lista):
    lista.sort(key=lambda x: (x[0], x[1]))
    return lista

def exp_mod(b, e, mod):
    resp = 1
    b = b % mod

    while e > 0:
        if e % 2 == 1:
            resp = (resp * b) % mod
        b = (b * b) % mod
        e //= 2

    return resp

def bfs(grafo, verticie):
    visitados = set()
    fila = deque([verticie])
    visitados.add(verticie)

    while fila:
        atual = fila.popleft()
        print("visitando:", atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

def dijkstra(grafo, verticie):
    dist = [INF] * len(grafo)
    dist[verticie] = 0

    pai = [None] * len(grafo)


    fila = [(verticie, 0)]
    print(dist)

    while fila:
        atual, distAtual = heapq.heappop(fila)

        if distAtual < dist[atual]:
            continue

        for vizinho, d in grafo[atual]:
            if dist[vizinho] > dist[atual] + d:
                dist[vizinho] = dist[atual] + d
                pai[vizinho] = atual
                heapq.heappush(fila, (vizinho, dist[vizinho]))

    return dist, pai


