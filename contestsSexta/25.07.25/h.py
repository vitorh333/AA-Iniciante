t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    if a == b:
        print("0 0")
    else:
        dif = abs(a - b)
        op = min(a % dif, dif - a % dif)
        print(dif, op)
