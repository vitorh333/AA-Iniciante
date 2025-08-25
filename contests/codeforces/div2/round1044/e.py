# Consulto o no da vez que tem mais conexoes
# Quebro a aresta
# reeogranizo as conexoes pq agora ele pode ta preso
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solve():
    t = int(input())  # número de casos de teste
    for _ in range(t):
        n = int(input())
        grafo = defaultdict(list)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            grafo[u].append(v)
            grafo[v].append(u)

        operacoes = []

        # corta a raiz uma única vez
        raiz = 1
        operacoes.append((2, raiz))

        # DFS para ir até a folha mais profunda e subir
        def dfs(no, pai):
            filhos = [v for v in grafo[no] if v != pai]
            if not filhos:
                # folha: marca
                operacoes.append((1, no))
                return [no]  # caminho de volta
            # visitar filhos recursivamente
            caminhos = []
            for v in filhos:
                caminho = dfs(v, no)
                caminhos.append(caminho)
            # pegar o caminho mais longo
            max_caminho = max(caminhos, key=lambda x: len(x))
            # subir fazendo check no backtracking
            for x in reversed(max_caminho):
                operacoes.append((1, x))
            # agora visitar os outros filhos restantes
            for c in caminhos:
                if c != max_caminho:
                    for x in reversed(c):
                        operacoes.append((1, x))
            return [no]  # caminho de volta para o pai

        dfs(raiz, -1)

        # saída para este caso
        print(len(operacoes))
        for t_op, x in operacoes:
            print(t_op, x)

if __name__ == "__main__":
    solve()
