def encontraPrimeiroMaior(k, ini, fim, num):
    resp = -1
    while fim >= ini:
        meio = (ini+fim)//2
        if k[meio] >= num:
            resp = meio
            fim = meio - 1
        else:
            ini = meio + 1
    return resp

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# ai + aj > bi + bj
# ai - bi > bj - aj

aux = []

for i in range(len(a)):
    aux.append(a[i] - b[i])

aux.sort()
cont = 0

for i in range(len(aux)):
    if aux[i] > 0:
        pos = encontraPrimeiroMaior(aux, 0, n-1, -aux[i] + 1)
        cont += i -pos
print(cont)
#print(aux)
