import math

def comb(n, k):
    if n < 2: return 0
    else:
        return math.factorial(n)/(math.factorial(k) * math.factorial(n-k))

n = int(input())
m = []

for i in range(n):
    l = input()
    aux = []
    for i in range(n):
        aux.append(l[i])
    m.append(aux)

geral = 0


for i in range(n):
    cont = 0
    for j in range(n):
        if m[i][j] == "C":
            cont += 1
    geral += comb(cont, 2)

j = 0
i = 0
cont = 0

while j < n:
    if m[i][j] == "C":
        cont += 1

    i += 1

    if i == n:
        i = 0
        j += 1
        geral += comb(cont, 2)
        cont = 0

print(int(geral))
