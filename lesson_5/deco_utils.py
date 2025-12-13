from log.server_log_config import server_log
from log.client_log_config import client_log
from datetime import datetime


def func_srv_logging(func):
    date_time_srv = datetime.now()
    server_log.info(f'{date_time_srv} Функция {func.__name__} вызвана из функции main')
    return func


def func_cli_logging(func):
    date_time_cli = datetime.now()
    client_log.info(f'{date_time_cli} Функция {func.__name__} вызвана из функции main')
    return func






date_time = datetime.now()
print(date_time)