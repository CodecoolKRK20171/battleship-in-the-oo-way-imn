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

    def add_ship(self, position_x, position_y, size, is_horizontal):


        if is_horizontal:
            if position_x+size < 9 and position_y == 0:     # 9
                SQUARES_AROUND_SHIP = [[-1, 1],
                                       [0, 1],
                                       [1, 1],
                                       [1, 0],
                                       [1, -1],
                                       [0, -1],
                                       [-1, -1],
                                       [-1, 0]]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()


            elif position_x == 0 and position_y == 0:   # 1
                SQUARES_AROUND_SHIP = [[1, 0],
                                       [1, -1],
                                       [0, -1]]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()

            elif position_x+size < 9 and position_y == 0:     # 2
                SQUARES_AROUND_SHIP = [[1, 0],
                                       [1, -1],
                                       [0, -1],
                                       [-1, -1],
                                       [-1, 0]]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()

            elif position_x+size == 9 and position_y == 0:     # 3
                SQUARES_AROUND_SHIP = [[0, -1],
                                       [-1, -1],
                                       [-1, 0]]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()

            elif position_x+size == 9 and position_y in range(1, 9):     # 4
                SQUARES_AROUND_SHIP = [[-1, 1],
                                       [0, 1],
                                       [0, -1],
                                       [-1, -1],
                                       [-1, 0]]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()

            elif position_x+size == 9 and position_y == 9:     # 5
                SQUARES_AROUND_SHIP = [[-1, 1],
                                       [0, 1],
                                       [-1, 0]]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()

            elif position_x+size < 9 and position_y in range(1, 9):     # 6
                SQUARES_AROUND_SHIP = [[-1, 1],
                                       [0, 1],
                                       [1, 1],
                                       [1, 0],
                                       [-1, 0]]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()

            elif position_x == 0 and position_y == 9:     # 7
                SQUARES_AROUND_SHIP = [[0, 1],
                                       [1, 1],
                                       [1, 0],]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()

            elif position_x == 0 and position_y in range(1, 9):     # 8
                SQUARES_AROUND_SHIP = [[0, 1],
                                       [1, 1],
                                       [1, 0],
                                       [1, -1],
                                       [0, -1]]
                for i in range(size):
                    self.ocean.board[position_y][position_x+i].ship()
                    self.ocean.board[position_y][position_x+i].water()

                    for j in range(len(SQUARES_AROUND_SHIP)):
                        self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()



        else:   # horizontal = False
            pass

            # for i in range(size):
            #     self.ocean.board[position_y+i][position_x].ship()
            #     self.ocean.board[position_y+i][position_x].water()

            #     for j in range(len(SQUARES_AROUND_SHIP)):
            #         self.ocean.board[position_y + SQUARES_AROUND_SHIP[j][0]][position_x + SQUARES_AROUND_SHIP[j][1]].water()


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
