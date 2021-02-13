# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot 
# be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time

tic = time.perf_counter()

def sumDivisors(number):
    divisor = 2
    total = 1
    while divisor <= number/divisor:
        if number % divisor == 0:
            total += divisor
            if divisor < int(number/divisor):
                total += int(number/divisor)
        divisor += 1
    return total


def checkSums(numbers, test):
    for number in numbers:
        if test - number in numbers:
            return True
    return False

abundants = []
total = 0

for n in range(1,28124):
    total += n
    if n < sumDivisors(n):
        abundants.append(n)

prelim = []

timeA = time.perf_counter()
for n in range(len(abundants)):
    for x in range(n,len(abundants)):
        prelim.append(abundants[n]+abundants[x])

timeB = time.perf_counter()

sums = set(prelim)

for number in sums:
    if number < 28124:
        total -= number

print(total)

toc = time.perf_counter()
print(f"Ran in {toc - tic:0.4f} seconds")
print(f"Ran in {timeB - timeA:0.4f} seconds")
