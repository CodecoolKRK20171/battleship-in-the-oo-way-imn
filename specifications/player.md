## Specification

Create a player, add ship in proper place.

### Class Player

__Attributes__

* `name`
  - data: string
  - description: name of the player

* `ocean`
  - data: list of lists
  - description: board (nested list) made of squares

__Instance methods__

* ##### ` __init__(self)`

  Constructs an Player object.

* `shot(self, position_x, position_y)`

  Takes a shot i proper position in the board.

* `add_ship(self, position_x, position_y, size, is_horizontal)`

  Adds ships in proper positions in board.
