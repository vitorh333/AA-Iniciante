n, q = map(int, input().split())
lista = list(map(int, input().split()))

qtduns = lista.count(1)

for i in range(q):
    t, ax = map(int, input().split())

    if t == 1:
        if lista[ax-1] == 1:
            qtduns -= 1
        else:
            qtduns += 1
        lista[ax-1] = 1 - lista[ax-1]
    else:
        if qtduns >= ax:
            print(1)
        else:
            print(0)
