
def add_item(collection, text):
    while True:
        data = input(f'{text}: ').lower()
        if data == '':
            print(f'Please enter {text}.\n')
        elif data in collection:
            print('Use a little more variety.')
        else:
            collection.append(data)
            break

        # Make sure inputted data is not repeated and exists, then add to list


def report_madlib(collection):
    print('\n\nMadLib Prompt: Our New Cat.\n')
    print(
        f'We love our new cat {collection[0].title()}. They are {collection[1]} with {collection[2]} spots'
        f' and is incredibly {collection[3]}. \nWhen we saw {collection[0].title()} at the shelter, '
        f'we wanted them so bad we {collection[4]}. \nHowever, when we returned home {collection[0].title()} instantly'
        f' knocked over a{collection[5]} and then wouldn\'t stop meowing until we held them in our arms and '
        f'told them they were {collection[6]}. \nAll in all, things worked out though. {collection[0].title()} '
        f'has been fairly'
        f' active outside, even meeting a{collection[7]}. {collection[0].title()} is very {collection[8]} at'
        f' night and loves {collection[9]}.\n\n'
    )
# Give prompt using list of collected words


def vowel_check(collection):
    last_entry = collection[-1]
    if last_entry[0] in 'aeiou':
        new_word = 'n '
        new_word += collection[-1]
    else:
        new_word = ' '
        new_word += collection[-1]
    collection[-1] = new_word

    # Some words require additional care if they start with a vowel.
    # Add n' ' before a word to accommodate grammar


def execute_madlib_two():
    collection = []

    add_item(collection, 'A name')
    add_item(collection, 'A color')
    add_item(collection, 'Another color')
    add_item(collection, 'An adjective')
    add_item(collection, 'A past tense verb')
    add_item(collection, 'A household object')
    # vowel check, if starts with vowel, add 'n-' to it
    vowel_check(collection)
    add_item(collection, 'An adjective')
    add_item(collection, 'An animal')
    # vowel check
    vowel_check(collection)
    add_item(collection, 'An adjective')
    add_item(collection, 'A plural noun')

    report_madlib(collection)


def madlib_two():
    while True:
        gate = input("If you would like to exit the program, type 'q'. Otherwise, type 'ok' for the upcoming prompt. ")
        if gate.strip().lower() == 'q':
            quit()
        elif gate.strip().lower() == 'ok':
            execute_madlib_two()
            break
        else:
            print('Try again.\n')

# Give user chance to exit by typing q or to proceed by typing ok
