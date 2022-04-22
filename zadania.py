import numpy as np

# zad 1

a = np.arange(4, 4 * 20 + 1, 4)
print(a)
print(len(a))

# zad 2

b = np.arange(5, 10, 0.5)
print(b)
c = b.astype('int32')
print(c)


# zad 3

def create_powers_of_two_array(n):
	array = np.full((n, n), 2)

	return array


print(create_powers_of_two_array(2))


# zad 4

def logspace_array(d, n):
	return d ** np.arange(n)


print(logspace_array(3, 5))


# zad 5

def do_something(length):
	wektor = np.arange(length)[::-1]
	return np.diag(wektor, 2)


print(do_something(5))


# zad 6

def wykreslanka():
	krzysztof = np.array(list('krzysztof'))
	domek = np.array(list('domek    '))[::-1]
	skos = np.diag(np.array(list('skos')), -5)
	pionowo = np.array(list('pionowo'))
	skos[0] = krzysztof
	skos[1] = domek
	np.append(skos, pionowo)
	return skos


print(wykreslanka())
