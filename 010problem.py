from math import sqrt

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    return True

sum = 0

for n in range(2,2000001):
    if isprime(n):
        sum += n

print(sum)
