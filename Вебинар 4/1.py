# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Input the number: '))
d = {i : 3*i + 1 for i in range(1,number+1)}
print(f"Dictionary: {d}")



# d = {'one': None }
# d['one'] = 5
# d['two'] = 6
# d.update(three=7, four=8, five=9) # withiut 
# d.update(three='7', four='8', five='9') # str'7'
# d.setdefault('six', )
# d.update({'ten': 3})
# d.update({'one': 3}) # переопределение
# print(d)
