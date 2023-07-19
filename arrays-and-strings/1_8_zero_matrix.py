'''
Write an algorithm given an element in an M X N matrix is 0,
its entire row and columns are set to 0
'''

def zero_matrix(matrix):
    """
    given an element in an M X N matrix is 0,
    its entire row and columns are set to 0

    >>> zero_matrix([[0, 1], [2, 3]])
    [[0, 0], [0, 3]]

    >>> zero_matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    [[0, 0, 0], [0, 4, 5], [0, 7, 8]]

    """
    M = len(matrix)
    N = len(matrix[0])

    rows_with_zeros = set([])
    cols_with_zeros = set([])

    #if either all rows or all cols contain zeros, whole matrix is 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                rows_with_zeros.add(i)
                cols_with_zeros.add(j)

    matrix = cols_to_zeros(matrix=matrix, cols=cols_with_zeros)
    matrix = rows_to_zeros(matrix=matrix, rows=rows_with_zeros)


    return matrix

def cols_to_zeros(matrix, cols):
    """
    Turn a column in a matrix to all zeros

    >>> cols_to_zeros([[0, 1], [2, 3]], [0])
    [[0, 1], [0, 3]]
    """

    for col in cols:
        #iterate over each row
        for row in range(len(matrix)):
            matrix[row][col] = 0
        #turn index (col) to 0 for each row
    return matrix

def rows_to_zeros(matrix, rows):
    """
    Turn a row in a matrix to all zeros

    >>> rows_to_zeros([[0, 1], [2, 3]], [0])
    [[0, 0], [2, 3]]
    """
    #iterate over each row
    for row in rows:
        for col in range(len(matrix[0])):
            matrix[row][col] = 0
        #turn index (col) to 0 for each row
    return matrix
