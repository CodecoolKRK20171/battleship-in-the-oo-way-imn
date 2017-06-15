# Battleship in the OOP way

## The story

The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates. Neither you nor the other player can see the other's board so you must try to guess where they are.

## Specification


### `main.py`

* `read_file`

  Reads data from file and formats list of lists to a string.

* `print_table(table, table_list)`

  Prints given table with nice, smooth order and with centered values in cells.
  Args:
    table (nested list): table with data
    title_list (list of strings): list with titles of data in table
  Returns:
    None
* `insert_ships_to_table(ocean, player)`

  Gets inputs from user(name/coordinates/type of ship/horizontal or vertical position) and adds ships with given coordinates to ocean board.
  Args:
    ocean: *Ocean* object.
    player: *player* object.

* `main`

  Controls the whole program.



### `square.py`

### Class Square

__Attributes__

* `is_hidden`
  - data: boolean
  - description: is square hidden - yes-True, no-False

* `is_water`
  - data: boolean
  - description: is square water - yes-True, no-False

* `is_ship`
  - data: boolean
  - description: is square ship - yes-True, no-False

* `row`
  - data: int
  - description: number of row in board

* `column`
  - data: int
  - description: number of column in board

__Instance methods__

* ##### ` __init__(self, row, column)`

  Constructs an Square object.
  Sets *is_marked* value.

* `__str__(self)`

  Returns proper string sign of *is_hidden*, *is_ship*, *is_water*.

* `hide(self)`

  Sets *is_hidden* value to True.

* `ship(self)`

  Sets *is_ship* value to True.

* `water(self)`

  Sets *is_water* value to True.

### `ocean.py`

### Class Ocean

__Attributes__
* `ships`
  - data: list
  - description: empty list of ships

* `board`
  - data: list
  - description: empty list of board


__Instance methods__

* ##### ` __init__(self)`

  Constructs an Ocean object.
  Initializes empty lists.

* `__str__(self)`

  Returns string with proper composition.


* `load_board(self)`

  Append empty spaces to board.
  Adds ship to board on proper places.


### `player.py`

### Class Player
__Attributes__
* `name`
  - data: str
  - description: name of player

* `ocean`
  - data: *Ocean* object
  - description:

__Instance methods__

* ##### ` __init__(self)`

  Constructs an Player object.

* `shot(self, position_x, position_y)`

  Unhides squares with given coordinates.
  Prints appropriate message for user('Hit'/'Miss')

* `add_squares_around_horizontal(self, square_around_list, position_x,  position_y, size, is_horizontal)`

  Horizontally adds forbidden signs (where user can't locate a ship) around already located ship.

* `add_squares_around_horizontal(self, square_around_list, position_x,  position_y, size, is_vertical)`

  Vertically adds forbidden signs (where user can't locate a ship) around already located ship.

* `add_ship(self, position_x, position_y, size, is horizontal)`

  Creating list of positions of the Ship and add this to list ships.

* `check_position(self, position_x, position_y, is_horizontal)`

  Checks if ship can be located with given coordinates by checking if it's in range of table size and if there is no already located ships.
  Returns True if ship can be located. Otherwise, returns False.

### `intro.txt`

    File with ASCII art used as introduction screen of the game.
