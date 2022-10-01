# Реализовать алгоритм перемешивания списка. 
original = [0, 2, 4, 6, 9] 
print(original)

import time


from time import time

def time_random():
 return time() - float(str(time()).split('.')[0])


def random_number(min, max):
 return int(time_random() * (max - min) + min)

def mixing_list(array):
    for i in range(0, len(array)):
        rnd_position = int(random_number(0, len(array)))
        temp1 = original[i]
        original[i] = original[rnd_position]
        original[rnd_position] = temp1

mixing_list(original)
print(original)