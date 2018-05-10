#socket_echo_client_mod.py

import socket
import sys

#dude class definition
class dude:
    def __init__(self, *args):
        if len(args) == 1:
            # case for generating dude from serialized dude
            dude_bytes = args[0]
            self.x = int.from_bytes(dude_bytes[0:2])
            self.y = int.from_bytes(dude_bytes[2:4])
            self.c = str(dude_bytes[4:], 'utf-8')
        elif len(args) == 3:
            # case for generating dude from non-serialized dude parts
            self.x = x_pos
            self.y = y_pos
            self.c = c_type
        else:
            #TODO: THROW TANTRUM

    def serialize(self):
        return self.x.to_bytes(2, 'big') + self.y.to_bytes(2, 'big') + bytearray(self.c, 'utf-8')

#create a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    #get your dude
    c_input = input('What does your dude look like? (one ascii character): ')
    print('Where does your dude start?')
    x_input = input('   x coord [1, 16]: ')
    y_input = input('   y coord [1, 10]: ')
    d = dude(int(x_input), int(y_input), c_input)

    #send dude to server
    print('Sending your dude to the dude-wanderer server')
    sock.sendall(d.serialize())

    buffer_size = 11
    while True:
        #wait for response
        dude_bytes = sock.recv(buffer_size)
        #deserialize response
        d = dude(dude_bytes)
        #print response to terminal
        print('Your dude ({}) is now at\n   x: {}\n   y: {}'.format(d.c, d.x, d.y))
        #get directional input
        direction = input('Wander your dude. (w, a, s, d):')
        #serialize directional input
        direction_bytes = bytearray(direction, 'utf-8')
        #transmit directional input
        sock.sendall(direction_bytes)

finally:
    print('closing socket')
    sock.sendall(bytearray('x', 'utf-8'))
    sock.close()

