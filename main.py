import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# pierwszy wykres liniowy
# sns.set(rc={'figure.figsize': (8, 8)})
# array = [1, 2, 3, 4]
# sns.lineplot(x=array, y=[x ** 2 for x in array], label='linia nr1', color='red', marker='o', linestyle=':')
# sns.lineplot(x=array, y=[x ** 2 + 1 for x in array], label='linia nr2', color='green', marker='^', linestyle=':')
#
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres liniowy')
# plt.show()

# drugi wykres liniowy
# s = pd.Series(np.random.randn(1000)).cumsum()
# sns.set()
# wykres = sns.relplot(kind='line', data=s, label='linia')
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('Wykres liniowy losowych danych')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
# plt.show()

# trzeci wykres liniowy


# wykres punktowy
# sns.set()
# data = {'a': np.arange(50),
# 		'c': np.random.randint(0, 50, 50),
# 		'd': np.random.randn(50)}
#
# data['b'] = data['a'] + 10 * data['c']
# data['d'] = np.abs(data['d']) * 100
#
# df = pd.DataFrame(data)
# plot = sns.relplot(data=df, x='a', y='b', hue='c', palette='bright', size='d', legend=False)
# plot.fig.set_size_inches(6, 6)
# # plot.set(xticks=data['a'])
# plt.show()

# wykres kolumnowy
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
# 		'Stolica': ['Bruksela', 'New Delphi', 'Brasilia', 'Warszawa'],
# 		'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
# 		'Populacja': [11190846, 1303171035, 207847528, 38675467]}
#
# df = pd.DataFrame(data)
# sns.set(rc={'figure.figsize': (8, 6)})
# # pierwszy sposób
# # plot = sns.catplot(data=df, x='Kontynent', y='Populacja', kind='bar', ci=None, hue='Kontynent', estimator=np.sum,
# # 				   dodge=False, palette=['red', 'green', 'yellow'], legend_out=False)
# # plot.fig.set_size_inches(8, 6)
# # plot.add_legend(title='Populacja na kontynentach', loc='upper right')
# # plot.fig.suptitle('Populacja na kontynentach')
#
# # drugi sposób
# plot = sns.barplot(data=df, x='Kontynent', y='Populacja', ci=None, hue='Kontynent', estimator=np.sum,
# 				   dodge=False, palette=['red', 'green', 'yellow'])
# plot.legend(title='Populacja na kontynentach')
# plot.set(title='Wykres słupkowy')
# plt.show()

# wykres liniowy 3d
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# print(type(ax))
#
# t = np.linspace(0, 2 * np.pi, 100)
# z = t
# x = np.sin(t) * np.cos(t)
# y = np.tan(t)
# ax.plot(x, y, z, label='zadanie 1')
# ax.legend()
# plt.show()

# wykres punktowy 3d

np.random.seed(19680801)


def randrange(n, vmin, vmax):
	return (vmax - vmin) * np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100

for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
	xs = randrange(n, 23, 32)
	ys = randrange(n, 0, 100)
	zs = randrange(n, zlow, zhigh)
	ax.scatter(xs, ys, zs, c=c, marker=m)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.view_init(elev=10, azim=-35)
plt.show()
