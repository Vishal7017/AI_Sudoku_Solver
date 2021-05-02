from Cross import cross
def cross(A, B):
    "Cross product of elements in A and B"
    return [a+b for a in A for b in B]

digits = '12345678'
rows = 'ABCEDFGHI'
cols = digits
# print(cross(row,cols))

squares = cross(rows, cols)
def grid_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

digits= '123456789'
grid = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"

print(grid_values(grid))
# def parse_grid(grid):
#     values = dict((s, digits) for s in squares)
#     for s,d in grid_values(grid).items():
#         if d in digits and not assign(values, s,d):
#             return False
        
#     return values


