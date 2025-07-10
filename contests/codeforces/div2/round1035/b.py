t = int(input())

for _ in range(t):
    n = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    pos = list(map(int, input().split()))
    
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    raio = sum(pos)

    if n == 1:
        # Se for só 2 movimento, tem que ser exatamente a distância
        if abs(dist - pos[0]) < 1e-18:
            print("Yes")
        else:
            print("No")
    else:
        # Todas as distâncias implicam em uma circunferência de raio igual à soma dos a_i
        # Se o raio for menor que a distância, não chega
        if dist > raio:
            print("No")
        else:
            # Se a diferença do raio e da distância for par, dá para "ir e voltar"
            # Geometricamente isso é se perguntar se existe um polígono
            # tal que um dos vértices seja (x3, y2)
            # OU EU TO MALUCO?
            # Pensando bem, faz sentido, pq a distância dos movimentos é inteiro
            maior = max(pos)
            baixo = max(0, 2 * maior - raio)

            if baixo <= dist <= raio:
                print("Yes")
            else:
                print("No")



# Se for isso aqui, é eu y LEONHARD EULER

