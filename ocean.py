from square import Square


class Ocean:
    def __init__(self):
        self.ships = []
        self.board = []

    def __str__(self):
        ocean_str = ' ABCDEFGHIJ\n'
        i = -1
        for lista in self.board:
            i += 1
            ocean_str += str(i)
            for item in lista:
                ocean_str += str(item)
            ocean_str += '\n'
        return ocean_str

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

    def load_board(self):
        for i in range(0, 10):
            self.board.append([])
            for j in range(0, 10):
                self.board[i].append(Square(i, j))
