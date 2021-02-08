# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from math import sqrt

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    return True

primes = []

for n in range(2,1000000):
    if isprime(n):
        primes.append(n)

most = (953, 21)

index = 0
total = 0

while total < 1000000:
    total += primes[index]
    index += 1

for n in range(index):
    if index-n < most[1]:
        break
    print("starting")
    total = primes[n]
    count = 1
    for x in range(n+1,index):
        print(total, count)
        if total in primes and count > most[1]:
            most = (total, count)
            print(most)
        total += primes[x]
        count += 1
        if total > 1000000:
            break

print(most)