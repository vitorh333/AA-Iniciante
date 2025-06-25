t = int(input())
 
for _ in range(t):
    n, s = map(int, input().split())
    cont = 0
    for i in range(n):
        dx, dy, xi, yi = map(int, input().split())
 
        if dy == dx:
            if xi == yi:
                cont += 1
 
        if dy != dx:
            if xi + yi == s:
                cont += 1
    print(cont)
