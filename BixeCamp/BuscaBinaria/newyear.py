n, k = map(int, input().split())

time = [5] * n
total = 240 - k

for i in range(1, n):
    time[i] = time[i-1] + 5*(i+1)

ini = 0
fim = n-1
resp = n

while fim >= ini:
    meio = (fim + ini) // 2

    if time[meio] > total:
        resp = meio
        fim = meio -1
    else:
        ini = meio + 1

print(resp)
