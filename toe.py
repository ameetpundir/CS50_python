# Tic-Tac-Toe Game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Main function to play the game


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_idx = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player_idx]}'s turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        # Check if the chosen cell is empty
        if board[row][col] == " ":
            board[row][col] = players[current_player_idx]
            # Check if the current player has won
            if check_winner(board, players[current_player_idx]):
                print_board(board)
                print(
                    f"Player {players[current_player_idx]} wins! Congratulations!")
                break
            # Switch to the next player
            current_player_idx = 1 - current_player_idx
        else:
            print("This cell is already occupied. Choose another one.")


# Run the game
if __name__ == "__main__":
    tic_tac_toe()
