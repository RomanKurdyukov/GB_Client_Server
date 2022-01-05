import sys
from socket import socket, AF_INET, SOCK_STREAM
from time import time
from cli_service_layer import *

client_socket.connect((client_config.get('SERVER'), client_config.get('PORT')))


def check_response(response):
    if response.get('action') is None:
        print(f'Response received...')
        for value in response.values():
            print(value)
    else:
        if response.get('action') == 'probe':
            print(f'Probation request was received...\n {response}')
            username = input('Enter desired username:')
            client_socket.send(presence_msg_create(username))


while True:
    data_from_server = decode_data(client_socket.recv(client_config['BUFFER_SIZE']))
    if len(data_from_server) == 0:
        break
    else:
        check_response(data_from_server)


