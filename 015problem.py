# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

a = [[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]

for row in range(1,len(a)):
    for col in range(1,len(a[0])):
        a[row].insert(col,a[row][col-1] + a[row-1][col])

print(a[20][20])
