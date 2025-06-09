n = int(input())
resp = f"{n} "

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = (n * 3) + 1
    resp += f"{n} "
print(resp.strip())
