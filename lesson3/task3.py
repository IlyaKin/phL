#Задание3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает
# сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    max_args = []
    if arg1 < arg2 and arg1 < arg3:
        max_args.append(arg2)
        max_args.append(arg3)
    elif arg2 < arg1 and arg2 < arg3:
        max_args.append(arg1)
        max_args.append(arg3)
    else:
        max_args.append(arg1)
        max_args.append(arg2)
    return max_args[0]+max_args[1]

print(my_func(6, 12, 186))