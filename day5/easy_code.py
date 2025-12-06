ingrendientIdList = []
availableIdList = []
ingrendientIdSet = set()
result = 0

with open('example.txt', 'r') as file:
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
            availableIdList.append(int(line))

print(ingrendientIdList)
print(availableIdList)

for ranges in ingrendientIdList:
    start = int(ranges.split('-')[0])
    end = int(ranges.split('-')[1])
    for i in range(start, end + 1):
        ingrendientIdSet.add(i)
        
for id in availableIdList:
    if id in ingrendientIdSet:
        result += 1

print(result)