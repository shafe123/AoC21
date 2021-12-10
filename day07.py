import statistics
import math

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
        fuelSum += sum1toN(abs(position - location))
    return fuelSum


def sum1toN(N):
    return (N*(N+1))/2


crabList = readFile('input/day07.txt')
print(crabList)
mean = statistics.mean(crabList)
median = statistics.median(crabList)
print("mean:", math.floor(mean))
print(fuelUsage(crabList, math.floor(mean)))
print("median:", median)
print(fuelUsage(crabList, median))


