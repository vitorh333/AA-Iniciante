#Thais deve sempre tirar o maior numero dentre os q ela pode tirar
#Davi pode pegar sempre o menor numero e fazer com q ele nunca mais possa ser tirado
#Posso tentar chutar um numero k qualquer e simular o comportamento dojogo


def procuraUltimoMenorIgual(v, target):
    ini = 0
    fim = len(v) - 1
    r = -1
    while ini <= fim:
        meio = (ini + fim) // 2
        if v[meio] <= target:
            r = meio
            ini = meio + 1
        else:
            fim = meio - 1
    return r

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    resp = 0

    for k in range(1, n + 1):
        v = list(a)
        ganhou = True
        for i in range(k):
            target = k - i
            pos = procuraUltimoMenorIgual(v, target)
            if pos == -1:
                ganhou = False
                break
            v.pop(pos)
            if v:
                #somar pode trocar a ordem da lista, tenho q sortar denovo
                v[0] += target
                v.sort()
        if ganhou and len(v) + k == n:
            resp = k
    print(resp)


