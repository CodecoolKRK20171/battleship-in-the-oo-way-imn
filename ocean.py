from ship import Ship


class Ocean:

    def __init__(self):
        self.ships = []
        self.board = []

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

    def fill_board(self):
        self.board.append('ABCDEFGHIJ')
        for i in range(0, 10):
            self.board.append([' ']*10 + [str(i+1)])

        for ship in self.ships:
            for square in ship.squares:
                self.board[square.column][square.row] = str(square)
