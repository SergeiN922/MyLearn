"""
1. Создать программный файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных будет
свидетельствовать пустая строка.
"""
with open('text_new.txt', 'a') as file:
    file.write(input('Введите через пробел данные:').replace('', '\n'))
"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, 
выполнить подсчёт строк и слов в каждой строке.
"""
with open('text_new.txt', 'r', encoding='utf-8') as file:
    print(f'Кол-во сторк в файле: {len(file.readlines())}')
    file.seek(0)
    for i, word in enumerate(file.readlines(), 1):
        len_str = len(word.split(" "))
        print(f'кол-во слов в {i} строке: {len_str}')

"""
3. Создать текстовый файл (не программно). Построчно записать фамилии 
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из 
сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open('task3.txt', "r", encoding='UTF-8') as f:
    list_worker = []
    salary = 0
    for i, worker in enumerate(f.readlines()):
        a = worker.split(" ")
        i += 1
        salary += float(a[1])
        if float(a[1]) < 20000:
            list_worker.append(a[0])
    print(f'Сотрудники с доходом менее 20 тыс. : {list_worker}')
    print(f'Cреднея величина дохода сотрудников: {salary / i}')

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
© geekbrains.ru 24
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('Task4.txt', 'r', encoding='UTF-8') as f:
    for i in f.readlines():
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('Task4_new.txt', 'w', encoding='UTF-8') as f2:
    f2.writelines(new_file)

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и 
выводить её на экран.
"""


def summary():
    with open('Task5.txt', 'w+', encoding='UTF-8') as f:
        line = input('Введите цифры через пробел:')
        f.writelines(line)
        my_numb = line.split()
        sum_ = sum(map(int, my_numb))
        f.writelines(f'\nСумма чисел: {sum_}')
        print(f'Сумма чисел: {sum_}')


summary()
"""
6. Сформировать (не программно) текстовый файл. В нём каждая строка должна
описывать учебный предмет и наличие лекционных, практических и лабораторных
занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого 
предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий 
по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re

report = {}
with open('Task6.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    for row in file:
        row_items = row.split(': ')
        hours = re.findall(r"\d+", row_items[1])
        report.update({row_items[0]: sum([int(i) for i in hours])})

print(f"Исходный данные:\n{text}\n")
print(f"Словарь:\n{report}")

"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором 
каждая строка будет содержать данные о фирме: название, форма собственности, 
выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не 
включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить 
её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
               {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста
"""

import json

report = []
with open('Task7.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    profits = {}
    profit_sum = 0
    for row in file:
        items = row.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            profits.update({items[0]: profit})
            profit_sum += profit
    report.append(profits)
    report.append({'average_profit': (profit_sum / len(profits))})

with open('Task7.json', 'w', encoding='UTF-8') as json_file:
    json.dump(report, json_file, ensure_ascii=False)

json_report = json.dumps(report, ensure_ascii=False)

print(f"Исходный данные:\n{text}\n")
print(f"Список:\n{report}\n")
print(f"json-объект:\n{json_report}")