# How many, not necessarily distinct, values of (n r) for 1 <= n <= 100, are greater than one-million?

from math import factorial

def nCr(n,r):
    return factorial(n) / (factorial(r)*factorial(n-r))

count = 0

for n in range(1,101):
    for r in range(1,n):
        if nCr(n,r) > 1000000:
            count += 1

print(count)
