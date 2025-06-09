from collections import defaultdict

v, l = map(int, input().split())

mapa = defaultdict(set)

for i in range(l):
    v1, v2 = map(int, input().split())
    mapa[v1].add(v2)
    mapa[v2].add(v1)

q = int(input())
passeio = []

for i in range(q):
    p = list(map(int, input().split()))
    passeio.append(p)
cont = 0
for a in range(len(passeio)):
    pode = True
    for b in range(1, (len(passeio[a]) - 1)):
        if passeio[a][b+1] not in mapa[passeio[a][b]]:
            pode = False
            cont += 1
            break
print(q - cont)
