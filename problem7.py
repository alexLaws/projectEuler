# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from math import sqrt

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    return True

n = 6
num = 14

while n < 10001:
    num += 1
    if isprime(num):
        n += 1

print(num)
