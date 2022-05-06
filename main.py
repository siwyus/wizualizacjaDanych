import pandas as pd

# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
# print(s)

# ZAD 1

# imiona_xsls = pd.ExcelFile('datasets/imiona.xlsx')
# imiona = pd.read_excel(imiona_xsls, header=0)
# print(imiona)

# ZAD 2
# print('\nRekordy gdzie liczba nadanych imion była większa od 1000 w danym roku\n')
# print(imiona[(imiona.Liczba > 1000)])
# print('\nRekordy o imieniu Krzysztof\n')
# print(imiona[imiona.Imie == 'KRZYSZTOF'])
# print('\nLiczba wszystkich urodzonych dzieci w całym okresie\n')
# print(imiona.Liczba.sum())
# print('\nLiczba wszystkich urodzonych dzieci w danym okresie(od 2000 do 2005)\n')
# print(imiona[(imiona.Rok > 2000) & (imiona.Rok < 2010)].Liczba.sum())
# print('\nSuma urodzonych chlopcow\n')
# print(imiona[imiona.Plec == 'M'].Liczba.sum())
# print('\nSuma urodzonych chlopcow\n')
# print(imiona[imiona.Plec == 'K'].Liczba.sum())
# print('\nNajbardziej popularne imie dziewczynki i chlopca w calym okresie')
# most_popular_woman = imiona[imiona.Plec == 'K'].sort_values(by='Liczba', ascending=False).head(
# 	1)
# most_popular_man = imiona[imiona.Plec == 'M'].sort_values(by='Liczba', ascending=False).head(
# 	1)
# most_popular = pd.DataFrame(most_popular_woman).append(most_popular_man)
# print(most_popular)
# print('\nNajbardziej popularne imie dziewczynki i chlopca w danym roku')
# most_popular_woman1 = imiona[imiona.Plec == 'K'].sort_values(by='Liczba').drop_duplicates('Rok', keep='last')
# most_popular_man1 = imiona[imiona.Plec == 'M'].sort_values(by='Liczba').drop_duplicates('Rok', keep='last')
#
# most_popular1 = pd.DataFrame(most_popular_woman1).append(most_popular_man1)
# print(most_popular1.sort_values(by='Rok'))

# ZAD 3

zamowienia_csv = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';')
zamowienia = pd.DataFrame(zamowienia_csv)
print(zamowienia)
print('\nLista unikalnych sprzedawcow\n')
print(zamowienia.Sprzedawca.unique())
print('\n5 najwwiekszych wartosci zamowien\n')
print(zamowienia.sort_values(by='Utarg', ascending=False).head(5))
print('\nilosc zamowien zlozonych przez kazdego sprzedawce\n')
print(zamowienia.groupby(by='Sprzedawca').size())
print('\nsuma zamowien dla kazdego kraju\n')
print(zamowienia.groupby(by='Kraj').agg({'Utarg': ['sum']}))
print('\nsuma zamówień w roku 2005 dla sprzedawcow z Polski\n')
print(zamowienia[(zamowienia.Kraj == 'Polska') & (zamowienia['Data zamowienia'] >= '2005-01-01') & (
		zamowienia['Data zamowienia'] <= '2005-12-31')].agg(
	{'Utarg': ['sum']}))
print('\nsrednia kwota zamowien w 2004roku\n')
print(zamowienia[(zamowienia['Data zamowienia'].str[:4] == '2004')].agg({'Utarg': ['mean']}))

s = zamowienia[(zamowienia['Data zamowienia'].str[:4] == '2004')]
s2 = zamowienia[(zamowienia['Data zamowienia'].str[:4] == '2005')]
s.to_csv('2004.csv', index=False)
s2.to_csv('2005.csv', index=False)
