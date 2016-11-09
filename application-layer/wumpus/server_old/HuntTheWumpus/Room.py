class Room(object):

    def __init__(self, num, adjacent, description):
        super(Room, self).__init__()
        
        self.num = num                  # integer
        self.adjacent = adjacent        # [integer, integer, integer]
        self.description = description  # string

    def __str__(self):
        return 'Room: {}\n  Adjacent rooms: {}, {}, {}\n  Description:{}'.format(self.num, self.adjacent[0], self.adjacent[1], self.adjacent[2], self.description)
