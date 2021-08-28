### Tic Tac Toe
# TODO: Resume from Chapter 8 v9/15
print("Welcome to Play Tic Tac Toe")


# Create Board
# Choose Initial Player
# Until someone wins, check for winner
#   show the board
#   Get Moves from players, check validity of move, mark it
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

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]

        announce_turn(player)
        show_board(board)
        input("paused")

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
    return False

if __name__ == '__main__':
    main()
