import sys
from collections import deque

input = sys.stdin.readline

MOVS = [(1, 0, "D"), (-1, 0, "U"), (0, -1, "L"), (0, 1, "R")]

def bfs(grafo, start, end, n, m):
    fila = deque([start])
    visitados = [[False] * m for _ in range(n)]
    anterior = [[None] * m for _ in range(n)]
    passo = [[None] * m for _ in range(n)]

    si, sj = start
    visitados[si][sj] = True

    while fila:
        i, j = fila.popleft()
        if (i, j) == end:
            caminho = []
            while (i, j) != start:
                caminho.append(passo[i][j])
                i, j = anterior[i][j]
            caminho.reverse()
            return "".join(caminho)

        for di, dj, letra in MOVS:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not visitados[ni][nj] and grafo[ni][nj] != "#":
                visitados[ni][nj] = True
                anterior[ni][nj] = (i, j)
                passo[ni][nj] = letra
                fila.append((ni, nj))

    return None


# -------------------------
n, m = map(int, input().split())
grafo = [list(input().strip()) for _ in range(n)]

start = end = None
for i in range(n):
    for j in range(m):
        if grafo[i][j] == "A":
            start = (i, j)
        if grafo[i][j] == "B":
            end = (i, j)

caminho = bfs(grafo, start, end, n, m)

if caminho:
    sys.stdout.write("YES\n")
    sys.stdout.write(str(len(caminho)) + "\n")
    sys.stdout.write(caminho + "\n")
else:
    sys.stdout.write("NO\n")

