# Battleship in the OOP way

## The story

The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates. Neither you nor the other player can see the other's board so you must try to guess where they are.

## Specification


### `main.py`
Controls of the program.


### `square.py`

### Class Square

__Attributes__

* `is_marked`
  - data: boolean
  - description: is square mark - yes-True, no-False

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

  Returns proper string sign of *is_marked*.


### `ship.py`

### Class Ship

__Attributes__

* `position`
  - data: tuple
  - description: tuple with ship positions

__Instance methods__

* ##### ` __init__(self, positions)`

  Constructs an Ship object.
  Creating list *squares* with Ship positions.

* `__str__(self)`

  Creating a string with proper length of Ship *x* and returns it.


### `ocean.py`

### Class Ocean

__Attributes__
  --

__Instance methods__

* ##### ` __init__(self)`

  Constructs an Ocean object.

* `__str__(self)`

  Returns string with proper composition.

* `add_ship(self, position_x, position_y, size, is horizontal=False)`

  Creating list of positions of the Ship and add this to list ships.

* `fill_board(self)`

  Append empty spaces to board.
  Adds ship to board on proper places/


### `player.py`

### Class Player

__Attributes__
* `shot_position`
  - data:
  - description: 

__Instance methods__

* ##### ` __init__(self)`

  Constructs an Player object.
