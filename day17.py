def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    line = inputLines[0].strip()
    line = line[13:].split(', ')
    xBounds = list(map(int, line[0][2:].split('..')))
    yBounds = list(map(int, line[1][2:].split('..')))
    return xBounds, yBounds


def tryShot(initialX, initialY, xBound, yBound):
    xVelocity = initialX
    yVelocity = initialY
    xPos = 0 + xVelocity
    yPos = 0 + yVelocity
    yMax = max(0, yPos)

    while True:
        xVelocity = max(0, xVelocity - 1)
        yVelocity -= 1

        xPos += xVelocity
        yPos += yVelocity

        if yPos > yMax:
            yMax = yPos

        if xBound[0] <= xPos <= xBound[1] and \
                yBound[0] <= yPos <= yBound[1]:
            return True, yMax

        if xPos > xBound[1] or yPos < yBound[0]:
            return False, yMax


def bruteForce(xBounds, yBounds):
    maxHeights = []
    for xVel in range(1 ,1000):
        for yVel in range(-10, 1000):
            worked, yMax = tryShot(xVel, yVel, xBounds, yBounds)
            if worked:
                maxHeights.append(yMax)

    return max(maxHeights)

xb, yb = readFile('input/day17.txt')
print(xb, yb)
print(bruteForce(xb, yb))