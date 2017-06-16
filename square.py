class Square:
    def __init__(self, row, column):
        self.is_hidden = False
        self.is_forbidden = False
        self.is_ship = False
        self.row = row
        self.column = column

    def __str__(self):

        if self.is_hidden:
            mark = '~'
        else:
            if self.is_ship:
                mark = 'x'
            else:
                mark = '0'

        return mark

    def hide(self):
        self.is_hidden = True

    def un_hide(self):
        self.is_hidden = False

    def ship(self):
        self.is_ship = True

    def forbidden(self):
        self.is_forbidden = True
