# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

total = 0

for n in range(1,1000000):
    if str(n) == str(n)[::-1]:
        binary = bin(n)[2:]
        if binary == binary[::-1]:
            total += n
            print(n, binary)

print(total)
