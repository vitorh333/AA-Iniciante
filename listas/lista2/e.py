
    resp = -1
    while fim >= ini:
        meio = (fim + ini) // 2

        if auxmax[meio] > num:
            resp = meio
            fim = meio - 1
        else:
            ini = meio + 1

    return resp

t = int(input())

for _ in range(t):
    n, q = map(int,input().split())
    deg = list(map(int, input().split()))
    cons = list(map(int, input().split()))
    
    prefixsum = [0] * n
    prefixsum[0] = deg[0]

    auxmax = [0] * n
    auxmax[0] = deg[0]



    for i in range(1,n):
        prefixsum[i] = prefixsum[i-1] + deg[i]
        auxmax[i] = max(auxmax[i-1], deg[i])
    
    resposta = []
    for c in cons:
        ind = buscaPrimeiroMaior(0, n-1, c)
        #print(ind)
        if ind == -1:
            resposta.append(prefixsum[n-1])
        elif ind == 0:
            resposta.append(0)
        else:
            resposta.append(prefixsum[ind-1])
    print(*resposta)
