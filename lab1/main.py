import numpy as numpy


def ex7_1(m, n):
    mMatrix = numpy.arange(m).reshape((1, m))
    nMatrix = numpy.arange(n).reshape((1, n))

    return mMatrix.T * nMatrix


def ex7_2_3(matrix, ax):
    s = numpy.sum(matrix, axis=ax)
    return matrix/s if ax == 0 else matrix.T/s


def main():
    # part II
    # ex 7
    print(f"Ex 7 result: \n{ex7_1(4, 5)}\n\n")

    m = numpy.array([[1, 2, 6, 4], [3, 4, 3, 7], [1, 4, 6, 9]], dtype=numpy.float64)

    print(f"Ex 7.b:\n.\
        Original matrix:\n.\
        {m}\n.\
        Normalized matrix:\n.\
        {ex7_2_3(m, 0)}\n\n")
    print(f"Ex 7.c:\n.\
        Original matrix:\n{m}.\
        \nNormalized matrix:\n.\
        {ex7_2_3(m, 1)}\n\n")


main()
