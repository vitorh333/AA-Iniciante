import math

def ehprimo(n):

    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    target = int(math.sqrt(n) + 1)

    for i in range(3, target, 2):
        if n % i == 0:
            return False

    return True


n = int(input())

if ehprimo(n-2):
    print(f"{2} {n-2}")
else:
    print(-1) 
