def euclides(a, b):
    while b!= 0:
        a, b = b, a % b

    return a

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

mdc = nums[0]

for i in range(1, n):
    mdc = euclides(mdc, nums[i]);

target = int(mdc ** 0.5)

ok = False

if(target == mdc ** 0.5):
    ok = True

cont = 0
for i in range(1, target + 1):
    if mdc % i == 0:
        cont += 1

if ok:
    print(2 * cont -1)
else:
    print(2 * cont)
