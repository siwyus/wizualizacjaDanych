#
# a = np.array([0, 1])
# print(a)
#
# a = np.arange(1, 5, 0.1)
# print(a)
# print(type(a))
# print(a.dtype)
#
# b = np.arange(5, dtype='int64')
# print(b)
# print(b.dtype)  # typ zmiennych tablicy
# print(b.shape)  # długość tablicy
# print(b.ndim)  # ilość wymiarów tablicy
#
# c = np.array([np.arange(3), np.arange(3)])
# print(c)
# print(c.shape)  # długość tablicy
# print(c.ndim)  # ilość wymiarów tablicy
import numpy as np

# zero = np.zeros((5, 5), dtype='int64')
# print(zero)
#
# jedynki = np.ones((4, 4))
# print(jedynki)
#
# pusta = np.empty((2, 2))
# print(pusta)
#
# poz_1 = pusta[1, 1]
# print(poz_1)
#
# macierz = np.array([[1, 2], [3, 4]])
# print(macierz)
#
# a = np.linspace(1, 2, 5, endpoint=False)
# print(a)
#
# b = np.indices((5, 3))
# print(b)
# print(b[1, 1, 2])
# print(b[1][1][2])  # to samo co wyżej
#
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
#
# mat_dia = np.diag([a for a in range(5)], -1)
# print(mat_dia)
#
# z = np.fromiter(range(5), dtype='int32')
# print(z)
#
# krzysztof = b'Krzysztof'
# print(krzysztof)
# krz = np.frombuffer(krzysztof, dtype='S3')
# print(krz)

# krzysztof = 'Krzysztof'
# krz = np.array(list(krzysztof))
# print(krz)
# krz_2 = np.array(list(b'Krzysztof'))
# print(krz_2)
# krz_3 = np.fromiter(krzysztof, dtype='S1')
# print(krz_3)
# krz_4 = np.fromiter(krzysztof, dtype='U1')
# print(krz_4)

# mat1 = np.ones((2, 2))
# mat2 = np.ones((2, 2))
#
# a = mat1 + mat2
# print(a)
# a = a - mat2
# print(a)
# b = 4 * a
# print(b)
# print(b / a)


# a = np.arange(10)
# print(a)
#
# s = slice(2, 7, 2)
# print(a[s])
#
# print(a[2:7:2])
#
# print(a[1:5])

# a = np.arange(25)
# print(a)
#
# mat = a.reshape((5, 5))
# print(mat)
#
# print(mat[1:])
# print(mat[:, 1:])
# print(mat[:, -1:])
# print(mat[2:6, 1:3])
# print(mat[:, range(2, 5, 1)])

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)
