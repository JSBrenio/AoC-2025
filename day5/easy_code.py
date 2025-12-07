ingrendientIdList = []
availableList = [] 
result = 0

with open('input.txt', 'r') as file:
    lineBreakFlag = False
    for line in file:
        line = line.strip()
        print(line)
        if not line:
            lineBreakFlag = not lineBreakFlag
            continue
        
        if not lineBreakFlag:
            ingrendientIdList.append(line)
        else:
            availableList.append(int(line))

print(ingrendientIdList)
print(availableList)

while availableList:
    found = False
    id = availableList.pop()
    # print(f"ID: {id}")
    for ranges in ingrendientIdList:
        start = int(ranges.split('-')[0])
        end = int(ranges.split('-')[1])
        # print(f"{start} - {end}")
        if start <= id <= end:
            result += 1
            break

print(result)