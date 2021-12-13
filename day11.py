def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    outputRows =[]
    for row in range(len(inputLines)):
        inputLines[row] = inputLines[row].strip('\n')
        newRow = []
        for character in inputLines[row]:
            newRow.append(int(character))
        outputRows.append(newRow)

    return outputRows


def flash(grid, row, col):
    # top row
    if row > 0:
        if col > 0:
            grid[row-1][col-1] += 1
        grid[row-1][col+0] += 1
        if col < len(grid[0])-1:
            grid[row-1][col+1] += 1

    #current row
    if col > 0:
        grid[row][col-1] += 1
    if col < len(grid[0])-1:
        grid[row][col+1] += 1

    #bottom row
    if row < len(grid)-1:
        if col > 0:
            grid[row+1][col-1] += 1
        grid[row+1][col] += 1
        if col < len(grid[0])-1:
            grid[row+1][col+1] += 1


def recurseFlash(grid, haveFlashed):
    toFlash = []
    synchronized = False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 9 and (row, col) not in haveFlashed:
                toFlash.append((row, col))

    if len(haveFlashed) == 100:
        synchronized = True

    if len(toFlash) == 0:
        for coord in haveFlashed:
            grid[coord[0]][coord[1]] = 0
        return len(haveFlashed), synchronized

    for coord in toFlash:
        flash(grid, coord[0], coord[1])

    # recurse
    haveFlashed.extend(toFlash)
    return recurseFlash(grid, haveFlashed)


def takeStep(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] += 1

    return recurseFlash(grid, [])


def takeSteps(grid,  numTimes):
    countFlashes = 0
    count = 0
    synched = False

    while not synched:
        newFlashes, synched = takeStep(grid)
        countFlashes += newFlashes
        count += 1

    print(count)

    return countFlashes


grid = readFile('input/day11.txt')
print(grid)
print(takeSteps(grid, 100))
print(grid)
