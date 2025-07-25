n = int(input())
c = list(map(int, input().split()))

i = 0
j = n-1

while i < n:
    if c[i] != c[j]:
        print((j- i))
        break
    else:
        j -= 1

    if j == i:
        i += i
        j = n-1

