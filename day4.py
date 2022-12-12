# part 1
def findcontains(line):
    mid = line.find(',')

    left = line[:mid]
    right = line[mid+1:]

    ranges = [left,right]

    for i in range(2):
        mid = ranges[i].find('-')
        ranges[i] = [int(ranges[i][:mid]), int(ranges[i][mid+1:])]


    if ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]: return 1
    elif ranges[0][0] >= ranges[1][0] and ranges[0][1] <= ranges[1][1]: return 1
    else: return 0

#part 2
def findoverlaps(line):
    if findcontains(line):
        return 1

    mid = line.find(',')

    left = line[:mid]
    right = line[mid+1:]

    ranges = [left,right]

    for i in range(2):
        mid = ranges[i].find('-')
        ranges[i] = [int(ranges[i][:mid]), int(ranges[i][mid+1:])]

    
    if ranges[0][1] >=ranges[1][0] and ranges[0][0] <= ranges[1][0]: return 1
    elif ranges[0][0] <= ranges[1][1] and ranges[0][1] >= ranges[1][1]: return 1
    else: return 0

with open("day4.txt", 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    numcontained = 0
    numoverlapped = 0
    for line in lines:
        numcontained += findcontains(line)
        numoverlapped += findoverlaps(line)

    print(numcontained)
    print(numoverlapped)