# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите координаты x: "))
if x == 0:
    x = int(input("x не должно быть равным 0! Введите коордиаты x: "))
y = int(input("Введите координаты y: "))
if y == 0:
    y = int(input("y не должно быть равным 0! Введите коордиаты y: "))
if x > 0 and y > 0:
    print("1 четверть")
elif x < 0 and y > 0:
    print("2 четверть")
elif x < 0 and y < 0:
    print("3 четверть")
elif x > 0 and y < 0:
    print("4 четверть")