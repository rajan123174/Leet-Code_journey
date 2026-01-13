def binaryExponentiation(x,n):
    ans = 1
    if n == 0:
        return 1.0
    if x == 0:
        return 0.0
    if x == 1:
        return 1.0
    if x == -1 and n%2 == 0:
        return 1.0
    if x == -1 and n%2 != 0:
        return -1.0
    if n < 0:
        x = 1/x
        n = -n
    while n > 0:
        if n % 2 == 1:
            ans *= x
        x *= x
        n //= 2
    return ans

x = 3
n = 5
print(binaryExponentiation(x,n))