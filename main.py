from square import Square
from ship import Ship
from ocean import Ocean
from player import Player


def player_inputs(ship_x, ship_y, ship_size, is_horizontal):
    pass


def main():
    
    ocean = Ocean()
    ocean.fill_board()
    player = Player('Andrzej', ocean)

    player.add_ship(1, 5, 3, True)
    player.add_ship(4, 4, 3, False)
    player.shot(4, 4)
    player.shot(1, 5)
    player.shot(5, 1)
    print(ocean)


if __name__ == '__main__':
    main()
