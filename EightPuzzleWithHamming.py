from EightPuzzle import *

def h(s):
    sum = 0
    block = s.b
    for row_index, row in enumerate(block):
        for column_index, column in enumerate(row):
            origin_index = row_index * 3 + column_index
            current_index = row[column_index]
            if origin_index != 0 and origin_index != current_index:
                sum += 1
    return sum