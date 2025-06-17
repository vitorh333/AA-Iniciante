from collections import defaultdict
 
n, k = map(int, input().split())
l = list(map(int, input().split()))
 
mapa = defaultdict(list)
 
if k == 1:
    print("IMPOSSIBLE")
    exit()
for i in range(len(l)):
    mapa[l[i]].append(i)
 
l.sort()
j = n-1
i = 0
 
tem = False
while j > i:
    if l[j] + l[i] == k:
        tem = True
        i1 = mapa[l[i]][0]
        i2 = mapa[l[j]][-1]
        break
    elif l[j] + l[i] < k:
        i += 1
    else:
        j -= 1
if tem:
    print(f"{i1+1} {i2+1}")
 
else:
    print("IMPOSSIBLE")
