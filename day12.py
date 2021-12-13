def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    for row in range(len(inputLines)):
        inputLines[row] = inputLines[row].strip('\n').split('-')

    return inputLines


def buildPath(currentPath, allPaths, pathMap):
    currentNode = currentPath[-1]

    if currentNode not in pathMap:
        return

    for entry in pathMap[currentNode]:
        if entry.islower() and entry in currentPath:
            continue
        elif entry == 'end':
            newPath = currentPath.copy()
            newPath.append(entry)
            allPaths.append(newPath)
        else:
            newPath = currentPath.copy()
            newPath.append(entry)
            buildPath(newPath, allPaths, pathMap)

    return


def buildMap(inputList):
    mapping = {}

    for pair in inputList:
        if pair[0] not in mapping:
            mapping[pair[0]] = []
        mapping[pair[0]].append(pair[1])

    # build reverse mapping as well

    mapKeys = list(mapping.keys())
    for index in mapKeys:
        for entry in mapping[index]:
            if entry not in mapping:
                mapping[entry] = []
            if index not in mapping[entry]:
                mapping[entry].append(index)

    return mapping


mapList = readFile('input/day12.txt')
mapDict = buildMap(mapList)

foundPaths = []
buildPath(['start'], foundPaths, mapDict)
print(foundPaths)
print(len(foundPaths))
