a = int(input("Кол-во километров в 1 день"))
b = int(input("Цель:"))
counter = 1
while (a != b) and (a < b):
    a = a + a/10
    counter+=1
print(counter)
