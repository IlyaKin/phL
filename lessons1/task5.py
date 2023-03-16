proceeds = int(input("Введите значение выручки:"))
costs = int(input("Введите значение издержек:"))
if proceeds > costs:
    print(f"Ваша прибыль составляет: {proceeds-costs}")
    rent = (proceeds-costs)/proceeds
    print(f"Рентабельность составила: {rent}")
    count_workers = int(input("Введите кол-во сотрудников:"))
    print(f"Прибыль фирмы на одного сотрудника составляет:{(proceeds-costs)/count_workers}")

elif proceeds == costs:
    print("Вы вышли в ноль")
else:
    print(f"Ваш убыток составляет:{costs-proceeds}")