def valid(i, j, visitados):
    if 0 <= i < n and 0 <= j < m:
        if not visitados[i][j] and greed[i][j] != "#":
            return True
    return False


def dfs(greed, i, j, visitados, contv, target):
    visitados[i][j] = True
    contv[0] += 1

    if contv[0] == target:
        return True

    if valid(i +1, j, visitados):
        if dfs(greed, i + 1, j, visitados, contv, target):
            return True

    if valid(i -1, j, visitados):
        if dfs(greed, i - 1, j, visitados, contv, target):
            return True

    if valid(i, j+1, visitados):
        if dfs(greed, i, j + 1, visitados, contv, target):
            return True

    if valid(i, j - 1, visitados):
        if dfs(greed, i, j - 1, visitados, contv, target):
            return True

    return False


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, input().split())

greed = []
c = 0
visitados = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    s = list(input())
    c += s.count(".")
    greed.append(s)

contv = [0]
target = c - k
#print(target)
for i in range(n):
    cabou = False
    for j in range(m):
        #print('oi')
        if greed[i][j] == ".":
            dfs(greed, i, j, visitados, contv, target)
            cabou = True
        if cabou:
            break
    if cabou:
        break

for i in range(n):
    for j in range(m):
        if not visitados[i][j] and greed[i][j] != "#":
            greed[i][j] = "X"

#print(visitados)

for i in range(n):
    for j in range(m):
        sys.stdout.writelines(greed[i][j])
    print()
