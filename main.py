from square import Square
from ocean import Ocean
from player import Player



BATTLESHIP_SIZES = [['Carrier', 5],
                    ['Battleship', 4],
                    ['Cruiser', 3],
                    ['Submarine', 3],
                    ['Destroyer', 2]]


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


# def add_player():


def main():


    player1 = input('Enter your name: ')
    ocean1 = Ocean()
    ocean1.load_board()
    player = Player(player1, ocean1)
    print_table(BATTLESHIP_SIZES, ['Battleship', 'Size'])


    for ship in BATTLESHIP_SIZES:
        ship_choice = input('Enter which ship you would like to locate:')
        if ship_choice.upper() == ship[0].upper():
            ship_type = ship
            BATTLESHIP_SIZES.remove(ship)
    print(BATTLESHIP_SIZES)
        # else:
        #     raise IndexError('There are only 5 ships!')



    is_horizontal = int(input('\nEnter if your ship is horizontal(1/0):'))
    print('\nNow you need to locate your battleships')
    position_x = int(input('\nEnter X coordinate:'))
    position_y = int(input('\nEnter Y coordinate:'))






    player.add_ship(1, 5, 3, True)
    player.add_ship(4, 4, 3, False)
    player.shot(4, 4)
    player.shot(1, 5)
    player.shot(5, 1)
    print(ocean1)


if __name__ == '__main__':
    main()
