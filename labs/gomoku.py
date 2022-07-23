def is_empty(board):
    '''
    returns true if board is empty, false if not empty
    '''

    for i in board:
        if i != [" "]*len(board):
            return False

    return True


def is_full(board):
    '''
    retursn true if board is full
    '''

    for i in board:
        if " " in i:
            return False

    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    '''
    determines if a sequence is open, semiopen, or closed
    for specific sequence length, direction, end point
    '''

    end = [y_end + d_y, x_end + d_x]
    start = [y_end - length * d_y, x_end - length * d_x]

    # check if position goes beyond board, check if beside is not ' '
    if is_open(board, end) and is_open(board, start):
        return "OPEN"
    elif is_open(board, end) or is_open(board, start):
        return "SEMIOPEN"
    else:
        return "CLOSED"


def is_open(board, position):

    if max(position) <= 7 and min(position) >= 0:
        if board[position[0]][position[1]] == " ":
            return True

    return False


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    '''
    starts at border and checks row in direction d_y, d_x
    finds number of open and semi open sequences equal to length
    '''
    open_seq_count = 0
    semi_open_seq_count = 0

    y = y_start
    x = x_start
    cur_length = 0

    while max(y, x) <= 7 and min(y, x) >= 0:
        if board[y][x] == col:
            cur_length += 1
        else:
            cur_length = 0

        if cur_length == length and sequence_end(board, col, y, x, d_y, d_x):
            if is_bounded(board, y, x, length, d_y, d_x) == "OPEN":
                open_seq_count += 1
            elif is_bounded(board, y, x, length, d_y, d_x) == "SEMIOPEN":
                semi_open_seq_count += 1

        y += d_y
        x += d_x

    return open_seq_count, semi_open_seq_count


def sequence_end(board, col, y, x, d_y, d_x):
    if max(y + d_y, x + d_x) <= 7 and min(y + d_y, x + d_x) >= 0:
        if board[y + d_y][x + d_x] == col:
            return False
        else:
            return True

    return True


def detect_rows(board, col, length):
    '''
    Checks every row on board, finds number of open and semiopen seq of len for col
    '''
    open_seq_count, semi_open_seq_count = 0, 0

    for start in range(8):
        horizontal = detect_row(board, col, start, 0, length, 0, 1)
        vertical = detect_row(board, col, 0, start, length, 1, 0)
        top_left_diag = detect_row(board, col, 0, start, length, 1, 1)
        bot_left_diag = detect_row(board, col, start, 0, length, 1, 1)
        top_right_diag = detect_row(board, col, 0, start, length, 1, -1)
        bot_right_diag = detect_row(board, col, start, 7, length, 1, -1)

        open_seq_count += horizontal[0] + vertical[0] + top_left_diag[0] + \
            bot_left_diag[0] + top_right_diag[0] + bot_right_diag[0]

        semi_open_seq_count += horizontal[1] + vertical[1] + top_left_diag[1] + \
            bot_left_diag[1] + top_right_diag[1] + bot_right_diag[1]

    # for overlap in diagnols
    overlap_top_left = detect_row(board, col, 0, 0, length, 1, 1)
    overlap_top_right = detect_row(board, col, 0, 7, length, 1, -1)

    open_seq_count -= overlap_top_left[0] + overlap_top_right[0]
    semi_open_seq_count -= overlap_top_left[1] + overlap_top_right[1]

    return open_seq_count, semi_open_seq_count


def search_max(board):
    '''
    find position that maximizes score
    '''
    max_score = -100001
    positions = open_positions(board)
    move_y = None
    move_x = None

    for place in positions:
        board[place[0]][place[1]] = "b"

        if score(board) > max_score:
            move_y, move_x = place[0], place[1]
            max_score = score(board)

        board[place[0]][place[1]] = " "

    return move_y, move_x


def open_positions(board):
    '''
    returns list of all open positions
    '''

    positions = []

    for m in range(8):
        for n in range(8):
            if board[m][n] == ' ':
                positions.append([m, n])

    return positions


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    '''
    Returns current status of game: White won, Black won, Draw, Continue playing
    '''
    # DOES NOT ACCOUNT FOR CLOSED SEQUENCE WINS

    for start in range(8):
        for col in ['w', 'b']:
            if detect_row_win(board, col, start, 0, 0, 1) or detect_row_win(board, col, 0, start, 1, 0) or detect_row_win(board, col, 0, start, 1, 1) \
                    or detect_row_win(board, col, start, 0, 1, 1) or detect_row_win(board, col, 0, start, 1, -1) or detect_row_win(board, col, start, 7, 1, -1):
                if col == 'w':
                    return 'White won'
                else:
                    return 'Black won'

    return 'Continue playing'


def detect_row_win(board, col, y_start, x_start, d_y, d_x):
    '''
    starts at border and checks row in direction d_y, d_x
    finds if there is a winning sequence, >5 does not count
    '''

    y = y_start
    x = x_start
    cur_length = 0

    while max(y, x) <= 7 and min(y, x) >= 0:
        if board[y][x] == col:
            cur_length += 1
        else:
            cur_length = 0

        if cur_length == 5 and sequence_end(board, col, y, x, d_y, d_x):
            return True

        y += d_y
        x += d_x

    return False


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i % 10) + "|"
    s += str((len(board[0])-1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 5
    y = 1
    d_x = -1
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 2
    y = 5
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, 2, length, d_y, d_x) == (0, 1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)

    put_seq_on_board(board, 3, 3, 1, 1, 1, "w")
    put_seq_on_board(board, 4, 4, 1, 1, 2, "b")
    print_board(board)
    if detect_rows(board, 'b', 2) == (0, 1):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5
    y = 0
    d_x = 0
    d_y = 1
    length = 4
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6
    y = 0
    d_x = 0
    d_y = 1
    length = 4
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4, 6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")


def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5
    x = 2
    d_x = 0
    d_y = 1
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3
    x = 5
    d_x = -1
    d_y = 1
    length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5
    x = 3
    d_x = -1
    d_y = 1
    length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


if __name__ == '__main__':
    play_gomoku(8)
    # some_tests()  # Passed
    # test_is_empty()        PASSED
    # test_is_bounded()      PASSED
    # test_detect_row()  # PASSED
    # test_detect_rows()
    # test_search_max()      NEEDS MORE TESTS
    # easy_testset_for_main_functions()
