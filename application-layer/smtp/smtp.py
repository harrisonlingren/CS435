#!/usr/bin/env python
import socket
import sys

def main(argv):
    #create an INET, STREAMing socket
    s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the mail server on port 25
    s.connect(('bumail.butler.edu', 25))

    # send our message
    s.send('HELO thomas.butler.edu')

    # receive and print 1024 B of response
    r = s.recv(1024)
    print("Received: %s" % (str(r)))

    # signal our intent to close the socket and then close it
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == "__main__":
    # pass arguments if any exist, otherwise send some defaults (not complete)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main( ['bumail.butler.edu', 25] )

