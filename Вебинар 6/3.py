field = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

def print_field(field):
    for el in field:
        print(el)

def fill_num_in_field(field, n):
    for el in field:
        for i in range(len(el)):
            if el[i] == n:
                el[i] = 'x'

print_field(field)

a = int(input('Введите цифру, куда хотите поставить крестик: '))
fill_num_in_field(field, a)
print_field(field)
