"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess

args = ['ping', 'yandex.ru']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

# у меня ubuntu ничего не изменилось, пингуется всегда в латиннице,
# Вы на уроке предупреждали, что это работает только на win

for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

