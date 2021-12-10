import queue


def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        inputLines = inputFile.readlines()

    for row in range(len(inputLines)):
        inputLines[row] = inputLines[row].strip('\n')

    return inputLines


pointDict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

pointDict2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

delimiterDict = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

leftDelimiterDict = {value: key for key, value in delimiterDict.items()}

leftDelimiters = ['(', '[', '{', '<']
rightDelimiters = [')', ']', '}', '>']


def processLine(line):
    q = queue.LifoQueue()
    for character in line:
        if character in leftDelimiters:
            q.put(character)
        elif character in rightDelimiters:
            lastChar = q.get()
            if lastChar != delimiterDict[character]:
                return lastChar, character

    return '', ''


def autoComplete(line):
    q = queue.LifoQueue()
    for character in line:
        if character in leftDelimiters:
            q.put(character)
        elif character in rightDelimiters:
            lastChar = q.get()

    autoScore = 0
    while not q.empty():
        currentCharacter = q.get()
        matchingCharacter = leftDelimiterDict[currentCharacter]
        autoScore = autoScore * 5 + pointDict2[matchingCharacter]
    return autoScore


def processLines(allLines):
    errors = []
    incompleteScores = []

    for line in allLines:
        expected, got = processLine(line)
        if expected != '':
            errors.append((expected, got))
        else:
            incompleteScores.append(autoComplete(line))

    errorSum = 0
    for error in errors:
        errorSum += pointDict[error[1]]

    incompleteScores.sort()

    return errorSum, incompleteScores[int((len(incompleteScores)-1)/2)]


input = readFile('input/day10.txt')
print(processLines(input))
