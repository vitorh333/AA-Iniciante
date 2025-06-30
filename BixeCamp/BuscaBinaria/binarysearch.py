import sys

def buscaBinaria(a, target):
    ini = 0
    fim = len(a) - 1
    resp = -1

    while fim >= ini:
        meio = (ini + fim) // 2
        if a[meio] == target:
            resp = meio
            fim = meio - 1
        elif a[meio] > target:
            fim = meio - 1
        else:
            ini = meio + 1
    return resp

input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

respostas = []
for _ in range(q):
    num = int(input())
    respostas.append(buscaBinaria(a, num))

sys.stdout.write('\n'.join(map(str, respostas)) + '\n')
#SE NAO PASSAR AGORA EU VOU DORMIR HEIN CARA

