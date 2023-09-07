import random
from ml1 import madlib_one
from ml2 import madlib_two
from ml3 import madlib_three
from ml4 import madlib_four

# Imported madlibs from other files


def pick_madlib(queue):
    picked_madlib = random.choice(queue)

    # Randomly select an item from list and connect each item to a madlib. Remove from list after madlib

    if picked_madlib == 'one':
        queue.remove('one')
        madlib_one()
        picked_madlib = ''
    elif picked_madlib == 'two':
        queue.remove('two')
        madlib_two()
        picked_madlib = ''
    elif picked_madlib == 'three':
        queue.remove('three')
        madlib_three()
        picked_madlib = ''
    else:
        queue.remove('four')
        madlib_four()
        picked_madlib = ''


def main():
    print('\nWelcome to MadLibs! Here you will be given 4 Madlib prompts in random order.\n')
    queue = ['one', 'two', 'three', 'four']

    # Make a list of 4 items and use it to randomly select madlibs

    while True:
        if queue:
            pick_madlib(queue)
        else:
            print('\n\nCongrats! You have finished all of the mad libs!')
            break

            # Finish the program after all the madlibs are done


main()

