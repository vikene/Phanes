from random import randint
import numpy as np

#Generates and returns a random number between 0 to n-1
def randomBound(limit):
    return randint(0, limit)


def getRandomMatrix(row, col, bound):
    randomMatrix = np.zeros((row,col),dtype=np.uint64)
    for i in range(row):
        for j in range(col):
            randomMatrix[i,j] = randomBound(bound)
    return randomMatrix


if __name__ == "__main__":
    print(getRandomMatrix(10,10,1000))