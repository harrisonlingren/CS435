#!/usr/bin/env python
import socket
import sys

def main(argv):
    server = argv[0]
    port = argv[1]

    #create an INET, DATAGRAM socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = raw_input('Input a message to send:')
    s.sendto(message,(server, port))

    # receive and print 2048 B of response
    response, serverAddress = s.recvfrom(2048)
    print("Received from %s: %s" % (str(serverAddress), str(response)))

    # close the socket
    s.close()

if __name__ == "__main__":
    # pass arguments if any exist, otherwise send some defaults (not complete)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main( ['localhost', 12000] )

