my_var = int(input("Введите целое положительное число:"))
x = -1
while my_var > 10:
    d = my_var % 10
    my_var //= 10
    if d > x:
        x = d
print(x)