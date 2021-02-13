# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

from math import sqrt
from itertools import permutations

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    return True

digits = '123456789'
output = False

for length in reversed(range(len(digits))):
    a = list(permutations(digits[:length]))
    a.sort(reverse = True)
    for number in a:
        if isprime(int(''.join(number))):
            output = int(''.join(number))
            break
    if output:
        break

print(output)
