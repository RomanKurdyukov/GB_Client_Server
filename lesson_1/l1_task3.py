"""
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
"""

word_list = ['attribute', 'класс', 'функция', 'type']
for word in word_list:
    try:
        bytes_word = bytes(word, encoding="ascii")
        print(f'Слово "{word}" возможно записать в байтовом типе')
    except UnicodeEncodeError:
        print(f'Слово "{word}" НЕВОЗМОЖНО записать в байтовом типе,\n'
              f'символы вне предела диапазона печати таблицы ASCII')