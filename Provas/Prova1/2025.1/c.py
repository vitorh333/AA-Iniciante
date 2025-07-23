def buscaPrimeiroMaior(k):
    ini = 0
    fim = n-1
    resp = -1

    while fim >= ini:
        meio = (ini + fim) // 2
        if c[meio] > k:
            resp = meio
            fim = meio - 1
        else:
            ini = meio + 1

    return resp

n = int(input())
c = list(map(int, input().split()))
q = int(input())
c.sort()
for i in range(q):

    s = int(input())
    r = buscaPrimeiroMaior(s)

    if r == -1:
        print(n)
    else:
        print(r)
