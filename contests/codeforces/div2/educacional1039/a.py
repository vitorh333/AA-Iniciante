def buscaMaior(l, c):
    ini = 0
    fim = len(l) - 1
    r = -1

    while fim >= ini:
        meio = (ini + fim) // 2

        if l[meio] <= c:
            r = meio
            ini = meio + 1
        else:
            fim = meio - 1
    return r

def multiplica(l):
    for i in range(len(l)):
        l[i] *= 2

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    cont = 0

    while l:
        resp = buscaMaior(l, c)
        if resp != -1:
            l.pop(resp)
            multiplica(l)
        else:
            cont += len(l)
            break

    print(cont)

