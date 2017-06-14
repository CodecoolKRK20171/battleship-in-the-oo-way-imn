from square import Square
from ocean import Ocean
from player import Player


LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


# BATTLESHIP_SIZES = [['Carrier', 5],
#                     ['Battleship', 4],
#                     ['Cruiser', 3],
#                     ['Submarine', 3],
#                     ['Destroyer', 2]]


BATTLESHIP_SIZES = {'c': 3, 'b': 2}



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



# # def add_player():

def main():
    player1 = input('Enter your name: ')

    ocean1 = Ocean()
    ocean1.load_board()
    player1 = Player(player1, ocean1)

    ship_kinds = []
    for key in BATTLESHIP_SIZES:
        ship_kinds.append(key)

    while len(ship_kinds) > 0:
        print_table([[ship, BATTLESHIP_SIZES[ship]] for ship in ship_kinds], ['Battleship kind', 'Size'])
        ship_choice = input('Enter which ship you would like to locate: ')

        if ship_choice in ship_kinds:
            ship_size = int(BATTLESHIP_SIZES[ship_choice])

            is_horizontal = ''
            while is_horizontal not in ['1', '0']:
                is_horizontal = input('\nEnter if your ship is horizontal(1/0): ')

            if is_horizontal == '1':
                is_horizontal = True
            else:
                is_horizontal = False

            print('\nNow you need to locate your battleships')

            position = input('Enter coordinates(e.g. H5): ')

            for letter in LETTERS:
                if position[0].upper() == letter:
                    position_x = int(LETTERS.index(letter))
            position_y = int(position[1])
            # check = player1.check_position(position_x, position_y, ship_size, is_horizontal)
            # print(check)
            # if check:
            player1.add_ship(position_x, position_y, ship_size, is_horizontal)
            print(ocean1)

            ship_kinds.remove(ship_choice)

        else:
            print('There is no such option!')

    for row in ocean1.board:
        for column in row:
            column.un_hide()
    print(ocean1)

<<<<<<< HEAD
    player2 = input('Enter your name: ')

    ocean2 = Ocean()
    ocean2.load_board()
    player2 = Player(player2, ocean2)

    # position_x2, position_y2, ship_size2, is_horizontal2 = get_coordinates(player2)
    player2.add_ship(position_x2, position_y2, ship_size2, is_horizontal2)
    for row in ocean1.board:
        for column in row:
            column.un_hide()
    print(ocean2)






    # player.add_ship(4, 4, 3, False)
    # player.shot(4, 4)
    # player.shot(1, 5)
    # player.shot(5, 1)


=======
>>>>>>> 6f9adf101a879956fa10aa7752f75646aa40a7f0

if __name__ == '__main__':
    main()
