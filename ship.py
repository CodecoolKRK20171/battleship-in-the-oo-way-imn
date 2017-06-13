from square import Square

class Ship:
    def __init__(self, positions):
        self.positions = positions
        self.squares = []
        for i in range(len(self.positions)):
            square = Square(self.positions[i][0], self.positions[i][1])
            self.squares.append(square)

    def __str__(self):
        ship7 = ''
        for i in range(len(self.squares)):
            ship7 += str(self.squares[i])
        return ship7