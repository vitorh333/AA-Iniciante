
    ini = 0
    fim = len(pk) - 1
    resp = 0

    while fim >= ini:
        meio = (fim+ini) // 2
        if pk[meio] > k:
            resp = meio
            fim = meio -1
        else:
            ini = meio +1

    return resp

def medo(k, primes):
    s = str(k)
    #if "0" in s:
        #return False

    fator = 10
    while k >= fator:
        trunc = k // fator
        if not primes[trunc]:
            return False
        fator *= 10

    return True

def solve(limit):
    crivo = [True] * (limit+1)
    crivo[0] = crivo[1] = False
    saida = []

    for i in range(2, int(limit**0.5)+1):
        if crivo[i]:
            for j in range(i*i, limit+1, i):
                crivo[j] = False

    for i in range(2, limit):
        if crivo[i] and medo(i, crivo):
            saida.append(i)

    return saida

t = int(input())
pk = solve(740400)

for _ in range(t):
    k = int(input())
    r = buscabinaria(k)

    if r == 0:
        print(len(pk))
    else:
        print(r)

