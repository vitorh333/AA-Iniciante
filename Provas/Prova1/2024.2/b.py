t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    s = input()

    cont = 0
    zeros = 0
    i = 0

    while i < n:
        if s[i] == "0":
            zeros += 1

        else:
            zeros = 0

        if zeros == m:
            cont += 1
            zeros = 0
            i += k
        else:
            i += 1

    print(cont)
