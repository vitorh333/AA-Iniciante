#CE TA MEDINO EU FILHO??
#QUER Q EU TE ESTRANHE AQUI BACANA?

from collections import defaultdict
import sys



t = int(input())

for _ in range(t):
    n, x, y = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))

    freq = defaultdict(int)

    cont = 0

    #OS MODULOSY TEM Q SER IGUAIS
    #SO PROCURO O TARGET

    for i in range(n):
        modx = l[i] % x
        mody = l[i] % y

        target = (x - modx) % x

        cont += freq[(target, mody)]

        freq[(modx, mody)] += 1

    print(cont)

