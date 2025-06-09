l, c = map(int, input().split())
m = []

for i in range(l):
    l = list(map(int, input().split()))
    m.append(l)
q = int(input())
cont = 0
for i in range(q):
    li, ci = map(int, input().split())
    li -= 1
    ci -= 1

    if m[li][ci] > 0:
        cont += 1
        m[li][ci] -= 1
print(cont)
