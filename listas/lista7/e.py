from collections import deque

xini, yini, xfim, yfim = map(int, input().split())
n = int(input())
seg = []
for i in range(n):
    l, a, b = map(int, input().split())
    seg.append((l, a, b))

mapa = {}
segmentos = []
index = 0

for l, a, b in seg:
    for c in range(a, b + 1):
        if (l, c) not in mapa:
            segmentos.append((l, c))
            mapa[(l, c)] = index
            index += 1
#print(segmentos)
#print(mapa)

dist = [-1] * len(segmentos)
pai = [-1] * len(segmentos)
ini = mapa[(xini, yini)]
fim = mapa[(xfim, yfim)]
dist[ini] = 0
fila = deque([ini])

posx = [-1, -1, -1, 0, 0, 1, 1, 1]
posy = [1, -1, 0, 1, -1, 0, 1, -1]

while fila:
    u = fila.popleft()
    x, y, = segmentos[u]

    for i in range(8):
        xa, ya, = x + posx[i], y + posy[i]

        if(xa, ya) in mapa:
            if dist[mapa[(xa, ya)]] == -1:
                dist[mapa[(xa, ya)]] = dist[u] + 1
                pai[mapa[(xa, ya)]] = u
                fila.append(mapa[(xa, ya)])

print(dist[fim])




