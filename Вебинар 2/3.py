# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
# Используйте форматирование строк. 3661
import datetime
sec = int(input('Введите время в секундах: '))
hours = (sec//3600)
minutes = (sec%3600)//60
seconds = sec%60

timeobj = datetime.time(hours, minutes, seconds)
print(timeobj)


