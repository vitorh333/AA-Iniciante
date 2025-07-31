n = int(input())
c = list(map(int, input().split()))

dist = -1

for i in range(1, n):
    if c[i] != c[0]:
        dist = max(dist, abs(i))
for j in range(len(c) - 2, -1, -1):
    if c[j] != c[n-1]:
        dist = max(dist, abs(n - 1 - j))

print(dist)
