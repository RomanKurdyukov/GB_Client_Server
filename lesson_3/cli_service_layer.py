from socket import socket, AF_INET, SOCK_STREAM
import yaml
import os
from time import time
import base64


client_socket = socket(AF_INET, SOCK_STREAM)

with open('app_config.yaml', 'r') as config:
    client_config = yaml.load(config, Loader=yaml.Loader)


def encode_data(data):
    encoded_answer = str(data).encode(client_config['ENCODING'])
    encoded_data = base64.b64encode(encoded_answer)
    return encoded_data


def decode_data(data):
    decoded_data = eval(base64.b64decode(data))
    return decoded_data


def presence_msg_create(username):
    presence_data = {
        "action": "presence",
        "time": time(),
        "type": "status",
        "user": {
            "account_name": username,
            "status": "Yep, I am here!"
        }
    }
    return encode_data(presence_data)

