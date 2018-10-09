from testPathStub import pathStub
pathStub()
import phanes.vhe as vhe


def test_random():
    assert vhe.matrixUtils.random_bound(1000) <= 999
    assert vhe.matrixUtils.random_bound(1000) >= 0
    assert vhe.matrixUtils.random_bound(10) <= 9
    assert vhe.matrixUtils.random_bound(10) >= 0

def test_getRandomMatrix():
    size = 10
    boundValue = 1000
    sampleMatrix = vhe.matrixUtils.get_random_matrix(size,size, boundValue)
    print(sampleMatrix.shape)
    assert sampleMatrix.shape == (size,size)
    assert sampleMatrix.shape != (size,size + 10)
    assert sampleMatrix.shape != (size + 10, size)
    for i in range(10):
        for j in range(10):
            assert sampleMatrix[i,j] <= boundValue
            assert sampleMatrix[i,j] >= 0

    