from .Room import Room
class Cave(object):

    def __init__(self, filepath):
        super(Cave, self).__init__()

        room_nums = []
        adj_rooms = []
        descriptions = []

        self.rooms = []

        try:
            with open(filepath) as f:
                lines = []
                for line in f:
                    lines.append(line)

                self.num_rooms = int(lines[0])

                for line in lines[1::2]:
                    numbers = line.split(' ')
                    room_nums.append(int(numbers[0]))
                    adj_rooms.append([ int(numbers[1]), int(numbers[2]), int(numbers[3])])

                for line in lines[2::2]:
                    descriptions.append(line)

                for i in range(self.num_rooms):
                    next_room = Room(i, adj_rooms[i], descriptions[i])
                    self.rooms.append(next_room)
        except IOError:
            print("Cannot open file", arg)

    def __str__(self):
        outp = 'Cave with {} rooms:'.format(self.num_rooms)
        for i in range(self.num_rooms):
            outp += '\n  {}'.format(self.rooms[i])

        return outp
