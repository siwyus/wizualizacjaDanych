import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# ZAD 1
# x = np.arange(1, 20)
# plt.plot(x, 1 / x)
# plt.title('Wykres funkcji f(x) dla x [1,20]')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend(labels=['f(x) = 1/x'])
# plt.axis([1, len(x), 0, 1])
# plt.show()
#
# # ZAD 2
#
# # x = np.arange(1, 20)
# plt.plot(x, 1 / x, 'g:')
# plt.plot(x, 1 / x, 'g>')
# plt.title('Wykres funkcji f(x) dla x [1,20]')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend(labels=['f(x) = 1/x'])
# plt.axis([0, len(x) + 1, 0, 1])
# plt.show()
#
# # ZAD 3
#
# x2 = np.arange(0, 30, 0.1)
# s = np.sin(x2)
# c = np.cos(x2)
# plt.subplot(2, 1, 1)
# plt.plot(s)
# plt.title('wykres sin(x)')
# plt.legend(labels=['sin(x)'])
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.grid()
#
# plt.subplot(2, 1, 2)
# plt.plot(c)
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.legend(labels=['cos(x)'])
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.grid()
# plt.show()

# ZAD 4

# df = pd.read_csv('iris.data', header=None, sep=',', decimal=".")
# plt.scatter(df[0], df[1], c=np.random.randint(0, 150, 150), s=df[0] - df[1])
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.title('Wykres punktowy danych z iris')
# plt.show()

# ZAD 5
imiona_xsls = pd.ExcelFile('imiona.xlsx')
i = pd.read_excel(imiona_xsls, header=0)
print(i)
etykiety = list(i.Plec.unique())
etykiety.reverse()
slupki = i.groupby(by='Plec')['Liczba'].sum()
print(slupki)
print(etykiety)
plt.bar(x=etykiety, height=slupki)
# i = i.groupby(by='Plec').agg({'Liczba': ['sum']})
# d = i.plot.bar(subplots=True)
# d.set_xlabel('Płeć')
# d.set_ylabel('Liczba urodzeń')
# d.set_title('Liczba urodzeń z podziałem na płeć')
# d.legend(labels=['kobiety', 'mężczyźni'])

plt.show()
