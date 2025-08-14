t = int(input())
cont = 0
 
for _ in range(t):
    a, k = map(str, input().split())
    if a == "P":
        cont += int(k)
    else:
        k = int(k)
        s = int(k)
        k -= min(k, cont)
        cont -= min(s, cont)
        #print(k)
        #print(cont)
        if k > 0:
            print("YES")
        else:
            print("NO")
