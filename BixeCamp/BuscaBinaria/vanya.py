n, r = map(int, input().split())
l = list(map(int, input().split()))

l.sort()

r1 = -1
r2 = -1
r3 = -1

print(l)

for i in range(n - 1):
    r3 = max(r3, abs(l[i] - l[i + 1]))


r3 /= 2
r1 = l[0]
r2 = abs(l[n-1] - r)

print(max(r1, r2, r3))

