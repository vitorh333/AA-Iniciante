import sys

sys.setrecursionlimit(10**6)

def validChuva(i, j):
    if validPos(i-1, j):
        if(greed[i-1][j] == "o"):
            return True
    if validPos(i, j-1) and validPos(i+1, j-1):
        if greed[i][j-1] == "o" and greed[i+1][j-1] == "#":
            return True
    if validPos(i, j+1) and validPos(i+1, j+1):
        if greed[i][j+1] == "o" and greed[i+1][j+1] == "#":
            return True

    return False

def validPos(i, j):
    return i < n and j < m and i >= 0 and j >= 0

def dfs(i, j):
    if not validPos(i, j) or visitado[i][j] or greed[i][j] == "#":
        return
    visitado[i][j] = True
    greed[i][j] = "o"

    dfs(i + 1, j)

    if validPos(i + 1, j) and greed[i+1][j] == "#":
        dfs(i, j-1)
        dfs(i, j+1)

n, m = map(int, input().split())
greed = []

for i in range(n):
    s = input()
    k = []

    for i in range(len(s)):
        k.append(s[i])

    greed.append(k)

visitado = [[False for _ in range(m)] for _ in range(n)]

for j in range(m):
    if greed[0][j] == "o":
        dfs(0, j)
        break

for i in range(n):
    print("".join(greed[i]))
