from __future__ import print_function

startingBoard = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True
            board[row][column] = 0
    return False

def valid(board, number, position):

    # check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check box
    box_X = position[1] // 3
    box_Y = position[0] // 3

    for i in range(box_Y * 3, box_Y * 3 + 3):
        for j in range(box_X * 3, box_X * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


def printBoard(board):
    for i in range(len(startingBoard)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

printBoard(startingBoard)
solve(startingBoard)
print("_____________________")
print("")
printBoard(startingBoard)