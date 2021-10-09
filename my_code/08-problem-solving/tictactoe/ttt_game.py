### Tic Tac Toe
# TODO: Resume from Chapter 8 v9/15
print("Welcome to Play Tic Tac Toe")


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
        [None, None, None],
        [None, None, None],
        [None, None, None],
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
    print(f"Game over {player} has won!")
    show_board(board)

def choose_location(board, symbol):
    row = int(input("Choose which row:"))
    column = int(input("Choose which column:"))

    row -= 1
    column -= 1
    if row <0 or row >= len(board):
        return False
    if column <0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
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
    # TODO: implement how we check for a winner
    # Win by rows
    rows = board
    for row in rows:
        symbol1 = row[0]
        if symbol1 and all(symbol1 == cell for cell in row):  # if this does not happen it will continue to WBC
            return True

    # Win by columns WBC
    columns = []
    for col_index in range(0,3):  # start in inclusive while stop is exclusive in range function
        col= [
            board[0][col_index],
            board[1][col_index],
            board[2][col_index],
        ]
        columns.append(col)

    for col in columns:
        symbol1 = col[0]
        if symbol1 and all(symbol1 == cell for cell in col):  # if this does not happen it will continue to WBD
            return True


    # Win by diagonals WBD
    diagonals = [
        [board[0][0],board[1][1],board[2][2]],
        [board[0][2],board[1][1],board[2][0]]
    ]
    for diag in diagonals:
        symbol1 = diag[0]
        if symbol1 and all(symbol1 == cell for cell in diag):  # if this does not happen it will continue to WBD
            return True

    return False

if __name__ == '__main__':
    main()
