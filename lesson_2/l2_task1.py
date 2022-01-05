"""
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений
извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных
отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в
файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import re
import csv


def get_data():
    i = 1
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []
    patterns = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
    while i:
        try:
            with open('info_' + str(i) + '.txt', 'r', encoding='cp1251') as info_file:
                for row in info_file:
                    for pattern in patterns:
                        if re.match(pattern, row):
                            new_row = re.sub('\s{2,30}|\n', '', row)
                            main_data_part, separator, os_data_part = new_row.partition(':')
                            if main_data_part not in main_data:
                                main_data.append(main_data_part)
                            if main_data_part == patterns[0]:
                                os_prod_list.append(os_data_part)
                            elif main_data_part == patterns[1]:
                                os_name_list.append(os_data_part)
                            elif main_data_part == patterns[2]:
                                os_code_list.append(os_data_part)
                            elif main_data_part == patterns[3]:
                                os_type_list.append(os_data_part)
                i += 1
        except FileNotFoundError:
            print('Выборка завершена!')
            return main_data, os_name_list, os_code_list, os_prod_list, os_type_list


def write_to_csv():
    incoming_data = get_data()
    rows = zip(incoming_data[1], incoming_data[2], incoming_data[3], incoming_data[4])

    with open('workstations_data.csv', 'w') as stations_file:
        csv_writer = csv.DictWriter(stations_file, fieldnames=incoming_data[0])
        csv_writer.writeheader()
        writer = csv.writer(stations_file)
        for row in rows:
            writer.writerow(row)


if __name__ == '__main__':

    write_to_csv()

    with open('workstations_data.csv', 'r') as result:
        csv_reader = csv.DictReader(result)
        for row in csv_reader:
            print(row)



# что-то мне кажется я перемудрил =), но всё работает