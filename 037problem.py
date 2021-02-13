# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from math import sqrt

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    if num < 2:
        return False
    return True

def checkRightToLeft(number):
    number = number // 10
    while number > 0:
        if isprime(number):
            pass
        else:
            return False
        number = number // 10
    return True

def checkLeftToRight(number):
    while len(str(number)) > 1:
        number = int(str(number)[1:])
        if isprime(number):
            pass
        else:
            return False
    return True

primes = 0
test = 11
total = 0

while primes < 11:
    if isprime(test) and checkRightToLeft(test) and checkLeftToRight(test):
        primes += 1
        total += test
    test += 2

print(total)
