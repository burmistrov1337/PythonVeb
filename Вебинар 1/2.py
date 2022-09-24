# Найти максимальное из пяти чисел

numbers = [1,2,3,4,5]
print (numbers)
max = numbers[0]
for i in numbers:
    if i > max: 
        max = i
print (max)