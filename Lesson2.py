"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не
запрашивать у пользователя, а указать явно, в программе.
"""
list_ = [1, "letter", 2.6, [1, 5]]
num = int(input("Введите номер элемента списка:"))
print(type(list_[num]))
print(type(list_[1]))
print(type(list_[3]))
"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
items = list(input('Введите элементы списка:'))
len_ = len(items)
i = 0
items_new = []
while i < len_:
    pair_el = items[(0 + i):(2 + i)]
    pair_el.reverse()
    items_new = items_new + pair_el
    i += 2
print(list(items_new))
"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
digit = int(input('Введите номер месяца:'))
list_month = ['Зима', 'Весна', 'Лето', 'Осень']
dict_ = {list_month[0]: [1, 2, 12], list_month[1]: [3, 4, 5],
         list_month[2]: [6, 7, 8]}
if digit in dict_.get(list_month[0]):
    print(list_month[0])
elif digit in dict_.get(list_month[1]):
    print(list_month[1])
elif digit in dict_.get(list_month[2]):
    print(list_month[2])
else:
    print(list_month[3])
"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. Если в слово длинное, выводить только
первые 10 букв в слове.
"""
letter = str(input('Введите предложение:'))
list_let = letter.split(' ')
length = len(list_let)
i = 0
while i < length:
    print(f'строка №{i + 1}: {list_let[i]:.10}')
    i += 1
"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор 
натуральных чисел. У пользователя необходимо запрашивать новый элемент 
рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
"""
num = [2, 7, 5, 4, 3, 8, 7, 4, 5]
print(type(num))
list_ = list(set(num))
print(list_)
print(type(list_[1]))
el = int(input('Введите число(прерывание опреации 999):'))
while el != 999:
    if el not in list_:
        num.append(el)
        print(num)
    else:
        print('Структура рейтинга без изменений!')
    el = int(input('Введите число(прерывание опреации 999):'))
print(f'последнии данные: {num}')

"""
1* Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно
быть два элемента — номер товара и словарь с параметрами (характеристиками
товара: название, цена, количество, единица измерения). Структуру нужно
сформировать программно, т.е. запрашивать все данные у пользователя.
"""
exit_ = str()
string_a = []
string_b = []
string_c = []
string_d = []
my_tupl = ''
table_ = ('Название', 'Цена', 'Кол-во', 'ед.изм')
i = 0
while True:
    # a = 0
    if not (exit_ == 'stop' or exit_ == 'info'):
        key1 = input('Введите название товара:')
        key2 = float(input('Введите цена товара:'))
        key3 = int(input('Введите количество товара:'))
        key4 = input('Введите единицу измерения количества:')
        exit_ = str(input('Если желаете прекратить ввод и отобразить аналитику '
                          'данных введите слово'
                          ' "stop", если нужна информация о товарах введите'
                          ' "info" '))
        string_a.insert(i, key1)
        string_b.insert(i, key2)
        string_c.insert(i, key3)
        string_d.insert(i, key4)
        my_dir = {table_[0]: string_a, table_[1]: string_b, table_[2]: string_c,
                  table_[3]: string_d}
        i += 1
        my_tupl = (f' {my_tupl} \n {i} {table_[0]}: {key1},'
                        f' {table_[1]}: {key2}, {table_[2]}: {key3},'
                        f'{table_[3]}: {key4}')
    elif exit_ == 'info':
        print(my_tupl)
        break
    elif exit_ == 'stop':
        print('Аналитика:')
        for key, value in my_dir.items():
            print(f' {key}: {value}')
        break