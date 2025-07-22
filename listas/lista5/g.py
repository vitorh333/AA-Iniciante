import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = 2 * n

    for d in range(2, 1001):
        usados = [False] * total
        pares = []

        for i in range(total):
            if usados[i]:
                continue
            for j in range(i + 1, total):
                if not usados[j] and (a[i] + a[j]) % d == 0:
                    usados[i] = usados[j] = True
                    pares.append((i + 1, j + 1))
                    break

        if len(pares) >= n - 1:
            for i in range(n - 1):
                print(pares[i][0], pares[i][1])
            break

