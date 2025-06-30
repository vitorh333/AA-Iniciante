t = int(input())

for _ in range(t):
    n = int(input())
    quad = list(map(int, input().split()))
    soma = sum(quad)

    if soma ** 0.5 == int(soma ** 0.5):
        print("Yes")
    else:
        print("No")

