# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isDivisible(num):
    out = True
    for x in range(1,21):
        if num % x > 0:
            out = False
    return out

integer = 2520

while True:
    if isDivisible(integer):
        break
    integer += 2520

print(integer)
