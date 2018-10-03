import numpy as np 
from random import randint


def random_bound(limit):
    return randint(0, limit)

def h_cat(matrix_a, matrix_b):
    if(matrix_a.shape[0] != matrix_b.shape[0]):
        raise NameError('Matrixs Rows are not same')
    row = matrix_a.shape[0]
    col_matrix_a= matrix_a.shape[1]
    col_matrix_b = matrix_b.shape[1]

    result_matrix = np.zeros((row, col_matrix_a + col_matrix_b))

    for i in range(row):
        for j in range(col_matrix_a):
            result_matrix[i,j] = matrix_a[i,j]
    
    for i in range(row):
        for j in range(col_matrix_b):
            result_matrix[i, col_matrix_a+j] = matrix_b[i,j]
    
    return result_matrix


def v_cat(matrix_a, matrix_b):
    # Columns has to be equal
    if(matrix_a.shape[1] != matrix_b.shape[1]):
        raise NameError("Matrix Columns has to be same")
    row_a = matrix_a.shape[0]
    row_b = matrix_b.shape[0]
    col = matrix_a.shape[1]

    result_matrix = np.zeros((row_a + row_b, col), dtype = np.float64)

    for i in range(row_a):
        for j in range(col):
            result_matrix[i,j] = matrix_a[i,j]

    for i in range(row_b):
        for j in range(col):
            result_matrix[row_a+i,j]  = matrix_b[i,j]
    
    return result_matrix

def get_random_matrix(row, col, bound):
    random_matrix = np.zeros((row,col),dtype=np.float64)
    for i in range(row):
        for j in range(col):
            random_matrix[i,j] = random_bound(bound)
    return random_matrix