# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

numbers = int(input("Введите число N: "))
n = list(range(-numbers, numbers+1))
print(n, end = ' ')

path = 'text.txt'
data = open(path, 'r')
datalist = [int(line.strip()) for line in data]
print('\n',datalist)
data.close()

mult = 1
for i in datalist:
    mult *= n[i]

print(mult)
