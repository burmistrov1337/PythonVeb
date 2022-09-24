# Вывести на экран числа от -N до N

n = int(input ("Введите число N: "))
r = range(-n,n+1)
for i in r:
    print(i, end=' ')