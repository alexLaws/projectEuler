# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from math import sqrt

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    primes[num] = True
    return True

def countPrimeFactors(number):
    count = 0
    for n in range(2,int(number/2+1)):
        try:
            if number % n == 0 and primes[n]:
                count += 1
        except:
            if number % n == 0 and isprime(n):
                count += 1
    return count

consecutive = 0
product = 2
primes = {}

while consecutive < 4:
    product += 1
    if countPrimeFactors(product) >= 4:
        consecutive += 1
    else:
        consecutive = 0

print(product-3)
