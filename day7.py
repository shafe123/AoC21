import statistics

def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLine = inputFile.readline().strip('\n')

    crabs = []
    for val in inputLine.split(','):
        crabs.append(int(val))

    return crabs


def fuelUsage(crabs, location):
    fuelSum = 0
    for position in crabs:
        fuelSum += abs(position - location)
    return fuelSum

crabList = readFile('input/day7.txt')
print(crabList)
mean = statistics.mean(crabList)
median = statistics.median(crabList)
print(round(mean))
print(fuelUsage(crabList, round(mean)))
print(median)
print(fuelUsage(crabList, median))


