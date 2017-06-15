from square import Square


class Ocean:
    def __init__(self):
        self.ships = []
        self.board = []

    def __str__(self):
        ocean_str = '   ABCDEFGHIJ\n'
        ocean_str += '--------------\n'
        i = -1
        for lista in self.board:
            i += 1
            ocean_str += '|' + str(i) + '|'
            for item in lista:
                ocean_str += str(item)
            ocean_str += '|' + '\n'
        ocean_str += '--------------\n'
        return ocean_str

    def load_board(self):
        for i in range(0, 10):
            self.board.append([])
            for j in range(0, 10):
                self.board[i].append(Square(i, j))


    def check_end_game(self):
        
        for line in self.board:
            for square in line:
                if square.is_ship:
                    if square.is_hidden:
                        return False
        return True
