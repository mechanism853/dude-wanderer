#!/usr/bin/python3

import socket
import sys
from shared.dude import dude

##
#
##
def dude_builder_prompts():
    c_input = 'X'
    x_input = 0
    y_input = 0

    print("\033[H\033[J")
    while True:
        c_input = input('\033[H\033[JWhat does your dude look like? (one ascii character): ')
        if len(c_input) == 1:
            break

    print("\033[H\033[J")
    while True:
        print("Dude: " + c_input)
        print('What\'s your dude\'s starting location?')
        try:
            x_input = int(input('   x coord [1, 16]: '))
            y_input = int(input('   y coord [1, 10]: '))
        except ValueError:
            print("\033[H\033[J !!!Please, integers only!!!")
        else:
            break

    return dude(x_input, y_input, c_input)

##
# Get directional input
##
def prompt_and_send_commands(sock):
    print("Wander your dude!")
    print("w, a, s, and d for direction")
    #Validate user input
    while True:
        #TODO: Add exit letter? q? (ahh, i see you exit with x, nice)
        cmd = input('> ').lower()
        if (cmd == 'w') or (cmd == 'a') or (cmd == 's') or (cmd == 'd'):
            #serialize directional input
            cmd_bytes = bytearray(cmd, 'utf-8')
            #transmit directional input
            sock.sendall(cmd_bytes)
            break
        elif (cmd == 'help') or (cmd == 'h'):
            print("\th (or help): display this dialog")
            print("\tw: move your dude north (upward on the screen)")
            print("\ta: move your dude west (leftward on the screen)")
            print("\ts: move your dude south (downward on the screen)")
            print("\td: move your dude east (you get the idea)")
            print("\tx: exit dude walker (not yet implemented!!! ;D )")
        else:
            print("Invalid. See h or help for command list.")

##
#
##
def receive_and_display_status(sock):
    #wait for response
    buffer_size = 11
    dude_bytes = sock.recv(buffer_size)
    #deserialize response
    #TODO: Validate dude return value - since there's an else that throws up
    d = dude.deserialize(dude_bytes)
    #print response to terminal
    print("\033[H\033[J Dude Status: " + d.as_string())

##
#
##
def setup_socket(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect the socket to the port where the server is listening
        server_address = (host, port)
        print('Connecting to server at {}, {}'.format(*server_address))
        #TODO: Verify your socket connection is valid before using it.
        sock.connect(server_address)
        return sock
    except Exception:
        print("Error! Could not connect to server at {}, {}".format(host, port))

##
#
##
def print_usage():
    print("Usage: ./dude_client.py [HOST] [PRINT]")

##
#
##
def parse_args(argv):
    try:
        host = socket.inet_aton(argv[1])
        port = int(argv[2])
        return (host, port)
    except Exception:
        print_usage()
        sys.exit(2)

##
# main
##
def main(argv):
    #parse cmd line
    (host, port) = parse_args(argv)

    #create a tcp/ip socket
    sock = setup_socket(host, port)

    try:
        #get your dude
        d = dude_builder_prompts()
        #send dude to server
        print('Sending your dude to the dude-wanderer server')
        sock.sendall(dude.serialize(d))

        while True:
            receive_and_display_status(sock)
            prompt_and_send_commands(sock)

    #TODO: Add signal handler to exit cleanly on ctrl-c (^C)
    finally:
        print('closing socket')
        sock.sendall(bytearray('x', 'utf-8'))
        sock.close()

main(sys.argv)
