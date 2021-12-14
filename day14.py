from collections import Counter

def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    starter = list(inputLines[0].strip())
    pairs = {}
    for row in range(len(inputLines)):
        if inputLines[row] == '\n':
            continue
        elif '->' in inputLines[row]:
            pair, insert = inputLines[row].strip('\n').split(' -> ')
            pair = tuple(pair)
            pairs[pair] = insert

    return starter, pairs


def stepOnce(line, substitutionRules):
    length = len(line)
    index = 0
    while index < length:
        pair = tuple(line[index:index+2])
        if pair in substitutionRules:
            line.insert(index+1, rules[pair])
            index += 1
            length += 1
        index += 1


def stepN(line, substitutionRules, N):
    for i in range(N):
        stepOnce(line, substitutionRules)




start, rules = readFile('input/day14.txt')
print(start, rules)
stepOnce(start, rules)
print(start)
stepN(start, rules, 9)
countDict = dict(Counter(start))
print(countDict)
countDict = dict(sorted(countDict.items(), key=lambda item: item[1]))
print(countDict)
dictKeys = list(countDict.keys())
print(countDict[dictKeys[-1]] - countDict[dictKeys[0]])
