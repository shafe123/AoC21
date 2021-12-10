def readFile(inputLocation):
    with open(inputLocation, 'r') as inputFile:
        lines = inputFile.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.strip('\n')

    return lines


def buildBoards(lines):
    boards = []

    counter = 0
    currentBoard = []
    for line in lines:
        if len(line) == 0:
            continue
        if counter % 5 == 0:
            if len(currentBoard) > 0:
                boards.append(currentBoard.copy())
            currentBoard = []

        currentBoard.append([int(entry) for entry in line.split()])
        counter += 1

    return boards


def checkRows(board):
    for row in board:
        if sum(row) == 0:
            return True
    return False


def checkCols(board):
    for col in range(5):
        sum = 0
        for row in range(5):
            sum += board[row][col]
        if sum == 0:
            return True

    return False


def processNumbers(boards, order):
    winningNumbers = []
    winningBoards = []
    for number in order:
        for board in range(len(boards)):
            if board not in winningBoards:
                for row in range(5):
                    for entry in range(5):
                        if boards[board][row][entry] == number:
                            boards[board][row][entry] = 0

        for board in range(len(boards)):
            if board not in winningBoards and (checkRows(boards[board]) or checkCols(boards[board])):
                winningBoards.append(board)
                winningNumbers.append(number)
            else:
                continue

    return winningBoards, winningNumbers


def sumBoard(board):
    boardSum = 0
    for row in range(5):
        for col in range(5):
            boardSum += board[row][col]

    return boardSum


lines = readFile('input/day04.txt')
print(lines)

order = [int(number) for number in lines[0].split(',')]
boardLines = lines[1:]
boards = buildBoards(boardLines)

winningBoards, winningNumbers = processNumbers(boards.copy(), order)
winningBoard = winningBoards[-1]
winningSum = sumBoard(boards[winningBoard])
winningNumber = winningNumbers[-1]

print(winningNumber, winningSum, winningNumber * winningSum)


