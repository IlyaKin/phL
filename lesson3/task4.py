#Задание4.Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания
# нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(x, y):
    if x < 0 or y > 0:
        print("Введите правильный набор чисел, где x>0, y<0")
    else:
        print(x ** y)
        res = 1
        for i in range(abs(y)):
            res *= x
        print(1 / res)


x = int(input("Введите положительное х: "))
y = int(input("Введите отрицательное y: "))
my_func(x, y)
