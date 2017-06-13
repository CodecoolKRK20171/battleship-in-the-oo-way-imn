from ship import Ship

class Ocean:

    def __init__(self):
        self.ships = []
        self.board = []

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.board])

    def add_ship(self, position_x, position_y, size, is_horizontal=False):
        positions = []

        for i in range(size):
            if is_horizontal:
                position_x += 1
            else:
                position_y += 1
            positions.append((position_x, position_y))

        positions = tuple(positions)
        self.ships.append(Ship(positions))
        

    def fill_board(self):
        for i in range(0,10):
            self.board.append([' ']*10)


        for ship in self.ships:
            for square in ship.squares:
                self.board[square.column][square.row] = str(square)