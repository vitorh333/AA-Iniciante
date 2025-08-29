t = int(input())
 
for _ in range(t):
    n = int(input())
    resp = []
    cont = 0
    k = 1
 
    while n >= 10 ** k + 1:
        if (n % (1 + 10 ** k)) == 0:
            resp.append(int(n // (1 + 10 ** k)))
            cont += 1
        k += 1
 
    print(cont)
    
    if cont != 0:
        resp.sort()
        print(*resp)
