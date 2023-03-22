#Задание3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

month = int(input("Введите номер месяца от 1 до 12: "))
my_list = ('зима', 'весна', 'лето', 'осень')
my_dict = {1:'winter', 2:'spring', 3:'summer', 4:'autumn'}
if month < 3 or month == 12:
    print(my_list[0])
    print(my_dict.get(1))
elif month >= 3 and month < 6:
    print(my_list[1])
    print(my_dict.get(2))
elif month >= 6 and month < 9:
    print(my_list[2])
    print(my_dict.get(3))
elif month >= 9 and month < 12:
    print(my_list[3])
    print(my_dict.get(4))
else: print("Вы ввели неверный номер месяца")


