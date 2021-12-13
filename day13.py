def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    coordinates = []
    folds = []
    for row in range(len(inputLines)):
        if inputLines[row] == '\n':
            continue
        elif 'fold' in inputLines[row]:
            folds.append(inputLines[row].strip('\n')[11:])
        else:
            thisLine = inputLines[row].strip('\n').split(',')
            coordinates.append((int(thisLine[0]), int(thisLine[1])))

    return coordinates, folds


def buildGrid(coordinateList):
    maxX = 0
    maxY = 0
    for entry in coordinateList:
        if entry[0] > maxX:
            maxX = entry[0]
        if entry[1] > maxY:
            maxY = entry[1]

    if maxX % 2 == 1 and maxY % 2 == 1:
        grid = [[0 for i in range(maxX+2)] for j in range(maxY+2)]
    elif maxX % 2 == 1:
        grid = [[0 for i in range(maxX+2)] for j in range(maxY+1)]
    elif maxY % 2 == 1:
        grid = [[0 for i in range(maxX+1)] for j in range(maxY+2)]
    else:
        grid = [[0 for i in range(maxX+1)] for j in range(maxY+1)]

    for entry in coordinateList:
        grid[entry[1]][entry[0]] = 1
    return grid


def fold(grid, foldTuple):
    foldType = foldTuple[0]
    foldPlace = int(foldTuple[1])

    for distance in range(1, foldPlace+1):
        if foldType == 'y':
            for col in range(len(grid[0])):
                grid[foldPlace - distance][col] = max(grid[foldPlace - distance][col], grid[foldPlace + distance][col])
        if foldType == 'x':
            for row in range(len(grid)):
                grid[row][foldPlace - distance] = max(grid[row][foldPlace - distance], grid[row][foldPlace + distance])

    if foldType == 'y':
        del grid[foldPlace:]
    if foldType == 'x':
        for row in range(len(grid)):
            del grid[row][foldPlace:]


def countDots(grid):
    dotCount = 0
    for line in grid:
        dotCount += sum(line)
    return dotCount


def foldAll(grid, folds):
    for entry in folds:
        fold(grid, entry.split('='))
        # print(countDots(grid))


coords, allFolds = readFile('input/day13.txt')
paperGrid = buildGrid(coords)
foldAll(paperGrid, allFolds)
for row in range(len(paperGrid)):
    for col in range(len(paperGrid[0])):
        if paperGrid[row][col] == 0:
            print(' ', end='')
        else:
            print('X', end='')
    print()
