
class Player:

    def __init__(self):
        self.name = name
        pass

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

    def shot(self):
        pass
