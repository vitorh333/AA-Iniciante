#Posso chutar um numero de dias arbitrario
#Se for possivel fazer com esse chute, com certeza e possivel fazer com mais
#Vou voltando ate encontrar o menor possivel

n, t = map(int, input().split())
maquinas = list(map(int, input().split()))

ini = 1
fim = 10**18 + 100

resp = 1

while fim >= ini:
    meio = (fim+ini)// 2
    total = 0

    for maq in maquinas:
        total += meio//maq

    if total >= t:
        fim = meio -1
        resp = meio
    else:
        ini = meio +1
print(resp)


