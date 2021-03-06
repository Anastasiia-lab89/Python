# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [25, 'Hello', True, None, 25.4, (1, 2), {1: 2, 2: 3}, [1, 2], {2, 3}]
for i in my_list:
    print(type(i))

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

my_list = (input('Введите данные для списка:')).split()

for i in range(0, (len(my_list) - 1), 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
# Решение через List:
month = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
name = ['Зима', 'Весна', 'Лето', 'Осень']
number = int(input('Введите месяц числом от 1 - 12: '))
for i in range(len(month)):
    if number in month[i]:
        print(f'{number} - й месяц - это {name[i]}')

# Решение через dict:
number = int(input('Введите месяц числом от 1 - 12: '))

month = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for key in month:
    if number in month[key]:
        print(key)

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

my_list = (input('Введите слова через пробел: ')).split()

for i, el in enumerate(my_list, 1):
    print(i, el[:10])

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число: '))
for i in range(len(my_list)):
    if (number - my_list[i]) > 0:
        my_list.insert(i, number)
        break
    elif (number - my_list[-1]) <= 0:
        my_list.append(number)
        break
print(my_list)

# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара

my_list = []

while True:
    my_list.append({'название': input('Введите название товара: '),
                    'цена': int(input('Введите цену товара: ')),
                    'количество': int(input('Введите количество товара: ')),
                    'ед': input('Введите еденицу измерения товара: ')})
    goods = input('Добавить товар? да/нет ')
    if goods == 'да':
        continue
    else:
        break

for i in enumerate(my_list, 1):
    print(i)


# ------------------------------Вариант 2:----------------------------
my_list = []
name_list = []
price_list = []
q_list = []
unit_list = []
m = []
while True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите еденицу измерения товара: ')
    my_list.append({'название': name, 'цена': price, 'количество': quantity, 'ед': unit})
    name_list.append(name)
    price_list.append(price)
    q_list.append(quantity)
    unit_list.append(unit)
    goods = input('Добавить товар? да/нет ')
    if goods == 'да':
        continue
    else:
        break
for i in enumerate(my_list, 1):
    print(i)
m.append(name_list)
m.append(price_list)
m.append(q_list)
m.append(unit_list)
n = my_list[0].keys()
print(dict(zip(n, m)))
