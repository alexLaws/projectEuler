# Euler discovered the remarkable quadratic formula: n^2 + n + 41


# It turns out that the formula will produce 40 primes for the consecutive integer values 0 -> 39. However, when n = 40, the answer is divisible by 41,
# and certainly when n=41 the answer is clearly divisible by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0->79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form: n^2 + an + b

# where abs(a) < 1000 and abs(b) < 1000

# where abs(n) is the modulus/absolute value of n

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for 
# consecutive values of n, starting with n=0.

from math import sqrt

def isprime(num):
    root = int(sqrt(abs(num)))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    return True

maxPrimes = 0
maxProduct = 0

for a in range(-999,1000):
    for b in range(-999,1000):
        testCount = 0
        value = 0
        while True:
            if isprime(value*value + (a*value) + b):
                testCount += 1
            else:
                break
            value += 1
        if testCount > maxPrimes:
            maxPrimes = testCount
            maxProduct = a*b

print(maxProduct)