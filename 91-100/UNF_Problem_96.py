import numpy as np


def possible(r,c,n):
    global matrix
    if n in matrix[r,:]:
        return False
    if n in matrix[:,c]:
        return False
    r0 = r//3 * 3
    c0 = c//3 * 3
    for i in range(0,3):
        for j in range(0,3):
            if matrix[r0 + i, c0+j] == n:
                return False
    return True


def create_suduko_matrix(string):
    lists = []
    lines = string.splitlines()
    for i in lines:
        lists.append(num_to_list(i))
    matrix = np.matrix(lists)

    return matrix

def solve():
    global matrix
    for r in range(9):
        for c in range(9):
            if matrix[r, c] == 0:
                for n in range(1,10):
                    if possible(r, c, n):
                        matrix[r, c] = n
                        solve()
                        matrix[r, c] = 0
                return
    print(matrix)



suduko_string = '''003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300'''

matrix = np.matrix('5 3 0 0 7 0 0 0 0; 6 0 0 1 9 5 0 0 0; 0 9 8 0 0 0 0 6 0; 8 0 0 0 6 0 0 0 3; 4 0 0 8 0 3 0 0 1; 7 0 0 0 2 0 0 0 6; 0 6 0 0 0 0 2 8 0; 0 0 0 4 1 9 0 0 5; 0 0 0 0 8 0 0 0 9')
solve()