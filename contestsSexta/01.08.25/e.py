from collections import defaultdict

t = int(input())

for _ in range(t):
    s = input()

    freq = defaultdict(list)

    l = []
    maior = 1
    for i in range(len(s)):
        freq[s[i]].append(i)
        if len(freq[s[i]]) > maior:
            l = s[i]
            maior = len(freq[s[i]])
            l = []
            l.append(s[i])
        elif len(seq[i]) == maior:
            l.append(s[i])


    if len(freq) == 1:
        print(0)
    else:
        maxpos = 1
        for i in range(len(l)):
            chute = []
            contp = conti = 0
            for s in range(len(l[i])):
                if freq[l[i]][s] % 2 == 0:
                    contp += 1
                else:
                    conti += 1
        chute.append(maxpos)
        chute.append(contp)
        chute.append(conti)
        maxpos(max(chute))
            

print(maxpos)
print(freq)
