t = int(input())

for _ in range(t):
    a, x, y = map(int, input().split())

    l = min(x, y)
    r = max(x, y)

    if l <= a <= r:
        print("NO")
    else:
        print("YES")
