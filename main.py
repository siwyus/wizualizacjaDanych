def is_even(liczba):
	return liczba % 2 == 0


def show_exercise_number(number):
	print('Zadanie %d' % number)


# Zadanie 1
show_exercise_number(1)
A = [1 - x for x in range(1, 10)]
B = [4 ** x for x in range(0, 7)]
C = [x for x in B if is_even(x)]

print(A)
print(B)
print(C)

# Zadanie 2
show_exercise_number(2)

from numpy import random

random_number_array = random.randint(100, size=10)

only_even_numbers = [x for x in random_number_array if is_even(x)]

print(only_even_numbers)

# Zadanie 3
show_exercise_number(3)
by_piece = 'sztuki'
products_dictionary = {'mąka': 'kg', 'chleb': by_piece, 'jajka': by_piece, 'szynka': 'kg'}

only_products_by_piece = [key for key, value in products_dictionary.items() if value == by_piece]

print(only_products_by_piece)

# Zadanie 4
show_exercise_number(4)


def is_right_triangle(a, b, c):
	return a ** 2 + b ** 2 == c ** 2


print(is_right_triangle(3, 4, 5))

# Zadanie 5
show_exercise_number(5)


def calc_trapezoid_field(base_top=5, base_bottom=10, height=7):
	return (base_top + base_bottom) * height / 2


print(calc_trapezoid_field())


# Zadanie 6
show_exercise_number(6)


def calc_products_of_the_sequence(initial_value=1, quotient=4, elements_amount=10):
	sequence = [initial_value]
	for x in range(0, elements_amount - 1):
		sequence.append(x * quotient)
	print(sequence)

calc_products_of_the_sequence()
