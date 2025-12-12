from pprint import pprint
grid = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # print(line)
        grid.append(list(line))

# pprint(grid)

START = 'S'
TACHYON = '|'
SPLITTER = '^'
SPACE = '.'
foundStart = False
split = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        try:
            # space below start
            if not foundStart and grid[row - 1][col] == START:
                grid[row][col] = TACHYON
            # Tachyon above splitter
            if grid[row][col] == SPLITTER and grid[row - 1][col] == TACHYON:
                grid[row][col - 1] = TACHYON; grid[row][col + 1] = TACHYON
                split += 1
            # Tachyon above space
            elif grid[row][col] == SPACE and grid[row - 1][col] == TACHYON:
                grid[row][col] = TACHYON
        except:
            None
            
# pprint(grid)
# print(len([cell for cell in grid[-1] if cell == TACHYON]))
print(split)