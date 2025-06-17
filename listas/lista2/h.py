n, k = map(int, input().split())
l = list(map(int, input().split()))

prefixsum = [0] * n
prefixsum[0] = l[0]

for i in range(1, n):
    prefixsum[i] = prefixsum[i-1] + l[i]

if k == n:
    print(1)
else:
    i = 0
    j = k-1
    minimo = prefixsum[j]
    indi = 1

    while n-1 > j:
        #print(prefixsum[j+1] - prefixsum[i])
        if (prefixsum[j+1] - prefixsum[i] < minimo):
            minimo = prefixsum[j+1] - prefixsum[i]
            indi = i + 2
        i += 1
        j += 1
    print(indi)

    
