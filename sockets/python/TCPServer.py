#!/usr/bin/env python
import socket
import sys

def main(argv):
    port = argv[0]

    #create an INET, STREAMing socket
    s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
    # now bind the server to the port
    s.bind(('', port))
    s.listen(1)
    print('Listening for messages')
    while 1:
        conn, addr = s.accept()
	message = conn.recv(1024)
	response = message.upper()
	conn.send(response)
	conn.close()

    # signal our intent to close the socket and then close it
    # the shutdown step is _essentially_ optional
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == "__main__":
    # pass arguments if any exist, otherwise send some defaults (not complete)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main( [12000] )

