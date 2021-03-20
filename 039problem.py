# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

from math import ceil, sqrt

most = 0
pValue = 0

for p in range(12,121):
    print(p)
    count = 0
    for hypotenuse in range(ceil(p/3),p):
        for sideA in range(1, p-hypotenuse):
            sideB = (p**2 - 2*p*sideA)/(2*p - 2*sideA)
            if type(sideB) == int:
                count += 1
    if count > most:
        most = count
        pValue = p

print(pValue)
print(most)
