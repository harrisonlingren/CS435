
class Person(object):
    """ Person is the base class for all kinds of people
    """

    # __init__
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def getName(self):
        return self.firstname + ' ' + self.lastname

