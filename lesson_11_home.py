import re

# print("Урок одинадцатый, домашнее задание №1")
# """В примере найти и вывести трехзначные числа с помощью регулярных выражений."""
#
# sample = 'Exercises number 1, 12, 13, and 345 are important 456'
# print(re.findall(r' \d{3}', sample))


# print("Урок одинадцатый, домашнее задание №2")
# """Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов."""
#
# collors = ['#ABCDEF', '#54#', '#F08080', '#FA8072', 'fghw3d', '#8B0000']
# print(re.findall(r'\#[A-F0-9]{6}', str(collors)))


# print("Урок одинадцатый, домашнее задание №3")
# """Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00.
# Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время."""
#
# text = ['Завтрак в 09:00', 'Завтрак в 90:00', 'Обед  в 13:00', 'Обед в 13:61', 'Ужин в 19:05', 'Ужин в 37:98', 'Ужин в 24:01']
# b = (re.findall(r'Завтрак в [0,1][1-9]:[0-9]{2}', str(text)))
# print(b)


# print("Урок одинадцатый, домашнее задание №4")
# """Создать запрос для выбора из текста дробных чисел с разделителем дробной
# части в виде точки. Разряды целой части могут не выделяться или отделяться пробелом или запятой. 1231.12313"""
# numbers = [1231.12313, 2121.121, 3.14, 6598, 9898787, 999.99, '098 90', '123,123']
# b = (re.findall(r'\d{4}\.\d+', str(numbers)))
# print(b)

print("Урок одинадцатый, домашнее задание №4/1")
""" ** Добавить регулярное выражения для поиска и вывода MAC адресов в скрипте который работал с конфигурациями маршрутизатора (можно переделать весь скрипт для работы с регуляркой)"""
mac = 'aa:bb:cc:11:22:33,aa12:cc11:c23f,ff1a.cc11.c23f,bb15-aa56-d43a,bb-15-aa-56-d4-3a, 99234239, wefwefw, 1df23fs, 33ff.ghj8'
b = (re.findall(r'\w+-?:?\w+[:.-]\w+[:.-]\w+-?:?\w+-?:?\w+', mac))
print(b)
