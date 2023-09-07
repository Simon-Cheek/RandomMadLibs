
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

            # Bug the user if they try to repeat entries, and use prompts as given in the parameters
            # Once ensured data is inputted, add to list


def report_madlib(collection):
    print('\n\nMadLib Prompt: First Day of Work.\n')
    print(
          f'It has always been my dream to work at {collection[0].title()}! I have always loved their '
          f'{collection[1]} {collection[2]}! \nWhen they offered me a job, I was so {collection[3]}, '
          f'because that means I get to {collection[4]} every single day. I also get an employee '
          f'discount for {collection[5]}! \nWhen I arrived on the first day, they told me that I was '
          f'assigned to work with {collection[6]}. All was going well until I accidentally dropped '
          f'my {collection[7]} in a bunch of {collection[8]}! \nThat\'s when they told me that I was {collection[9]}. '
          f'Unfortunately, my boss said that the company ran out of {collection[10]} so I needed to find '
          f'another job.\n\n'
    )
# Madlib prompt given using list of collected words


def execute_madlib_one():
    collection = []

# Create an empty list to use for the madlib entries. Once made, punch them into the madlib prompt.

    add_item(collection, 'A place to work')
    add_item(collection, 'An adjective')
    add_item(collection, 'A plural noun')
    add_item(collection, 'An emotion')
    add_item(collection, 'A verb')
    add_item(collection, 'A plural noun')
    add_item(collection, 'A plural noun')
    add_item(collection, 'An everyday object')
    add_item(collection, 'A plural noun')
    add_item(collection, 'An adjective')
    add_item(collection, 'A plural noun')
    report_madlib(collection)


def madlib_one():
    while True:
        gate = input("If you would like to exit the program, type 'q'. Otherwise, type 'ok' for the upcoming prompt. ")
        if gate.strip().lower() == 'q':
            quit()
        elif gate.strip().lower() == 'ok':
            execute_madlib_one()
            break
        else:
            print('Try again.\n')

        # Tell the user to either proceed with typing 'ok' or to end the program by typing 'q'









