class Room(object):

    def __init__(self, num, adjacent, description):
        super(Room, self).__init__()
        self.num = num
        self.adjacent = adjacent
        self.description = description
