from pprint import pprint
from collections import defaultdict
grid = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # print(line)
        grid.append(list(line))

# pprint(grid)

START = 'S'
SPLITTER = '^'

beams = defaultdict(int)
beams[grid[0].index(START)] = 1
# print(tuple(beams.keys()))
for line in grid[::2]:
    for i in tuple(beams.keys()):
        if line[i] == SPLITTER:
            beams[i-1] += beams[i]
            beams[i+1] += beams[i]
            del beams[i]

# print(tuple(beams.keys()))
print(sum(beams.values()))