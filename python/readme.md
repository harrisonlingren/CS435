
Python Socket examples already exist in the github repo

Running python programs:
You may invoke python programs a couple different ways on thomas.butler.edu.

1. make your script executable with chmod and make the first line of your program:
#!/usr/bin/env python
after which you can just run it, e.g. ./myscript.py

2. invoke the python interpreter with your script as an argument, e.g.:
python myscript.py

Indentation matters - usually folks indent 4 or 8 spaces at a time.  Code that is aligned is in the same class/function/block.

Classes and imports
to import your own classes from the same directory you must create an empty file named: __init__.py
Then, if you name a file Person.py, with a class named Person, you can import it by writing:
from Person import Person

Python has no switch/case controls.  Several alternative options exist, the easiest of which is using a dictionary or if/else blocks.

Lists are lists of items, e.g.
weekdays = [ ‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’ ]

Dictionaries are key-value data types, e.g.:  
d = { ‘red’: ‘apple’, ‘green’:’grape’ }

Reference:
https://docs.python.org/2/tutorial/datastructures.html

