def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        lines = inputFile.readlines()

    maxCoord = 0

    for index, line in enumerate(lines):
        currentLine = []
        for coordinate in line.strip('\n').split(' -> '):
            for element in coordinate.split(','):
                element = int(element)
                if element > maxCoord:
                    maxCoord = element
                currentLine.append(int(element))
        lines[index] = currentLine

    return lines, maxCoord


# Draw line segment, given two points
# From Bresenham's line algorithm
# http://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
def drawLine(grid, x0, y0, x1, y1):

   dx = abs(x1-x0)
   dy = abs(y1-y0)

   sx = 1 if x0 < x1 else -1
   sy = 1 if y0 < y1 else -1

   err = dx - dy

   while True:
     grid[x0][y0] += 1

     if (x0 == x1) and (y0 == y1):
       break

     e2 = 2 * err
     if e2 > -dy:
       err = err - dy
       x0 = x0 + sx

     if (x0 == x1) and (y0 == y1):
       grid[x0][y0] += 1
       break

     if (e2 <  dx):
       err = err + dx
       y0 = y0 + sy


def buildGrid(coordinateList, maxCoord):
    # initialize grid to 0s
    grid = [[0]*(maxCoord+1) for i in range(maxCoord+1)]

    for line in coordinateList:
        # vertical line
        if line[0] == line[2]:
            if line[1] < line[3]:
                y1 = line[1]
                y2 = line[3]
            elif line[1] >= line[3]:
                y1 = line[3]
                y2 = line[1]

            for y in range(y1, y2+1):
                grid[line[0]][y] += 1
        # horizontal line
        elif line[1] == line[3]:
            if line[0] < line[2]:
                x1 = line[0]
                x2 = line[2]
            elif line[0] >= line[2]:
                x1 = line[2]
                x2 = line[0]
            for x in range(x1, x2+1):
                grid[x][line[1]] += 1
        # diagonal lines
        else:
            drawLine(grid, line[0], line[1], line[2], line[3])

    return grid


def countGrid(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] >= 2:
                count += 1
    return count

lines, maxCoord = readFile('input/day05.txt')
grid = buildGrid(lines, maxCoord)
count = countGrid(grid)
print(count)
