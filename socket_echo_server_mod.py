#socket_echo_server_mod.py

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

#create a TCP/IP socket
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
        
        #get dude definition from client
        d1_bytes = connection.recv(5)
        print('Received serialized dude: ', d1_bytes)
        d1 = dude(d1_bytes)
        print('Deserialized dude, c: {}, x: {}, y: {}'.format(d1.c, d1.x, d1.y))

        #send back initial dude status
        connection.sendall(d1.serialize())

        #wait to receive command (one byte (w, s, a, d))
        buffer_size = 1
        cmd_bytes = connection.recv(buffer_size)
        while cmd_bytes:
            #modify dude
            cmd = str(cmd_bytes, 'utf-8')
            if cmd == 'w':
                print(d1.y)
                d1.y = d1.y - 1
            elif cmd == 's':
                d1.y = d1.y + 1
            elif cmd == 'a':
                d1.x = d1.x - 1
            elif cmd == 'd':
                d1.x = d1.x + 1

            #serialize dudes and send to client
            connection.sendall(d1.serialize())

            #wait to receive command
            cmd_bytes = connection.recv(buffer_size)

        print('Session from {} ended.'.format(client_address))

    finally:
        #clean up the connection
        connection.close()
