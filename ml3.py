
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

# Make sure inputted data has variety and also exists, then add to list of collected words


def report_madlib(collection):
    print('\n\nMadLib Prompt: My Garden.\n')
    print(
        f'This last spring I decided to start a garden. I decided to grow {collection[0]} and {collection[1]}. '
        f'\nIt took {collection[2]} days for the sprouts to pop up, and when they did I felt so {collection[3]}. '
        f'\nMy {collection[4]} would go outside every day to take a look, until one day a{collection[5]} '
        f'came and ate half of my plants!\nThankfully, the rest made it through, and in the summer I got to eat '
        f'them with {collection[6]}!\n\n'
    )
# Gives prompt with all the collected words into the madlib


def vowel_check(collection):
    last_entry = collection[-1]
    if last_entry[0] in 'aeiou':
        new_word = 'n '
        new_word += collection[-1]
    else:
        new_word = ' '
        new_word += collection[-1]
    collection[-1] = new_word

    # Check and accommodate for words that start with vowels


def execute_madlib_three():
    collection = []

    add_item(collection, 'A plant')
    add_item(collection, 'Another plant')
    add_item(collection, 'A number')
    add_item(collection, 'An emotion')
    add_item(collection, 'An animal that is a pet')
    add_item(collection, 'An animal')
    # vowel check, if starts with vowel, add 'n-' to it
    vowel_check(collection)
    add_item(collection, 'A food (plural)')

    report_madlib(collection)


def madlib_three():
    while True:
        gate = input("If you would like to exit the program, type 'q'. Otherwise, type 'ok' for the upcoming prompt. ")
        if gate.strip().lower() == 'q':
            quit()
        elif gate.strip().lower() == 'ok':
            execute_madlib_three()
            break
        else:
            print('Try again.\n')

# Give user chance to exit by typing q or to proceed by typing ok
