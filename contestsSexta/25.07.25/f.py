s = input()
cont = 0
conj = set()

for i in range(len(s)):
    conj.add(s[i])

for i in range(len(s)):
    if s[i] in conj:
        cont += 1
print(cont)
