def calculapot(x):
    return (3 ** (x + 1)) + (x * (3 ** (x -1)))
 
 
pot = []
 
for i in range(30, -1, -1):
    pot.append(3 ** i)
 
#print(pot)
 
t = int(input())
 
for _ in range(t):
    
    n = int(input())
    k = 0
    cont = 0
    while n > 0:
        if pot[k] <= n:
            n -= pot[k]
            #print(30 - k)
            cont += int(calculapot(30 - k))
        else:
            k += 1
    print(cont)
 
