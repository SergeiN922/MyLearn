"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('11 - 1 - 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(1, 11, 2000))
"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на 
ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не 
завершиться с ошибкой.
"""


class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def smart_divider(a, b):
    if b == 0:
        raise DivisionByZeroError(f'{a} / {b} = На ноль делть нельзя!')
    return a / b


try:
    smart_divider(6, 0)
except DivisionByZeroError as e:
    print(e)

print(f"45 / 5 = {smart_divider(45, 5)}")

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое 
списка на наличие только чисел. Проверить работу исключения на реальном 
примере. Запрашивать у пользователя данные и заполнять список необходимо только
числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду 
«stop». При этом скрипт завершается, сформированный список с числами выводится 
на экран. Подсказка: для этого задания примем, что пользователь может вводить 
только числа и строки. Во время ввода пользователем очередного элемента 
необходимо реализовать проверку типа элемента. Вносить его в список, только 
если введено число. Класс-исключение должен не позволить пользователю ввести 
текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class NaNError(Exception):
    def __init__(self, txt):
        self.txt = txt


def number_filter(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            raise NaNError(f'Error: {string} - is not a number')


input_txt = ''
counter = 1
numbers_list = []
print("Введите числа по одному, для выхода введите 'stop'")
while input_txt != 'stop':
    try:
        input_txt = input(f"{counter}: ")
        numbers_list.append(number_filter(input_txt))
        counter += 1
    except NaNError as e:
        if input_txt != 'stop':
            print(e.txt)

print(f"Result list:\n{numbers_list}")

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий 
склад. А также класс «Оргтехника», который будет базовым для 
классов-наследников. Эти классы —конкретные типы оргтехники (принтер, сканер, 
ксерокс). В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
"""

"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
за приём оргтехники на склад и передачу в определённое подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также 
других данных, можно использовать любую подходящую структуру (например, 
словарь).
"""
"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации 
вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на  склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум 
возможностей, изученных на уроках по ООП.
"""
# 4-6 задания объединены


class Warehouse:
    __storage = []
    __summary = {}

    def push(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise Exception('Склад может принимать только оргтехнику')
        self.__storage.append(equipment)
        if self.__summary.get(equipment.type) is not None:
            self.__summary[equipment.type] += 1
        else:
            self.__summary.setdefault(equipment.type, 1)

    def report_items(self):
        for item in self.__storage:
            print(item)

    def report_total(self):
        for k, v in self.__summary.items():
            print(f'{k}: {v} шт')


class OfficeEquipment:
    def __init__(self, type: str, model: str, cost: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)


class Scanner(OfficeEquipment):
    def __init__(self, model: str, cost: float, dpi: str, sn: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)


class Copier(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str,
                 velocity: int, sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('МФУ', model, cost, sn)


if __name__ == '__main__':
    printer01 = Printer('Epson L120', 7300.12, True, 'N6SS549876548')
    printer02 = Printer('HP Laser 107a', 6600, False, 'FG64855SFG5')
    scanner01 = Scanner('Epson Perf V19', 5010, '4800x4800', '65482321FF5')
    scanner02 = Scanner('Canon LiDE 300', 4700.45, '2400x2400', '31313131FFF')
    copier01 = Copier('Canon PIXMA MG2540S', 2299.73, True, '4800x600', 8,
                      'FG8#HHHF')
    copier02 = Copier('Brother MFC-L2720DWR', 19100, False, '2400x600', 30,
                      '9BB654852133')
    copier03 = Copier('HP LaserJet M132nw', 14604.20, False, '1200x1200', 22,
                      '9BB654848554')

    warehouse = Warehouse()
    warehouse.push(printer01)
    warehouse.push(printer02)
    warehouse.push(scanner01)
    warehouse.push(scanner02)
    warehouse.push(copier01)
    warehouse.push(copier02)
    warehouse.push(copier03)

    warehouse.report_items()
    warehouse.report_total()

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс 
«Комплексное число». Реализуйте перегрузку методов сложения и умножения 
комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры 
класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return ComplexNumber(a, b)

    def __str__(self):
        return f'{self.a} + {self.b}i'


if __name__ == '__main__':
    z1 = ComplexNumber(2, 5)
    z2 = ComplexNumber(3, 6)
    z3 = z1 + z2
    z4 = z1 * z2

    print(f'z1 = {z1}')         # z1 = 2 + 5i
    print(f'z2 = {z2}')         # z2 = 3 + 6i
    print(f'z1 + z2 = {z3}')    # z1 + z2 = 5 + 11i
    print(f'z1 * z2 = {z4}')    # z1 * z2 = -24 + 27i
