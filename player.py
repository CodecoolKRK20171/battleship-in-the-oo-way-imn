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
            for i in range(size):
                self.ocean.board[position_y][position_x+i].ship()
                self.ocean.board[position_y][position_x+i].water()
                self.ocean.board[position_y+1][position_x].water()
                self.ocean.board[position_y+1][position_x+1].water()
                self.ocean.board[position_y+1][position_x-1].water()
                self.ocean.board[position_y-1][position_x].water()
                self.ocean.board[position_y-1][position_x+1].water()
                self.ocean.board[position_y-1][position_x-1].water()
                self.ocean.board[position_y][position_x+1].water()
                self.ocean.board[position_y][position_x-1].water()


        else:
            for i in range(size):
                self.ocean.board[position_y+i][position_x].ship()
                self.ocean.board[position_y+i][position_x].water()               
                self.ocean.board[position_y+1][position_x].water()
                self.ocean.board[position_y+1][position_x+1].water()
                self.ocean.board[position_y+1][position_x-1].water()
                self.ocean.board[position_y-1][position_x].water()
                self.ocean.board[position_y-1][position_x+1].water()
                self.ocean.board[position_y-1][position_x-1].water()
                self.ocean.board[position_y][position_x+1].water()
                self.ocean.board[position_y][position_x-1].water()

    def check_position(self, position_x, position_y, size, is_horizontal):

        checking_size = size + 2

        if is_horizontal:
            horizontal_position_x = position_x - 1
            for i in range(checking_size):
                if self.ocean.board[position_y][horizontal_position_x+i].is_water:
                    return False
                elif self.ocean.board[position_y+1][horizontal_position_x+i].is_water or self.ocean.board[position_y-1][horizontal_position_x+i].is_water:
                    return False
                else:
                    return True
        else:
            horizontal_position_y = position_y - 1
            for i in range(checking_size):
                if self.ocean.board[horizontal_position_y+i][position_x].is_water:
                    return False
                elif self.ocean.board[horizontal_position_y+i][position_x+1].is_water or self.ocean.board[horizontal_position_y+i][position_x-1].is_water:
                    return False
                else:
                    return True

player1 = input('Enter your name: ')
ocean1 = Ocean()
ocean1.load_board()
player = Player(player1, ocean1)

player.add_ship(1, 5, 3, True)
check = player.check_position(2, 5, 3, True)
print(check)
player.add_ship(4, 4, 3, False)
player.shot(4, 4)
player.shot(1, 5)
player.shot(5, 1)
print(ocean1)