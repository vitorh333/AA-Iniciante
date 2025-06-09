a = int(input())

t = input()
n = input()

tem = False

for i in range(len(n)):
    if n[i] == "o" == t[i]:
        tem  = True
        break
if tem:
    print("Yes")
else:
    print("No")

