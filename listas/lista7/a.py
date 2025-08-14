#Posso usar um dfs para identificar um componente conexo
#Rodo para um qualquer, vejo os q nao foram visitados, rodo, dnv
#Mantenho os que eu rodei, e ligo todos.

def dfs(no):
    visitados[no] = True

    for vizinho in grafo[no]:
        if not visitados[vizinho]:
            dfs(vizinho)

from collections import defaultdict

import sys
sys.setrecursionlimit(10**6)

n, v = map(int, input().split())
grafo = defaultdict(list)

for i in range(v):
    v1, v2, = map(int, input().split())
    
    grafo[v1].append(v2)
    grafo[v2].append(v1)

candidatos = []
visitados = [False] * (n + 1)

for i in range(1, n+1):
    if not visitados[i]:
        candidatos.append(i)
        dfs(i)

if len(candidatos) == 1:
    print(0)
else:
    print(len(candidatos) - 1)
    for i in range(len(candidatos) - 1):
        print(candidatos[i], candidatos[i+1])
