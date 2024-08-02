#!/usr/bin/python3

import socket

clientsocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname('localhost')
host = '10.211.55.5'

port = 2002

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
