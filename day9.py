def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    grid = []
    for row in range(len(inputLines)):
        newRow = []
        for col in range(len(inputLines[row])):
            if inputLines[row][col] != '\n':
                newRow.append(int(inputLines[row][col]))
        grid.append(newRow)

    return grid


def checkLeft(grid, row, col):
    if col == 0:
        return True

    return grid[row][col-1] > grid[row][col]


def checkRight(grid, row, col):
    if col == len(grid[row]) - 1:
        return True

    return grid[row][col+1] > grid[row][col]


def checkUp(grid, row, col):
    if row == 0:
        return True

    return grid[row-1][col] > grid[row][col]


def checkDown(grid, row, col):
    if row == len(grid) - 1:
        return True

    return grid[row+1][col] > grid[row][col]


def findLows(grid):
    lowPoints = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if checkLeft(grid, row, col) and checkRight(grid, row, col) and \
                    checkUp(grid, row, col) and checkDown(grid, row, col):
                lowPoints.append((row, col))
    return lowPoints


def sumRiskLevel(grid, coords):
    result = 0
    for points in coords:
        result += grid[points[0]][points[1]]
    result += len(coords)
    return result


heightMap = readFile('input/day9.txt')
print(heightMap)
lows = findLows(heightMap)
print(lows)
risk = sumRiskLevel(heightMap, lows)
print(risk)