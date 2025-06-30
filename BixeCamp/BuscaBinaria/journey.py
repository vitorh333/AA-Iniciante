def chute(m):
    vz = m // 3
    k = m % 3
    r = (a + b + c) * vz

    if k == 1:
        r += a
    elif k == 2:
        r += b + a

    return r


t = int(input())

for _ in range(t):

    n, a, b, c = map(int, input().split())

    ini = 0
    fim = 10**10 + 10
    resp = 0

    while fim >= ini:
        dia = (ini+fim) // 2
        if chute(dia) >= n:
            resp = dia
            fim = dia - 1
        else:
            ini = dia + 1

    print(resp)
