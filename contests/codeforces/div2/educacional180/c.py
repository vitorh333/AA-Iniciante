t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    
    l.sort(reverse=True)
    maiorgeral = l[0]
    cont = 0

    for i in range(n):
        for j in range(i + 1, n):
            soma_parcial = l[i] + l[j]

            # Previne IndexError
            if j + 1 < n and soma_parcial + l[j + 1] <= maiorgeral:
                continue

            for s in range(j + 1, n):
                soma = soma_parcial + l[s]
                maior = l[i]

                pode1 = False
                pode2 = False

                tem_maiorgeral = (l[i] == maiorgeral or l[j] == maiorgeral or l[s] == maiorgeral)

                if tem_maiorgeral:
                    if soma - maiorgeral > maiorgeral:
                        pode2 = True
                        cont += 1
                else:
                    if soma - maior > maior and soma > maiorgeral:
                        pode1 = True
                        cont += 1

                # Como está decrescente, se não funcionou, os próximos s só vão piorar
                if not pode1 and not pode2:
                    break

    print(cont)

