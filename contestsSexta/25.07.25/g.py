n = int(input())
p = list(map(int, input().split()))
s = set()
r = 0

while True:
    r += 1
    for i in range(n):
        flag = False
        for j in range(n):
            if abs(p[i]-p[j]) not in s and p[i] != p[j]:
                s.add(abs(p[i] - p[j]))
                flag = True
                break
        if flag:
            break
    if not flag:
        break

if r % 2 == 0:
    print("Alice")
else:
    print("Bob")
