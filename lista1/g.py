n, q = map(int, input().split())
s = input()

pk = ["A"] * n
cont = 0

for i in range(len(s) - 2):
    if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
        cont += 1
    pk[i] = s[i]

pk[-1] = s[-1]
pk[-2] = s[-2]

for i in range(q):
    xi, l = map(str, input().split())
    xi = int(xi) - 1

    #somente 3 strings importam
    #analisar a difrenca antes e depois

    for t in range(3):
        k = xi - t
        if k < n - 2 and k >= 0:
            if pk[k] == "A" and pk[k+1] == "B" and pk[k+2] == "C":
                cont -= 1

    pk[xi] = l

    for t in range(3):
        k = xi - t
        if k < n - 2  and k >= 0:
            if pk[k] == "A" and pk[k+1] == "B" and pk[k+2] == "C":
                cont += 1

    print(cont)
        











