# a quantidade se subseqs e (n * n-1) / 2
# se eu colocar o 1 no final eu ja somo g(t) = n

import sys

t = int(input())

for _ in range(t):
    n = int(input())

    for i in range(n-1):
        sys.stdout.writelines("0")

    sys.stdout.writelines("1")
    print()

