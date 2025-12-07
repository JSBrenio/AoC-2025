with open('input.txt', 'r') as file:
    input = []
    result = 0
    for line in file:
        input = line.split(',')
    print(input) 
    for ranges in input:
        start = int(ranges.split('-')[0])
        end = int(ranges.split('-')[1])
        # print(start,end)
        for i in range(start, end + 1):
            # print(i)
            word = str(i)
            mid = len(word) // 2
            if word[0:mid] == word[mid:]:
                # print(word[0:mid], word[mid:])
                result += i
    
    print(result)