# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

from math import sqrt

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    if num < 2:
        return False
    return True

count = 13

n = 101

while n < 1000000:
    if isprime(n):
        possibilities = []
        for x in range(1,len(str(n))):
            possibilities.append(int(str(n)[x:]+str(n)[:x]))
        if all([isprime(num) for num in possibilities]):
            count += 1
    n += 2

print(count)
