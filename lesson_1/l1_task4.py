"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode).
"""

word_list = ['разработка', 'администрирование', 'protocol', 'standard']

for word in word_list:
    str_to_bytes_word = word.encode('utf-8')
    print(f'Слово "{word}" преобразованное в байтовую строку:\n{str_to_bytes_word}')
    print(f'Обратное преобразование:\n{str_to_bytes_word.decode()}\n'
          f'--------------------------------')
