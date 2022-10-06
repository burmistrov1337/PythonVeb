# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 4.3, 10.02]


def pairs(numbers):
    results = []
    while len(numbers) != 0:
        st = round((numbers[0]-int(numbers[0])), 2)
        results.append(st)
        del numbers[0]
    return results


array = pairs(numbers)
array1 = max(array) - min(array)
print(f'{array1:.2f}')


# array = pairs(numbers)

# max = [0]
# max1 = [i for i in array if array[i] > max]
# print(max1)
# min = [0]

# for i in range(len(array)):
#     if array[i] > max:
#         max = array[i]
#     elif array[i] < min:
#         min = array[i]

# result = max - min
# print(f"Разница между максимальным и минимальным значением дробной части элементов равна: {result}")
