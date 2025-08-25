t = int(input())

for _ in range(t):
    n = int(input())
    e = list(map(int, input().split()))
    v = set()
    achei = False

    for i in range(n):
        if e[i] not in v:
            v.add(e[i])
        else:
            achei = True
            break
    if achei:
        print("Yes")
    else:
        print("No")

