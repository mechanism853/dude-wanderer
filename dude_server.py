#!/usr/bin/python3

import socket
import sys
from dude import dude

def print_usage():
    print("Usage: /dude_server.py [PORT]")

def main(argv):
    
    PORT = 10000
    
    #check for command line inputs
    if len(argv) == 2 :
        try:
            PORT = int(argv[1])
        except ValueError:
            print_usage()
            sys.exit(2)
    elif len(argv) > 2:
        print_usage()
        sys.exit(2)
        
    #create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #bind socket to port
    #TODO: Make the port to bind to setable by command line argument
    server_address = ('localhost', PORT)
    print('Starting up server on {} on {}'.format(*server_address))
    #TODO: Verify bind success
    sock.bind(server_address)

    #set to listen for 1 incoming connection at a time
    sock.listen(1)
    
    while True:
        #actually wait for connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
    
            #get dude definition from client
            d1_bytes = connection.recv(5)
            print('Received serialized dude: ', d1_bytes)
            #TODO: validate user data
            d1 = dude.deserialize(d1_bytes)
            print('Deserialized dude, c: {}, x: {}, y: {}'.format(d1.c, d1.x, d1.y))
    
            #send back initial dude status
            connection.sendall(dude.serialize(d1))

            #wait to receive command (one byte (w, s, a, d))
            buffer_size = 1
            cmd_bytes = connection.recv(buffer_size)
            while cmd_bytes:
                #modify dude
                #TODO: Set limits to not allow dude to wander off the grid
                #TODO: Have a default/command not recognized option, separate from an exit commandi
                cmd = str(cmd_bytes, 'utf-8')
                if cmd == 'w':
                    d1.move_north()
                elif cmd == 's':
                    d1.move_south()
                elif cmd == 'a':
                    d1.move_west()
                elif cmd == 'd':
                    d1.move_east()
                elif cmd == 'x':
                    connection.close()

                #serialize dudes and send to client
                connection.sendall(dude.serialize(d1))

                #wait to receive command
                cmd_bytes = connection.recv(buffer_size)

            print('Session from {} ended.'.format(client_address))
        #TODO: Handle ctrl-c (^C) and exit cleanly
        finally:
            #clean up the connection
            connection.close()

main(sys.argv)

