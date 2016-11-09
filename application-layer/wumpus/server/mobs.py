import random

class wumpus(object):

    def __init__(self, location = None):
        if location == None:
            self.location = random.randint(0,20)
        else:
            self.location = location

