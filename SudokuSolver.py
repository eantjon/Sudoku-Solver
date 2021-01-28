sboard = [
    [0,0,0,6,0,0,4,0,0],
    [7,0,0,0,0,3,6,0,0],
    [0,0,0,0,9,1,0,8,0],
    [0,0,0,0,0,0,0,0,0],
    [0,5,0,1,8,0,0,0,3],
    [0,0,0,3,0,6,0,4,5],
    [0,4,0,2,0,0,0,6,0],
    [9,0,3,0,0,0,0,0,0],
    [0,2,0,0,0,0,1,0,0]
]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            #Last element added does not solve the solution, therefore it is reset to 0 (backtracking)
            board[row][col] = 0

    return False

#Find empty square on the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def valid(board, num, pos):
    # Check if number is valid in row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # # Check if number is valid in column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
            
    # # Check if number is valid in 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

#Print the Sudoku board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


print_board(sboard)
solve(sboard)
print("________________________")
print("")
print_board(sboard)