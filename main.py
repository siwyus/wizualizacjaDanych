import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# print(ts)
#
# ts.plot()
# plt.show()

# ZAD 1
imiona_xsls = pd.ExcelFile('datasets/imiona.xlsx')
imiona = pd.read_excel(imiona_xsls, header=0)
print(imiona)

zad1 = imiona.groupby(by='Rok').agg({'Liczba': ['sum']})
zad1.plot(kind='line', xlabel='Rok urodzenia',
		  ylabel='Liczba urodzeń', legend=False,
		  title='Liczba urodzeń dzieci w danym roku',
		  xticks=imiona.Rok.unique(), rot=90, figsize=(12, 8))
plt.show()

# ZAD 2
zad2 = imiona.groupby(by='Plec').agg({'Liczba': ['sum']})
d = zad2.plot.bar(legend=False)
d.set_xlabel('Płeć')
d.set_ylabel('Liczba urodzeń')
d.set_title('Liczba urodzeń z podziałem na płeć w latach 2000-2017')
d.ticklabel_format(axis='y', style='plain')
plt.show()

# ZAD 3
zad3 = imiona[(imiona.Rok >= 2013)] \
	.groupby(['Plec']) \
	.agg({'Liczba': ['sum']})
zad3.plot(kind='pie', subplots=True, legend=False,
		  autopct='%1.1f%%', ylabel='Liczba urodzen', colors=['Pink', 'lightBlue'],
		  title='Procent urodzonych chłopców i dziewczynek w latach 2013-2017')
plt.show()

# ZAD 4
zamowienia_csv = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';')
zamowienia = pd.DataFrame(zamowienia_csv)
zad4 = zamowienia.groupby(by='Sprzedawca').size()
zad4.plot(kind='bar', xlabel='Sprzedawca', ylabel='Ilość zamówień',
		  legend=False, title='Ilość zamówień dla poszczególnych sprzedawców',
		  figsize=(12, 10))
plt.show()
