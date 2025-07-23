t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    temPar = False
    contImpar = 0

    for i in range(len(a)):
        if a[i] % 2 == 0:
            temPar = True
        else:
            contImpar += 1

    if temPar:
        print(contImpar+1)
    else:
        print(contImpar-1)
