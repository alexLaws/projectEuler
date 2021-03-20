# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from math import sqrt

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    if num < 2:
        return False
    return True

n = 1
doubleSquares = []
primes = []

while True:
    output = False
    if isprime(n):
        primes.append(n)
    doubleSquares.append((n**2)*2)
    if n > 33 and n % 2 == 1 and isprime(n) == False:
        for prime in primes:
            if (n - prime) in doubleSquares:
                pass
            else:
                output = n
    if output:
        break
    n += 1

print(output)
