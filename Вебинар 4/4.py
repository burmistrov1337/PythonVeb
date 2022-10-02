# Найти НОК двух чисел
import math

nok1 = int(input("Введите число M: "))
nok2 = int(input("Введите число N: "))


nok = 0
min = nok1
if nok2 < min:
    min = nok2
nok = (nok1 * nok2)// math.gcd(nok1, nok2)
print(nok)


