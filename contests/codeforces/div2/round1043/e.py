t = int(input())

for _ in range(t):
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()

    resp = []

    for i in range(q):
        xa, yb, zt = map(int, input().split())

        ca = cb = ct = 0
        i = j = 0
        cont = 0

        while ct < zt:
            
            if ca < xa and a[i] > b[j]:
                cont += a[i]
                i += 1
                ca += 1
            else:
                cont += b[j]
                j += 1
                cb += 1
            
            ct += 1

        resp.append(cont)

    for i in range(q):
        print(resp[i])
