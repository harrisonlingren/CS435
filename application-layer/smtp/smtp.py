#!/usr/bin/env python
import socket, sys

def main():
    # port and host
    if len(sys.argv) <= 1:
        host = input("Hostname to connect to: ")
        port = int(input("Port number: "))
    else:
        host = sys.argv[0]
        port = int(sys.argv[1])

    # connect to given host and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # connect
    try:
        print('\nConnection initiated:\n  %s\n' % s.recv(1024).decode('UTF-8'))
        pass
    except socket.error as e:
        print('Error: %s' % e)
        raise


    # send handshake
    domain_line = "HELO %s\n" % input("Domain to send from: ")
    s.send(domain_line.encode())

    from_email = input("Email to send from:  ")
    from_line = ("MAIL from: %s\n") % from_email
    to_email = input("Email to send to:    ")
    to_line = ("RCPT to: %s\n") % to_email

    s.send(from_line.encode())
    s.send(to_line.encode())


    # start message data
    print("Message data:")
    subject_line = ("Subject: %s\n" % input("  Subject: "))

    print("  Body:")
    message = []
    go = True
    while go:
        message_line = input("    > ")
        message.append(message_line)
        if message_line == "":
            message_line = input("    > ")
            if message_line == "":
                go = False
                message.pop()
            else:
                message.append(message_line)

    from_line2 = ("From: %s\n" % from_email)
    to_line2 = ("To: %s\n" % to_email)


    # send DATA initializer, construct data from user input
    print("Starting data transfer...")
    s.send(("DATA\n").encode())

    # construct final list of commands
    msg_headers = ""
    msg_data = ""

    msg_headers = (subject_line + from_line2 + to_line2)
    for line in message:
        msg_data += (line + "\n")
    msg_data += ".\n"

    msg = msg_headers + msg_data

    # send all message data
    s.send((msg).encode())
    print("%s" % s.recv(1024).decode('UTF-8'))

    print('Closing connection...')

    # signal our intent to close the socket and then close it
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    main()
