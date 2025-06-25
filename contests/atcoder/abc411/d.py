#ESSA PORRA NAO PASSOU
#VER COMO OTIMIZAR


from collections import defaultdict
import sys

input = sys.stdin.readline

n, q = map(int, input().split())

pcs = defaultdict(list)
servidor = []

for _ in range(q):
    f = input().split()
    indx = int(f[1]) - 1

    if f[0] == "1":
        pcs[indx] = servidor.copy()

    elif f[0] == "2":
        pcs[indx].append(f[2])

    else:
        servidor = pcs[indx].copy()
sys.stdout.write(''.join(servidor) + '\n')

#COMEMORA, COMEMORA Q E GOL
