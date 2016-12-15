class Player(object):
    def __init__(self, name = None):
        self.location = 1
        self.arrows = 3

        if name == None:
            self.name = 'player'
        else:
            self.name = name

    def move(self, loc):
        self.location = int(loc)

    def shoot(self):
        self.arrows -= 1

    def print(self):
        print("Player: {}, Location: {}".format(self.name, self.location))
