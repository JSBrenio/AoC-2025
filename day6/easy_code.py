import re

nums_and_ops = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = re.sub(r'\s+', ' ', line).strip()
        # print(line)
        nums_or_ops = line.split(" ")
        token = nums_or_ops[0]
        if token.isdigit():
            nums_and_ops.append(nums_or_ops)
        else:
            nums_and_ops.append(nums_or_ops)

print(nums_and_ops)

result = 0
for col in range(len(nums_and_ops[0])):

    operation = nums_and_ops[-1][col]
    print(f"current operation: {operation}")
    curr_sum = None
    if operation == '+':
        curr_sum = 0
    elif operation == '*':
        curr_sum = 1
    else:
        raise Exception

    for row in range(len(nums_and_ops) - 1):
        print(f"current number: {nums_and_ops[row][col]}")
        number = int(nums_and_ops[row][col])
        if operation == '+':
            curr_sum += number
        elif operation == '*':
            curr_sum *= number
        else:
            raise Exception

    print(f"curr_sum = {curr_sum}")
    result += curr_sum

print(result)