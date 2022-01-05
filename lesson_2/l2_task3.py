"""
Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

yaml_data = {
    "first_key": [969, 'somesetting', None, 'message_key_1'],
    "second_key": 10000,
    "third_key": {
        'Eur': [100, '€'],
        'Gbp': [200, '£'],
        'Usd': [300, '$']
    }
}

with open('task_3.yaml', 'w') as yaml_file:
    yaml.dump(yaml_data, yaml_file, allow_unicode=True, default_flow_style=False)

with open('task_3.yaml', 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file, Loader=yaml.Loader)
    print(yaml_data)
