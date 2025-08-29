t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
 
    max1s = 0
    count = 0
    for c in s:
        if c == "1":
            count += 1
            max1s = max(max1s, count)
        else:
            count = 0
 
    if max1s >= k:
        print("NO")
        continue
 
    perm = [0] * n
    menor = 1
    maior = n
 
    for i in range(n):
        if s[i] == "1":
            perm[i] = menor
            menor += 1
 
    for i in range(n):
        if s[i] == "0":
            perm[i] = maior
            maior -= 1
 
    print("YES")
    print(*perm)
