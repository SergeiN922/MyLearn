"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, production_per_hour, rate_per_hour, prize_in_rubles = argv
result = int(production_per_hour) * int(rate_per_hour) + int(prize_in_rubles)

print(f'заработная плата сотрудника составит - {result} руб.')

"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для 
формирования списка использовать генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([numb for el, numb in enumerate(start_list) if el > 0 and start_list[el]
       > start_list[el - 1]])

"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы 
вывести в порядке их следования в исходном списке. Для выполнения задания 
обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [el for el in start_list if start_list.count(el) == 1]

print(new_list)


"""
5. Реализовать формирование списка, используя функцию range() и возможности 
генератора. В список должны войти четные числа от 100 до 1000 (включая 
границы). Необходимо получить результат вычисления произведения всех элементов 
списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)

print(reduce(lambda prev_el, el: prev_el * el, my_list))


"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, 
при котором повторение элементов списка будет прекращено.
"""

# script <a>

from itertools import count

n = int(input('Введите начальное число: '))
for el in count(n):
    if el > 15:
        break
    else:
        print(el)

# script <b>

from itertools import cycle


list_ = [1, 10.7, None, "my_list", True, [1, 3]]

n = 0
for el in cycle(list):
    if n > 15:
        break
    else:
        print(el)
        n += 1

"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим 
очередное значение. При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fact(n). Функция 
отвечает за получение факториала числа, а в цикле необходимо выводить только 
первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, 
факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from itertools import count
from math import factorial


def fact():
    for x in count(1):
        yield factorial(x)


n = 0

for el in fact():
    if n < 10:
        print(el)
        n += 1
    else:
        break
