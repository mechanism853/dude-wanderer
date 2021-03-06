#socket_echo_client_mod.py

import socket
import sys
from dude import dude

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

