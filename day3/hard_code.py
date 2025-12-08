input = []
result = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        input.append([char for char in line])

print(input)

k = 12
for bank in input:
    print(bank)
    stack = []
    for idx, val in enumerate(bank):
        # While stack not empty and we can pop (i.e., enough digits remain to still fill k) 
        # and current digit is better (larger)
        while stack and val > stack[-1] and len(stack) - 1 + (len(bank) - idx) >= k:
            stack.pop()
        if len(stack) < k:
            stack.append(val)
    
    result += int("".join(stack[:]))
        
print(result)