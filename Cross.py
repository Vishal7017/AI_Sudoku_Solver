def cross(A, B):
    "Cross product of elements in A and B"
    return [a+b for a in A for b in B]

digits = '12345678'
rows = 'ABCEDFGHI'
cols = digits
# print(cross(row,cols))

squares = cross(rows, cols)
# print(squares)
unitlist = [[cross(rows, c) for c in cols]+
            [cross(r, cols) for r in rows]+

            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123','456','789')]]

# print(unitlist)
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
# print(units)
peers = dict((s, set(sum(units[s], []))-set([s])) for s in squares)
# print(peers)
# def test():
#     "A set of unit tests."
#     assert len(squares) == 81
#     assert len(unitlist) == 27
#     assert all(len(units[s]) == 3 for s in squares)
#     assert all(len(peers[s]) == 20 for s in squares)
#     assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
#                            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
#                            ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
#     assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
#                                'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
#                                'A1', 'A3', 'B1', 'B3'])
#     print ('All tests pass.')


# test()

def grid_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

grid = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"

# print(grid_values(grid))

def parse_grid(grid):
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s,d):
            return False
    return values

print(values)