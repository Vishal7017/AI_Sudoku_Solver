def cross(A, B):
    "Cross product of elements in A and B"
    return [a+b for a in A for b in B]

row = '12345678'
cols = 'ABCEDFGHI'
print(cross(row,cols))