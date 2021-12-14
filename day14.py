import math
from collections import Counter

def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    firstLine = inputLines[0].strip()
    linePairs = {}
    for i in range(len(firstLine)-1):
        pair = firstLine[i:i+2]
        if pair in linePairs:
            linePairs[pair] += 1
        else:
            linePairs[pair] = 1

    rules = {}
    for row in range(len(inputLines)):
        if inputLines[row] == '\n':
            continue
        elif '->' in inputLines[row]:
            pair, insert = inputLines[row].strip('\n').split(' -> ')
            rules[pair] = insert

    return linePairs, rules


def stepOnce(lineDict, substitutionRules):
    newDict = {}

    for key in lineDict:
        if key in substitutionRules:
            newKey1 = key[0] + substitutionRules[key]
            newKey2 = substitutionRules[key] + key[1]

            if newKey1 in newDict:
                newDict[newKey1] += lineDict[key]
            else:
                newDict[newKey1] = lineDict[key]

            if newKey2 in newDict:
                newDict[newKey2] += lineDict[key]
            else:
                newDict[newKey2] = lineDict[key]
        else:
            if key in newDict:
                newDict[key] += lineDict[key]
            else:
                newDict[key] = lineDict[key]

    return newDict


def stepN(line, substitutionRules, N):
    nextStep = line.copy()
    for i in range(N):
        print("Processing step {}".format(i+1))
        nextStep = stepOnce(nextStep, substitutionRules)
        print(nextStep)
    return nextStep


def countLetters(line):
    countDict = {}
    for key in line.keys():
        for character in key:
            if character in countDict:
                countDict[character] += line[key]
            else:
                countDict[character] = line[key]

    for key in countDict.keys():
        countDict[key] = math.ceil(countDict[key]/2)
    return countDict


start, rules = readFile('input/day14.txt')
print(start, rules)

print("Processing step 0")
start = stepOnce(start, rules)
print(start)

start = stepN(start, rules, 9)

countDict = countLetters(start)
countDict = dict(sorted(countDict.items(), key=lambda item: item[1]))
print(countDict)
dictKeys = list(countDict.keys())
print(countDict[dictKeys[-1]] - countDict[dictKeys[0]])

start = stepN(start, rules, 30)

countDict = countLetters(start)
countDict = dict(sorted(countDict.items(), key=lambda item: item[1]))
print(countDict)
dictKeys = list(countDict.keys())
print(countDict[dictKeys[-1]] - countDict[dictKeys[0]])