# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

x = 600851475143
n = 3
maxPrime = 0

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    return True

while n < sqrt(x):
    if x % n == 0:
        if isprime(n):
            maxPrime = n
    n+= 1

print(maxPrime)
