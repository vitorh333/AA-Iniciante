matriz = []

for i in range(5):
    l = list(map(int, input().split()))
    matriz.append(l)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            linha = i
            coluna = j
print(abs(2 - linha) + abs(2 - coluna))
