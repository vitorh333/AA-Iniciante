from collections import defaultdict

s = input()
mapa = defaultdict(int)
cont = 0

for i in range(len(s)):
    mapa[s[i]] += 1


for i in range(len(s)):
    cont += mapa[s[i]]

print(cont)
