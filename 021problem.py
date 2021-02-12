# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt

divisorsSum = {}
amicableSum = 0

def getDivisorSum(number):
    total = 1
    for possibleFactor in range(2,int(sqrt(number))+1):
        if number % possibleFactor == 0:
            total += possibleFactor
            total += int(number/possibleFactor)
    return total

for n in range(2,10000):
    divisorsSum[n] = getDivisorSum(n)

for n in range(4,10000):
    try:
        test = divisorsSum[n]
        if n == divisorsSum[test] and test == divisorsSum[n]:
            if test == n:
                pass
            else:
                amicableSum += n
    except:
        pass

print(amicableSum)
