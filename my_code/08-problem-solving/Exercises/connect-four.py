### Connect Four the Game 

print("Welcome to Connect Four")

# TODO: 

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
    row = 0 
    column = int(input("Choose which column:"))
    column -= 1
    if column <0 or column >= len(board[0]):
        return False

    cell = board[row][column]

    if cell is not None:
        row += 1
        cell = board[row][column]
        if row >6:
            return False
    

    board[row][column] = symbol
    return True


def show_board(board):
    display_board = board[::-1]
    for row in display_board:
        #row.reverse()
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

    # Win by rows
    rows = board
    sequences.extend(rows)

    # Win by columns
    for col_index in range(0, 3):  # start in inclusive while stop is exclusive in range function
        col = [
            board[0][col_index],
            board[1][col_index],
            board[2][col_index],
        ]
        sequences.append(col)

    #Win by diagonals
    diagonals = [
        [board[0][0],board[1][1],board[2][2]],
        [board[0][2],board[1][1],board[2][0]]
    ]
    sequences.extend(diagonals)
    return sequences

if __name__ == '__main__':
    main()
