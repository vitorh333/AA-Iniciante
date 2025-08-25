n = int(input())

e = 2 * 4 * 3 * (4 ** (n - 3))

if n >= 4:
    meio = (n - 3) * 4 * (3 ** 2) * (4 ** (n - 4))
else:
    meio = 0

print(e + meio)
