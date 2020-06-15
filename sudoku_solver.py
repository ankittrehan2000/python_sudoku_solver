#find the position of the item on the board
def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return False


#print board to look better
def print_board(board):
    for i in range(len(board)):
        if (i % 3 == 0) and (i != 0):
            print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(len(board[i])):
            if j % 3 == 0 and (j != 0):
                #end so that we do not go to the next line
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]), end=" ")



#backtracker function recursive
def backtracker(board):
    #base case - see if the board is full
    if not find_zero(board):
        return True
    else:
        row, column = find_zero(board)

    #try values from 1 to 10
    for num in range(1, 10):
        #check if the number will be valid for the position
        if checker(board, num, (row, column)):
            #replace the item on that position if that is true
            board[row][column] = num

            #recursively try to finish the solution and if it works return true
            if backtracker(board):
                return True

            #if it does not solve then set it back to 0 and try with a different number
            board[row][column] = 0
    return False


#checker for every element
def checker(board, value, position):
    #check row
    for i in range(len(board[0])):
        #check if there are any of them in the row from position and ignore if it is because of the column we just inserted
        if board[position[0]][i] == value and position[1] != i:
            return False

    #for column
    for i in range(len(board)):
        #check if there are any of them in every sub list in the list using the postion tuple and ignore if it is the same as the row value from the position
        if board[i][position[1]] == value and position[0] != i:
            return False

    #check a small grid
    #break each grid into boxes and integer divide to find the value
    box_row = position[1] // 3
    box_column = position[0] // 3

    #multiply again to find the values
    for i in range(box_column * 3, box_column * 3 + 3):
        for j in range(box_row * 3, box_row * 3 + 3):
            #check to see that we do not equate to the position just inserted
            if board[i][j] == value and (i, j) != position:
                return False

    return True

sudoku_board = [[5, 1, 7, 6, 0, 0, 0, 3, 4], [2, 8, 9, 0, 0, 4, 0, 0, 0],
                [3, 4, 6, 2, 0, 5, 0, 9, 0], [6, 0, 2, 0, 0, 0, 0, 1, 0],
                [0, 3, 8, 0, 0, 6, 0, 4, 7], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 7, 8], [7, 0, 3, 4, 0, 0, 5, 6, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

if __name__ == "__main__":
    board = input("Enter sudoku board ")
    if not board == '':
        sudoku_board = board
    print("Original Board was")
    print_board(sudoku_board)
    backtracker(sudoku_board)
    print("\nSolved Board\n")
    print_board(sudoku_board)
