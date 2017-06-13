class Square:
    def __init__(self, row, column):
        self.is_marked = True
        self.row = row
        self.column = column

    def __str__(self):

        if self.is_marked:
            mark = 'x'
        else:
            mark = '0'
        return mark