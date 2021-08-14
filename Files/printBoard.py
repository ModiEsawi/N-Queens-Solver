from random import choice


def printBoard(result):
    if not result:
        print([None])
    else:
        board = []
        for col in result:
            line = ['.'] * len(result)
            line[col] = 'Q'
            board.append(str().join(line))

        charlist = map(list, board)
        for line in charlist:
            print(" ".join(line))
    print("\n")
