t = int(input())

d = set()

for i in range(t):
    n = input()
    if n in d:
        print("YES")
    else:
        d.add(n)
        print("NO")

