import math
import sys

def comb(n, p):
    if n == 1 or n == 0: return 0;
    return math.factorial(n) / (math.factorial(n - p) * math.factorial(p))


t  = int(input())

for _ in range(t):
    flag = False
    n, k = map(int, input().split())

    for i in range(n):
        n1 = i
        n0 = n - i
        qtd1 = int(comb(n1, 2))
        qtd0 = int(comb(n0, 2))

        #print(n1)
        #print(n0)

        if qtd1 + qtd0 == k:
            flag = True
            break

    if flag:
        print("YES")
        for s in range(n1):
            sys.stdout.writelines(f"1 ")

        for s in range(n0):
            sys.stdout.writelines(f"-1 ")

        print()

    else:
        print("NO")
