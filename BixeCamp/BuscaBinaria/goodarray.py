t = int(input())

for _ in range(t):
    l, r = map(int, input().split())

    i = 1
    resp = 1 
    while r >= l:
        l += i
        i += 1

        if r >= l:
            resp += 1
    print(resp)


