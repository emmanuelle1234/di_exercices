# EXERCISE 1
def display_message():
    print('Hello everyone, I am learning a lot of things in that course.')


display_message()


# EXERCISE 2
def favorite_book(title):
    print(f'One of my favorite books is {title}')


favorite_book('\"This is not a title\"')


# EXERCISE 3
def describe_city(city, country="Israel"):
    print(f'{city} is in {country}')


describe_city('Jerusalem')

# EXERCISE 4
import random


def guess(number):
    if 100 > number < 1:
        print('Number invalid')
    else:
        computer_number = random.randint(1, 100)
        print('congratulations') if computer_number == number else print(
            f'You failed as the number was {computer_number} whereas you input {number}')


guess(32)


# EXERCISE 5

def make_shirt(size='L', text='I love Python'):
    print(f'The size of the shirt is {size} and the message on the shirt is \"{text}\"')


make_shirt('XXXL', 'I hate messages on shirts')

make_shirt('L')

make_shirt('M')

make_shirt('S', "Why")

make_shirt(text='This is a bad practice', size='XS')



# EXERCISE 6
list = ['magician1', 'magician2', 'magician3', 'magician4']


def show_magicians(list):
    names = f'{list[0]}, {list[1]}, {list[2]}, {list[3]}'
    print(names)
    return names

show_magicians(list)


def make_great(list):
    for i in range(len(list)):
        list[i] = f'the Great {list[i]}'
    return list


make_great(list)
show_magicians(list)
