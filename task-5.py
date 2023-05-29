"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def ping_url(url):
    res = subprocess.Popen(['ping', url], stdout=subprocess.PIPE)
    for line in res.stdout:
        print(line.decode(chardet.detect(line)['encoding'])
              .encode('utf-8')
              .decode('utf-8'), end="")


ping_url('ya.ru')
ping_url('youtube.com')