#!/usr/bin/env python
import socket
import sys

def main(argv):
    # port and host
    if sys.argv == 1:
        host = input("Hostname to connect to: ")
        port = input("Port number: ")
    else:
        host = argv[0]
        port = int(argv[1])

    #create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the mail server on port 25
    s.connect((host, port))

    # initiate handshake
    try:
        print('\nConnection initiated:\n  %s\nType SMTP headers below, each on a new line:' % s.recv(1024))
        pass
    except socket.error as e:
        print('Error: %s' % e)
        raise

    # start message
    line = ''
    msg = ''

    to_email = input("Email to send to: ")
    to_line = bytes(("%s\n") % to_email)
    s.send(to_line)
    print("\n%s" % s.recv(1024))

    from_email input("Email to send from: ")
    from_line = bytes(("%s\n") % from_email)
    s.send(from_line)
    print("\n%s" % s.recv(1024))

    # TODO: finish DATA section


    while 'QUIT' not in line:
        #print('  line here:')
        line = raw_input('  >  ')
        msg = line + '\n'

        s.send(msg.encode())
        print('  ' + str( s.recv(1024) ))

        if 'DATA' in line:
            while line != '.':
                nextLine = raw_input('  >  ') + '\n'
                s.send(nextLine)
            s.send(('\n.\n').encode())
            print('  ' + str( s.recv(1024) ))

    print('Closing connection...')

    # signal our intent to close the socket and then close it
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    # pass arguments if any exist, otherwise send some defaults (not complete)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main( ['bumail.butler.edu', 25] )
