# class Ksztalty:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
# 		self.opis = 'Klasa dla podstawowych kształtów'
#
# 	def pole(self):
# 		return self.x * self.y
#
# 	def obwod(self):
# 		return 2 * (self.x + self.y)
#
# 	def dodaj_opis(self, tekst):
# 		self.opis = tekst
#
# 	def skalowanie(self, czynnik):
# 		self.x = self.x * czynnik
# 		self.y = self.y * czynnik
#
#
# class Kwadrat(Ksztalty):
# 	def __init__(self, x):
# 		self.x = x
# 		self.y = x
#
# 	def __str__(self):
# 		return 'kwadrat o boku {}'.format(self.x)
#
# class KwadratLiteral(Kwadrat):
# 	def pole(self):
# 		return 3 * self.x * self.y
#
# 	def obwod(self):
# 		return 8 * self.x
#
#
# kwadrat = Kwadrat(5)
# print(kwadrat.__str__())
# print(kwadrat.pole())
# print(kwadrat.obwod())
#
# # print(kwadrat.opis)
# kwadrat.dodaj_opis('Ta figura to kwadrat')
# print(kwadrat.opis)
#
# kwadrat.skalowanie(0.3)
# print(kwadrat.pole())
# print(kwadrat.obwod())
#
# litera_l = KwadratLiteral(5)
# print(litera_l.pole())
# print(litera_l.obwod())
#
# litera_l.dodaj_opis('Kwadraty ułożone w literę L')
# print(litera_l.opis)
#
# litera_l.skalowanie(0.3)
# print(litera_l.pole())
# print(litera_l.obwod())
#


# class Osoba:
# 	def __init__(self, imie, nazwisko):
# 		self.imie = imie
# 		self.nazwisko = nazwisko
#
# 	def przestaw_sie(self):
# 		return 'Nazywam się {} {}'.format(self.imie, self.nazwisko)
#
#
# class Pracownik():
# 	def __init__(self, pensja):
# 		# super().__init__(imie, nazwisko)
# 		# Osoba.__init__(self, imie, nazwisko)
# 		self.pensja = pensja
#
# 	def przestaw_sie(self):
# 		return 'Nazywam się {} {} i zarabiam {}'.format(self.imie, self.nazwisko, self.pensja)
#
#
# class Menadzer(Osoba, Pracownik):
# 	def __init__(self, imie, nazwisko, pensja):
# 		Osoba.__init__(self, imie, nazwisko)
# 		Pracownik.__init__(self, pensja)
#
# 	def przestaw_sie(self):
# 		return 'Nazywam się {} {}, jestem menadżerem i zarabiam {}'.format(self.imie, self.nazwisko, self.pensja)
#
#
# # jozek = Pracownik('Józef', 'Bajka', 2000)
# adrian = Menadzer('Adrian', 'Mikulski', 10000)
#
# # print(jozek.przestaw_sie())
# print(adrian.przestaw_sie())

# for i in range(1, 10):
# 	print(i)

# imie = 'Reks'
#
# it = iter(imie)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# class Wspak:
# 	def __init__(self, data):
# 		self.data = data
# 		self.index = len(data)
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		if self.index == 0:
# 			raise StopIteration
# 		self.index -= 1
# 		return self.data[self.index]
#
# napis = Wspak('Reks')
# print(napis.__next__())
# print(napis.__next__())
#
# for a in napis:
# 	print(a)

# def reverse(data):
# 	for a in range(len(data)-1, -1, -1):
# 		yield data[a]
#
#
# gen = reverse('Napis')
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))

