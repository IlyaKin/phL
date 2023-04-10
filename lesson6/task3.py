# Задание3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage: float = 0, bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return ' '.join(sorted([self.name, self.surname]))

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Ilya',
            'surname': 'Iliin',
            'position': 'Developer',
            'wage': 40000,
            'bonus': 60000
        },
        {
            'name': 'Fedor',
            'surname': 'Shapkin',
            'position': 'Senior',
            'wage': 100000,
            'bonus': 80000
        }]
    for item in position_data:
        position = Position(**item)

        print('Имя: ', position.name)
        print('Фамилия: ', position.surname)
        print('Имя и Фамилия: ', position.get_full_name())
        print('Доход: ', position.get_total_income())
