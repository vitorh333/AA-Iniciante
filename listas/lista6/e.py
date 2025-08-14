MOD = 10**9 + 7

def expRapida(base, expoente):
    res = 1
    base = base % MOD

    while expoente > 0:
        if expoente % 2 == 1:
            res = (res * base) % MOD
        base = (base * base) % MOD
        expoente //= 2

    return res

n = int(input())

ni = list(map(int, input().split()))
ki = list(map(int, input().split()))

for i in range(len(ki)):
    print(expRapida(2, ki[i]))


