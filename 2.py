# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = map(int, input("Введите значения X, Y, Z через запятую: ").split(","))
left_statement = not (x or y or z)
right_statement = not x and not y and not z
if left_statement == right_statement:
    print("Истина")
else:
    print("Ложь")