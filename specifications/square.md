## Specification

Square is one of 100 elements of board (ocean).
Each square holds information about ship/water/mark.

### Class Square

__Attributes__

* `is_hidden`
  - data: boolean
  - description: are ships hidden

* `is_ship`
  - data: boolean
  - description: is there a ship in position_x

* `row`
  - data: int
  - description: number of row in board

* `column`
  - data: int
  - description: number of column in board

__Instance methods__

* ##### ` __init__(self, row, column)`

  Constructs an Square object.
  Sets *is_hidden* value.
  Sets *is_ship* value.

* `__str__(self)`

  Returns proper string sign of *mark*.

* `un_hide`

  Sets *is_hidden* to False.

* `ship`

  Sets *is_ship* to True.
