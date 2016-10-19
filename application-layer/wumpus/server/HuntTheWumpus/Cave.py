class Cave(object):

    def __init__(self, num_rooms):
        super(Cave, self).__init__()
        self.num_rooms = num_rooms

        for i in range(num_rooms):
            next_room = new Room(i)
            self.rooms.add(next_room)
