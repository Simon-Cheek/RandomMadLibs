
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

# Makes sure inputted data is valid and has variety


def report_madlib(collection):
    print('\n\nMadLib Prompt: Vacation.\n')
    print(
        f'Our vacation this year was {collection[0]}, especially since we went in the month of {collection[1]}!'
        f'\nWe drove {collection[2]} hours to the coast and tried some amazing {collection[3]} at a '
        f'local restaurant.\nWe went to the beach and were about to get into the water until we saw that '
        f'the clouds were looking pretty {collection[4]}. We figured we would come back later after we '
        f'visited the hotel first and {collection[5]} for the rest of the day.\nThe next day, we went '
        f'to the beach and had a great time. A{collection[6]} washed up on shore!\nAll in all, it was '
        f'a great vacation!\n\n'
    )

# Gives madlib prompt with collected words in the list

def vowel_check(collection):
    last_entry = collection[-1]
    if last_entry[0] in 'aeiou':
        new_word = 'n '
        new_word += collection[-1]
    else:
        new_word = ' '
        new_word += collection[-1]
    collection[-1] = new_word

# Accommodate grammar for some words that start with vowels


def execute_madlib_four():
    collection = []

    add_item(collection, 'An adjective')
    add_item(collection, 'A month of the year')
    add_item(collection, 'A number')
    add_item(collection, 'A fish')
    add_item(collection, 'An adjective')
    add_item(collection, 'A past verb')
    add_item(collection, 'An object')
    # check for vowels in this entry
    vowel_check(collection)

    report_madlib(collection)


def madlib_four():
    while True:
        gate = input("If you would like to exit the program, type 'q'. Otherwise, type 'ok' for the upcoming prompt. ")
        if gate.strip().lower() == 'q':
            quit()
        elif gate.strip().lower() == 'ok':
            execute_madlib_four()
            break
        else:
            print('Try again.\n')

# Give user chance to exit by typing q or to proceed by typing ok
