from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))

soma = 0
cont = 0

mapa = defaultdict(int)
mapa[0] = 1

for i in range(n):
    soma += l[i]

    if soma - k in mapa:
        cont += mapa[soma -k]
    mapa[soma] += 1
sys.stdout.writelines(f"{cont}")
sys.stdout.writelines('\n')

