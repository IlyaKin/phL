# Задание4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, color: str, name: str, is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        try:
            self.speed = float(speed)
        except ValueError:
            pass
    def stop(self):
        self.speed = 0

    def turn(self, direction: str):
        if direction not in ('left', 'right'):
            print(f"'{direction}' неверное неправление")
            return

        if not self.speed:
            print(f"'Невозможно повернуть на {direction}' на месте")
            return

        self._direction = direction

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')

        if (hasattr(self, 'max_speed')
                and self.max_speed
                and self.speed > self.max_speed):
            print(f'Превышение скорости на {self.speed - self.max_speed} км/ч')

    @property
    def direction(self):
        return self._direction


class TownCar(Car):
    max_speed = 60


class SportCar(Car):
    pass


class WorkCar(Car):
    max_speed = 40


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_data = {
        ('Red', 'Skoda Yeti'): TownCar,
        ('Yellow', 'Lambo Diablo'): SportCar,
        ('White', 'Lada Largus'): WorkCar,
        ('Blue', 'Toyota Camry'): PoliceCar,
    }

    for car_desc, car_item in cars_data.items():
        car = car_item(*car_desc)

        print(f"Модель машины '{car.name}'")
        print(f"Цвет '{car.color}'")
        print(f"Это полицейская машина? '{car.is_police}'")
        print(f"Скорость '{car.speed}'")
        print(f"Направление движения '{car.direction}'")
        print(f"Текущая скорость: '{car.show_speed()}'")

        car.turn('asd')
        car.turn('left')
        car.go('asd')
        print("Превышение на: ", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('left')
        print(f"Направление '{car.direction}'")
        car.turn('right')
        print(f"Направление '{car.direction}'")
        car.stop()
        car.show_speed()


