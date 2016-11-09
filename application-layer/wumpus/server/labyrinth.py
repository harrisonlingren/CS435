import json


class room(object):
    ''' A class for a single room in the maze '''

    def __init__(self, attrs):
        self.rid = attrs['id']
        self.adjacent = attrs['adjacent']
        self.name = attrs['name']
        self.hazard = False


class labyrinth(object):
    ''' A class for the game maze '''

    def __init__(self, name):
        self.name = name
        self.rooms = {}

    def load(self, file):
        with open(file) as f:
            rooms_dict = json.load(f)
        for r in rooms_dict['rooms']:
            #print("{}".format(r)
            rm = room(r)
            self.rooms[rm.rid] = room(r)    

    def print(self):
        for k, r in self.rooms.items():
            print("{}: {}".format(r.name, r.adjacent))
