def pegaMaior(k):
    maior = 0

    for i in range(k):
        maior = max(maior, c[i])


    return maior

t =  int(input())

for _ in range(t):
    n = int(input())
    c  = list(map(int, input().split()))
    cont = 0
    i = 0

    while i < len(c):
        if c[i] == 0:
            target = pegaMaior(i)
            #print(target)
            if target != 0:
                cont += target
                c.remove(target)
            else:
                i += 1
        else:
            i += 1

    print(cont)
