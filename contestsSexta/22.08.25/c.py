n, m = map(int, input().split())

if n == m:
    print(-1)
else:
    resp = []

    for i in range(1, n + 1):
        resp.append(i)

    for i in range(n-1 -m):
        resp[i], resp[i+1] = resp[i+1], resp[i]

    print(*resp)



