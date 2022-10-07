# 1) Вычислить число π c заданной точностью d

# *Пример:*

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# def π(n):
#     k = 1
#     s = 0

#     for i in range(n):
#         if i % 2 == 0:
#             s += 4 / k
#         else:
#             s -= 4 / k
#             k += 2


# d = int(input("Введите точность поиска числа π: "))
# print(π(d))

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# n = 20000000

# mypi = 4 * (sum(1/x for x in range(1, n + 1, 4)) + sum(-1/x for x in range(3, n + 1, 4)))

# print(format(mypi, '.4'))



k = 1
s = 0

for i in range(10000000):
    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4/k
    k += 2

print(s)
