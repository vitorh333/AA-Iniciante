t = int(input())
MOD = 1e9 + 7

for _ in range(t):
    n, k = map(int, input().split())
    resp = 1
    for i in range(k):
        resp = (n * resp) % MOD

    print(int(resp))

