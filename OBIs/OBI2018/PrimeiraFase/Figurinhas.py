n, c, m = map(int, input().split())
carimbadas = list(map(int, input().split()))
compradas = list(map(int, input().split()))
    
compradas = set(compradas)
cont = 0
for i in range(len(carimbadas)):
    if carimbadas[i] not in compradas:
        cont += 1
print(cont)
