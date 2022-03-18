# array = []
# for x in range(0, 9):
# 	array.append(x ** 2)
# print(array)
#
# array2 = [x ** 2 for x in range(0, 9)]
# print(array2)
#
# array3 = []
# for x in range(0, 6):
# 	array3.append(3 ** x)
# print(array3)
#
# array4 = [3 ** x for x in range(0, 6)]
# print(array4)
#
#
# def is_odd(element):
# 	return element % 2 != 0
#
#
# array5 = []
# for x in array:
# 	if is_odd(x):
# 		array5.append(x)
# print(array5)
#
# array6 = [x for x in array if is_odd(x)]
# print(array6)
#
# lista = []
# for a in [1, 2, 3]:
# 	for b in [4, 5, 6]:
# 		lista.append((a, b))
# print(lista)
#
# lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista2)

# slownik = {'PZU': 'Państwowy zakład ubezpieczeń',
# 		   'ZUS': 'Zakład ubezpieczeń społecznych',
# 		   'PKO': 'Państwowa kasa oszczedności'}
# slownik2 = {}
# for key, value in slownik.items():
# 	slownik2[value] = key
# print(slownik)
# print(slownik2)
#
# slownik3 = {value: key for key, value in slownik.items()}
# print(slownik3)

# import math
#
#
# def row_kwadratowe(a, b, c):
# 	delta = b**2 - 4 * a * c
# 	if delta < 0:
# 		print('brak rozwiazan')
# 		return -1
# 	elif delta == 0:
# 		print('jedno rozwiazanie')
# 		return (-b)/(2*a)
# 	else:
# 		print('dwa rozwiazania')
# 		x1 = ((-b) - math.sqrt(delta))/(a*2)
# 		x2 = ((-b) + math.sqrt(delta))/(a*2)
# 		return x1, x2
#
#
# print(row_kwadratowe(6, 1, 3))
# print(row_kwadratowe(1, 2, 1))
# print(row_kwadratowe(1, 4, 1))


# def jest_podzielna_przez_5(liczba):
# 	if liczba % 5 == 0:
# 		print('liczba %d jest podzielna przez 5' % liczba)
# 		return True
# 	else:
# 		print('liczba %d nie jest podzielna przez 5' % liczba)
# 		return False
#
#
# print(jest_podzielna_przez_5(10))
# print(jest_podzielna_przez_5(17))
# print(jest_podzielna_przez_5(-23))
# print(jest_podzielna_przez_5(-20))


# def dlugosc_odcinka(x1=1, y1=2, x2=3, y2=4):
# 	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(2, 2, y2=5, x2=4))
# print(dlugosc_odcinka(y2=3, x2=7))

#
# def ciag(* liczby):
# 	if len(liczby) == 0:
# 		return 0
# 	else:
# 		suma = 0
# 		for i in liczby:
# 			suma += i
# 		return suma
#
#
# print(ciag())
# print(ciag(1, 2, 3, 5, 6))
# print(ciag(-20, 10, -20, 10, -20, 10))


# def gwiazdki(**rzeczy):
# 	for cos in rzeczy:
# 		print({cos: rzeczy[cos]})
#
#
# print(gwiazdki(gry=[1, 2, 3], asd='asd', liczba=2)


from package import *
napis = 'dzis jest piątek'
module.wyswietl(napis)
module.dlugosc(napis)
print(dodawanie.dodaj(5, 15))