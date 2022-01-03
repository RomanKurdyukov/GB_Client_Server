from socket import socket, AF_INET, SOCK_STREAM
import yaml
import os
from time import time
import base64


server_socket = socket(AF_INET, SOCK_STREAM)

with open('app_config.yaml', 'r') as config:
    server_config = yaml.load(config, Loader=yaml.Loader)


def encode_data(data):
    encoded_answer = str(data).encode(server_config['ENCODING'])
    encoded_base64_data = base64.b64encode(encoded_answer)
    return encoded_base64_data


def decode_data(data):
    decoded_data = eval(base64.b64decode(data))
    return decoded_data


def response_ok_msg():
    response_set = {
        'response': server_config['RESPONSE']['OK'],
        'alert': 'OK'
    }
    return response_set


def clients_probation():
    probation_set = {
        'action': server_config['ACTION'][0],
        'time': time()
    }
    return probation_set


def check_probation_data(data):
    if len(data) <= server_config['MAX_MESSAGE_LENGHT'] \
            and data.get('action') == server_config['ACTION'][3]:
        return True



