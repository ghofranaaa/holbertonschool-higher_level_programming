#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a new matrix with the results.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided. Each element in the matrix must be an integer or float.
    div (int/float): The number by which each element in the matrix will be divided. Must be a non-zero integer or float.

    Returns:
    list of lists of float: A new matrix with each element divided by the divisor, rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers/floats, if the rows of the matrix are not of the same size,
               or if div is not an integer or float.
    ZeroDivisionError: If div is zero.
    OverflowError: If any element in the matrix is infinity or NaN.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            if num == float('inf') or num == float('-inf') or num != num:
                raise OverflowError("cannot convert \
float infinity or NaN to integer")
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")