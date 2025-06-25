from collections import defaultdict

n, target = map(int, input().split())
lista = list(map(int, input().split()))
    
cont = 0
soma_acumulada = 0
somas_vistas = defaultdict(int)
somas_vistas[0] = 1
    
for num in lista:
    soma_acumulada += num
    
    if soma_acumulada - target in somas_vistas:
        cont += somas_vistas[soma_acumulada - target]
    
    somas_vistas[soma_acumulada] += 1
    
print(cont)
