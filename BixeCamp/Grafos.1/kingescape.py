import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def valid(greed, i, j):
    if 0 <= i < n and 0 <= j < n:
        if greed[i][j] != "X" and not visitados[i][j]:
            return True
    return False

def dfsQ(greed, i, j, pos):
    
    if pos != 0:
        greed[i][j] = "X"
    
    if pos == 0:
        if valid(greed, i - 1, j):
            dfsQ(greed, i - 1, j, 1)

        if valid(greed, i - 1, j + 1):
            dfsQ(greed, i - 1, j + 1, 2)

        if valid(greed, i, j + 1):
            dfsQ(greed, i, j + 1, 3)

        if valid(greed, i + 1, j + 1):
            dfsQ(greed, i + 1, j + 1, 4)

        if valid(greed, i + 1, j):
            dfsQ(greed, i + 1, j, 5)

        if valid(greed, i + 1, j - 1):
            dfsQ(greed, i + 1, j - 1, 6)

        if valid(greed, i, j - 1):
            dfsQ(greed, i, j - 1, 7)
        
        if valid(greed, i - 1, j - 1):
            dfsQ(greed, i - 1, j - 1, 8)

    if pos == 1:
        if valid(greed, i - 1, j):
            dfsQ(greed, i - 1, j, 1)

    if pos == 2:
        if valid(greed, i - 1, j + 1):
            dfsQ(greed, i - 1, j + 1, 2)

    if pos == 3:
        if valid(greed, i, j + 1):
            dfsQ(greed, i, j + 1, 3)

    if pos == 4:
        if valid(greed, i + 1, j + 1):
            dfsQ(greed, i + 1, j + 1, 4)

    if pos == 5:
        if valid(greed, i + 1, j):
            dfsQ(greed, i + 1, j, 5)

    if pos == 6:
        if valid(greed, i + 1, j - 1):
            dfsQ(greed, i + 1, j - 1, 6)

    if pos == 7:
        if valid(greed, i, j - 1):
            dfsQ(greed, i, j - 1, 7)
    if pos == 8:
        if valid(greed, i - 1, j - 1):
            dfsQ(greed, i - 1, j - 1, 8)


def dfsR(greed, i, j):
    if greed[i][j] != "R":
        visitados[i][j] = True

    if valid(greed, i, j + 1):
        dfsR(greed, i, j + 1)

    if valid(greed, i, j - 1):
        dfsR(greed, i, j - 1)

    if valid(greed, i + 1, j):
        dfsR(greed, i + 1, j)

    if valid(greed, i - 1, j):
        dfsR(greed, i - 1, j)

    if valid(greed, i + 1, j + 1):
        dfsR(greed, i + 1, j + 1)

    if valid(greed, i - 1, j - 1):
        dfsR(greed, i - 1, j - 1)

    if valid(greed, i - 1, j + 1):
        dfsR(greed, i - 1, j + 1)

    if valid(greed, i + 1, j - 1):
        dfsR(greed, i + 1, j - 1)



n = int(input())
qn, qc = map(int, input().split())
xn, xc = map(int, input().split())
rn, rc = map(int, input().split())

greed = [["." for _ in range(n)] for i in range(n)]
greed[qn - 1][qc - 1] = "Q"
greed[rn -1][rc - 1] = "R"

visitados = [[ False for _ in range(n)] for _ in range(n)]

dfsQ(greed, qn -1, qc -1, 0)
dfsR(greed, rn -1, rc -1)

#print(visitados)
#print(greed)

if visitados[xn -1][xc -1]:
    print("YES")
else:
    print("NO")
