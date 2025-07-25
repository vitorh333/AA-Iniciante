t  = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    f = list(map(int, input().split()))

    f.sort()
    flag = True
    cont = n

    for i in range(n):
        if f[cont] - f[i] < k:
            flag = False
        cont += 1
    if flag:
        print("YES")
    else:
        print("NO")


