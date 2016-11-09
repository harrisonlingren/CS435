import select
import socket
import sys
from threading import Lock, Thread
from labyrinth import *
from mobs import *

# global variables can be accessed by all client-handling threads
players = {}
players_lock = Lock()

l = labyrinth("cave")
l.load("cave.json")
l.print()

w = wumpus()
print("There's a wumpus in room: {}".format(w.location))


def main():
    s = game_server(43500)
    s.start()



class client_handler(Thread):
    def __init__(self,clientsocket,address):
        Thread.__init__(self) 
        self.client = clientsocket 
        self.address = address 
        self.size = 1024 
        self.player_id = None

    def run(self): 
        running = 1 
        while running: 
            data = self.client.recv(self.size).decode('UTF-8').rstrip()
            if data:
                print("{}: {}".format(self.address,req))

                # game logic - each thread handles one player


                self.client.send(str(res).encode('utf-8')) 

            else: 
                self.client.close() 
                running = 0 


class game_server(object):

    def __init__(self, port):
        self.host = '' 
        self.port = port
        self.threads = []


    def start(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 and TCP
            print('Socket created')
            self.s.bind((self.host, self.port))
            print('Socket bind complete')
            self.s.listen(10)
            print('Socket listening for connections')
            print('Press any key to quit the server')
        except socket.error as e: 
            if self.s: 
                self.s.close() 
            print("Could not open socket: {}".format(e)) 
            sys.exit(1)            
            
        # linux
        input = [self.s, sys.stdin]

        # windows
        # input = [self.s]

        running = 1 
        while running: 
            inputready,outputready,exceptready = select.select(input,[],[]) 

            for i in inputready: 

                if i == self.s: 
                    # handle the server socket
                    (clientsocket, address) = self.s.accept() 
                    c = client_handler(clientsocket, address) 
                    c.start() 
                    self.threads.append(c) 

                elif i == sys.stdin: 
                    # handle standard input 
                    # junk = sys.stdin.readline() 
                    running = 0 

                #else:
                # handle all other sockets / not multithreaded

        # close all threads 
        self.s.close() 
        for c in self.threads: 
            c.join() 

        sys.exit()

if __name__ == "__main__":
    main()
