#!/usr/bin/python3

import socket

#socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 378

#bindign host and port to socket
serversocket.bind((host, port))

#TCP Listener
serversocket.listen(4)

while True:
    #start of connection
    clientsocket, address = serversocket.accept()

    print("received connection from " + str(address))

#message sent after succesful connection
    message = "Hi ! Thanks for connecting to the server" + "\n"
    clientsocket.send(message)

    clientsocket.close()

