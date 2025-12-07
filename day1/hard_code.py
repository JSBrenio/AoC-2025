start = 50
zeros = 0
rotations = []
with open('input.txt', 'r') as file:
    for line in file:
        # print(line)
        dir = line[0]
        dist = int(line[1:])
        # print(dir, dist)
        rotations.append((dir, dist))
# print(rotations)

N = 100
result = start
for dir, dist in rotations:
    # print(dir, dist)
    mult = 1 if dir == 'R' else -1
    rotate = dist * mult
    total = result + rotate
    
    if total >= result:
        zeros += (total // N) - (result // N)
    else:
        zeros += ((result - 1) // N) - ((total - 1) // N)
    result = total % N

    print(result)

print(zeros)