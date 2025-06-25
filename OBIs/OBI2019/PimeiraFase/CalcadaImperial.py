def simulalista(n1, n2):
    lista = []
    for i in range(len(calcada)):
        if calcada[i] == n1 or calcada[i] == n2 and calcada[i]:
            if len(lista) == 0:
                lista.append(calcada[i])
            else:
                if lista[-1] != calcada[i]:
                    lista.append(calcada[i])
                else:
                    continue
    return len(lista)

n = int(input())
calcada = [0] * n
for i in range(n):
    calcada[i] = int(input())
cont = 1
visitadosprincipal = set()
#teste = 0
    
for i in range(len(calcada)):
    visitados = set()
    visitados.add(calcada[i])
    if calcada[i] not in visitadosprincipal:
        visitadosprincipal.add(calcada[i])
        for j in range(len(calcada)):
            if calcada[j] not in visitados:
                cont = max(cont, simulalista(calcada[i], calcada[j]))
                visitados.add(calcada[j])
                #teste += 1
            else:
                continue
    else:
        continue
    #print(teste)
print(cont)

