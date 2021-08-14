import time
import sys
start = 0
end = 0
'''Print the solution for the N-queens puzzle'''


def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    global end
    end = time.time()
    print("Total time: ", end - start)


""" An Optimized function to check if a queen can be placed on the board in the [row][col] place """


def isSafe(row, col, slashMatrix, backslashMatrix, rowLookup, slashMatrixLookup, backslashMatrixLookup):
    if (slashMatrixLookup[slashMatrix[row][col]] or
            backslashMatrixLookup[backslashMatrix[row][col]] or
            rowLookup[row]):
        return False
    return True


""" A recursive utility function to solve N Queen problem """


def solveNQueensUtil(board, col, slashMatrix, backSlashMatrix,
                     rowLookup, slashMatrixLookup,
                     backslashMatrixLookup, N):
    # base case: If all queens are placed then return True
    if col >= N:
        return True
    for row in range(N):
        if isSafe(row, col, slashMatrix, backSlashMatrix, rowLookup, slashMatrixLookup, backslashMatrixLookup):

            # Place this queen on the board in [row][col] placement.
            board[row][col] = 1
            rowLookup[row] = True
            slashMatrixLookup[slashMatrix[row][col]] = True
            backslashMatrixLookup[backSlashMatrix[row][col]] = True

            # recur to place rest of the queens
            if (solveNQueensUtil(board, col + 1, slashMatrix, backSlashMatrix, rowLookup, slashMatrixLookup,
                                 backslashMatrixLookup, N)):
                return True

            ''' If placing a queen on the board in [row][col] placement doesn't lead to a solution,
              then backtrack and Remove the queen from board[row][col]'''
            board[row][col] = 0
            rowLookup[row] = False
            slashMatrixLookup[slashMatrix[row][col]] = False
            backslashMatrixLookup[backSlashMatrix[row][col]] = False

    # If queen can not be place in any row in this column col then return False
    return False


""" This function solves the N Queen problem using Branch or Bound. It mainly uses solveNQueensUtil()to 
solve the problem. It returns False if queens cannot be placed,otherwise return True or 
prints placement of queens in the form of 1s. Please note that there may be more than one 
solutions,this function prints one of the feasible solutions."""


def BranchAndBoundSolver(boardSize):
    board = [[0 for i in range(boardSize)]
             for j in range(boardSize)]
    # metrics for diagonal lookup
    slashMatrix = [[0 for i in range(boardSize)]
                   for j in range(boardSize)]
    backSlashMatrix = [[0 for i in range(boardSize)]
                       for j in range(boardSize)]

    # arrays to tell us which rows are occupied
    occupiedRows = [False] * boardSize

    # keep two arrays to tell us
    # which diagonals are occupied
    arraySize = 2 * boardSize - 1
    slashMatrixLookup = [False] * arraySize
    backslashMatrixLookup = [False] * arraySize

    # initialize helper matrices
    for row in range(boardSize):
        for column in range(boardSize):
            slashMatrix[row][column] = row + column
            backSlashMatrix[row][column] = row - column + (boardSize - 1)
    global start
    start = time.time()
    if not solveNQueensUtil(board, 0, slashMatrix, backSlashMatrix, occupiedRows, slashMatrixLookup,
                            backslashMatrixLookup, boardSize):
        print("Solution does not exist")
        return False

    # solution found
    printSolution(board, boardSize)
    return True


def get_BranchAndBound_result(boardSize):
    board = [[0 for i in range(boardSize)]
             for j in range(boardSize)]
    # metrics for diagonal lookup
    slashMatrix = [[0 for i in range(boardSize)]
                   for j in range(boardSize)]
    backSlashMatrix = [[0 for i in range(boardSize)]
                       for j in range(boardSize)]

    # arrays to tell us which rows are occupied
    occupiedRows = [False] * boardSize

    # keep two arrays to tell us
    # which diagonals are occupied
    arraySize = 2 * boardSize - 1
    slashMatrixLookup = [False] * arraySize
    backslashMatrixLookup = [False] * arraySize

    # initialize helper matrices
    for row in range(boardSize):
        for column in range(boardSize):
            slashMatrix[row][column] = row + column
            backSlashMatrix[row][column] = row - column + (boardSize - 1)
    global start
    start = time.time()
    if not solveNQueensUtil(board, 0, slashMatrix, backSlashMatrix, occupiedRows, slashMatrixLookup,
                            backslashMatrixLookup, boardSize):
        return []

    # solution found
    result = []
    for l in board:
        result.append(l.index(1))
    return result

