q = int(input())
l = []
    
a = int(input())
b = int(input())
c = int(input())
    
l.append(a)
l.append(b)
l.append(c)
    
l.sort()
    
i = 0
cont = 0
    
while l and q >= l[i]:
    q -= l[i]
    cont += 1
    l.pop(0)
print(cont)

