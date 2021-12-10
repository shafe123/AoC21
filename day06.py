def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLine = inputFile.readline().strip('\n')

    fishDict = {}
    for val in range(9):
        fishDict[val] = 0
    for val in inputLine.split(','):
        fishDict[int(val)] += 1

    return fishDict


def stepDay(inputFish):
    day0 = inputFish[0]
    for val in range(8):
        inputFish[val] = inputFish[val+1]
    inputFish[6] += day0
    inputFish[8] = day0


def stepDays(inputFish, numDays):
    for i in range(numDays):
        stepDay(inputFish)


inputFish = readFile('input/day06.txt')
print(inputFish)
stepDays(inputFish, 1)
print(inputFish)
stepDays(inputFish, 1)
print(inputFish)
stepDays(inputFish, 1)
print(inputFish)
stepDays(inputFish, 1)
print(inputFish)
stepDays(inputFish, 252)
print(inputFish)
fishCount = 0
for i in range(9):
    fishCount += inputFish[i]
print(fishCount)
