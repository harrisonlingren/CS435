import socket, sys

def main(argv):
    host = argv[0]
    port = int(argv[1])

    # message to be sent
    msg = input('Input a message to send:')
    print(msg.encode())

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
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main(['localhost', 8080])
