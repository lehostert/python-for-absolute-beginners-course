### Connect Four the Game 
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Welcome to Connect Four ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# TODO: Review lines 185- 192 for why they cause a special break
# TODO: Add diagonals for up-to-down direction.
# TODO: Add random number generator for computer plays

# Create the board
# Establish Players
# Players Take turns
# Record Turn
# Check for winner

# Create Board
# Choose Initial Player
# Until someone wins, check for winner
#   show the board
#   Get Moves from players (choose a location), check validity of move, mark it
#   Change active player
# Game Over

def main():
# CREATE THE BOARD
    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    # board = None
    # board[0]
    # board = [
    #     [r1_c1, r1_c2, r1_c3],
    #     [r2_c1, r2_c2, r2_c3],
    #     [r3_c1, r3_c2, r3_c3],
    # ]

     # r2_c3 = board[1][2]

    # CHOOSE THE INITIAL PLAYER
    active_player_index = 0
    p1 = input("Enter player 1's name: ")
    players = [p1, "Computer"]
    symbols = ["X", "0"]
    player = players[active_player_index]

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue

        # Toggle Active Player
        active_player_index = (active_player_index + 1) % len(players)
    print()
    print(f"Congratulations, {player} has won the game!")
    show_board(board)
    print()


def choose_location(board, symbol):
    row = 5 
    column = int(input("Choose which column:"))
    column -= 1
    if column <0 or column >= len(board[0]):
        return False

    cell = board[row][column]

    while cell is not None:
        row -= 1
        cell = board[row][column]
        if row <0:
            return False
    
    board[row][column] = symbol
    return True


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print("")
    print(f"It's {player}'s turn. Here is the board:")
    print("")


def find_winner(board):
    sequences = get_winning_sequences(board)
    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):  # If this does not happen continue & Return FALSE
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # Win by row C4
    for row_index in range(0, 6):  # start in inclusive while stop is exclusive in range function
        row1 = [
            board[row_index][0],
            board[row_index][1],
            board[row_index][2],
            board[row_index][3],
        ]
        sequences.append(row1)

    for row_index in range(0, 6):  # start in inclusive while stop is exclusive in range function
        row2 = [
            board[row_index][1],
            board[row_index][2],
            board[row_index][3],
            board[row_index][4],
        ]
        sequences.append(row2)

    for row_index in range(0, 6):  # start in inclusive while stop is exclusive in range function
        row3 = [
            board[row_index][2],
            board[row_index][3],
            board[row_index][4],
            board[row_index][5],
        ]
        sequences.append(row3)

    for row_index in range(0, 6):  # start in inclusive while stop is exclusive in range function
        row4 = [
            board[row_index][3],
            board[row_index][4],
            board[row_index][5],
            board[row_index][6],
        ]
        sequences.append(row4)

    # Win by columns C4
    for col_index in range(0, 7):  # start in inclusive while stop is exclusive in range function
        col1 = [
            board[0][col_index],
            board[1][col_index],
            board[2][col_index],
            board[3][col_index],
        ]
        sequences.append(col1)

    for col_index in range(0, 7):  # start in inclusive while stop is exclusive in range function
        col2 = [
            board[1][col_index],
            board[2][col_index],
            board[3][col_index],
            board[4][col_index],
        ]
        sequences.append(col2)

    for col_index in range(0, 7):  # start in inclusive while stop is exclusive in range function
        col3 = [
            board[2][col_index],
            board[3][col_index],
            board[4][col_index],
            board[5][col_index],
        ]
        sequences.append(col3)

    #Win by diagonals
    # TODO: Why doesn't this work? It causing code to break with a winner after inputing someones name but no play
    # for diag_index in range(0, 4):  # start in inclusive while stop is exclusive in range function
    #     diag= [
    #         [board[3][diag_index], board[2][diag_index + 1], board[1][diag_index + 2], board[0][diag_index + 3]],
    #         [board[4][diag_index], board[3][diag_index + 1], board[2][diag_index + 2], board[1][diag_index + 3]],
    #         [board[5][diag_index], board[4][diag_index + 1], board[3][diag_index + 2], board[2][diag_index + 3]]
    #     ]
    #     sequences.append(diag)


    diagonals = [
        [board[3][0],board[2][1],board[1][2],board[0][3]],
        [board[4][0],board[3][1],board[2][2],board[1][3]],
        [board[5][0],board[4][1],board[3][2],board[2][3]],

        [board[3][1], board[2][2], board[1][3], board[0][4]],
        [board[4][1], board[3][2], board[2][3], board[1][4]],
        [board[5][1], board[4][2], board[3][3], board[2][4]],

        [board[3][2], board[2][3], board[1][4], board[0][5]],
        [board[4][2], board[3][3], board[2][4], board[1][5]],
        [board[5][2], board[4][3], board[3][4], board[2][5]],

        [board[3][3], board[2][4], board[1][5], board[0][6]],
        [board[4][3], board[3][4], board[2][5], board[1][6]],
        [board[5][3], board[4][4], board[3][5], board[2][6]],
    ]
    sequences.extend(diagonals)
    return sequences

if __name__ == '__main__':
    main()
