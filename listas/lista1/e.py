nums = list(map(int, input().split()))
soma = 0

for i in range(len(nums)):
    if nums[i] != 0:
        soma += 2 ** i 
print(soma)
