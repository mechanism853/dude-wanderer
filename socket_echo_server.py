#socket_echo_server.py

import socket
import sys

#create teh TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket to port
server_address = ('localhost', 10000)
print('starting up server on {} on {}'.format(*server_address))
sock.bind(server_address)

#set to listen for incoming connections?
sock.listen(1)

while True:
    #actually wait for connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        
        #receive the data in small chunks and retransmit it
        data = connection.recv(16)
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        #clean up the connection
        print('closing the connection')
        connection.close()
