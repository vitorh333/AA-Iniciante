n, m = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
cont = 0
for i in range(m):
    if t[i] < 1:
        cont += -t[i]

print(cont)
