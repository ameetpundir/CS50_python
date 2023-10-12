class TicTacToeBoard:
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    def is_empty(self, row, col):
        return self.board[row][col] == '-'

    def mark_position(self, row, col, symbol):
        self.board[row][col] = symbol

    def is_winner(self, symbol):
        # Check rows
        for i in range(3):
            if self.board[i][0] == symbol and self.board[i][1] == symbol and self.board[i][2] == symbol:
                return True

        # Check columns
        for i in range(3):
            if self.board[0][i] == symbol and self.board[1][i] == symbol and self.board[2][i] == symbol:
                return True

        # Check diagonals
        if self.board[0][0] == symbol and self.board[1][1] == symbol and self.board[2][2] == symbol:
            return True
        elif self.board[0][2] == symbol and self.board[1][1] == symbol and self.board[2][0] == symbol:
            return True

        return False

    def is_full(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    return False

        return True

    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end=' ')
            print()


class TicTacToeGame:
    def __init__(self, players):
        self.board = TicTacToeBoard()
        self.players = players
        self.current_player = players[0]

    def play_turn(self):
        print('It is {}\'s turn'.format(self.current_player))

        while True:
            row = int(input('Enter a row (0-2): '))
            col = int(input('Enter a column (0-2): '))

            if not self.board.is_empty(row, col):
                print('The position is already filled. Please try again.')
            else:
                break

        self.board.mark_position(row, col, self.current_player)

    def switch_players(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def is_game_over(self):
        return self.board.is_full() or self.board.is_winner(self.current_player)

    def get_winner(self):
        if self.board.is_winner(self.players[0]):
            return self.players[0]
        elif self.board.is_winner(self.players[1]):
            return self.players[1]
        else:
            return None


def main():
    players = ['X', 'O']
    game = TicTacToeGame(players)

    while not game.is_game_over():
        game.play_turn()
        game.switch_players()

    winner = game.get_winner()

    if winner is not None:
        print('{} wins!'.format(winner))
    else:
        print('The game is a tie.')

    game.board.print_board()


if __name__ == '__main__':
    main()
