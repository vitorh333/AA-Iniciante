t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    resp = 0

    if n % 2 == 0: a.append(0)

    for i in range(1, n, 2):
        soma = a[i-1] + a[i + 1]

        if soma > a[i]:
            resp += soma - a[i]
            a[i + 1] -= min(a[i+1], soma - a[i])
    print(resp)
