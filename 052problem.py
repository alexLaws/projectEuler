# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

number = 1

while True:
    if set(str(2 * number)) == set(str(3 * number)) == set(str(4 * number)) == set(str(5 * number)) == set(str(6 * number)):
        break
    else:
        number += 1

print(number)
