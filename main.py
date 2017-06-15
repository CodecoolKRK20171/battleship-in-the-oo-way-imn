from square import Square
from ocean import Ocean
from player import Player
import os


LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

BATTLESHIP_SIZES = {'C': 5}
                    # 'Battleship': 4,
                    # 'Cruiser': 3,
                    # 'Submarine': 3,
                    # 'Destroyer': 2}


def read_file():
    board = []
    column = []
    with open('intro.txt') as text:
        for line in text.readlines():
            column.append(line)
        board.append(column)
    for line in board:
        print(''.join(line))


def print_table(table, title_list):
    '''Prints given table with nice, smooth order and with centered values in cells.

    Args:
        table (nested list): table with data
        title_list (list of strings): list with titles of data in table

    Returns:
        None

    '''
    for i in range(len(table)):     # changing ints (ship sizes) to strings
        table[i][1] = str(table[i][1])

    cell_widths = []
    columns = []
    SPACES_AROUND_STRING = 2

    for i in range(len(title_list)):
        columns.append([title_list[i]])
        for j in range(len(table)):
            columns[i].append(table[j][i])  # columns - nested list with lists of elements of table columns
        cell_widths.append(max(map(len, columns[i])))   # cell_widths - list with max len of str in table columns

    width_of_table = 0

    for width in cell_widths:
        width_of_table += width     # sum of the longest string length from row in table
    width_of_table += len(title_list) * SPACES_AROUND_STRING + len(title_list) + 1

    print('/' + '-' * (width_of_table-SPACES_AROUND_STRING) + '\\')
    row_to_print = '|'
    line_between_rows = '|'

    for i in range(len(table)+1):

        for j in range(len(title_list)):
            row_to_print += columns[j][i].center(cell_widths[j]+SPACES_AROUND_STRING) + '|'
            line_between_rows += '-'*(cell_widths[j]+SPACES_AROUND_STRING) + '|'

        print(row_to_print)

        if i == len(table):
            print('\\' + '-' * (width_of_table-SPACES_AROUND_STRING) + '/')

        else:
            print(line_between_rows)
            row_to_print = '|'
            line_between_rows = '|'

def insert_ships_to_table(ocean, player):

    ship_kinds = []
    
    for key in BATTLESHIP_SIZES:
        ship_kinds.append(key)

    while len(ship_kinds) > 0:
        print_table([[ship, BATTLESHIP_SIZES[ship]] for ship in ship_kinds], ['Battleship kind', 'Size'])
        
        ship_choice = input('Enter which ship you would like to locate: ')

        if ship_choice in ship_kinds:
            ship_size = BATTLESHIP_SIZES[ship_choice]

            is_horizontal = ''

            while is_horizontal not in ['1', '0']:
                is_horizontal = input('\nEnter if your ship is horizontal(1/0): ')

            if is_horizontal == '1':
                is_horizontal = True
            elif is_horizontal == '0':
                is_horizontal = False

            print('\nNow you need to locate your battleships\n')

            print(ocean)

            position = input('\nEnter coordinates(e.g. H5): ')

            for letter in LETTERS:
                if position[0].upper() == letter:
                    position_x = int(LETTERS.index(letter))
            position_y = int(position[1])
            check = player.check_position(position_x, position_y, ship_size, is_horizontal)
            if check:
                player.add_ship(position_x, position_y, ship_size, is_horizontal)
                ship_kinds.remove(ship_choice)
                print(ocean)
                input('Press Enter to continue')
                os.system('clear')
            else:
                print('You can\'t locate your ship here.')
        else:
            print('There is no ship with that name!')

def hide_squares(ocean):
    for row in ocean.board:
        for column in row:
            column.hide()

def player_round(ocean, player):

    next_player = False
    print(ocean)
    while not next_player:
        
        position = input('\nEnter coordinates where you want to shot(e.g. H5): ')
        for letter in LETTERS:
            if position[0].upper() == letter:
                position_x = int(LETTERS.index(letter))
            position_y = int(position[1])
        
        result = player.shot(position_x, position_y)
        print(ocean)
        if result == True:
            print('You hited the ship, another shot for you')
            continue

        input('Press enter to change player.')
        os.system('clear')
        next_player = True




def main():
    read_file()
    player1_name = input('Enter your name: ')
    ocean1 = Ocean()
    ocean1.load_board()
    player1 = Player(player1_name, ocean1)
    insert_ships_to_table(ocean1, player1)

    print('Now player 2')

    player2_name = input('Enter your name: ')
    ocean2 = Ocean()
    ocean2.load_board()
    player2 = Player(player2_name, ocean2)
    insert_ships_to_table(ocean2, player2)

    os.system('clear')
    print('Now its time to start the game!\n')
    print(player1_name + ' is starting:')

    input('If ' + player2_name + ' is not watching we can start. Press Enter to continue')

    hide_squares(ocean1)
    hide_squares(ocean2)

    while True:
        
        os.system('clear')
        print(player1_name + ' is now shooting')

        player_round(ocean2, player2)

        os.system('clear')
        print(player2_name + ' is now shooting')
        
        player_round(ocean1, player1)





if __name__ == '__main__':
    main()
