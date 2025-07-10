t = int(input())
for _ in range(t):
    a, b, x, y = map(int, input().split())
    custo = 0
    ok = True

    # a e b <= 100

    # TESTEMUNHAS DE TOKIODK

    while a != b:
        if a < b:
            # Verificar oq cada operacao faz
            a1 = a + 1
            axor = a ^ 1

            dista1 = abs(b - a1)
            distxor = abs(b - axor)

            # Melhor opcao
            if dista1 < distxor:
                a = a1
                custo += x
            elif distxor < dista1:
                a = axor
                custo += y
            else:
                if x <= y:
                    a = a1
                    custo += x
                else:
                    a = axor
                    custo += y
        else:
            if a % 2 == 0:
                # Xor aumenta 1, loopei
                ok = False
                break
            else:
                a = a ^ 1
                custo += y

    if ok:
        print(custo)
    else:
        print(-1)

