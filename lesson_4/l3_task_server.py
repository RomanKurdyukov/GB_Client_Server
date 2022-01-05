from socket import socket, AF_INET, SOCK_STREAM
import base64
from time import time, sleep
from serv_service_layer import *
import sys

server_socket.bind((server_config.get('HOST'), server_config.get('PORT')))
server_socket.listen(server_config.get('MAX_CONNECTIONS'))

clients = {}

try:
    while True:
        client, addr = server_socket.accept()
        print(f'Connection request from IP {addr[0]} PORT {addr[1]} accepted...')
        client.send(response_ok_msg())
        print(f'Connection ACK was sent...')
        sleep(1)
        client.send(clients_probation())
        print(f'Probe action was sent...')
        client_data = decode_data(client.recv(server_config['BUFFER_SIZE']))
        if check_probation_data(client_data):
            print(client_data)
            client.send(encode_data(response_ok_msg()))
            print(f'Probation passed, ACK was sent...')
except KeyboardInterrupt:
    print('\nServer was shut down manually!')
