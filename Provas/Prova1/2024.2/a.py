def buscaBinariaPrimeiroMaior(valor):
    ini = 0
    fim = n - 1
    resp = -1

    while fim >= ini:
        meio = (ini+fim) // 2
        if l[meio] > valor:
            resp = meio
            fim = meio - 1
        else:
            ini = meio +1

    return resp

n = int(input())
l = list(map(int, input().split()))
d = int(input())
l.sort()

for i in range(d):
    q = int(input())
    r = buscaBinariaPrimeiroMaior(q)

    if r == -1:
        print(n)
    else:
        print(r)
