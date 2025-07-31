t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    ok = True

    for i in range(n):
        # x precisa ser > min(a)
        x = b[i]
        minimo = min(a)
        if x <= minimo:
            ok = False
            break
        # encontrar primeiro índice i onde a[i] < x e a[0..i-1] >= x
        idx = -1
        for j in range(n):
            if a[j] < x and all(a[k] >= x for k in range(j)):
                idx = j
                break
        if idx == -1:
            ok = False
            break
        a[idx] += x
    print("YES" if ok else "NO")

