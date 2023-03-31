#Задание1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.


with open("file.txt", "w", encoding='utf-8') as myfile:
    line=input("Введите строку \n")
    while line:
        myfile.writelines(line+'\n')
        line=input("Введите строку \n")
        if not line:
            break
