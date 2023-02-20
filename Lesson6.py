"""
1. Создать класс TrafficLight (светофор).
- определить у него один атрибут color (цвет) и метод running (запуск);
- атрибут реализовать как приватный;
- в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
- продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
- переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
- проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт
"""
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Режим светофора: \n\t '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


a = TrafficLight()
a.running()

"""
2. Реализовать класс Road (дорога).
- определить атрибуты: length (длина), width (ширина);
- значения атрибутов должны передаваться при создании экземпляра класса;
- атрибуты сделать защищёнными;
- определить метод расчёта массы асфальта, необходимого для покрытия всей 
дороги;
- использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. 
метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
- проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т
"""


class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def get_mass(self, mass_1m2: int, thickness: int) -> int:
        mass = self._length * self._width * mass_1m2 * thickness // 1000
        return mass


road = Road(5000, 20)
assert road.get_mass(25, 5) == 12500

"""
3. Реализовать базовый класс Worker (работник).
- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
- создать класс Position (должность) на базе класса Worker;
- в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
- проверить работу примера на реальных данных: создать экземпляры класса 
Position, передать данные, проверить значения атрибутов, вызвать методы 
экземпляров.
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int,
                 bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


vasya = Position('Илья', 'Иванов', 'Айтишник', 100000, 20000)
print(vasya.get_full_name())
print(vasya.position)
print(vasya.get_total_income())

"""
4. Реализуйте базовый класс Car.
- у класса должны быть следующие атрибуты: speed, color, name, is_police 
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к 
атрибутам, выведите результат. Вызовите методы и покажите результат
"""


class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Не можем повернуть - мы стоим на месте')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(auto):
    print(f"Тест-драйв {'полицейского' if auto.is_police else 'гражданского'} "
          f"автомобиля {auto.name}, цвет {auto.color}")
    auto.go(40)
    auto.show_speed()
    auto.turn('направо')
    auto.stop()
    auto.show_speed()
    auto.turn('налево')
    auto.go(60)
    auto.show_speed()
    auto.go(120)
    auto.show_speed()
    auto.stop()
    print("Тест-драйв окончен", end="\n\n")


car = Car('белый', 'Kia Optima', False)
test_drive(car)

polo = TownCar('коричневый', 'Volkswagen Polo')
test_drive(polo)

veyron = SportCar('желтый', 'Bugatti Veyron')
test_drive(veyron)

largus = WorkCar('красный', 'Lada Largus')
test_drive(largus)

mondeo = PoliceCar('синий', 'Ford Mondeo')
test_drive(mondeo)

"""
5. Реализовать класс Stationery (канцелярская принадлежность).
- определить в нём атрибут title (название) и метод draw (отрисовка). Метод 
выводит сообщение «Запуск отрисовки»;
- создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
- в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
- создать экземпляры классов и проверить, что выведет описанный метод для 
каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашем {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")


stationery = Stationery('Гусиное перо')
stationery.draw()

pen = Pen('Гелевая')
pen.draw()

pencil = Pencil('Учебный')
pencil.draw()

handle = Handle('Для белой доски')
handle.draw()
