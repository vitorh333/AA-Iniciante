n, k = map(int, input().split())
s = list(map(str, input().split()))
resp = 0
for i in range(len(s)):
    cont = 0
    for j in range(len(s[i])):
        if s[i][j] == "4" or s[i][j] == "7":
            cont += 1
    if cont <= k:
        resp += 1

print(resp)

