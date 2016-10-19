import socket, sys

def strip_headers(req):
    headers = {}
    for line in req.split('\n')[1:]:
        if line == '\r':
            break
        head_line = line.partition(':')
        headers[head_line[0].lower()] = head_line[2].strip()
    return headers

def get_response(req):
    r = req.split('\n')[0]
    h = strip_headers(req)

    print('>  Request type:  {}'.format(r))

    if r != '':
        method = r.split(' ')[0]
        print(method)

    # Parse request and form response here
    # aka do_game()
    # going to make a game module with necessary stuff
    response_code = 000


    # Combine all of the above and return response object
    print(">  Response code: {}\n".format(response_code))
    return response_code

def main(argv):
    port = int(argv[0])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    print('Listening on port {} for connections...\n'.format(port))

    # Main loop
    while(True):
        connection, address = s.accept()
        message = connection.recv(1024).decode('UTF-8')

        # decode the message and send response
        resp = get_response(message)
        connection.send(resp)
        connection.close()

    # Cleanup
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    # Check if port is specified
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        # If not, run on port 8080
        main([8080])
