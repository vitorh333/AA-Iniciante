t = int(input())

for _ in range(t):
    n = int(input())
    px, py, qx, qy = map(int, input().split())
    a = list(map(int, input().split()))

    dist = ((qx - px)**2 + (qy - py)**2) ** 0.5
    soma = sum(a)
    maior = max(a)
    limite_inferior = max(0, 2 * maior - soma)

    if limite_inferior <= dist <= soma:
        print("Yes")
    else:
        print("No")

