import numpy as np

#
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
#
# c = a + b
# print(c)
#
# d = b ** 2
# print(d)
#
# e = np.sqrt(a)
# print(e)
#
# print(e + b)
#
# a += b
# print(a)

#
# a = np.arange(12).reshape((3, 4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))

# a = np.array([[3, 1, 5], [6, 2, 1]])
# b = np.array([[3, 2], [5, 3], [6, 1]])
#
# c = np.dot(a, b)
# d = a.dot(b)
# print(c)
# print(d)

# a = np.arange(3)
# b = np.arange(3)
#
# print(a.dot(b))
#

# a = np.arange(6).reshape((3, 2))
#
# for b in a:
# 	for c in b:
# 		print(c)
#
# for b in a.flat:
# 	print(b)

a = np.arange(12).reshape((3, 4))

print(a)

b = a.reshape((4, 3))
print(b)

print(a.ravel())

c = b.T
print(c)
