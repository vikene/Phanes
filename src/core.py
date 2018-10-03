import numpy as np
from matrixUtils import h_cat
from binaryBits import get_binary_bits
from matrixUtils import get_random_matrix, v_cat
l = 100
w = 1 << 40
#returns nearest Integer 
def nearest_integer(x, w):
    return int((x + (w+1)/2)/ w)

def get_bit_matrix(input_matrix):
    rows = input_matrix.shape[0]
    columns = input_matrix.shape[1]
    result_matrix = np.zeros((rows, l * columns), dtype= np.float64)
    #powers = np.zeros((1,l))
    powers = [0] * l
    powers[0] = 1
    for i in range(1, l):
        powers[i] = powers[i - 1] * 2
    for i in range(rows):
        for j in range(columns):
            for k in range(l):
                result_matrix[i, j*l + k] = input_matrix[i,j] * powers[k]
    return result_matrix

    
def get_bit_vector(input_vector):
    length = len(input_vector)
    result_vector = [0] * (length * l)
    for i in range(length):
        sign = -1 if (input_vector[i] < 0) else 1
        value = input_vector[i] * sign
        bit_matrix = get_binary_bits(value)
        for j in range(l):
            result_vector[(i*l)+j] = sign * bit_matrix[j]
    return result_vector

def key_switch(input_matrix, input_vector):
    c_star = get_bit_vector(input_vector)
    c_star = np.asarray(c_star,dtype=np.float64)
    print(c_star.shape)
    print(input_matrix.shape)
    return np.matmul(input_matrix, c_star)

def key_switch_matrix(input_matrix_S, input_matrix_T):
    abound = 1000
    ebound = 1000
    input_matrix_sstar = get_bit_matrix(input_matrix_S)
    input_matrix_a = get_random_matrix(input_matrix_T.shape[1], input_matrix_sstar.shape[1],abound)
    input_matrix_e = get_random_matrix(input_matrix_sstar.shape[0], input_matrix_sstar.shape[1], ebound)
    temp = np.add(input_matrix_sstar, input_matrix_e)
    temp = np.subtract(temp, np.matmul(input_matrix_T, input_matrix_a))
    print(temp.shape)
    print(v_cat(temp,input_matrix_a).shape)
    return v_cat(temp  , input_matrix_a)

def encrypt(input_matrix_T, input_vector_x):
    I = np.identity(len(input_vector_x), dtype=np.float64)
    ksm = key_switch_matrix(I,input_matrix_T)
    vector_scalar = np.dot(input_vector_x, w)
    return key_switch(ksm, vector_scalar)

def decrypt(input_matrix_s, input_vector_c):
    input_vector_sc = np.matmul(input_matrix_s , input_vector_c)
    input_vector_output = [0] * len(input_vector_sc)
    for i in range(len(input_vector_sc)):
        input_vector_output[i] = nearest_integer(input_vector_sc[i],w)
    return input_vector_output
def get_secret_key(input_matrix):
    #Generate an Identity Matrix size of input matrix row 
    I = np.identity(input_matrix.shape[0], dtype=np.float64)
    return h_cat(I, input_matrix)

if __name__ == "__main__":
    x1  = [2813, 8765, 7120, 6573, 1167, 6491 ,1345, 918, 4715, 3082]
    print(x1)
    input_matrix_T = get_random_matrix(10,10,1000)
    input_matrix_S = get_secret_key(input_matrix_T)
    cipher = encrypt(input_matrix_T, x1)
    print(cipher)
    plain = decrypt(input_matrix_S,cipher)
    print(plain)
    cipher = cipher + cipher
    plain = decrypt(input_matrix_S,cipher)
    print(plain)
