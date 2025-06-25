t, q = map(int, input().split())
c = list(map(int, input().split()))

quad = [False] * t
intervalos = 0

for pos in c:
    idx = pos - 1

    if quad[idx]:
        e = (idx > 0 and quad[idx - 1])
        d = (idx < t - 1 and quad[idx + 1])

        if not e and not d:
            intervalos -= 1  
        elif e and d:
            intervalos += 1

        quad[idx] = False

    else:
        e = (idx > 0 and quad[idx - 1])
        d = (idx < t - 1 and quad[idx + 1])

        if not e and not d:
            intervalos += 1
        elif e and d:
            intervalos -= 1

        quad[idx] = True

    print(intervalos)
