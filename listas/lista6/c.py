t = int(input())

for _ in range(t):
    s = input()
    resp = 1
    flag = s[0] == "0"

    for i in range(len(s)):
        if s[i] == "?" and i == 0:
            resp *= 9
        elif s[i] == "?":
            resp *= 10

    if flag:
        print(0)
    else:
        print(resp)

