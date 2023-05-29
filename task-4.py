"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def encodedecode(words):
    for i in range(len(words)):
        if isinstance(words[i], bytes):
            words[i] = words[i].decode()
        else:
            words[i] = str.encode(words[i])
    return words


words = ["разработка", "администрирование", "protocol", "standard"]

print(encodedecode(words))
print(encodedecode(words))
