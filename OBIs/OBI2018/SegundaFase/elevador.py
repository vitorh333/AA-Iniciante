def verificaSePodeSubir(peso, cima):
    for i in range(9):
        p1 = peso - i
        p2 = peso + i

        if p1 in cima or p2 in cima:
            return True

    return False



n = int(input())
p = list(map(int, input().split()))

p.sort()

pode = True
cima = set()

for peso in p:
    if peso <= 8:
        cima.add(peso)
    else:
        if verificaSePodeSubir(peso, cima):
            cima.add(peso)
        else:
            pode = False
            break

if pode:
    print("S")
else:
    print("N")

