def chute(m):
    ini = 0
    fim = n - 1
    r = n

    while fim >= ini:
        meio = (ini + fim) // 2
        if q[meio] > m:
            r = meio
            fim = meio -1
        else:
            ini = meio + 1

    return (m * r) - prefixsum[r - 1]

t = int(input())

for _ in range(t):
    n, a = map(int, input().split())
    q = list(map(int, input().split()))
    q.sort()

    prefixsum = [q[0]] * n

    for i in range(1, n):
        prefixsum[i] = prefixsum[i-1] + q[i]

    fim = 10**10 + 10
    ini = 1
    resp = 0

    while fim >= ini:
        meio = (ini+fim) // 2

        if chute(meio) > a:
            fim = meio -1
        else:
            resp = meio
            ini = meio + 1
    print(resp)
