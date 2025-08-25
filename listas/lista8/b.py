def find(x):
    if pai[x] != x:
        pai[x] = find(pai[x])
    return pai[x]

def union(x, y):
    paix = find(x)
    paiy = find(y)

    pai[paiy] = pai[paix]

import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

pai = [0] * (n + 1)

for i in range(1, n + 1):
    pai[i] = i

resp = []

for i in range(n-1):
    v, u = map(int, input().split())

    if find(v) != find(u):
        union(v, u)
    else:
        resp.append((v, u))

for x in range(1, n):
    if find(pai[x]) != find(pai[x + 1]):
        union(x, x+1)
        resp.append((x, x + 1))
#print(pai)
#print(resp)

if len(resp) > 0:
    print(len(resp) // 2)
    ini = 0
    fim = len(resp) - 1

    while fim >= ini:
        sys.stdout.writelines(f"{resp[ini][0]} {resp[ini][1]} {resp[fim][0]} {resp[fim][1]} ")
        ini += 1
        fim -= 1
        print()
else:
    print(0)


