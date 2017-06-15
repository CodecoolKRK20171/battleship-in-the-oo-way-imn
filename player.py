from square import Square
from ocean import Ocean

SQRS_ARND_SHIP = [[-1, 1],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [1, -1],
                    [0, -1],
                    [-1, -1],
                    [-1, 0]]

SQUARES_AROUND_SHIP = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]


class Player:
    def __init__(self, name, ocean):
        self.name = name
        self.ocean = ocean

    def shot(self, position_x, position_y):
        self.ocean.board[position_y][position_x].un_hide()
        if self.ocean.board[position_y][position_x].is_ship:
            print('Hit!')
            return True
        else:
            print('Miss!')
            return False

    def add_squares_around_horizontal(self, square_around_list, position_x, position_y, size, is_horizontal):
        for i in range(size):
            self.ocean.board[position_y][position_x+i].ship()

            for j in square_around_list:
                x = position_y + j[0]
                y = position_x + j[1] + i

                if x in range(0, 10) and y in range(0, 10):
                    self.ocean.board[x][y].water()

    def add_squares_around_vertical(self, square_around_list, position_x, position_y, size, is_horizontal):
        for i in range(size):
            self.ocean.board[position_y+i][position_x].ship()

            for j in square_around_list:
                x = position_y + j[0] + i
                y = position_x + j[1]

                if x in range(0, 10) and y in range(0, 10):
                    self.ocean.board[x][y].water()

    def add_ship(self, position_x, position_y, size, is_horizontal):
        if is_horizontal:
            self.add_squares_around_horizontal(SQUARES_AROUND_SHIP, position_x, position_y, size, is_horizontal)

        else:   # vertical (horizontal = False)
            self.add_squares_around_vertical(SQUARES_AROUND_SHIP, position_x, position_y, size, is_horizontal)

    def check_position(self, position_x, position_y, size, is_horizontal):
    

        if is_horizontal:

            for i in range(size):
                x = position_y 
                y = position_x + i
                if x in range(0, 10) and y in range(0, 10):
                    if self.ocean.board[x][y].is_water:
                        return False
                else:
                    return False
            return True

        else:

            for i in range(size):
                x = position_y + i
                y = position_x
                if x in range(0, 10) and y in range(0, 10):
                    if self.ocean.board[x][y].is_water:
                        return False
                else:
                    return False
            return True
