def ehpalindromo(p):
    i = 0
    j = len(p) - 1
    palindromo = True
    while j > i:
        if p[i] != p[j]:
            palindromo = False
            break
        i += 1
        j -= 1

    if palindromo:
        return True
    else:
        return False

a, b = map(int, input().split())
cont = 0

for i in range(a, b+1):
    if ehpalindromo(str(i)):
        cont += 1
print(cont)
