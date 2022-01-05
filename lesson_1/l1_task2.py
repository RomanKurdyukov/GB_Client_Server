"""
Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

word_list = ['class', 'function', 'method']
for word in word_list:

    # не использовал b' т.к. работал с переменной из списка,
    # но по сути bytes это ведь тоже самое

    bytes_word = bytes(word, encoding="ascii")
    print(f'После кодирования:\n'
          f'1) тип - {type(bytes_word)}\n'
          f'2) содержание - {bytes_word}\n'
          f'3) длина - {len(bytes_word)}\n'
          f'-----------------------------')
