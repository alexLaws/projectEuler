# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

import time

tic = time.perf_counter()

five  = ['5', '221', '2111','11111']

ten = ['T', '22222']

for x in five:
    for y in five:
        ten.append("".join(sorted(x+y)))

ten = list(set(ten))

print(f"Through 10 in {time.perf_counter() - tic:0.4f} seconds with {len(ten)} entries")

twenty = ['W']

for x in ten:
    for y in ten:
        twenty.append("".join(sorted(x+y)))

twenty = list(set(twenty))

print(f"Through 20 in {time.perf_counter() - tic:0.4f} seconds with {len(twenty)} entries")

fifty = ['F']

for x in twenty:
    for y in twenty:
        for z in ten:
            fifty.append("".join(sorted(x+y+z)))

for x in twenty:
    for y in ten:
        for z in ten:
            for za in ten:
                fifty.append("".join(sorted(x+y+z+za)))

for x in ten:
    for y in ten:
        for z in ten:
            for za in ten:
                for zb in ten:
                    fifty.append("".join(sorted(x+y+z+za+zb)))

fifty = list(set(fifty))

print(f"Through 50 in {time.perf_counter() - tic:0.4f} seconds with {len(fifty)} entries")

pound = ['H', 'WWWWW']

for x in fifty:
    for y in fifty:
        pound.append("".join(sorted(x+y)))

pound = list(set(pound))

print(f"Through 100 in {time.perf_counter() - tic:0.4f} seconds with {len(pound)} entries")

twoP = ['twopound']

for x in pound:
    for y in pound:
        twoP.append("".join(sorted(x+y)))

twoP = list(set(twoP))

print(len(twoP))

print(f"Finished in {time.perf_counter() - tic:0.4f} seconds")
