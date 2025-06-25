import sys

n, m = map(int, input().split())
p = input()

abertos = 0
fechados = 0

for c in p:
    if c == '(':
        if abertos < m // 2:
            sys.stdout.writelines("(")
            abertos += 1
    else:
        if fechados < abertos:
            sys.stdout.writelines(")")
            fechados += 1
    if abertos + fechados == m:
        break
print()

