#socket_echo_server.py

import socket
import sys

#create a coord class
class dude:
    def __init__(self, xPos, yPos, cType):
        self.x = xPos
        self.y = yPos
        self.c = cType
    
    def location():
        return self.x + self.y + self.c

#get data from user
print('Let\'s instantiate a dude on the server:')
xInput = input('Please enter an x coord (1 <= x <= 16): ')
yInput = input('Please enter a y coord (1 <= y <= 10): ')
cInput = input('Please enter a printable character: ')
d1 = dude(xInput, yInput, cInput)

#create teh TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket to port
server_address = ('localhost', 10000)
print('starting up server on {} on {}'.format(*server_address))
sock.bind(server_address)

#set to listen for 1 incoming connection at a time
sock.listen(1)

while True:
    #actually wait for connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        
        #receive the command, modify the dude, and transmit a copy of the dude
        buffer_size = 3
        cmd_bytes = connection.recv(buffer_size)
        while data:
            cmd = str(data, 'utf-8')
            if cmd == 'w':
                d1.y = d1.y - 1
            elif cmd == 's':
                d1.y = d1.y + 1
            elif cmd == 'a':
                d1.x = d1.x - 1
            elif cmd == 'd':
                d1.x = d1.x + 1
            #serialize dude and send to client
            print(d1.location())
            connection.sendall(bytearray(d1.location(), 'utf-8'))
            data = connection.recv(buffer_size)
        print('no data from', client_address)

    finally:
        #clean up the connection
        connection.close()
