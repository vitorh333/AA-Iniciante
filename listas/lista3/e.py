f = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

n = set()

for i in range(1, len(a)):
    n.add(a[i])
for i in range(1, len(b)):
    n.add(b[i])

todos = True

for i in range(1, f+1):
    if i not in n:
        todos = False
        break
if todos:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
