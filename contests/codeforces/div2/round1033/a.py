t = int(input())
 
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    lados = [(l1, b1), (l2, b2), (l3, b3)]
    lado = max(l1, b1, l2, b2, l3, b3)
    ok = False
 
    for x in range(6):
        
        if x == 0:
            i1, i2, i3 = 0, 1, 2
        elif x == 1:
            i1, i2, i3 = 0, 2, 1
        elif x == 2:
            i1, i2, i3 = 1, 0, 2
        elif x == 3:
            i1, i2, i3 = 1, 2, 0
        elif x == 4:
            i1, i2, i3 = 2, 0, 1
        else: 
            i1, i2, i3 = 2, 1, 0
 
        x1, y1 = lados[i1]
        x2, y2 = lados[i2]
        x3, y3 = lados[i3]
 
        if x1 == x2 == x3 == lado and y1 + y2 + y3 == lado:
            ok = True
 
        if y1 == y2 == y3 == lado and x1 + x2 + x3 == lado:
            ok = True
 
        if x1 + x2 == lado and y1 == y2 and x3 == lado and y1 + y3 == lado:
            ok = True
 
        if y1 + y2 == lado and x1 == x2 and y3 == lado and x1 + x3 == lado:
            ok = True
 
    if ok:
        print("YES")
    else:
        print("NO")
