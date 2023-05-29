"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
try:
    src = ["attribute", "класс", "функция", "type"]
    for word in src:
        print(bytes(word, encoding="ascii"))
except UnicodeEncodeError:
    print("Неверная кодировка!")