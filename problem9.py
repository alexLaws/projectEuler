# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

found = False

for a in range(999):
    for b in range(999-a):
        c = 1000-a-b
        if a**2 + b**2 == c**2 and a*b*c > 0:
            print(a*b*c)
            found = True
            break
    if found == True:
        break
