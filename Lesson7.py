"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data: list):
        self.data = data

    def __str__(self):
        result = []
        for row in self.data:
            result.append(' '.join([str(k) for k in row]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.data) == len(other.data):
            result = []
            for i, row in enumerate(self.data):
                new_list = list(map(lambda x, y: x + y, row, other.data[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return



list_lists_01 = [[1, 2, 3], [3, 3, 3], [4, 3, 2]]
list_lists_02 = [[2, 5, 5], [4, 3, 3], [1, 1, 2]]

matrix01 = Matrix(list_lists_01)
matrix02 = Matrix(list_lists_02)
matrix03 = matrix01 + matrix02

print(matrix01, end='\n\n')
print(matrix02, end='\n\n')
print(matrix03)

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь 
определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост 
(для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для 
пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на
реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на 
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


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


class Suit(Clothes):
    def __init__(self, name: str, height: int):
        self.height = height
        super().__init__(name)

    @property
    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 2)


if __name__ == '__main__':
    green_coat = Coat('Зеленое махровое пальто, зима-лето 2020', 56)
    yellow_suit = Suit('Желтный двубортный костюм с блестками', 45)
    print(green_coat.fabric_consumption)
    print(yellow_suit.fabric_consumption)

"""
3) Реализовать программу работы с органическими клетками, состоящими из ячеек. 
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, 
соответствующий количеству ячеек клетки (целое число). В классе должны быть 
реализованы методы перегрузки арифметических операторов: сложение (__add__()), 
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные 
методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
умножение и целочисленное (с округлением до целого) деление клеток, 
соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно 
равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если 
разность количества ячеек двух клеток больше нуля, иначе выводить 
соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки 
определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр 
класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки 
по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где 
количество ячеек между \n равно переданному аргументу. Если ячеек на 
формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class OrganicCell(object):
    def __init__(self, size: int):
        if size <= 0:
            raise Exception('Клетка не может иметь меньше одной ячейки')
        self.size = size

    def __add__(self, other):
        return OrganicCell(self.size + other.size)

    def __sub__(self, other):
        result = self.size - other.size
        if result > 0:
            return OrganicCell(result)
        else:
            raise Exception(f'Ошибка! Вычитание {self} из {other} невозможно!')

    def __mul__(self, other):
        return OrganicCell(self.size * other.size)

    def __truediv__(self, other):
        return OrganicCell(self.size // other.size)

    def make_order(self, row_size: int) -> str:
        rows = ['*' * row_size for _ in range(self.size // row_size)]
        tail = '*' * (self.size % row_size)
        rows.append(tail)
        return '\n'.join(rows)

    def __str__(self):
        return '*' * self.size


if __name__ == '__main__':
    ameba_1 = OrganicCell(2)
    ameba_2 = OrganicCell(6)
    ameba_add = ameba_1 + ameba_2
    try:
        ameba_sub1 = ameba_1 - ameba_2
    except Exception as e:
        ameba_sub1 = None
        print(e)
    ameba_sub2 = ameba_2 - ameba_1
    ameba_mul = ameba_1 * ameba_2
    ameba_div = ameba_2 / ameba_1

    print('ameba_1\t', ameba_1)
    print('ameba_2\t', ameba_2)
    print('add\t\t', ameba_add)
    print('sub1\t', ameba_sub1)
    print('sub2\t', ameba_sub2)
    print('mul\t\t', ameba_mul)
    print('div\t\t', ameba_div)

    ameba_3 = OrganicCell(18)
    order_18_5 = ameba_3.make_order(5)
    print(f'\norder_18_5\n{order_18_5}')
