import time
import sys
start = 0
end = 0


def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    global end
    end = time.time()
    print("Total time: ", end - start)


''' A utility function to check if a queen can be placed on board[row][col]. Note that this 
function is called when "col" queens are already placed in columns from 0 to col -1. 
So we need to check only left side for attacking queens '''


def isSafe(board, row, col, N):
    # Look for queens in the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, column, N):
    # base case: If all queens are placed then return true
    if column >= N:
        return True

    # Consider this column and try placing this queen in all rows in this column one by one
    for row in range(N):

        if isSafe(board, row, column, N):

            # Place this queen in board[i][col]
            board[row][column] = 1

            # recur to place rest of the queens
            if solveNQUtil(board, column + 1, N):
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[row][column] = 0

    # if the queen can not be placed in any row in this column col then return false
    return False


''' This function solves the N Queen problem using Backtracking. It mainly uses solveNQUtil() to solve the problem.
It returns false if queens cannot be placed, otherwise return true and placement of queens in the form of 1s. note that 
there may be more than one solutions, this function prints one of the feasible solutions. '''


def simpleBackTrackingSolver(boardSize):
    # setting up the board
    board = [[0 for i in range(boardSize)]
             for j in range(boardSize)]
    # solution does not exist
    global start
    start = time.time()
    if not solveNQUtil(board, 0, boardSize):
        print("Solution does not exist")
        return False
    # print the solution if it exists
    printSolution(board, boardSize)
    return True


def get_simpleBackTrackingSolver_result(boardSize):
    board = [[0 for i in range(boardSize)]
             for j in range(boardSize)]
    global start
    start = time.time()
    if not solveNQUtil(board, 0, boardSize):
        return []
    # print the solution if it exists
    printSolution(board, boardSize)

    result = []
    for l in board:
        result.append(l.index(1))
    return result


#simpleBackTrackingSolver(5)

#print(get_simpleBackTrackingSolver_result(5))