# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.

from math import sqrt

# last digit is 0 so the digit before that must also be 0, so we can just divide the numbers by 100 and then multiply the answer by 10 to get the final answer

n = int(sqrt(10203040506070809))-1

# since we know the new number ends in 9, the square root must end in 3 or 7

if n % 10 < 3:
    n += 3 - n % 10
elif n > 3 and n < 7:
    n += 7 - n % 10
elif n > 7:
    n += 13 - n % 10

while n < int(sqrt(19293949596979899))+1:
    number = str(n**2)
    if number[0] == '1' and number[2] == '2' and number[4] == '3' and number[6] == '4' and number[8] == '5' and number[10] == '6' and number[12] == '7' and number[14] == '8' and number[16] == '9':
        print(number, n)
        print(n*10)
        break
    if n % 10 == 7:
        n += 6
    else:
        n += 4
