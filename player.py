from ship import Ship
from square import Square
from ocean import Ocean


class Player:
    def __init__(self, name, ocean):
        self.name = name
        self.ocean = ocean

    def shot(self, position_x, position_y):
        self.ocean.board[position_y][position_x].un_hide()

    def add_ship(self, position_x, position_y, size, is_horizontal):
        if is_horizontal:
            for i in range(size):
                self.ocean.board[position_y][position_x+i].ship()
        else:
            for i in range(size):
                self.ocean.board[position_y+i][position_x].ship()
