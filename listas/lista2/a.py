n, q = map(int, input().split())
l = list(map(int, input().split()))

prefixsum = [0] * n
prefixsum[0] = l[0]

for i in range(1, n):
    prefixsum[i] = prefixsum[i-1] + l[i]

for i in range(q):
    l, r = map(int, input().split())

    if l == 1:
        print(prefixsum[r-1])
    else:
        print(prefixsum[r-1] - prefixsum[l-2])
