import sys

input = sys.stdin.readline

n, l, h = map(int, input().split())
nums = list(map(int, input().split()))
marc = list(map(int, input().split()))

prefixsum = [0] * (n + 1)
prefixmarc = [0] * (n + 1)

for i in range(n):
    prefixsum[i+1] = prefixsum[i] + nums[i]
    prefixmarc[i+1] = prefixmarc[i] + marc[i]

maior = - (10**18)

for i in range(n):
    for j in range(i+1, n+1):
        qtdmarcados = prefixmarc[j] - prefixmarc[i]
        if l <= qtdmarcados <= h:
            somaatual = prefixsum[j] - prefixsum[i]
            maior = max(maior, somaatual)

print(maior)

