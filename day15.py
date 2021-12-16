import math
from heapq import heappush, heappop


def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    grid = []
    for row in inputLines:
        line = []
        for character in row[0:-1]:
            line.append(int(character))
        grid.append(line)

    return grid


def calcHeuristic(currentCoordinate, goalCoordinate):
    # assuming the goal coordinate is always bigger than our current coordinate
    return (goalCoordinate[0] - currentCoordinate[0]) + (goalCoordinate[1] - currentCoordinate[1])


def calcBackPath(fromNode, backPath, startNode):
    pass


def aStar(map):
    maxX = len(map[0])-1
    maxY = len(map)-1

    goalCoord = (maxY, maxX)

    toVisit = []
    backPath = {}
    gScores = {}
    fScores = {}

    startCoord = (0, 0)
    gScore = 0
    hScore = calcHeuristic(startCoord, goalCoord)
    fScore = gScore + hScore
    gScores[startCoord] = gScore
    fScores[startCoord] = fScore
    heappush(toVisit, (fScore, startCoord))

    while len(toVisit) > 0:
        currentNode = heappop(toVisit)
        nodeCoord = currentNode[1]

        if nodeCoord == goalCoord:
            return fScores[nodeCoord]

        neighbors = []
        if nodeCoord[0] > 0:
            neighbors.append((nodeCoord[0]-1, nodeCoord[1]))
        if nodeCoord[0] < maxY:
            neighbors.append((nodeCoord[0]+1, nodeCoord[1]))
        if nodeCoord[1] > 0:
            neighbors.append((nodeCoord[0], nodeCoord[1]-1))
        if nodeCoord[1] < maxX:
            neighbors.append((nodeCoord[0], nodeCoord[1]+1))

        for neighbor in neighbors:
            newGScore = gScores[nodeCoord] + map[neighbor[0]][neighbor[1]]
            if neighbor not in gScores:
                gScores[neighbor] = math.inf
            if newGScore < gScores[neighbor]:
                gScores[neighbor] = newGScore
                fScores[neighbor] = newGScore + calcHeuristic(neighbor, goalCoord)
                backPath[neighbor] = nodeCoord

                found = False
                for node in toVisit:
                    if neighbor == node[1]:
                        found = True
                if not found:
                    heappush(toVisit, (fScores[neighbor], neighbor))


def tileHorizontally(map, n):
    maxX = len(map[0])
    maxY = len(map)
    newMap = [[0 for i in range(maxX*n)] for j in range(maxY)]
    for row in range(maxY):
        for col in range(maxX):
            newMap[row][col] = map[row][col]

    for iteration in range(0, n-1):
        previousCol = iteration*maxX
        nextCol = (iteration+1)*maxX
        for row in range(maxY):
            for col in range(maxX):
                newMap[row][nextCol + col] = newMap[row][previousCol + col] + 1
                if newMap[row][nextCol + col] == 10:
                    newMap[row][nextCol + col] -= 9

    return newMap


def tileVertically(map, n):
    maxX = len(map[0])
    maxY = len(map)
    newMap = [[0 for i in range(maxX)] for j in range(maxY*n)]
    for row in range(maxY):
        for col in range(maxX):
            newMap[row][col] = map[row][col]

    for iteration in range(0, n - 1):
        previousRow = iteration * maxY
        nextRow = (iteration + 1) * maxY
        for row in range(maxY):
            for col in range(maxX):
                newMap[nextRow + row][col] = newMap[previousRow + row][col] + 1
                if newMap[nextRow + row][col] == 10:
                    newMap[nextRow + row][col] -= 9

    return newMap


def tileMap(map, n):
    map = tileHorizontally(map, 5)
    map = tileVertically(map, 5)
    return map


mapGrid = readFile('input/day15.txt')
mapGrid = tileMap(mapGrid, 5)
finalCost = aStar(mapGrid)
print(finalCost)
