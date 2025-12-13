from cli_service_layer import *
from log.client_log_config import client_log
from deco_utils import func_cli_logging

client_socket.connect((client_config.get('SERVER'), client_config.get('PORT')))

try:
    @func_cli_logging
    def check_response(response):
        if response.get('action') is None:
            client_log.info(f'Response received...')
            for value in response.values():
                client_log.info(value)
        else:
            if response.get('action') == 'probe':
                client_log.info(f'Probation request was received...\n{response}')
                username = input('Enter desired username:')
                client_socket.send(encode_data(presence_msg_create(username)))
                client_log.info(f'Probation answer was sent...')


    while True:
        data_from_server = decode_data(client_socket.recv(client_config['BUFFER_SIZE']))
        if len(data_from_server) == 0:
            break
        else:
            check_response(data_from_server)

except KeyboardInterrupt:
    client_log.warning('Connection to the server was closed manually!')

