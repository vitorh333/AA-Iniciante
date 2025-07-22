n, x = map(int, input().split())
a = list(map(int, input().split()))

arr = [(val, idx) for idx, val in enumerate(a)]
arr.sort()

for i in range(n):
    target = x - arr[i][0]
    l = i + 1
    r = n - 1
    while l < r:
        total = arr[l][0] + arr[r][0]
        if total == target:
            i1 = arr[i][1] + 1
            i2 = arr[l][1] + 1
            i3 = arr[r][1] + 1
            print(i1, i2, i3)
            exit()
        elif total < target:
            l += 1
        else:
            r -= 1

print("IMPOSSIBLE")

