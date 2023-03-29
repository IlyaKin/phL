#Задание1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
#Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
#значений необходимо запускать скрипт с параметрами.

from sys import argv
from itertools import count

if len(argv) > 1:
    script_name, hours, salary, premium = argv
    hours = int(hours)
    salary = int(salary)
    premium = int(premium)
    result = (hours * salary) + premium
    print(result)
else:
    hours = int(input("Введите кол-во отработанных часов: "))
    salary = int(input("Введите ставку в час: "))
    premium = int(input("Введите размер премии в рублях: "))
    result = (hours * salary) + premium
    print(result)
