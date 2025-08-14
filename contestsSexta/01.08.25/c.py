t = int(input())

for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    q.sort()
    flag = False
    resp = ""

    achei = False
    i = 0
    while i < len(q) - 1:
        if q[i] == q[i+1]:
            l = q[i]
            q.pop(i+1)
            q.pop(i)
            achei = True
            break
        i += 1

    if achei:
        j = 0
        while j < len(q) - 1:
            if abs(q[j] - q[j+1]) < 2 * l:
                flag = True
                resp = f"{l} {l} {q[j]} {q[j+1]}"
                break
            j += 1

    if flag:
        print(resp)
    else:
        print(-1)

