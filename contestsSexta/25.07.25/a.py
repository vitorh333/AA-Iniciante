n, k = map(int, input().split())
s = input()

dist1 = abs(1 - k)
dist2 = abs(n - k)
#print(dist1)
#print(dist2)
if dist1 <= dist2:
    for i in range(k, 1, -1):
        print("LEFT")
    for i in range(len(s)):
        if i != len(s) - 1:
            print(f"PRINT {s[i]}")
            print("RIGHT")
        else:
            print(f"PRINT {s[i]}")
else:
    for i in range(k, n):
        print("RIGHT")
    for i in range(len(s) - 1, -1, -1):
        if i != 0:
            print(f"PRINT {s[i]}")
            print("LEFT")
        else:
            print(f"PRINT {s[i]}")

