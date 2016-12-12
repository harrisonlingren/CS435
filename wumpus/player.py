class Player(object):
    def __init__(self, name = None):
        self.location = 1
        if name == None:
            self.name = 'player'
        else:
            self.name = name

    def move(self, loc):
        self.location = int(loc)

    def print(self):
        print("Player: {}, Location: {}".format(self.name, self.location))
