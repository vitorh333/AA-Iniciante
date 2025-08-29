t = int(input())
 
for _ in range(t):
    n = int(input())
    a = input()
    k = int(input())
    s1 = input()
    o = input()
 
    aux = "" 
 
    for i in range(k):
        if o[i] == "V":
            aux += s1[i]
        else:
            a += s1[i]
 
    aux2 = ""
    for i in range(len(aux) - 1, -1, -1):
        aux2 += aux[i]
    print(aux2 + a)
 
