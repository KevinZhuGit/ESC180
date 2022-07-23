import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " + board[i][0] + " | " + board[i][1] + " | " + board[i][2]
        line2 = "  " + str(3*i+1) + " | " + str(3*i+2) + " | " + str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")


def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)  # creates list ["", "", ""]
    return board


def coords(n):
    return [((n - 1) // 3), ((n - 1) % 3)]  # row, column


def make_move(board, mark, square_num):
    coord = coords(square_num)

    board[coord[0]][coord[1]] = mark


def get_free_squares(board):
    available = []

    for m in range(3):
        for n in range(3):
            if board[m][n] == " ":
                available.append([m, n])

    return available


def make_random_move(board, mark):
    available = get_free_squares(board)

    coord = available[(random.randrange(len(available)))]

    board[coord[0]][coord[1]] = mark


def is_row_all_marks(board, row_i, mark):
    for n in range(3):
        if board[row_i][n] != mark:
            return False

    return True


def is_col_all_marks(board, col_i, mark):
    for m in range(3):
        if board[m][col_i] != mark:
            return False

    return True


def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark) or is_col_all_marks(board, i, mark):
            return True

    if board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    else:
        return False


def smart_computer(board):
    available = get_free_squares(board)
    temp_board = board

    # checks for winning move
    for i in available:
        temp_board[i[0]][i[1]] = 'O'
        if is_win(temp_board, 'O'):
            board[i[0]][i[1]] = 'O'
            return
        # need to delete since list aliasing issues
        temp_board[i[0]][i[1]] = ' '

    # checks against losing moves, should come after since winning take prio
    for i in available:
        temp_board[i[0]][i[1]] = 'X'
        if is_win(temp_board, 'X'):
            board[i[0]][i[1]] = 'O'
            return
        temp_board[i[0]][i[1]] = ' '

    make_random_move(board, 'O')


# memory model and updating
if __name__ == '__main__':
    board = make_empty_board()  # 3 empty rows
    print_board_and_legend(board)  # prints cur board and side board

    print("\n")

    turns = 0
    game_won = False

    while turns < 9 and game_won != True:
        if turns % 2 == 0:
            choice = int(input("Enter your move: "))
            make_move(board, 'X', choice)
        else:
            print("Computer's Move")
            smart_computer(board)

        print_board_and_legend(board)
        print("\n")

        if is_win(board, 'X'):
            game_won = True
            print("You won!")
        elif is_win(board, 'O'):
            game_won = True
            print("Computer won!")

        turns += 1

    '''
    # Problem 1: User vs User
    turns = 0

    while turns < 9:
        choice = int(input("Enter your move: "))

        if turns % 2 == 0:
            make_move(board, 'X', choice)
        else:
            make_move(board, 'O', choice)

        print_board_and_legend(board)
        print("\n")

        turns += 1

    '''

    '''Problem 2: User vs Computer
    turns = 0
    game_won = False
    
    while turns < 9 and game_won != True:
        if turns % 2 == 0:
            choice = int(input("Enter your move: "))
            make_move(board, 'X', choice)
        else:
            print("Computer's move")
            make_random_move(board, 'O')

        print_board_and_legend(board)
        print("\n")

        if is_win(board, 'X'):
            game_won = True
            print("You won!")
        elif is_win(board, 'O'):
            game_won = True
            print("Computer won!")

        turns += 1
    '''
