# tcp-client-and-server

This project demonstrates a basic implementation of a TCP client and server using Python's `socket` library. The server listens for incoming connections and responds with a welcome message. The client connects to the server and receives the message.

## Program in Action
### Client/ Mac OS
([Mac OS Client with Displayed message which shows successful connection](https://github.com/myhavok/tcp-client-and-server/blob/main/images/Screenshot%202024-08-01%20at%2011.30.01%E2%80%AFPM.png)

### Server Kali Linux VM
[Kali Linux Server which confirms received connections IP address and port number](https://github.com/myhavok/tcp-client-and-server/blob/main/images/Screenshot%202024-08-01%20at%2011.29.13%E2%80%AFPM.png)

## Features
- TCP Server that listens for incoming connections.
- TCP Client that connects to the server and receives a message.

## Prerequisites

- Python installed on your system.
- Basic understanding of TCP/IP and socket programming.

## Setup

### Server

1. Open a terminal on your server machine.
2. Navigate to the directory containing `TCPserver.py`.
3. Run the server script:
   
### Client
1. Open a terminal on your client machine.
2. Navigate to the directory containing TCPClient.py.
3. Edit TCPClient.py to set the correct host and port to match the server's IP address and port.
4. Run the client script:

### Acknowledgements
Python socket documentation: https://docs.python.org/3/library/socket.html
