from pprint import pprint
from copy import deepcopy
# NW N NE
# W    E
# SW S SE
# -1,-1 | -1,0 | -1,1
#  0,-1 |      | 0,1
#  1,-1 |  1,0 | 1,1
dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
grid = []
result = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # print(line)
        grid.append([char for char in line])

# pprint(grid)
# print()
debug = deepcopy(grid)
threshold = 4

for row in range(len(grid)):
    for col in range(len(grid[row])):
        count = 0
        if grid[row][col] == '@':
            for (x, y) in dirs:
                try:
                    nR = row + x
                    nC = col + y
                    if nR < 0 or nC < 0:
                        continue
                    if grid[nR][nC] == '@':
                        # print(f"({nR}, {nC})")
                        count += 1
                except:
                    continue
            # print(f"({row}, {col}): {count}")
            if count < threshold:
                debug[row][col] = 'x'
                result += 1
pprint(debug)
print(result)