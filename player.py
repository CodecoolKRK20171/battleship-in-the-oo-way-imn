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

class Player:
    def __init__(self, name, ocean):
        self.name = name
        self.ocean = ocean

    def shot(self, position_x, position_y):
        self.ocean.board[position_y][position_x].un_hide()
        if self.ocean.board[position_y][position_x].is_ship:
            print('Hit!')
        else:
            print('Miss!')

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
            SQRS_ARND_SHIP = [[-1, 1],
                              [0, 1],
                              [1, 1],
                              [1, 0],
                              [1, -1],
                              [0, -1],
                              [-1, -1],
                              [-1, 0]]
            self.add_squares_around_horizontal(SQRS_ARND_SHIP, position_x, position_y, size, is_horizontal)

        else:   # horizontal = False
            SQRS_ARND_SHIP = [[-1, 1],
                              [0, 1],
                              [1, 1],
                              [1, 0],
                              [1, -1],
                              [0, -1],
                              [-1, -1],
                              [-1, 0]]
            self.add_squares_around_vertical(SQRS_ARND_SHIP, position_x, position_y, size, is_horizontal)

    def check_position(self, position_x, position_y, size, is_horizontal):
        checking_size = size + 2

        if is_horizontal:

            for i in range(size):
                x = position_y 
                y = position_x + i
                if x in range(0, 10) and y in range(0, 10):
                    if self.ocean.board[x][y].is_water:
                        return False
            return True

        else:

            for i in range(size):
                x = position_y + i
                y = position_x
                if x in range(0, 10) and y in range(0, 10):
                    if self.ocean.board[x][y].is_water:
                        return False
            return True


        
            
        #     for i in range(checking_size):
        #         if self.ocean.board[position_y][position_x+i].is_water:
        #             return False
        #         elif self.ocean.board[position_y+1][position_x+i].is_water or self.ocean.board[position_y-1][position_x+i].is_water:
        #             return False
        #     return True
        # else:
            
        #     for i in range(checking_size):
        #         if self.ocean.board[position_y+i][position_x].is_water:
        #             return False
        #         elif self.ocean.board[position_y+i][position_x+1].is_water or self.ocean.board[position_y+i][position_x-1].is_water:
        #             return False
        #     return True
