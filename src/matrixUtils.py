import numpy as np 

def hCat(matrixA, matrixB):
    if(matrixA.shape(0) != matrixB.shape(0)):
        raise NameError('Matrixs Rows are not same')
    row = matrixA.shape(0)
    colMatrixA= matrixA.shape(1)
    colMatrixB = matrixB.shape(1)

    resultMatrix = np.zeros((row, colMatrixA + colMatrixB))

    for i in range(row):
        for j in range(colMatrixA):
            resultMatrix[i,j] = matrixA[i,j]
    
    for i in range(row):
        for j in range(colMatrixB):
            resultMatrix[i, colMatrixA+j] = matrixB[i,j]
    
    return resultMatrix


def vCat(matrixA, matrixB):
    # Columns has to be equal
    if(matrixA.shape(1) == matrixB.shape(1)):
        raise NameError("Matrix Columns has to be same")
    rowA = matrixA.shape(0)
    rowB = matrixB.shape(0)
    col = matrixA.shape(1)

    resultMatrix = np.zeros((rowA + rowB, col), dtype = np.uint64)

    for i in range(rowA):
        for j in range(col):
            resultMatrix[i,j] = matrixA[i,j]

    for i in range(rowB):
        for j in range(col):
            resultMatrix[rowA+i,j]  = matrixB[i,j]
    
    return resultMatrix