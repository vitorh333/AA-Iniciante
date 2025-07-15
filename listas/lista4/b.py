ini, fim, t = map(int, input().split())
n = int(input())
tempos = list(map(int, input().split()))
 
k = 0
fila = []
melhor = 10**18
best = 10**18
 
for i in range(ini):
    if n > k and tempos[k] == i:
        fila.append(tempos[k])
        k += 1
    if len(fila) == 0:
        if melhor > ini - i:
            melhor = ini - i
            best = i
    else:
        if melhor > (ini - i) + (len(fila) * t):
            best = i
            melhor = (ini - i) + len(fila * t)
 
#print(best)
#print(melhor)
 
flag = False
pi = 0
time = 0
 
for i in range(ini, fim):

    #if melhor == 0:
        #break

    if pi == len(fila) and k == n and not flag:
        break

    if k < n and tempos[k] == i:
        fila.append(tempos[k])
        k += 1
 
    if time == t:
        flag = False
        time = 0
 
        if melhor > (len(fila) - pi) * t and i + ((len(fila) - pi) * t) < fim - 1:
            best = i
            melhor = (len(fila) - pi) * t
 
    if pi < len(fila) and not flag:
        flag = True
        pi += 1
 
    if flag:
        if melhor > (t - time) + ((len(fila) - pi) * t) and i + (t - time) + (len(fila) - pi) * t < fim - 1:
            best = i
            melhor = (t - time) + ((len(fila) - pi) * t)
 
        time += 1
 
    #print(f"{best} , {melhor}")
print(best)
