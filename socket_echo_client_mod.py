#socket_echo_client.py

import socket
import sys

#create a coord class
class dude:
    def __init__(self, xPos, yPos, cType):
        self.x = xPos
        self.y = yPos
        self.c = cType

#create a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    while True:
        #get data from user
        xInput = input('Please enter an x coord (1 <= x <= 16): ')
        yInput = input('Please enter a y coord (1 <= y <= 10): ')
        cInput = input('Please enter a printable character: ')

        #send data
        message = xInput + yInput + cInput
        print('sending ', message)
        messageBytes = bytearray(message, 'utf-8')
        sock.sendall(messageBytes)

        #look for response
        amount_received = 0
        amount_expected = len(messageBytes)

        while amount_received < amount_expected:
            #TODO: Write code
            data = sock.recv(8)
            amount_received += len(data)
            print('received ', str(data, 'utf-8'))

finally:
    print('closing socket')
    sock.close()

