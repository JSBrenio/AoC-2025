start = 50
with open('example.txt', 'r') as file:
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
        print(result)