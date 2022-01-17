from logging.handlers import TimedRotatingFileHandler
import logging
import sys

server_log = logging.getLogger('server_logger')
server_log.setLevel(logging.INFO)

server_file_handler = TimedRotatingFileHandler('log/logs/server.log', when='MIDNIGHT', interval=1)
server_file_handler.suffix = "%d-%m-%Y"
server_file_format = logging.Formatter('%(asctime)s %(levelname)-10s %(module)3s: %(message)s')
server_file_handler.setFormatter(server_file_format)
server_file_handler.setLevel(logging.INFO)

server_stream_handler = logging.StreamHandler(sys.stderr)
stream_format = logging.Formatter('%(levelname)-10s %(filename)s %(asctime)s %(message)s')
server_stream_handler.setFormatter(stream_format)
server_stream_handler.setLevel(logging.DEBUG)

server_log.addHandler(server_file_handler)
server_log.addHandler(server_stream_handler)
