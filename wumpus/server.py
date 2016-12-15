import select, socket, sys
from labyrinth import *
from mobs import *
from player import *
import random

playerName = ""

greeting = "\n                    _     _   _            __    __                                 \n  /\  /\_   _ _ __ | |_  | |_| |__   ___  / / /\ \ \_   _ _ __ ___  _ __  _   _ ___ \n / /_/ / | | | '_ \| __| | __| '_ \ / _ \ \ \/  \/ / | | | '_ ` _ \| '_ \| | | / __|\n/ __  /| |_| | | | | |_  | |_| | | |  __/  \  /\  /| |_| | | | | | | |_) | |_| \__ \ \n\/ /_/  \__,_|_| |_|\__|  \__|_| |_|\___|   \/  \/  \__,_|_| |_| |_| .__/ \__,_|___/\n                                                                   |_|              \n"
print(greeting)

l = labyrinth("cave")
l.load("cave.json")
l.print()

adj_messages = {
    "wumpus" : "You smell some nasty Wumpus!",
    "spiders" : "You hear a faint clicking noise.",
    "pits" : "You smell a dank odor.",
    "bats" : "You hear squeaks around the corner..."
}

room_messages = {
    "wumpus" : "You enter the Wumpus' cave, and he eats you!\nGAME OVER",
    "spiders" : "Spiders overcome you and the room goes dark!\nGAME OVER",
    "pits" : "You fall into an endless pit!\nGAME OVER",
    "bats" : "You are carried away by a swarm of bats to a new room!\n"
}

locations = []
for i in range(2,20):
    locations.append(i)
random.shuffle(locations)

w = wumpus(location=locations[0])
s1 = wumpus(location=locations[1])
s2 = wumpus(location=locations[2])
b1 = wumpus(location=locations[3])
b2 = wumpus(location=locations[4])
p1 = wumpus(location=locations[5])
p2 = pit(location=locations[6])

# l.rooms

print("There's a wumpus in room: {}".format(w.location))
print("There's spiders in rooms: {}, {}".format(s1.location, s2.location))
print("There's bats in rooms: {}, {}".format(b1.location, b2.location))
print("There's pits in rooms: {}, {}".format(p1.location, p2.location))


this_player = Player()

def get_response(req):
    commands = req.split(" ")
    print(commands)

    loc = this_player.location
    adj = l.rooms[loc].getAdj()
    room_message = ""

    # if join, init player obj with username
    if "JOIN" in commands[0]:
        playerName = commands[1]
        this_player.name = playerName
        this_player.location = 1

        print("Player: {} joined the game!".format(this_player.name))
        res = "202 Accepted"

    # if move, move player to new room
    elif "MOVE" in commands[0]:
        move_room = int(commands[1])
        if move_room in adj:
            results = handle_move(move_room)

            this_player.move(results[0])
            room_message = results[1]

            print("Moving {} to location: {}".format(this_player.name, move_room))
            loc = this_player.location
            adj = l.rooms[loc].getAdj()
            res = "301 Moved permanently"

        else:
            print("Can't move to room {} from room {}".format(move_room, loc))
            res = "400 Bad request"

    # if shoot, check if room is adjacent, and shoot into it if so
    elif "SHOOT" in commands[0]:
        arrow_count = this_player.arrows
        shoot_room = int(commands[1])
        if shoot_room in adj:
            print("Shooting in room: {}".format(shoot_room))
            results = handle_shoot(shoot_room)
            this_player.shoot()
            if results:
                room_message = "You killed the Wumpus! Congratulations!\nGAME OVER"
            else:
                room_message = "Your arrow shoots down the corridor and is lost..."
                if arrow_count < 1:
                    room_message = "You are out of arrows!\nGAME OVER"
            res = "200 Ok"
        else:
            room_message = "Can't shoot into room {} from room {}".format(shoot_room, loc)
            res = "400 Bad request"
    else:
        res = "400 Bad request"

    res += ("\n{}\n{} {} {} {}\n{}".format(loc, len(l.rooms[loc].adjacent), adj[0], adj[1], adj[2], room_message))
    if 'GAME OVER' in room_message:
        res += "\n  Quitting game..."
        this_player.move(1)
        arrow_count = 3

    return res.encode('UTF-8')


def handle_move(loc):
    msg = "You are in room {}\n".format(loc)

    if loc == w.location:
        msg += room_messages["wumpus"]
    elif (loc == s1.location or loc == s2.location):
        msg += room_messages["spiders"]
    elif (loc == p1.location or loc == p2.location):
        msg += room_messages["pits"]
    elif (loc == b1.location or loc == b2.location):
        msg += room_messages["bats"]
        new_loc = random.randint(1,20)
        handle_move(new_loc)

    if 'GAME OVER' not in msg:
        adj = l.rooms[loc].adjacent
        if w.location in adj:
            msg += "\n" + adj_messages['wumpus']
        if (s1.location in adj or s2.location in adj):
            msg += "\n" + adj_messages['spiders']
        if (p1.location in adj or p2.location in adj):
            msg += "\n" + adj_messages['pits']
        if (b1.location in adj or b2.location in adj):
            msg += "\n" + adj_messages['bats']

    return [loc, msg]


def handle_shoot(loc):
    if loc == w.location:
        return True
    else:
        return False


def main(argv):
    port = int(argv[0])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", port))
    s.listen(1)
    print("Listening on port {} for connections...\n".format(port))

    # Main loop
    while(True):
        connection, address = s.accept()
        message = connection.recv(1024).decode("UTF-8")

        # decode the message and send response
        resp = get_response(message)
        connection.send(resp)
        connection.close()

    # Cleanup
    s.shutdown(socket.SHUT_RDWR)
    s.close()


if __name__ == "__main__":
    # Check if port is specified
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        # If not, run on port 43500
        main([43500])
