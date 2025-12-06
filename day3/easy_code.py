input = []
result = 0
with open('example.txt', 'r') as file:
    for line in file:
        line = line.strip()
        input.append([char for char in line])

# print(input)

for bank in input:
    print(bank)
    running_max = float('-inf')
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            running_max = max(int(bank[i] + bank[j]), running_max)
    print(running_max)
    result += running_max

print(result)