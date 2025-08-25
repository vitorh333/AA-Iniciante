n, k = map(int, input().split())
g = list(map(int, input().split()))
b = input()

i = 0

while i < n:
    j = i
    while j < n and b[j] == b[i]:
        j += 1
    g[i:j] = sorted(g[i:j], reverse=True)
    i = j

atual = ""
cont = 0
resp = 0

for i in range(n):
    #print(atual)
    #print(resp)
    if b[i] == atual:
        if cont < k:
            cont += 1
            resp += g[i]
    else:
        atual = b[i]
        cont = 1
        resp += g[i]

print(resp)
