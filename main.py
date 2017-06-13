from square import Square
from ship import Ship
from ocean import Ocean

def main():
    ship = Ship(((2, 3), (2, 4), (2, 5)))
    ocean = Ocean()
    ocean.add_ship(2, 3, 4, True)
    ocean.add_ship(0, 0, 2, False)
    ocean.fill_board()
    print(ocean)


if __name__ == '__main__':
    main()