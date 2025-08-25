from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        grafo = defaultdict(list)
        for _ in range(n-1):
            u, v = map(int, input().split())
            grafo[u].append(v)
            grafo[v].append(u)

        operacoes = []

        # 1) corta a raiz
        raiz = 1
        operacoes.append((2, raiz))

        visited = [False] * (n + 1)

        # marca nós de grau >= 3 para cortes adicionais
        cortes = set()
        for u in range(1, n+1):
            if u != raiz and len(grafo[u]) >= 3:
                cortes.add(u)

        for u in cortes:
            operacoes.append((2, u))

        # DFS para varrer paths lineares
        def dfs(u, p):
            visited[u] = True
            for v in grafo[u]:
                if v != p and not visited[v] and v not in cortes:
                    dfs(v, u)
            operacoes.append((1, u))

        for u in range(1, n+1):
            if not visited[u]:
                dfs(u, 0)

        print(len(operacoes))
        for t_op, x in operacoes:
            print(t_op, x)

if __name__ == "__main__":
    solve()

