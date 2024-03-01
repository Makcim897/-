import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
a = int(input())#Вводим строку
b = int(input())#Вводим строку
article = pd.read_csv('data1.csv', delimiter=';',names=['user_id', 'user_name', 'user_age'])#Читаем CSV
print(article.iloc[a-1, b-1])#Выводим что выбрал пользователь

article = pd.read_csv('data1.csv', delimiter=';',names=['user_id', 'user_height', 'user_age'])#Читаем CSV
x = article["user_height"]#\
y = article["user_id"]#     |задаем от куда брать х и у
fig, ax = plt.subplots()#Задаем значение ax
ax.plot(x, y, linewidth=2.0)#Задаем тип линий
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),#  \
       ylim=(0, 8), yticks=np.arange(1, 8))#   |Задаем лимиты
plt.xlabel("x")#  \
plt.ylabel("y")#   |Подписываем х и у лабел
plt.show()# Вынимаем пирог из печи и он готов можете смотреть


plt.style.use('_mpl-gallery')
n_radii = 8
n_angles = 36
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]#создание масивав
x = np.append(0, (radii*np.cos(angles)).flatten())#  |Создаем пробелы между радиусами и углами
y = np.append(0, (radii*np.sin(angles)).flatten())# /
z = np.sin(-x*y)#синус от -х*у
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})#настройки 3д
ax.plot_trisurf(x, y, z, vmin=z.min() * 2, )
ax.set(xticklabels=[],#\
       yticklabels=[],# >устанавливаем x,y,z
       zticklabels=[])#/
plt.show()# Вынимаем чипсы из печи и он готов можете смотреть
