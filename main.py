from square import Square
from ocean import Ocean
from player import Player

BATTLESHIP_SIZES = [['Carrier', 5],
                    ['Battleship', 4],
                    ['Cruiser', 3],
                    ['Submarine', 2],
                    ['Destroyer', 1]]


# def add_player():




def main():


    player1 = input('Enter your name: ')
    ocean1 = Ocean()
    ocean1.load_board()
    player = Player(player1, ocean1)
    ship_choice = int(input('Enter which ship you would like to locate:')

    for i in range(len(BATTLESHIP_SIZES)):
        if ship_choice == BATTLESHIP_SIZES[i]:
            ship_type = BATTLESHIP_SIZES[i-1]
            BATTLESHIP_SIZES.remove(BATTLESHIP_SIZES[i-1])
    print('Now you need to locate your battleships\n')





    player.add_ship(1, 5, 3, True)
    player.add_ship(4, 4, 3, False)
    player.shot(4, 4)
    player.shot(1, 5)
    player.shot(5, 1)
    print(ocean1)

if __name__ == '__main__':
    main()
