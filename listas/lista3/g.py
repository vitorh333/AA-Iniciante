import sys


def buscaPrimeiroMaior(a, target):
    ini = 0
    fim = len(a) -1
    resp = len(a)

    while fim >= ini:
        meio = (ini+fim) // 2
        if a[meio] > target:
            resp = meio
            fim = meio - 1
        else:
            ini = meio + 1
    return resp

n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

for i in range(len(b)):
    if i != len(b) - 1:
        sys.stdout.writelines(f"{buscaPrimeiroMaior(a, b[i])} ")
    else:
        sys.stdout.writelines(f"{buscaPrimeiroMaior(a, b[i])}")
print()

