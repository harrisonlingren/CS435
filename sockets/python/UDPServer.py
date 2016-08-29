#!/usr/bin/env python
import socket
import sys

def main(argv):
    port = argv[0]

    #create an INET, DATAGRAM socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', port))
    print('Listening for messages')

    while 1:
        message, clientAddress = s.recvfrom(2048)
	response = message.upper()
	s.sendto(response, clientAddress)

if __name__ == "__main__":
    # pass arguments if any exist, otherwise send some defaults (not complete)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main( [12000] )

