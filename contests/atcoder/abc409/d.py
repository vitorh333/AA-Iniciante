from collections import defaultdict

n, r = map(int, input().split())
d = list(map(int, input().split()))

# PUTA Q PARIU AS POSICOES ESTAO EM PREFIXSUM
# GABRIEL E UM GENIO

prefixsum = [0]
for dist in d:
    prefixsum.append((prefixsum[-1] + dist) % r)

freq = defaultdict(list)

for i, p in enumerate(prefixsum):
    freq[p].append(i + 1)

res = 0
if r % 3 == 0:
    passo = r // 3
    for p in freq:
        p1 = p
        p2 = (p + passo) % r
        p3 = (p + 2 * passo) % r
        if p2 in freq and p3 in freq:
            a = len(freq[p1])
            b = len(freq[p2])
            c = len(freq[p3])
            res += a * b * c

print(res//3)

