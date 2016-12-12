import socket, sys

def main(args):
    print("Host: " + args[1])
    host = args[1]
    print("Port: "+ str(args[2]))
    port = int(args[2])


    while 1:
        # message to be sent
        msg = input('Input a message to send:')

        # Create socket and send message to host
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(msg.encode())

        # Print response
        resp = s.recv(1024).decode()
        print("Response: %s" % str(resp))

    # Close socket
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    # pass host, port
    if len(sys.argv) >= 3:
        main(sys.argv)
    elif len(sys.argv) == 2:
        main([sys.argv[0], sys.argv[1], 80])
    else:
        main(['', 'localhost', 80])
