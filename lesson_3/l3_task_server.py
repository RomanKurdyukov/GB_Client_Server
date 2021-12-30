from socket import socket, AF_INET, SOCK_STREAM
import base64
from time import time

host = ''
port = 60000
max_connections = 5

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))
s.listen(max_connections)

clients = {}


def clients_probation(clt):
    probation = {
        "action": "probe",
        "time": str(time())
    }
    encoded_probation = str(probation).encode('utf-8')
    base64_probation = base64.b64encode(encoded_probation)
    clt.send(base64_probation)
    client_answer = client.recv(10000000)
    base64_presence = eval(base64.b64decode(client_answer))
    print(f'Presence answer from client was received {base64_presence}')
    client.close()
    client_action = base64_presence.get('action')
    if client_action == 'presence':
        return True


try:
    while True:
        client, addr = s.accept()
        print(f'Connection request from {addr} accepted...')
        if clients_probation(client):
            clients[addr] = client
except KeyboardInterrupt:
    print('\nServer was shut down manually!')
