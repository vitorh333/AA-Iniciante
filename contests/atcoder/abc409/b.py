t = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)

res = 0
for i in range(t):
    if l[i] >= i + 1:
        res = i + 1
print(res)

