t = int(input())
 
for _ in range(t):
    n, a, b = map(int, input().split())
    
    if b >= a:
        if (n - b) %  2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if (a - b) % 2 == 0 and (n - a) % 2 == 0:
            print("YES")
        else:
            print("NO")
