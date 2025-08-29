def pode(x, y):
    return max(x, y) <= 2 * min(x, y) + 2
 
t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if pode(a, b) and pode(c - a, d - b):
        print("YES")
    else:
        print("NO")
