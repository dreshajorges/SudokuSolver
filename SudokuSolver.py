board = [
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


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)

    return None


def is_valid(board, number, position):
    # row check
    for i in range(len(board)):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # column check
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # box check
    row_box = position[0] // 3
    column_box = position[1] // 3

    for i in range(row_box * 3, row_box * 3 + 3):
        for j in range(column_box * 3, column_box * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if is_valid(board, i, (row, column)):
            board[row][column] = i

            if solve_sudoku(board):
                return True
            else:
                board[row][column] = 0




print("this is the unsolved sudoku")
print_board(board)
print("###########################")
solve_sudoku(board)
print_board(board)
print("this is the solved sudoku")
