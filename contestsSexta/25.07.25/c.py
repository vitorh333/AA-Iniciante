t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    soma = sum(x - 1 for x in a)

    if soma % 2 == 1:
        print("errorgorn")
    else:
        print("maomao90")

