# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 10.01]

def pairs(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]-int(numbers[-1]))
        del numbers[0]
        del numbers[-1]
    return results
print(pairs(numbers))

# n = array
# max = 0
# min = [0]
# for i in range(len(n)):
#     if n[i]>max:
#         max = n[i]
#     elif n[i]<min:
#         min = n[i]
# result = max - min
# print(f"Разница между максимальным и минимальным значением дробной части элементов равна: {result}")