# import sys
# import math
#
# print(sys.version)
# a = 'zajęcia\n z wizualizacji danych'
# print(a)
# print(type(a))
# b, c = 5.4, 5
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# d = 3 + 2j
# print(d)
# print(type(d))
#
# f = 'zajęcia'
# g = ' z wizualizacji'
# print(f + g)
#
# h = 7
# i = 3
# print(h // i)
# print((2/3) ** i)
# print(math.pow(2/3, i))
#
# h += 5
# print(h)

a, b = 5, 3
c = a - b
print('wynik działania %(z1)d - %(z2)d = %(z3)d' %{'z1': a, 'z2': b, 'z3': c})
print('wynik działania {0:d} = {1:d} = {2:d}'.format(a, b, c))