

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    aux1 = [0] * n
    aux2 = [0] * n

    tem = False

    for i in range(n-1):
        aux1[i] = l[i]
        aux2[i] = l[i]
        if abs(l[i] - l[i+1]) <= 1:
            tem = True

    aux1[-1] = l[-1]
    aux2[-1] = l[-1]

    if tem:
        print(0)
    elif n == 2:
        print(-1)
    else:
        aux1.sort()
        aux2.sort()
        aux2.reverse()

        if l == aux1 or l == aux2:
            print(-1)
        else:
            print(1)



