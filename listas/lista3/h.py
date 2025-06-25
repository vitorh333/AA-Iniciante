#Um aumento de x na riqueza do mais rico implica em um aumeto de x/total de pessoas na media
#posso chutar um aumento x a riqueza do maior, se mais da metade ja estao infelizes com mais aumento com certeza um numero maior ou igual ficarao infelizes

def buscaQtdInfelizes(r, target):
    ini = 0
    fim = n-1
    resp = -1

    while fim >= ini:
        meio = (ini + fim) // 2
        if r[meio] >= target:
            resp = meio
            fim = meio - 1
        else:
            ini = meio + 1

    return resp


t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))

    if n == 1 or n == 2:
        print(-1)
    else:
        r.sort()
        k = sum(r)

        maior = r[-1]
        metade = n // 2

        xmin = 0
        xmax = 10**15 + 10

        resp = 0

        while xmax >= xmin:

            meio = (xmax + xmin) // 2
            r[-1] = maior + meio
            media = ((k + meio)/n)
            #print(meio)
            #print(media)

            if(buscaQtdInfelizes(r, media / 2)) > metade:
                xmax = meio -1
                resp = meio
            else:
                xmin = meio + 1
        print(resp)
