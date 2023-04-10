# Задание2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т

class Road:
    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _spec_weight: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):

        self._length = float(length)
        self._width = float(width)

    def calc_m(self, thickness: float) -> [float, None]:
        try:
            return (self._length * self._width
                    * thickness * self._spec_weight)
        except TypeError:
            return None


if __name__ == '__main__':
    try:
        road = Road(3000, 6)
        print(
            'Масса дорожного покрытия:',
            road.calc_m(10),
            'тонн'
        )
    except TypeError:
        print('Впишите длинну и ширину дороги')

