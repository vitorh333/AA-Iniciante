import sys

n, k, num = map(int, input().split())
a = list(map(int, input().split()))
cont = 0
for i in range(k):
    sys.stdout.writelines(f"{a[i]} ")
sys.stdout.writelines(f"{num} ")
for i in range(k, n):
    sys.stdout.writelines(f"{a[i]} ")

print()

