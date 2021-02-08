# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from math import sqrt
from itertools import permutations

def isprime(num):
    root = int(sqrt(num))
    for n in range(2,root+1):
        if num % n == 0:
            return False
    return True

def getPerms(number):
    perms = []
    for perm in list(permutations(str(number))):
        permNumber = int(''.join(perm)) 
        if isprime(permNumber) and permNumber > 1000:
            if permNumber in perms:
                pass
            else:
                perms.append(int(''.join(perm)))
    perms.sort()
    return perms

def testPrimes(primeList):
    if len(primeList) == 3:
        if testPerms[1] - testPerms[0] == testPerms[2] - testPerms[1]:
            return ''.join(testPerms)
    elif len(primeList) > 3:
        firstNum = 0
        while firstNum + 2 <= len(primeList):
            for n in range(firstNum + 2,len(primeList)):
                difference = primeList[n] - primeList[firstNum]
                if (primeList[firstNum] + difference/2) in primeList:
                    return'{}{}{}'.format(primeList[firstNum], primeList[firstNum] + difference//2, primeList[n])
            firstNum += 1
    return False

primes = []

for n in range(1000,10000):
    if isprime(n):
        if getPerms(n)[0] in primes:
            pass
        else:
            primes.append(n)

for prime in primes:
    testPerms = getPerms(prime)
    if testPrimes(testPerms):
        print(testPrimes(testPerms))