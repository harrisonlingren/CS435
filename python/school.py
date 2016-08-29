import sys
from Student import Student

def main(argv):
    dl = Student("David", "Lightman", "Senior")
    jm = Student("Jennifer", "Mack", "Senior")

    # more on lists, dictionaries, etc can be found at:
    # https://docs.python.org/2/tutorial/datastructures.html

    # list of items
    juniors = []
    seniors = [ dl, jm ]
    for senior in seniors:
    	print(senior)

    # dictionaries are Key-value pairs
    classes = { 'seniors': seniors, 'juniors': juniors }
    
    # you can easily iterate over keys
    print("\nClasses:")
    for c in classes:
    	print("   %s" % (c))

    # or keys and values
    print("\nStudents per class year:")
    for c,students in classes.items():
    	print("  %s: %d" % (c, len(students)))

if __name__ == "__main__":
    # pass arguments if any exist, otherwise send some defaults (not complete)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main( [] )

