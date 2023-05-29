"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

src = ["class", "function", "method", "программа", 42]

for word in src:
    if isinstance(word, str):
        print(f"{type(word)}: {bytes(word, encoding='utf-8')}({len(word)})")
    else:
        print(word)