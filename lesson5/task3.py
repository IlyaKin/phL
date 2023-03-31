# Задание3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину
# их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open("file3.txt", "r", encoding='utf-8') as file3:
    salary_list = file3.readlines()
    count_salary = 0
    for i in range(len(salary_list)):
        line=salary_list[i].split()
        salary=float(line[1])
        count_salary += float(line[1])
        if salary<20000:
            print(line[0])
    print(f"Средняя зарплата = {count_salary/len(salary_list)}")