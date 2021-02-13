# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

curiousSum = 0

for n in range(3,2500000):
    total = 0
    for digit in str(n):
        total += factorial(int(digit))
    if total == n:
        curiousSum += n

print(curiousSum)
