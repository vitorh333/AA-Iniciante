n , r = map(int, input().split())
d = list(map(int, input().split()))

#PUTA Q PARIU AS POSICOES ESTAO EM PREFIXSUM
#GABRIEL É UM GENIO

prefixsum = [0]
for i in range(len(d) - 1):
    prefixsum.append((prefixsum[-1] + d[i]) % r)

posicoes = set(prefixsum)

if r % 3 != 0:
    print(0)
else:
    passo = r // 3
    cont = 0
    for p in posicoes:
        if ((p + passo) % r) in posicoes and ((p + 2 * passo) % r) in posicoes:
            menor = min(p, (p + passo) % r, (p + 2 * passo) % r)
            if p == menor:
                cont += 1
    print(cont)


