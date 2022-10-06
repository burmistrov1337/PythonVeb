# 2) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [6, 5, 4, 3, 2] => [12, 15, 16];
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


numbers = [6, 5, 4, 3, 2]


def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0]
        del numbers[-1]
    if len(numbers) == 1:
        results.append(numbers[0]**2)
    return results
print(pairs_mult(numbers))