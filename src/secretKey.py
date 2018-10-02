import numpy as np
from matrixUtils import hCat
def getSecretKey(inputMatrix):
    #Generate an Identity Matrix size of input matrix row 
    I = np.identity(inputMatrix.shape(0), dtype=np.uint64)
    return hCat(I, inputMatrix)
    


