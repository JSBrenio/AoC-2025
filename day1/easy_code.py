start = 50
zeros = 0
with open('input.txt', 'r') as file:
    result = start
    for line in file:
        # print(line)
        dir = line[0]
        dist = int(line[1:])
        # print(dir, dist)
        if dir is "L":
            result = (result - dist) % 100
        elif dir is "R":
            result = (result + dist) % 100
        
        if result == 0:
            zeros += 1
        print(result)
print(zeros)