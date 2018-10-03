from testPathStub import pathStub
pathStub()
from matrixUtils import random_bound,get_random_matrix


def test_random():
    assert random_bound(1000) <= 999
    assert random_bound(1000) >= 0
    assert random_bound(10) <= 9
    assert random_bound(10) >= 0

def test_getRandomMatrix():
    size = 10
    boundValue = 1000
    sampleMatrix = get_random_matrix(size,size, boundValue)
    print(sampleMatrix.shape)
    assert sampleMatrix.shape == (size,size)
    assert sampleMatrix.shape != (size,size + 10)
    assert sampleMatrix.shape != (size + 10, size)
    for i in range(10):
        for j in range(10):
            assert sampleMatrix[i,j] < boundValue
            assert sampleMatrix[i,j] >= 0

    