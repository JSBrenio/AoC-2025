import math
from pprint import pprint

nums_and_ops = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        print(line)
        nums_and_ops.append(list(line))

pprint(nums_and_ops)

result = 0
running_calc = []
for col in range(len(nums_and_ops[0]) - 1, -1, -1):
    # print("COL", col)
    number = ''
    calculate = False
    operation = ' '
    for row in range(len(nums_and_ops)):
        # print("ROW", row, "COL", col)
        token = nums_and_ops[row][col]
        if token == ' ':
            # print("SPACE")
            continue
        elif token == '+':
            calculate = True
            operation = token
        elif token == '*':
            calculate = True
            operation = token
        else:
            number += token
        # print(token)
    running_calc.append(int(number)) if number else None
    # print(running_calc)
    if calculate:
        if operation == '+':
            result += sum(running_calc)
        elif operation == '*':
            result += math.prod(running_calc)
        running_calc.clear()
    # print("RES:", result)       

print(result)