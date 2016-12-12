import random

class wumpus(object):
    def __init__(self, location = None):
        if location == None:
            self.location = random.randint(0,20)
        else:
            self.location = location

class spiders(object):
    def __init__(self, location = None):
        if location == None:
            self.location = random.randint(0,20)
        else:
            self.location = location

class bats(object):
    def __init__(self, location = None):
        if location == None:
            self.location = random.randint(0,20)
        else:
            self.location = location

class pit(object):
    def __init__(self, location = None):
        if location == None:
            self.location = random.randint(0,20)
        else:
            self.location = location
