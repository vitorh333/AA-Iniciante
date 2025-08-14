def dfs(no, f):
    total = 0

    for vizinho in grafo[no]:
        total += dfs(vizinho, f) + 1

    f[no] = total
    return total

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

n = int(input())
func = list(map(int, input().split()))
grafo = defaultdict(list)

for i in range(len(func)):
    grafo[func[i]].append(i + 2)


f = [0] * (n + 1)
dfs(1, f) #chefe

for i in range(1, len(f)):
    sys.stdout.writelines(f"{f[i]} ")

print()



