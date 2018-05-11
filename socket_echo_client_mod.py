#socket_echo_client_mod.py

import socket
import sys

#dude class definition
#TODO: Define dude in seperate file and import in both server and client. This helps keep any changes in sync if nothing else.
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
            #TODO: Fix these args[#]
            self.x = x_pos
            self.y = y_pos
            self.c = c_type
        else:
            #TODO: THROW TANTRUM
            #TODO: Actually add something here so it works ;)

    def serialize(self):
        return self.x.to_bytes(2, 'big') + self.y.to_bytes(2, 'big') + bytearray(self.c, 'utf-8')
#TODO: Create a main function and encapsulate all of this into it. Call main at the end of this file.
#create a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port where the server is listening
#TODO: Make the server and port setable by command line arguments.
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
#TODO: Verify your socket connection is valid before using it.
sock.connect(server_address)

try:
    #get your dude
    #TODO: Validate user input
    c_input = input('What does your dude look like? (one ascii character): ')
    print('Where does your dude start?')
    #TODO: Validate user input
    x_input = input('   x coord [1, 16]: ')
    #TODO: Validate user input
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
        #TODO: Validate dude return value - since there's an else that throws up
        d = dude(dude_bytes)
        #print response to terminal
        print('Your dude ({}) is now at\n   x: {}\n   y: {}'.format(d.c, d.x, d.y))
        #get directional input
        #TODO: Validate user input
        #TODO: Add exit letter? q? (ahh, i see you exit with x, nice)
        direction = input('Wander your dude. (w, a, s, d):')
        #serialize directional input
        direction_bytes = bytearray(direction, 'utf-8')
        #transmit directional input
        sock.sendall(direction_bytes)

#TODO: Add signal handler to exit cleanly on ctrl-c (^C)
finally:
    print('closing socket')
    sock.sendall(bytearray('x', 'utf-8'))
    sock.close()

