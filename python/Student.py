from Person import Person

class Student(Person):
    """ Student is a class which inherits from Person
    """

    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.year = year

    def getYear(self):
        return self.year

    # special function to specify a string representation of the object
    def __str__(self):
        return "%s %s is a %s" % (self.firstname, self.lastname, self.year)


