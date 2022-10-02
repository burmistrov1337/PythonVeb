# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел
ls1 = input("Введите набор чисел: ")

ls2 = ls1.split(' ')
print(ls2)

min = ls2[0]
max = ls2[0]

for i in range(len(ls2)):
    if int(ls2[i]) > int(max):
        max = ls2[i]
    elif int(ls2[i]) < int(min):
        min = ls2[i]
print(f'max number = {max}, min number = {min}')
