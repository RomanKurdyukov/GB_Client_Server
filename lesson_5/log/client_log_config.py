from logging.handlers import TimedRotatingFileHandler
import logging
import sys

client_log = logging.getLogger('client_logger')
client_log.setLevel(logging.INFO)

client_file_handler = TimedRotatingFileHandler('log/logs/client.log', when='MIDNIGHT', interval=1)
client_file_handler.suffix = "%d-%m-%Y"
server_file_format = logging.Formatter('%(asctime)s %(levelname)-10s %(module)3s: %(message)s')
client_file_handler.setFormatter(server_file_format)
client_file_handler.setLevel(logging.INFO)

client_stream_handler = logging.StreamHandler(sys.stderr)
stream_format = logging.Formatter('%(levelname)-10s %(filename)s %(asctime)s %(message)s')
client_stream_handler.setFormatter(stream_format)
client_stream_handler.setLevel(logging.DEBUG)

client_log.addHandler(client_file_handler)
client_log.addHandler(client_stream_handler)
