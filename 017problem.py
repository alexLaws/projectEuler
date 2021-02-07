# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

ones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3}
teens = {11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
tens = {10:3, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}

length = 0

for x in range(1,1001):
    n = x
    if n == 1000:
        length += 11
    elif n//100 > 0:
        length += 7
        length += ones[n//100]
        if n % 100 > 0:
            length += 3
        n -= n//100 * 100
    if n <= 10:
        length += ones[n]
    elif n < 20:
        length += teens[n]
    elif n < 100:
        length += ones[n % 10]
        length += tens[n - (n%10)]

print(length)
