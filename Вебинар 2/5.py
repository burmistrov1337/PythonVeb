# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.
a = int(input("Введите число: "))
maxNumber = 0
while a > 0:
    b = a % 10
    if b > maxNumber:
        maxNumber = b
        if maxNumber == 9:
            break
    a //= 10

print(maxNumber)
