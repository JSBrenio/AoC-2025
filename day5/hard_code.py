ingrendientIdList = []

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
            break

print(ingrendientIdList)

# ex: 100 - 10000
# Start Inside - End Inside:   101-1000 -> skip
# Start Inside - End outside:  101-10001 -> add upper bound
# Start Outside - End Inside:  99-1000 -> add lower bound
# Start Outside - End outside: 99-10001 -> add lower/upper bound
# Mutually Exclusive: 10-11 -> add new lower/upper bounds
result = []
result.append((int(ingrendientIdList[0].split('-')[0]), int(ingrendientIdList[0].split('-')[1])))
for ranges in ingrendientIdList[1:]:
    start = int(ranges.split('-')[0])
    end = int(ranges.split('-')[1])
    print(f"{start} - {end}")
    
    mutex = False
    for i, (rStart, rEnd) in enumerate(result):
        mutex= False
        # print(f"{start} - {end} versus {rStart} - {rEnd}")
        if start >= rStart and end <= rEnd:
            # print("Inside -> skip")
            break
        elif start >= rStart and start < rEnd and end > rEnd:
            # print("Add upper bound")
            result[i] = (rStart, end)
            break
        elif start < rStart and end <= rEnd and end >= rStart:
            # print("Add lower bound")
            result[i] = (start, rEnd)
            break
        elif start < rStart and end > rEnd:
            # print("Add lower/upper bound")
            result[i] = (start, end)
            break
        else:
            mutex = True
    # print(mutex) 
    if mutex:
        result.append((start, end))

print(result)

result.sort()

folded = []
for (start, end) in result:
    # if last ele's end is less than start
    if not folded or folded[-1][1] < start - 1:
        folded.append([start, end])
    else:
        folded[-1][1] = max(folded[-1][1], end)

print(folded)
resCount = 0
for (start, end) in folded:
    # print(start, end)
    resCount += end - start + 1
print(resCount)