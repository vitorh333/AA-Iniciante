t, q = map(int, input().split())
sa = list(map(int, input().split()))
sb = list(map(int, input().split()))
    
i = j = 0
cont = 0
    
while i < q and j < t:
    #print(f"{sb[i]} {sa[j]}")
    if sb[i] == sa[j]:
        cont += 1
        i += 1
    if cont == q:
        break
    j += 1
    
    
    
if cont == q:
    print("S")
else:
    print("N")
