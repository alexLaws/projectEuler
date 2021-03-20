# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

from itertools import permutations

test = 345

# while True:
#     num_cubes = 0
#     cubed = test**3
#     print(cubed)
#     perms = list(set(permutations(str(cubed))))
#     print(perms)
#     for perm in perms:
#         number = int("".join(perm))
#         if int(number**(1/3)) == number**(1/3):
#             num_cubes += 1
#     print(test, num_cubes)
#     if num_cubes == 3:
#         break
#     test += 1
#     break

# print(test)


test = 345**3
print('345')
print(test)
print(test**(1/3))

print(66430125**(1/3))

# print(int(cubed**(1/3)))
# print(cubed**(1/3))
# print(int(cubed**(1/3))==cubed**(1/3))
# print(int(not_cubed**(1/3)))
# print(not_cubed**(1/3))
# print(int(not_cubed**(1/3))==not_cubed**(1/3))