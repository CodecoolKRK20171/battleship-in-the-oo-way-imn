from square import Square
from ocean import Ocean


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

    def add_squares_around_horizontal(self, square_around_list):
        self.square_around_list = square_around_list
        for i in range(size):
            self.ocean.board[position_y][position_x+i].ship()
            self.ocean.board[position_y][position_x+i].water()
            for j in range(len(square_around_list)):
                self.ocean.board[position_y + square_around_list[j][0]][position_x + square_around_list[j][1]].water()

    def add_squares_around_vertical(self, square_around_list):
        self.square_around_list = square_around_list
        for i in range(size):
            self.ocean.board[position_y+i][position_x].ship()
            self.ocean.board[position_y+i][position_x].water()
            for j in range(len(SQRS_ARND_SHIP)):
                self.ocean.board[position_y + SQRS_ARND_SHIP[j][0]][position_x + SQRS_ARND_SHIP[j][1]].water()

    def add_ship(self, position_x, position_y, size, is_horizontal):
        if is_horizontal:
            if position_x+size < 9 and position_y in range(1, 9):     # 9
                SQRS_ARND_SHIP = [[-1, 1],
                                  [0, 1],
                                  [1, 1],
                                  [1, 0],
                                  [1, -1],
                                  [0, -1],
                                  [-1, -1],
                                  [-1, 0]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

            elif position_x == 0 and position_y == 0:   # 1
                SQRS_ARND_SHIP = [[1, 0],
                                  [1, -1],
                                  [0, -1]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

            elif position_x+size < 9 and position_y == 0:     # 2
                SQRS_ARND_SHIP = [[1, 0],
                                  [1, -1],
                                  [0, -1],
                                  [-1, -1],
                                  [-1, 0]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

            elif position_x+size < 9 and position_y == 0:     # 3
                SQRS_ARND_SHIP = [[0, -1],
                                  [-1, -1],
                                  [-1, 0]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

            elif position_x+size == 9 and position_y in range(1, 9):     # 4
                SQRS_ARND_SHIP = [[-1, 1],
                                  [0, 1],
                                  [0, -1],
                                  [-1, -1],
                                  [-1, 0]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

            elif position_x+size == 9 and position_y == 9:     # 5
                SQRS_ARND_SHIP = [[-1, 1],
                                  [0, 1],
                                  [-1, 0]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

            elif position_x+size < 9 and position_y in range(1, 9):     # 6
                SQRS_ARND_SHIP = [[-1, 1],
                                  [0, 1],
                                  [1, 1],
                                  [1, 0],
                                  [-1, 0]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

            elif position_x == 0 and position_y == 9:     # 7
                SQRS_ARND_SHIP = [[0, 1],
                                  [1, 1],
                                  [1, 0]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

            elif position_x == 0 and position_y in range(1, 9):     # 8
                SQRS_ARND_SHIP = [[0, 1],
                                  [1, 1],
                                  [1, 0],
                                  [1, -1],
                                  [0, -1]]
                add_squares_around_horizontal(SQRS_ARND_SHIP)

        else:   # horizontal = False
            if position_x in range(1, 9) and position_y+size < 9:     # 9
                SQRS_ARND_SHIP = [[-1, 1],
                                  [0, 1],
                                  [1, 1],
                                  [1, 0],
                                  [1, -1],
                                  [0, -1],
                                  [-1, -1],
                                  [-1, 0]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

            elif position_x == 0 and position_y == 0:   # 1
                SQRS_ARND_SHIP = [[1, 0],
                                  [1, -1],
                                  [0, -1]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

            elif position_x in range(1, 9) and position_y+size < 9:     # 2
                SQRS_ARND_SHIP = [[1, 0],
                                  [1, -1],
                                  [0, -1],
                                  [-1, -1],
                                  [-1, 0]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

            elif position_x == 9 and position_y+size < 9:     # 3
                SQRS_ARND_SHIP = [[0, -1],
                                  [-1, -1],
                                  [-1, 0]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

            elif position_x == 9 and position_y+size < 9:     # 4
                SQRS_ARND_SHIP = [[-1, 1],
                                  [0, 1],
                                  [0, -1],
                                  [-1, -1],
                                  [-1, 0]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

            elif position_x == 9 and position_y+size == 9:     # 5
                SQRS_ARND_SHIP = [[-1, 1],
                                  [0, 1],
                                  [-1, 0]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

            elif position_x in range(1, 9) and position_y+size < 9:     # 6
                SQRS_ARND_SHIP = [[-1, 1],
                                  [0, 1],
                                  [1, 1],
                                  [1, 0],
                                  [-1, 0]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

            elif position_x == 0 and position_y+size < 9:     # 7
                SQRS_ARND_SHIP = [[0, 1],
                                  [1, 1],
                                  [1, 0]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

            elif position_x == 0 and position_y+size < 9:     # 8
                SQRS_ARND_SHIP = [[0, 1],
                                  [1, 1],
                                  [1, 0],
                                  [1, -1],
                                  [0, -1]]
                add_squares_around_vertical(SQRS_ARND_SHIP)

    def check_position(self, position_x, position_y, size, is_horizontal):
        checking_size = size + 2

        if is_horizontal:
            horizontal_position_x = position_x - 1
            for i in range(checking_size):
                if self.ocean.board[position_y][horizontal_position_x+i].is_water:
                    return False
                elif self.ocean.board[position_y+1][horizontal_position_x+i].is_water or self.ocean.board[position_y-1][horizontal_position_x+i].is_water:
                    return False
            return True
        else:
            horizontal_position_y = position_y - 1
            for i in range(checking_size):
                if self.ocean.board[horizontal_position_y+i][position_x].is_water:
                    return False
                elif self.ocean.board[horizontal_position_y+i][position_x+1].is_water or self.ocean.board[horizontal_position_y+i][position_x-1].is_water:
                    return False
            return True

# player1 = input('Enter your name: ')
# ocean1 = Ocean()
# ocean1.load_board()
# player = Player(player1, ocean1)

# player.add_ship(1, 5, 3, True)
# check = player.check_position(2, 5, 3, True)
# print(check)
# player.add_ship(4, 4, 3, False)
# player.shot(4, 4)
# player.shot(1, 5)
# player.shot(5, 1)
# print(ocean1)
