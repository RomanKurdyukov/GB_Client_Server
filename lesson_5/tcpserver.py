from time import sleep
from serv_service_layer import *
from log.server_log_config import server_log

server_socket.bind((server_config.get('HOST'), server_config.get('PORT')))
server_socket.listen(server_config.get('MAX_CONNECTIONS'))

clients = {}

try:
    while True:
        client, addr = server_socket.accept()
        server_log.info(f'Connection request from IP {addr[0]} PORT {addr[1]} accepted...')
        client.send(response_ok_msg())
        server_log.info(f'Connection ACK was sent...')
        sleep(1)
        client.send(clients_probation())
        server_log.info(f'Probe action was sent...')
        client_data = decode_data(client.recv(server_config['BUFFER_SIZE']))
        if check_probation_data(client_data):
            server_log.info(f'Answer received:\n{client_data}')
            client.send(response_ok_msg())
            server_log.info(f'Probation passed, ACK was sent...')
        else:
            server_log.warning(f'Client probation data does not meet the requirements...')
            client.send(response_bad_request())
except KeyboardInterrupt:
    server_log.critical('Server was shut down manually!')
