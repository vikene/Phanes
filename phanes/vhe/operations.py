from .core import *
import numpy as np 

def copy_rows(input_matrix_rows, num_rows):
    output_matrix_ans = np.zeros(num_rows, input_matrix_rows.shape[0])
    for i in range(output_matrix_ans.shape[0]):
        for j in range(output_matrix_ans.shape[1]):
            output_matrix_ans[i][j] = input_matrix_rows[0][j]
    return output_matrix_ans

def add_vectors(input_vector_c1, input_vector_c2):
    return input_vector_c1 + input_vector_c2

def vectorize(input_matrix_m):
    row = input_matrix_m.shape[0]
    col = input_matrix_m.shape[1]
    output_matrix_ans = np.zeros((row * col, 1))
    for i in range(row):
        for j in range(col):
            output_matrix_ans[i * col + j][0] = input_matrix_m[i][j]
    return output_matrix_ans

def inner_product_client(input_matrix_t):
    matrix_secret_key = get_secret_key(input_matrix_t)
    tvsts = np.matmul(matrix_secret_key.T, matrix_secret_key)
    tvsts = vectorize(tvsts)
    tvsts = tvsts.T
    print(tvsts)
    mvsts = 

if __name__ == "__main__":
    x1  = [2813, 8765, 7120, 6573, 1167, 6491 ,1345, 918, 4715, 3082]
    print(x1)
    input_matrix_T = get_random_matrix(10,10,1000)
    #input_matrix_S = get_secret_key(input_matrix_T)
    inner_product_client(input_matrix_T)