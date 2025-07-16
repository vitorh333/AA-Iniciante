import sys

def preprocessa(limit):
    saida = [0] * (limit+1)
    cont = 0
    crivo = [True] * (limit + 1)
    crivo[0] = crivo[1] = False

    for i in range(2, limit+1):
        if crivo[i]:
            for j in range(i+i, limit+1, i):
                crivo[j] = False
            if confere(i, crivo):
                cont += 1

        saida[i] = cont
    return saida

def confere(s, l):
    p = str(s)

    if "0" in p:
        return False

    for i in range(len(p)):
        num = int(p[i:])
        if not l[num]:
            return False

    return True


s = preprocessa(10**6)
t = int(sys.stdin.readline())

for i in range(t):
    k = int(sys.stdin.readline())
    sys.stdout.write(f"{s[k]}")
    sys.stdout.write('\n')
