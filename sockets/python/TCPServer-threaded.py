#!/usr/bin/env python
import socket
import sys
import thread

def clientThread(conn, addr):
    message = conn.recv(1024)
    print("Received %s from %s" % (message.rstrip(), str(addr[0]))) 
    response = message.upper()
    conn.send(response)
    conn.close()
    

def main(argv):
    port = argv[0]

    #create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # now bind our server to its port and start listening
    s.bind(('', port))
    s.listen(5)
    print('Listening for messages...')

    while 1:
        conn, addr = s.accept()
        # start new thread takes 1st argument as a function name to be run,
        # second is the tuple of arguments to the function.
        thread.start_new_thread(clientThread, (conn, addr))

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

