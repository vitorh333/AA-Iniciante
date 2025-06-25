import sys

n = int(input())
e = list(map(int, input().split()))

for i in range(len(e)):
    sys.stdout.writelines(f"{e[i]} ")
    soma = e[i]
    for s in range(i+1, len(e)):
        soma += e[s]
        sys.stdout.writelines(f"{soma} ")
    print()
