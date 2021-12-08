def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    left = []
    right = []
    for line in inputLines:
        sides = line.split(' | ')
        left.append(sides[0].split())
        right.append(sides[1].split())

    return left, right


def countWordLength(segmentList):
    countByLength = {}
    for i in range(8):
        countByLength[i] = 0

    for line in segmentList:
        for word in line:
            countByLength[len(word)] += 1

    return countByLength


leftLines, rightLines = readFile('input/day8.txt')
print(leftLines)
print(rightLines)
lengthCounts = countWordLength(rightLines)
print(lengthCounts)
# 1 + 7 + 4 + 8
print(lengthCounts[2] + lengthCounts[3] + lengthCounts[4] + lengthCounts[7])
