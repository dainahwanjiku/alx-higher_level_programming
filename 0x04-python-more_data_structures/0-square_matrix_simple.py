#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for elm in matrix:
        square_matrix.append([c**2 for c in elm])
    return square_matrix
