from EightPuzzle import *


def h(s):
    sum = 0
    block = s.b
    for row_index, row in enumerate(block):
        for column_index, column in enumerate(block[row_index]):
            origin_index = row_index * 3 + column_index
            current_index = row[column_index]
            if origin_index != 0 and origin_index != current_index:
                sum += distance(origin_index, current_index)
    return sum


def distance(origin, current):
    origin_row = (origin - origin % 3) / 3 + 1
    origin_col = origin % 3
    current_row = (current - current % 3) / 3 + 1
    current_col = current % 3
    return abs(origin_row - current_row) + abs(origin_col + current_col)
