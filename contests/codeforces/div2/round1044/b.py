t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    resp = 0
    if n % 2 == 0:
        for i in range(0, n - 1, 2):
            resp += max(l[i], l[i + 1])

    else:
        for i in range(n-1, 1, -2):
            resp += max(l[i], l[i-1])
        resp += l[0]

    print(resp)
