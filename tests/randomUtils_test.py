from testPathStub import pathStub
pathStub()
from randomUtils import randomBound,getRandomMatrix

def test_random():
    assert randomBound(1000) <= 999
    assert randomBound(1000) >= 0
    assert randomBound(10) <= 9
    assert randomBound(10) >= 0

def test_getRandomMatrix():
    size = 10
    boundValue = 1000
    sampleMatrix = getRandomMatrix(size,size, boundValue)
    print(sampleMatrix.shape)
    assert sampleMatrix.shape == (size,size)
    assert sampleMatrix.shape != (size,size + 10)
    assert sampleMatrix.shape != (size + 10, size)
    for i in range(10):
        for j in range(10):
            assert sampleMatrix[i,j] < boundValue
            assert sampleMatrix[i,j] >= 0

    