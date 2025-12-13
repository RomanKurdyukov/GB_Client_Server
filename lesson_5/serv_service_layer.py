from socket import socket, AF_INET, SOCK_STREAM
import yaml
from time import time
import base64
from deco_utils import func_srv_logging


server_socket = socket(AF_INET, SOCK_STREAM)

with open('app_config.yaml', 'r') as config:
    server_config = yaml.load(config, Loader=yaml.Loader)


@func_srv_logging
def encode_data(data):
    encoded_answer = str(data).encode(server_config['ENCODING'])
    encoded_data = base64.b64encode(encoded_answer)
    return encoded_data


@func_srv_logging
def decode_data(data):
    decoded_data = eval(base64.b64decode(data))
    return decoded_data


@func_srv_logging
def response_ok_msg():
    response_set = {
        'response': server_config['RESPONSE']['OK'],
        'time': time(),
        'alert': 'OK'
    }
    return encode_data(response_set)


@func_srv_logging
def response_bad_request():
    response_set = {
        'response': server_config['RESPONSE']['BAD_REQUEST'],
        'time': time(),
        'alert': 'BAD_REQUEST'
    }
    return encode_data(response_set)


@func_srv_logging
def clients_probation():
    probation_set = {
        'action': server_config['ACTION'][0],
        'time': time()
    }
    return encode_data(probation_set)


@func_srv_logging
def check_probation_data(data):
    if len(data) <= server_config['MAX_MESSAGE_LENGTH'] \
            and data.get('action') == server_config['ACTION'][3]:
        return True




