# Задание4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
result_file = []
with open('file4.txt', 'r') as file4:
    for i in file4:
        i = i.split(' ', 1)
        result_file.append(rus[i[0]] + '  ' + i[1])
    print(result_file)

with open('file4_new.txt', 'w') as file4new:
    file4new.writelines(result_file)