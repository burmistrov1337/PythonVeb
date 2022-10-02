# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
import math

a = float(input("Введите число A: "))
b = float(input("Введите число B: "))
c = float(input("Введите число C: "))

discr = b ** 2 - 4 * a * c
print(f"Дискриминант D = {round (discr,2)}")

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {round(x1,2)}")
    print(f"x2 = {round(x2,2)}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"x = {round(x,2)}")
else:
    print("Корней нет")
