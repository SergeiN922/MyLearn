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
    pair_el = items[(0+i):(2+i)]
    pair_el.reverse()
    items_new = items_new + pair_el
    i += 2
print(list(items_new))
"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. Если в слово длинное, выводить только
первые 10 букв в слове.
"""
"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор 
натуральных чисел. У пользователя необходимо запрашивать новый элемент 
рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
"""
