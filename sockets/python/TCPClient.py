#!/usr/bin/env python
import socket
import sys

def main(argv):
    server = argv[0]
    port = argv[1]

    #create an INET, STREAMing socket
    s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
    # now connect server on the specified port
    s.connect((server, port))

    message = raw_input('Input a message to send:')
    s.send(message)

    # receive and print 1024 B of response
    response = s.recv(1024)
    print("Received: %s" % (str(response)))

    # signal our intent to close the socket and then close it
    # the shutdown step is _essentially_ optional
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == "__main__":
    # pass arguments if any exist, otherwise send some defaults (not complete)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main( ['localhost', 12000] )

