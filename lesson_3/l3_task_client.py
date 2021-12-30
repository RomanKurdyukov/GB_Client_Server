from socket import socket, AF_INET, SOCK_STREAM
from time import time
import base64

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 60000))

presence_data = {
    "action": "presence",
    "time": str(time()),
    "type": "status",
    "user": {
        "account_name": "C0deMaver1ck",
        "status": "Yep, I am here!"
    }
}


def send_presence():
    encoded_presence = str(presence_data).encode('utf-8')
    base64_presence = base64.b64encode(encoded_presence)
    s.send(base64_presence)


server_request = s.recv(10000000)
decoded_request = eval(base64.b64decode(server_request))
print(f'Request from the server was received {decoded_request}')
requested_action = decoded_request.get('action')

if requested_action == 'probe':
    send_presence()

s.close()
